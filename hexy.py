#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import html_pages
import bars
import exmxaxixl
import blog
import re
import xml.etree.ElementTree as XML
import subprocess

tile_ids = []
with open ("./hexy_source/tile_ids_hack.svg", encoding = "utf-8") as something:
  for match in re.finditer(r'''id="(g\d*?)"''', something.read()):
    id = match.group (1)
    if id != "layer1":
      tile_ids.append (match.group (1))

def build_hexy():
  source_svg = ""
  used_ids = {}
  with open ("./hexy_source/game.svg", encoding = "utf-8") as source_svg_file:
    source_svg = source_svg_file.read()

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
  find (elements_by_id ["path16699-3"])

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
  modified.set ("style", "display: none")

  text_ids = []
  for element in modified.findall (".//*[@"+svg_id+"]"):#for element in modified.findall (".//text"):
    if element.tag == "{http://www.w3.org/2000/svg}text":
      text_ids.append(element.get (svg_id))
    
  trimmed_svg = XML.tostring (modified, encoding = "unicode", method = "html")

  with open ("./hexy_generated/trimmed.svg", "w", encoding = "utf-8") as dst_svg_file:
    print (trimmed_svg, file=dst_svg_file)

  Inkscape_commands = ["inkscape"]
  for id in text_ids:
    Inkscape_commands.extend ([
      "--select=" + id,
      "--verb", "ObjectToPath",
    ])
  Inkscape_commands.extend (["--verb", "FileSave", "--verb", "FileClose", "--verb", "FileQuit", "./hexy_generated/trimmed.svg"])
  print(Inkscape_commands)
  subprocess.run (Inkscape_commands)

with open ("./hexy_generated/trimmed.svg", "r", encoding = "utf-8") as dst_svg_file:
  trimmed_svg = dst_svg_file.read()

blurb = "A sexual board game for two or more players"
	  
def add_game(page_dict):
  utils.make_page (page_dict,
    '/hexy-classic',
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
  <p>In June 2017, I made <a href="/hexy">a web version of Hexy Bondage for players to play together on the same device</a>. The web version is generally better than this printable version. But I'm leaving this older, printable version available in case you find it useful.</p>
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
  '''+blog.comments_section("hexy_classic")+'''
</div>
</div>
  </div>
</main>'''), {"html_class":"hexy", "blurb": blurb + ".", "blurb_image": "/media/hexy-thumbnail.png?rr"}
  )
  
  """
  utils.make_page (page_dict,
    '/hexy-future',
      "Hexy Bondage ⊂ Eli Dupree's website",
      r'''
<style>

.tile {
  transition-duration: 0.6s;
}
.rotation_arrow {
  --arrow-fill: #ffffff;
}
.rotation_arrow:hover {
  --arrow-fill: #ffff00;
}
button {
  font-size: 120%;
  padding: 3px 5px;
  border:2px solid black;
  border-radius:5px;
}

</style>
<script src="https://unpkg.com/react@latest/dist/react.js"></script>
<script src="https://unpkg.com/react-dom@latest/dist/react-dom.js"></script>
<script src="https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>
''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''<main>
  <div id="content">
    <!-- <div id="messages"></div> -->
    
    <!-- <div id="tile_controls"></div> -->
  </div>
  '''+ trimmed_svg+'''
</main>'''), {"html_class":"hexy", "blurb": blurb + ".", "blurb_image": "/media/hexy-thumbnail.png?rr", "after_body":'''

     <script type="text/javascript" src="/media/lodash.min.js?rr"></script>

     <script type="text/javascript">
       window.hexy_tile_ids = ['''+ (",".join (['"'+id+'"' for id in tile_ids])) +''']
     </script>
     
     <!-- <script type="text/javascript" src="/media/hexy.js?rr"></script> -->
     <script type="text/babel" src="/media/hexy-react.js?rr">
'''}
  )
  """
  
  utils.make_page (page_dict,
    '/hexy',
      "Hexy Bondage ⊂ Eli Dupree's website",
      r'''
<style>

html,body {
  background-color: var(--meta-fill);
  --hex-fill: #ffffff;
  --hex-stroke: transparent;
  --meta-stroke: black;
  --meta-fill: #ccc;
}
.game_svg {
  display: block;
  /*margin: 0 auto;*/
  /* prevent it from overflowing its box before being sized */
  width: 0; height: 0;
}
.message_area {
  /*background-color:#ffaaaa;*/
  margin: 0.2em;
  padding: 0.5em;
  border-radius: 1em;
  border: 0.2em solid var(--meta-stroke);
  /*color: var(--meta-stroke);*/
  font-family: Arial, Helvetica, sans-serif;
  flex-grow: 1;
}
.message_area p {
  margin: 0;
  line-height: 1.10em;
}
.message_area p~p {
  margin-top: 0.5em;
}
.tile {
  /*transition-duration: 0.6s;*/
}
.prompt_options {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.prompt_option {
  font-size: 100%;
  margin: 0.5em;
  white-space: normal;
}

input[type="button"],.fake_button {
  background-color: var(--meta-fill);
  border: 0.2em solid var(--meta-stroke);
  padding: 0.5em;
  border-radius: 1em;
  color: var(--meta-stroke);
  font-family: Arial, Helvetica, sans-serif;
  cursor: pointer;
}
input[type="button"]:hover,.fake_button:hover {
  background-color: var(--meta-stroke);
  border-color: 0.2em solid var(--meta-fill);
  color: var(--meta-fill);
}

.board_container {
  width: 100%;
  overflow: auto;
}
.non_board_container {
  display: flex;
  font-size: 3vh;
}
.buttons_area {
  display: flex;
  flex-direction: column;
}
.buttons_area input[type="button"] {
  display: block;
  font-size: 100%;
  padding: 0.3em;
  margin: 0.2em;}


#menu_wrapper {
  position: fixed;
  left: 0; right: 0; top: 0; bottom: 0;
}
#menu {
  position: fixed;
  left: 5%; right: 5%; top: 8%; bottom: 5%;
  border: 1.5vh solid black; border-radius: 6vh;
  box-shadow: 10px 5px 15px #fff;
  background-color: white;
  --meta-stroke: black;
  --meta-fill: white;
  text-align: center;
}
h1 {font-size: 200%;}
h2 {font-size: 150%; margin: 0.5em;}
#menu p {}
#menu ul {text-align: left; line-height: 1.35em;}
#menu_contents {
  padding: 2vh;
  overflow: auto;
}
#menu_navigation {
  padding: 0.8em 0.2em;
  background-color: #aaa;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.modes {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  max-width: 40em;
  margin: 0 auto;
  text-align: left;
}
.mode_box {
  margin:0.2em;
}
.modes input {
  width:2em; height:2em; vertical-align: middle;
}
.modes label {
  vertical-align: middle; margin-left:0.2em;
}

.players {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
.player_options {
  margin: 0.2em;
  border-radius:0.4em;
  padding:0.5em;
  background-color:#ddd;
}
.player_options input[type="text"] {
  width: 6em;
}

.fake_boards {
  display: flex ;
  justify-content: center;
}
.fake_board {
  margin: 0.6em;
  flex-shrink: 0;
}

.connection_type {
  display: inline-block;
  margin: 0.6em;
  max-width: 40em;
  background-color:#ccc;
}
@media screen and (max-width: 400px) {
  .fake_board {
    margin: 0.1em;
    flex-shrink: 0;
  }
  .connection_type {
    margin: 0.6em -0.2em;
  }
}
.connection_type p {
  padding: 0 1.1em;
}
.connection_type .fake_board {
  margin: 0.1em;
}

#comments {
  display: none;
}

.noscript {
  margin: 3em auto;
  padding: 0 1.1em;
  max-width: 40em;
  font-size: 130%;
}

</style>
''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''<main>
  <div id="content">
    <div class="noscript">This game requires JavaScript to play. To play, enable JavaScript in your browser and reload the page. Alternatively, look at <a href="/hexy-classic">the older printable board game</a>, which doesn't require JavaScript.
    <!-- <div id="messages"></div> -->
    
    <!-- <div id="tile_controls"></div> -->
  </div>
  '''+blog.comments_section("hexy")+'''
  '''+ trimmed_svg+'''
</main>'''), {"html_class":"hexy", "blurb": "A sexual game for two players (or more) to play together on the same device.", "blurb_image": "/media/hexy-thumbnail.png?rr", "after_body":'''

     <script type="text/javascript" src="/media/lodash.min.js?rr"></script>

     <script type="text/javascript">
       window.hexy_tile_ids = ['''+ (",".join (['"'+id+'"' for id in tile_ids])) +''']
     </script>
     
     <script type="text/javascript" src="/media/hexy-3-mechanics.js?rr"></script>
     <script type="text/javascript" src="/media/hexy-3-game-modes.js?rr"></script>
     <script type="text/javascript" src="/media/hexy-3-game-ui.js?rr"></script>
     <script type="text/javascript" src="/media/hexy-3-meta-ui.js?rr"></script>
'''}
  )


