"use strict";


var global_game;
function autosave_game (game) {
  localStorage.setItem ("hexy_bondage_autosave", JSON.stringify(game));
}
function autoload_game () {
  undraw_game (global_game);
  var save = localStorage.getItem ("hexy_bondage_autosave");
  global_game = JSON.parse(save);
  if (global_game === null) {restart_game(); }
}
function restart_game () {
  undraw_game (global_game);
  global_game = new_game ([
      {based_on: "white", name: "White", fill: "#ffffff", stroke: "#000000"},
      {based_on: "black", name: "Black", fill: "#000000", stroke: "#ffffff"},
      /*{based_on: "white", name: "Pink", fill: "#ffaaff", stroke: "#ff00ff"},
      {based_on: "white", name: "Green", fill: "#99ff99", stroke: "#008800"},
      {based_on: "black", name: "Blue", fill: "#0000ff", stroke: "#ffffff"},
      {based_on: "black", name: "Purple", fill: "#5500aa", stroke: "#ffffff"},*/
    ]);
  autosave_game (global_game);
}


function tick() {
  requestAnimationFrame (tick);
  
  draw_game (global_game) ;
}
autoload_game ();
tick();

