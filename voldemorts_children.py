#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import css
import gimp_stuff


active_cw_color = "ff5050"
active_cw_color_dull = "be2626"
arrow_color_bright = "996100"
arrow_color_dull = "653c00"

css.insert('''

html.voldemorts_children div.comic_archive {
  color: #'''+arrow_color_bright+'''; }
html.voldemorts_children a.comic_archive_entry {
  border: 1px solid transparent; }
html.voldemorts_children a.comic_archive_entry:hover {
  border-color: #ddaa00; }
html.voldemorts_children div.comic_content_warning_text {
  color: white; }
html.voldemorts_children .meta_controls_coloring {
  color: #e09d00; }
html.voldemorts_children .comic_metabar {
  color: #ccc19a; }
html.voldemorts_children .metabar_content_warnings_enabled {
  color: #fff1c0; }
html.voldemorts_children .metabar_content_warnings_enabled.content_warning {
  color: #'''+active_cw_color+'''; }
html.voldemorts_children .metabar_content_warnings_disabled {
  color: #989073; }
html.voldemorts_children img.comic_nav_button_main {
  background-color: #'''+arrow_color_dull+''';
  border-color: black; }
html.voldemorts_children div.comic_nav_button:hover img.comic_nav_button_main {
  background-color: #'''+arrow_color_bright+''';
  border-color: black; }
html.voldemorts_children                                                      img.comic_nav_button_main.content_warning { background-color: #'''+active_cw_color_dull+'''; }
html.voldemorts_children                           div.comic_nav_button:hover img.comic_nav_button_main.content_warning { background-color: #'''+active_cw_color     +'''; }
html.voldemorts_children.content_warnings_disabled                            img.comic_nav_button_main.content_warning { background-color: #'''+arrow_color_dull    +'''; }
html.voldemorts_children.content_warnings_disabled div.comic_nav_button:hover img.comic_nav_button_main.content_warning { background-color: #'''+arrow_color_bright  +'''; }
html.voldemorts_children .comic_nav_content_warning {
  color: #'''+active_cw_color+'''; }
html.voldemorts_children div.comic_nav_button:hover .comic_nav_content_warning {
  color: #'''+active_cw_color+'''; }

html.voldemorts_children div.comic_transcript_inner {
  /*border: 1px dashed white;*/
  color: #ccc19a; }
html.voldemorts_children .post_content_section {
  background-color: #cccccc }
html.voldemorts_children .comment_body {
  background-color: #cccccc }
html.voldemorts_children div.all_comments:hover div.comment_body {
  background-color: #aaaaaa; }
html.voldemorts_children div.user_comment:hover>div.comment_body_hover_marker>*>div.comment_body {
  background-color: #cccccc; }
html.voldemorts_children .blog_post_metadata {
  background-color: rgba(204,204,204,.7) }
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
html.voldemorts_children div.comic_transcript_inner .dialogue { font-weight: bold; }
html.voldemorts_children div.comic_transcript_inner .TITLE { color: #c07200; /*#412f16;*/ }
html.voldemorts_children div.comic_transcript_inner .TONKS { color: #bf98af; /*#7f6574;*/ }
html.voldemorts_children div.comic_transcript_inner .GRANGER { color: #8080ff; /*#6060c0;*/ }
html.voldemorts_children div.comic_transcript_inner .HARRY { color: #ff0000; }
html.voldemorts_children div.comic_transcript_inner .WIRELESS { color: #737373; }
html.voldemorts_children div.comic_transcript_inner .VOLDEMORT { color: #80ff80; }
html.voldemorts_children div.comic_transcript_inner .HARRYMORT { color: #ba823f; }
html.voldemorts_children div.comic_transcript_inner .LESTRANGE { color: #c8ff00; }
html.voldemorts_children div.comic_transcript_inner .SNAPE { color: #9bc09b; /*#809e80;*/ }
html.voldemorts_children div.comic_transcript_inner .DUMBLEDORE { color: #aa00ff; /*#8000c0;*/ }
html.voldemorts_children div.comic_transcript_inner .deep_purple { color: #aa00ff; /*#8000c0;*/ }
html.voldemorts_children div.comic_transcript_inner .ZABINI { color: #eec832; }
html.voldemorts_children div.comic_transcript_inner .LUNA { color: #00ff00; }
html.voldemorts_children div.comic_transcript_inner .grey { color: '''+dialogue_50pct_grey+'''; }
html.voldemorts_children div.comic_transcript_inner .pure_blue { color: #3030ff; /*#0000ff;*/ }
html.voldemorts_children div.comic_transcript_inner .bright_orange { color: #ffc800; }
html.voldemorts_children div.comic_transcript_inner .bright_green { color: #00ff00; }
html.voldemorts_children div.comic_transcript_inner .bright_red { color: #ff0000; }
html.voldemorts_children div.comic_transcript_inner .cyan { color: #00ffff; }
html.voldemorts_children div.comic_transcript_inner .pale_blue { color: #6483c4; }
html.voldemorts_children div.comic_transcript_inner .light_pink { color: #ff80c0; }
html.voldemorts_children div.comic_transcript_inner .dark_green { color: #4b984b; /*#326632*/; }
''')


def convert_vc_page(page_dict):
  gimp_stuff.generate_vc_images(page_dict["xcf_base"], page_dict["list_index"])
