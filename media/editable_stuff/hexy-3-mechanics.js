  "use strict"
  
  function get_link (whatever) {return whatever.getAttributeNS('http://www.w3.org/1999/xlink', 'href'); }
  function set_link (whatever, value) {return whatever.setAttributeNS('http://www.w3.org/1999/xlink', 'xlink:href', value); }
  
  function iterate_sources (element, callback) {
    callback (element);
    var link = get_link (element);
    if (link) {iterate_sources (document.getElementById (link.slice (1)), callback);}
    $(element).children().each (function() {iterate_sources (this, callback);});
  }
  
  function random_range (min, max) {
    return min + Math.floor (Math.random()*(max - min));
  }
  function random_choice (sequence) {
    return sequence [random_range (0, sequence.length)];
  }

  var tile_ids = window.hexy_tile_ids
  var blank_hex_id = "g7168"
  var long_radius = 36;
  var short_radius = long_radius*0.866;
   function tile_position (horizontal, vertical) {
    if (vertical === undefined) {vertical = horizontal.vertical; horizontal = horizontal.horizontal;}
    return {horizontal: horizontal*1.5*long_radius, vertical: vertical*short_radius}
  }
  
  // CSS rotations are clockwise, so I'm making the directions be clockwise so that I don't screw up.
  // Direction 0 is up in user space, up-right in the source (I rotate the tiles by 1/2
  // because I'm familiar with hexagonal tiles being oriented that way in Wesnoth)
  var directions = [
    {horizontal:  0, vertical: -2},
    {horizontal:  1, vertical: -1},
    {horizontal:  1, vertical:  1},
    {horizontal:  0, vertical:  2},
    {horizontal: -1, vertical:  1},
    {horizontal: -1, vertical: -1}
  ];
  
  function in_direction (location, direction) {
    var offset = directions [direction];
    return {horizontal: location.horizontal + offset.horizontal, vertical: location.vertical + offset.vertical};
  }
  
  function position_string (location) {
    return location.horizontal.toString() + "_" + location.vertical;
  }
  
  var dead= "dead";var icon= "icon";var lock= "lock";
  var connections_table = {
    [blank_hex_id]: { offset: {horizontal: 0, vertical: 1050.862}},
  
    g8043: {connections: [3, 2, 1, 0, 5, 4], offset: {horizontal: 3, vertical: 1038.862}, weight: 10, pieces: ["use7975","use8039","use8041"]},
    g8261: {connections: [2, 4, 0, 5, 1, 3], offset: {horizontal: 3, vertical: 1026.862}, weight: 15, pieces: ["use8257","use8259","use8255"]},
    g8571: {connections: [2, 3, 0, 1, 5, 4], offset: {horizontal: 3, vertical: 1014.862}, weight: 15, pieces: ["use8567","use8565","use8569"]},
    g8657: {connections: [1, 0, 3, 2, 5, 4], offset: {horizontal: 20, vertical: 1007.862}, weight: 4, pieces: ["use8655","use8653","use8651"]},
    g8985: {connections: [3, 4, 5, 0, 1, 2], offset: {horizontal: 20, vertical: 1001.862}, weight: 0, pieces: ["use8983","use8981","use8979"]},
    
    
    g9384: {connections: [5, dead, icon, 4, 3, 0], offset: {horizontal: 20, vertical: 1036.862}, weight: 8, pieces: ["use9344","use9348","use9382","use9346"]},
    g9425: {connections: [1, 0, icon, 4, 3, dead], offset: {horizontal: 20, vertical: 1036.862 - 2}, weight: 34, pieces: ["use9395","use9401","use9397","use9399"]},
    g9432: {connections: [1, 0, icon, dead, 5, 4], offset: {horizontal: 20, vertical: 1036.862 - 4}, weight: 8, pieces: ["use9409","use9413","use9411","use9407"]},
    g9631: {connections: [2, 3, 0, 1, icon, dead], offset: {horizontal: 20, vertical: 1036.862-6}, weight: 29, pieces: ["g9154","g9144","use9607","use9609"]},
    g9625: {connections: [2, 3, 0, 1, dead, icon], offset: {horizontal: 20, vertical: 1036.862-8}, weight: 29, pieces: ["g9154","g9144","use9617","use9615"]},
    g9812: {connections: [4, 2, 1, icon, 0, dead], offset: {horizontal: 20, vertical: 1036.862-10}, weight: 10, pieces: ["use9798","use9796","use9800","use9794"]},
    g9843: {connections: [2, dead, 0, icon, 5, 4], offset: {horizontal: 20, vertical: 1036.862-12}, weight: 10, pieces: ["use9806","use9810","use9808","use9804"]},
    g10007: {connections: [3, 2, 1, 0, icon, dead], offset: {horizontal: 20, vertical: 1036.862-14}, weight: 24, pieces: ["use9987","use9995","use9993","use9991"]},
    g10014: {connections: [3, 2, 1, 0, dead, icon], offset: {horizontal: 20, vertical: 1036.862-16}, weight: 24, pieces: ["use10001","use9999","use10003","use10005"]},
    g10195: {connections: [3, 4, dead, 0, 1, icon], offset: {horizontal: 20, vertical: 1036.862-18}, weight: 0},
    g10315: {connections: [2, 4, 0, dead, 1, icon], offset: {horizontal: 20, vertical: 1036.862-20}, weight: 0},
    g10325: {connections: [icon, 4, dead, 5, 1, 3], offset: {horizontal: 20, vertical: 1036.862-22}, weight: 0},
    g10573: {connections: [lock, lock, lock, 5, lock, 3], offset: {horizontal: 20, vertical: 1012.862}, weight: 1},
    g10495: {connections: [2, 3, 0, 1, lock, lock], offset: {horizontal: 20, vertical: 1010.862}, weight: 3},
  };
  document.getElementById ("use10453").style.setProperty ("--path-fill", "var(--path-fill-lock)");
  document.getElementById ("use15461").style.setProperty ("--path-fill", "var(--path-fill-lock)");
  document.getElementById ("use10515").style.setProperty ("--path-fill", "var(--path-fill-lock)");
  document.getElementById ("use10539").style.setProperty ("--path-fill", "var(--path-fill-lock)");
  document.getElementById ("path15465").style.setProperty ("--path-fill", "var(--path-fill-lock)");
  document.getElementById ("use10527").style.setProperty ("--path-fill", "var(--path-fill-3-5)");
  
  document.getElementById ("path16699-3").style.setProperty ("fill", "var(--arrow-fill)");
  
  var icons_table = {
    g9171: {grid_position: 1, icon: "hand", color: "black", side: "right", weight: 12},
    g9179: {grid_position: 2, icon: "hand", color: "white", side: "right", weight: 12},
    g9187: {grid_position: 3, icon: "hand", color: "black", side: "left", weight: 12},
    g9202: {grid_position: 4, icon: "hand", color: "white", side: "left", weight: 12},
    g9224: {grid_position: 5, icon: "foot", color: "black", side: "right", weight: 6},
    g9231: {grid_position: 6, icon: "foot", color: "white", side: "right", weight: 6},
    g9217: {grid_position: 7, icon: "foot", color: "black", side: "left", weight: 6},
    g9210: {grid_position: 8, icon: "foot", color: "white", side: "left", weight: 6},
    g9278: {grid_position: 11, icon: "crotch", color: "black", weight: 17},
    g9267: {grid_position: 12, icon: "crotch", color: "white", weight: 17},
    g9289: {grid_position: 9, icon: "torso", color: "black", weight: 23},
    g9299: {grid_position: 10, icon: "torso", color: "white", weight: 23},
    g9250: {grid_position: 13, icon: "furniture", weight: 16},
    g9238: {grid_position: 14, icon: "toybox", weight: 8},
  };
   
  Object.getOwnPropertyNames(connections_table).forEach(function(id) {
    var info = connections_table [id];
    info .id = id;
    info.offset.horizontal += 0.866;
    info.offset.vertical += 1;
    var piece_index = 0;
    if (info.connections) {info.connections.forEach(function(connection, index) {
      function do_connection (identifier) {
        if (!info.pieces) {return;}
        //console.log (info.pieces [piece_index]);
        var piece_element = document.getElementById (info.pieces [piece_index]);
        piece_element.style.setProperty ("--path-fill", "var(--path-fill-" + identifier +")");
        //piece_element.style.setProperty ("transition-delay", "1s");
        ++piece_index;
      }
      if (typeof connection == "number") {
        if (info.connections[connection] !== index) {
          console.log ("error: mismatched connections");
        }
        if (index <connection) {
          do_connection (index + "-" + connection);
        }
      }
      else if (connection == "lock") {
        do_connection ("lock");
      } else {
        do_connection (index + "-" + connection);
      }
    });}
    iterate_sources (document.getElementById (id), function(source) {
      //if (source.style.fill) {source.style.setProperty ("transition-delay", "1s"); }
      source.style.removeProperty ("filter");
    });
  });
  
  Object.getOwnPropertyNames(icons_table).forEach(function(id) {
    var info = icons_table [id];
    info .id = id;
    iterate_sources (document.getElementById (id), function(source) {
      if (info . color === "black") {
        if (source.style.fill === "rgb(0, 0, 0)") {source.style.fill = "var(--icon-fill)";}
        if (source.style.stroke === "rgb(255, 255, 255)") {source.style.stroke = "var(--icon-stroke)";}
        if (source.style.fill === "rgb(255, 255, 255)") {source.style.fill = "var(--icon-stroke)";}
      }
      if (info . color === "white") {
        if (source.style.fill === "rgb(255, 255, 255)") {source.style.fill = "var(--icon-fill)";}
        if (source.style.stroke === "rgb(0, 0, 0)") {source.style.stroke = "var(--icon-stroke)";}
        if (source.style.fill === "rgb(0, 0, 0)") {source.style.fill = "var(--icon-stroke)";}
      }
    });
  });
  
  
  function get_tile_info (element) {
    var original = (typeof element === "string") && ('#'+element) || get_link (element);
    var direct = connections_table [original.slice (1)];
    if (direct) {return direct;}
    var indirect;
    $(original).children().each (function (index) {
      if (!indirect) {
        var link = get_link (this);
        if (link) {
          indirect = connections_table [link.slice (1)];
        }
      }
    });
    return indirect;
  }
  function get_connections (element) {
    return get_tile_info (element).connections;
  }
   
  function get_icon (element) {
    var original = (typeof element === "string") && ('#'+element) || get_link (element);
    var indirect;
    $(original).children().each (function (index) {
      if (!indirect) {
        var link = get_link (this);
        if (link) {
          indirect = icons_table [link.slice (1)];
        }
      }
    });
    return indirect;
  }

  var icons_by_tile_id = {};
  var info_by_tile_id = {};

  tile_ids.forEach(function(id) {
    icons_by_tile_id[id] = get_icon(id);
    info_by_tile_id[id] = get_tile_info(id);
  });
  info_by_tile_id [blank_hex_id] = connections_table [blank_hex_id];
  
  
  
  
  function get_tile (tiles, location) {
    return tiles [position_string (location)]
  }
  function set_tile (tiles, tile) {
    tiles [position_string (tile)] = tile
  }
  function remove_tile (tiles, location) {
    delete tiles [position_string (location)]
  }

    
  function collect_path (tiles, tile, from_direction) {
    var found = {};
    var result = {components: [], icons: [], lock: false, completed: true};
    function find (tile, from_direction) {
      if (!tile) {result.completed = false; return;}
      if (!found [position_string (tile)+"_"+from_direction]) {
        found [position_string (tile)+"_"+from_direction] = true;
        var connections = info_by_tile_id[tile.tile_id].connections;
        var index = (from_direction + 6 - tile.rotation) % 6;
        var destination = connections[index];
        if (typeof destination === "number") {
          destination = (connections[index] + tile.rotation) % 6;
          found [position_string (tile)+"_"+destination] = true;
          var neighbor = get_tile (tiles, in_direction (tile, destination));
          find(neighbor, (destination + 3) % 6);
          result.components.push ({tile, from: from_direction, towards: destination});
        }
        else if (destination === "lock") {
          result.components.push ({tile, from: from_direction, towards: destination})
          result.lock = true;
          for (var direction = 0; direction <6 ;++direction) {
            if (connections [(direction + 6 - tile.rotation) % 6] == lock) {
              var neighbor = get_tile (tiles, in_direction (tile, direction));
              find(neighbor, (direction + 3) % 6);
            }
          }
        }
        else {
          result.components.push ({tile, from: from_direction, towards: destination});
          if (destination === icon) {result.icons.push (tile);}
        }
      }
    }
    find (tile, from_direction);
    find (get_tile (tiles, in_direction (tile, from_direction)), (from_direction + 3) % 6);
    return result;
  }
  
  function collect_paths (tiles, tile) {
    // TODO: no repeats
    var connections = info_by_tile_id[tile.tile_id].connections;
    var result = [];
    var done_lock = false;
    for (var direction = 0; direction <6 ;++direction) {
      var index = (direction + 6 - tile.rotation) % 6;
      var destination = connections[index];
      if (typeof destination === "number" && destination <index) { continue; }
      if (destination === lock) {
        if (done_lock) {continue;}
        done_lock = true;
      }
      result.push (collect_path (tiles, tile, direction));
    }
    return result;
  }
  

  function path_effects (path) {
    if (path.icons.length <2) {return;}
    
    var success = {text: "Okay, done"};
    function fail_option (victim, message) {
      if (victim === undefined) {
        return {text: message};
      } else {
        return {text: message+` ${victim.name} skips two turns`, action: function() {
          victim.skip_turns = (victim.skip_turns || 0) + 2;
        }};
      }
    }
    
    function tie(icons, victim) {
      if (icons.length === 2) {
        return {
          message:`tie ${describe_tile_icon(icons [0])} to ${describe_tile_icon(icons [1])}`,
          options: [success, fail_option (victim, "that's physically impossible")]
        };
      }
      else {
        var result = `tie together ${describe_tile_icon(icons [0])}`
        for (var index = 1; index <icons.length - 1;++index) {
          result += `, ${describe_tile_icon(icons [index])}`
        }
        return {
          message:result+ `, and ${describe_tile_icon(icons [icons.length - 1])}`,
          options: [success, fail_option (victim, "that's physically impossible")]
        };
      }
    }
    
    if (path.lock) {
      return tie (path.icons);
    }
    
    
    
    function strip (player, text) {
      return {
        message:`${player.name}, remove a piece of clothing${text}`,
        options: [
          success,
          fail_option (player, `${player.name} has nothing left to remove`),
        ]
      };
    }
    
    var handlers = [
      function (first, second) {
        if (first.player === second.player && first.icon.icon === "torso" && second.icon.icon === "crotch") {
          return strip(first.player,"");
        }
      },
      function (first, second) {
        if (first.player === second.player && first.icon.icon === "torso") {
          return strip(first.player," from your torso");
        }
      },
      function (first, second) {
        if (first.player === second.player && first.icon.icon === "crotch") {
          return strip(first.player," from your legs");
        }
      },
      function (first, second) {
        if (first.player && second.icon.icon === "furniture") {
          return tie ([first, second], first.player);
        }
      },
      function (first, second) {
        if (first.player && second.icon.icon === "toybox") {
          return {
            message:`${first.player.name}, choose a toy to be used on you`
          };
        }
      },
      function (first, second) {
        if (first.player === second.player && first.icon.icon === "hand" && second.icon.icon === "foot") {
          return tie ([first, second], first.player);
        }
      },
      function (first, second) {
        if (first.player === second.player && first.icon.icon === "foot" && second.icon.icon === "foot") {
          return {
            message:`tie ${first.player.name}'s feet together`
          };
        }
      },
      function (first, second) {
        if (first.player === second.player && first.icon.icon === "hand" && second.icon.icon === "hand") {
          if (first.player.hands_tied === undefined) {
            return {
              message:`tie ${first.player.name}'s hands together in front of them`,
              options: [
                {text: "Drat", action: function() {first.player.hands_tied = "front";}},
                fail_option (first.player, "")
              ]
            };
          }
          if (first.player.hands_tied === "front") {
            return {
              message:`re-tie ${first.player.name}'s hands together behind them`
            };
          }
          if (first.player.hands_tied === "back") {
            return {
              message:`${first.player.name}'s hands are already tied behind their back`,
              options: [
                fail_option (first.player, "Drat")
              ]
            };
          }
        }
      },
      function (first, second) {
        if (first.player && second.player && first.icon.icon !== second.icon.icon && (first.icon.icon === "hand" || first.icon.icon === "foot") && (second.icon.icon === "foot" || second.icon.icon === "torso" || second.icon.icon === "crotch")) {
          return {
            message: `from now on, ${first.player.name} can stimulate ${describe_tile_icon (second)} with their ${describe_tile_icon (first, true)}`
            
          };
        }
      },

    ];
    
    for (var index = 0; index <handlers.length;++index) {
      var handler = handlers [index];
      var result = handler(path.icons [0],path.icons [1]);
      if (result !== undefined) {return result;}
      result = handler(path.icons [1],path.icons [0]);
      if (result !== undefined) {return result;}
    };
  }
  
  function path_legality (path, placed_tile) {
    var forbidden = false;
    if (path.icons.length >1) {path.icons.forEach(function(tile) {
      if (tile === placed_tile) {forbidden = true;}
    });}
    if (forbidden) {return "forbidden";}
    
    if (!path.completed) {return "acceptable";}
    
    if (path.icons.length === 0) {return "acceptable";}
    if (path.icons.length === 1) {return "waste";}
    if (path_effects (path) === undefined) {return "waste";}
    
    return "success";
  }

  
  function placement_results (tile, paths) {
    var paths_by_legality={};
    paths.forEach(function(path) {
      var legality = path_legality (path, tile);
      paths_by_legality[legality] = paths_by_legality[legality] || [];
      paths_by_legality[legality].push(path);
    });
    if (paths_by_legality.forbidden) {
      return {
        legality: "forbidden",
        relevant_paths: paths_by_legality.forbidden
      };
    }
    if (paths_by_legality.success) {
      return {
        legality: "success",
        relevant_paths: paths_by_legality.success
      };
    }
    if (paths_by_legality.waste) {
      return {
        legality: "waste",
        relevant_paths: paths_by_legality.waste
      };
    }
    return {
      legality: "acceptable",
      relevant_paths: paths_by_legality.acceptable
    };
  }
  
  
  function create_random_tile (game_state) {
    var choose_icon = Math.random() < 0.8;
    var id;
    var player;
    while (true) {
      id = random_choice (tile_ids);
      var icon = icons_by_tile_id[id];
      var info = info_by_tile_id[id];
      
      //console.log(info.weight*(icon && icon.weight || 1));
      if ((!!icon === !!choose_icon) && (Math.random()*10000 < info.weight*(icon && icon.weight || 1))) {
        //hack: preserve the ratio of player-specific icons to non-player-specific icons, regardless of the number of players
        if (icon && icon.color && !player) {
          player = random_choice (game_state.players);
        }
        if (!(player && icon.color !== player.based_on)) {
          break;
        }
      }
    }
    var result = {tile_id: id, rotation: random_range (0, 6)};
    result.graphical_rotation = result.rotation;
    result.player = player;
    result.key = game_state.next_tile_key++;
    result.icon = icons_by_tile_id [result.tile_id];
    return result;
  }
  
  function new_tile(game_state) {
    var tile = create_random_tile(game_state);
    game_state.tiles.push (tile);
  }
  
  function begin_turn (state) {
    var current_player_index = (state.current_player.index + 1) % state.players.length;
    var old_player = state.current_player;
    var player = state.current_player = state.players [current_player_index];
    
    if (old_player.skip_turns >0) {
      old_player.skip_turns--;
    }
    if (player.skip_turns >0) {
      state.current_prompt = {
        kind: "message",
        message: "still_skipping",
      };
      return;
    }
    
    var tile = create_random_tile(state);
    
    /*if (tile.player === player && (tile.icon.icon === "torso" || tile.icon.icon === "crotch")) {
      state.current_prompt = {
        kind: "message",
        message: "tile_based_skipping",
        tile: tile,
      };
      return;
    }*/
    
    state.floating_tile = tile;
    state.current_prompt = {kind:"place_tile", tile: tile};
  }
  
  var messages = {
    still_skipping: function (state) {
      
    },
    tile_based_skipping: function (state) {
      
    },
  }
  
  
  function new_game (players) {
    var game ={
      anchored_tiles: [],
      tiles: {},
      players: _.cloneDeep(players),
    };
    game.players.forEach(function(player, index) {
      player.index = index;
      player.skip_turns = 0;
    });
    var tile;
    while (!(tile && tile.player)) {
      tile = create_random_tile (game);
    }
    game.current_player = game.players [
      (game.players.length + tile.player.index - 1) % game.players.length
    ];
    tile.horizontal = 0;
    tile.vertical = 0;
    game.anchored_tiles.push (tile);
    set_tile (game.tiles, tile);
    begin_turn (game);
    return game;
  }
  
  function place_floating_tile(game, location) {
      game.floating_tile.horizontal = location.horizontal;
      game.floating_tile.vertical = location.vertical;
      game.floating_tile.rotation = location.rotation;
      game.anchored_tiles.push (game.floating_tile);
      set_tile (game.tiles, game.floating_tile) ;
      delete game.floating_tile;
        
      game.current_player.played_yet = true;
      begin_turn (game);
    }
    /*    
    
    dismiss_message() {
      var that = this;
      return function () {that.setState (function (state, props) {
        state = _.cloneDeep (state);
        
        begin_turn (state);
        
        return state;
      });}
    }
*/

var global_game = new_game ([
      {based_on: "white", name: "white", fill: "#ffffff", stroke: "#000000"},
      {based_on: "black", name: "black", fill: "#000000", stroke: "#ffffff"},
      /*{based_on: "white", name: "pink", fill: "#ffaaff", stroke: "#ff00ff"},
      {based_on: "white", name: "green", fill: "#99ff99", stroke: "#008800"},
      {based_on: "black", name: "blue", fill: "#0000ff", stroke: "#ffffff"},
      {based_on: "black", name: "purple", fill: "#5500aa", stroke: "#ffffff"},*/
    ]);
