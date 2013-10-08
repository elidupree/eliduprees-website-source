#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


global afterbody_js
afterbody_js = r'''
document.body.className += ' javascript_enabled';
function remove_class(element, class_name) {
  element.className = element.className.replace(new RegExp('(\\s|^)'+class_name+'(\\s|$)'), ' ');
}
function add_event_listener(element, event_type, listener) {
  if (element.addEventListener) { element.addEventListener(     event_type, listener, false); }
  if (element.attachEvent     ) { element.attachEvent     ('on'+event_type, listener       ); }
}
'''

# previously   p { margin-top: 0.75em; margin-bottom: 0.75em; }

def do_after_body(js_snippet):
  global afterbody_js
  afterbody_js = afterbody_js + '''
(function(){
''' + js_snippet + '''
})();'''


def add_event_listener(element, event_type, listener):
  return "if ("+element+"."+"addEventListener) { "+element+"."+"addEventListener('"+event_type+"', "+listener+", false); }"+"if ("+element+"."+"attachEvent) { "+element+"."+"attachEvent('on"+event_type+"', "+listener+"); }"
  
def filename():
  return "media/scripts.js"
def build():
  # maybe minify it?
  return afterbody_js
