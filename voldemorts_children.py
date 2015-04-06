#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import re
import utils
import css
import blog
import comics
from voldemorts_children_pages import vc_pages
import gimp_stuff

print('TODO: content_notices_disabled on the big content notices box can make the bottom bar show up in the wrong place on a very tall window')

css.insert('''

body.voldemorts_children div.comic_content_notice_text {
  color: white; }
body.voldemorts_children div.comic_content_notice_main_text a {
  color: #ffc800; }
body.voldemorts_children div.comic_toggle_content_notices {
  color: #808080; }
body.voldemorts_children a.comic_toggle_content_notices {
  color: #ffc800; }
body.voldemorts_children a.comic_disable_content_notices {
  color: #ffc800; }
body.voldemorts_children div.comic_nav_button {
  color: #ffc800; }
body.voldemorts_children a.comic_nav_button:link{ color: #807059 /*#99994e;*/ /*#7e7e40*/ }
body.voldemorts_children a.comic_nav_button:visited{ color: #804c00; /*#4d6699;*/ /*#40557f*/ }
body.voldemorts_children div.comic_nav_button.content_notice a.comic_nav_button:link{ color: #ccb38f; /*#ffff82;*/ /*#7e7e40*/ }
body.voldemorts_children div.comic_nav_button.content_notice a.comic_nav_button:visited{ color: #cc7900; /*#81abff;*/ /*#40557f*/ }
body.voldemorts_children.content_notices_disabled div.comic_nav_button.content_notice a.vc_nav_button:link{ color: #807059 /*#99994e;*/ /*#7e7e40*/ }
body.voldemorts_children.content_notices_disabled div.comic_nav_button.content_notice a.vc_nav_button:visited{ color: #804c00; /*#4d6699;*/ /*#40557f*/ }
body.voldemorts_children div.comic_transcript_inner {
  /*border: 1px dashed white;*/
  color:white; }
body.voldemorts_children div.comic_transcript_inner a {
  color: #ffc800; }
body.voldemorts_children .post_content_section {
  background-color: #cccccc }
body.voldemorts_children .comment_body {
  background-color: #cccccc }
body.voldemorts_children div.all_comments:hover div.comment_body {
  background-color: #aaaaaa; }
body.voldemorts_children div.user_comment:hover>div.comment_body_hover_marker>*>div.comment_body {
  background-color: #cccccc; }
body.voldemorts_children .blog_post_metadata {
  background-color: rgba(204,204,204,.7) }
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
body.voldemorts_children div.comic_transcript_inner .dialogue { font-weight: bold; }
body.voldemorts_children div.comic_transcript_inner .TITLE { color: #804c00; /*#412f16;*/ }
body.voldemorts_children div.comic_transcript_inner .TONKS { color: #bf98af; /*#7f6574;*/ }
body.voldemorts_children div.comic_transcript_inner .GRANGER { color: #8080ff; /*#6060c0;*/ }
body.voldemorts_children div.comic_transcript_inner .HARRY { color: #ff0000; }
body.voldemorts_children div.comic_transcript_inner .WIRELESS { color: #737373; }
body.voldemorts_children div.comic_transcript_inner .VOLDEMORT { color: #80ff80; }
body.voldemorts_children div.comic_transcript_inner .HARRYMORT { color: #ba823f; }
body.voldemorts_children div.comic_transcript_inner .LESTRANGE { color: #c8ff00; }
body.voldemorts_children div.comic_transcript_inner .SNAPE { color: #809e80; }
body.voldemorts_children div.comic_transcript_inner .DUMBLEDORE { color: #8000c0; }
body.voldemorts_children div.comic_transcript_inner .deep_purple { color: #8000c0; }
body.voldemorts_children div.comic_transcript_inner .ZABINI { color: #eec832; }
body.voldemorts_children div.comic_transcript_inner .LUNA { color: #00ff00; }
body.voldemorts_children div.comic_transcript_inner .grey { color: '''+dialogue_50pct_grey+'''; }
body.voldemorts_children div.comic_transcript_inner .pure_blue { color: #0000ff; }
body.voldemorts_children div.comic_transcript_inner .bright_orange { color: #ffc800; }
body.voldemorts_children div.comic_transcript_inner .bright_green { color: #00ff00; }
body.voldemorts_children div.comic_transcript_inner .bright_red { color: #ff0000; }
body.voldemorts_children div.comic_transcript_inner .cyan { color: #00ffff; }
body.voldemorts_children div.comic_transcript_inner .pale_blue { color: #6483c4; }
body.voldemorts_children div.comic_transcript_inner .light_pink { color: #ff80c0; }
body.voldemorts_children div.comic_transcript_inner .dark_green { color: #326632; }
''')


def convert_vc_page(page_dict):
  gimp_stuff.generate_vc_images(page_dict["xcf_base"], page_dict["list_index"])
