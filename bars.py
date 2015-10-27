#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import css
import top_bar
import html_pages
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
  background-image: url("/media/top-bar-background.png");
  background-size: 100% 100%; }
.voldemorts_children div.bottom_bar {
  background-image: url("/media/top-bar-background-vc.png"); }
div.bottom_bar_inner {
  padding: 0.25em;
}
.bottom_bar_short {
  white-space: nowrap; }

address.eli_exmxaxixl {
  display: inline;
  font-style: normal; }



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
  return 'Please share this!'+utils.inline_separator+'<address class="eli_exmxaxixl bottom_bar_short">Contact: '+exmxaxixl.a(exmxaxixl.axdxrxexsxs)+'</address>'+utils.inline_separator+'<a class="bottom_bar_short" href="/about-eli">About Eli</a>'+utils.inline_separator+'<a class="bottom_bar_short" href="/policies">Policies</a>'+utils.inline_separator+'<a class="bottom_bar_short" href="/atom.xml"><img src="/media/feed-icon-14x14.png"> RSS (Atom)</a>'+utils.inline_separator+'<a href="https://github.com/elidupree/eliduprees-website-source">Website source (code CC-0, content CC-BY-SA)</a>'
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
  utils.checked_insert(page_dict,
    '/index.html',
    html_pages.make_page(
      "Eli Dupree's website",
      '',
      '''
        <div><img role="presentation" alt="" class="background" src="/media/top-bar-background.png" /></div>
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
          </div>
        </div>
      '''
    )
  )
