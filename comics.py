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
a.comic_splash {
  display: block;
  clear:both;
  background: white;
  background: rgba(255,255,255,0.9);
  padding: 0.5em;
  margin: 3em 1em;
  text-align: center;
  text-decoration: none; }
div.comic_splash_blurb {
  color: black; }
div.comic_splash_start_reading {
  display: block;
  padding: 0.6em;
  font-size: 250%;
  white-space: nowrap;
  text-decoration: underline; }
div.recent_updates_header {
  height: 0;
  overflow: visible; }
h1.recent_updates_header {
  padding: 0;
  padding-top: 1em;
  padding-right: 3.5em;
  z-index: 999;
  position: relative;
  font-family: Arial, Helvetica, sans-serif;
  font-weight: bold;
  pointer-events: none;
  color: rgba(255,255,255,.9); }
a.recent_update:hover div.recent_update {
  background-color: #ffff66; }
a.recent_update {
  display: block; }
div.recent_update_outer {
  max-width: 30em;
  padding: 0 '''+str(blog.post_separation)+'''em;
  margin: 2px auto; }
div.recent_update {
  background-color:'''+blog.metacontent_color_IE8+''';
  background-color:'''+blog.metacontent_color+''';
  border-radius: 0.6em;
  font-weight: bold;
  float: right;
  clear: both;
  padding: 0 0.5em;
  font-family: Arial, Helvetica, sans-serif; }
div.recent_update_end {
  clear:both; }
div.recent_update>img {
  width: 9em;
  height: 2.34em; }
@media screen and (max-width: 40em) {
  h1.recent_updates_header { font-size: 200%; }
}
@media screen and (max-width: 30em) {
  div.recent_update>img { display: none; }
  h1.recent_updates_header { padding-top: 0.5em; }
}

a.comic_splash>img {
  display: block;
  position: relative;
  padding: 1em;
  background-color: rgba(255,255,255,0.3);
  margin-bottom: 2em; }
a.comic_splash.vc>img {
  float: left;
  width: 300px;
  height: 400px;
  margin-top: -6em;
  border-radius: 2em 8em;
  margin-left: 2em; }
a.comic_splash.paws {
  margin-top: 7em; }
a.comic_splash.paws>img {
  float: right;
  margin-top: -6em;
  border-radius: 1.5em 1.5em;
  margin-right: 2em; }
a.comic_splash.acobs {
  margin-top: 7em; }
a.comic_splash.acobs>img {
  float: left;
  margin-top: -6em;
  border-radius: 1.5em 1.5em;
  margin-left: 1em; }
@media screen and (max-width: 45em) {
  a.comic_splash {
    margin: 2em 0; }
  a.comic_splash>img {
    padding: 0.8em;
    margin-bottom: 1em; }
  a.comic_splash.vc>img    { margin-left:0; margin-right:0; }
  a.comic_splash.paws>img  { margin-left:0; margin-right:0; }
  a.comic_splash.acobs>img { margin-left:0; margin-right:0; }
  div.comic_splash_start_reading {
    font-size: 200%; }
}
@media screen and (max-width: 33em) {
  a.comic_splash>img { padding: 0.5em; margin: -0.5em; }
  a.comic_splash.vc>img { display: inline; float: none; margin: 0; }
  a.comic_splash.paws>img { display: inline; float: none; margin: 0; }
  a.comic_splash.acobs>img { display: inline; float: none; margin: 0; }
  a.comic_splash.paws { margin-top: 2em; }
  a.comic_splash.acobs { margin-top: 2em; }
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
    <a href="/voldemorts-children" class="comic_splash vc">
      <img alt="" src="/media/VC_0.png" />
      <div class="comic_splash_blurb">
      voldemortVoldemort's Children, my ongoing Harry Potter fanfic graphic novel, which updates daily is on hiatus until at least May 2013.
      </div>
      <div class="comic_splash_start_reading">Start reading</div>
    </a>
    <a href="/people-are-wrong-sometimes" class="comic_splash paws">
      <img alt="" src="http://deqyc5bzdh53a.cloudfront.net/PAWS_thumbnail.png" />
      <div class="comic_splash_blurb">
      voldemortVoldemort's Children, my ongoing Harry Potter fanfic graphic novel, which updates daily is on hiatus until at least May 2013.
      </div>
      <div class="comic_splash_start_reading">Start reading</div>
    </a>
    <a href="/a-couple-of-badass-superheroes" class="comic_splash acobs">
      <img alt="" src="http://deqyc5bzdh53a.cloudfront.net/ACOBS_thumbnail.png" />
      <div class="comic_splash_blurb">
      voldemortVoldemort's Children, my ongoing Harry Potter fanfic graphic novel, which updates daily is on hiatus until at least May 2013.
      </div>
      <div class="comic_splash_start_reading">Start reading</div>
    </a>
  </div>
</main>''')+'</body>'
    )
  )
