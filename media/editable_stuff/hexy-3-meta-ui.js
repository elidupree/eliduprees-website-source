"use strict";

function to_rgb(color) {
  return {
    red: parseInt (color.substring (1, 3), 16),
    green: parseInt (color.substring (3, 5), 16),
    blue: parseInt (color.substring (5, 7), 16),
  }
}

function UI_colors (player) {
  var results = {
    fill: to_rgb (player.fill),
    stroke: to_rgb (player.stroke),
  };
  var lighter = player.based_on === "white" && results.fill || results.stroke;
  var darker = player.based_on === "white" && results.stroke || results.fill;
  lighter.red = Math.round(255-(255-lighter.red)/3);
  lighter.green = Math.round(255-(255-lighter.green)/3);
  lighter.blue = Math.round(255-(255-lighter.blue)/3);
  darker.red = Math.round(darker.red/3);
  darker.green = Math.round(darker.green/3);
  darker.blue = Math.round(darker.blue/3);
  results.fill = `rgb(${results.fill.red}, ${results.fill.green}, ${results.fill.blue})`;
  results.stroke = `rgb(${results.stroke.red}, ${results.stroke.green}, ${results.stroke.blue})`;
  return results ;
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
  function make_player_area(player) {
    var player_info = {};
    var default_name = player.name;
    var default_fill = player.fill;
    var default_stroke = player.stroke;
    function update_player_colors() {
      player.fill = player_info.fill_input.val();
      player.stroke = player_info.stroke_input.val();
      var fill = to_rgb (player.fill);
      var stroke = to_rgb (player.stroke);
      player.based_on = (fill.red + fill.green + fill.blue >stroke.red + stroke.green + stroke.blue) && "white" || "black";
    }
    function update_player_name() {
      var input = player_info.name_input.val();
      if (players.every (existing => existing.name !== input)) {
        player.name = input;
      } else {
        player_info.name_input.val(player.name);
      }
    }
  
    return player_info.element = $("<div>", {class:"player_options"}).append(
      $("<div>", {class:"player_row"}).append(
        $("<label>", {for: "player_name_" + default_name}).text("Player name: "),
        player_info.name_input = $("<input>", {type: "text", value: default_name, id: "player_name_" + default_name}).change (update_player_name)
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
      if (players.length > 0) { 
        result.remove();
        undraw_game (global_game);
        global_game = new_game (players);
        autosave_game (global_game);
      }
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

