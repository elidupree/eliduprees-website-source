#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import bars
import blog
	  
def add_game(page_dict):
  (head, body) = utils.import_html ("vendor/the_path.html")
  utils.make_page (page_dict,
    '/games/the-path-prototype-2',
      "The Path ⊂ Eli Dupree's website",
      head,
      body, {"blurb": "An unfinished online game.", "after_body":'''
    <script type='text/javascript' src="/media/paper-core.min.js?rr"></script>
    <script type='text/javascript' src="/media/the_path.js?rr"></script>
  '''}
  )

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

var turn = Math.PI*2;
var game_element = $("#game");
var top_bar = $(".top_bar");
var bottom_bar = $(".bottom_bar");
$(".bars_inner_box").css ("padding-bottom", 0);
//var body = $("body");
//game_element.height (600);
var background_element = $("<canvas>").addClass ("game_canvas")
game_element.append (background_element);
var background_context = background_element[0].getContext ("2d");
var canvas_element = $("<canvas>").addClass ("game_canvas")
game_element.append (canvas_element);
var canvas_context = canvas_element[0].getContext ("2d");

var visible_path_components = 1200;
var seconds_to_travel_visible = 20;
var path_components_per_second = visible_path_components/seconds_to_travel_visible;
var frames_per_second = 60;
var path_components_per_frame = path_components_per_second/frames_per_second;
var player_max_speed = 0.1; // in screens per second
var thing_start_distance = 0.8;

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
    background_element.attr ("width", width).attr ("height", height);
  }
}
update_dimensions();

var horizon =function() {
    return game_height - game_height/(Math.PI/2);
  };
var flat = {
  height: function (distance) {
    return horizon() + (game_height - horizon()) *(1-distance);
  },
  scale: function (distance) {
    return 1;
  }
}
var cylindrical_fake = {
  height: function (distance) {
    return game_height - Math.sin (distance*(Math.PI/2))*game_height/(Math.PI/2);
  },
  scale: function (distance) {
    return 1 - distance;
  },
}
var linear = function (scale) {return {
  height: function (distance) {
    return horizon() + Math.exp (- scale*distance)*(game_height - horizon());
  },
  scale: function (distance) {
    return Math.exp (- scale*distance);
  },
};};
var hybrid;
hybrid = function (scale) {
  var specific_linear = linear (scale);
  return {
  height: function (distance) {
    return cylindrical_fake.height (distance)*distance + specific_linear.height (distance)*(1 - distance);
  },
  scale: function (distance) {
    return cylindrical_fake.scale (distance)*distance + specific_linear.scale (distance)*(1 - distance);
  },
};};
var cylindrical_real = function (camera_distance, angle_range) {
  function get_coordinates(distance) {
    return [
      camera_distance - Math.sin (angle_range*(1 - distance)),
      1 - Math.cos (angle_range*(1 - distance))
    ];
  }
  function get_camera_distance (coordinates) {
    var Delta_X = coordinates [0];
    return Math.sqrt (Delta_X*Delta_X + coordinates [1]*coordinates [1]);
  }
  function get_drop (coordinates) {
    return Math.atan2 (coordinates [1], coordinates [0]);   
  }
  var distance_factor = get_camera_distance (get_coordinates (0));
  var drop_factor = get_drop (get_coordinates (0));
return {
  height: function (distance) {
    var coordinates = get_coordinates (distance);
    var drop = get_drop (coordinates);
    return horizon() + (game_height - horizon()) *drop/drop_factor;
  },
  scale: function (distance) {
    return distance_factor/get_camera_distance (get_coordinates (distance));
  },
};};

var perspective = cylindrical_real (.11, .1);//hybrid (seconds_to_travel_visible/10);

var default_path = {info: {max_speed: player_max_speed}, data: [{position: 0, velocity: 0, acceleration: 0, element: $("<div/>") .addClass ("path_component")}]};
var player = {kind: "person", position: 0, distance: 0.08, radius: 0.02, speech: []};
var companion = {kind: "person", position: 0, distance: 0.01, radius: 0.025, speech: [], path: default_path,
pronouncements: [
  {text: "Don't stray from the path", delay_from_same: 100, delay_from_any: 5, automatically_at_distance: [0.9,1.1]},
  {text: "It's dangerous out there", delay_from_same: 100, delay_from_any: 5, automatically_at_distance: [2,1000]}
  
]};
var paths = [default_path];
var hills = [];
var skies = [];
var stuff = [];
stuff.push (player); stuff.push (companion);

function draw_position (position, distance) {
  var scale = perspective.scale (distance);
  return game_width*((position - player.position)*scale + 0.5);
}
function draw_at (position, distance) {
  canvas_context.save();
  var scale = perspective.scale (distance);
  var height = perspective.height (distance);
  canvas_context.translate (draw_position (position, distance), height);
  canvas_context.scale (scale, scale);
}

for (var index = 0; index < 15; index++){
  skies.push ({peak: Math.random(), height: Math.random(), steepness: Math.random()*0.1+0.1});
}
function hill_step(draw) {
  var hill_scale = 30;
  if (Math.random() < 1.6/frames_per_second) {
    var hill = {position: player.position + (Math.random ()*2 - 1)*70, height: Math.random()*0.1 + 0.1, radius: Math.random()*0.2 + 0.2, age: 0};
    if ((hill.position-player.position)/hill_scale+ hill.radius <0 || (hill.position-player.position)/hill_scale - hill.radius >0) {
      hills.push (hill);
    }
  }
  
  hills = hills.filter (function (hill) {
    hill.age += 1/frames_per_second;
    if (draw) {
      var peak_height = horizon() - (hill.height * Math.sin ((hill.age/50)*turn/4))*game_height;
      var base_height = peak_height + hill.height*game_height;
      var center = game_width*((hill.position - player.position)/hill_scale + 0.5);
      var radius = game_width*hill.radius;
      
      background_context.beginPath();
      background_context.moveTo(center - radius, base_height);
      background_context.lineTo (center, peak_height);
      background_context.lineTo (center + radius, base_height);
      background_context.fillStyle = "rgb(0, 0, 0)";
      background_context.fill();
    }
    
    return hill.age < 100;
  });
}
for (var index = 0; index < 200*frames_per_second; index++){
  hill_step (false);
}

var mouse_X = 0;
var mouse_Y = 0;
game_element.mousemove (function (event) {
  var offset = game_element.offset();
  mouse_X = event.pageX - offset.left;
  mouse_Y = event.pageY - offset.top;
});

function speech_bubble (text, direction, alpha) {
  canvas_context.save();
  if (direction) {canvas_context.scale (-1, 1);}
  var text_height = Math.min (22, game_width/32);

  canvas_context.font = text_height +"px Arial, Helvetica, sans-serif";
  canvas_context.textBaseline = "middle";
  var text_width = canvas_context.measureText (text).width;
  var padding = Math.max (text_height/2, text_width/13);
  var text_middle = -16-padding - text_height/2;
  var text_top = text_middle-text_height/2;
  var text_bottom = text_middle+text_height/2;
  canvas_context.beginPath();
  canvas_context.moveTo (0,0);
  canvas_context.quadraticCurveTo (17,-5,17, text_bottom + padding);
  canvas_context.quadraticCurveTo (-padding, text_bottom + padding,-padding, text_middle);
  canvas_context.quadraticCurveTo (-padding,text_top - padding, text_width/2, text_top - padding);
  canvas_context.quadraticCurveTo (text_width+padding, text_top - padding, text_width + padding, text_middle);
  canvas_context.quadraticCurveTo (text_width+padding, text_bottom + padding, 30, text_bottom + padding);
  canvas_context.quadraticCurveTo (30,-5,0,0);
  canvas_context.closePath();
  canvas_context.fillStyle = "rgba(255, 255, 255,"+ alpha +")";
  canvas_context.fill();
  canvas_context.strokeStyle = "rgba(0,0,0,"+ alpha +")";
  canvas_context.stroke();
  canvas_context.fillStyle = "rgba(0, 0, 0,"+ alpha +")";
  
  if (direction) {
    canvas_context.scale (-1, 1);
    canvas_context.translate (-text_width, 0);
  }
  canvas_context.fillText (text, 0, text_middle);
  canvas_context.restore();
}

function polygon (points, fill, stroke) {
  canvas_context.beginPath();
  canvas_context.moveTo(points [0], points [1]);
  for (var index = 2; index <points.length; index += 2){
    canvas_context.lineTo(points [index], points [index + 1]);
  }
  close_shape(fill, stroke);
}

function generic_polygon (points) {
  canvas_context.beginPath();
  canvas_context.moveTo(points [0], points [1]);
  for (var index = 2; index <points.length; index += 2){
    canvas_context.lineTo(points [index], points [index + 1]);
  }
  close_generic_shape();
}

function close_shape (fill, stroke) {
  canvas_context.closePath();
  if (fill) {canvas_context.fillStyle = fill;
  canvas_context.fill();}
  if (stroke) {canvas_context.strokeStyle = stroke;
  canvas_context.stroke();}
}


function close_generic_shape () {
  close_shape ("rgb(255, 255, 255)", "rgb(0,0,0)");
}


function draw_person (person) {
  //draw_at (person.position, person.distance);
  //var center = game_width*((person.position - player.position)*perspective.scale (person.distance) + 0.5);
  var center = 0;
  var radius = game_width*person.radius;
  var body_height = - radius*2/3;
  var leg_height = - radius;
  var offset = Math.sin (Date.now()*turn/900)*radius/4;
  if (person.falling_down) {canvas_context.rotate (turn/4);}
  generic_polygon ([
    center - radius/8, leg_height - offset,
    center - radius*2/3, leg_height - offset,
    center - radius*11/24, leg_height - offset + radius
  ]);
  generic_polygon ([
    center + radius/8, leg_height + offset,
    center + radius*2/3, leg_height + offset,
    center + radius*11/24, leg_height + offset + radius
  ]);
  generic_polygon ([
    center - radius, body_height,
    center + radius, body_height,
    center, body_height - 2*radius
  ]);
  canvas_context.beginPath();
  canvas_context.arc (center, body_height - 1.7*radius, radius*0.7, 0, turn, true);
  close_generic_shape();
  //canvas_context.restore();
}

function draw_speech (person) {
  var scale = perspective.scale (person.distance);
  var reference_position = draw_position (person.position, person.distance);
  var radius = game_width*person.radius*scale;
  
  person.speech = person.speech.filter (function(speech) {
    speech.age += 1/frames_per_second;
    if (speech.age >= 3.5) {return false;}
    
    if (speech.age >1.0 && speech.response) {
      speech.response.age = 0;
      speech.response.person.speech.push (speech.response);
      speech.response = undefined;
    }
    
    var distortion = 0;
    if (speech.age < 0.25) {distortion = (0.25 - speech.age)*4;}
    if (speech.age > 3.25) {distortion = (3.25 - speech.age)*4;}
    
    if (reference_position <game_width/3) {speech.direction = false;}
    if (reference_position >game_width*2/3) {speech.direction = true;}
    var speech_position = reference_position + (speech.direction && -1 || 1)* radius;
    if (!speech.direction) {speech_position = Math.max (speech_position, 5);}
    if (speech.direction) {speech_position = Math.min (speech_position, game_width - 5);}
    
    canvas_context.save();
    canvas_context.translate(speech_position, perspective.height (person.distance) - radius*2/3 - 1.7*radius);
    canvas_context.rotate (distortion*turn/17);
    speech_bubble (speech.text, speech.direction, 1.0 - Math.abs (distortion));
    canvas_context.restore();
    return true;
  });
}

function draw_tree (thing) {
  var center = 0;
  var radius = game_width*thing.radius;

  var tree_color = "rgb(70, 70, 70)"
  polygon ([
    center - radius*0.3, 0,
    center + radius*0.3, 0,
    center, - 2*radius
  ],tree_color);
  polygon ([
    center - radius, - radius,
    center + radius, - radius,
    center, - 2.8*radius
  ],tree_color);
  polygon ([
    center - radius*0.8, - 2*radius,
    center + radius*0.8, - 2*radius,
    center, - 3.5*radius
  ],tree_color);
}
function draw_thing (thing) {
  draw_at (thing.position, thing.distance);
  canvas_context.globalAlpha = (thing_start_distance - thing.distance)/0.2;
  
  if (thing.kind == "tree") {draw_tree (thing);}
  if (thing.kind == "person") {draw_person (thing);}
  if (thing.kind == "reward") {
    var points = [];
    var radius = game_width*thing.radius;
    var progress = thing.receiving || 0;
    var offset = - (radius*(1 + 2*progress));
    canvas_context.globalAlpha = Math.min (1, 10 - progress*10);
    for (var index = 0; index <5;++index) {
      points.push (radius*Math.sin (turn*(progress + index/5)));
      points.push (offset - radius*Math.cos (turn*(progress + index/5)));
      points.push (radius*Math.sin (turn*(progress + 0.1 + index/5))/Math.sqrt (5));
      points.push (offset - radius*Math.cos (turn*(progress + 0.1 + index/5))/Math.sqrt (5));
    }
    generic_polygon (points);
  }
  if (thing.kind == "box") {
    var radius = game_width*thing.radius;
    var progress = thing.receiving || 0;
    canvas_context.globalAlpha = Math.min (1, 1 - progress*1);
    canvas_context.beginPath();
    canvas_context.rect (- radius, - radius*1.6, radius*2, radius*1.6);
    canvas_context.fillStyle = "rgb(255, 255, 255)";
    canvas_context.fill();
    canvas_context.strokeStyle = "rgb(0, 0, 0)";
    canvas_context.stroke();

  canvas_context.font = 24+"px Arial, Helvetica, sans-serif";
  canvas_context.textBaseline = "middle";
  canvas_context.textAlign = "center";
  canvas_context.translate (0, - radius*0.8);
  canvas_context.scale (radius/24, radius/24);
  canvas_context.fillStyle = "rgb(0, 0, 0)";
  canvas_context.fillText ("?", 0, 0);

  }
  if (thing.kind == "monster") {
    var radius = game_width*thing.radius;
    var progress = thing.receiving || 0;
    generic_polygon ([- radius*0.8, 0, radius*0.8, 0, 0, - radius*1.6]);
    for (var index = 0; index <3;++index) {
      for (var direction= -1; direction<=1;direction+=2) {
        var height = (0.2 + index/3);
        var tips = (thing.attacking !== undefined) && (1-thing.attacking*1.5) || 1;
        canvas_context.beginPath();
        canvas_context.moveTo (radius*direction/3, - radius*(height+0.8));
        canvas_context.quadraticCurveTo (radius*direction, - radius*(height+0.6), radius*direction*tips, - radius*height);
        canvas_context.quadraticCurveTo (radius*direction*0.84, - radius*(height+0.4), radius*direction/3, - radius*(height+0.2));
        close_generic_shape();
      }
    }
  }

  
  canvas_context.restore();
}

function closest_component (path, distance) {
  return path.data [Math.floor (distance*visible_path_components)];
}
var path_radius = 0.12;
function normalized_distance_from (path, person) {
  return Math.abs (person.position - closest_component (path, person.distance).position)/path_radius;
}

var start = Date.now();
var step = 0;
var pause_next_frame = false;
var permanent_pain = 0.4;
var temporary_pain = 0.4;
var transient_pain = 0.4;
function tick() {
  requestAnimationFrame (tick);
  if (Math.random() <0.2) {return;}
  step++;
  var updated = update_dimensions();
  var width = game_width;
  var height = game_height;
  var time = step/frames_per_second;//(Date.now() - start)/1000;
  var draw_background = updated || (step % Math.floor (frames_per_second/20)) == 1;
  
  var moving = !pause_next_frame;
  
  canvas_context.clearRect (0, 0, width, height);

  
  if (draw_background) {
    background_context.fillStyle = "rgb(0,0,0)";
    background_context.fillRect (0, 0, width, height);
  }
  skies.forEach (function(sky) {
    sky.peak += ((Math.random()*2) - 1)*0.05/frames_per_second;
    sky.height += ((Math.random()*2) - 1)*0.05/frames_per_second;
    sky.peak -= (sky.peak - 0.5)*0.0006/frames_per_second;
    sky.height -= (sky.height - 0.7)*0.0003/frames_per_second;
    if (draw_background) {
    background_context.beginPath();
    var peak = sky.peak*width;
    var sky_height = sky.height*horizon();
    background_context.moveTo(peak - width, sky_height + height*sky.steepness);
    background_context.bezierCurveTo(
      peak - width*0.6,
      sky_height + height*sky.steepness,
      peak - width*0.4,
      sky_height,
      peak,
      sky_height
    );
    background_context.bezierCurveTo(
      peak + width*0.4,
      sky_height,
      peak + width*0.6,
      sky_height + height*sky.steepness,
      peak + width,
      sky_height + height*sky.steepness
    );
    var limit = Math.max (sky_height + height*sky.steepness, horizon());
    background_context.lineTo (width, limit);
    background_context.lineTo (0, limit);
    background_context.fillStyle = "rgba(255, 255, 255, 0.04)";
    background_context.fill();
    }
  });
  
  if (draw_background) {
    background_context.fillStyle = "rgb(0,0,0)";
    background_context.fillRect (0, horizon(), width, height - horizon());
  }
  
  hill_step (draw_background);
        
  paths.forEach (function(path) {
    if (moving) {while (path.data.length <visible_path_components+path_components_per_frame) {
      var previous = path.data [path.data.length - 1];
      var current = {
        position: previous.position + previous.velocity/path_components_per_second,
        velocity: previous.velocity + previous.acceleration/path_components_per_second,
      };
      var max_speed =path.info.max_speed;
      
      var default_change_radius = max_speed*2.16/path_components_per_second;
      var bias = -previous.velocity*0.36/path_components_per_second;
      // the path secretly follows the player if the player moves too far away,
      // for both gameplay and symbolism reasons
      if (player.position - previous.position > 0.7) {
        bias += (player.position - previous.position - 0.7)*0.04/path_components_per_second;
      }
      if (player.position - previous.position < -0.7) {
        bias += (player.position - previous.position + 0.7)*0.04/path_components_per_second;
      }
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
    companion.position = closest_component (path, companion.distance).position;
    }
    
    // you can't get TOO far away from the paths.
    // TODO: possibly better symbolism and gameplay if the paths stay near YOU instead
    //if (player.position - deleted.position > 0.5) {
    //  player.position -= (player.position - deleted.position - 0.5)*3/600/paths.length;
    //}
    //if (player.position - deleted.position < -0.5) {
    //  player.position -= (player.position - deleted.position + 0.5)*3/600/paths.length;
    //}
    
    var component_width = function (index) {
      return width*path_radius*2*perspective.scale (index/visible_path_components); // * Math.sqrt ((1 + Math.abs (current.velocity)*width/(height/visible_path_components)));
    };
    
    canvas_context.fillStyle = "rgb(255, 255, 255)";
    canvas_context.beginPath();
    var began = false;
    var center_X = function (component, index) {return width*((component.position - player.position)*perspective.scale (index/visible_path_components)+ 0.5);};
    path.data.forEach (function(current, index) {
     
      //current.element.css ("bottom", index).css ("left", game_element.width()*(current.position - deleted.position +0.45));
      
      if (began) {
        canvas_context.lineTo(center_X (current, index) -component_width (index)/2, perspective.height (index/visible_path_components));
      }
      else {
        canvas_context.moveTo(center_X (current, index) -component_width (index)/2, perspective.height (index/visible_path_components));
        began = true;
      }
      
    });
    for (var index = path.data.length - 1; index >= 0; index -= 1){
      var current = path.data [index];
      canvas_context.lineTo(center_X (current, index) +component_width (index)/2, perspective.height (index/visible_path_components));
    }
    canvas_context.fill();
  });
  
  
  if (moving && Math.random() < 16/frames_per_second) {
    var thing = {kind: "tree", distance: thing_start_distance, position: player.position + ((Math.random()*2) - 1)*20, radius: 0.05};
    if (Math.random() <0.1) {thing.kind = "monster"; thing.radius = 0.05;}
    if (Math.random() <0.05) {thing.kind = "reward"; thing.radius = 0.03;}
    if (Math.random() <0.1) {thing.kind = "box"; thing.radius = 0.03;}
    stuff.push (thing);
  }
  
  //var boxes = {}
  var collision;
  
  stuff = stuff.filter (function (thing) {
    if (moving && thing.kind != "person") {
      thing.distance -= 1/seconds_to_travel_visible/frames_per_second;
      if (thing.kind == "monster") {
        thing.position += (((Math.random()*2) - 1)*0.1 + (player.position - thing.position)*0.03)/frames_per_second;
      }
    }
    if (thing.distance < -0.3) {return false;}
    if (thing.distance >player.distance && thing.distance <= player.distance + 2/seconds_to_travel_visible/frames_per_second && Math.abs (thing.position - player.position) <thing.radius + player.radius &&!(collision && collision.distance < thing.distance)) {
      collision = thing;
    }
    return true;
  });
  
  stuff.sort (function (first, second) {return second.distance - first.distance;});
  
  stuff.forEach (function (thing) {
    draw_thing (thing);
  });
  
  if (moving) {
    var player_velocity_request = Math.max (-1, Math.min (1, ((mouse_X/width) - 0.5)*10));
    player.position += player_velocity_request*player_max_speed/frames_per_second;
  }
  
  var distance = normalized_distance_from (companion.path, player);
  
  if (collision) {
    pause_next_frame = true;
    if (collision.kind == "tree") {
      if (collision.position >player.position) {player.position -= 0.025/frames_per_second;}
      else {player.position += 0.025/frames_per_second;}
      if (!player.falling_down) {
        temporary_pain += 0.15;
        player.speech.push ({
          text: "Ow, it hurts",
          age: 0,
          response: {
            person: companion,
            text: (distance <= 1.2) && "That's just part of life" || "It's your fault for straying"
          }
        });
      }
      player.falling_down = true;
    }
    if (collision.kind == "reward") {
      if (moving) {
        permanent_pain -= 0.02;
        temporary_pain -= 0.03;
        player.speech.push ({
          text: "Yay!",
          age: 0,
          response: {
            person: companion,
            text: (distance <= 1.2) && "I'm proud of you" || "That's not good for you"
          }
        });
      }
      collision.receiving = (collision.receiving || 0) + 0.7/frames_per_second;
      if (collision.receiving >1) {
        //hack: destroy
        collision.distance = - 1;
      }
    }
    if (collision.kind == "box") {
      if (moving) {
        player.speech.push ({
          text: "What's inside?",
          age: 0,
        });
        var thing = {kind: "reward", distance: collision.distance + 0.001, position: collision.position, radius: 0.03};
        if (Math.random() < 0.24) {
          thing.kind = "monster"; thing.radius = 0.05;
        }
        stuff.push (thing);
      }
      collision.receiving = (collision.receiving || 0) + 1.5/frames_per_second;
      if (collision.receiving >1) {
        //hack: destroy
        collision.distance = - 1;
      }
    }
    if (collision.kind == "monster") {
      if (moving) {
        permanent_pain += 0.02;
        temporary_pain += 0.3;
        player.speech.push ({
          text: "Ow, it hurts!",
          age: 0,
          response: {
            person: companion,
            text: (distance <= 1.2) && "Liar, that would never happen on the path" || "It's your fault for straying"
          }
        });
      }
      collision.attacking = (collision.attacking || 0) + 2/frames_per_second;
      if (collision.attacking>1) {
        // wander past the player without disappearing
        collision.distance = player.distance - 0.001;
      }
    }

  }
  else {
    player.falling_down = false;
    pause_next_frame = false;
  }
  
  temporary_pain += (permanent_pain - temporary_pain)/(2*frames_per_second);
  transient_pain += (temporary_pain - transient_pain)/(frames_per_second/20);

  companion.pronouncements.forEach (function (pronouncement) {
    if (companion.last_pronouncement && companion.last_pronouncement + pronouncement.delay_from_any >time) {return;}
    if (pronouncement.last_spoken && pronouncement.last_spoken + pronouncement.delay_from_same>time) {return;}
    if (pronouncement.automatically_at_distance) {
      if (pronouncement.automatically_at_distance [0] <= distance && pronouncement.automatically_at_distance [1] >= distance) {
        companion.last_pronouncement = time;
        pronouncement.last_spoken = time;
        var direction = companion.position <player.position;
        if (Math.abs (companion.position - player.position) >0.3) {direction =!direction;}
        companion.speech.push ({text: pronouncement.text, direction: direction, age: 0});
      }
    }
  });
  
  canvas_context.save();
  canvas_context.beginPath();
  //canvas_context.moveTo()
  canvas_context.rect (0, 0, width, height);
  canvas_context.scale (width, height);
  canvas_context.arc(0.5, 0.5, (1-transient_pain)/Math.sqrt (2), 0, turn, true);
  //canvas_context.globalCompositeOperation = "destination-in";
  canvas_context.fillStyle = "rgb(0,0,0)";
  canvas_context.fill();
  canvas_context.restore();
  
  draw_speech (player);
  draw_speech (companion);

  
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
