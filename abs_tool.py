#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import bars
import blog
	  
def add_page(page_dict):
  utils.make_page (page_dict,
    '/abs-tool',
      "ABS tool ⊂ Eli Dupree's website",
      r'''<style type="text/css">
html,body {background-color: white;}
#game {position: relative;}
.game_canvas {position: absolute; height: 100%; width: 100%;}
p {font-size: 200%; text-align: center;}
    </style> 
    <script type="text/javascript">
$(function() {
"use strict";

var turn = Math.PI*2;
var game_element = $("#game");
var top_bar = $(".top_bar");
var bottom_bar = $(".bottom_bar");
$(".bars_inner_box").css ("padding-bottom", 0);
//var body = $("body");
//game_element.height (600);

var canvas_element = $("<canvas>").addClass ("game_canvas")
game_element.append (canvas_element);
var canvas_context = canvas_element[0].getContext ("2d");

var frames_per_second = 60;


var game_height;
var game_width;
function update_dimensions() {
  var game_top = top_bar.offset().top + top_bar.height();
  var game_bottom = $(window).height() - bottom_bar.height();
  game_element.height (game_bottom - game_top);
  var width = game_element.width();
  var height = game_element.height();
  game_height = height;
  game_width = width;
  if (canvas_element.attr ("width") != width || canvas_element.attr ("height") != height) {
    canvas_element.attr ("width", width).attr ("height", height);
  }
}
update_dimensions();




function close_shape (fill, stroke) {
  canvas_context.closePath();
  if (fill) {canvas_context.fillStyle = fill;
  canvas_context.fill();}
  if (stroke) {canvas_context.strokeStyle = stroke;
  canvas_context.stroke();}
}


var start = Date.now();
var step = 0;

var position = 0;
var direction = 1;





function tick() {
  requestAnimationFrame (tick);
  step++;
  var updated = update_dimensions();
  var width = game_width;
  var height = game_height;
  var time = step/frames_per_second;//(Date.now() - start)/1000;  
  
  canvas_context.clearRect (0, 0, width, height);
  
  canvas_context.save();
  canvas_context.translate (width*0.05, height*0.05);
  canvas_context.scale (width*0.9, height*0.9);
  
  
  
  var cycles_per_frame = 0.5/frames_per_second;
  if (true||linear) {
    position = position + direction*4*cycles_per_frame;
    if (position*direction > 1) {
      position = direction*2 - position;
      direction *= -1;
    }
  }
  else {
    var new_angle = Math.asin (position*direction) + turn*cycles_per_frame;
    if (new_angle > turn/4) {
      new_angle -= turn/2;
      direction *= -1;
    }
    position = direction*Math.sin (new_angle);
  }
  
  canvas_context.beginPath();
  canvas_context.arc (0.5 + position/2, 0.5, 0.05, 0, turn, true);
  canvas_context.lineWidth = 0.001;
  
  close_shape ("rgb(0, 0, 0)", "rgb(0,0,0)");
  
  
  canvas_context.restore();  
}
tick();


});
    </script>''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''<main><div id="content">
      
      <p>I made this tool to help with ABS (alternating bilateral stimulation) therapy, but I have no expertise in it and only designed this based on third hand information. Use at your own risk!</p>
      <div id="game"></div>

    '''+
    # blog.comments_section ("the_path") +
    '''
  </div>
</main>'''), {
  "jQuery_before": True,
  "blurb": "A unfinished online tool.",
  #"blurb_image": "/media/pac-asteroids-thumbnail.png?rr"
}
  )
  