#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import bars
	  
def add_game(page_dict):
  utils.make_page (page_dict,
    '/games/green-caves',
      "Enter the green caves ⊂ Eli Dupree's website",
      r'''
    <style type="text/css">
html,body { height: 100%; margin: 0; padding: 0; background-color: #50d050 }
div,canvas { margin: 0; padding: 0; }
    </style>''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''<main>
      
    <div style="min-height: 50%;"><div style="min-height: 390px"></div></div><div style=" margin-top:-390px; text-align: center;">
      <p>You are surrounded by endless caves.</p>
      <p>Will you explore peacefully, doing as little damage as possible? Or will you destroy everything in sight?</p>
      <p>Arrow keys or WASD to move. Point and click to shoot.</p>
    </div>
    <div style="margin: 0 auto; width:640px; cursor: crosshair"><canvas id="game_canvas" width="804" height="600">
Your browser does not support the canvas element.
    </canvas></div>
    <!--<p id="info"></p>-->

   
</main>''')+''' <script type="text/javascript">
      Module = {};
      window.green_caves = {};
      window.green_caves.holding_mouse_down_ingame = false;
      Module.TOTAL_MEMORY = 100000000; // 100 MB, about six times the default
      Module.memoryInitializerPrefixURL = "/media/";
      Module.onRuntimeInitialized = function(){
"use strict";

var game_canvas = document.getElementById("game_canvas");

var h = GL.createContext(game_canvas, {});
if (h > 0) {
  window.green_caves.gl = true;
  GL.makeContextCurrent(h);
}
else {
  window.green_caves.gl = false;
  window.green_caves.canvas_context = game_canvas.getContext("2d");
}

/*  (function(window){
    var green_caves = {
      window.green_caves.canvas_context: game_canvas.getContext("2d"),
    };
    window.green_caves = green_caves;
  })(window);*/

  var canvas_rect = game_canvas.getBoundingClientRect();
  function update_canvas_rect() {
    canvas_rect = game_canvas.getBoundingClientRect();
    window._set_display_size(canvas_rect.right - canvas_rect.left, canvas_rect.bottom - canvas_rect.top, window.green_caves.gl);
  }
  update_canvas_rect();
  
  function mouse_xy_relative_to_top_left_of_canvas(mouseevent) {
    // bug?- assumes the event target is 'document'
    var mouse_screen_x = mouseevent.clientX;
    var mouse_screen_y = mouseevent.clientY;
    // compute this every time in case the window resizes/scrolls
    update_canvas_rect();
    var canvas_screen_top  = canvas_rect.top;
    var canvas_screen_left = canvas_rect.left;
    var mouse_canvas_x = mouse_screen_x - canvas_screen_left;
    var mouse_canvas_y = mouse_screen_y - canvas_screen_top;
    return { x: mouse_canvas_x, y: mouse_canvas_y };
  }
  
  var now_milliseconds = (function(){
    var now = new Date();
    return now.getTime();
  });
  var update = (function(){
    window._update_to_real_time(now_milliseconds());
  });

  // TODO make these events not update but instead insert
  // a fiat event at event.timeStamp
  var mousemove_while_mouse_down_ingame = function(e){
    var pos = mouse_xy_relative_to_top_left_of_canvas(e);
    window._mouse_moves(e.timeStamp, pos.x, pos.y);
    // prevent selecting text while aiming
    e.preventDefault();
  };
  document.addEventListener('mousedown', function(e){
    if(e.button == 0 && e.target == game_canvas) {
      // left-click in game area
      // (allow left-clicks elsewhere to do normal things like selecting text)
      window.green_caves.holding_mouse_down_ingame = true;
      document.addEventListener('mousemove', mousemove_while_mouse_down_ingame, false);
      var pos = mouse_xy_relative_to_top_left_of_canvas(e);
      window._mouse_down(e.timeStamp, pos.x, pos.y);
    }
  }, false);
  document.addEventListener('mouseup', function(e){
    if(e.button == 0 && window.green_caves.holding_mouse_down_ingame) {
      // release left-click
      window.green_caves.holding_mouse_down_ingame = false;
      document.removeEventListener('mousemove', mousemove_while_mouse_down_ingame, false);
      var pos = mouse_xy_relative_to_top_left_of_canvas(e);
      window._mouse_up(e.timeStamp, pos.x, pos.y);
    }
  }, false);
  document.addEventListener('keydown', function(e){
    var keycode = (e.keyCode ? e.keyCode : e.which);
    var keystr = String.fromCharCode(keycode);
    if (keycode === 37 || keystr === "A") { _set_left(e.timeStamp, true); e.preventDefault(); }
    if (keycode === 38 || keystr === "W") { _set_up(e.timeStamp, true); e.preventDefault(); }
    if (keycode === 39 || keystr === "D") { _set_right(e.timeStamp, true); e.preventDefault(); }
    if (keycode === 40 || keystr === "S") { _set_down(e.timeStamp, true); e.preventDefault(); }
  }, false);
  document.addEventListener('keyup', function(e){
    var keycode = (e.keyCode ? e.keyCode : e.which);
    var keystr = String.fromCharCode(keycode);
    if (keycode === 37 || keystr === "A") { _set_left(e.timeStamp, false); e.preventDefault(); }
    if (keycode === 38 || keystr === "W") { _set_up(e.timeStamp, false); e.preventDefault(); }
    if (keycode === 39 || keystr === "D") { _set_right(e.timeStamp, false); e.preventDefault(); }
    if (keycode === 40 || keystr === "S") { _set_down(e.timeStamp, false); e.preventDefault(); }
  }, false);
  
  var draw = (function(){
    update_canvas_rect();
    if (window.green_caves.gl) {
      
    }
    else {
      window.green_caves.canvas_context.fillStyle = "black";
      window.green_caves.canvas_context.fillRect(0,0,640,640);
    }
    window._draw(window.green_caves.gl);
  });
  
  var tick_finished = true;
  (function tickloop(){
    setTimeout(tickloop, 10);
    if (tick_finished) {
      tick_finished = false;
      update();
      draw();
      tick_finished = true;
    }
  }());

};
    </script>
    <script type="text/javascript" src="/media/green_caves.js?rr"></script>''', {}
  )
