#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import bars
import blog

	  
def add_page(page_dict):
  utils.make_page (page_dict,
    '/design-generator',
      "Design generator ⊂ Eli Dupree's website",
      r'''<style type="text/css">
html,body {background-color: white;}
    </style> 
    ''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''<main><div id="content">
      <canvas id="canvas" width="1056" height="816">
      </div>
     </main>'''), {"after_body":'''
     <script type="text/javascript" src="/media/paper-full.js?rr"></script>
     <script type="text/paperscript" src="/media/design-generator.js?rr" canvas="canvas"></script>'''}
  )
