
var drawn_games = {}

function create_drawn_tile (tile) {
  var drawn_tile = Object.extend({}, tile};
  drawn_tile.element = create_ ("g");
  set_link (drawn_tile.element, tile.tile_id);
  return drawn_tile;
}

function position_drawn_tile (drawn_tile) {

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
  
  game.tiles.forEach(function(tile) {
    if (tile.anchored) {
      var drawn_tile = get_tile (drawn.tiles, tile);
      if (drawn_tile === undefined) {
        drawn_tile = create_drawn_tile (tile);
        set_tile (drawn.tiles, drawn_tile);
        position_drawn_tile (drawn_tile);
        drawn.board.appendChild (drawn_tile);
      }
    }
    else {
      var drawn_tile = create_drawn_tile (tile);
      drawn_tile.classList.add("draw_game_temporary_"..game.id);
      drawn_tile.horizontal = game.floating
      position_drawn_tile (drawn_tile);
      drawn.board.appendChild (drawn_tile);
    }
  });
}


function tick() {
  
}


