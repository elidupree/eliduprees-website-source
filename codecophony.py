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

.project_editor {display: none;}
.project_editor_inner,.tool_box_top {
display: flex;
justify-content: space-between;
}
.tool_box,.codecophony_space {
flex: 1 1 50%;
min-width: 0;
}

.project_select {
  padding: 4%;
}
.project_select p {
  text-align: center;
  font-size: 130%;
}
.project_select h1 {
  text-align: center;
}
.project_select h2 {
  text-align: center;
  font-weight: bold;
  font-size: 150%;
}
.project_select button {
  font-weight: bold;
  font-size: 150%;
}
.project_select code {
  white-space: nowrap;
  background-color: #ddd;
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
  <div class="project_select ">
    <h1>Welcome to Codecophony! This is an early prototype.</h1>
    <p>Codecophony is a tool to compose music through programming, although it may be usable by non-programmers as well.</p>
    <p>Create a new "project" using the button below, then edit it using the "edit" button. Then you'll see the edit screen. The left side lets you record sounds just like my <a href="/voice-practice-tool">voice practice tool</a>. The right side lets you create scripts. Here's an example script (try it out!):</p>
    <pre>var notes = codecophony.scrawl (
  `with instrument acoustic_guitar_steel duration 0.28

play 0 then 2 then 3 then 5 then 7 lasting 4
[with pitch -7 start -0.05 instrument trumpet
  play 0 then 2 then 3 then 5 then 7 lasting 4
]
[with pitch 0 start -0.02
  play -3 0 then -4 2 then -3 3 then -4 5 then -4 7 lasting 4
]
`
)
items.example_notes = notes;
var example_sequence = items.example_sequence = codecophony.render_notes (notes);
example_sequence.start += 4800;
var a = items.input_sequence;
codecophony.amplify (a, 0.14);
items.combined_sequence = codecophony.add_sequences ([example_sequence, a]);
</pre>
  
  <p>For this script to work, you will also need to import the <code>trumpet</code> and <code>acoustic_guitar_steel</code> instruments using the menu in the top right, and record something and rename the recording "input_sequence".</p>
  
  <p>These scripts are written in JavaScript. <code>codecophony</code> is a table containing various utility functions. <code>items</code> is a proxy table that lets you examine the "items" (recordings and other stuff) that you see on screen, and create new ones. A "sequence" is either a Float32Array, like those used by the web audio API, or <code>{start: &lt;starting time in number of 44100 Hz samples&gt;, data: Float32Array}</code>. lodash is available as <code>_</code>.</p>
  
  <h2>The codecophony.scrawl format:</h2>
  <p><code>play</code> starts a new note at the default start time. <code>and</code> starts a new note at the same time as the last note you made. <code>then</code> starts a new note immediately after the last note ends. <code>with</code> sets defaults for all notes that come after it, until the end of the current [] block.</p>
  
  <p>Everything else sets the <em>attributes</em> of the note objects. <code>pitch</code> is additive, measured in number of semitones, starting at middle C. <code>duration</code> and <code>volume</code> are multiplicative. Everything else (like <code>instrument</code>) just overwrites its previous value. A number with no attribute name in front of it means pitch by default. Times are measured in seconds.</p>
  
  <p>A few other attributes exist. I'll eventually write full documentation.</p>
  
  <p>Your creations will be autosaved in your browser. I will eventually make a way to import and export projects, but I haven't yet. Right now, you can only copy/paste the scripts and save the generated sound files.</p>
  
  </div>
  <div class="project_editor "><div class="project_editor_inner ">
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
  </div></div>
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
  
