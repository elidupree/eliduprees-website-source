#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import bars
import blog

blurb = "A simple test case of TimeSteward physics."
blurb_image ="/media/voice-practice-tool-screenshot.png?rr"
	  
def add_pages(page_dict):
  add_page (page_dict, "bouncy-circles", "Bouncy circles")
  add_page (page_dict, "simple-diffusion", "Simple diffusion")
  
def add_page(page_dict, hyphenated_name, human_name):
  utils.make_page (page_dict,
    '/time-steward-examples/' + hyphenated_name,
      human_name + " ⊂ TimeSteward examples ⊂ Eli Dupree's website",
      r'''
      <style>
      html,body {background-color: white;}
      </style>
      <link rel="stylesheet" type="text/css" href="/media/time-steward-examples/emscripten-examples.css?rr">''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"misc":True}, '''
  <main>
    <div class="spinner" id='spinner'></div>
    <div class="emscripten" id="status">Downloading...</div>

    <div class="emscripten">
      <progress value="0" max="100" id="progress" hidden=1></progress>
    </div>

    
    <div class="emscripten_border">
      <canvas class="emscripten" id="canvas" oncontextmenu="event.preventDefault()"></canvas>
    </div>
    <textarea id="output" rows="8"></textarea>
  </main>
'''), {"blurb": blurb, "blurb_image": blurb_image, "after_body":'''
    <script type='text/javascript' src="/media/time-steward-examples/emscripten-examples.js?rr"></script>
    <script async type="text/javascript"  src="/media/time-steward-examples/'''+ hyphenated_name +'''.js?rr"></script>'''}
  )
