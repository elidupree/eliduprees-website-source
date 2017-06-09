#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import bars
import blog

blurb = "An unfinished tool for helping deal with annoying sound."
blurb_image ="/media/voice-practice-tool-screenshot.png?rr"
	  
def add_page(page_dict):
  utils.make_page (page_dict,
    '/annoying-sound-tool',
      "Annoying sound tool ⊂ Eli Dupree's website",
      r'''<style type="text/css">
html,body {background-color: white;}

    </style> 
    ''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''
  <main>
    <div id="content"></div>
  </main>
'''), {"blurb": blurb, "blurb_image": blurb_image, "after_body":'''
     
     <script type="text/javascript" src="/media/sound-processing-utils.js?rr"></script>
     
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
  
  var source;

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
        var total = 0;
        for (var channel = 0; channel < input.numberOfChannels; ++channel) {
          var data = input.getChannelData (channel);
          if (memories.length <= channel) {memories.push (annoying.create_memory(audio));}
          var memory = memories [channel];
          for (var sample = 0; sample < data.length; ++sample) {
            annoying.process_sample (memory, data [sample]);
          }
          total += memory.average_excess;
        }
        var average = total/input.numberOfChannels;
        //$("#content").text(Math.round(average*100)).css("text-align", "right");
        $("#content").append($("<div>").css({display:"inline-block", width: 1, height: Math.round(average*100), "background-color": "black"}).text(" "));
      }
    },

    // Error callback
    function(err) {
      console.log('The following gUM error occured: ' + err);
    }
  );
  
});
</script>
'''}
  )
