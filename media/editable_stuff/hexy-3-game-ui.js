"use strict";

var turn = Math.PI*2;
var top_bar = $(".top_bar");
var bottom_bar = $(".bottom_bar");
$(".bars_inner_box").css ("padding-bottom", 0);

var frames_per_second = 60;
var game_height;
var game_width;
var window_height;
var window_width;
var resized = true;

var global_menu;

function update_dimensions() {
  window_height = $(window).height();
  window_width = $(window).width();
  var bars_size = window_height*window_width < 300000 ? window_height*window_width/300000*16 : "unset";
  top_bar.css ("font-size", bars_size);
  bottom_bar.css ("font-size", bars_size);

  var game_top = top_bar.offset().top + top_bar.height();
  var game_bottom = window_height - bottom_bar.height();
  
  var height = game_bottom - game_top;
  resized = game_width != window_width || game_height != height;
  game_height = height;
  game_width = window_width;

  if (global_menu) { resize_menu_navigation(); }
}
function did_update_dimensions() {
  if (resized) {
    resized = false;    
    return true;
  }
}
update_dimensions();
$(window).resize (update_dimensions);



var drawn_games = {};

  var legality_fill = {
    acceptable: ["#0000ff","#0099ff","#9900ff","#9999ff"],
    forbidden: ["#ff0000"],
    waste: ["#990000","#995500","#990055","#995555"],
    success: ["#aaaa00","#99dd00","#dd9900"]
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


function clear_paths (tile, color) {
      function do_connection (identifier, display_override) {
        tile.element.style.setProperty ("--path-fill-" + identifier, color || "#808080");
        tile.element.style.setProperty ("--path-display-" + identifier, display_override ? "none" : "unset");
        
      }
      info_by_tile_id[tile.tile_id].connections.forEach(function(connection, index) {
        if (typeof connection == "number") {
          if (index <connection) {
            do_connection (index + "-" + connection, tile.drawn_components && !tile.drawn_components [index]);
          }
        }
        else if (connection == "lock") {
          do_connection ("lock");
        } else {
          do_connection (index + "-" + connection, tile.drawn_components && !tile.drawn_components [index]);
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

function calculate_transform (drawn, id, horizontal, vertical, rotation) {
    var result = neutral_transform (id);
    
    var position = visual_position (horizontal, vertical);
    result.transform = result.transform + (
      " translate(" + position.horizontal*drawn.scale + "px," + position.vertical*drawn.scale + "px) rotate("+(-0.0833 + rotation/6)+"turn) scale(" + long_radius*drawn.scale+ "," + long_radius*drawn.scale+ ")"
    );
    return result
}


function position_drawn_tile (drawn, tile) {
  var CSS = calculate_transform (drawn, tile.tile_id, tile.horizontal, tile.vertical, tile.rotation);
  tile.element.style.setProperty ("transform", CSS.transform);
  tile.element.style.setProperty ("transform-origin", CSS.transformOrigin);
}

function visual_to_exact (visual, modified) {
  modified = modified || {};
  modified.horizontal = visual.horizontal/(1.5*long_radius);
  modified.vertical = visual.vertical/short_radius;
  return modified;
}

function move_to_nearest_hex (exact, modified) {
  //modified = modified || exact;
  modified = modified || {};
  // this can be improved
  modified.horizontal = Math.round(exact.horizontal);
  var adjustment = modified.horizontal & 1;
  modified.vertical = Math.round((exact.vertical-adjustment)/2)*2+adjustment;
  if (exact.rotation) {
    modified.rotation = ((Math.round(exact.rotation) % 6) + 6) % 6;
  }
  return modified;
}

var speed_switch_threshold = frames_per_second/2;
// at a distance of speed*speed_switch_threshold, this times speed*speed_switch_threshold should equal speed
var speed_exponential_factor = 1/speed_switch_threshold;

function move_towards (value, target, speed) {
  if (value === undefined) {return target;}
  if (Math.abs (value - target) <speed) {return target;}
  if (Math.abs (value - target) > speed*speed_switch_threshold) {
    return target*speed_exponential_factor + value*(1-speed_exponential_factor);
  }
  if (value >target) {return value - speed;}
  return value + speed;
}

function draw_game (game) {
  var drawn = drawn_games [game.id];
  var mode = game_modes [game.settings.mode];
  
  function floating_tile_playable() {
    return game.floating_tile && drawn.floating_tile && !get_tile (game.tiles, drawn.floating_tile) && mode.location_playable (game, drawn.floating_tile);
  }
  
  function get_floating_tile_paths() {
    if (get_tile (game.tiles, drawn.floating_tile)) { return []; }
    // set temporarily in order to collect paths
    set_tile (drawn.tiles, drawn.floating_tile);
    var result = collect_paths (drawn.tiles, drawn.floating_tile);
    remove_tile (drawn.tiles, drawn.floating_tile);
    return result;
  }
  
  function rotate (amount) {
    if (game.floating_tile && drawn.floating_tile) {
      drawn.rotation_target += amount;
      return true;
    }
  }
  
  function visual_horizontal_from_pageX (pageX) {
    return (pageX - drawn.svg_offset.left)/drawn.scale + drawn.min_horizontal;
    
  }
  function visual_vertical_from_pageY (pageY) {
    return (pageY - drawn.svg_offset.top)/drawn.scale + drawn.min_vertical;
  }
  
  function update_touch_position (touch) {
    var info = drawn.touches [touch.identifier];
    info.visual_location = {horizontal: visual_horizontal_from_pageX (touch.pageX), vertical: visual_vertical_from_pageY (touch.pageY)};
    if (!info.original_location) {info.original_location = info.visual_location;}
    if (
      Math.abs(info.original_location.horizontal-info.visual_location.horizontal) > 3 || 
      Math.abs(info.original_location.vertical-info.visual_location.vertical) > 3 ) {
      info.moved = true;
    }
    info.exact_location = visual_to_exact (info.visual_location);
    info.rounded_location = move_to_nearest_hex (info.exact_location);
    if (info.moved && drawn.touch_holding_tile === touch.identifier) {
      drawn.mouse_visual.horizontal = info.visual_location.horizontal;
      drawn.mouse_visual.vertical = info.visual_location.vertical;
    }
  }
  
  var just_created = (drawn === undefined);
  if (just_created) {
    drawn_games [game.id] = drawn = {
      tiles:{},
      tiles_list: [],
      touches: {},
      time_since_last_touch: 999,
      frame: 0,
    };
    drawn.element = $("<div>", {id:"game_"+game.id,class:"game" });
    
    drawn.svg = create_("svg", {class:"game_svg" });
    drawn.board = create_ ("g");
    drawn.svg.appendChild (drawn.board);
    document.getElementById("content").appendChild (drawn.element[0]);
    drawn.element.append (
      drawn.board_container = $("<div>", {class:"board_container"}).append(
        drawn.svg
      ),
      drawn.non_board_container = $("<div>", {class:"non_board_container"}).append(
        drawn.message_area = $("<div>", {class:"message_area message_area_"+game.id}).append(
          drawn.message_contents = $("<div>")
        ),
        $("<div>", {class:"buttons_area"}).append(
          $("<input>", {type: "button", value: "rotate left"}).on("click", function() {
            rotate (-1);
          }),
          $("<input>", {type: "button", value: "rotate right"}).on("click", function() {
            rotate (1);
          }),
          $("<input>", {type: "button", value: "menu"}).on("click", function() {
            show_menu ();
          })
        )
      )
    );
    document.addEventListener ("keydown", event => {
      if (event.keyCode === 37 && rotate (-1)) {event.preventDefault();}
      if (event.keyCode === 39 && rotate (1)) {event.preventDefault();}
    });
    
    
    drawn.mouse_visual = {horizontal: 0, vertical: 0};
    drawn.mouse_exact = {horizontal: 0, vertical: 0, rotation: 0};
    drawn.mouse_rounded = {horizontal: 0, vertical: 0, rotation: 0};
    drawn.rotation_target = 0;
    drawn.svg.addEventListener("mousemove", function (event) {
      if (drawn.time_since_last_touch > 5) {
        drawn.svg_offset = $(drawn.svg).offset();
        drawn.mouse_visual.horizontal = visual_horizontal_from_pageX (event.pageX);
        drawn.mouse_visual.vertical = visual_vertical_from_pageY (event.pageY);
        delete drawn.tile_hover_location;
      }
    });
    
    drawn.svg.addEventListener("click", function (event) {
      if (!drawn.floating_tile) {return;}
      if (event.button !== 0) {return;}
      var location =move_to_nearest_hex (visual_to_exact ({horizontal:visual_horizontal_from_pageX (event.pageX), vertical:visual_vertical_from_pageY (event.pageY)}));
      if (floating_tile_playable() && (
            location.horizontal === drawn.floating_tile.horizontal && location.vertical === drawn.floating_tile.vertical
          )) {
        var legality = placement_results (game, drawn.floating_tile, get_floating_tile_paths()).legality;
        if (legality !== "forbidden" && legality !== "waste") {
          place_floating_tile (game, drawn.floating_tile);
          autosave_game (game);
        }
      }
      else {
        drawn.tile_hover_location = visual_position (location);
      }
    });
    
    /*drawn.svg.addEventListener("contextmenu", function (event) {
      if (game.floating_tile && drawn.floating_tile) {
        drawn.rotation_target++;
      }
      event.preventDefault();
    });*/
    
    
    
    drawn.svg.addEventListener("touchstart", function (event) {
      drawn.svg_offset = $(drawn.svg).offset();
      var touches = event.changedTouches;
      drawn.time_since_last_touch = 0;
      for (var i = 0; i < touches.length; i++) {
        var touch = touches[i];
        var info = drawn.touches [touch.identifier] = {};
        update_touch_position (touch);
        
        console.log(drawn.touch_holding_tile, info.rounded_location.horizontal , info.rounded_location.vertical , drawn.floating_tile.horizontal , drawn.floating_tile.vertical)
        if (drawn.touch_holding_tile === undefined && drawn.floating_tile && info.rounded_location.horizontal === drawn.floating_tile.horizontal && info.rounded_location.vertical === drawn.floating_tile.vertical) {
          drawn.touch_holding_tile = touch.identifier;
          delete drawn.tile_hover_location;
          update_touch_position (touch);
          //event.preventDefault();
        }
      }
    });
    drawn.svg.addEventListener("touchmove", function (event) {
      drawn.svg_offset = $(drawn.svg).offset();
      drawn.time_since_last_touch = 0;
      var touches = event.changedTouches;
      for (var i = 0; i < touches.length; i++) {
        var touch = touches[i];
        var info = drawn.touches [touch.identifier];
        update_touch_position (touch);
        if (drawn.touch_holding_tile === touch.identifier) {
          event.preventDefault();
        }
      }
    });
    drawn.svg.addEventListener("touchend", function (event) {
      drawn.svg_offset = $(drawn.svg).offset();
      drawn.time_since_last_touch = 0;
      var touches = event.changedTouches;
      for (var i = 0; i < touches.length; i++) {
        var touch = touches[i];
        delete drawn.touches [touch.identifier];
        if (drawn.touch_holding_tile === touch.identifier) {
          delete drawn.touch_holding_tile;
          drawn.tile_hover_location = visual_position (drawn.floating_tile);
          //event.preventDefault();
        }
      }
    });



  }
  
  ++drawn.frame;
  ++drawn.time_since_last_touch;
  
  if (drawn.tile_hover_location) {
    var cycle = turn*drawn.frame/(frames_per_second*2);
    var horizontal = drawn.tile_hover_location.horizontal + long_radius/6*Math.cos(cycle);
    var vertical = drawn.tile_hover_location.vertical + long_radius/10*Math.sin(cycle);
    var distance = (drawn.mouse_visual.horizontal - horizontal)*(drawn.mouse_visual.horizontal - horizontal) + (drawn.mouse_visual.vertical - vertical)*(drawn.mouse_visual.vertical - vertical);
    if (distance !== 0) {
      var new_distance = move_towards (distance, 0, long_radius*100/frames_per_second);
      var factor = new_distance / distance;
      drawn.mouse_visual.horizontal = drawn.mouse_visual.horizontal * factor + horizontal*(1 - factor);
      drawn.mouse_visual.vertical = drawn.mouse_visual.vertical * factor + vertical*(1 - factor);
    }
  }
  visual_to_exact (drawn.mouse_visual, drawn.mouse_exact) ;
  move_to_nearest_hex (drawn.mouse_exact, drawn.mouse_rounded);
  
  var prompt = game.prompt_stack.length > 0 && game.prompt_stack [game.prompt_stack.length - 1];
  
  if (drawn.current_player !== game.current_player) {
    var colors = UI_colors (current_player (game));
    document.body.style.setProperty ("--meta-fill", colors.fill);
    document.body.style.setProperty ("--meta-stroke", colors.stroke);
    drawn.current_player = game.current_player;
  }
  
  var floating_changed = just_created || (game.floating_tile && game.floating_tile.key) !== (drawn.floating_tile && drawn.floating_tile.key);
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
  
  var dimensions_changed = did_update_dimensions();
  if (dimensions_changed || just_created) {
    var board_share = Math.ceil(game_height * 0.7);
    drawn.board_container.height(board_share);
    drawn.non_board_container.height(game_height - board_share);
    var scale = Math.min (1, Math.min(game_width, board_share)/ (long_radius*10));
    var scale_changed = just_created || scale !== drawn.scale;
    drawn.scale = scale;
    drawn.dimensions = {horizontal: game_width, vertical: board_share};
  }
  
  
      var min_horizontal = 0;
      var max_horizontal = 0;
      var min_vertical = 0;
      var max_vertical = 0;
      function include (location) {
        var position = tile_position (location);
        min_horizontal = Math.min (min_horizontal, position.horizontal - long_radius);
        max_horizontal = Math.max(max_horizontal, position.horizontal + long_radius);
        min_vertical = Math.min (min_vertical , position.vertical - short_radius);
        max_vertical = Math.max(max_vertical , position.vertical + short_radius);
      }
      
  game.anchored_tiles.forEach(function(tile) {
    var drawn_tile = get_tile (drawn.tiles, tile);
    if (drawn_tile === undefined || drawn_tile.key !== tile.key) {
      drawn_tile = create_drawn_tile (tile);
      drawn.tiles_list.push (drawn_tile);
      set_tile (drawn.tiles, drawn_tile);
      console.log("aaa")
      position_drawn_tile (drawn, drawn_tile);
      drawn.board.appendChild (drawn_tile.element);
    }
    else if (scale_changed) {
      position_drawn_tile (drawn, drawn_tile);
    }
    if (floating_rounded_position_changed) {
      clear_paths (drawn_tile);
    }
    drawn_tile.frame_existed = drawn.frame;
    include (tile);
    if (!tile.edge) {
    for (var direction = 0; direction <6 ;++direction) {
      var neighbor = in_direction (tile, direction);
      include (neighbor);
    }
    }
  });
  drawn.tiles_list.filter (tile => {
    if (tile.frame_existed !== drawn.frame) {
      $(tile.element).remove();
      if (get_tile (drawn.tiles, tile) === tile) {remove_tile (drawn.tiles, tile);}
      return false;
    }
    return true;
  }) ;
  
  if (floating_changed || scale_changed) {
    if (mode.fog_tiles) {
      drawn.fog_tiles = drawn.fog_tiles || {};
      var fog_tiles =mode.fog_tiles (game);
      Object.getOwnPropertyNames (fog_tiles).forEach(function(index) {
        var tile = fog_tiles [index];
        var drawn_tile = get_tile (drawn.fog_tiles, tile);
        if (drawn_tile === undefined) {
          tile.tile_id = blank_hex_id;
          tile.rotation = 0;
          drawn_tile = create_drawn_tile (tile);
          set_tile (drawn.fog_tiles, drawn_tile);
          position_drawn_tile (drawn, drawn_tile);
          //console.log (tile, drawn_tile);
          drawn_tile.element.style.setProperty ("--hex-fill-opacity", tile.opacity);
          drawn.board.appendChild (drawn_tile.element);
          console.log("dfdfd");
        }
        else if (scale_changed) {
          console.log("aaaa");
          position_drawn_tile (drawn, drawn_tile);
        }
        console.log("afafa");
        drawn_tile.frame_existed = drawn.frame;
      });
      Object.getOwnPropertyNames (drawn.fog_tiles).forEach(function(index) {
        var tile = drawn.fog_tiles [index];
        if (tile.frame_existed !== drawn.frame) {
          $(tile.element).remove();
          remove_tile (drawn.fog_tiles, tile);
        }
      });
    }
  }
  
  var deficiency = drawn.dimensions.horizontal/drawn.scale - (max_horizontal - min_horizontal);
  if (deficiency >0) {max_horizontal += deficiency/2; min_horizontal -= deficiency/2;}
  deficiency = drawn.dimensions.vertical/drawn.scale - (max_vertical - min_vertical);
  if (deficiency >0) {max_vertical += deficiency/2; min_vertical -= deficiency/2;}


  function color_messages (color) {
    drawn.message_area.css({color:color, "border-color":color});
    if (drawn.location_indicator) {
      drawn.location_indicator.element.style.setProperty ("--hex-stroke", color);
    }
  }
  
  var redraw_messages = floating_rounded_position_changed || prompt !== drawn.prompt;
  if (redraw_messages) {
    drawn.message_contents.empty();
    color_messages("var(--meta-stroke)");
  }
  
  if (floating_changed) {    
    delete drawn.floating_tile;
    delete drawn.touch_holding_tile;
    $(".floating_tile_"+game.id).remove();
    if (game.floating_tile) {
      var tile = game.floating_tile;
      drawn.mouse_exact.rotation = drawn.mouse_rounded.rotation = drawn.rotation_target = tile.rotation;
      drawn.floating_tile = create_drawn_tile (tile);
      drawn.floating_tile.element.classList.add("floating_tile_"+game.id);
      drawn.board.appendChild (drawn.floating_tile.element);
      
      drawn.location_indicator = create_drawn_tile ({ horizontal: drawn.floating_tile.horizontal, vertical: drawn.floating_tile.vertical, tile_id: blank_hex_id, rotation: 0 });
      //drawn.location_indicator.element.style.setProperty ("opacity", "0.3");
      drawn.location_indicator.element.style.setProperty ("--hex-fill", "transparent");
      drawn.location_indicator.element.classList.add("floating_tile_"+game.id);
      drawn.board.insertBefore (drawn.location_indicator.element, drawn.board.firstChild);
    }
  }
  if (drawn.floating_tile) {
    drawn.floating_tile.horizontal = drawn.mouse_exact.horizontal;
    drawn.floating_tile.vertical = drawn.mouse_exact.vertical;
    drawn.floating_tile.rotation = drawn.mouse_exact.rotation;
    position_drawn_tile (drawn, drawn.floating_tile);
    drawn.floating_tile.horizontal = drawn.mouse_rounded.horizontal;
    drawn.floating_tile.vertical = drawn.mouse_rounded.vertical;
    drawn.floating_tile.rotation = drawn.mouse_rounded.rotation;
    if (floating_changed) {
      drawn.mouse_visual.horizontal = min_horizontal - long_radius*3;
      drawn.mouse_visual.vertical = min_vertical - long_radius*3;
      drawn.tile_hover_location = visual_position (drawn.floating_tile);
    }
  }
  
  function list(things, transform) {
      if (things.length === 1) { return " "+transform (things[0]); }
      var result = "...</p><ul>"
      things.forEach(function(thing, index) {
        var item = transform (thing);
        result = result + "<li>"+item+"</li>";
      });
      return result+"</ul><p>"
    }
    
  if (drawn.floating_tile && floating_rounded_position_changed) {
    clear_paths (drawn.floating_tile, legality_fill.acceptable[0]);
    
    drawn.location_indicator.horizontal = drawn.mouse_rounded.horizontal;
    drawn.location_indicator.vertical = drawn.mouse_rounded.vertical;
    drawn.location_indicator.rotation = drawn.mouse_rounded.rotation;
    position_drawn_tile (drawn, drawn.location_indicator);
    
    drawn.message_contents.append (`<p>${current_player (game).name}'s turn.</p>`) ;
    
    var no_message = false;
    if (!floating_tile_playable()) {
      no_message = true;
      drawn.location_indicator.element.style.setProperty ("display", "none");
    }
    else {
      drawn.location_indicator.element.style.setProperty ("display", "unset");
    
    var paths = get_floating_tile_paths();
    var legality_counts = {};
    paths.forEach(function(path) {
      var legality =path_legality (game, path, drawn.floating_tile);
      legality_counts[legality] = (legality_counts[legality] + 1) || 0;
      var fill = legality_fill [legality] [legality_counts[legality]];
      path.components.forEach(function(component) {
        fill_component (component.tile, component.from, component.towards, fill);
      });
    });
    var results = placement_results (game, drawn.floating_tile, paths);
    
    if (results.legality === "forbidden") {
      drawn.message_contents.append ("<p>You can't place the tile there because you can't connect your current icon to an icon that's already on the board.</p>") ;
      color_messages (legality_fill [results.legality] [0]);
    }
    else if (results.legality === "waste") {
      drawn.message_contents.append ("<p>You can't place the tile there because"+ list (results.relevant_paths, path => {
        if (path.icons.length >1) {
          return `a connection between ${describe_tile_icon (path.icons [0])} and ${describe_tile_icon (path.icons [1])} doesn't do anything`;
        }
        else {
          return `it would connect ${describe_tile_icon (path.icons [0])} to a dead end`;
        }
      })+ " (and you didn't also make any connections that <em>do</em> do something.)</p>") ;
      color_messages (legality_fill ["forbidden"] [0]);
    }
    else if (results.legality === "success") {
      var all_effects = [];
      results.relevant_paths.forEach(function(path) {
        var effects = path_effects (game, path);
        all_effects = all_effects.concat(effects);
      }) ;
      drawn.message_contents.append ("<p>If you place the tile there, then"+list (all_effects, effect => effect.hypothetical)+"</p>");
      color_messages (legality_fill [results.legality] [0]);
    }
    else {
      no_message = true;
    }
    }
    
    if (no_message) {
      if (game.players.reduce ((count, player) => player.eliminated? count: count + 1, 0) === 1) {
        drawn.message_contents.append (`<p>${current_player (game).name} is the only player left. They win! You can keep placing tiles if you want.</p>`) ;
      } else {
        drawn.message_contents.append (`<p>Mouse/touch-and-drag to position the tile. Buttons or arrow keys to rotate. Tap to place it.</p>`) ;
        drawn.message_contents.append ($("<div>", {role: "button", class: "prompt_option fake_button"}).html (`(click here if ${current_player (game).name} is unable to play)`).on("click", function() {
          eliminate_current_player (game);
          autosave_game (game);
        }));
      }
    }
  }
  
  if (prompt && prompt !== drawn.prompt) {
    drawn.message_contents.append ($("<p>").html(prompt.message));
    var options = $("<div>", {class: "prompt_options"});
    drawn.message_contents.append (options);
    prompt.options.forEach(function(option) {
      options.append ($("<div>", {role: "button", class: "prompt_option fake_button"}).html (option.text).on("click", function() {
        answer_prompt (game, option);
        autosave_game (game);
      }));
    });
  }
  drawn.prompt = prompt;
  
  if (redraw_messages || dimensions_changed) {
    var font_size = 100;
    drawn.message_contents.css ("font-size", `${font_size}%`);
    while (font_size > 30 && (drawn.message_contents.outerHeight() > drawn.message_area.height())) {
      font_size -= 5;
      drawn.message_contents.css ("font-size", `${font_size}%`);
    }
  }
  
  var board_changing = drawn.min_horizontal !== min_horizontal || drawn.max_horizontal !== max_horizontal || 
  drawn.min_vertical !== min_vertical || 
  drawn.max_vertical !== max_vertical;
  
  var speed = dimensions_changed ? 99999999 : 120/frames_per_second;
  drawn.min_horizontal = move_towards (drawn.min_horizontal, min_horizontal, speed);
  drawn.max_horizontal = move_towards (drawn.max_horizontal, max_horizontal, speed);
  drawn.min_vertical = move_towards (drawn.min_vertical, min_vertical, speed);
  drawn.max_vertical = move_towards (drawn.max_vertical, max_vertical, speed);
  drawn.mouse_exact.rotation = move_towards (drawn.mouse_exact.rotation, drawn.rotation_target, 6/frames_per_second);
  var width = Math.floor ((drawn.max_horizontal - drawn.min_horizontal)*drawn.scale);
  var height = Math.floor ((drawn.max_vertical - drawn.min_vertical)*drawn.scale);
  if (board_changing) {
    drawn.svg.setAttribute("width", width);
    drawn.svg.setAttribute("height", height);
    drawn.svg.style.setProperty("width", width);
    drawn.svg.style.setProperty("height", height);
    drawn.board_container.css("overflow", width>drawn.dimensions.horizontal || height >drawn.dimensions.vertical? "auto": "visible");
    drawn.board.style.setProperty ("transform", "translate(" + (-drawn.min_horizontal*drawn.scale) + "px, "+ (-drawn.min_vertical*drawn.scale) + "px)");
  }
}


function undraw_game (game) {
  if (game) {
    var drawn = drawn_games [game.id];
    if (drawn) {
      drawn.element.remove();
      delete drawn_games [game.id];
      document.body.style.setProperty ("--meta-fill", "unset");
      document.body.style.setProperty ("--meta-stroke", "unset");
    }
  }
}
  

