#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import css

print('TODO: content_notices_disabled on the big content notices box can make the bottom bar show up in the wrong place on a very tall window')

css.insert('''

body.acobs div.bars_outer_box {
  background-color: #909090 /*#a00000*/; }
body.acobs div.comic_content_notice_text {
  color: black; }
body.acobs .meta_controls_coloring {
  color: blue; }
body.acobs div.comic_toggle_content_notices {
  color: black; }

body.acobs div.comic_transcript_inner {
  color: black; }
''')
print ("TODO: find a better way to make modified versions of CSS rules")



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
body.acobs div.comic_transcript_inner .dialogue { font-weight: bold; }
body.acobs div.comic_transcript_inner .TITLE { color: #804c00; /*#412f16;*/ }
body.acobs div.comic_transcript_inner .TONKS { color: #bf98af; /*#7f6574;*/ }
body.acobs div.comic_transcript_inner .GRANGER { color: #8080ff; /*#6060c0;*/ }
body.acobs div.comic_transcript_inner .HARRY { color: #ff0000; }
body.acobs div.comic_transcript_inner .WIRELESS { color: #737373; }
body.acobs div.comic_transcript_inner .VOLDEMORT { color: #80ff80; }
body.acobs div.comic_transcript_inner .HARRYMORT { color: #ba823f; }
body.acobs div.comic_transcript_inner .LESTRANGE { color: #c8ff00; }
body.acobs div.comic_transcript_inner .SNAPE { color: #809e80; }
body.acobs div.comic_transcript_inner .DUMBLEDORE { color: #8000c0; }
body.acobs div.comic_transcript_inner .deep_purple { color: #8000c0; }
body.acobs div.comic_transcript_inner .ZABINI { color: #eec832; }
body.acobs div.comic_transcript_inner .LUNA { color: #00ff00; }
body.acobs div.comic_transcript_inner .grey { color: '''+dialogue_50pct_grey+'''; }
body.acobs div.comic_transcript_inner .pure_blue { color: #0000ff; }
body.acobs div.comic_transcript_inner .bright_orange { color: #ffc800; }
body.acobs div.comic_transcript_inner .bright_green { color: #00ff00; }
body.acobs div.comic_transcript_inner .bright_red { color: #ff0000; }
body.acobs div.comic_transcript_inner .cyan { color: #00ffff; }
body.acobs div.comic_transcript_inner .pale_blue { color: #6483c4; }
body.acobs div.comic_transcript_inner .light_pink { color: #ff80c0; }
body.acobs div.comic_transcript_inner .dark_green { color: #326632; }
''')

