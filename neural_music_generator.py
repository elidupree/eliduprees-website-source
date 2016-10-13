#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import bars
import blog

do_stuff = "record your own voice, play it back to yourself, and save the recordings to your computer."
blurb = "A tool to " + do_stuff
blurb_image ="/media/voice-practice-tool-screenshot.png?rr"
	  
def add_page(page_dict):
  utils.make_page (page_dict,
    '/neural-music-generator',
      "Neural music generator ⊂ Eli Dupree's website",
      r'''<style type="text/css">
html,body {background-color: white;}
    </style> 
    <link rel="stylesheet" href="/media/font-awesome-4.6.3/css/font-awesome.min.css?rr">
    ''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''<main><div id="content"></div>
     </main>'''), {"blurb": blurb, "blurb_image": blurb_image, "after_body":'''
     <script type="text/javascript" src="/media/audiobuffer-to-wav.js?rr"></script>
     <script type="text/javascript" src="/media/download.js?rr"></script>
     <script type="text/javascript" src="/media/jszip.min.js?rr"></script>
     <script type="text/javascript">

/* possible risk of things getting garbage collected when they shouldn't be? Stick them in a global */
window.global_hack = {}
$(function(){
  "use strict";
  
  var audio = new (window.AudioContext || window.webkitAudioContext)();
  var rate = audio.sampleRate;
  var generator_buffer_length = 2048;
  
  var turn = Math.PI*2;
    
  var source;
  var analyzer = audio.createAnalyser ();
  var generator_node = window.global_hack.generator_node = audio.createScriptProcessor (generator_buffer_length, 1, 1);
  
  var memory = new Float32Array (50);
  var base_matrix = new Float32Array (memory.length*memory.length);
  var current_matrix;
  var mod_locations = new Float32Array (memory.length*memory.length);
  var mod_magnitudes = new Float32Array (memory.length*memory.length);
  
  function duplicate_vector (vector) {
    var result = new Float32Array (vector.length);
    for (var index = 0; index <vector.length;++index) {
      result [index] = vector [index];
    }
    return result
  }
  function randomize (vector) {
    for (var index = 0; index <vector.length;++index) {
      vector [index] = Math.random()*2 - 1;
    }
  }
  function randomize_positive (vector) {
    for (var index = 0; index <vector.length;++index) {
      vector [index] = Math.random();
    }
  }
  randomize (memory);
  randomize (base_matrix);
  randomize_positive (mod_locations);
  randomize (mod_magnitudes);
  current_matrix = duplicate_vector(base_matrix);
  
  function multiply (vector, matrix) {
    var result = new Float32Array (vector.length);
    for (var index = 0; index <vector.length;++index) {
      var whatever = 0;
      for (var output = 0; output <vector.length;++output) {
        whatever += vector [output]*matrix [output + index*vector.length];
      }
      result [index] = Math.tanh (whatever);
    }
    return result;
  }
  
  function draw_matrix (matrix, width, height, canvas, context, scale) {
    canvas.attr ("width", width*scale);
    canvas.attr ("height", height*scale);
    
    for (var index = 0; index <width;++index) {
      for (var output = 0; output <height;++output) {
        var value = matrix [output + index*height];
        var converted = Math.floor ((value + 1)*128);
        context.fillStyle = "rgb(" + converted + "," + converted + "," + converted + ")"
        context.fillRect (index*scale, output*scale, scale, scale);
      }
    }
  }

var top_bar = $(".top_bar");
var bottom_bar = $(".bottom_bar");
var game_element = $("#content");
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
}
update_dimensions();
var mouse_X = 0;
var mouse_Y = 0;

function mouse_moved (event) {
  var offset = game_element.offset();
  mouse_X = (event.pageX - offset.left)/game_width;
  mouse_Y = (event.pageY - offset.top)/game_height;
  
  for (var index = 0; index <current_matrix.length;++index) {
    var distance = Math.abs (mod_locations [index] - mouse_X);
    var weight = Math.max (0, 1-distance*10);
    current_matrix [index] = base_matrix [index] + (mouse_Y-0.5)*2*mod_magnitudes [index]*weight;
  }
  draw_matrix (current_matrix, memory.length, memory.length, current_canvas, current_context,3);
  draw_matrix (base_matrix, memory.length, memory.length, base_canvas, base_context,3);
  console.log ("completed");
}
game_element.mousemove (mouse_moved);
game_element.click (function (event) {
  base_matrix = duplicate_vector(current_matrix);
  randomize_positive (mod_locations);
  randomize (mod_magnitudes);
  mouse_moved (event);
});
  
  var base_canvas = $("<canvas>");
  var current_canvas = $("<canvas>");
  var base_context = base_canvas[0].getContext ("2d");
  var current_context = current_canvas[0].getContext ("2d");
  game_element.append (base_canvas).append (current_canvas);

  generator_node.connect (audio.destination);
  
  var time = 0;
  function evaluate (node) {
    if (typeof node === 'number') {return node;}
    return node.evaluate (node.parameters);
  }
  function total (parameters) {
    var result = 0;
    parameters.forEach (function (parameter) {
      result += evaluate (parameter);
    });
    return result;
  }
  function product (parameters) {
    var result = 1;
    parameters.forEach (function (parameter) {
      result *= evaluate (parameter);
    });
    return result;
  }
  function get_time() {return time;}
  function sin (parameters) {
    return Math.sin (evaluate (parameters [0])*40);
  }
  
  function generate_random_node (level) {
    if (level <= 0) {
      if (Math.random() <0.5) {
        return Math.random()*2-1;
      }
      else {
        return {evaluate: get_time};
      }
    }
    if (Math.random() <0.3) {
      return {
        parameters: [generate_random_node (level-1), generate_random_node (level-2)],
        evaluate: total
      };
    }
    if (Math.random() <0.4) {
      return {
        parameters: [generate_random_node (level-1), generate_random_node (level-2)],
        evaluate: product
      };
    }
      return {
        parameters: [generate_random_node (level-1)],
        evaluate: sin
      };
  }
  
  var root = {
          parameters: [generate_random_node (5)],
                  evaluate: sin
                };
  console.log (root);  console.log (evaluate (root));console.log (evaluate (Math.random()*2-1));
  
    
  generator_node.onaudioprocess = window.global_hack.audio_process = function (event) {
    update_dimensions();
    var output = event.outputBuffer.getChannelData (0);
    memory = multiply (memory, current_matrix);
    
    var log_min = Math.log (20);
    var log_max = Math.log (20000);
    var half_log_range = (log_max - log_min)/2;
    
    for (var sample = 0; sample <generator_buffer_length;++sample) {
      time += 1/rate;
      output [sample] = evaluate (root);
      //output [sample] = 0;
      //for (var index = 0; index <10;++index) {
      //  var frequency = Math.exp (log_min + (memory [index]+1)*half_log_range);
      //  output [sample] += Math.sin (frequency*turn*sample/rate);
      //}
    }
  }
});

    </script>'''}
  )
