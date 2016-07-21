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
canvas {float: left; margin:2px;}
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

  
var source;
  var analyzer = audio.createAnalyser ();
var recorder_buffer_length = 4096;
  var rate = audio.sampleRate
  var recorder = audio.createScriptProcessor (recorder_buffer_length, 1, 1);
  var recording_1_second_width = 10;
  var recording_height = 100;
  var current_playback;
  var current_recording;
function stop_playback () {
    if (current_playback) {
    var old_player = current_playback.player;
    var redraw = current_playback.recording;
    current_playback = undefined;
    old_player.stop ();
    draw_recording (redraw);
    }
  }
  function set_current_recording (recording) {
    var old_recording = current_recording;
    current_recording = recording;
    if (old_recording) {draw_recording (old_recording);}
  }
  function create_recording () {
    var output = {buffer: audio.createBuffer (1, audio.sampleRate, audio.sampleRate), next_sample: 0, lines: []};
    output.canvas = $("<canvas/>").attr("width", recording_1_second_width).attr("height", recording_height).click (function (event) {
      var offset = output.canvas.offset ();
      var X = event.pageX - offset.left;
      stop_playback ();
      var start_position =X/recording_1_second_width;
      var start_function = function () {
        var start_position =current_playback.start_position + (audio.currentTime - current_playback.start_time);
        var current_end = output.next_sample/rate;
        if (start_position >current_end - 0.05) {
          stop_playback ();
          return;
        }

        var player = audio.createBufferSource ();
        player.buffer = output.buffer;
        var finished_function= function () {
          if (!(current_playback && current_playback.player=== player)) {return;}
          if (player.buffer === output.buffer) {stop_playback ();}
          else {start_function ();}
        };
        player.onended = finished_function;
        player.connect (audio.destination);
        current_playback.player = player;
        setTimeout (function () {
          if (!(current_playback && current_playback.player=== player)) {return;}
          player.stop ();
          start_function ();
          }, (current_end - start_position)*500);
        player.start (audio.currentTime, start_position); 
      };
      current_playback = {start_time: audio.currentTime, start_position: start_position, recording: output};
      start_function ();
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
    if (current_playback && current_playback.recording=== recording) {
    context.strokeStyle = "rgb(255, 255, 0)"
    context.beginPath ();
      var X = (current_playback.start_position + (audio.currentTime - current_playback.start_time))*recording_1_second_width; context.moveTo (X, 0); context.lineTo (X, recording_height); context.stroke ();
    }
  }
  current_recording = create_recording ();
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
    if (current_playback) {draw_recording (current_playback.recording);}
  }
  draw ();
  
  $("#histogram_canvas").click (function () {set_current_recording (create_recording ());});
});
    </script>'''}
  )
