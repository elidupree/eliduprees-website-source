#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import css

css.insert('''

html.acobs div.bars_outer_box {
  background-color: #909090 /*#a00000*/; }
html.acobs div.comic_content_warning_text {
  color: black; }
html.acobs .meta_controls_coloring {
  color: blue; }
html.acobs div.comic_toggle_content_warnings {
  color: black; }

html.acobs div.comic_transcript_inner {
  color: black; }
''')



dialogue_50pct_grey = '#8c8c8c'
dialogue_name_replace = {
  "TITLE":True,
  "TONKS":True,"GRANGER":True,"HARRY":True,"VOLDEMORT":True,"DUMBLEDORE":True,"ZABINI":True,"LUNA":True,
  "WIRELESS":True,"LESTRANGE":True,"SNAPE":True,
  "PRESENT HARRY":"HARRY",
  "PRESENT GRANGER":"GRANGER",
  "FUDGE":"grey", "PAST GRANGER":"grey", "MCGONAGALL":"grey", "RON":"grey", "DRACO":"grey",
}
css.insert('''
html.acobs div.comic_transcript_inner .dialogue { font-weight: bold; }
html.acobs div.comic_transcript_inner .TITLE { color: #804c00; /*#412f16;*/ }
html.acobs div.comic_transcript_inner .TONKS { color: #bf98af; /*#7f6574;*/ }
html.acobs div.comic_transcript_inner .GRANGER { color: #8080ff; /*#6060c0;*/ }
html.acobs div.comic_transcript_inner .HARRY { color: #ff0000; }
html.acobs div.comic_transcript_inner .WIRELESS { color: #737373; }
html.acobs div.comic_transcript_inner .VOLDEMORT { color: #80ff80; }
html.acobs div.comic_transcript_inner .HARRYMORT { color: #ba823f; }
html.acobs div.comic_transcript_inner .LESTRANGE { color: #c8ff00; }
html.acobs div.comic_transcript_inner .SNAPE { color: #809e80; }
html.acobs div.comic_transcript_inner .DUMBLEDORE { color: #8000c0; }
html.acobs div.comic_transcript_inner .deep_purple { color: #8000c0; }
html.acobs div.comic_transcript_inner .ZABINI { color: #eec832; }
html.acobs div.comic_transcript_inner .LUNA { color: #00ff00; }
html.acobs div.comic_transcript_inner .grey { color: '''+dialogue_50pct_grey+'''; }
html.acobs div.comic_transcript_inner .pure_blue { color: #0000ff; }
html.acobs div.comic_transcript_inner .bright_orange { color: #ffc800; }
html.acobs div.comic_transcript_inner .bright_green { color: #00ff00; }
html.acobs div.comic_transcript_inner .bright_red { color: #ff0000; }
html.acobs div.comic_transcript_inner .cyan { color: #00ffff; }
html.acobs div.comic_transcript_inner .pale_blue { color: #6483c4; }
html.acobs div.comic_transcript_inner .light_pink { color: #ff80c0; }
html.acobs div.comic_transcript_inner .dark_green { color: #326632; }
''')

