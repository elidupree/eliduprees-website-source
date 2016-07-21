#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import bars
import blog
	  
def add_page(page_dict):
  utils.make_page (page_dict,
    '/voice-practice-tool',
      "Voice practice tool ⊂ Eli Dupree's website",
      r'''<style type="text/css">
html,body {background-color: white;}
    </style> 
    ''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''<main><canvas id="histogram_canvas" width="1024" height="256">
The histogram should appear here, but it hasn't. Maybe you don't have JavaScript enabled. Or maybe your browser doesn't support the canvas element.
    </canvas>

</main>'''), {"after_body":'''<script type="text/javascript">

$(function(){
  var audio = new (window.AudioContext || window.webkitAudioContext)();
  var canvas = document.getElementById("histogram_canvas").getContext("2d");
  var current_player;
  
var source;
  var analyzer = audio.createAnalyser ();
var recorder_buffer_length = 4096;
  var rate = audio.sampleRate
  var recorder = audio.createScriptProcessor (recorder_buffer_length, 1, 1);
  var recording_1_second_width = 10;
  var recording_height = 100;
  function create_recording () {
    output = {buffer: audio.createBuffer (1, audio.sampleRate, audio.sampleRate), next_sample: 0, lines: []};
    output.canvas = $("<canvas/>").attr("width", recording_1_second_width).attr("height", recording_height).click (function () {
      var player = audio.createBufferSource ();
      player.buffer = output.buffer;
      player.connect (audio.destination);
      if (current_player) {current_player.stop ();}
      player.start ();
      current_player = player;
    });
    $("main").append (output.canvas);
    output.canvas_context = output.canvas [0].getContext("2d");
    return output;
  }
  function draw_recording (recording) {
    var context = recording.canvas_context;
    if(recording=== current_recording) {
      context.fillStyle = "rgb(0, 0, 0)"
      } else {
      context.fillStyle = "rgb(50, 50, 50)"
            }
context.strokeStyle = "rgb(255, 0, 0)"
    recording.canvas_context.fillRect (0, 0, recording.canvas.width (), recording.canvas.height ());
context.beginPath ();
    for (var I = 0; I <recording.lines.length;++I) {
context.moveTo (I, recording_height/2 + recording.lines [I]*recording_height/512);
context.lineTo (I, recording_height/2 - recording.lines [I]*recording_height/512);
    }
context.stroke ();
    
  }
  var current_recording = create_recording ();
  analyzer.connect (recorder);
  
  analyzer.maxDecibels = 0;
  analyzer.fftSize = 2048;
  var buffer_length = analyzer.frequencyBinCount; 
  var frequency_data = new Uint8Array(buffer_length);
  
  recorder.onaudioprocess = function (event) {
    var input = event.inputBuffer.getChannelData (0);
    var output = current_recording.buffer.getChannelData (0);
    for (var sample = 0; sample <recorder_buffer_length;++sample) {
      if (current_recording.next_sample >= current_recording.buffer.length) {
        var old_buffer = current_recording.buffer;
        var old_output = output;
        current_recording.buffer = audio.createBuffer (1, current_recording.buffer.length*2, rate);
        current_recording.canvas.attr("width", current_recording.canvas.width ()*2);
        output = current_recording.buffer.getChannelData (0);
        for (var I = 0; I <old_buffer.length;++I) {
          output [I] = old_output [I];
        }
      }
      output [current_recording.next_sample] = input [sample];
      ++current_recording.next_sample;
    }
    draw_recording (current_recording);
  }
  
  navigator.getUserMedia = (navigator.getUserMedia ||
                          navigator.webkitGetUserMedia ||
                          navigator.mozGetUserMedia ||
navigator.msGetUserMedia);
  navigator.getUserMedia ({ audio: true },

  // Success callback
  function(stream) {
    source = audio.createMediaStreamSource(stream);
    source.connect(analyzer);
},

  // Error callback
  function(err) {
    console.log('The following gUM error occured: ' + err);
  }
);
  
  var last_line_added = audio.currentTime;
  var line_adding_increment = 1/recording_1_second_width;
  function draw () {
    requestAnimationFrame (draw);
    analyzer.getByteFrequencyData (frequency_data);
    var total = 0;
    canvas.fillStyle = "rgb(0, 0, 0)"
    canvas.strokeStyle = "rgb(255, 0, 0)"
    canvas.fillRect (0, 0, 1024, 256);
    canvas.beginPath ();
    for (var I = 0; I <1024;++I) {
      total = total + frequency_data [I];
      canvas.moveTo (I, 256);
      canvas.lineTo (I, 256 - frequency_data [I]);
    }
    canvas.stroke ();
    var average = total/1024;
    if (audio.currentTime >= last_line_added + line_adding_increment) {
      current_recording.lines.push (average);
      last_line_added = last_line_added + line_adding_increment
    }
  }
  draw ();
});
    </script>'''}
  )
