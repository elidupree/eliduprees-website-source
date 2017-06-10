"use strict";

function to_rgb(color) {
  return {
    red: parseInt (color.substring (1, 3), 16),
    green: parseInt (color.substring (3, 5), 16),
    blue: parseInt (color.substring (5, 7), 16),
  }
}

var default_players = [
  {based_on: "white", name: "White", fill: "#ffffff", stroke: "#000000"},
  {based_on: "black", name: "Black", fill: "#000000", stroke: "#ffffff"},
  {based_on: "white", name: "Pink", fill: "#ffaaff", stroke: "#ff00ff"},
  {based_on: "white", name: "Green", fill: "#99ff99", stroke: "#008800"},
  {based_on: "black", name: "Blue", fill: "#0000ff", stroke: "#ffffff"},
  {based_on: "black", name: "Purple", fill: "#5500aa", stroke: "#ffffff"},
];

function make_game_setup_area (initial_players) {
  var players = [];
  function make_player_area(player, default_name, default_fill, default_stroke) {
    var player_info = {};
    var default_name = player.name;
    var default_fill = player.fill;
    var default_stroke = player.stroke;
    function update_player_colors() {
      player.fill = player_info.fill_input.value();
      player.stroke = player_info.stroke_input.value();
      var fill = to_rgb (player.fill);
      var stroke = to_rgb (player.stroke);
      player.based_on = (fill.red + fill.green + fill.blue >stroke.red + stroke.green + stroke.blue) && "white" || "black";
    }
  
    return player_info.element = $("<div>", {class:"player_options"}).append(
      $("<div>", {class:"player_row"}).append(
        $("<label>", {for: "player_name_" + default_name}).text("Player name: "),
        player_info.name_input = $("<input>", {type: "text", value: default_name, id: "player_name_" + default_name})
      ),
      $("<div>", {class:"player_row"}).append(
        $("<label>", {for: "player_fill_" + default_name}).text("Color: "),
        player_info.fill_input = $("<input>", {type: "color", value: default_fill, id: "player_fill_" + default_name}).on("input", update_player_colors)
      ),
      $("<div>", {class:"player_row"}).append(
        $("<label>", {for: "player_stroke_" + default_name}).text("Outline color: "),
        player_info.stroke_input = $("<input>", {type: "color", value: default_stroke, id: "player_stroke_" + default_name}).on("input", update_player_colors)
      ),
      $("<div>", {class:"player_row"}).append(
        $("<input>", {type: "button", value: "Remove this player"}).click (function() {
          players = players.filter (other => other !== player);
          player_info.element.remove();
        })
      )
    );
  }
  
  var info = {};
  
  function add_player (prototype) {
    var created = _.cloneDeep (prototype);
    players.push (created);
    info.players_area.append (make_player_area (created));
  }
  
  var result = $("<div>", {class:"game_setup"}).append(
    info.players_area = $("<div>", {class:"players"}),
    $("<input>", {type: "button", value: "Add player"}).click (function() {
      var prototype =
        default_players.find(function(proposed) {
          return players.every (function (existing) {
            return proposed.name !== existing.name && proposed.fill !== existing.fill;
          });
        });
      if (prototype) {add_player (prototype);}
    }),
    $("<input>", {type: "button", value: "Start game"}).click (function() {
      result.remove();
      undraw_game (global_game);
      global_game = new_game (players);
      autosave_game (global_game);
    })
  );
  
  result.append (
    $("<input>", {type: "button", value: "Cancel"}).click (function() {
      result.remove();
    })
  );
  
  initial_players.forEach(function(player) {
    add_player (player);
  });
  
  return result;
}

var global_game;
function autosave_game (game) {
  localStorage.setItem ("hexy_bondage_autosave", JSON.stringify(game));
}
function autoload_game () {
  undraw_game (global_game);
  var save = localStorage.getItem ("hexy_bondage_autosave");
  global_game = JSON.parse(save);
  if (global_game === null) {restart_game(new_game (default_players.slice (0, 2))); }
}
function restart_game (new_game) {
  undraw_game (global_game);
  global_game = new_game;
  autosave_game (global_game);
}


function tick() {
  requestAnimationFrame (tick);
  
  draw_game (global_game) ;
}
autoload_game ();
tick();

