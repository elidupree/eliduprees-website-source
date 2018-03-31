#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import bars
import blog
	  
def add_page(page_dict):
  utils.make_page (page_dict,
    '/webfxr',
      "WebFXR ⊂ Eli Dupree's website",
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
var panels = $("#panels");




var start = Date.now();
var audio = new AudioContext();
var audio_source;
var sample_rate = 44100;

var something = 20;

function play_buffer (buffer) {
  if (audio_source) {audio_source.stop();}
  audio_source = audio.createBufferSource();
  audio_source.buffer = buffer;
  audio_source.connect (audio.destination);
  audio_source.start ();
}

function synthesize_and_play () {
  let length = sample_rate*2;
  let buffer = audio.createBuffer (1, length, sample_rate);
  let data = buffer.getChannelData (0);
  for (var index = 0; index <length ;++index) {
    let time = index/sample_rate;
    data [index] = Math.sin (time*turn*11*something)/5 ;
  }
  play_buffer (buffer)
}

function numerical_input(id, callback) {
  function range_overrides() {
    let value = $("#"+id+"_numerical_range").val();
    if (value === NaN) {return;}
    $("#"+id+"_numerical_number").val(value);
    callback (value) ;
  }
  function number_overrides() {
    let value = $("#"+id+"_numerical_number").val();
    if (value === NaN) {return;}
    $("#"+id+"_numerical_range").val(value);
    callback (value);
  }
  function value_overrides(value) {
    if (value === NaN) {return;}
    $("#"+id+"_numerical_number").val(value);
    $("#"+id+"_numerical_range").val(value);
    callback (value);
  }

  return $("<div>", {class: "labeled_input"}).append (
    $("<input>", {type: "range", id: id+"_numerical_range", value: 20, min: 1, max: 100, step: 1}).on ("input", range_overrides),
    $("<input>", {type: "number", id: id+"_numerical_number", value: 20, min: 1, max: 100, step: 1}).on ("input", number_overrides),
    $("<label>", {"for": id+"_numerical_number", text: "numerical input"})
  ).on("wheel", function (event) {
    something += Math.sign(event.originalEvent.deltaY) || Math.sign(-event.originalEvent.deltaX) || 0;
    value_overrides (something);
  });
}

$("#panels").append ($("<div>", {class: "panel"}).append (numerical_input ("foo", function (value) {
  something = value;
  synthesize_and_play () ;
})));



function tick() {
  requestAnimationFrame (tick); 
}
tick();


});
    </script>''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"misc":True}, '''<main><div id="content">
      
      <p class="disclaimer"></p>
      <div id="panels"></div>
  </div>
</main>'''), {
  "jQuery_before": True,
  "blurb": "A unfinished online tool.",
  #"blurb_image": "/media/pac-asteroids-thumbnail.png?rr"
}
  )
  