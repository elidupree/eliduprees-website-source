#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import bars
import blog

do_stuff = "record your own voice, play it back to yourself, and save the recordings to your computer."
blurb = "A tool to " + do_stuff
blurb_image ="/media/voice-practice-tool-screenshot.png?rr"
	  
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
.recent_box {float: right; background-color:#ccc;}
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
      '''+bars.bars_wrap({"games":True}, '''
  <main>
    <canvas id="histogram_canvas" width="320" height="80">
The histogram should appear here, but it hasn't. Maybe you don't have JavaScript enabled. Or maybe your browser doesn't support the canvas element.
    </canvas>
    <div class="page_description "></div>
    <div class="control_panels "></div>
    <div class="recent_box">
      <div class="recent_magnitudes_caption "></div>
      <canvas id="recent_magnitudes"></canvas>
    </div>
    <div class="recordings "></div>
  </main>
'''), {"blurb": blurb, "blurb_image": blurb_image, "after_body":'''
     <script type="text/javascript" src="/media/audiobuffer-to-wav.js?rr"></script>
     <script type="text/javascript" src="/media/download.js?rr"></script>
     <script type="text/javascript" src="/media/jszip.min.js?rr"></script>
     
     <!--<script type="text/javascript" src="/media/complex.js?rr"></script>
     <script type="text/javascript" src="/media/pitch.js?rr"></script>-->
     <script type="text/javascript" src="/media/pitchdetect.js?rr"></script>
     
     <script type="text/javascript" src="/media/voice-practice-tool-lib.js?rr"></script>
     
     <script type="text/javascript">
$(function(){
  initialize_voice_practice_tool ({
    page_description: "This page lets you '''+ do_stuff +''' Tested in Firefox and Chrome; may not work in other browsers.",
    recording_created: function (recording) {
      $(".recordings").append (recording.element);
    },
    sizes: function() {
      var width = $("body").width();
      var height = $("body").height();
      return {
        recent_magnitudes_width: Math.ceil (Math.min (width/3, 200)),  
        recent_magnitudes_height: Math.min (height/3, 200),
        histogram_width: width,
        histogram_height: Math.min (height/4, 128),
      }
    },
    controls_next_to_recent: true,
  });
});
</script>
'''}
  )
