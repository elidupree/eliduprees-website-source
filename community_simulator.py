#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import bars
import blog
	  
def add_game(page_dict):
  utils.make_page (page_dict,
    '/games/community-simulator',
      "Community simulator ⊂ Eli Dupree's website",
      r'''<style type="text/css">
html,body {background-color: black;}
#game {position: relative;}
.game_canvas {position: absolute; height: 100%; width: 100%;}
.path_component {position: absolute; background-color: white; height: 1px; width: 10%;}
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
var interaction_distance = 0.05;


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



var mouse_X = 0;
var mouse_Y = 0;
game_element.mousemove (function (event) {
  var offset = game_element.offset();
  mouse_X = event.pageX - offset.left;
  mouse_Y = event.pageY - offset.top;
});


function close_shape (fill, stroke) {
  canvas_context.closePath();
  if (fill) {canvas_context.fillStyle = fill;
  canvas_context.fill();}
  if (stroke) {canvas_context.strokeStyle = stroke;
  canvas_context.stroke();}
}


function close_generic_shape () {
  canvas_context.lineWidth = 0.005;
  
  close_shape ("rgb(255, 255, 255)", "rgb(0,0,0)");
}




var resource_names = ["energy", "companionship"];


var people = [];
for (var index = 0; index <20;++index) {
  var resources = {};
  resource_names.forEach(resource => {
    resources [resource] = {immediate: Math.random(),};
  });
  people.push ({
    x: Math.random(),
    y: Math.random(),
    resources,
    relationships: {},
  });
}
people.forEach(function(person) {
  people.forEach(function(other) {
    if (other != person) {
      var resources = {};
      resource_names.forEach(resource => {
        resources [resource] = Math.random()*2-1;
      });
      person.relationships [other] = {received_resources: resources}
    }
  });
  
    person.heading = Math.random()*turn;
    person.y += 0.1/frames_per_second*Math.cos(person.heading) ;
    person.x += 0.1/frames_per_second*Math.sin (person.heading) ;
    draw_person (person);
});

function draw_person (person) {
  
  canvas_context.beginPath();
  canvas_context.arc (person.x, person.y, 0.05, 0, turn, true);
  canvas_context.lineWidth = 0.005;
  
  close_shape ("rgb("+Math.floor(255*person.resources.energy.immediate) +", 255, 255)", "rgb("+Math.floor(255*person.resources.companionship.immediate) +",0,0)");
}

function desire (person, other) {
  var relationship = person.relationships [other];
  var result = 0;
  resource_names.forEach(resource => {
    result += (1 - person.resources [resource].immediate)*relationship.received_resources [resource];
  });
  return result;
}






//resources.forEach(function(




var start = Date.now();
var step = 0;

function tick() {
  requestAnimationFrame (tick);
  step++;
  var updated = update_dimensions();
  var width = game_width;
  var height = game_height;
  var time = step/frames_per_second;//(Date.now() - start)/1000;  
  
  canvas_context.clearRect (0, 0, width, height);
  
  canvas_context.save();
  canvas_context.scale (width, height);
  
  people.forEach(function(person) {
    person.neighbors =[];
    person.avoidance = {x:0,y:0};
    var best;
    var best_desire;
    people.forEach(function(other) {
      if (other != person) {
        var whatever = desire (person, other);
        if (best === undefined || whatever >best_desire) {
          best = other;
          best_desire = whatever;
        }
        var distance = Math.sqrt ((person.x - other.x)*(person.x - other.x) + (person.y - other.y)*(person.y - other.y));
        if (distance <= interaction_distance*2) {
          var factor = Math.min (1, 2 - distance/interaction_distance);
          if (whatever <0) {
            var heading = Math.atan2 (other.y - person.y, other.x - person.x);
            person.avoidance.x += factor*whatever*Math.cos(heading);
            person.avoidance.y += factor*whatever*Math.sin(heading);
          }
        }
        if (distance <= interaction_distance) {
          person.neighbors.push (other);
          
        }
      }
    });
  
    person.heading = Math.atan2 (best.y - person.y, best.x - person.x);//Math.random()*turn;
  });
  people.forEach(function(person) {
    person.x += 0.1/frames_per_second*Math.cos(person.heading) ;
    person.y += 0.1/frames_per_second*Math.sin (person.heading) ;
    person.x += person.avoidance.x/frames_per_second;
    person.y += person.avoidance.y/frames_per_second;
    draw_person (person);
  });
  
  canvas_context.restore();  
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
