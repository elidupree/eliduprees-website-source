#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division



import css
import javascript

def make_page(title, head_stuff, body_stuff):
  return '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>'''+title+'''</title>
    <link rel="stylesheet" type="text/css" href="/'''+css.filename()+'''">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    '''+head_stuff+'''
  </head>
  '''+body_stuff+'''
  <script type="text/javascript" src="/'''+javascript.filename()+'''"></script>
</html>'''
