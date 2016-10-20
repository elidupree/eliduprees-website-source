#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import bars
import blog

do_stuff = "compose music through programming."
blurb = "A tool to " + do_stuff
blurb_image ="/media/voice-practice-tool-screenshot.png?rr"
	  
def add_page(page_dict):
  utils.make_page (page_dict,
    '/codecophony',
      "Codecophony: compose music through programming ⊂ Eli Dupree's website",
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
.recordings,.generated {
    display: flex;
    flex-wrap: wrap-reverse;
}
.page_description {padding:0.3em 2em; font-size: 110%;}

main,.tool_box_top {
display: flex;
justify-content: space-between;
}
.tool_box,.codecophony_space {
flex: 1 1 50%;
min-width: 0;
}

.generated {
  border-top:3px solid black;
}
div.item {display: inline-block; margin:3px; background-color:#bbb;}

textarea {
  width: 96%;
}
textarea:focus {
  height: 60vh;
}

#sandbox {display: none;}

.fa-stack.force_small {width:1em; height:1em; line-height:0.7em;}
span.no_underlay {position: absolute; top: 0; left: 0; z-index: 1;}
    </style> 
    <link rel="stylesheet" href="/media/font-awesome-4.6.3/css/font-awesome.min.css?rr">
    ''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''
<main>
  <iframe sandbox="allow-scripts" id="sandbox" src="/media/codecophony-iframe.html"></iframe>
  <div class="tool_box">
    <div class="tool_box_top">
      <canvas id="histogram_canvas" width="320" height="80">
The histogram should appear here, but it hasn't. Maybe you don't have JavaScript enabled. Or maybe your browser doesn't support the canvas element.
      </canvas>
      <div class="recent_box">
        <div class="recent_magnitudes_caption "></div>
        <canvas id="recent_magnitudes"></canvas>
      </div>
    </div>
    <div class="control_panels "></div>
    <div class="recordings "></div>
    <div class="generated "></div>
  </div>
  <div class="codecophony_space"></div>
</main>
'''), {"blurb": blurb, "blurb_image": blurb_image, "after_body":'''
     <script type="text/javascript" src="/media/audiobuffer-to-wav.js?rr"></script>
     <script type="text/javascript" src="/media/download.js?rr"></script>
     <script type="text/javascript" src="/media/jszip.min.js?rr"></script>
     
     <!--<script type="text/javascript" src="/media/complex.js?rr"></script>
     <script type="text/javascript" src="/media/pitch.js?rr"></script>-->
     <script type="text/javascript" src="/media/pitchdetect.js?rr"></script>
     <script type="text/javascript" src="/media/audio-loader.min.js?rr"></script>
     
     <script type="text/javascript" src="/media/voice-practice-tool-lib.js?rr"></script>
    
     <script type="text/javascript" src="/media/codecophony.js?rr"></script>
'''}
  )
  
