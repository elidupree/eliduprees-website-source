"use strict";

var entityMap = {
  '&': '&amp;',
  '<': '&lt;',
  '>': '&gt;',
  '"': '&quot;',
  "'": '&#39;',
  '/': '&#x2F;',
  '`': '&#x60;',
  '=': '&#x3D;'
};

function escape_string(string) {
  return String(string).replace(/[&<>"'`=\/]/g, function (s) {
    return entityMap[s];
  });
}

function unescape_string (string) {
  return (new DOMParser().parseFromString (string, "text/html")).documentElement.textContent;
}

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

function draw_fake_board (tiles_list) {
  var svg = create_("svg", {class:"game_svg" });
  var board = create_ ("g");
  var tiles = {};
  svg.appendChild (board);
  var border = 5;
      var min_horizontal = 0;
      var max_horizontal = 0;
      var min_vertical = 0;
      var max_vertical = 0;
      function include (location) {
        var position = tile_position (location);
        min_horizontal = Math.min (min_horizontal, position.horizontal - long_radius-border);
        max_horizontal = Math.max(max_horizontal, position.horizontal + long_radius+border);
        min_vertical = Math.min (min_vertical , position.vertical - short_radius-border);
        max_vertical = Math.max(max_vertical , position.vertical + short_radius+border);
      }
      
  tiles_list.forEach(function(tile) {
    var drawn_tile = create_drawn_tile (tile);
    set_tile (tiles, drawn_tile);
    position_drawn_tile ({scale:1}, drawn_tile);
    board.appendChild (drawn_tile.element);
    clear_paths (drawn_tile);
    include (tile);
  });
  var width = max_horizontal - min_horizontal;
  var height = max_vertical - min_vertical;
    
    svg.setAttribute("width", width);
    svg.setAttribute("height", height);
    svg.style.setProperty("width", width);
    svg.style.setProperty("height", height);
    svg.style.setProperty("background-color", "#ccc");
    svg.classList.add ("fake_board");
    board.style.setProperty ("transform", "translate(" + (-min_horizontal) + "px, "+ (-min_vertical) + "px)");

  tiles_list.forEach(function(tile) {
    (tile.paths || []).forEach(function(path_specs) {
      var path = collect_path (tiles, tile, path_specs.direction);
      path.components.forEach(function(component) {
        fill_component (component.tile, component.from, component.towards, path_specs.fill);
      });
    });
  });
  return svg;
}

var default_players = [
  {based_on: "black", name: "Black", fill: "#000000", stroke: "#ffffff"},
  {based_on: "white", name: "White", fill: "#ffffff", stroke: "#000000"},
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
      var input = escape_string (player_info.name_input.val());
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
    $("<input>", {type: "button", value: "Add another player"}).click (function() {
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
        close_menu();
        restart_game (new_game (players));
      }
    })
  );
  
  /*result.append (
    $("<input>", {type: "button", value: "Cancel"}).click (function() {
      result.remove();
    })
  );*/
  
  initial_players.forEach(function(player) {
    add_player (player);
  });
  
  return result;
}

function navigation(current) {
  var result = $("<div>", {id: "menu_navigation"});
  if (current !== "instructions") {result.append (
    $("<input>", {type: "button", value: "Back to instructions"}).click (function() {
      instructions();
    })
  );}
  if (current !== "start_game") {result.append (
    $("<input>", {type: "button", value: global_game? "Start a new game": "Start a game"}).click (function() {
      before_playing();
    })
  );}
  if (global_game) {
    if (current !== "game_menu") {result.append (
      $("<input>", {type: "button", value: "Current game options"}).click (function() {
        game_menu();
      })
    );}
    result.append (
      $("<input>", {type: "button", value: "Close menu"}).click (function() {
        close_menu();
      })
    );
  }
  
  return result;
}

function instructions() {
  $("#menu").empty().scrollTop (0).append (
    $("<h1>").text ("Welcome to Hexy Bondage!"),
    $("<p>").text ("Hexy Bondage is a sexual game for two players (or more) to play together on the same device."),
    $("<h2>").text ("Instructions"),
    $("<p>").text ("You take turns placing tiles like this:"),
    $("<div>", {class: "fake_boards"}).append (
      draw_fake_board ([{tile_id: "g8043", horizontal: 0, vertical: 0, rotation: 0}]),
      draw_fake_board ([{tile_id: "g8261", horizontal: 0, vertical: 0, rotation: 0}]),
      draw_fake_board ([{tile_id: "g8571", horizontal: 0, vertical: 0, rotation: 0}]),
    ),
    $("<p>").text ("Your goal is to connect different icons together, like this:"),
  
    $("<div>", {class: "fake_boards"}).append (
      draw_fake_board ([
        {tile_id: "g4955", horizontal: -1, vertical: -1, rotation: 0, player: default_players [0]},
        {tile_id: "g8261", horizontal: 0, vertical: 0, rotation: 5},
        {tile_id: "g8571", horizontal: 1, vertical: -1, rotation: 2},
        {tile_id: "g5188", horizontal: 2, vertical: 0, rotation: 0, player: default_players [1], paths:[{direction:5, fill: legality_fill.success [0]}]}
      ]),
    ),

    $("<p>").text ("When you finish a connection, you do something in real life. Some connections make the players get tied up. When you're too tied up to play your turns, you lose the game!"),
  
    $("<p>").text ("Connecting someone's torso or crotch to their other body parts makes them remove a piece of clothing."),
  
    $("<p>").text ("Connecting your own hands or feet to an opponent's body parts gives you a chance to stimulate that body part in some way. (Groping? Tickling? Slapping?) Players should talk before the game about what kind of stimulation they want."),
    navigation("instructions")
  );
}
function before_playing() {
  $("#menu").empty().scrollTop (0).append (
    $("<p>").text ("Ready to play a game with your partner(s)?"),
    $("<ul>", {class: "big_list"}).append (
      $("<li>").text ("Get plenty of things to tie people up with. (Rope? Handcuffs? Clothing?) Find a place to play with furniture nearby, where you could keep playing even if everyone has an arm or leg tied to it. Keep scissors nearby in case of emergencies. (Preferably medical scissors.)"),
    
      $("<li>").text ("Talk about what each of you wants. When it comes up in the game, what kind of stimulation do you want? What toys can be used on you? What do you want your partner(s) to do if you lose the game? (Untie you right away? Leave you tied up? Stimulate you more?)"),
  
      $("<li>").text (`Remember that any player can withdraw consent at any time, even if you planned to finish the game together. If you like to playfully protest, choose a safeword that means "stop" unambiguously. If someone speaks the safeword, stop and untie them right away.`),
  
      $("<li>").text ("Set up the players below and have fun!")
    ),
    make_game_setup_area (global_game && global_game.players_immutable || default_players.slice (0, 2)),
    navigation("start_game")
  );
}
function game_menu() {
  var save_box;
  $("#menu").empty().scrollTop (0).append (
    $("<p>").text ("Save string (copy this somewhere to save the game, or paste here to load one):"),
    save_box = $("<input>", {type: "text", value: save_game (global_game)}).click (function() {
      save_box[0].select();
    }).on("input", function() {
      var loaded = load_game (save_box.val());
      if (loaded) {
        restart_game (loaded);
        close_menu();
      }
    }),
    $("<p>").text ("The game also autosaves, although it will delete the autosave after four hours of not playing."),
    $("<input>", {type: "button", value: "End the game and delete your autosave"}).click (function() {
      restart_game (null);
      close_menu();
      show_menu();
    }),
    navigation("game_menu")
  );
}

function show_menu() {
  $("#content").append (global_menu = $("<div>", {id: "menu", class: global_game? "game_exists" : "no_game"}));
  global_game ? game_menu() : instructions();
}
function close_menu() {
  $("#menu").remove();
  global_menu = null;
}

var global_game;
var global_menu;
function autosave_game (game) {
  if (global_game) {
    localStorage.setItem ("hexy_autosave", save_game (game));
    localStorage.setItem ("hexy_autosave_date", Date.now());
  }
  else {
    delete_autosave ();
  }
}
function delete_autosave () {
  localStorage.removeItem ("hexy_autosave");
  localStorage.removeItem ("hexy_autosave_date");
}
function autoload_game () {
  undraw_game (global_game);
  global_game = null;
  var date = localStorage.getItem ("hexy_autosave_date");
  /*
elidupree 
[2 hours ago] I can assume that the players have sufficient privacy WHILE they are playing; I'm thinking about scenarios where an untrusted or semi-trusted person examines the device later, after the game.

elidupree 
[2 hours ago] 
Now, this might not be relevant if you merely don't want the attacker to know that you have BDSM interests at all; then you would delete your history and not show them

elidupree 
[2 hours ago] 
But the game data might also include the names of the players, and that might be an extra level of sensitive information

elidupree 
[2 hours ago] 
For instance, you could play it with one person and then want to play it with (or just show it to) another person who mustn't know that you played it with the first person for one reason or another

elidupree [2 hours ago] 
"The app deletes your autosave on load after 4 hours of not playing" would probably take care of that case
  */
  if (date && date > Date.now() - 1000*60*60*4) {
    var save = localStorage.getItem ("hexy_autosave");
    restart_game (load_game (save));
  }
  else {
    delete_autosave ();
  }
  //if (global_game === null) {restart_game(new_game (default_players.slice (0, 2))); }
}
function restart_game (new_game) {
  undraw_game (global_game);
  global_game = new_game;
  autosave_game (global_game);
}
function load_game (save) {
  var game = JSON.parse(save, (key, value) => {
    if (typeof value === "string") { return escape_string (value) }
    return value;
  });
  game.tiles = {};
  game.anchored_tiles.forEach(function(tile) {
    tile.player = game.players_immutable [tile.player];
    tile.icon = get_tile_icon (tile.tile_id);
    set_tile (game.tiles, tile);
  });
  return game;
}
function save_game (game) {
  return JSON.stringify(game, (key, value) => {
    if (typeof value==="string") {return unescape_string (value);}
    if (key === "tiles") {return undefined;}
    if (key === "icon") {return undefined;}
    if (key === "player" && value) {return value.index;}
    return value;
  });
}


function tick() {
  requestAnimationFrame (tick);
  
  if (global_game) {
    draw_game (global_game) ;
  }
  else if (!global_menu) {
    show_menu();
  }
}
autoload_game ();
tick();

