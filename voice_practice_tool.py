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
  
var source;
  var analyzer = audio.createAnalyser ();
  var recorder = audio.createScriptProcessor (4096, 1, 1);
  var current_recording = {buffer: audio.createBuffer (1, audio.sampleRate, audio.sampleRate)}
  analyzer.connect (recorder);
  
  analyzer.fftSize = 2048;
  var buffer_length = analyzer.frequencyBinCount; 
  var frequency_data = new Uint8Array(buffer_length);
  
  recorder.onaudioprocess = function (event) {
    var input = events.inputBuffer.getChannelData (0);
    
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
  
  function draw () {
    requestAnimationFrame (draw);
    analyzer.getByteFrequencyData (frequency_data);
    canvas.fillStyle = "rgb(0, 0, 0)"
    canvas.strokeStyle = "rgb(255, 0, 0)"
    canvas.fillRect (0, 0, 1024, 256);
    canvas.beginPath ();
    for (var I = 0; I <1024;++I) {
      canvas.moveTo (I, 256);
      canvas.lineTo (I, 256 - frequency_data [I]);
    }
    canvas.stroke ();
  }
  draw ();
});
    </script>'''}
  )
