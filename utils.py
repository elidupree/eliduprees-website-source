#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division



import re
import css
import html_pages

css.insert('''
span.inline_separator {
  margin: 0 0.3em; }
''')

inline_separator = '<span class="inline_separator"> &#8231; </span>'
# TODO 'https://www.elidupree.com':
canonical_scheme_and_domain = 'http://www.elidupree.com'

def background_image (name):
  return '<div><img role="presentation" alt="" class="background" src="/media/' + (name if name else 'colorful-background.jpg') + '?rr" /></div>'

def capitalize_string(string):
  if len(string) == 0:
    return string
  return string[0].upper()+string[1:]

def strip_tags(string):
  return re.sub(r"<.+?>","",string)

def format_for_url(string):
   # ,.!$+*'() are allowed in URLs, but I've ommitted them because they will almost always just make the URL look ugly, and some programs omit them from automatically linkified text URLs if they're at the end.
   # I use <i> tags for titles in some things that will be passed through this function.
  return re.sub(r"[^-a-zA-Z0-9_]","",re.sub(" ","-",strip_tags(string))).lower()
  
def checked_insert(dicti, idx, contents):
  if idx in dicti:
    raise Exception("checked_insert fail: "+idx)
  else:
    dicti[idx] = contents
    
def make_page (page_dict, idx, title, head, body, extras = {}):
  checked_insert (page_dict, idx + ".html", html_pages.make_page (title, head + '<link rel="canonical" href="' + canonical_scheme_and_domain + (extras ["canonical_path_override"] if "canonical_path_override" in extras else idx ) + '">', body, extras))