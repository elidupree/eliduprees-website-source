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
.recent_box {float: right; width: 300px;}
    </style> 
    ''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''<main><canvas id="histogram_canvas" width="1024" height="256">
The histogram should appear here, but it hasn't. Maybe you don't have JavaScript enabled. Or maybe your browser doesn't support the canvas element.
    </canvas> <div class="recent_box "> When using auto recording, record exactly when the box is not empty. Click to move the corner of the box.<canvas id="recent_magnitudes"></canvas></div>
     
    
<div class="control_panel"><div class="control on">On</div><div class="control off selected">Off</div><div class="control auto">Auto</div></div>

<div class="control_panel"><div class="control pause_during_playback selected "> During playback, pause recording and display the playback data in the histogram </div><div class="control no_pause"> During playback, continue recording and displaying the microphone input data in the histogram </div></div>


<div class="control_panel"><div class="control auto_playback "> Whenever a recording finishes, play it back automatically </div><div class="control no_auto_playback selected "> Don't </div></div>

</main>'''), {"after_body":'''<script type="text/javascript">

$(function(){
  var audio = new (window.AudioContext || window.webkitAudioContext)();
  var histogram_canvas = document.getElementById("histogram_canvas").getContext("2d");
  
  var recent_magnitudes_size = 20;
  var recent_magnitudes_scale = 5;
  var recent_magnitudes_width =recent_magnitudes_size*recent_magnitudes_scale;
  var recent_magnitudes_height = 300;
  $("#recent_magnitudes").attr("width", recent_magnitudes_width).attr("height", recent_magnitudes_height);
  var recent_magnitudes_canvas = document.getElementById("recent_magnitudes").getContext("2d");
  var recent_magnitudes = [];
  for (var I = 0; I <recent_magnitudes_size ;++I) {recent_magnitudes.push (0);}
  
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
  var auto_recording = false;
  var auto_playback = false;
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
    if (old_recording) {
      draw_recording (old_recording);
      if (auto_playback) {begin_playback (old_recording, 0);}
    }
  }
  function begin_playback (recording, start_position) {
  var last_length = recording.next_sample;
      var start_function = function () {
        var new_start_position =current_playback.start_position + (audio.currentTime - current_playback.start_time);
        var current_end = recording.next_sample/rate;
        if (new_start_position >current_end - 0.0005) {
          stop_playback ();
          return;
        }

        var player = audio.createBufferSource ();
        player.buffer = recording.buffer;
        var finished_function= function () {
          if (!(current_playback && current_playback.player=== player)) {return;}
          if (recording.next_sample === last_length) {stop_playback ();}
          else {last_length = recording.next_sample; start_function ();}
        };
        player.onended = finished_function;
        player.connect (playback);
        current_playback.player = player;
        player.start (audio.currentTime, new_start_position, current_end - new_start_position); 
      };
      current_playback = {start_time: audio.currentTime, start_position: start_position, recording: recording};
      if (pause_during_playback) {
        source.disconnect (analyzer);
        /*disconnecting from only one thing at a time doesn't seem to work*/
        source.connect (recorder);
        playback.connect (analyzer);
      }
      start_function ();

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
      begin_playback (output, start_position);
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
    context.fillRect (0, 0, recording.canvas.width (), recording.canvas.height ());
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
  var start_recording_threshold = 0.1;
  var stop_recording_timeout = 5;
  
  recorder.onaudioprocess = function (event) {
    var input = event.inputBuffer.getChannelData (0);
    var square_total = 0;
    for (var sample = 0; sample <recorder_buffer_length;++sample) {
      square_total += input [sample]*input [sample];
    }
    var magnitude = Math.sqrt (square_total/4096);
    
    for (var I = 0; I <recent_magnitudes_size - 1 ;++I) {recent_magnitudes [I] = recent_magnitudes [I + 1];}
    recent_magnitudes [recent_magnitudes_size - 1] = magnitude;
    
    var context = recent_magnitudes_canvas;
      context.fillStyle = "rgb(0, 0, 0)"
    context.fillRect (0, 0, recent_magnitudes_width, recent_magnitudes_height);
      context.fillStyle = "rgb(255, 0, 0)"
    for (var I = 0; I <recent_magnitudes_size;++I) {
      context.fillRect (I*recent_magnitudes_scale, recent_magnitudes_height*(1 - recent_magnitudes [I]), recent_magnitudes_scale, recent_magnitudes_height*recent_magnitudes [I]);
    }
    context.strokeStyle = "rgb(255, 255, 0)"
    context.beginPath ();
      var X = recent_magnitudes_width - stop_recording_timeout*recent_magnitudes_scale;
      var Y = recent_magnitudes_height*(1 - start_recording_threshold);
       context.moveTo (X, 0); context.lineTo (X, Y); context.lineTo (recent_magnitudes_width, Y); context.stroke ();

    
    
    if (current_playback && pause_during_playback) {return;}
    
    if (auto_recording) {
      var should_record = false;
      for (var I = recent_magnitudes_size - stop_recording_timeout; I <recent_magnitudes_size ;++I) { if (recent_magnitudes [I] >=start_recording_threshold) {should_record = true; break;}}
      if (should_record &&!current_recording) {
        set_current_recording (create_recording ());
      }
      if (!should_record && current_recording){
        set_current_recording (undefined);
      }
    }
    
    if (!current_recording) {return;}

    var output = current_recording.buffer.getChannelData (0);
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
      ++current_recording.next_sample;
    }
    current_recording.lines.push (magnitude);
    draw_recording (current_recording);
  }
  
  var last_line_added = audio.currentTime;
  var line_adding_increment = 1/recording_1_second_width;
  function draw () {
    requestAnimationFrame (draw);
    analyzer.getByteFrequencyData (frequency_data);
    var total = 0;
    histogram_canvas.fillStyle = "rgb(0, 0, 0)"
    histogram_canvas.strokeStyle = "rgb(255, 0, 0)"
    histogram_canvas.fillRect (0, 0, 1024, 256);
    histogram_canvas.beginPath ();
    for (var I = 0; I <1024;++I) {
      total = total + frequency_data [I];
      histogram_canvas.moveTo (I, 256);
      histogram_canvas.lineTo (I, 256 - frequency_data [I]);
    }
    histogram_canvas.stroke ();
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
    auto_recording = false;
  });
  $(".control.off").click (function () {
    $(".control.off").addClass ("selected");
    $(".control.on").removeClass ("selected");
    $(".control.auto").removeClass ("selected");
    
    set_current_recording (undefined);
    auto_recording = false;
  });
  $(".control.auto").click (function () {
    $(".control.auto").addClass ("selected");
    $(".control.on").removeClass ("selected");
    $(".control.off").removeClass ("selected");
    
    auto_recording = true;
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

  $(".control.auto_playback").click (function () {
    $(".control.auto_playback").addClass ("selected");
    $(".control.no_auto_playback").removeClass ("selected");
    
auto_playback = true;
  });
  $(".control.no_auto_playback").click (function () {
    $(".control.no_auto_playback").addClass ("selected");
    $(".control.auto_playback").removeClass ("selected");
    
auto_playback = false;
  });

  $("#recent_magnitudes").click (function (event) {
      var offset = $("#recent_magnitudes").offset ();
            var X = event.pageX - offset.left;
       var Y = event.pageY - offset.top;
       start_recording_threshold  = 1-(Y/recent_magnitudes_height);
  stop_recording_timeout = Math.ceil( (recent_magnitudes_width - X)/recent_magnitudes_scale);
  });
});
    </script>'''}
  )
