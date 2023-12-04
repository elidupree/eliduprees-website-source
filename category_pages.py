#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import utils
import css
import javascript
import comics
import blog
import blog_posts
import studio_art

css.insert('''
div.category_page_bottom { clear:both; }
a.exhibit, div.exhibit {
  display: block;
  clear:both;
  background: white;
  background: rgba(255,255,255,0.9);
  margin: 3em 1em;  
  margin-top: 7em;
  text-align: center;
  text-decoration: none; }
.exhibit.no_image {margin-top:4em;}
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
  padding-bottom: 0.6em;
  padding-top: 0.2em;
  font-size: 250%;
  white-space: nowrap;
  text-decoration: underline; }
a.exhibit.fadeout>div.exhibit_start_reading {
  margin-top: -2em; }

.exhibit p {margin: 0 0; padding:0.3em 0;}

img.exhibit {
  display: block;
  position: relative;
  z-index: 1;
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
img.exhibit.nwia {
  width: 20em;
  height: 10em;
  margin-top: -3em;
  border-radius: 2em 4em; }
img.exhibit.generic.left {
  width: 300px;
  height: 300px;
  border-radius: 2em 8em; }
img.exhibit.generic.right {
  width: 300px;
  height: 300px;
  border-radius: 8em 2em; }
@media screen and (max-width: 45em) {
  a.exhibit, div.exhibit {
    margin-bottom: 2em;
    margin-left: 0;
    margin-right: 0; }
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
  a.exhibit, div.exhibit { margin-top: 2em; }
}
@media screen and (max-width: 25em) {
  img.exhibit.left { width: 95%; height: auto; }
  img.exhibit.right { width: 95%; height: auto; }
}

.orphaned_page_link {display: block}

.fake_warning_link {font-size: 71%; margin:0.4em 0; position: relative; z-index: 0;}
.fake_reveal_warning_button {color: blue; text-decoration: underline;}
html.javascript_enabled .fake_warning_link {display: inline-block;}
html.javascript_enabled .fake_reveal_warning_button {display: block;}
html.javascript_enabled .comic_warnings_list {display: none;}

.debug {display: none;}
html.debug_mode .debug {display: block; display: initial;}
html.debug_mode .not_debug {display: none;}
''')

javascript.do_after_body (r'''
$(".fake_warning_link").click (function () {
  $(this).css ("display", "block");
  $(this).children (".fake_reveal_warning_button").hide ();
  $(this).children (".comic_warnings_list").show ();
  return false;
});
''')

import html_pages
import bars

def exhibit (href, classes, thumbnail, blurb, enter_text):
  class_string ='''exhibit '''+ classes + (" no_image" if thumbnail is None else "")
  return (
    (('''<a href="'''+href +'''" class="'''+ class_string +'''">''') if  href else '<div class="'+ class_string + '">') +
      ('<img class="exhibit ' + classes + '" alt="" src="' + thumbnail + '" />' if thumbnail else '') +
      '<div class="exhibit_blurb">' + blurb + '</div>' +
      ('<div class=" exhibit_start_reading">' + enter_text + '</div>' if enter_text else '') + 
    ('</a>' if  href else '</div>') )

def content_warning_summary (contents):
  return '''
  <div class="hidden_cw_box fake_warning_link">
    <div class="fake_reveal_warning_button">Reveal content warnings</div>
    <div class="comic_warnings_list">
      '''+ contents +'''
      </div>
  </div>'''

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
        <p><cite>Voldemort's Children</cite>, my ongoing Harry Potter fanfic graphic novel, explores possible answers. It's about 80% complete, but is on hiatus while my hands recover from an injury.</p>'''+ content_warning_summary ("<p>Content warnings: This comic depicts verbal and physical abuse; physical violence, with occasional cartoon blood and gore; ableist language; negative self-talk; some discussion of suicide.</p><p>As you read the comic, each page will be marked with the warnings that apply to that page.</p>"), "Start reading") +
        exhibit ("/a-couple-of-badass-superheroes" , "acobs right", "/media/ACOBS_thumbnail.png?rr",'''
        <p><cite>A Couple of Badass Superheroes</cite> go on a silly adventure. I wrote the first part September-December 2011 to get used to drawing using my tablet. (14 pages)</p>''', "Start reading") +
        exhibit ("/people-are-wrong-sometimes", "paws left", "/media/PAWS_thumbnail.png?rr",'''
        <p>In <cite>People Are Wrong Sometimes</cite>, two friends are about to leave high school and part ways. But do they really know each other? (10 pages)</p>'''+ content_warning_summary ("<p>Content warnings: This comic depicts neurelitist statements; brief descriptions of bullying and violence; one instance of cartoon blood.</p>"), "Start reading") +
'''
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
    '''
    + exhibit ("/games/the-path", "generic left", "/media/the-path-screenshot.png?rr", '''The Path, a 10-minute online game about social expectations.''', "Play now")
    #+ exhibit ("http://lasercake.net/", "generic right", "/media/lasercake-snapshot-progressive.jpg?rr", '''Lasercake, an (early prototype of an) open-world game about the environment.''', "Go to website")
    + exhibit ("/games/green-caves", "generic left", "/media/green-caves-screenshot.png?rr", '''A simple online game where you fly around in some green caves.''', "Play now")
    + exhibit ("/hexy", "generic right", "/media/hexy-thumbnail.png?rr", '''Hexy Bondage, a sexual game for two players (or more) to play together on the same device.''', "[NSFW] Play now")
    + exhibit ("/games/pac-asteroids", "generic left", "/media/pac-asteroids-thumbnail.png?rr",'''Pac-asteroids, a half-baked unfinished online game I wrote while learning JavaScript.''', "Play now")
    +'''<div class="category_page_bottom"></div>
  </div>
</main>''')
  )
  
  
  import voice_practice_tool
  utils.make_page (page_dict,
    '/misc',
      "Miscellaneous things ⊂ Eli Dupree's website",
      '',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+ utils.background_image () +'''
      '''+bars.bars_wrap({"games":True}, '''<main>
  <div id="content">
    '''+ exhibit ("/voice-practice-tool", "generic left", voice_practice_tool.blurb_image, voice_practice_tool.blurb, "Use it now") +'''
    
    '''+ exhibit ("/ap-studio-art", "generic right", "/media/studio_art_12.png?rr",'''
        <p>'''+ studio_art.blurb +'''</p>''', "View the gallery") + '''

    <div class="category_page_bottom"></div>
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

javascript.do_before_body (r'''
if (read_cookie ("debug_mode")) {document.documentElement.className += " debug_mode";}
''')

def add_secrets (page_dict, orphaned_pages):
  utils.make_page (page_dict,
    '/secrets',
    "Secrets ⊂ Eli Dupree's website",
    "",
      '''<a class="skip" href="#content">Skip to content</a>
      '''+ utils.background_image () +'''
      '''+bars.bars_wrap({"games":True}, '''<main>
  <div id="content">
    '''
    + exhibit (None, "", None, '''<h1> Secrets </h1> <p>Congratulations! You've arrived at the secret page. You probably got here by supporting <a href="https://www.patreon.com/EliDupree">my Patreon page</a>. (Thank you so much!) Or maybe you found it by snooping through <a href="https://github.com/elidupree">my code on GitHub</a>. (You're very clever!) Either way, welcome! Enjoy the secrets below.</p> ''', None)
    + exhibit (None, "", None, '''<p>When I work on designing this website, I use a debug mode that displays some extra information. Right now, the only hidden information is an estimate of the reading difficulty (in US grade level) of each post.</p> <p><a class="debug" id="disable_debug_mode" href=" javascript:;">Disable debug mode</a><a class="not_debug" id="enable_debug_mode" href=" javascript:;">Enable debug mode</a></p> ''', None)
    + exhibit (None, "", None, '''<p>Not all of my posts are accessible from the main page. Sometimes, I create a temporary page for testing purposes, or a game that is still a work-in-progress. Sometimes, I write things to share with specific fandoms, which wouldn't necessarily be interesting to a general audience (or I might want to avoid recommending a show even by mentioning it). You, dear reader, have special access.</p> <p>All currently inaccessible pages are listed below. If you start from this page and follow links, you can reach everything on elidupree.com.</p> <p></p> <p>'''+ "".join (['''<a class="orphaned_page_link" href="'''+ path +'''">'''+ title +'''</a>''' for (path, title) in orphaned_pages]) + "</p> ", None)
        
    +'''<div class="category_page_bottom"></div>
  </div>
</main>'''), {"after_body":'''<script type="text/javascript">
add_event_listener (document.getElementById ("enable_debug_mode"), "click", function () {set_cookie ("debug_mode", true, 30);document.documentElement.className += " debug_mode";});
add_event_listener (document.getElementById ("disable_debug_mode"), "click", function () {delete_cookie ("debug_mode"); remove_class (document.documentElement, "debug_mode");});
</script>'''}
  )

    
