#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import bars
import blog

blurb = "A simple test case of TimeSteward physics."
blurb_image ="/media/bouncy-circles-screenshot.png?rr"
	  
def add_pages(page_dict):
  add_page (page_dict, "bouncy-circles", "Bouncy circles", '''<p>Bouncy-circles example for <a href="https://github.com/elidupree/time-steward">TimeSteward</a>. Click near any circle to make it zoom towards the center. (Known bug: Clicks land in the wrong place if you scroll the page.) The circles should move smoothly if your computer is fast enough, but this prototype isn't very efficient, so they may move jerkily instead.</p>''')
  add_page (page_dict, "simple-diffusion", "Simple diffusion", '''<p>Simple diffusion example for <a href="https://github.com/elidupree/time-steward">TimeSteward</a>. Click anywhere to add some ink. (Known bug: Clicks land in the wrong place if you scroll the page.)</p>''')
  add_page (page_dict, "quadtree-diffusion", "Quadtree diffusion", '''<p>Quadtree diffusion example for <a href="https://github.com/elidupree/time-steward">TimeSteward</a>. Click anywhere to add some ink. (Known bug: Clicks land in the wrong place if you scroll the page.)</p>''')
  
def add_page(page_dict, hyphenated_name, human_name, description):
  utils.make_page (page_dict,
    '/time-steward-examples/' + hyphenated_name,
      human_name + " ⊂ TimeSteward examples ⊂ Eli Dupree's website",
      r'''
      <style>
      html,body {background-color: white;}
      p {text-align: center; font-size: 110%; max-width: 50em; margin: 0.9em auto;}
      </style>
      <link rel="stylesheet" type="text/css" href="/media/time-steward-examples/emscripten-examples.css?rr">''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"misc":True}, '''
  <main>
    <div class="spinner" id='spinner'></div>
    <div class="emscripten" id="status">Downloading...</div>

    <div class="emscripten">
      <progress value="0" max="100" id="progress" hidden></progress>
    </div>

    
    <div class="emscripten_border">
      '''+ description +'''
      <canvas class="emscripten" id="canvas" oncontextmenu="event.preventDefault()"></canvas>
    </div>
    <textarea id="output" rows="8"></textarea>
  </main>
'''), {"blurb": blurb, "blurb_image": blurb_image, "after_body":'''
    <script type='text/javascript' src="/media/time-steward-examples/emscripten-examples.js?rr"></script>
    <script async type="text/javascript"  src="/media/time-steward-examples/'''+ hyphenated_name +'''.js?rr"></script>'''}
  )
