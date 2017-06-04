"use strict";

var drawn_games = {};

  var legality_fill = {
    acceptable: "#0000ff",
    forbidden: "#ff0000",
    waste: "#990000",
    success: "#aaaa00"
  };

function create_(tag, attributes) {
  var result = document.createElementNS("http://www.w3.org/2000/svg", tag);
  if (attributes) { Object.getOwnPropertyNames (attributes).forEach(function(name) {
    result.setAttribute(name, attributes [name]);
  }); }
  return result;
}

function create_drawn_tile (tile) {
  var drawn_tile = _.clone(tile);
  drawn_tile.element = create_ ("use");
  set_link (drawn_tile.element, "#"+tile.tile_id);
  drawn_tile.element.classList.add("tile");
  
  if (tile.player) {
    drawn_tile.element.style.setProperty ("--icon-fill", tile.player.fill);
    drawn_tile.element.style.setProperty ("--icon-stroke", tile.player.stroke);
  }
  return drawn_tile;
}


function clear_paths (tile) {
      function do_connection (identifier) {
        tile.element.style.setProperty ("--path-fill-" + identifier, "#808080");
      }
      info_by_tile_id[tile.tile_id].connections.forEach(function(connection, index) {
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
}

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

var long_radius = 36;
var short_radius = long_radius*0.866;
function visual_position (horizontal, vertical) {
  if (vertical === undefined) {vertical = horizontal.vertical; horizontal = horizontal.horizontal;}
  return {horizontal: horizontal*1.5*long_radius, vertical: vertical*short_radius}
}

function neutral_transform (id) {
    var original = $("#"+id)[0];
    
    var offset = info_by_tile_id[id].offset;
    var icon = icons_by_tile_id[id];
    var offset_horizontal = offset.horizontal + (icon && icon.grid_position*1.732 || 0);
    var offset_vertical = 1052.36218-offset.vertical;
    
    var transform_origin = ""+(offset_horizontal)+"px "+(offset_vertical)+"px 0px"//"50% 50% 0";//""+ (offset.x+0.5*offset.width)+"px "+ (offset.y+0.5*offset.height)+"px 0px";
    var transform = "translate("+ (-(offset_horizontal))+"px, "+ (-(offset_vertical))+"px)";
    return {"transformOrigin": transform_origin, transform: transform}
}

function calculate_transform (id, horizontal, vertical, rotation) {
    var result = neutral_transform (id);
    
    var position = visual_position (horizontal, vertical);
    result.transform = result.transform + (
      " translate(" + position.horizontal + "px," + position.vertical + "px) rotate("+(-0.0833 + rotation/6)+"turn) scale(" + long_radius+ "," + long_radius+ ")"
    );
    return result
}


function position_drawn_tile (tile) {
  var CSS = calculate_transform (tile.tile_id, tile.horizontal, tile.vertical, tile.rotation);
  tile.element.style.setProperty ("transform", CSS.transform);
  tile.element.style.setProperty ("transform-origin", CSS.transformOrigin);
}

function move_to_nearest_hex (approximate, modified) {
  //modified = modified || approximate;
  // this can be improved
  modified.horizontal = Math.round(approximate.horizontal);
  var adjustment = modified.horizontal & 1;
  modified.vertical = Math.round((approximate.vertical-adjustment)/2)*2+adjustment;
  modified.rotation = Math.round(approximate.rotation) % 6;
}

function move_towards (value, target, speed) {
  if (value === undefined) {return target;}
  if (Math.abs (value - target) <speed) {return target;}
  if (value >target) {return value - speed;}
  return value + speed;
}

function draw_game (game) {
  var drawn = drawn_games [game.id];
  
  function get_floating_tile_paths() {
    if (get_tile (game.tiles, drawn.floating_tile)) { return []; }
    // set temporarily in order to collect paths
    set_tile (drawn.tiles, drawn.floating_tile);
    var result = collect_paths (drawn.tiles, drawn.floating_tile);
    remove_tile (drawn.tiles, drawn.floating_tile);
    return result;
  }
  
  if (drawn === undefined) {
    drawn_games [game.id] = drawn = {tiles:{}};
    drawn.svg = create_("svg", {id:"game_"+game.id, class:"game" });
    drawn.board = create_ ("g");
    drawn.svg.appendChild (drawn.board);
    document.getElementById("content").appendChild (drawn.svg);
    drawn.message_area = $("<div>", {id:"message_area", class:"draw_game_temporary_"+game.id});
    $("#content").append (drawn.message_area);
    
    drawn.mouse_exact = {horizontal: 0, vertical: 0, rotation: 0};
    drawn.mouse_rounded = {horizontal: 0, vertical: 0, rotation: 0};
    drawn.rotation_target = 0;
    drawn.svg.addEventListener("mousemove", function (event) {
      var offset = $(drawn.svg).offset();
      var mouse_X = event.pageX - offset.left;
      var mouse_Y = event.pageY - offset.top;
      drawn.mouse_exact.horizontal = (mouse_X + drawn.min_horizontal)/(long_radius*1.5);
      drawn.mouse_exact.vertical = (mouse_Y + drawn.min_vertical)/short_radius;
    });
    
    drawn.svg.addEventListener("click", function (event) {
      if (event.button == 0 && game.floating_tile && drawn.floating_tile && !get_tile (game.tiles, drawn.floating_tile)) {
        var legality = placement_results (drawn.floating_tile, get_floating_tile_paths()).legality;
        if (legality !== "forbidden" && legality !== "waste") {
          place_floating_tile (game, drawn.floating_tile);
        }
      }
    });
    
    drawn.svg.addEventListener("contextmenu", function (event) {
      if (game.floating_tile && drawn.floating_tile) {
        drawn.rotation_target++;
      }
      event.preventDefault();
    });
  }
  
  move_to_nearest_hex (drawn.mouse_exact, drawn.mouse_rounded);
  
  var prompt = game.prompt_stack.length > 0 && game.prompt_stack [game.prompt_stack.length - 1];
  
  if (drawn.current_player !== game.current_player) {
    document.documentElement.style.setProperty ("--meta-fill", game.current_player.fill);
    document.documentElement.style.setProperty ("--meta-stroke", game.current_player.stroke);
    drawn.current_player = game.current_player;
  }
  
  var floating_changed = (game.floating_tile && game.floating_tile.key) !== (drawn.floating_tile && drawn.floating_tile.key);
  var floating_rounded_position_changed = floating_changed || (drawn.floating_tile && (
    drawn.floating_tile.horizontal !== drawn.mouse_rounded.horizontal ||
    drawn.floating_tile.vertical !== drawn.mouse_rounded.vertical ||
    drawn.floating_tile.rotation !== drawn.mouse_rounded.rotation
  ));
  /*var floating_exact_position_changed = floating_changed || (drawn.floating_tile && (
    drawn.floating_tile.horizontal !== drawn.mouse_exact.horizontal ||
    drawn.floating_tile.vertical !== drawn.mouse_exact.vertical ||
    drawn.floating_tile.rotation !== drawn.mouse_exact.rotation
  ));*/
  
  
  
      var min_horizontal = 0;
      var max_horizontal = 0;
      var min_vertical = 0;
      var max_vertical = 0;
      function include (location) {
        var position = tile_position (location);
        min_horizontal = Math.min (min_horizontal, position.horizontal - long_radius*2);
        max_horizontal = Math.max(max_horizontal, position.horizontal + long_radius*2);
        min_vertical = Math.min (min_vertical , position.vertical - short_radius*2);
        max_vertical = Math.max(max_vertical , position.vertical + short_radius*2);
      }
      
  game.anchored_tiles.forEach(function(tile) {
    var drawn_tile = get_tile (drawn.tiles, tile);
    if (drawn_tile === undefined) {
      drawn_tile = create_drawn_tile (tile);
      set_tile (drawn.tiles, drawn_tile);
      position_drawn_tile (drawn_tile);
      drawn.board.appendChild (drawn_tile.element);
    }
    if (floating_rounded_position_changed) {
      clear_paths (drawn_tile);
    }
    
    for (var direction = 0; direction <6 ;++direction) {
      var neighbor = in_direction (tile, direction);
      include (neighbor);
    }
  });
  
  if (floating_rounded_position_changed || prompt !== drawn.prompt) {
    drawn.message_area.empty();
    drawn.message_area.css({color:"", "border-color":""});
  }
  
  function color_messages (color) {
    drawn.message_area.css({color:color, "border-color":color});
  }
  
  if (floating_changed) {
    delete drawn.floating_tile;
    $(".floating_tile_"+game.id).remove();
    if (game.floating_tile) {
      var tile = game.floating_tile;
      drawn.floating_tile = create_drawn_tile (tile);
      drawn.floating_tile.element.classList.add("floating_tile_"+game.id);
      drawn.board.appendChild (drawn.floating_tile.element);
      
      drawn.location_indicator = create_drawn_tile ({ horizontal: drawn.floating_tile.horizontal, vertical: drawn.floating_tile.vertical, tile_id: blank_hex_id, rotation: 0 });
      drawn.location_indicator.element.style.setProperty ("opacity", "0.3");
      drawn.location_indicator.element.classList.add("floating_tile_"+game.id);
      drawn.board.insertBefore (drawn.location_indicator.element, drawn.board.firstChild);
    }
  }
  if (drawn.floating_tile) {
    drawn.floating_tile.horizontal = drawn.mouse_exact.horizontal;
    drawn.floating_tile.vertical = drawn.mouse_exact.vertical;
    drawn.floating_tile.rotation = drawn.mouse_exact.rotation;
    position_drawn_tile (drawn.floating_tile);
    drawn.floating_tile.horizontal = drawn.mouse_rounded.horizontal;
    drawn.floating_tile.vertical = drawn.mouse_rounded.vertical;
    drawn.floating_tile.rotation = drawn.mouse_rounded.rotation;
  }
  if (drawn.floating_tile && floating_rounded_position_changed) {
    clear_paths (drawn.floating_tile);
    
    drawn.location_indicator.horizontal = drawn.mouse_rounded.horizontal;
    drawn.location_indicator.vertical = drawn.mouse_rounded.vertical;
    drawn.location_indicator.rotation = drawn.mouse_rounded.rotation;
    position_drawn_tile (drawn.location_indicator);
    
    drawn.message_area.append (`<p>${game.current_player.name}'s turn.</p>`) ;
    
    if (!get_tile (game.tiles, drawn.floating_tile)) {
    
    var paths = get_floating_tile_paths();
    paths.forEach(function(path) {
      var fill = legality_fill [path_legality (path, drawn.floating_tile)];
      path.components.forEach(function(component) {
        fill_component (component.tile, component.from, component.towards, fill);
      });
    });
    var results = placement_results (drawn.floating_tile, paths);
    function list(things, transform) {
      if (things.length === 1) { return " "+transform (things[0]); }
      var result = "...</p><ul>"
      things.forEach(function(thing, index) {
        var item = transform (thing);
        result = result + "<li>"+item+"</li>";
      });
      return result+"</ul><p>"
    }
    
    if (results.legality === "forbidden") {
      drawn.message_area.append ("<p>You can't place the tile there because you can't connect your current icon to an icon that's already on the board.</p>") ;
      color_messages (legality_fill [results.legality]);
    }
    if (results.legality === "waste") {
      drawn.message_area.append ("<p>You can't place the tile there because"+ list (results.relevant_paths, path => {
        if (path.icons.length >1) {
          return `a connection between ${describe_tile_icon (path.icons [0])} and ${describe_tile_icon (path.icons [1])} doesn't do anything`;
        }
        else {
          return `it would connect ${describe_tile_icon (path.icons [0])} to a dead end`;
        }
      })+ " (and you didn't also make any connections that <em>do</em> do something.)</p>") ;
      color_messages (legality_fill ["forbidden"]);
    }
    if (results.legality === "success") {
      drawn.message_area.append ("<p>If you place the tile there, it will cause"+list (results.relevant_paths, path => {
        var effects = path_effects (path);
        return '"'+ effects.message +'"';
      })+"</p>");
      color_messages (legality_fill [results.legality]);
    }
    
    }
  }
  
  if (prompt && prompt !== drawn.prompt) {
    drawn.message_area.append (prompt.message);
    prompt.options.forEach(function(option) {
      drawn.message_area.append ($("<input>", {type: "button", class: "prompt_option", value: option.text}).on("click", function() {
        answer_prompt (game, option);
      }));
    });
  }
  drawn.prompt = prompt;
  
  var speed = 2;
  drawn.min_horizontal = move_towards (drawn.min_horizontal, min_horizontal, speed);
  drawn.max_horizontal = move_towards (drawn.max_horizontal, max_horizontal, speed);
  drawn.min_vertical = move_towards (drawn.min_vertical, min_vertical, speed);
  drawn.max_vertical = move_towards (drawn.max_vertical, max_vertical, speed);
  drawn.mouse_exact.rotation = move_towards (drawn.mouse_exact.rotation, drawn.rotation_target, 0.1);
  var width = drawn.max_horizontal - drawn.min_horizontal;
  var height = drawn.max_vertical - drawn.min_vertical;
  drawn.svg.setAttribute("width", width);
  drawn.svg.setAttribute("height", height);
  drawn.board.style.setProperty ("transform", "translate(" + (-drawn.min_horizontal) + "px, "+ (-drawn.min_vertical) + "px)");
  
}



function tick() {
  requestAnimationFrame (tick);
  
  draw_game (global_game) ;
}
tick();

