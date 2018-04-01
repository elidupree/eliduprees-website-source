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

var definition = {};

function play_buffer (buffer) {
  if (audio_source) {audio_source.stop();}
  audio_source = audio.createBufferSource();
  audio_source.buffer = buffer;
  audio_source.connect (audio.destination);
  audio_source.start ();
}

function synthesize_and_play () {
  const length = sample_rate*2;
  const buffer = audio.createBuffer (1, length, sample_rate);
  const data = buffer.getChannelData (0);
  
  let phase = 0;
  const frame_duration = 1/sample_rate;
  const frequency = definition.frequency;
  for (var index = 0; index <length ;++index) {
    const time = index/sample_rate;
    phase += frequency*turn*frame_duration;
    data [index] = Math.sin (phase)/5;
  }
  play_buffer (buffer);
}

function numerical_input(data) {
  const range_input = $("<input>", {type: "range", id: data.id+"_numerical_range", value: data.min, min: data.min, max: data.max, step: data.step });
  const number_input = $("<input>", {type: "number", id: data.id+"_numerical_number", value: data.min, min: data.min, max: data.max, step: data.step });
  
  function range_overrides() {
    const value = range_input[0].valueAsNumber;
    if (value === NaN) {return;}
    number_input.val(value);
    updated(value);
  }
  function number_overrides() {
    const value = number_input[0].valueAsNumber;
    if (value === NaN) {return;}
    range_input.val(value);
    updated(value);
  }
  function value_overrides() {
    const value = definition [data.field];
    if (value === NaN) {return;}
    number_input.val(value);
    range_input.val(value);
    updated(value);
  }
  function updated(value) {
    definition [data.field] = value;
    synthesize_and_play ();
  }

  const result = $("<div>", {class: "labeled_input"}).append (
    range_input.on ("input", range_overrides),
    number_input.on ("input", number_overrides),
    $("<label>", {"for": data.id+"_numerical_number", text: data.text})
  ).on("wheel", function (event) {
    console.log (definition [data.field]) ;
    definition [data.field] += (Math.sign(event.originalEvent.deltaY) || Math.sign(-event.originalEvent.deltaX) || 0)*data.step;
    value_overrides ();
  });
  
  if (definition [data.field] === undefined) {
    definition [data.field] = data.default;
  }
  value_overrides ();
  
  return result;
}

$("#panels").append ($("<div>", {class: "panel"}).append (numerical_input ({
  id: "frequency",
  field: "frequency",
  text: "Frequency (Hz)",
  min: 1,
  max: 22050,
  step: 1,
  default: 220,
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
  