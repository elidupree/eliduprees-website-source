  "use strict"
  /*
  var corridor_weightings = {
    g8043: 15,
    g8261: 15,
    g8571: 15,
    g8657: 1,
    g8985: 1,
  }

  var icons_by_tile_id = {};
  var info_by_tile_id = {};
  var tile_ids_with_icon = [];
  var tile_ids_without_icon = [];
  var tile_ids_with_icon_by_connections = {};

  tile_ids.forEach(function(id) {
    var icon = excavate_icon(id);
    var info = excavate_tile_info(id);
    icons_by_tile_id[id] = icon;
    info_by_tile_id[id] = info;
    var weight = info.weight*(icon && icon.weight || 1);
    var bucket = icon? tile_ids_with_icon: tile_ids_without_icon;
    for (var whatever = 0; whatever <weight;++whatever) {
      bucket.push (id);
    }
    if (icon) {
      bucket = tile_ids_with_icon_by_connections [info.id] =tile_ids_with_icon_by_connections [info.id] || [];
      for (var whatever = 0; whatever < icon.weight;++whatever) {
        bucket.push (id);
      }
    }
  });*/
  
  function get_distance_info (locations, max_distance) {
    var distance_map = {};
    var frontiers = [[]];
    locations.forEach(function(tile) {
      tile = {horizontal: tile.horizontal, vertical: tile.vertical, distance: 0};
      frontiers[0].push (tile);
      set_tile (distance_map, tile);
    });
    
    for (var next_distance = 1; next_distance <= max_distance; ++next_distance) {
      var frontier = frontiers [frontiers.length - 1];
      var next_frontier = [];
      frontiers.push (next_frontier)
      frontier.forEach(function(tile) {
        for (var direction = 0; direction <6 ;++direction) {
          var neighbor = in_direction (tile, direction);
          if (get_tile (distance_map, neighbor) === undefined) {
            neighbor.distance = next_distance;
            set_tile (distance_map, neighbor);
            next_frontier.push (neighbor);
          }
        }
      });
    }
    return {distance_map, frontiers};
  }
  
  var origin = {horizontal: 0, vertical: 0};
  
  function populate (game) {
    var info = get_distance_info (game.anchored_tiles, 3);
    var tile = create_random_tile (game, 1);
    var candidate = random_choice (info.frontiers [2]);
    var other_candidate = random_choice (info.frontiers [3]);
    
    if (logical_distance (other_candidate, origin) <logical_distance (candidate, origin)) {
      candidate = other_candidate;
    }
    tile.horizontal = candidate.horizontal; tile.vertical = candidate.vertical; tile.rotation = random_range (0, 6);
    
    place_tile (game, tile);
  }
  
  function make_arena (game, size) {
    var max_width = size + 3;
    var info = get_distance_info (game.anchored_tiles, max_width+1);
    var walker;
    for (var which = size+1; which <= max_width; ++which) {
      info.frontiers [which].forEach(function(location) {
        location.worse_neighbors = 0;
        location.better_neighbors = 0;
        for (var direction = 0; direction <6 ;++direction) {
          var neighbor = get_tile (info.distance_map, in_direction (location, direction));
          if (neighbor.distance > location.distance) {
            ++location.worse_neighbors;
          };
          if (neighbor.distance < location.distance) {
            ++location.better_neighbors;
          };
        }
        if (which == max_width && location.worse_neighbors >0 && !walker) {
          walker = location;
        }
      });
    }
    var contours_live = true;
    var previous;
    var next;
    var original_walker = walker;
    function find_next() {
      for (var direction = 0; direction <6 ;++direction) {
        var neighbor = get_tile (info.distance_map, in_direction (walker, direction));
        if (neighbor.distance == walker.distance && neighbor.worse_neighbors >0 && neighbor !== previous) {
          next = neighbor;
          break;
        };
      }
    }
    function step() {
      previous = walker;
      walker = next;
      find_next();
    }
    find_next();
    step();
    while (true) {
      walker.boundary = true;
      walker.previous = previous;
      walker.next = next;
      walker.previous_live = contours_live;
      if (walker.worse_neighbors !== 2) {
        contours_live = !contours_live;
      }
      walker.next_live = contours_live;
      if (walker === original_walker) {break;}
      step();
    }
    
    function not_escaping (tile) {
      var location = get_tile (info.distance_map, tile);
      if (!location.boundary) { return true; }
      var connections = info_by_tile_id[tile.tile_id].connections;
      for (var direction = 0; direction <6 ;++direction) {
        var index = (direction + 6 - tile.rotation) % 6;
        var destination = connections[index];
        if (typeof destination === "number") {
          var first = get_tile (info.distance_map, in_direction (tile, direction));
          var second = get_tile (info.distance_map, in_direction (tile, (destination + tile.rotation) % 6));
                    
          var live = neighbor => (
            neighbor.distance < location.distance ||
            (neighbor.distance === location.distance && (
              (neighbor === location.previous && location.previous_live === true) ||
              (neighbor === location.    next && location.    next_live === true) ||
              !neighbor.boundary)));
          if (live (first) !== live (second)) {
            return false;
          }
        }
        else {
          return false;
        }
      }
      return true;
    }
    var proposed_tiles = {};
    var locations_list = [];
    for (var which = size+1; which <= max_width; ++which) {
      info.frontiers [which].forEach(function(location) {
        var tile;
        while (!(tile && (which <max_width || not_escaping (tile)))) {
          tile = create_random_tile (game, 0, {no_locks: true});
          tile.horizontal = location.horizontal; tile.vertical = location.vertical;
        }
        locations_list.push(location);
        set_tile (proposed_tiles, tile);
      });
    }
    
    locations_list.forEach(function(location) {
      location.badness = 0;
      location.paths = {};
    });
    var found_accumulator = {};
    function path_badness (path) {return path.live ? Math.max (0, path.components.length*path.components.length - 25) : 0;}
    info.frontiers [size].forEach(function(location) {
      for (var direction = 0; direction <6 ;++direction) {
        var path = collect_path (proposed_tiles, location, direction, found_accumulator);
        path.live = true;
        if (path.components.length > 5) {
          path.components.forEach(function(component) {
            var location = get_tile (info.distance_map, component.tile)
            location.badness += path_badness (path);
            location.paths [component.from] = location.paths [component.towards] = path;
          });
        }
      }
    });
    
    var consider_live = function (component) {
      return get_tile (info.distance_map, in_direction (component.tile, component.from)).distance === size || get_tile (info.distance_map, in_direction (component.tile, component.towards)).distance === size;
    }
    var evaluate = function (location, tile) {
      var badness = 0;
      var paths = collect_paths (proposed_tiles, tile);
      paths.forEach(function(path) {
        path.live = false;
        var multiplier = 0;
        path.components.forEach(function (component) {
          if (consider_live (component)) {path.live = true;}
          if (component.tile === tile) {++multiplier; }
        });
        if (path.components.length > 5 && path.live) {
          badness += multiplier*path_badness (path);
        }
      });
      return {badness: badness, paths: paths};
    }
    
    for (var whatever = 0; whatever <locations_list.length*20;++whatever) {
      var query = random_choice (locations_list);
      //console.log (query);
      if (!query.boundary) {
        var original = get_tile (proposed_tiles, query);
        var original_badness = query.badness;
        var candidate = create_random_tile (game, 0, {no_locks: true});
        candidate.horizontal = query.horizontal; candidate.vertical = query.vertical;
        set_tile (proposed_tiles, candidate);
        var candidate_evaluation = evaluate (query, candidate);
        //console.log (original_badness, candidate_evaluation);
        if (original_badness < candidate_evaluation.badness) {
          set_tile (proposed_tiles, original);
        }
        else {
          candidate_evaluation.paths.forEach(function(path) {
            path.components.forEach(function(component) {
              var location = get_tile (info.distance_map, component.tile)
              if (location.paths [component.from]) {
                location.badness -= path_badness (location.paths [component.from]);
                //if (location.paths [component.towards] !== location.paths [component.from] && location !== query) {console.log ("what", location); return;}
              }
              location.badness += path_badness (path);
              location.paths [component.from] = location.paths [component.towards] = path;
            });
          });
          query.badness = candidate_evaluation.badness;
          //query.paths = candidate_badness.paths;
        }
      }
    }
    
    info.frontiers [size].forEach(function(location) {
      for (var direction = 0; direction <6 ;++direction) {
        collect_path (proposed_tiles, location, direction).components.forEach(function(component) {
          if (!component.tile.confirmed) {
            component.tile.confirmed = true;
            component.tile.edge = true;
            component.tile.drawn_components = {};
            place_tile (game, component.tile);
          }
          component.tile.drawn_components [(component.from + 6 - component.tile.rotation) % 6] = true;
          component.tile.drawn_components [(component.towards + 6 - component.tile.rotation) % 6] = true;
        });
      }
    });
  }
  
  var game_modes = {
    classic: {
      location_playable: function(game, location) {
        for (var direction = 0; direction <6;++direction) {
          if (get_tile (game.tiles, in_direction (location, direction))) {return true;}
        }
        return false;
      },
    },
    corridor: {
      location_playable: function(game, location) {
        for (var direction = 0; direction <6;++direction) {
          var neighbor =in_direction (location, direction);
          if ((neighbor.horizontal === -1 || neighbor.horizontal === 2) && !get_tile (game.tiles, neighbor)) {return false;}
        }
        return location.horizontal === 0 || location.horizontal === 1;
      },
      on_turn_start: function (game) {
      
      
      var place = function (location, connections, direction) {
        var tile = create_random_tile (game, 1, {force_connections: connections});
        tile.horizontal = location.horizontal; tile.vertical = location.vertical;
        var connections = info_by_tile_id [tile.tile_id].connections;
        for (tile.rotation = 0; tile.rotation <6 ;++tile.rotation) {
          if (connections [(direction + 6 - tile.rotation) % 6] === icon) {
            break;
          }
        }
        place_tile (game, tile) ;
      }
      var place_boundary = function (location, id, rotation, drawn_components) {
        var tile = create_tile (game, id, rotation);
        tile.horizontal = location.horizontal; tile.vertical = location.vertical;
        tile.drawn_components = drawn_components;
        tile.edge = true;
        place_tile (game, tile);
      }
      var info = get_distance_info (game.anchored_tiles.filter (tile => tile.horizontal === 0 || tile.horizontal === 1).concat([origin]), 4);
      info.frontiers.forEach(function(frontier) {frontier.forEach(function(location) {
        if (!get_tile (game.tiles, location)) {
          if (location.horizontal == -1) {
            place (location, (mod (location.vertical, 4) === 1)?"g9384":"g9812", 1);
          }
          if (location.horizontal == 2 &&!get_tile (game.tiles, location)) {
            place (location, (mod (location.vertical, 4) === 2)?"g9384":"g9812", 4);
          }
          if (location.horizontal === -2) {
            if (mod (location.vertical, 4) === 2) {
              place_boundary (location, "g8043", 0, {0: true, 1: true, 2: true, 3: true});
            }
            else {
              place_boundary (location, "g8571", 0, {0: true, 1: true, 2: true, 3: true});
            }
          }
          if (location.horizontal === 3) {
            if (mod (location.vertical, 4) === 1) {
              place_boundary (location, "g8043", 3, {0: true, 1: true, 2: true, 3: true});
            }
            else {
              place_boundary (location, "g8571", 3, {0: true, 1: true, 2: true, 3: true});
            }
          }
        }
      })});
      
      
      },
    },
  };
  
  // turn start functions for other game modes I tried it didn't turn out too well
  
    if (false && game.available_icons === 0) {
      game.anchored_tiles = [];
      game.tiles = {};
      
      /*var location = {};
      for (location.horizontal = -4; location.horizontal <= 4; ++location.horizontal) {
      for (location.vertical = ((location.horizontal % 2) ===0)? -6 : -3; location.vertical <= 6; location.vertical += 6) {
      if (logical_distance (location, origin) <= 4) {
        var tile = create_random_tile (game, 1);
        tile.horizontal = location.horizontal; tile.vertical = location.vertical;
        place_tile (game, tile);
      }}}*/
      
      var place = function (location, direction) {
        var tile = create_random_tile (game, 1);
        tile.horizontal = location.horizontal; tile.vertical = location.vertical;
        var connections = info_by_tile_id [tile.tile_id].connections;
        for (tile.rotation = 0; tile.rotation <6 ;++tile.rotation) {
          if (connections [(direction + 6 - tile.rotation) % 6] === dead) {
            break;
          }
        }
        place_tile (game, tile) ;
      }
      for (var direction = 0; direction <6 ;++direction) {
        var location = in_direction (in_direction (origin, direction), direction);
        place (location, (direction + 5) % 6);
        place (in_direction (location, (direction + 5) % 6), (direction + 2) % 6);
      }
      
      make_arena (game, 1) ;
    }

  
