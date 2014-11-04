#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import utils
import css
import voldemorts_children
import blog

css.insert('''
div.recent_pages {
  margin-top:'''+str(blog.post_separation)+'''em;
  text-align: center; }
div.comic_splash {
  background: white;
  padding: 0.5em;
  margin: 1em; }
div.comic_splash_end {
  clear:both; }
div.recent_updates_header {
  height: 0;
  overflow: visible; }
h1.recent_updates_header {
  padding: 0;
  padding-top: 1em;
  padding-right: 3em;
  z-index: 999;
  position: relative;
  font-family: Arial, Helvetica, sans-serif;
  font-weight: bold;
  pointer-events: none;
  color: rgba(255,255,255,.9); }
a.recent_update:hover>div.recent_update {
  background-color: #ffff66; }
a.recent_update {
  display: block; }
div.recent_update {
  background-color:'''+blog.metacontent_color_IE8+''';
  background-color:'''+blog.metacontent_color+''';
  max-width: 25em;
  margin: 2px auto;
  border-radius: 0.6em;
  font-weight: bold;
  font-family: Arial, Helvetica, sans-serif; }
div.recent_update>img {
  width: 9em;
  height: 2.34em; }
@media screen and (max-width: 40em) {
  h1.recent_updates_header { font-size: 200%; }
}
@media screen and (max-width: 25em) {
  div.recent_update>img { display: none; }
  h1.recent_updates_header { padding-top: 0.5em; }
}
''')

import html_pages
import bars

def recent_page_link(num):
  return voldemorts_children.recent_page_link(num)

def add_comics_page(page_dict):
  utils.checked_insert(page_dict,
    'comics.html',
    html_pages.make_page(
      "Comics ⊂ Eli Dupree's website",
      '',
      '''<body><a class="skip" href="#content">Skip to content</a>
      <div><img role="presentation" alt="" class="background" src="/media/blog-background.jpg" /></div>
      '''+bars.bars_wrap({"comics":True}, '''<main>
  <div id="content">
    <div class="recent_pages">
      <div class="recent_updates_header">
        <h1 class="recent_updates_header">Recent updates...</h1>
      </div>
      '''+recent_page_link(0)+'''
      '''+recent_page_link(1)+'''
      '''+recent_page_link(2)+'''
      '''+recent_page_link(3)+'''
      '''+recent_page_link(4)+'''
    </div>
    <div class="comic_splash vc">
      <img width style="display:block; float:left; width: 210px; height: 280px;" alt="A comic page; see below for a transcript" src="http://deqyc5bzdh53a.cloudfront.net/VC_1.png" />voldemortVoldemort's Children, my ongoing Harry Potter fanfic graphic novel, which updates daily is on hiatus until at least May 2013.
      <div class="comic_splash_end"></div>
    </div>
  </div>
</main>''')+'</body>'
    )
  )
