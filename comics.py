#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import utils
import css
import voldemorts_children

css.insert('''
div.recent_pages {
  max-width: 35em;
  margin: 0 auto;
  text-align: center;
  padding: 0.75em;
  background-color: white; }
div.comic_splash {
  background: white;
  padding: 0.5em;
  margin: 1em; }
div.comic_splash_end {
  clear:both; }
a.recent_update {
  display: block;
  padding: 0.3em;
  vertical-align: middle; }
a.recent_update>img {
  width: 9em;
  height: 2.34em; }
''')

import html_pages
import bars

def add_comics_page(page_dict):
  utils.checked_insert(page_dict,
    'comics.html',
    html_pages.make_page(
      "Comics ⊂ Eli Dupree's website",
      '',
      '<body><a class="skip" href="#content">Skip to content</a>'+bars.bars_wrap({"comics":True}, '''<main>
  <div id="content">
    <div class="recent_pages">
      <h1>Recent updates</h1>
      '''+voldemorts_children.recent_page_link(0)+'''
      '''+voldemorts_children.recent_page_link(1)+'''
      '''+voldemorts_children.recent_page_link(2)+'''
      '''+voldemorts_children.recent_page_link(3)+'''
      '''+voldemorts_children.recent_page_link(4)+'''
    </div>
    <div class="comic_splash vc">
      <img width style="display:block; float:left; width: 210px; height: 280px;" alt="A comic page; see below for a transcript" src="http://deqyc5bzdh53a.cloudfront.net/VC_1.png" />voldemortVoldemort's Children, my ongoing Harry Potter fanfic graphic novel, which updates daily is on hiatus until at least May 2013.
      <div class="comic_splash_end"></div>
    </div>
  </div>
</main>''')+'</body>'
    )
  )
