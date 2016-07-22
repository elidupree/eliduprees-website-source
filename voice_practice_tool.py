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
div.recording {float: left; margin:3px; padding-left:12px; background-color:#66c;}
canvas.recording {}
.control_panel {border-radius:8px;}
.control {display: inline-block; background-color:#ccc; color:#555; font-weight: bold; padding:4px;}
.control.selected {background-color:#5f5; color:#000;}
    </style> 
    ''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''<main><canvas id="histogram_canvas" width="1024" height="256">
The histogram should appear here, but it hasn't. Maybe you don't have JavaScript enabled. Or maybe your browser doesn't support the canvas element.
    </canvas>
    
<div class="control_panel"><div class="control on">On</div><div class="control off selected">Off</div><div class="control auto">Auto</div></div>

<div class="control_panel"><div class="control pause_during_playback selected "> During playback, pause recording and display the playback data in the histogram </div><div class="control no_pause"> During playback, continue recording and displaying the microphone input data in the histogram </div></div>

</main>'''), {"after_body":'''<script type="text/javascript">

$(function(){
  var audio = new (window.AudioContext || window.webkitAudioContext)();
  var canvas = document.getElementById("histogram_canvas").getContext("2d");

  
var source;
  var analyzer = audio.createAnalyser ();
var recorder_buffer_length = 4096;
  var rate = audio.sampleRate
  var recorder = audio.createScriptProcessor (recorder_buffer_length, 1, 1);
  var playback = audio.createGain ();
  playback.connect (audio.destination);
  var recording_1_second_width = rate/4096;
  var recording_height = 100;
  var current_playback;
  var current_recording;
  var pause_during_playback = true;
function stop_playback () {
    if (current_playback) {
    var old_player = current_playback.player;
    var redraw = current_playback.recording;
    current_playback = undefined;
    if (old_player) {old_player.stop ();}
    source.connect (analyzer);
    /*disconnecting from only one thing at a time doesn't seem to work*/
    playback.disconnect (analyzer);
    playback.connect (audio.destination);
    
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
    output.canvas = $("<canvas/>").attr("width", 1).attr("height", recording_height).addClass ("recording");
    output.element = $("<div/>").addClass ("recording").append (output.canvas).click (function (event) {
      var offset = output.canvas.offset ();
      var X = event.pageX - offset.left;
      if (X <0) {X = 0;}
      stop_playback ();
      var start_position =X/recording_1_second_width;
      var start_function = function () {
        var new_start_position =current_playback.start_position + (audio.currentTime - current_playback.start_time);
        var current_end = output.next_sample/rate;
        if (new_start_position >current_end - 0.05) {
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
        player.connect (playback);
        current_playback.player = player;
        setTimeout (function () {
          if (!(current_playback && current_playback.player=== player)) {return;}
          player.stop ();
          start_function ();
          }, (current_end - new_start_position)*500);
        player.start (audio.currentTime, new_start_position); 
      };
      current_playback = {start_time: audio.currentTime, start_position: start_position, recording: output};
      if (pause_during_playback) {
        source.disconnect (analyzer);
        /*disconnecting from only one thing at a time doesn't seem to work*/
        source.connect (recorder);
        playback.connect (analyzer);
      }
      start_function ();
    });
    $("main").append (output.element);
    output.canvas_context = output.canvas [0].getContext("2d");
    return output;
  }
  function draw_recording (recording) {
    var context = recording.canvas_context;
    recording.canvas.attr("width", recording.lines.length);
    if(recording=== current_recording) {
      context.fillStyle = "rgb(0, 0, 0)"
      } else {
      context.fillStyle = "rgb(50, 50, 50)"
            }
context.strokeStyle = "rgb(255, 0, 0)"
    recording.canvas_context.fillRect (0, 0, recording.canvas.width (), recording.canvas.height ());
context.beginPath ();
    for (var I = 0; I <recording.lines.length;++I) {
context.moveTo (I, recording_height/2 + recording.lines [I]*recording_height/2);
context.lineTo (I, recording_height/2 - recording.lines [I]*recording_height/2);
    }
context.stroke ();
    if (current_playback && current_playback.recording=== recording) {
    context.strokeStyle = "rgb(255, 255, 0)"
    context.beginPath ();
      var X = (current_playback.start_position + (audio.currentTime - current_playback.start_time))*recording_1_second_width; context.moveTo (X, 0); context.lineTo (X, recording_height); context.stroke ();
    }
  }

  
  analyzer.maxDecibels = 0;
  analyzer.fftSize = 2048;
  var buffer_length = analyzer.frequencyBinCount; 
  var frequency_data = new Uint8Array(buffer_length);
  
  recorder.onaudioprocess = function (event) {
    if (!current_recording) {return;}
    if (current_playback && pause_during_playback) {return;}
    var input = event.inputBuffer.getChannelData (0);
    var output = current_recording.buffer.getChannelData (0);
    var square_total = 0;
    for (var sample = 0; sample <recorder_buffer_length;++sample) {
      if (current_recording.next_sample >= current_recording.buffer.length) {
        var old_buffer = current_recording.buffer;
        var old_output = output;
        current_recording.buffer = audio.createBuffer (1, current_recording.buffer.length*2, rate);
        output = current_recording.buffer.getChannelData (0);
        for (var I = 0; I <old_buffer.length;++I) {
          output [I] = old_output [I];
        }
      }
      output [current_recording.next_sample] = input [sample];
      square_total += input [sample]*input [sample];
      ++current_recording.next_sample;
    }
    var magnitude = Math.sqrt (square_total/4096);
    current_recording.lines.push (magnitude);
    draw_recording (current_recording);
  }
  
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
    if (current_playback) {draw_recording (current_playback.recording);}
  }
  draw ();

  navigator.getUserMedia = (navigator.getUserMedia ||
                          navigator.webkitGetUserMedia ||
                          navigator.mozGetUserMedia ||
navigator.msGetUserMedia);
  navigator.getUserMedia ({ audio: true },

  // Success callback
  function(stream) {
    source = audio.createMediaStreamSource(stream);
    source.connect(analyzer);
    source.connect (recorder);
    draw ();
},

  // Error callback
  function(err) {
    console.log('The following gUM error occured: ' + err);
  }
);  

  $(".control.on").click (function () {
    $(".control.on").addClass ("selected");
    $(".control.off").removeClass ("selected");
    $(".control.auto").removeClass ("selected");
    
    set_current_recording (create_recording ());
  });
  $(".control.off").click (function () {
    $(".control.off").addClass ("selected");
    $(".control.on").removeClass ("selected");
    $(".control.auto").removeClass ("selected");
    
    set_current_recording (undefined);
  });

  $(".control.pause_during_playback").click (function () {
    $(".control.pause_during_playback").addClass ("selected");
    $(".control.no_pause").removeClass ("selected");
    
    pause_during_playback = true;
  });

  $(".control.no_pause").click (function () {
    $(".control.no_pause").addClass ("selected");
    $(".control.pause_during_playback").removeClass ("selected");
    
    pause_during_playback = false;
  });

});
    </script>'''}
  )
