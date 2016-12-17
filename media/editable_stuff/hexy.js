$(function(){
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
  
  var game_height;
  var game_width;
  function update_dimensions() {
    game_height = $(window).height();
    game_width = $(window).width();
    //$("svg").width (game_width).height(game_height);
  }
  update_dimensions();
  var board = document.createElementNS("http://www.w3.org/2000/svg", 'g');
  board.setAttribute ("id", "board");
  $("svg").attr("id", "main_display").append (board);
  $("#board").css({["transform-origin"]: "0px 0px 0px"
    //, "transition-delay": "1.5s"
  });
  
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
  
  function fill_component (tile, from, towards, fill) {
    from = (from + 6 - tile.rotation) % 6;
    if (typeof towards === "number") {
      towards = (towards + 6 - tile.rotation) % 6 ;
      if (from >towards) {[from, towards] = [towards, from];}
      tile.element.style.setProperty ("--path-fill-" + from + "-" + towards, fill);
    }
    else if (towards === lock) {
      tile.element.style.setProperty ("--path-fill-lock", fill);
    } else {
      tile.element.style.setProperty ("--path-fill-" + from + "-" + towards, fill);
    }
  }
    
  function collect_path (tile, from_direction) {
    var found = {};
    var result = {components: [], icons: [], lock: false, completed: true};
    function find (tile, from_direction) {
      if (!tile || tile.border) {result.completed = false; return;}
      if (!found [position_string (tile)+"_"+from_direction]) {
        found [position_string (tile)+"_"+from_direction] = true;
        var connections = get_connections (tile.element);
        var index = (from_direction + 6 - tile.rotation) % 6;
        var destination = connections[index];
        if (typeof destination === "number") {
          destination = (connections[index] + tile.rotation) % 6;
          found [position_string (tile)+"_"+destination] = true;
          var neighbor = get_tile (in_direction (tile, destination));
          find(neighbor, (destination + 3) % 6);
          result.components.push ({tile, from: from_direction, towards: destination});
        }
        else if (destination === "lock") {
          result.components.push ({tile, from: from_direction, towards: destination})
          result.lock = true;
          for (var direction = 0; direction <6 ;++direction) {
            if (connections [(direction + 6 - tile.rotation) % 6] == lock) {
              var neighbor = get_tile (in_direction (tile, direction));
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
    find (get_tile (in_direction (tile, from_direction)), (from_direction + 3) % 6);
    return result;
  }
  
  function collect_paths (tile) {
    // TODO: no repeats
    var connections = get_connections (tile.element);
    var result = [];
    for (var direction = 0; direction <6 ;++direction) {
      result.push (collect_path (tile, direction));
    }
    return result;
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
  var legality_fill = {
    acceptable: "#0000ff",
    forbidden: "#ff0000",
    waste: "#990000",
    success: "#ffff00"
  };
  
  function describe_tile_icon (tile, omit_player) {
    var icon = get_icon (tile.element);
    if (icon.icon === "furniture") {
      return "a piece of furniture";
    }
    if (icon.icon === "toybox") {
      return "a toy";
    }
    return (!omit_player && `${tile.player.name}'s` || "") + (icon.side && " "+ icon.side || "") +  icon.icon;
  }
  function path_effects (path) {
    function tie(icons) {
      if (icons.length === 2) {
        return {
          message:`tie ${describe_tile_icon(icons [0])} to ${describe_tile_icon(icons [1])}`
        };
      }
      else {
        var result = `tie together ${describe_tile_icon(icons [0])}`
        for (var index = 1; index <icons.length - 1;++index) {
          result += `, ${describe_tile_icon(icons [index])}`
        }
        return {
          message:result+ `, and ${describe_tile_icon(icons [icons.length - 1])}`
        };
      }
    }
    
    if (path.lock) {
      return tie (path.icons);
    }
    
    function strip (player, text) {
      return {
        message:`${player.name}, remove a piece of clothing${text}`,
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
          return tie ([first, second]);
        }
      },
      function (first, second) {
        if (first.player && second.icon.icon === "toybox") {
          return {
            message:`${first.player.name}, choose a toy to be used on you.`
          };
        }
      },
      function (first, second) {
        if (first.player === second.player && first.icon.icon === "hand" && second.icon.icon === "foot") {
          return tie ([first, second]);
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
  
  function iterate_tiles (callback) {
    var found = {};
    function find (tile) {
      if (!found [position_string (tile)]) {
        found [position_string (tile)] = true;
        callback (tile);
        for (var direction = 0; direction <6 ;++direction) {
          var neighbor = get_tile (in_direction (tile, direction));
          if (neighbor) {find (neighbor);}
        }
      }
    }
    find (get_tile ({horizontal: 0, vertical: 0}));
    callback (floating_tile);
  }
  
  function refresh_paths() {
    iterate_tiles (function(tile) {if (!tile.border) {
      function do_connection (identifier) {
        tile.element.style.setProperty ("--path-fill-" + identifier, "#808080");
      }
      get_tile_info (tile.element).connections.forEach(function(connection, index) {
        if (typeof connection == "number") {
          if (index <connection) {
            do_connection (index + "-" + connection);
          }
        }
        else if (connection == "lock") {
          do_connection ("lock");
        } else {
          do_connection (index + "-" + connection);
        }
      });
    }});
    if (floating_tile.horizontal !== undefined) {collect_paths (floating_tile).forEach(function(path) {
      var fill = legality_fill [path_legality (path, floating_tile)];
      path.components.forEach(function(component) {
        fill_component (component.tile, component.from, component.towards, fill);
      });
    });}
  }
  
  /*function draw_path (horizontal, vertical, from_direction, towards) {
    follow_path({horizontal, vertical}, from_direction, function(tile, from, towards) {
      //$(tile.element).css({opacity: 0.5});
      tile.element.style.setProperty ("--path-fill", "red");
      fill_component (tile, from, towards, "blue");
    });
  }*/
  
  function neutral_transform (clone) {
    var original = $(get_link (clone))[0];
    
    //does not take into account clipping paths
    var inaccurate_offset = original.getBBox();
    
    var offset = get_tile_info (clone).offset;
    var icon = get_icon (clone);
    var offset_horizontal = offset.horizontal + (icon && icon.grid_position*1.732 || 0);
    var offset_vertical = 1052.36218-offset.vertical;
    
    //console.log (offset);
    var transform_origin = ""+(offset_horizontal)+"px "+(offset_vertical)+"px 0px"//"50% 50% 0";//""+ (offset.x+0.5*offset.width)+"px "+ (offset.y+0.5*offset.height)+"px 0px";
    //console.log (transform_origin);
    var transform = (
      //"translate("+ (-(offset.x+0.5*offset.width))+"px, "+ (-(offset.y+0.5*offset.height))+"px)"
      "translate("+ (-(offset_horizontal))+"px, "+ (-(offset_vertical))+"px)"
    );
    //console.log (transform);
    return {"transform-origin": transform_origin, transform: transform}
  }
  function calculate_transform (clone, horizontal, vertical, rotation) {
    var result = neutral_transform (clone);
    
    var position = tile_position (horizontal, vertical);
    result.transform = result.transform + (
      " translate(" + position.horizontal + "px," + position.vertical + "px) rotate("+(-0.0833 + rotation/6)+"turn) scale(" + long_radius+ "," + long_radius+ ")"
    );
    //console.log (transform);
    return result
  }
  function update_position (tile) {
    if (tile.horizontal !== undefined) {
      $("#board").append(tile.element);
      $(tile.element).css(calculate_transform (tile.element, tile.horizontal, tile.vertical, tile.graphical_rotation));
    }
    else {
      var result = neutral_transform (tile.element);
      
      var radius = long_radius;
      result.transform = result.transform + (
        " translate(" + (radius) + "px," + (radius/**short_radius/long_radius*/) + "px) rotate("+(-0.0833 + tile.graphical_rotation /6)+"turn) scale(" + radius+ "," + radius+ ")"
      );
      //console.log (result.transform);
      $(tile.element).css(result);
    }
  }
  
  var players = [
    {based_on: "white", name: "white", fill: "#ffffff", stroke: "#000000"},
    {based_on: "black", name: "black", fill: "#000000", stroke: "#ffffff"},
    /*{based_on: "white", name: "pink", fill: "#ffaaff", stroke: "#ff00ff"},
    {based_on: "white", name: "green", fill: "#99ff99", stroke: "#008800"},
    {based_on: "black", name: "blue", fill: "#0000ff", stroke: "#ffffff"},
    {based_on: "black", name: "purple", fill: "#5500aa", stroke: "#ffffff"},*/
  ];
  
  var tiles = {};
  var floating_tile;
  
  function create_clone (id) {
    var whatever =document.createElementNS("http://www.w3.org/2000/svg", 'use');
    set_link (whatever, '#'+id);
    //console.log (get_link (whatever));
    whatever.setAttribute("x", 0);
    whatever.setAttribute("y", 0);
    return whatever;
  }
  function create_tile (id, rotation) {
    var element = create_clone (id);
    var tile = {rotation, graphical_rotation: rotation, element};
    var icon = get_icon (element);
    tile.icon = icon;
    $(element).addClass("tile").click(function() {
      if (tile === floating_tile) {
        rotate_right();
        /*create_borders_around (tile);
        floating_tile = create_random_tile ();
        refresh_paths();*/
      } else {
        //draw_path(tile.horizontal, tile.vertical, 0);
      }
    });
    return tile;
  }
  function create_random_tile () {
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
          player = random_choice (players);
        }
        if (!(player && icon.color !== player.based_on)) {
          break;
        }
      }
    }
    var result = create_tile(id, random_range (0, 6));
    result.player = player;
    if (player) {
      result.element.style.setProperty ("--icon-fill", player.fill);
      result.element.style.setProperty ("--icon-stroke", player.stroke);
    }
    return result;
  }
  function create_border_tile (location) {
    var element = create_clone (blank_hex_id);
    $(element).addClass("tile border").css(calculate_transform (element, location.horizontal, location.vertical, 0)).click(function() {
      if (skip_turn) {return;}
      set_tile (location, floating_tile);
      refresh_paths();
    });
    set_tile (location, {element: element, rotation: 0, border: true});
  }
  function create_borders_around (location) {
    for (var direction = 0; direction <6 ;++direction) {
      var neighbor = in_direction (location, direction);
      if (!get_tile (neighbor)) {create_border_tile (neighbor);}
    }
  }
  function remove_tile (location) {
    var previous = get_tile (location);
    if (previous) {
      delete previous.horizontal; delete previous.vertical;
      $(previous.element).detach();
      delete tiles [position_string (location)];
    }
  }
  function position_string (location) {
    return location.horizontal.toString() + "_" + location.vertical;
  }
  function set_tile (location, tile) {
    remove_tile (location);
    tiles [position_string (location)] = tile
    if (tile.horizontal !== undefined) {
      delete tiles [position_string (tile)]
      create_border_tile ({horizontal: tile.horizontal, vertical: tile.vertical});
    }
    tile.horizontal = location.horizontal; tile.vertical = location.vertical;
    update_position (tile) ;
    
    if (!(tile.border || tile === floating_tile)) {
      create_borders_around (location);
    }
  }
  function get_tile (location) {
    return tiles [position_string (location)]
  }
  
  function hack (horizontal, vertical) {
    var tile = create_random_tile ();
    //$(whatever).css(calculate_transform (whatever, horizontal, vertical+0.00001, rotation));
   
    $(tile.element).css(calculate_transform (tile.element, horizontal*1.3, vertical*1.3-2, tile.rotation+0.5));
    //whatever.css({transform:"scale(20, 20)"});
    
    setTimeout (function() {
      set_tile ({horizontal, vertical}, tile);
      //$(whatever).css(calculate_transform (whatever, horizontal, vertical, rotation));
    }, 10);
  }
  /*
  for (var index = -5; index <=5;++index) {
    for (var terrible = index-6; terrible <=index+4;terrible+=2) {
      hack (index, terrible);
    }
  }*/
  
  hack (0,0);
  
  
  floating_tile = create_random_tile ();
  setTimeout (function() {
    begin_turn();
  }, 15);
  
  function draw() {
    requestAnimationFrame (draw);
    update_dimensions();
    var min_horizontal = 0;
    var max_horizontal = 0;
    var min_vertical = 0;
    var max_vertical = 0;
    iterate_tiles (function (tile) {
      if (tile.horizontal === undefined) {return;}
      var position = tile_position (tile);
      min_horizontal = Math.min (min_horizontal, position.horizontal - long_radius);
      max_horizontal = Math.max(max_horizontal, position.horizontal + long_radius);
      min_vertical = Math.min (min_vertical , position.vertical - short_radius);
      max_vertical = Math.max(max_vertical , position.vertical + short_radius);
    });
    //var scale = Math.min (game_width/(max_horizontal - min_horizontal), game_height/(max_vertical - min_vertical));
    //var transform ="translate(" + (game_width - max_horizontal*scale - min_horizontal*scale)/2 + "px, "+ (game_height - max_vertical*scale - min_vertical*scale)/2 + "px) scale("+ scale+","+ scale +")";
    var transform ="translate(" + (-min_horizontal) + "px, "+ (-min_vertical) + "px)";
    
    //console.log (transform);
    $("#main_display").width (max_horizontal - min_horizontal).height(max_vertical - min_vertical).css ({display: "block", margin: "0 auto"});
    $("#board").css({transform});
  }
  setTimeout (draw, 20);
  //draw();
  
  
  var skip_turn = false;
  
  function rotate_right ()
  {
    if (skip_turn) {return;}
    floating_tile.rotation = (floating_tile.rotation + 1) % 6;
    floating_tile.graphical_rotation += 1;
    update_position (floating_tile) ;
    refresh_paths ();
  }
  $("#tile_controls").append ($("<button>").text ("rotate left").click (function() {
    if (skip_turn) {return;}
    floating_tile.rotation = (floating_tile.rotation + 5) % 6;
    floating_tile.graphical_rotation -= 1;
    update_position (floating_tile) ;
    refresh_paths ();
  }));
  $("#tile_controls").append ($("<button>").text ("rotate right").click (rotate_right));
  $("#tile_controls").append ($("<button>").text ("place tile").click (function() {
    if (skip_turn) {return;}
    if (floating_tile.horizontal === undefined) {return;}
    var legalities = {};
    collect_paths (floating_tile).forEach(function(path) {
      legalities [path_legality (path, floating_tile)] = true;
    });
    if (legalities.forbidden || (legalities.waste &&!legalities.success)) {return;}

    create_borders_around (floating_tile);
    begin_turn();
  }));
  $("#tile_controls").css({position: "fixed",left:0,top:"50%"});  
  $("#tile_controls button").css({display:"block"});
  
  var current_player_index = 0;
  function begin_turn() {
    current_player_index = (current_player_index + 1) % players.length;
    var player = players [current_player_index];
    
    floating_tile = create_random_tile ();
    update_position (floating_tile) ;
    refresh_paths();
    var icon = get_icon (floating_tile.element);
    
    function paragraph (text) { return $("<p>").text (text);}
    var drat = $("<button>").css({width:"16em", height: "3em",}).text ("Drat").click (function() {
      begin_turn();
    });
    
    $("#messages").empty().css({"background-color":"#ffcccc", "text-align": "center", padding: "0.1em", "font-size": "120%"}).append (paragraph (`${player.name}'s turn!`));
    
    
    $("#messages").append (
      paragraph (`${player.name}, you drew:`),
      $(`<svg width="${long_radius*2}" height="${long_radius*2}">`).css({display: "block", margin: "0.9em auto"}).append (floating_tile.element)
    );
    
    if (floating_tile.player === player && (icon.icon === "torso" || icon.icon === "crotch")) {
      skip_turn = true;
      $("#messages").append (
        paragraph (`Whoops! It's your own ${icon.icon}. You skip your turn.`),
        drat
      );
      return;
    }
    
    skip_turn = false;
  }
  /*
    The starting tile is ${player.name}, so ${player.name} goes first.
    
    ${player.name}'s turn!
    
    ${player.name}, you drew:
    
    [tile]
    
    move_instructions = tap a different border hex to try a different location. TODO if you want to rotate it.
    
    
    Tap one of the border hexes to move it there.
    
    Great! Tap it again to put it there and pass your turn, or ${move_instructions}   

    Whoops! You can't place it there because its icon connects to the ${path pre-existing icons description} that's already on the board. ${move_instructions}
    
    
    Whoops! It's your own ${icon.icon}. You skip your turn. [Drat]
    what's! It's ${player.name}'s ${icon.icon}, and ${player.name} already lost. You skip your turn. [Drat]
    
    ${player.name}, you skip your turn because ${ you couldn't connection effect}. [Drat]
    
    a connection has been formed! [Picture of the icons]
    
    Tie ${player.name}'s hands together in front of them! [Okay, done] [We can't do that]
    
    Why not? [${player.name} is already too tied up] [${player.name} only has one usable hand] [something else]
    
    Okay. ${Player.name} will skip their next 2 turns instead.
    
    Okay. We'll skip the connection this time.
    
    Re-tie ${player.name}'s hands together behind them!
    Tie ${player.name}'s hand behind them!
    
    Tie ${player.name}'s ${icon.side} ${icon.icon} to their ${icon.side} ${icon.icon}!
    
    From now on, ${player0.name} can stimulate ${player1.name}'s ${stuff} with their ${stuff}!
    ${player0.name} was already allowed to stimulate ${player1.name}'s ${stuff} with their ${stuff}, so ${player1} skips 2 turns instead.
    
    ${player.name}, choose a toy to be used on you. [Okay, done] [All my toys are already used]
    
    Tie X to Y!
    Tie together all of these: []!
    
    (Probably only in multiplayer:)
    [Click here if ${player.name} can't reach the board, and thus has lost the game]
  */
  
});