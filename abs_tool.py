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
p.disclaimer {font-size: 200%; text-align: center; margin:0.4em 0.8em;}
#panels {display: flex; justify-content: center; flex-wrap: wrap; }
.panel {margin:0.8em; padding:0.8em; background-color:#eee;}
.panel .labeled_input {margin:0.2em;}
.panel label {margin-left: 0.2em; margin-right: 0.6em;}
input[type='checkbox'] {width:2em;height:2em;}
input[type='radio'] {width:2em;height:2em;}
input[type='button'] {padding: 0 0.8em;}
input[type='number'] {width:3em;}
input {height:2em; vertical-align: middle;}
label {vertical-align: middle;}

@media screen and (max-width: 30em) {
  p.disclaimer {font-size: 85%;}
  #panels { }
}

    </style> 
    <script type="text/javascript">
$(function() {
"use strict";

var turn = Math.PI*2;
var game_element = $("#game");
var panels = $("#panels");
var buffer_element = $("#buffer");
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
  var bottom_height = bottom_bar.height();
  var game_top = panels.offset().top + panels.outerHeight();
  var game_bottom = $(window).height() - bottom_height;
  game_element.height (Math.max(game_bottom - game_top, $(window).width()/10));
  buffer_element.height(bottom_height);
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
var audio = new AudioContext();
var panner = audio.createStereoPanner();
var gain = audio.createGain();
gain.connect (panner);
panner.connect (audio.destination);

var default_cycles = 20;

var create_component = function (id, name) {
  var result = {
    id: id,
    position:0,
    direction:1,
    cycles_per_minute:default_cycles,
  }
  
  function range_overrides(){
    $("#"+id+"_speed_number").val($("#"+id+"_speed_range").val());
  }
  function number_overrides(){
    $("#"+id+"_speed_range").val($("#"+id+"_speed_number").val());
  }
  
  result.panel = $("<div>", {class: "panel"});
  result.panel.append (
    $("<label>", {text: name}),
    $("<div>", {class: "labeled_input"}).append (
      $("<input>", {type: "checkbox", id: id+"_enabled"}),
      $("<label>", {"for": id+"_enabled", text: "enabled"})
    ),
    $("<div>", {class: "labeled_input"}).append (
      $("<input>", {type: "range", id: id+"_speed_range", value: default_cycles, min: 1, max: 100, step: 1}).on ("input", range_overrides),
      $("<input>", {type: "number", id: id+"_speed_number", value: default_cycles, min: 1, max: 100, step: 1}).on ("input", number_overrides),
      $("<label>", {"for": id+"_speed_number", text: "cycles per minute"})
    ),
    $("<div>", {class: "labeled_input"}).append (
      $("<label>", {text: "Waveform:"}),
      $("<input>", {type: "radio", id: id+"_sinusoidal", name: id+"_waveform", value: "sinusoidal", checked: true}),
      $("<label>", {"for": id+"_sinusoidal", text: "sinusoidal"}),
      $("<input>", {type: "radio", id: id+"_sawtooth", name: id+"_waveform", value: "sawtooth"}),
      $("<label>", {"for": id+"_sawtooth", text: "sawtooth"})
    )
  );
  $("#panels").append (result.panel);
  return result;
}

function update_component (component) {
  var cycle_input = $("#"+component.id+"_speed_number").val();
  if (cycle_input !== NaN) {
    component.cycles_per_minute = cycle_input;
  }
  var cycles_per_frame = component.cycles_per_minute/(60*frames_per_second);
  var waveform = $("input:radio[name="+component.id+"_waveform]:checked").val();
  if (waveform === "sinusoidal") {
    var new_angle = Math.asin (component.position*component.direction) + turn*cycles_per_frame;
    if (new_angle > turn/4) {
      new_angle -= turn/2;
      component.direction *= -1;
    }
    component.position = component.direction*Math.sin (new_angle);
  }
  else if (waveform === "sawtooth") {
    component.position = component.position + component.direction*4*cycles_per_frame;
    if (component.position*component.direction > 1) {
      component.position = component.direction*2 - component.position;
      component.direction *= -1;
    }
  }
  
}

var visuals = create_component ("visuals", "Visuals:");
var audio_component = create_component ("audio", "Audio:");
audio_component.panel.append (
  $("<div>", {class: "labeled_input"}).append (
    $("<label>", {text: "Audio file:"}),
    $("<input>", {type: "radio", id: "brown_noise", name: "audio_file", value: "brown_noise", checked: true}).click (switch_audio),
    $("<label>", {"for": "brown_noise", text: "brown noise"}),
    $("<input>", {type: "radio", id: "bird_calls", name: "audio_file", value: "bird_calls"}).click (switch_audio),
    $("<label>", {"for": "bird_calls", text: "bird calls"}),
    $("<input>", {type: "radio", id: "water_flowing", name: "audio_file", value: "water_flowing"}).click (switch_audio),
    $("<label>", {"for": "water_flowing", text: "water flowing"}),
    $("<input>", {type: "radio", id: "audio_custom", name: "audio_file", value: "custom"}).click (switch_audio),
    $("<label>", {"for": "audio_custom", text: "custom"}),
    $("<input>", {type: "file", id: "audio_file", accept: "audio/*"}).change (reload_custom_audio)
    //$("<label>", {"for": "audio_file", text: "Audio file to play"})
  ),
  $("<div>", {class: "unlabeled_input"}).append (
    $("<input>", {type: "button", id: "audio_sync", value:"Synchronize with visuals"}).click (sync_audio)
  )
);

function setup_node (node, buffer) {
  node.buffer = buffer;
  node.loop = true;
  node.start();
}

function reload_custom_audio () {
  var reader = new FileReader();
  reader.onload = function() {
    audio.decodeAudioData (reader.result).then(function(decoded) {
      custom_audio_node = audio.createBufferSource();
      setup_node (custom_audio_node, decoded);
      $("#audio_custom").prop("checked", true);
      switch_audio();
    });
  }
  reader.readAsArrayBuffer($("#audio_file")[0].files [0]);
}

function sync_audio () {
  audio_component.position = visuals.position;
  audio_component.direction = visuals.direction;
  audio_component.cycles_per_minute = visuals.cycles_per_minute;
  $("#audio_"+$("input:radio[name=visuals_waveform]:checked").val()).prop("checked", true);
  $("#audio_speed_number").val($("#visuals_speed_number").val());
  $("#audio_speed_range").val($("#visuals_speed_range").val());
}

var audio_presets = {};
var custom_audio_node;



function make_preset (id, file) {
  var node = audio.createBufferSource();
  audio_presets [id] = node;
  var request = new XMLHttpRequest();
  request.open ("GET", file, true);
  request.responseType = 'arraybuffer';
  
  request.onload = function() {
    audio.decodeAudioData (request.response).then(function(decoded) {
      setup_node (node, decoded);
      switch_audio();
    });
  };
  request.send();
}

make_preset ("brown_noise", "/media/brown-noise.wav?rr");
make_preset ("bird_calls", "/media/bird_calls.mp3?rr");
make_preset ("water_flowing", "/media/water_flowing.mp3?rr");

function switch_audio() {
  var choice = $("input:radio[name=audio_file]:checked").val();
  if (audio_component.node) {
    audio_component.node.disconnect (gain);
  }
  if (audio_presets [choice]) {
    audio_component.node = audio_presets [choice];
  }
  else {
    audio_component.node = custom_audio_node;
  }
  if (audio_component.node) {
    audio_component.node.connect (gain);
  }
}






function tick() {
  requestAnimationFrame (tick);
  step++;
  var updated = update_dimensions();
  var width = game_width;
  var height = game_height;
  var time = step/frames_per_second;//(Date.now() - start)/1000;  
  
  canvas_context.clearRect (0, 0, width, height);
  
  canvas_context.save();
  canvas_context.translate (width*0.05, height*(0.5+0.05));
  canvas_context.scale (width*0.9, height*0.9*4);
  
  update_component (visuals);
  update_component (audio_component);
  
  if ($("#visuals_enabled").prop("checked")) {
    canvas_context.beginPath();
    canvas_context.arc (0.5 + visuals.position/2, 0, 0.05, 0, turn, true);
    canvas_context.lineWidth = 0.001;
    
    close_shape ("rgb(0, 0, 0)", "rgb(0,0,0)");
  }
  if ($("#audio_enabled").prop("checked")) {
    panner.pan.value = audio_component.position;
    gain.gain.value = 1;
  }
  else {
    gain.gain.value = 0;
  }
  
  canvas_context.restore();  
}
tick();


});
    </script>''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''<main><div id="content">
      
      <p class="disclaimer">I made this tool to help with ABS (alternating bilateral stimulation) therapy, but I have no expertise in it and only designed this based on third hand information. Use at your own risk!</p>
      <div id="panels"></div>
      <div id="game"></div>
      <div id="buffer"></div>
  </div>
</main>'''), {
  "jQuery_before": True,
  "blurb": "A unfinished online tool.",
  #"blurb_image": "/media/pac-asteroids-thumbnail.png?rr"
}
  )
  