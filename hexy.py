#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import html_pages
import bars
import exmxaxixl
import blog

source_svg = ""
with open ("./hexy_source/game.svg", encoding = "utf-8") as source_svg_file:
  source_svg = source_svg_file.read()

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


</style>
''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''<main>
  <div id="content">
    '''+source_svg+'''
  </div>
</main>'''), {"html_class":"hexy", "blurb": blurb + ".", "blurb_image": "/media/hexy-thumbnail.png?rr", "after_body":'''

     
     <script type="text/javascript">
$(function(){
  "use strict"
  
  function get_link (whatever) {return whatever.getAttributeNS('http://www.w3.org/1999/xlink', 'xlink:href'); }
  function set_link (whatever, value) {return whatever.setAttributeNS('http://www.w3.org/1999/xlink', 'xlink:href', value); }
  
  function calculate_transform (clone) {
    var original = $(get_link (clone))[0];
    
    var offset = original.getBBox();
    console.log (offset);
    var transform_origin = "50% 50% 0";//""+ (offset.x+0.5*offset.width)+"px "+ (offset.y+0.5*offset.height)+"px 0px";
    console.log (transform_origin);
    var transform ="translate(-"+ (offset.x+0.5*offset.width)+"px, -"+ (offset.y+0.5*offset.height)+"px) translate(500px, 300px) rotate(0.0833turn) scale(36,36)"
    return {"transform-origin": transform_origin, transform: transform}
  }
  
  var whatever =document.createElementNS("http://www.w3.org/2000/svg", 'use');
  set_link (whatever, '#g5028');
  console.log (get_link (whatever));
  $(whatever).css(calculate_transform (whatever));
  //whatever.css({transform:"scale(20, 20)"});
  $("svg").append(whatever);
});
</script>
'''}
  )

