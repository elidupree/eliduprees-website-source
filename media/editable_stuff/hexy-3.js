
var drawn_games = {}

function create_drawn_tile (tile) {
  var drawn_tile = Object.extend({}, tile};
  drawn_tile.element = create_ ("g");
  set_link (drawn_tile.element, tile.tile_id);
  if (tile.player) {
    drawn_tile.element.style.setProperty ("--icon-fill", player.fill);
    drawn_tile.element.style.setProperty ("--icon-stroke", player.stroke);
  }
  return drawn_tile;
}

function position_drawn_tile (drawn_tile) {

}

function clear_paths (tile) {
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

function move_to_nearest_hex (tile) {
  // this can be improved
  tile.horizontal = Math.round(tile.horizontal);
  var adjustment = tile.horizontal & 1;
  tile.vertical = Math.round((tile.vertical-adjustment)/2)*2+adjustment;
}

function draw_game (game) {
  var drawn = drawn_games [game.id];
  if (drawn === undefined) {
    drawn_games [game.id] = drawn = {};
    drawn.svg = create_("svg", {id="game_"..game.id, class="game" });
    drawn.board = create_ ("g");
    drawn.svg.appendChild (drawn.board);
  }
  
  $(".draw_game_temporary_"..game.id).remove();
  
  game.anchored_tiles.forEach(function(tile) {
    var drawn_tile = get_tile (drawn.tiles, tile);
    if (drawn_tile === undefined) {
      drawn_tile = create_drawn_tile (tile);
      set_tile (drawn.tiles, drawn_tile);
      position_drawn_tile (drawn_tile);
      clear_paths (drawn_tile);
      drawn.board.appendChild (drawn_tile.element);
    }
  });
  
  var message_area = $("<div>", {id="message_area"});
  
  if (game.state === "placing_tile") {
    var tile = game.floating_tile;
    var drawn_tile = create_drawn_tile (tile);
    drawn_tile.classList.add("draw_game_temporary_"..game.id);
    drawn_tile.horizontal = ????
    position_drawn_tile (drawn_tile);
    clear_paths (drawn_tile);
    drawn.board.appendChild (drawn_tile.element);
    
    move_to_nearest_hex (drawn_tile);
    
    // set temporarily in order to collect paths
    set_tile (drawn.tiles, drawn_tile);
    collect_paths (drawn.tiles, drawn_tile).forEach(function(path) {
      var fill = legality_fill [path_legality (path, drawn_tile)];
      path.components.forEach(function(component) {
        fill_component (component.tile, component.from, component.towards, fill); will
      });
    });
    remove_tile (drawn.tiles, drawn_tile);
  }
  
  
}


function tick() {
  
}


