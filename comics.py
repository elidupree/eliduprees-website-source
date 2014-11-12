#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import utils
import css
import voldemorts_children
import blog

css.insert('''
div.comics_bottom { clear:both; }
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

img.comic_splash {
  display: block;
  position: relative;
  padding: 1em;
  background-color: rgba(255,255,255,0.3);
  margin-top: -6em;
  margin-bottom: 2em; }
img.comic_splash.left {
  margin-left: 2em;
  float: left; }
img.comic_splash.right {
  margin-right: 2em;
  float: right; }
img.comic_splash.vc {
  width: 300px;
  height: 400px;
  border-radius: 2em 8em; }
a.comic_splash.successor {
  margin-top: 7em; }
img.comic_splash.paws {
  border-radius: 1.5em 1.5em; }
img.comic_splash.acobs {
  border-radius: 1.5em 1.5em;
  margin-left: 1em; }
img.comic_splash.lasercake {
  width: 300px;
  height: 300px;
  border-radius: 2em 8em; }
img.comic_splash.hexy {
  width: 300px;
  height: 300px;
  border-radius: 8em 2em; }
img.comic_splash.greencaves {
  width: 300px;
  height: 300px;
  border-radius: 2em 8em; }
@media screen and (max-width: 45em) {
  a.comic_splash {
    margin: 2em 0; }
  img.comic_splash {
    padding: 0.8em;
    margin-bottom: 1em; }
  img.comic_splash.left { margin-left: 0; }
  img.comic_splash.right { margin-right: 0; }
  div.comic_splash_start_reading {
    font-size: 200%; }
}
@media screen and (max-width: 33em) {
  img.comic_splash { padding: 0.5em; margin: -0.5em; }
  img.comic_splash.left { display: inline; float: none; margin: 0; }
  img.comic_splash.right { display: inline; float: none; margin: 0; }
  a.comic_splash.successor { margin-top: 2em; }
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
      <img class="comic_splash vc left" alt="" src="/media/VC_0.png" />
      <div class="comic_splash_blurb">
      voldemortVoldemort's Children, my ongoing Harry Potter fanfic graphic novel, which updates daily is on hiatus until at least May 2013.
      </div>
      <div class="comic_splash_start_reading">Start reading</div>
    </a>
    <a href="/people-are-wrong-sometimes" class="comic_splash paws successor">
      <img class="comic_splash paws right" alt="" src="http://deqyc5bzdh53a.cloudfront.net/PAWS_thumbnail.png" />
      <div class="comic_splash_blurb">
      voldemortVoldemort's Children, my ongoing Harry Potter fanfic graphic novel, which updates daily is on hiatus until at least May 2013.
      </div>
      <div class="comic_splash_start_reading">Start reading</div>
    </a>
    <a href="/a-couple-of-badass-superheroes" class="comic_splash acobs successor">
      <img class="comic_splash acobs left" alt="" src="http://deqyc5bzdh53a.cloudfront.net/ACOBS_thumbnail.png" />
      <div class="comic_splash_blurb">
      voldemortVoldemort's Children, my ongoing Harry Potter fanfic graphic novel, which updates daily is on hiatus until at least May 2013.
      </div>
      <div class="comic_splash_start_reading">Start reading</div>
    </a>
  </div>
</main>''')+'</body>'
    )
  )
  
  print("TODO: this doesn't go in a function called 'add_comics_page'")
  utils.checked_insert(page_dict,
    'games.html',
    html_pages.make_page(
      "Games ⊂ Eli Dupree's website",
      '',
      '''<body><a class="skip" href="#content">Skip to content</a>
      <div><img role="presentation" alt="" class="background" src="/media/blog-background.jpg" /></div>
      '''+bars.bars_wrap({"comics":True}, '''<main>
  <div id="content">
    <a href="http://lasercake.net/" class="comic_splash lasercake successor">
      <img class="comic_splash lasercake left" alt="" src="http://www.lasercake.net/_cacheable/lasercake-snapshot-progressive.jpg" />
      <div class="comic_splash_blurb">
        Lasercake, an open-world game about the environment.
      </div>
      <div class="comic_splash_start_reading">Go to website</div>
    </a>
    <a href="/hexy" class="comic_splash hexy successor">
      <img class="comic_splash hexy right" alt="" src="http://deqyc5bzdh53a.cloudfront.net/hexy_bondage_page_background.jpg" />
      <div class="comic_splash_blurb">
        Hexy Bondage, a sexual board game for two or more players.
      </div>
      <div class="comic_splash_start_reading">Go to website</div>
    </a>
    <a href="/green-caves-game" class="comic_splash greencaves successor">
      <img class="comic_splash greencaves left" alt="" src="/media/green-caves-screenshot.png" />
      <div class="comic_splash_blurb">
        A simple online game where you fly around in some green caves.
      </div>
      <div class="comic_splash_start_reading">Play now</div>
    </a>
    <div class="comics_bottom"></div>
  </div>
</main>''')+'</body>'
    )
  )
