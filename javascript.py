#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

import utils

global beforebody_js
global afterbody_js
afterbody_js = ''
beforebody_js = r'''
window.elidupree = {}
document.documentElement.className += ' javascript_enabled';
function remove_class(element, class_name) {
  element.className = element.className.replace(new RegExp('(\\s|^)'+class_name+'(\\s|$)'), ' ');
}
function add_event_listener(element, event_type, listener) {
  if (element.addEventListener) { element.addEventListener(     event_type, listener, false); }
  if (element.attachEvent     ) { element.attachEvent     ('on'+event_type, listener       ); }
}

function delete_cookie(name) {
  document.cookie = name+'=; expires=Thu, 01 Jan 1970 00:00:01 GMT; path=/';
}

var cookies_enabled = false;
if (typeof(document.cookie) === "string") {
  // They're... PROBABLY available if it's a string already?
  // However, just in case, I'll test to see if they function properly
  // (as opposed to, say, it being a regular string)
  document.cookie = 'testcookie1=foo';
  document.cookie = 'testcookie2=bar';
  if (document.cookie.indexOf('testcookie1') !== -1) {
    delete_cookie('testcookie1');
    delete_cookie('testcookie2');
    cookies_enabled = true;
    document.documentElement.className += ' cookies_enabled';
  }
}

function set_cookie(name, value, days) {
  var expires = "";
  var date;
  if (days) {
    date = new Date();
    date.setTime(date.getTime()+(days*24*60*60*1000));
    expires = "; expires="+date.toGMTString();
  }
  document.cookie = name+"="+value+expires+"; path=/";
}

function read_cookie(name) {
  if (!cookies_enabled) { return null; }
  var nameEQ = name + "=";
  var ca = document.cookie.split(';');
  var i;
  for(i=0;i < ca.length;i++) {
    var c = ca[i];
    while (c.charAt(0)===' ') {
      c = c.substring(1,c.length);
    }
    if (c.indexOf(nameEQ) === 0) {
      return c.substring(nameEQ.length,c.length);
    }
  }
  return null;
}
'''

print("TODO: add domain=elidupree.com to the cookie, but we can't do that while we're on localhost!")

# previously   p { margin-top: 0.75em; margin-bottom: 0.75em; }

def do_before_body(js_snippet):
  global beforebody_js
  beforebody_js = beforebody_js + '''
(function(){
''' + js_snippet + '''
})();'''
def do_after_body(js_snippet):
  global afterbody_js
  afterbody_js = afterbody_js + '''
(function(){
''' + js_snippet + '''
})();'''



def add_files(page_dict):
  global beforebody_js
  global afterbody_js
  utils.checked_insert(page_dict, '/before-body.js', beforebody_js)
  utils.checked_insert(page_dict, '/after-body.js', afterbody_js)
