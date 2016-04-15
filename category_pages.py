#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import utils
import css
import comics
import blog

css.insert('''
div.category_page_bottom { clear:both; }
div.recent_pages {
  margin-top:'''+str(blog.post_vertical_separation)+'''em;
  text-align: center; }
a.exhibit {
  display: block;
  clear:both;
  background: white;
  background: rgba(255,255,255,0.9);
  margin: 3em 1em;
  text-align: center;
  text-decoration: none; }
a.exhibit.fadeout {
  position: relative;
  overflow: hidden; }
a.exhibit.fadeout:link { color:#4488ff; }
a.exhibit.fadeout:visited { color:#aa33ff; }
img.exhibit_fadeout {
  height: 100%;
  width: 100%;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0; }
div.exhibit_blurb {
  position: relative;
  padding: 0.5em;
  color: black;
  font-size: 140%; }
div.exhibit_blurb>h1 {
  font-size: 180%;
  font-weight: bold; }
div.exhibit_start_reading {
  position: relative;
  display: block;
  padding: 0.6em;
  font-size: 250%;
  white-space: nowrap;
  text-decoration: underline; }
a.exhibit.fadeout>div.exhibit_start_reading {
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

img.exhibit {
  display: block;
  position: relative;
  padding: 1em;
  background-color: rgba(255,255,255,0.3);
  margin-top: -6em;
  margin-bottom: 2em; }
img.exhibit.left {
  margin-left: 2em;
  float: left; }
img.exhibit.right {
  margin-right: 2em;
  float: right; }
img.exhibit.vc {
  width: 300px;
  height: 400px;
  border-radius: 2em 8em; }
a.exhibit {
  margin-top: 7em; }
img.exhibit.paws {
  border-radius: 1.5em 1.5em; }
img.exhibit.acobs {
  border-radius: 1.5em 1.5em;
  margin-left: 1em; }
img.exhibit.lasercake {
  width: 300px;
  height: 300px;
  border-radius: 2em 8em; }
img.exhibit.nwia {
  width: 20em;
  height: 10em;
  margin-top: -3em;
  border-radius: 2em 4em; }
img.exhibit.hexy {
  width: 300px;
  height: 300px;
  border-radius: 8em 2em; }
img.exhibit.greencaves {
  width: 300px;
  height: 300px;
  border-radius: 2em 8em; }
@media screen and (max-width: 45em) {
  a.exhibit {
    margin: 2em 0; }
  img.exhibit {
    padding: 0.8em;
    margin-bottom: 1em; }
  img.exhibit.left { margin-left: 0; }
  img.exhibit.right { margin-right: 0; }
  div.exhibit_start_reading {
    font-size: 200%; }
}
@media screen and (max-width: 33em) {
  img.exhibit { padding: 0.5em; margin: -0.5em; }
  img.exhibit.left { display: inline; float: none; margin: 0; }
  img.exhibit.right { display: inline; float: none; margin: 0; }
  a.exhibit { margin-top: 2em; }
}
@media screen and (max-width: 25em) {
  img.exhibit.left { width: 95%; height: auto; }
  img.exhibit.right { width: 95%; height: auto; }
}

span.title { font-style: italic; }
''')

import html_pages
import bars

def recent_page_link(num):
  return comics.recent_page_link(num)

def add_category_pages(page_dict):
  def exhibit (href, classes, thumbnail, blurb, enter_text):
    return ('''<a href="'''+href +'''" class="exhibit '''+ classes +'''">'''+
      ('<img class="exhibit ' + classes + '" alt="" src="' + thumbnail + '" />' if thumbnail else '') +
      '<div class="exhibit_blurb">' + blurb + '</div><div class=" exhibit_start_reading">' + enter_text + '</div></a>')
  
  utils.checked_insert(page_dict,
    '/comics.html',
    html_pages.make_page(
      "Comics ⊂ Eli Dupree's website",
      '',
      '''<a class="skip" href="#content">Skip to content</a>
      <div><img role="presentation" alt="" class="background" src="/media/colorful-background.jpg?rr" /></div>
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
    '''+ exhibit ("/voldemorts-children", "vc left", "/media/VC_0.png?rr",'''
        <p>What if Dumbledore's idea of placing Harry Potter with an abusive family didn't turn out so well?</p>
        <span class="title">Voldemort's Children</span>, my ongoing Harry Potter fanfic graphic novel, explores possible answers. It's about 80% complete, but is on hiatus while my hands recover from an injury.''', "Start reading") +
        exhibit ("/people-are-wrong-sometimes", "paws right", "/media/PAWS_thumbnail.png?rr",'''
        In <span class="title">People Are Wrong Sometimes</span>, two friends are about to leave high school and part ways. But do they really know each other? (10 pages)''', "Start reading") +
        exhibit ("/a-couple-of-badass-superheroes" , "acobs left", "/media/ACOBS_thumbnail.png?rr",'''
        <span class="title">A Couple of Badass Superheroes</span> go on a silly adventure. I wrote the first part September-December 2011 to get used to drawing using my tablet. (10 pages)''', "Start reading") +'''
    <div class="category_page_bottom"></div>
  </div>
</main>''')
    )
  )
  
  print("TODO: reduce duplicate code between these three (and blog)'")
  utils.checked_insert(page_dict,
    '/games.html',
    html_pages.make_page(
      "Games ⊂ Eli Dupree's website",
      '',
      '''<a class="skip" href="#content">Skip to content</a>
      <div><img role="presentation" alt="" class="background" src="/media/blog-background.jpg?rr" /></div>
      '''+bars.bars_wrap({"games":True}, '''<main>
  <div id="content">
    <a href="http://lasercake.net/" class="exhibit lasercake successor">
      <img class="exhibit lasercake left" alt="" src="/media/lasercake-snapshot-progressive.jpg?rr" />
      <div class="exhibit_blurb">
        Lasercake, an (early prototype of an) open-world game about the environment.
      </div>
      <div class="exhibit_start_reading">Go to website</div>
    </a>
    <a href="/hexy" class="exhibit hexy successor">
      <img class="exhibit hexy right" alt="" src="/media/hexy_bondage_page_background.jpg?rr" />
      <div class="exhibit_blurb">
        Hexy Bondage, a sexual board game for two or more players.
      </div>
      <div class="exhibit_start_reading">Go to website</div>
    </a>
    <a href="/games/green-caves" class="exhibit greencaves successor">
      <img class="exhibit greencaves left" alt="" src="/media/green-caves-screenshot.png?rr" />
      <div class="exhibit_blurb">
        A simple online game where you fly around in some green caves.
      </div>
      <div class="exhibit_start_reading">Play now</div>
    </a>
    <div class="category_page_bottom"></div>
  </div>
</main>''')
    )
  )
  
  print("TODO: reduce duplicate code between these three (and blog)'")
  utils.checked_insert(page_dict,
    '/stories.html',
    html_pages.make_page(
      "Stories ⊂ Eli Dupree's website",
      '',
      '''<a class="skip" href="#content">Skip to content</a>
      <div><img role="presentation" alt="" class="background" src="/media/blog-background.jpg?rr" /></div>
      '''+bars.bars_wrap({"stories":True}, '''<main>
  <div id="content">
    <a href="/stories/not-what-i-am" class="exhibit nwia successor">
      <img class="exhibit nwia left" alt="" src="/media/NWIA_thumbnail.png?rr" />
      <div class="exhibit_blurb">
        <h1>Not What I Am</h1>
        An out-of-place middle schooler tries to find zir way in the world.
      </div>
      <div class="exhibit_start_reading">Start reading</div>
    </a>
    <a href="/stories/capitalism-sat" class="exhibit fadeout successor">
      <img class="exhibit_fadeout" alt="" src="/media/fade-to-black.png?rr" />
      <div class="exhibit_blurb">
        <h1>Capitalism Sat</h1>
        <p>...in Plato's cave, watching the shadows. Outside, ze knew, there were people buying and selling. Capitalism saw them trading goods for goods, services for services. And oh, most beautiful of all, the exchange of goods for services, whereon the economy turns. What supplies! What demand! Capitalism blushed to think of it all.</p>

<p>And then zir chains were loosed. Ze turned, a breath half indrawn, barely daring to hope. Ze rushed out into the open air, eager to offer zir labor on the open market for a fair value...</p>
      </div>
      <div class="exhibit_start_reading">Keep reading</div>
    </a>
    <a class="exhibit successor">
      <img class="exhibit left" alt="" src="/media/NWIA_thumbnail.png?rr" />
      <div class="exhibit_blurb">
        More stories coming at some point in the future
      </div>
    </a>
    <div class="category_page_bottom"></div>
  </div>
</main>''')
    )
  )
