#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division



import re
import html

import css
import html_pages

css.insert('''
span.inline_separator {
  margin: 0 0.3em; }
''')

inline_separator = '<span class="inline_separator"> &middot; </span>'
canonical_scheme_and_domain = 'https://www.elidupree.com'

def background_image (name ='colorful-background.jpg'):
  return '<div><img role="presentation" alt="" class="background" src="/media/' + name + '?rr" /></div>'

def capitalize_string(string):
  if len(string) == 0:
    return string
  return string[0].upper()+string[1:]

def strip_tags(string):
  return re.sub(r"<.+?>","",string)

def word_count (string):
  return len(re. findall (r"\w[\w']*", string))

def auto_paragraphs (string):
  return re.sub(r"""(?m)^([\w"]|<strong|<em|\[?\?\?\?\?).+?$""", lambda match: "<p>" + match.group (0) + "</p>", string)

def format_for_url(string):
   # ,.!$+*'() are allowed in URLs, but I've ommitted them because they will almost always just make the URL look ugly, and some programs omit them from automatically linkified text URLs if they're at the end.
   # I use <i> tags for titles in some things that will be passed through this function.
  return re.sub(r"[^-a-zA-Z0-9_]","",re.sub(" ","-",strip_tags(string))).lower()

def import_html (path):
  with open (path, "r", encoding="utf-8") as file:
    matches = re.search (
      re.escape(r"<!-- eliduprees-website-source head -->")
      +"(.*?)"+
      re.escape(r"<!-- /eliduprees-website-source head -->")
      +".*?"+
      re.escape(r"<!-- eliduprees-website-source body -->")
      +"(.*?)"+
      re.escape(r"<!-- /eliduprees-website-source body -->")
      +".*?"+
      re.escape(r"<!-- eliduprees-website-source after_body -->")
      +"(.*?)"+
      re.escape(r"<!-- /eliduprees-website-source after_body -->")
      , file.read(), re.DOTALL)
    return (matches.group (1), matches.group (2), matches.group (3))

def checked_insert(dicti, idx, contents):
  if idx in dicti:
    raise Exception("checked_insert fail: "+idx)
  else:
    dicti[idx] = contents
    
def make_page (page_dict, idx, title, head, body, extras = {}):
  canonical_URL = canonical_scheme_and_domain + (extras ["canonical_path_override"] if "canonical_path_override" in extras else idx ) 
  checked_insert (page_dict, 
      idx + ".html", 
      html_pages.make_page (
        title,
        head + 
        '<link rel="canonical" href="' + canonical_URL + '">' +
        '<meta property="og:url" content="' + canonical_URL + '">',
        body, extras))
