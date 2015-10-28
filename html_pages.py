#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division



import css
import javascript

def make_page(title, head_stuff, body_stuff, extras = {}):
  return '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>'''+title+'''</title>
    <link rel="shortcut icon" href="/favicon.ico" />
    <link rel="stylesheet" type="text/css" href="'''+css.domain_relative_url()+'''?rr">
    <link rel="alternate" type="application/atom+xml" href="/atom.xml" title="RSS (Atom) feed" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    '''+head_stuff+'''
  </head>
  <body'''+(' class="'+extras["body_class"]+'"' if "body_class" in extras else '')+'''>
    <script type="text/javascript" src="/before-body.js?rr"></script>
    '''+body_stuff+'''
    <script type="text/javascript" src="/after-body.js?rr"></script>
  </body>
</html>'''
