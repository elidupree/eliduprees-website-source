#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import utils
import css
import comics
import blog
import blog_posts

css.insert('''
div.category_page_bottom { clear:both; }
.exhibit {
  display: block;
  clear:both;
  background: white;
  background: rgba(255,255,255,0.9);
  margin: 3em 1em;  
  margin-top: 7em;
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
    margin: 2em 0;
    margin-top: 7em; }
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

def exhibit (href, classes, thumbnail, blurb, enter_text):
    return (
    (('''<a href="'''+href +'''" class="exhibit '''+ classes +'''">''') if  href else '<div class="exhibit">') +
      ('<img class="exhibit ' + classes + '" alt="" src="' + thumbnail + '" />' if thumbnail else '') +
      '<div class="exhibit_blurb">' + blurb + '</div>' +
      ('<div class=" exhibit_start_reading">' + enter_text + '</div>' if enter_text else '') + 
    ('</a>' if  href else '</div>') )

def add_category_pages(page_dict):  
  utils.make_page (page_dict,
    '/comics',
      "Comics ⊂ Eli Dupree's website",
      '',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+ utils.background_image () +'''
      '''+bars.bars_wrap({"comics":True}, '''<main>
  <div id="content">
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
  

  utils.make_page (page_dict,
    '/games',
      "Games ⊂ Eli Dupree's website",
      '',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+ utils.background_image () +'''
      '''+bars.bars_wrap({"games":True}, '''<main>
  <div id="content">
    '''+ exhibit ("http://lasercake.net/", "lasercake left", "/media/lasercake-snapshot-progressive.jpg?rr", '''Lasercake, an (early prototype of an) open-world game about the environment.''', "Go to website")
    + exhibit ("/hexy", "hexy right", "/media/hexy_bondage_page_background.jpg?rr", '''Hexy Bondage, a sexual board game for two or more players.''', "Go to website")
    + exhibit ("/games/green-caves", "greencaves left", "/media/green-caves-screenshot.png?rr", '''A simple online game where you fly around in some green caves.''', "Play now")
    +'''<div class="category_page_bottom"></div>
  </div>
</main>''')
  )
  

  utils.make_page (page_dict,
    '/stories',
      "Stories ⊂ Eli Dupree's website",
      '',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+ utils.background_image () +'''
      '''+bars.bars_wrap({"stories":True}, '''<main>
  <div id="content">'''+ blog_posts.stories_index (True) +'''
    <div class="category_page_bottom"></div>
  </div>
</main>''')
  )
