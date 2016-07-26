#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import html
import re
import utils
import css
import javascript

def make_page(title, head_stuff, body_stuff, extras = {}):
  jQuery ='''<script type="text/javascript" src="/media/jquery-3.0.0.min.js?rr"></script>'''
  jQuery_before = ""
  jQuery_after = ""
  if "jQuery_before" in extras:
    jQuery_before = jQuery
  else:
    jQuery_after = jQuery
  
  unbranded_title = re.sub(r"\s*⊂.*", "", title)
  image = (extras ["blurb_image"] if "blurb_image" in extras else "/media/colorful-background.jpg?rr")
  cooperation_stuff = ['''
    <meta name="twitter:card" content="summary">
    <meta name="twitter:site" content="@EliDupree">
    <meta property="og:site_name" content="Eli Dupree's website">
    <meta property="og:title" content="'''+ title +'''">
    <meta name="twitter:title" content="'''+ title +'''">
    <meta property="og:image" content="'''+ image +'''">
    <meta name="twitter:image" content="'''+ image +'''">
    ''']
  if "blurb" in extras:
    blurb = html.escape (utils.strip_tags (extras ["blurb"]))
    cooperation_stuff.append ('''
      <meta name="description" content="'''+ blurb +'''">
      <meta property="og:description" content="'''+ blurb +'''">
      <meta name="twitter:description" content="'''+ blurb +'''">
      ''')
  
  return '''<!DOCTYPE html>
<html lang="en" class="javascript_disabled'''+(' '+extras["html_class"] if "html_class" in extras else '')+'''">
  <head>
    <meta charset="utf-8" />
    <title>'''+title+'''</title>
    <link rel="shortcut icon" href="/favicon.ico" />
    <link rel="stylesheet" type="text/css" href="'''+css.domain_relative_url()+'''?rr">
    <link rel="alternate" type="application/atom+xml" href="/atom.xml" title="RSS (Atom) feed" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    '''+ "".join (cooperation_stuff) +'''
    <script type="text/javascript" src="/before-body.js?rr"></script>
    '''+ jQuery_before +'''
    '''+head_stuff+'''
  </head>
  <body>
    '''+body_stuff+'''
    '''+ jQuery_after +'''
    <script type="text/javascript" src="/after-body.js?rr"></script>
    '''+ (extras ["after_body"] if "after_body" in extras else "") +'''
  </body>
</html>'''
