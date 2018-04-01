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
  const waveform = definition.waveform;
  for (var index = 0; index <length ;++index) {
    const time = index/sample_rate;
    phase += frequency*turn*frame_duration;
    let sample;
    switch (waveform) {
      case "sine": sample = Math.sin (phase); break;
      case "square": sample = ((phase/turn)%1) < 0.5 ? 0.5 : -0.5; break;
      case "triangle": sample = 1 - Math.abs (((phase/turn)%1)-0.5)*4; break;
      case "sawtooth": sample = 1 - ((phase/turn)%1)*2; break;
    }
    data [index] = sample/25;
  }
  play_buffer (buffer);
}

function numerical_input(data) {
  let input_specs = {type: "range", id: data.id+"_numerical_range", value: data.min, min: data.min, max: data.max, step: data.step };
  if (data.logarithmic) {
    input_specs.min = 0;
    input_specs.max = 1;
    input_specs.step = 0.001;
    data.log_min = Math.log (data.min);
    data.log_range = Math.log (data.max) - data.log_min;
  }
  const range_input = $("<input>", input_specs);
  const number_input = $("<input>", {type: "number", id: data.id+"_numerical_number", value: data.min, min: data.min, max: data.max, step: data.step });
  
  function valid (value) {
    return Number.isFinite (value) && value !== 0;
  }
  
  function range_overrides() {
    const value = data.min*Math.exp(range_input[0].valueAsNumber*data.log_range);
    if (!valid (value)) {return;}
    number_input.val(value);
    updated(value);
  }
  function number_overrides() {
    const value = number_input[0].valueAsNumber;
    if (!valid (value)) {return;}
    set_range_input(value);
    updated(value);
  }
  function value_overrides() {
    const value = definition [data.field];
    if (!valid (value)) {return;}
    number_input.val(value);
    set_range_input(value);
    updated(value);
  }
  function set_range_input(value) {
    if (data.logarithmic) {
      const transformed = (Math.log (value) - data.log_min)/data.log_range;
      range_input.val(transformed);
    }
    else {
      range_input.val(value);
    }
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

function radio_input (data) {
  const result = $("<div>", {class: "labeled_input"}).append (
    $("<label>", {text: data.text + ":"})
  );
  
  data.options.forEach(function(option) {
    result.append (
      $("<input>", {type: "radio", id: data.id+"_radios_" + option.value, name: data.id+"_radios", value: option.value}).click (choice_overrides),
      $("<label>", {"for": data.id+"_radios_" + option.value, text: option.text}),
    );
  });
  
  function choice_overrides() {
    const value = $("input:radio[name="+data.id+"_radios]:checked").val();
    updated(value);
  }
  function value_overrides() {
    const value = definition [data.field];
    if (value === NaN) {return;}
    result.find ("#"+data.id+"_radios_" + value).prop ("checked", true);
    updated(value);
  }
  function updated(value) {
    definition [data.field] = value;
    synthesize_and_play ();
  }
  
  if (definition [data.field] === undefined) {
    definition [data.field] = data.default;
  }
  value_overrides ();
  
  return result;
}

/*
    $("<div>", {class: "labeled_input"}).append (
      $("<input>", {type: "checkbox", id: id+"_enabled"}),
      $("<label>", {"for": id+"_enabled", text: "enabled"})
    ),
*/

$("#panels").append ($("<div>", {class: "panel"}).append (numerical_input ({
  id: "frequency",
  field: "frequency",
  text: "Frequency (Hz)",
  min: 20,
  max: 22050,
  logarithmic: true,
  step: 1,
  default: 220,
})));


$("#panels").append ($("<div>", {class: "panel"}).append (radio_input ({
  id: "waveform",
  field: "waveform",
  text: "Waveform",
  default: "sine",
  options: [
    {value: "sine", text: "Sine"},
    {value: "square", text: "Square"},
    {value: "triangle", text: "Triangle"},
    {value: "sawtooth", text: "Sawtooth"},
  ]
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
  