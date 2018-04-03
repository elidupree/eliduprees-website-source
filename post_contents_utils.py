#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import exmxaxixl

def hidden_cw_box(contents):
  return '''<div class="hidden_cw_box">
    <a href="javascript:;" class="enable_content_warnings_button reveal_cw_button">Reveal content warnings</a>
    <div class="hidden_cws">
      '''+contents+'''
      <a class="disable_content_warnings_button" href="javascript:;" >(hide content warnings)</a>
    </div>
  </div>'''

def secondary_hidden_cw_box(contents):
  return '''<div class="hidden_cw_box secondary">
    '''+contents+'''
    <a class="disable_content_warnings_button" href="javascript:;" >(hide content warnings)</a>
  </div>'''
  
def content_warning_header(contents):
  return '''

<div class="story_content_warning_header">
  
  '''+hidden_cw_box('''
  '''+contents+'''
  <p>If you see other material that should be marked (such as common triggers or phobias), '''+exmxaxixl.a('e-mail me')+'''. I am serious about web accessibility, and I will respond to your concerns as soon as I can manage.</p>
  ''')+'''
</div>'''

def content_warning_section(contents):
  return secondary_hidden_cw_box('This section depicts '+contents+'.')
  