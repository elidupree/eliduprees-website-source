#!/usr/bin/python3
# -*- coding: utf-8 -*-

from post_contents_utils import *

yali_font = "Kreon" #"Roboto Slab"
rinn_font = "Kadwa" #"Arvo" #"Inika" #"Crete Round"
chapter_font = "Alegreya SC"

def fonts_css(fonts_path, mode="web"):
  def font_rules(name_style):
    if mode=="web":
      # note: we have to use double quotes around the urls, not single quotes,
      # because idupree-websitepy rewriting is only compatible with double quotes
      return '''
  src: url("'''+fonts_path+name_style+'''.eot?rr"); /* IE9 Compat Modes */
  src: local(''),
       url("'''+fonts_path+name_style+'''.eot?rr#iefix") format('embedded-opentype'), /* IE6-IE8 */
       url("'''+fonts_path+name_style+'''.woff2?rr") format('woff2'), /* Super Modern Browsers */
       url("'''+fonts_path+name_style+'''.woff?rr") format('woff'), /* Modern Browsers */
       url("'''+fonts_path+name_style+'''.ttf?rr") format('truetype'), /* Safari, Android, iOS */
       url("'''+fonts_path+name_style+'''.svg?rr#Kadwa") format('svg'); /* Legacy iOS */
       '''
    else:
      return '''
  src: url("'''+fonts_path+name_style+'''.ttf");
       '''
      
  
  return """
/* kadwa-regular - latin */
@font-face {
  font-family: 'Kadwa';
  font-style: normal;
  font-weight: 400;
  """+font_rules("kadwa-v5-latin-regular")+"""
}

/* kadwa-700 - latin */
@font-face {
  font-family: 'Kadwa';
  font-style: normal;
  font-weight: 700;
  """+font_rules("kadwa-v5-latin-700")+"""
}

/* kreon-regular - latin */
@font-face {
  font-family: 'Kreon';
  font-style: normal;
  font-weight: 400;
  """+font_rules("kreon-v24-latin-regular")+"""
}

/* kreon-700 - latin */
@font-face {
  font-family: 'Kreon';
  font-style: normal;
  font-weight: 700;
  """+font_rules("kreon-v24-latin-700")+"""
}

/* alegreya-sc-800 - latin */
@font-face {
  font-family: 'Alegreya SC';
  font-style: normal;
  font-weight: 800;
  """+font_rules("alegreya-sc-v15-latin-800")+"""
}

/* alegreya-sc-regular - latin */
@font-face {
  font-family: 'Alegreya SC';
  font-style: normal;
  font-weight: 400;
  """+font_rules("alegreya-sc-v15-latin-regular")+"""
}

/* lexend-regular - latin */
@font-face {
  font-family: 'Lexend';
  font-style: normal;
  font-weight: 400;
  """+font_rules("lexend-v12-latin-regular")+"""
}

/* lexend-700 - latin */
@font-face {
  font-family: 'Lexend';
  font-style: normal;
  font-weight: 700;
  """+font_rules("lexend-v12-latin-700")+"""
}
"""

head = """<style>

.table_of_contents_chapter {
  text-indent: 2em;
}
.table_of_contents_chapter .chapter_link {
  margin-right: 0.3em;
}
.table_of_contents_remaining {
  text-indent: 2em;
  font-style: italic;
}
div.blog_post h1 {
  text-align: center;
  padding-left: 0;
  padding-right: 0;
}
div.blog_post h2 {
  text-align: center;
  padding-left: 0;
  padding-right: 0;
  font-weight: 800;
  font-family: '"""+chapter_font+"""', serif;
}
div.blog_post p {
  clear: both;
}
div.blog_post img {
  display: block;
  margin: 2.8em auto;
  max-width: 100%;
}
div.blog_post div.end-of-texts {
  clear: both;
}
div.blog_post p.text {
  border-radius: 1.3em;
  max-width: 60%;
  text-indent: 0;
  padding: 6px 12px;
  margin: 1px 0;
  font-family: Arial, Helvetica, sans-serif;
}
p.text.right {
  background-color: #87e520;
  float: right;
}
p.text.left {
  background-color: #e5e4e4;
  float: left;
}
.story_content_warning_header {
  margin-top: 1.1em;
}
div.blog_post p {
  font-family: '"""+rinn_font+"""', serif;
}
div.blog_post.yali-narration p, .yali-narration.yali-narration.yali-narration p {
  /*font-family: Georgia, serif;*/
  font-family: '"""+yali_font+"""', serif;
  font-size: 112%;
  /*font-style: italic;*/
  line-height: 1.3em;
}
/*.yali-narration em {
font-weight: bold;
}*/
div.novel-current-status.novel-current-status.novel-current-status p, div.table_of_contents, div.table_of_contents p, div.hidden_cws, div.hidden_cws.hidden_cws.hidden_cws p, div.main_content_warnings p {
  font-family: Arial, Helvetica, sans-serif;
}
.prayer {
  text-align: center;
}
div.blog_post .prayer p {
  text-indent: 0;
}

div.blog_post img.emoji {
  display: inline-block;
  width: 1.5em;
  height: 1.5em;
  margin: 0 -.125em;
  vertical-align: middle;
}

div.blog_post img.rav-section-break {
  width: 90%;
  height: auto;
  margin: 2em auto;
}
div.blog_post img.rav-section-break.nonaligned {
  width: 80%;
}

html.debug_mode div.blog_post p.unnecessary_page_number {
  display: block;
  text-align: center;
  font-size: smaller;
  font-family: Arial, Helvetica, sans-serif;
  padding-bottom: 1.5em;
}

"""+fonts_css("/media/fonts/")+"""


  </style>
  """
