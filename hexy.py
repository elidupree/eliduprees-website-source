#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import html_pages
import bars
import exmxaxixl
import blog
import re
import xml.etree.ElementTree as XML

source_svg = ""
tile_ids = []
used_ids = {}
with open ("./hexy_source/game.svg", encoding = "utf-8") as source_svg_file:
  source_svg = source_svg_file.read()
with open ("./hexy_source/tile_ids_hack.svg", encoding = "utf-8") as something:
  for match in re.finditer(r'''id="(g\d*?)"''', something.read()):
    id = match.group (1)
    if id != "layer1":
      tile_ids.append (match.group (1))

elements_by_id = {}

svg_id = "id"
XML.register_namespace("","http://www.w3.org/2000/svg")
XML.register_namespace("sodipodi","http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd")
XML.register_namespace("xlink","http://www.w3.org/1999/xlink")
XML.register_namespace("inkscape","http://www.inkscape.org/namespaces/inkscape")
XML.register_namespace("cc","http://creativecommons.org/ns#")
modified = XML.fromstring (source_svg)

for element in modified.findall (".//*[@"+svg_id+"]"):
  elements_by_id [element.get (svg_id)] = element

def find(element):
  id = element.get (svg_id)
  if id not in used_ids:
    used_ids [id] = True
    link = element.get ("{http://www.w3.org/1999/xlink}href")
    if link:
      find (elements_by_id[link[1:]])
    style = element.get ("style")
    if style:
      for referenced in re.finditer(r'url\(#(.*?)\)', style):
        find (elements_by_id [referenced.group (1)])
      element.set ("style", re.sub(r'fill:#808080', "fill:var(--path-fill)", style))
    style = element.get ("clip-path")
    if style:
      for referenced in re.finditer(r'url\(#(.*?)\)', style):
        find (elements_by_id [referenced.group (1)])
    for descendent in element.iter():
      find (descendent)

for id in tile_ids:
  find (elements_by_id [id])

modified.remove (elements_by_id ["layer1"])
elements_by_id ["defs4"].append(elements_by_id ["layer1"])

def prune (element):
  if (False
  #or element.tag == "{http://www.w3.org/2000/svg}metadata"
  #or element.tag == "{http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd}namedview"
  ):
    return True
  
  self_used = (element.get (svg_id) in used_ids)
  for child in element.findall("*"):
    child_used = (child.get (svg_id) in used_ids) or prune (child)
    if child_used:
      self_used = True
    else:
      element.remove (child)
  return self_used

prune (modified)

trimmed_svg = XML.tostring (modified, encoding = "unicode", method = "html")



blurb = "A sexual board game for two or more players"
	  
def add_game(page_dict):
  utils.make_page (page_dict,
    '/hexy',
      "Hexy Bondage ⊂ Eli Dupree's website",
      r'''
<style>
html.hexy .bars_outer_box {
  background-color: #878787;
  background-image: url("/media/hexy-background.jpg?rr"); }

div.hexy_content h1{ font-size: 200%; font-weight: bold; padding-top: 0.20em; }
div.hexy_content h2{ font-size: 150%; font-weight: bold; padding-top: 0.30em; }
div.hexy_content p { margin: 0; padding: 0.5em 0; line-height: inherit; }
div.hexy_content a:link { color:blue }
div.hexy_content a:visited { color:purple }

div.hexy_content div.subtitle { font-weight: bold; font-size: 90%; padding-bottom: 0.5em;}
div.hexy_content {
  text-align: center;
  font-family: Arial, Helvetica, sans-serif;
  max-width: 50em;
  margin: 0 auto; }
div.hexy_content form,div.hexy_content table {
  display: inline; }
div.hexy_content .paynowbutton {
  vertical-align: middle; }
div.hexy_content div.bigbox_outer {
  padding: 0.2em 0.4em; }
div.hexy_content div.bigbox {
  border-radius: 1.4em;
  padding: 0.3em;
  background-color: #ffffff;
  background-color: rgba(255,255,255,0.95); }
div.hexy_content div.bigbox.thankyou {
  padding: 1.0em 0.3em;
  background-color: #ffff00;
  background-color: rgba(255,255,0,0.90); }
div.hexy_content div.bigbox_outer.narrower { display:inline-block; }
div.hexy_content div.bigbox_outer.last { padding-bottom: 0.4em; }
div.hexy_content div.bigbox_outer:first-child { padding-top: 0.4em; }

div.hexy_content div.bigbox_outer.comments {
  font-size: 80%;
  font-family: Times New Roman, Times, serif; }
div.hexy_content div.bigbox.comments {
  padding-bottom: 1.0em; }
div.hexy_content .important_link {
  font-size: 160%; font-weight: bold; }

@media (min-width: 30em) {
  div.hexy_content div.bigbox_outer {
    padding: 0.6em 1.8em; }
  div.hexy_content div.bigbox {
    border-radius: 2.2em;
    padding: 0.7em 1em;
  }
  div.hexy_content div.bigbox.thankyou {
    padding: 1.8em 1em; }
  div.hexy_content div.bigbox_outer.last { padding-bottom: 1.2em; }
  div.hexy_content div.bigbox_outer:first-child { padding-top: 1.2em; }
  div.hexy_content {
    font-size: 1.2em; 
  }
  div.hexy_content div.bigbox_outer.comments {
    font-size: 70%; }
}
@media (min-width: 13em) {
  div.hexy_content a.lesswrap {
    white-space: nowrap;
  }
}
</style>
''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''<main>
  <div id="content" class="hexy_content">
<div class="bigbox_outer">
<div class="bigbox">
  <h1>Hexy Bondage</h1>
  <div class="subtitle">'''+ blurb +'''</div>
  <p>
Hexy Bondage is a game where in-game actions cause you to be tied up in real life.
  </p>
  <p>
Players take turns placing tiles. Each tile has an icon (hand, foot, torso, crotch, furniture...)
and some paths. The paths can be used to connect icons together. Connections cause
things to happen in real life, like tying your body parts together. A player wins
when their “opponent” is too tied up to reach the board.
  </p>
  <p><a class=" important_link lesswrap" href="/hexy/hexy-bondage-rules.pdf">Read the full rules (pdf)</a></p>
  <p> <a class=" important_link lesswrap" href="/hexy/hexy-bondage-tiles.pdf">Download printable tiles</a> </p>
  <p class="hidden_from_restricted_users">If you like this game, consider <a href="https://www.patreon.com/EliDupree">supporting me on Patreon</a> so that I can continue making awesome things and sharing them for free on the Internet.</p>
</div>
</div>
<div class="bigbox_outer">
<div class="bigbox">
  <h2>Extras:</h2>
  <p>Tile sheets for extra players:
    <a class="lesswrap" href="/hexy/hexy-bondage-extra-tiles-green.pdf">green checkers</a>,
    <a class="lesswrap" href="/hexy/hexy-bondage-extra-tiles-pink.pdf">pink polka dots</a>,
    <a class="lesswrap" href="/hexy/hexy-bondage-extra-tiles-blue.pdf">blue waves</a>,
    <a class="lesswrap" href="/hexy/hexy-bondage-extra-tiles-purple.pdf">purple stripes</a></p>
  <p>Black-and-white versions of tiles for extra players:
    <a href="/hexy/hexy-bondage-extra-tiles-checkers.pdf">checkers</a>,
    <a href="/hexy/hexy-bondage-extra-tiles-polkadots.pdf">polka dots</a>,
    <a href="/hexy/hexy-bondage-extra-tiles-waves.pdf">waves</a>,
    <a href="/hexy/hexy-bondage-extra-tiles-stripes.pdf">stripes</a></p>
  <p><a href="/hexy/hexy-bondage-blank-tiles.pdf">Sheet of blank tiles</a></p>
</div>
</div>
<div class="bigbox_outer narrower comments last">
<div class="bigbox narrower comments last">
  '''+blog.comments_section("hexy")+'''
</div>
</div>
  </div>
</main>'''), {"html_class":"hexy", "blurb": blurb + ".", "blurb_image": "/media/hexy-thumbnail.png?rr"}
  )
  
  utils.make_page (page_dict,
    '/hexy-future',
      "Hexy Bondage ⊂ Eli Dupree's website",
      r'''
<style>

.tile {transition-duration: 1s; --path-fill: #808080; }

</style>
''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''<main>
  <div id="content">
    '''+ trimmed_svg+'''
  </div>
</main>'''), {"html_class":"hexy", "blurb": blurb + ".", "blurb_image": "/media/hexy-thumbnail.png?rr", "after_body":'''

     <script type="text/javascript">
       window.hexy_tile_ids = ['''+ (",".join (['"'+id+'"' for id in tile_ids])) +''']
     </script>
     
     <script type="text/javascript" src="/media/hexy.js?rr"></script>
'''}
  )

