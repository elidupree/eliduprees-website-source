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
div.recording {display: inline-block; margin:3px;/* padding-left:12px;*/ background-color:#ccc;}
canvas.recording {display: block; cursor: pointer;}
#recent_magnitudes {display: block; cursor: pointer;}
.control_panels {display: inline-block; vertical-align: middle;}
.control_panel {display: inline-block; background-color: transparent; margin:3px; vertical-align: top;}
.control {display: inline-block; background-color:#ccc; color:#555; font-weight: bold; padding:4px; vertical-align: top; cursor: pointer;}
.control.selected {background-color:#5f5; color:#000;}
.text-danger {color:#d9534f;}
.recent_box {display: inline-block; vertical-align: middle; background-color:#ccc;}
.recent_magnitudes_caption {padding:4px;}
.recording_button {padding:0 3px; cursor: pointer;}
.recordings {
    display: flex;
    flex-wrap: wrap-reverse;
}
.page_description {padding:0.3em 2em; font-size: 110%;}

.fa-stack.force_small {width:1em; height:1em; line-height:0.7em;}
span.no_underlay {position: absolute; top: 0; left: 0; z-index: 1;}
    </style> 
    <link rel="stylesheet" href="/media/font-awesome-4.6.3/css/font-awesome.min.css?rr">
    ''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''<main><canvas id="histogram_canvas" width="320" height="80">
The histogram should appear here, but it hasn't. Maybe you don't have JavaScript enabled. Or maybe your browser doesn't support the canvas element.
    </canvas><div class="page_description "></div><div class="control_panels "></div><!--
    --><div class="recent_box "><div class="recent_magnitudes_caption "></div><canvas id="recent_magnitudes"></canvas></div>
           <div class="recordings "></div>
     </main>'''), {"after_body":'''
     <script type="text/javascript" src="/media/audiobuffer-to-wav.js?rr"></script>
     <script type="text/javascript" src="/media/download.js?rr"></script>
     <script type="text/javascript" src="/media/jszip.min.js?rr"></script>
     <script type="text/javascript">

/* possible risk of things getting garbage collected when they shouldn't be? Stick them in a global */
window.global_hack = {}
$(function(){
  var audio = new (window.AudioContext || window.webkitAudioContext)();
  var rate = audio.sampleRate;
  var recorder_buffer_length = 2048;
  var histogram_canvas = document.getElementById("histogram_canvas").getContext("2d");
  
  var recent_magnitudes_size = 1;
  var recent_magnitudes_scale = 1;
  var recent_magnitudes_width = 1;
  var recent_magnitudes_height = 1;
  var recent_magnitudes_canvas = document.getElementById("recent_magnitudes").getContext("2d");
  var recent_magnitudes = [];
  for (var I = 0; I <recent_magnitudes_size ;++I) {recent_magnitudes.push (0);}
  var start_recording_threshold = 0.5;
  var stop_recording_timeout = Math.ceil (rate*0.5/recorder_buffer_length);
    
var source;
  var analyzer = audio.createAnalyser ();
  var recorder = window.global_hack.recorder = audio.createScriptProcessor (recorder_buffer_length, 1, 1);
  
  /* major hack: the recorder is NOT supposed to be connected to anything,
  but in Chrome, it literally doesn't work unless you connect it to the destination. In any case, it only outputs silence, so the workaround is tolerable. */
  recorder.connect (audio.destination); 
   
  var playback = audio.createGain ();
  playback.connect (audio.destination);
  var recording_1_second_width = rate/recorder_buffer_length;
  var recording_height = 100;
  var current_playback;
  var current_recording;
  var recordings = [];
  var pause_during_playback;
  var auto_recording;
  var auto_playback;
  var iterate_playback;
  var logarithmic;
  
var no = function (underlay) {return '<span class="fa-stack force_small">  <i class="fa fa-' + underlay + ' fa-stack-1x"></i> <i class="fa fa-ban fa-stack-1x text-danger fa-lg"></i></span>';};
  
function stop_playback (force) {
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
    if (iterate_playback && redraw.next &&!force) {begin_playback (redraw.next, 0);}
    }
  }
  function singleton_panel(elem) {
    elem.addClass ("control");
    return $("<div/>").addClass ("control_panel").append(elem);
  }
  function set_current_recording (recording) {
    var old_recording = current_recording;
    current_recording = recording;
    if (current_recording) {
      recordings.push (current_recording);
      if (recordings.length >1) {
        recordings [recordings.length - 2].next = current_recording;
      }
      if (recordings.length === 2) {
        var saving = false;
        $(".control_panels").append (singleton_panel($("<div/>").html ('<i class="fa fa-floppy-o"></i> All').click(function () {
          if (saving) {return;}
          saving = true;
          var zip = new JSZip();
          for (var I = 0; I <recordings.length;++I) {
      var wav = audioBufferToWav(recordings [I].buffer);
            var blob = new window.Blob([ new DataView(wav) ], { type: 'audio/wav' });
            zip.file (recordings [I].filename, blob);
          }

          zip.generateAsync ({type: "blob"}).then (function (blob) {download (blob, "all-recordings-" + recordings [recordings.length - 1].date_string + ".zip", "application/zip"); saving = false;});
        })));
      }      
    }
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
    output.canvas = $("<canvas/>").attr("width", 1).attr("height", recording_height).addClass ("recording").click (function (event) {
      var offset = output.canvas.offset ();
      var X = event.pageX - offset.left;
      if (X <0) {X = 0;}
      stop_playback (true);
      var start_position =X/recording_1_second_width;
      begin_playback (output, start_position);
    });
    output.play_button = $("<div/>").addClass ("recording_button").click (function () {
      var stop = (current_playback && current_playback.recording === output);
      stop_playback (true);
      if (!stop) { begin_playback (output, 0);}
    });
    var date = new Date ();
    output.date_string = date.getFullYear () + "-" + date.getMonth () + "-" + date.getDate () + "-" + date.getHours ()  + "-" + date.getMinutes ()  + "-" + date.getSeconds () ;
    output.filename ="recording-" + output.date_string + ".wav";
    output.save_button = $("<div/>").addClass ("recording_button").html ('<i class="fa fa-floppy-o"></i>').click (function () {
      var wav = audioBufferToWav(output.buffer);
      var blob = new window.Blob([ new DataView(wav) ], { type: 'audio/wav' });
      download (blob, output.filename, "audio/wav");
    });
    output.element = $("<div/>").addClass ("recording").append (output.canvas).append (output.play_button).append (output.save_button);
    $(".recordings").append (output.element);
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
recording.play_button.html ('<i class="fa fa-stop"></i>');
    context.strokeStyle = "rgb(255, 255, 0)"
    context.beginPath ();
      var X = (current_playback.start_position + (audio.currentTime - current_playback.start_time))*recording_1_second_width; context.moveTo (X, 0); context.lineTo (X, recording_height); context.stroke ();
    }
    else {
    recording.play_button.html ('<i class="fa fa-play"></i>');
    }
  }

  
  analyzer.maxDecibels = 0;
  analyzer.fftSize = 2048;
  var frequency_buffer_length = analyzer.frequencyBinCount; 
  var frequency_data = new Uint8Array(frequency_buffer_length);
  
  recorder.onaudioprocess = window.global_hack.audio_process = function (event) {
    var input = event.inputBuffer.getChannelData (0);
    var square_total = 0;
    for (var sample = 0; sample <recorder_buffer_length;++sample) {
      square_total += input [sample]*input [sample];
    }
    var magnitude = Math.sqrt (square_total/recorder_buffer_length);
    magnitude = 1-(Math.log (magnitude)/Math.log (1/1024));
    
    for (var I = 0; I <recent_magnitudes_size - 1 ;++I) {recent_magnitudes [I] = recent_magnitudes [I + 1];}
    recent_magnitudes [recent_magnitudes_size - 1] = magnitude;
    
  recent_magnitudes_size = Math.ceil (rate*2/recorder_buffer_length);
  recent_magnitudes_scale = Math.ceil (Math.min ($("body").width ()/3, 200)/recent_magnitudes_size);
  recent_magnitudes_width =recent_magnitudes_size*recent_magnitudes_scale;
  recent_magnitudes_height = Math.min ($("body").height ()/3, 300);
  
  $(".recent_box").width (recent_magnitudes_width);
  $("#recent_magnitudes").attr("width", recent_magnitudes_width).attr("height", recent_magnitudes_height);
  $(".control_panels").width ($("body").width () - recent_magnitudes_width);

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
    var width = $("body").width ();
    var height = Math.min (128, $("body").height ()/4);
    
    $("#histogram_canvas").attr("width", width).attr("height", height);
        
    histogram_canvas.fillStyle = "rgb(0, 0, 0)"
    histogram_canvas.fillRect (0, 0, width, height);
    histogram_canvas.fillStyle = "rgb(255, 0, 0)"
var previous = 0;
    for (var I = 0; I <frequency_buffer_length;++I) {
      total = total + frequency_data [I];
      var X = (I + 1)*width/frequency_buffer_length;
      var Y =frequency_data [I]*height/256
      if (logarithmic) {X = Math.log (I + 1)*width/Math.log (frequency_buffer_length);}
      histogram_canvas.fillRect (previous, height - Y, X - previous, Y);
      previous = X;
    }
    var average = total/frequency_buffer_length;
    if (current_playback) {draw_recording (current_playback.recording);}
  }
  draw ();

  var terse = [];
  var verbose = [];
terse.push ([$(".recent_magnitudes_caption"), ""]);
verbose.push ([$(".recent_magnitudes_caption"), "When using auto recording, record exactly when the box is not empty. Click to move the corner of the box."]);
terse.push ([$(".page_description"), ""]);
verbose.push ([$(".page_description"), "This page lets you record your own voice, play it back to yourself, and save the recordings to a file. Tested in Firefox and Chrome; may not work in other browsers."]);
  
  function update_controls (info) {
    for (var I = 0; I <info.length;++I) {
      info [I] [0].empty ().append (info [I] [1]).show ();
      if (info [I] [1] === "") {info [I] [0].hide ();}
    }
  }
  function make_control_panel (save, selected, controls){
    
    if (save) {
      save = "vpt_"+ save;
      value = read_cookie (save);
      if (value !== null) {selected =parseInt (value);}
    }

var panel = $("<div/>").addClass ("control_panel");
    for (var I = 0; I <controls.length;++I) {
      (function (index, info) {
      controls [index] = $("<div/>").addClass ("control").click(function () {
      for (var J = 0; J  <controls.length;++J) {
if (controls [J] [0] === $(this) [0]) {controls [J] .addClass ("selected");} else{controls [J] .removeClass ("selected");}
    
}
if (save) {set_cookie (save, index, 30);}
info [2] ();
  });
terse.push ([controls [index], info [0]]);
verbose.push ([controls [index], info [1]]);
  } (I, controls [I]));
  panel.append (controls [I]);
    }

  /*hack: the verbose option currently must be listed last, but we want it earlier in the page*/
   if (save === "vpt_verbose") { $(".control_panels").children ().first ().after (panel);} else { $(".control_panels").append (panel); }
    controls [selected].click ();
  }

  make_control_panel (null, 1, [
    ['<i class="fa fa-microphone"></i>',"On", function () {

    set_current_recording (create_recording ());
    auto_recording = false;}
],
[no ('microphone'),"Off", function () {
    set_current_recording (undefined);
    auto_recording = false;}
],
['<i class="fa fa-microphone"></i><i class="fa fa-cog"></i>',"Auto", function () {auto_recording = true;}]
]);

  make_control_panel ("pause_during_playback", 0, [
    ['<i class="fa fa-play"></i>' + no ('microphone'),"During playback, pause recording and display the playback data in the histogram", function () {

    pause_during_playback = true;}
],
['<i class="fa fa-play"></i><i class="fa fa-microphone"></i>',"During playback, continue recording and displaying the microphone input data in the histogram", function () {
    pause_during_playback = false;}
]]);

  make_control_panel ("auto_playback", 1, [
    ['<i class="fa fa-microphone"></i><i class="fa fa-play"></i>',"Whenever a recording finishes, play it back automatically", function () {

auto_playback = true;}
],
['<i class="fa fa-ban"></i>',"Don't", function () {
auto_playback = false;}
]]);

  make_control_panel ("iterate_playback", 1, [
    ['<i class="fa fa-play"></i><i class="fa fa-play"></i>',"Play back multiple recordings in a row", function () {

iterate_playback = true;}
],
['<i class="fa fa-play"></i>',"Only play back one recording at a time", function () {
iterate_playback = false;}
]]);

  make_control_panel ("logarithmic", 1, [
    ["Hz","Linear scale (1 pixel = X Hertz)", function () {

logarithmic = false;}
],
["Log","Log scale (1 pixel = X semitones)", function () {
logarithmic = true;}
]]);

$(".control_panels").append (singleton_panel($("<div/>").addClass("vpt_patreon").addClass("hidden_from_restricted_users")));
terse.push ([$(".vpt_patreon"), '<a href="https://www.patreon.com/EliDupree"><img class="small_inline_image" src="/media/patreon-logo.png?rr" alt="Patreon" /></a>']);
verbose.push ([$(".vpt_patreon"), 'If you like this tool, consider <a href="https://www.patreon.com/EliDupree">supporting me on Patreon</a> so that I can continue making awesome things and sharing them for free on the Internet.']);

  make_control_panel ("verbose", 0, [
    ["Verbose","Verbose options", function () {

update_controls (verbose);}
],
['<i class="fa fa-ban"></i>',"Terse options", function () {
update_controls (terse);}
]]);




  $("#recent_magnitudes").click (function (event) {
      var offset = $("#recent_magnitudes").offset ();
            var X = event.pageX - offset.left;
       var Y = event.pageY - offset.top;
       start_recording_threshold  = 1-(Y/recent_magnitudes_height);
  stop_recording_timeout = Math.ceil( (recent_magnitudes_width - X)/recent_magnitudes_scale);
  });

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
},

  // Error callback
  function(err) {
    console.log('The following gUM error occured: ' + err);
  }
);  

});

    </script>'''}
  )
