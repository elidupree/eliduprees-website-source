$(function(){
  "use strict"
  
  function get_link (whatever) {return whatever.getAttributeNS('http://www.w3.org/1999/xlink', 'href'); }
  function set_link (whatever, value) {return whatever.setAttributeNS('http://www.w3.org/1999/xlink', 'xlink:href', value); }
  
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
  
  var dead={};var icon={};var lock={};
  var connections_table = {
    [blank_hex_id]: { offset: {horizontal: 0, vertical: 1050.862}},
  
    g8043: {connections: [3, 2, 1, 0, 5, 4], offset: {horizontal: 3, vertical: 1038.862}, weight: 10, pieces: ["use7975","use8039","use8041"]},
    g8261: {connections: [2, 4, 0, 5, 1, 3], offset: {horizontal: 3, vertical: 1026.862}, weight: 15, pieces: ["use8257","use8259","use8255"]},
    g8571: {connections: [2, 3, 0, 1, 5, 4], offset: {horizontal: 3, vertical: 1014.862}, weight: 15, pieces: ["use8567","use8565","use8569"]},
    g8657: {connections: [1, 0, 3, 2, 5, 4], offset: {horizontal: 20, vertical: 1007.862}, weight: 4, pieces: ["use8655","use8653","use8651"]},
    g8985: {connections: [3, 4, 5, 0, 1, 2], offset: {horizontal: 20, vertical: 1001.862}, weight: 0, pieces: ["use8983","use8981","use8979"]},
    
    
    g9384: {connections: [5, dead, icon, 4, 3, 0], offset: {horizontal: 20, vertical: 1036.862}, weight: 8},
    g9425: {connections: [1, 0, icon, 4, 3, dead], offset: {horizontal: 20, vertical: 1036.862 - 2}, weight: 34},
    g9432: {connections: [1, 0, icon, dead, 5, 4], offset: {horizontal: 20, vertical: 1036.862 - 4}, weight: 8},
    g9631: {connections: [2, 3, 0, 1, icon, dead], offset: {horizontal: 20, vertical: 1036.862-6}, weight: 29},
    g9625: {connections: [2, 3, 0, 1, dead, icon], offset: {horizontal: 20, vertical: 1036.862-8}, weight: 29},
    g9812: {connections: [4, 2, 1, icon, 0, dead], offset: {horizontal: 20, vertical: 1036.862-10}, weight: 10},
    g9843: {connections: [2, dead, 0, icon, 5, 4], offset: {horizontal: 20, vertical: 1036.862-12}, weight: 10},
    g10007: {connections: [3, 2, 1, 0, icon, dead], offset: {horizontal: 20, vertical: 1036.862-14}, weight: 24},
    g10014: {connections: [3, 2, 1, 0, dead, icon], offset: {horizontal: 20, vertical: 1036.862-16}, weight: 24},
    g10195: {connections: [3, 4, dead, 0, 1, icon], offset: {horizontal: 20, vertical: 1036.862-18}, weight: 0},
    g10315: {connections: [2, 4, 0, dead, 1, icon], offset: {horizontal: 20, vertical: 1036.862-20}, weight: 0},
    g10325: {connections: [icon, 4, dead, 5, 1, 3], offset: {horizontal: 20, vertical: 1036.862-22}, weight: 0},
    g10573: {connections: [lock, lock, lock, 5, lock, 3], offset: {horizontal: 20, vertical: 1012.862}, weight: 1},
    g10495: {connections: [2, 3, 0, 1, lock, lock], offset: {horizontal: 20, vertical: 1010.862}, weight: 3},
  };
  
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
      if (typeof connection == "number") {
        if (info.connections[connection] !== index) {
          console.log ("error: mismatched connections");
        }
        if (info.pieces && index <connection) {
          var piece_element = document.getElementById (info.pieces [piece_index]);
          piece_element.style.setProperty ("--path-fill", "var(--path-fill-" + index + "-" + connection+")");
          ++piece_index;
        }
      }
    });}
  });
  
  Object.getOwnPropertyNames(icons_table).forEach(function(id) {
    var icon_info = icons_table [id];
    icon_info .id = id;
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
    if (typeof towards === "number") {
      from = (from + 6 - tile.rotation) % 6;
      towards = (towards + 6 - tile.rotation) % 6 ;
      if (from >towards) {[from, towards] = [towards, from];}
      tile.element.style.setProperty ("--path-fill-" + from + "-" + towards, fill);
    }
  }
  
  function follow_path (location, from_direction, tile_callback, finish_callback) {
    var tile = get_tile (location);
    if (!tile || tile.border) {
      if (finish_callback) { finish_callback (location, from_direction); }
      return;
    }
    var connections = get_connections (tile.element);
    var index = (from_direction + 6 - tile.rotation) % 6;
    var destination = connections[index];
    if (typeof destination === "number") {
      destination = (connections[index] + tile.rotation) % 6;
      tile_callback (tile, from_direction, destination);
      //var offset = directions [destination];
      //var next = get_tile (tile.horizontal + offset.horizontal, tile.vertical + offset.vertical);
      //if (next) {
        follow_path(in_direction (location, destination), (destination + 3) % 6, tile_callback, finish_callback);
      //}
    }
    else {
      tile_callback (tile, from_direction, destination);
      if (finish_callback) {finish_callback (location, from_direction, tile, destination);}
    }
  }
  
  function draw_path (horizontal, vertical, from_direction, towards) {
    follow_path({horizontal, vertical}, from_direction, function(tile, from, towards) {
      //$(tile.element).css({opacity: 0.5});
      tile.element.style.setProperty ("--path-fill", "red");
      fill_component (tile, from, towards, "blue");
    });
  }
  
  function calculate_transform (clone, horizontal, vertical, rotation) {
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
    var position = tile_position (horizontal, vertical);
    var transform = (
      //"translate("+ (-(offset.x+0.5*offset.width))+"px, "+ (-(offset.y+0.5*offset.height))+"px)"
      "translate("+ (-(offset_horizontal))+"px, "+ (-(offset_vertical))+"px)"
      +" translate(500px, 300px) translate(" + position.horizontal + "px," + position.vertical + "px) rotate("+(-0.0833 + rotation/6)+"turn) scale(" + long_radius+ "," + long_radius+ ")"
    );
    //console.log (transform);
    return {"transform-origin": transform_origin, transform: transform}
  }
  
  var tiles = {}
  var floating_tile;
  
  function create_clone (id) {
    var whatever =document.createElementNS("http://www.w3.org/2000/svg", 'use');
    set_link (whatever, '#'+id);
    //console.log (get_link (whatever));
    whatever.setAttribute("x", 0);
    whatever.setAttribute("y", 0);
    $("svg").append(whatever);
    return whatever;
  }
  function create_tile (id, rotation) {
    var element = create_clone (id);
    var tile = {rotation, element};
    $(element).addClass("tile").click(function() {
      if (tile === floating_tile) {
        create_borders_around (tile);
        floating_tile = create_tile(random_choice (tile_ids), 0);
      } else {
        draw_path(tile.horizontal, tile.vertical, 0);
      }
    });
    return tile;
  }
  function create_random_tile () {
    var choose_icon = Math.random() < 0.7;
    var id;
    while (true) {
      id = random_choice (tile_ids);
      var icon = icons_by_tile_id[id];
      var info = info_by_tile_id[id];
      //console.log(info.weight*(icon && icon.weight || 1));
      if ((!!icon === !!choose_icon) && (Math.random()*10000 < info.weight*(icon && icon.weight || 1))) {
        break;
      }
    }
    return create_tile(id, random_range (0, 6));
  }
  function create_border_tile (location) {
    var element = create_clone (blank_hex_id);
    $(element).addClass("tile border").css(calculate_transform (element, location.horizontal, location.vertical, 0)).click(function() {
      set_tile (location, floating_tile);
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
      delete tiles ["" + location.horizontal + "_" + location.vertical];
    }
  }
  function set_tile (location, tile) {
    remove_tile (location);
    tiles ["" + location.horizontal + "_" + location.vertical] = tile
    if (tile.horizontal) {
      delete tiles ["" + tile.horizontal + "_" + tile.vertical]
      create_border_tile ({horizontal: tile.horizontal, vertical: tile.vertical});
    }
    tile.horizontal = location.horizontal; tile.vertical = location.vertical;
    $(tile.element).css(calculate_transform (tile.element, location.horizontal, location.vertical, tile.rotation));
    if (!(tile.border || tile === floating_tile)) {
      create_borders_around (location);
    }
  }
  function get_tile (location) {
    return tiles ["" + location.horizontal + "_" + location.vertical]
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
  for (var index = -5; index <=5;++index) {
    for (var terrible = index-5; terrible <=index+5;terrible+=2) {
      hack (index, terrible);
    }
  }
  floating_tile = create_random_tile ();
});