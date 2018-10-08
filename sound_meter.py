#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import bars
import blog

blurb = "A simple tool I use to monitor how loudly I'm talking."
blurb_image ="/media/voice-practice-tool-screenshot.png?rr"
	  
def add_page(page_dict):
  utils.make_page (page_dict,
    '/sound-meter',
      "Sound meter ⊂ Eli Dupree's website",
      r'''<style type="text/css">
html,body {background-color: black; color: white;}
#content {height: 100%; width: 100%; display: flex; align-items: stretch;}
#info,#warning{width: 50%;}
#info {position: relative;}
#level {background-color: #888; position: absolute; bottom: 0; left: 0; right: 0;}
#threshold {background-color: yellow; position: absolute; height: 3px; left: 0; right: 0;}
    </style> 
    ''',
      '''
    <div id="content">
      <div id="warning">
      </div>
      <div id="info">
        '''+blurb+'''
        <div id="level">
        </div>
        <div id="threshold">
        </div>
      </div>
    </div>
''', {"blurb": blurb, "blurb_image": blurb_image, "after_body":'''
     
     <script type="text/javascript">
$(function(){
  "use strict";
 
  /* possible risk of things getting garbage collected when they shouldn't be? Stick them in a global */
  window.global_hack = {};
  
  var audio = new (window.AudioContext || window.webkitAudioContext)();
  var rate = audio.sampleRate;
  var recorder_buffer_length = 2048;
  var recorder;
  var memories = [];
  var memory_count = Math.ceil (audio.sampleRate/recorder_buffer_length/2);
  var storage = window.localStorage;
  var threshold;
  
  var source;
  
  function set_threshold (new_threshold) {
    threshold = new_threshold;
    storage.setItem ("threshold", threshold.toString());
    $("#threshold").css ("bottom", (threshold*100) + "%");
  }
  set_threshold (parseFloat (storage.getItem ("threshold") || "0.5"));

  navigator.getUserMedia = (navigator.getUserMedia ||
                            navigator.webkitGetUserMedia ||
                            navigator.mozGetUserMedia ||
                            navigator.msGetUserMedia);
  navigator.getUserMedia ({ audio: true },
    // Success callback
    function(stream) {
      source = audio.createMediaStreamSource(stream);
      recorder = window.global_hack.recorder = audio.createScriptProcessor (recorder_buffer_length, source.numberOfOutputs, 1);
      /* major hack: the recorder is NOT supposed to be connected to anything,
      but in Chrome, it literally doesn't work unless you connect it to the destination. In any case, it only outputs silence, so the workaround is tolerable. */
      recorder.connect (audio.destination);
      source.connect (recorder);
      
      recorder.onaudioprocess = window.global_hack.audio_process = function (event) {
        var input = event.inputBuffer;
        var square_total = 0;
        var samples_total = 0;
        for (var channel = 0; channel < input.numberOfChannels; ++channel) {
          var data = input.getChannelData (channel);
          samples_total += data.length;
          for (var sample = 0; sample < data.length; ++sample) {
            square_total += data [sample]*data [sample];
          }
        }
        memories.push (square_total/samples_total);
        if (memories.length > memory_count) {
          memories.shift();
        }
        square_total = 0;
        memories.forEach(function(memory) {square_total += memory;});
        var result = Math.sqrt (square_total/memory_count);
        if (result >= threshold*0.5) {
          $("#warning").css("background-color", "red");
        }
        else {
          $("#warning").css("background-color", "black");
        }
        $("#level").css("height", (result*200)+ "%");
      }
    },

    // Error callback
    function(err) {
      console.log('The following gUM error occured: ' + err);
    }
  );
  
  $("#info").click(event =>{
    var height = event.clientY / $(window).height();
    set_threshold(1.0 - height);
  });
  
  
});
</script>
'''}
  )
