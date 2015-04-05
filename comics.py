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
  margin-top:'''+str(blog.post_vertical_separation)+'''em;
  text-align: center; }
a.comic_splash {
  display: block;
  clear:both;
  background: white;
  background: rgba(255,255,255,0.9);
  margin: 3em 1em;
  text-align: center;
  text-decoration: none; }
a.comic_splash.fadeout {
  position: relative;
  overflow: hidden; }
a.comic_splash.fadeout:link { color:#4488ff; }
a.comic_splash.fadeout:visited { color:#aa33ff; }
img.comic_splash_fadeout {
  height: 100%;
  width: 100%;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0; }
div.comic_splash_blurb {
  position: relative;
  padding: 0.5em;
  color: black; }
div.comic_splash_blurb>h1 {
  font-size: 180%;
  font-weight: bold; }
div.comic_splash_start_reading {
  position: relative;
  display: block;
  padding: 0.6em;
  font-size: 250%;
  white-space: nowrap;
  text-decoration: underline; }
a.comic_splash.fadeout>div.comic_splash_start_reading {
  margin-top: -2em; }
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
  padding: 0 '''+str(blog.post_vertical_separation)+'''em;
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
img.comic_splash.nwia {
  width: 20em;
  height: 10em;
  margin-top: -3em;
  border-radius: 2em 4em; }
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
@media screen and (max-width: 25em) {
  img.comic_splash.left { width: 95%; height: auto; }
  img.comic_splash.right { width: 95%; height: auto; }
}

span.title { font-style: italic; }
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
      '''<a class="skip" href="#content">Skip to content</a>
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
        <p>What if Dumbledore's idea of placing Harry Potter with an abusive family didn't turn out so well?</p>
        <span class="title">Voldemort's Children</span>, my ongoing Harry Potter fanfic graphic novel, explores possible answers. It's about 80% complete, but is on hiatus while my hands recover from an injury.
      </div>
      <div class="comic_splash_start_reading">Start reading</div>
    </a>
    <a href="/people-are-wrong-sometimes" class="comic_splash paws successor">
      <img class="comic_splash paws right" alt="" src="http://deqyc5bzdh53a.cloudfront.net/PAWS_thumbnail.png" />
      <div class="comic_splash_blurb">
        In <span class="title">People Are Wrong Sometimes</span>, two friends are about to leave high school and part ways. But do they really know each other? (10 pages)
      </div>
      <div class="comic_splash_start_reading">Start reading</div>
    </a>
    <a href="/a-couple-of-badass-superheroes" class="comic_splash acobs successor">
      <img class="comic_splash acobs left" alt="" src="http://deqyc5bzdh53a.cloudfront.net/ACOBS_thumbnail.png" />
      <div class="comic_splash_blurb">
        <span class="title">A Couple of Badass Superheroes</span> go on a silly adventure. I wrote the first part September-December 2011 to get used to drawing using my tablet. (10 pages)
      </div>
      <div class="comic_splash_start_reading">Start reading</div>
    </a>
  </div>
</main>''')
    )
  )
  
  print("TODO: this doesn't go in a function called 'add_comics_page'")
  print("TODO: reduce duplicate code between these three (and blog)'")
  utils.checked_insert(page_dict,
    'games.html',
    html_pages.make_page(
      "Games ⊂ Eli Dupree's website",
      '',
      '''<a class="skip" href="#content">Skip to content</a>
      <div><img role="presentation" alt="" class="background" src="/media/blog-background.jpg" /></div>
      '''+bars.bars_wrap({"games":True}, '''<main>
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
    <a href="/games/green-caves-game" class="comic_splash greencaves successor">
      <img class="comic_splash greencaves left" alt="" src="/media/green-caves-screenshot.png" />
      <div class="comic_splash_blurb">
        A simple online game where you fly around in some green caves.
      </div>
      <div class="comic_splash_start_reading">Play now</div>
    </a>
    <div class="comics_bottom"></div>
  </div>
</main>''')
    )
  )
  
  print("TODO: this doesn't go in a function called 'add_comics_page'")
  print("TODO: reduce duplicate code between these three (and blog)'")
  utils.checked_insert(page_dict,
    'stories.html',
    html_pages.make_page(
      "Stories ⊂ Eli Dupree's website",
      '',
      '''<a class="skip" href="#content">Skip to content</a>
      <div><img role="presentation" alt="" class="background" src="/media/blog-background.jpg" /></div>
      '''+bars.bars_wrap({"stories":True}, '''<main>
  <div id="content">
    <a href="/stories/not-what-i-am" class="comic_splash nwia successor">
      <img class="comic_splash nwia left" alt="" src="http://deqyc5bzdh53a.cloudfront.net/NWIA_thumbnail.png" />
      <div class="comic_splash_blurb">
        <h1>Not What I Am</h1>
        An out-of-place middle schooler tries to find zir way in the world.
      </div>
      <div class="comic_splash_start_reading">Start reading</div>
    </a>
    <a href="/stories/capitalism-sat" class="comic_splash fadeout successor">
      <img class="comic_splash_fadeout" alt="" src="/media/fade-to-black.png" />
      <div class="comic_splash_blurb">
        <h1>Capitalism Sat</h1>
        <p>...in Plato's cave, watching the shadows. Outside, ze knew, there were people buying and selling. Capitalism saw them trading goods for goods, services for services. And oh, most beautiful of all, the exchange of goods for services, whereon the economy turns. What supplies! What demand! Capitalism blushed to think of it all.</p>

<p>And then zir chains were loosed. Ze turned, a breath half indrawn, barely daring to hope. Ze rushed out into the open air, eager to offer zir labor on the open market for a fair value...</p>
      </div>
      <div class="comic_splash_start_reading">Keep reading</div>
    </a>
    <a class="comic_splash successor">
      <img class="comic_splash left" alt="" src="http://deqyc5bzdh53a.cloudfront.net/NWIA_thumbnail.png" />
      <div class="comic_splash_blurb">
        More stories coming at some point in the future
      </div>
    </a>
    <div class="comics_bottom"></div>
  </div>
</main>''')
    )
  )
