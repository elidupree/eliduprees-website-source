"use strict";

var comments_area = $("#comments").detach().css("display", "block");

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
  lighter.red = Math.round(200-(200-lighter.red)/3);
  lighter.green = Math.round(200-(200-lighter.green)/3);
  lighter.blue = Math.round(200-(200-lighter.blue)/3);
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

function make_game_setup_area (initial_settings) {
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
        player_info.name_input = $("<input>", {type: "text", value: unescape_string (default_name), id: "player_name_" + default_name}).change (update_player_name)
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
  
  var mode_row = $("<div>", {class: "modes"});
  modes_list.forEach(function(id) {
    var mode = game_modes [id];
    mode_row.append ($("<div>", {class:"mode_box"}).append(
      $("<input>", {type: "radio", id: "mode_" + id, name: "mode", value: id, checked: initial_settings.mode === id}),
      $("<label>", {"for": "mode_" + id, text: mode.name + " (" + mode.description + ")"})
    )); 
  });
  
  var result = $("<div>", {class:"game_setup"}).append(
    mode_row,
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
    $("<input>", {type: "button", value: "Start game"}).css({display: "block", margin: "0.8em auto", "margin-bottom": "2.6em", "font-size": "180%", "font-weight": "bold"}).click (function() {
      if (players.length > 0) {
        var game = new_game ({players, mode: $("input:radio[name=mode]:checked").val()});
        close_menu();
        restart_game (game);
      }
    })
  );
  
  /*result.append (
    $("<input>", {type: "button", value: "Cancel"}).click (function() {
      result.remove();
    })
  );*/
  
  initial_settings.players.forEach(function(player) {
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
  if (current !== "connections") {result.append (
    $("<input>", {type: "button", value: "Connection effects"}).click (function() {
      connections();
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
  if (current !== "comments") {result.append (
    $("<input>", {type: "button", value: "Comments"}).click (function() {
      comments();
    })
  );}
  
  return result;
}

function instructions() {
  $("#menu").empty().scrollTop (0).append (
    $("<h1>").text ("Welcome to Hexy Bondage!"),
    $("<p>").html(`Hexy Bondage is a sexual game for two players (or more) to play together on the same device. It's based on <a href="/hexy-classic">a printable board game I designed four years earlier</a>.`),
    
    $("<p>").text ("This web game works best in Chrome. Firefox may have some display errors, and I haven't tested in other browsers."),
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
  
    $("<p>").text ("Other connections can make players remove clothing, have toys used on them, or allow other players to stimulate them in some way. (Groping? Tickling? Slapping?) Players should talk before the game about what kind of toys and stimulation they want."),
    
    navigation("instructions")
  );
}
function connections() {
  function orient (tile, direction) {
    tile.player = default_players [(get_tile_icon (tile.tile_id).color === "black")? 0:1];
    var connections = get_connections (tile.tile_id);
    for (tile.rotation = 0; tile.rotation <6 ;++tile.rotation) {
      var index = (direction + 6 - tile.rotation) % 6;
      if (connections [index] === icon) {
        tile.drawn_components = {[index]: true};
        break;
      }
    }
  }
  function connection (first, second) {
    first = {tile_id: first, horizontal: 0, vertical: -2};
    second = {tile_id: second, horizontal: 0, vertical: 2, paths:[{direction:0, fill: legality_fill.success [0]}]};
    orient (first, 3);
    orient (second, 0);
        
    return draw_fake_board ([
        first,
        {tile_id: "g8043", horizontal: 0, vertical: 0, rotation: 0, drawn_components: {[0]: true, [3]: true}},
        second
    ])
  }
  function connection_type (description, pairs) {
    var boards = $("<div>", {class: "fake_boards"});
    var area = $("<div>", {class: "connection_type"});
    area.append ($("<p>").html(description));
    area.append (boards);
    pairs.forEach(function(pair) {
      boards.append (connection (pair[0], pair[1]));
    });
    $("#menu").append (area);
  }
  $("#menu").empty().scrollTop (0).append (
    $("<h1>").text ("If you connect…")
  );
  connection_type ("Any body part to furniture: Tie that body part to a piece of furniture.", [["g5084", "g5265"], ["g5273", "g5265"], ["g4979", "g6990"]]);
  connection_type ("A player's hand to any other hand: Tie that player's hands together in front of them. (Left/right doesn't matter, and if you connect two different player's hands, <em>both</em> players get their hands tied.) If a player would get their hands tied a second time, re-tie their hands behind them.", [["g5305", "g5317"], ["g5035", "g5200"], ["g5016", "g5225"]]);
  connection_type ("A player's foot to any other foot: Tie that player's feet together.", [["g6913", "g5092"], ["g5051", "g5088"], ["g6924", "g7012"]]);
  connection_type ("A player's hand to the <em>same</em> player's foot: Tie exactly those two body parts together.", [["g5084", "g4975"], ["g4988", "g5024"], ["g5209", "g5384"]]);
  connection_type ("A player's hand/foot to a <em>different</em> player's torso, crotch, or foot: The first player gets a chance to use their hands/feet to stimulate the other body part.", [["g5301", "g5180"], ["g5285", "g5257"], ["g5028", "g5196"]]);
  connection_type ("A player's body part to a toybox: That player must choose a toy to be used on them. (Insert a dildo? Attach nipple clamps? Put on a collar?)", [["g5337", "g7382"], ["g5273", "g5136"], ["g7325", "g6990"]]);
  connection_type ("A player's torso/crotch to anything that doesn't have some other effect: That player removes a piece of clothing from that area. (If you connect the same player's torso and crotch together, they choose what to remove.).", [["g5020", "g5112"], ["g7155", "g5043"], ["g5104", "g5269"]]);
  $("#menu").append (
    $("<div>", {class: "connection_type"}).append (
    $("<p>").html("Any icons through a lock: Tie all those things together, regardless of the normal connection rules. Be creative. (If you're tied to another player, you still have to let them play their turns, as long as it's physically possible. Also, locks currently aren't included in corridor mode)"),
    $("<div>", {class: "fake_boards"}).append (
      draw_fake_board ([
        {tile_id: "g5096", horizontal: 2, vertical: 0, rotation: 1, player: default_players [1]},
        {tile_id: "g7166", horizontal: 0, vertical: 2, rotation: 1, player: default_players [1]},
        {tile_id: "g5172", horizontal: 2, vertical: 2, rotation: 0, player: default_players [0]},
        {tile_id: "g5265", horizontal: -1, vertical: -1, rotation: 5},
        {tile_id: "g8571", horizontal: 1, vertical: -1, rotation: 2},
        {tile_id: "g8261", horizontal: 1, vertical: 1, rotation: 1},
        {tile_id: "g10573", horizontal: 0, vertical: 0, rotation: 1, paths:[{direction:5, fill: legality_fill.success [0]}]}
      ]),
    )
    ),
    navigation("connections")
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
    make_game_setup_area (global_game && global_game.settings || {mode: "corridor", players: default_players.slice (0, 2)}),
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
    $("<p>").text ("The game also autosaves, although it will delete the autosave after four hours of not playing." + (global_game.autosave_failed? " (Also, the autosave is not currently working, possibly because your browser is forbidding local storage to be set.)": "")),
    $("<input>", {type: "button", value: "End the game and delete your autosave"}).click (function() {
      restart_game (null);
      close_menu();
      show_menu();
    }),
    navigation("game_menu")
  );
}

function comments() {
  $("#menu").empty().scrollTop (0).append (
    navigation("comments"),
    
    $("<h1>").text ("Comments"),
    comments_area,
    
    navigation("comments"),
  );
}

function show_menu() {
  $("#content").append (
    $("<div>", {id: "menu_wrapper"}).css ("top", top_bar.outerHeight()).click (function(event) {if (global_game) {event.stopPropagation(); close_menu();}})
    .append (
      global_menu = $("<div>", {id: "menu", class: global_game? "game_exists" : "no_game"}).click (event => event.stopPropagation())
    )
  );
  global_game ? game_menu() : instructions();
}
function close_menu() {
  $("#menu_wrapper").remove();
  global_menu = null;
}

var global_game;
var global_menu;
function autosave_game (game) {
  if (global_game) {
    try {
      localStorage.setItem ("hexy_autosave", save_game (game));
      localStorage.setItem ("hexy_autosave_date", Date.now());
      delete global_game.autosave_failed;
    }
    catch (exception) {
      global_game.autosave_failed = true;
    }
  }
  else {
    delete_autosave ();
  }
}
function delete_autosave () {
  try {
    localStorage.removeItem ("hexy_autosave");
    localStorage.removeItem ("hexy_autosave_date");
  } catch (exception) {}
}
function autoload_game () {
  undraw_game (global_game);
  global_game = null;
  try {
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
  } catch (exception) {}
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
    tile.player = game.settings.players [tile.player];
    tile.icon = get_tile_icon (tile.tile_id);
    set_tile (game.tiles, tile);
  });
  if (game.floating_tile) {
    var tile = game.floating_tile;
    tile.player = game.settings.players [tile.player];
    tile.icon = get_tile_icon (tile.tile_id);
  }
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

