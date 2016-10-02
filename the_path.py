#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import bars
import blog
	  
def add_game(page_dict):
  utils.make_page (page_dict,
    '/games/the-path',
      "The Path ⊂ Eli Dupree's website",
      r'''<style type="text/css">
html,body {background-color: black;}
#game {position: relative;}
.game_canvas {position: absolute; height: 100%; width: 100%;}
.path_component {position: absolute; background-color: white; height: 1px; width: 10%;}
    </style> 
    <script type="text/javascript">
$(function() {
"use strict";

var game_element = $("#game");
var top_bar = $(".top_bar");
var bottom_bar = $(".bottom_bar");
$(".bars_inner_box").css ("padding-bottom", 0);
//var body = $("body");
//game_element.height (600);
var canvas_element = $("<canvas>").addClass ("game_canvas")
game_element.append (canvas_element);
var canvas_context = canvas_element[0].getContext ("2d");

var visible_path_components = 600;
var seconds_to_travel_visible = 10;
var path_components_per_second = visible_path_components/seconds_to_travel_visible;
var frames_per_second = 60;
var path_components_per_frame = path_components_per_second/frames_per_second;
var player_max_speed = 0.1; // in screens per second

var game_height;
var game_width;
function linear_height (component_index) {
  return game_element.height() *(1-component_index/visible_path_components);
}
function cylindrical_height (component_index) {
  return game_height - Math.sin (component_index/visible_path_components*(Math.PI/2))*game_height/(Math.PI/2);
}
var perspective_height = cylindrical_height;

var player = {position: 0};
var paths = [{info: {max_speed: player_max_speed}, data: [{position: 0, velocity: 0, acceleration: 0, element: $("<div/>") .addClass ("path_component")}]}];

var mouse_X = 0;
var mouse_Y = 0;
game_element.mousemove (function (event) {
  var offset = game_element.offset();
  mouse_X = event.pageX - offset.left;
  mouse_Y = event.pageY - offset.top;
});

function tick() {
  requestAnimationFrame (tick);
  
  var game_top = top_bar.offset().top + top_bar.height();
  var game_bottom = $(window).height() - bottom_bar.height();
  game_element.height (game_bottom - game_top);
  var width = game_element.width();
  var height = game_element.height();
  game_height = height;
  game_width = width;
  paths.forEach (function(path) {
    while (path.data.length <visible_path_components) {
      var previous = path.data [path.data.length - 1];
      var current = {
        position: previous.position + previous.velocity/path_components_per_second,
        velocity: previous.velocity + previous.acceleration/path_components_per_second,
      };
      var max_speed =path.info.max_speed;
      
      var default_change_radius = max_speed*2.16/path_components_per_second;
      var bias = -previous.velocity*0.36/path_components_per_second;
      var max_acceleration = Math.min (previous.acceleration + default_change_radius + bias, (max_speed - previous.velocity)*20);
      var min_acceleration = Math.max (previous.acceleration - default_change_radius + bias, (-max_speed - previous.velocity)*20);
      current.acceleration = min_acceleration +Math.random()*(max_acceleration - min_acceleration);
      
      
      // What jerk do we need to stop velocity from
      //
      // the maximum acceleration makes the (velocity, time) curve a parabola that touches the maximum velocity line and has its time^2 coefficient based on the minimum jerk (which is negative).
      // I.e. velocity = acceleration*time + (minimum jerk/2)*time ^2, solve for acceleration
      // given that velocity = previous.velocity when acceleration = previous.acceleration
      //
      // acceleration = previous.velocity/time - (minimum jerk/2)*time
      //
      // previous.velocity = previous.acceleration*time + (minimum jerk/2)*time ^2
      // (minimum jerk/2)*time ^2 + previous.acceleration*time - previous.velocity = 0
      // time =
      
            
      //if (current.velocity >max_speed){current.velocity = max_speed;}
      //if (current.velocity <-max_speed){current.velocity = -max_speed;}
      //current.element = $("<div/>") .addClass ("path_component");
      //game_element.append (current.element);
      path.data.push (current);
    }
    //console.log (path.data [0]);
    
    //TODO: avoid rounding error if we adjust the values
    var deleted;
    for (var i=0;i<path_components_per_frame;++i){
      deleted = path.data.shift();
      //deleted.element.detach();
    }
    
    // you can't get TOO far away from the paths.
    // TODO: possibly better symbolism and gameplay if the paths stay near YOU instead
    if (player.position - deleted.position > 0.5) {
      player.position -= (player.position - deleted.position - 0.5)*3/600/paths.length;
    }
    if (player.position - deleted.position < -0.5) {
      player.position -= (player.position - deleted.position + 0.5)*3/600/paths.length;
    }
    
    var component_width = function (index) {
      return width*0.15*(visible_path_components - index)/visible_path_components; // * Math.sqrt ((1 + Math.abs (current.velocity)*width/(height/visible_path_components)));
    };
    canvas_element.attr ("width", width).attr ("height", height);
    canvas_context.fillStyle = "rgb(0,0,0)";
    canvas_context.fillRect (0, 0, width, height);
    canvas_context.fillStyle = "rgb(255, 255, 255)";
    canvas_context.beginPath();
    var began = false;
    var center_X = function (component, index) {return width*((component.position - player.position)*(visible_path_components - index)/visible_path_components+ 0.5);};
    path.data.forEach (function(current, index) {
     
      //current.element.css ("bottom", index).css ("left", game_element.width()*(current.position - deleted.position +0.45));
      
      if (began) {
        canvas_context.lineTo(center_X (current, index) -component_width (index)/2, perspective_height (index));
      }
      else {
        canvas_context.moveTo(center_X (current, index) -component_width (index)/2, perspective_height (index));
        began = true;
      }
      
    });
    for (var index = path.data.length - 1; index >= 0; index -= 1){
      var current = path.data [index];
      canvas_context.lineTo(center_X (current, index) +component_width (index)/2, perspective_height (index));
    }
    canvas_context.fill();
  });
  
  var player_velocity_request = Math.max (-1, Math.min (1, ((mouse_X/width) - 0.5)*10));
  player.position += player_velocity_request*player_max_speed/frames_per_second;
  
  canvas_context.beginPath();
  canvas_context.moveTo(width*0.47, height - 20);
  canvas_context.lineTo(width*0.53, height - 20);
  canvas_context.lineTo(width*0.5, height - width*0.06);
  canvas_context.closePath();
  canvas_context.fill();
  canvas_context.strokeStyle = "rgb(0,0,0)";
  canvas_context.stroke();
  
}
tick();


});
    </script>''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''<main><div id="content">
      
      <div id="game"></div>

    '''+
    # blog.comments_section ("the_path") +
    '''
  </div>
</main>'''), {
  "jQuery_before": True,
  "blurb": "A unfinished online game.",
  #"blurb_image": "/media/pac-asteroids-thumbnail.png?rr"
}
  )
