#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import css
import top_bar
import blog
import utils
import exmxaxixl

home_page_category_height = 12
home_page_contents_height = home_page_category_height + 5.625

css.insert('''
div.bars_outer_box {
  min-height: 100%;
  position: relative;
}
div.bars_inner_box {
  padding-bottom: 5em;
}
@media screen and (max-width: 30em) {
  div.bars_inner_box { padding-bottom: 6em; } }
@media screen and (max-width: 20em) {
  div.bars_inner_box { padding-bottom: 7em; } }
@media screen and (max-width: 14em) {
  div.bars_inner_box { padding-bottom: 8em; } }
@media screen and (max-width: 13em) {
  div.bars_inner_box { padding-bottom: 9em; } }
@media screen and (max-width: 12em) {
  div.bars_inner_box { padding-bottom: 10em; } }

div.bottom_bar {
  position: absolute;
  bottom: 0;
  width: 100%;
  font-family: Arial, Helvetica, sans-serif;
  text-align: center;
  background-color: black;
  background-image: url("/media/top-bar-background.png?rr");
  background-size: 100% 100%; }
.voldemorts_children div.bottom_bar {
  background-image: url("/media/top-bar-background-vc.png?rr"); }
div.bottom_bar_inner {
  padding: 0.25em;
}
.bottom_bar_short {
  white-space: nowrap; }

address.eli_exmxaxixl {
  display: inline;
  font-style: normal; }


div.home_page_outer span.top_bar_category.games {
  background-image: url("/media/green-caves-screenshot.png?rr");
  background-size: 24em 24em;
  background-position: center center;}
div.home_page_outer span.top_bar_category.comics {
  background-image: url("/media/comics-thumbnail.png?rr");
  background-size: auto;
  background-position: center center;}


div.home_page_buffer {
  position: relative;
  height: 50%; }
div.home_page_outer {
  position: relative;
  font-family: Arial, Helvetica, sans-serif;
  margin-top: -'''+str(home_page_contents_height/2)+'''em;
  height: '''+str(home_page_contents_height)+'''em;
  max-width: '''+str(top_bar.categories_get_squished_width)+'''em;
  margin-left: auto;
  margin-right: auto; }
div.home_page_categories {
  margin-left:auto; margin-right:auto;
  max-width:'''+str(top_bar.all_categories_width)+'''em; }
div.home_page_bottom {
  margin-top: 0.5em;
  height: 4.5em;
  text-align: center; }
div.home_page_outer span.top_bar_category {
  height: '''+str(home_page_category_height)+'''em;
  background-size: 100% 100%; }
div.home_page_outer span.top_bar_category_text {
  font-size: 160%; }
  
  
div.home_page_buffer div.top_bar_home {
  top: 50%;
  margin-top: -'''+str(4+home_page_contents_height/4)+'''em;
  width: 100%; }
div.home_page_buffer img.top_bar_home_image {
  display: block;
  margin: 0 auto;
  width:'''+str(top_bar.home_image_width*2)+'''em; height:'''+str(top_bar.bar_height*2)+'''em; }
div.home_page_buffer span.top_bar_home_text {
  width: 100%;
  text-align: center;
  font-size: 150%;
  padding: 0; }
div.home_page_outer h2 {color: #776;font-size: 150%; font-weight: bold; margin-bottom: -0.2em;}
div.home_page_recent_updates {display: inline-block; font-size: 75%; background-color:#ffc; padding: 0.7em;border-radius:1.3em; margin-top:4em;}
div.home_page_outer div.stream_media_reference_outer {text-align: left; }
div.home_page_outer a.stream_media_reference {text-align: left; background-color: transparent; font-weight: normal;}

.feed_icon_14x14 {width:14px; height:14px;}
  
@media screen and (max-height: 34em) {
  div.home_page_buffer div.top_bar_home {
    top: 100%;
    margin-top: -'''+str(34/4 + 4+home_page_contents_height/4)+'''em; }
  div.home_page_buffer {
    height: 17em; }
}
@media screen and (max-height: 26em) {
  div.home_page_buffer {
    position: absolute;
    height: 100%; }
  div.home_page_outer {
    position: absolute;
    bottom: 0; }
  div.home_page_buffer div.top_bar_home {
    position: relative;
    top: 0;
    margin-top: 0.3em; }
  div.home_page_buffer img.top_bar_home_image {
    display: inline-block;
    padding-left: 0.8em; }
  div.home_page_buffer span.top_bar_home_text {
    padding-left: 0.8em;
    width: inherit; }
}
@media screen and (max-height: 19.2em) {
  div.home_page_buffer div.top_bar_home {
    display: none; }
}
@media screen and (min-height: 20.8em) and (max-height: 26em) and (max-width: 19em) {
  div.home_page_buffer span.top_bar_home_text {
    width: 6em;
    text-align: left; }
}
@media screen and (max-height: 20.8em) and (max-width: 19em) {
  div.home_page_buffer img.top_bar_home_image {
    display: none; }
}
@media screen and (max-width: 15.5em) {
  div.home_page_buffer img.top_bar_home_image {
    display: none; }
}
  
@media screen and (max-width: '''+str(top_bar.categories_get_squished_width)+'''em) {
  div.home_page_categories {
    margin-left:'''+str(100 * top_bar.category_border_width / top_bar.categories_get_squished_width)+'''%; }
  div.home_page_outer span.top_bar_category_text {
    width: 100%;
    border-top-left-radius:0;
    border-bottom-left-radius:'''+str(top_bar.button_border_radius)+'''em; }
}
@media screen and (max-width: 28em) {
  div.home_page_outer span.top_bar_category_text {
    font-size: 120%;
    font-size: 5.6vw; }
  div.home_page_bottom_inner {
    font-size: 80%;
    font-size: 4vw; }
}
@media screen and (min-height: '''+str(home_page_contents_height)+'''em) {
  div.home_page_outer div.bars_inner_box {
    padding-bottom: 0; }
}
@media screen and (max-height: '''+str(home_page_contents_height)+'''em) {
  div.home_page_buffer {
    display: none; }
  div.home_page_outer {
    margin-top: 0;
    height: 100%;
    width: 100%; }
  div.home_page_categories {
    position: absolute;
    top: 0;
    bottom: 5em;
    right: 0;
    left: 0; }
  div.home_page_outer a.top_bar_category_link {
    height: 100%; }
  div.home_page_outer span.top_bar_category {
    height: 100%; }
  div.home_page_bottom {
    position: absolute;
    bottom: 0;
    right: 0;
    left: 0; }
}
''')

def bottom_bar_contents(info):
  return 'Please share this!'+utils.inline_separator+'<address class="eli_exmxaxixl bottom_bar_short">Contact: '+exmxaxixl.a(exmxaxixl.axdxrxexsxs)+'</address>'+utils.inline_separator+'<a class="bottom_bar_short" href="/about-eli">About Eli</a>'+utils.inline_separator+'<a class="bottom_bar_short" href="/policies">Policies</a>'+utils.inline_separator+'<a class="bottom_bar_short" href="/atom.xml"><img class="feed_icon_14x14" src="/media/feed-icon-14x14.png?rr" alt=""> RSS (Atom)</a>'+utils.inline_separator+'<a href="https://github.com/elidupree/eliduprees-website-source">Website source</a>'
def bottom_bar(info):
  return '<footer><div id="footer" class="bottom_bar'+(' '+info["extra_class"] if "extra_class" in info else '')+'"><div class="bottom_bar_inner">'+bottom_bar_contents(info)+'</div></div></footer>'

def bars_wrap(info, html):
  return '''<a class="skip" href="#footer">Skip to footer</a>
<div class="bars_outer_box">
  '''+top_bar.top_bar(info)+'''
  <div class="bars_inner_box">
    '''+html+'''
  </div>
  '''+bottom_bar(info)+'''
</div>'''

def add_home_page(page_dict):
  info = {"home":True}
  utils.make_page (page_dict,
    '/index',
      "Eli Dupree's website",
      '<link rel="" href="http://english-1467731550.spampoison.com/" />',
      '''
        <div><img role="presentation" alt="" class="background" src="/media/top-bar-background.png?rr" /></div>
        <div class="home_page_buffer">
          '''+top_bar.home_string(True)+'''
        </div>
        <div class="home_page_outer">
          <div class="home_page_categories">
            '''+top_bar.games_string(False)+'''<!-- Commenting out white space to prevent inline-block issues
            -->'''+top_bar.comics_string(False)+'''<!--
            -->'''+top_bar.stories_string(False)+'''<!--
            -->'''+top_bar.blog_string(False)+'''
          </div>
          <div class="home_page_bottom">
            <div class="home_page_bottom_inner">
              '''+bottom_bar_contents(info)+'''
            </div>
            <div class="home_page_recent_updates">
              <h2> Recent updates...</h2>
              '''+ blog.recent_updates (9) +'''
            </div>
          </div>
        </div>
      ''',
      {"canonical_path_override": "/", "blurb": "Games – Comics – Stories – Blog", "blurb_image": "/media/site-logo.png?rr"}
  )
