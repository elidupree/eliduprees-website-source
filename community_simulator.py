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



var resource_names = ["energy", "companionship"];
var default_speed = 0.1;
var person_radius = 0.04;
var interaction_distance = person_radius*2.2;
//var comfort_distance = person_radius*1.6;
var resource_decay = 1/10;




var people = [];
for (var index = 0; index <20;++index) {
  var resources = {};
  resource_names.forEach(resource => {
    resources [resource] = {immediate: Math.random(),};
  });
  people.push ({
    index: index,
    x: Math.random(),
    y: Math.random(),
    resources,
    relationships: {},
  });
}
people.forEach(function(person) {
  people.forEach(function(other) {
    if (other !== person) {
      var resources = {};
      resource_names.forEach(resource => {
        resources [resource] = Math.random()*2-1;
      });
      person.relationships [other.index] = {received_resources: resources}
    }
  });
  
    /*person.heading = Math.random()*turn;
    person.y += default_speed/frames_per_second*Math.cos(person.heading) ;
    person.x += default_speed/frames_per_second*Math.sin (person.heading) ;
    draw_person (person);*/
});





function draw_person (person) {
  
  canvas_context.beginPath();
  canvas_context.arc (person.x, person.y, person_radius* 0.95, 0, turn, true);
  canvas_context.lineWidth = person_radius* 0.1;
  
  close_shape ("rgb("+Math.floor(255*person.resources.energy.immediate) +", 255, 255)", "rgb("+Math.floor(255*person.resources.companionship.immediate) +",0,0)");
  
  var relationship = person.relationships [person.best.index];
  canvas_context.beginPath();
  canvas_context.moveTo(person.x, person.y);
  canvas_context.lineTo(person.x+ person_radius* 0.5*Math.cos(person.heading), person.y+ person_radius* 0.5*Math.sin(person.heading));
  canvas_context.strokeStyle = "rgb("+Math.floor(255*relationship.received_resources.companionship) +",0,0)";
  canvas_context.stroke();
  
}

function desire (person, other) {
  var relationship = person.relationships [other.index];
  var result = 0;
  resource_names.forEach(resource => {
    result += (1 - person.resources [resource].immediate)*relationship.received_resources [resource];
  });
  //console.log(result);
  return result / resource_names.length;
}

function interact (person, other) {
  var relationship = person.relationships [other.index];
  resource_names.forEach(resource => {
    person.resources [resource].immediate += relationship.received_resources [resource]/frames_per_second;
    if (person.resources [resource].immediate <0) {
      person.resources [resource].immediate = 0;
    }
    if (person.resources [resource].immediate >1) {
      person.resources [resource].immediate = 1;
    }
  });
}
function time_passes (person) {
  resource_names.forEach(resource => {
    person.resources [resource].immediate -= resource_decay/frames_per_second;
    if (person.resources [resource].immediate <0) {
      person.resources [resource].immediate = 0;
    }
  });
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
  canvas_context.translate (width*0.05, height*0.05);
  canvas_context.scale (width*0.9, height*0.9);
  
  
  people.forEach(function(person) {
    person.neighbors =[];
    person.avoidance = {x:0,y:0};
    var best;
    var best_desire;
    people.forEach(function(other) {
      if (other !== person) {
        var whatever = desire (person, other);
        var distance = Math.sqrt ((person.x - other.x)*(person.x - other.x) + (person.y - other.y)*(person.y - other.y));
        var heading = Math.atan2 (other.y - person.y, other.x - person.x);
        
        if ((best === undefined) || (whatever >best_desire)) {
          person.best = best = other;
          best_desire = whatever;
          person.best_distance = distance;
        }
        
        if (distance <= interaction_distance*2) {
          var factor = Math.min (1, 2 - distance/interaction_distance);
          //if (whatever <0) {
            person.avoidance.x += factor*whatever*Math.cos(heading);
            person.avoidance.y += factor*whatever*Math.sin(heading);
          //}
        }
        if (distance <= interaction_distance) {
          person.neighbors.push (other);
        }
        if (distance < person_radius*2) {
          var factor = 2*(1 - distance/(person_radius*2));
          person.avoidance.x -= factor*Math.cos(heading);
          person.avoidance.y -= factor*Math.sin(heading);
        }
      }
    });
  
    person.heading = Math.atan2 (best.y - person.y, best.x - person.x);//Math.random()*turn;
  });
  people.forEach(function(person) {
    var speed = default_speed*desire (person, person.best);
    person.x += speed/frames_per_second*Math.cos(person.heading) ;
    person.y += speed/frames_per_second*Math.sin (person.heading) ;
  });
  people.forEach(function(person) {
    person.neighbors.forEach(function(other) {
      interact (person, other);
    });
    time_passes (person);
    
    var max_avoidance = default_speed*3;
    var current_avoidance = Math.sqrt ((person.avoidance.x)*(person.avoidance.x) + (person.avoidance.y)*(person.avoidance.y));
    if (current_avoidance >max_avoidance) {
      person.avoidance.x *= max_avoidance/current_avoidance;
      person.avoidance.y *= max_avoidance/current_avoidance;
    }
    

    
    person.x += person.avoidance.x/frames_per_second;
    person.y += person.avoidance.y/frames_per_second;
    if (person.x <0) {person.x = 0 + (person.x - 0)*0.5;}
    if (person.x >1) {person.x = 1 + (person.x - 1)*0.5;}
    if (person.y <0) {person.y = 0 + (person.y - 0)*0.5;}
    if (person.y >1) {person.y = 1 + (person.y - 1)*0.5;}
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
  