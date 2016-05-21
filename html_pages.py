#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division



import css
import javascript

def make_page(title, head_stuff, body_stuff, extras = {}):
  return '''<!DOCTYPE html>
<html lang="en"'''+(' class="'+extras["html_class"]+'"' if "html_class" in extras else '')+'''>
  <head>
    <meta charset="utf-8" />
    <title>'''+title+'''</title>
    <link rel="shortcut icon" href="/favicon.ico" />
    <link rel="stylesheet" type="text/css" href="'''+css.domain_relative_url()+'''?rr">
    <link rel="alternate" type="application/atom+xml" href="/atom.xml" title="RSS (Atom) feed" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <!--<meta http-equiv="refresh" content="5">-->
    <script type="text/javascript" src="/before-body.js?rr"></script>
    '''+head_stuff+'''
  </head>
  <body>
    '''+body_stuff+'''
    <script type="text/javascript" src="/after-body.js?rr"></script>
  </body>
</html>'''
