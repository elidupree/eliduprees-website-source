#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import html_pages
import bars
import exmxaxixl
import blog
import re

source_svg = ""
tile_ids = []
with open ("./hexy_source/game.svg", encoding = "utf-8") as source_svg_file:
  source_svg = source_svg_file.read()
with open ("./hexy_source/tile_ids_hack.svg", encoding = "utf-8") as something:
  for match in re.finditer(r'''id="(g\d*?)"(?!>)''', something.read()):
    tile_ids.append (match.group (1))

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

.tile {transition-duration: 1s;}

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
  
  function get_link (whatever) {return whatever.getAttributeNS('http://www.w3.org/1999/xlink', 'href'); }
  function set_link (whatever, value) {return whatever.setAttributeNS('http://www.w3.org/1999/xlink', 'xlink:href', value); }
  
  function random_range (min, max) {
    return min + Math.floor (Math.random()*(max - min));
  }
  function random_choice (sequence) {
    return sequence [random_range (0, sequence.length)];
  }
  
  var tile_ids = ['''+ (",".join (['"'+id+'"' for id in tile_ids])) +''']
  var blank_hex_id = "g7168"
  var long_radius = 36;
  var short_radius = long_radius*0.866;
  
  function tile_position (horizontal, vertical) {
    return {horizontal: horizontal*1.5*long_radius, vertical: vertical*short_radius}
  }
  
  // CSS rotations are clockwise, so I'm making the directions be clockwise so that I don't screw up.
  // Direction 0 is up in user space, up-right in the source (I rotate the tiles by 1/2
  // because I'm familiar with hexagonal tiles being oriented that way in Wesnoth)
  var directions = [
    {horizontal:  0, vertical: -2},
    {horizontal:  1, vertical: -1},
    {horizontal:  1, vertical:  1},
    {horizontal:  0, vertical:  2},
    {horizontal: -1, vertical:  1},
    {horizontal: -1, vertical: -1}
  ];
  
  function in_direction (location, direction) {
    var offset = directions [direction];
    return {horizontal: location.horizontal + offset.horizontal, vertical: location.vertical + offset.vertical};
  }
  
  var dead={};var icon={};var lock={};
  var connections_table = {
    g8043: [3, 2, 1, 0, 5, 4],
    g8261: [2, 4, 0, 5, 1, 3],
    g8571: [2, 3, 0, 1, 5, 4],
    g8657: [1, 0, 3, 2, 5, 4],
    g8985: [3, 4, 5, 0, 1, 2],
    
    g9384: [5, dead, icon, 4, 3, 0],
    g9425: [1, 0, icon, 4, 3, dead],
    g9432: [1, 0, icon, dead, 5, 4],
    g9631: [2, 3, 0, 1, icon, dead],
    g9625: [2, 3, 0, 1, dead, icon],
    g9812: [4, 2, 1, icon, 0, dead],
    g9843: [2, dead, 0, icon, 5, 4],
    g10007: [3, 2, 1, 0, icon, dead],
    g10014: [3, 2, 1, 0, dead, icon],
    g10195: [3, 4, dead, 0, 1, icon],
    g10315: [2, 4, 0, dead, 1, icon],
    g10325: [icon, 4, dead, 5, 1, 3],
    g10573: [lock, lock, lock, 5, lock, 3],
    g10495: [2, 3, 0, 1, lock, lock],
  };
  
  Object.getOwnPropertyNames(connections_table).forEach(function(id) {
    var tile = connections_table [id];
    tile.forEach(function(connection, index) {
      if (typeof connection == "number") {
        if (tile [connection] !== index) {
          console.log ("error: mismatched connections");
        }
      }
    });
  });
  
  function get_connections (element) {
    var direct = connections_table [get_link (element).slice (1)];
    if (direct) {return direct;}
    var indirect;
    $(get_link (element)).children().each (function (index) {
      if (!indirect) {
        var link = get_link (this);
        if (link) {
          indirect = connections_table [link.slice (1)];
        }
      }
    });
    return indirect;
  }
  
  function follow_path (location, from_direction, tile_callback, finish_callback) {
    var tile = get_tile (location);
    if (!tile) {
      if (finish_callback) { finish_callback (location, from_direction); }
      return;
    }
    tile_callback (tile, from_direction);
    var connections = get_connections (tile.element);
    var index = (from_direction + 6 - tile.rotation) % 6;
    var destination = connections[index];
    if (typeof destination === "number") {
      destination = (connections[index] + tile.rotation) % 6;
      //var offset = directions [destination];
      //var next = get_tile (tile.horizontal + offset.horizontal, tile.vertical + offset.vertical);
      //if (next) {
        follow_path(in_direction (location, destination), (destination + 3) % 6, tile_callback, finish_callback);
      //}
    }
    else {
      if (finish_callback) {finish_callback (location, from_direction, tile, destination);}
    }
  }
  
  function draw_path (horizontal, vertical, from_direction) {
    follow_path({horizontal, vertical}, from_direction, function(tile) {
      $(tile.element).css({opacity: 0.5});
    });
  }
  
  function calculate_transform (clone, horizontal, vertical, rotation) {
    var original = $(get_link (clone))[0];
    
    var offset = original.getBBox();
    //console.log (offset);
    var transform_origin = "50% 50% 0";//""+ (offset.x+0.5*offset.width)+"px "+ (offset.y+0.5*offset.height)+"px 0px";
    //console.log (transform_origin);
    var position = tile_position (horizontal, vertical);
    var transform ="translate("+ (-(offset.x+0.5*offset.width))+"px, "+ (-(offset.y+0.5*offset.height))+"px) translate(500px, 300px) translate(" + position.horizontal + "px," + position.vertical + "px) rotate("+(-0.0833 + rotation/6)+"turn) scale(" + long_radius+ "," + long_radius+ ")"
    //console.log (transform);
    return {"transform-origin": transform_origin, transform: transform}
  }
  
  var tiles = {}
  var floating_tile;
  
  function create_clone (id) {
    var whatever =document.createElementNS("http://www.w3.org/2000/svg", 'use');
    set_link (whatever, '#'+id);
    //console.log (get_link (whatever));
    whatever.setAttribute("x", 0);
    whatever.setAttribute("y", 0);
    $("svg").append(whatever);
    return whatever;
  }
  function create_tile (id, rotation) {
    var element = create_clone (id);
    $(element).addClass("tile");
    return {rotation, element};
  }
  function create_border_tile (location) {
    var element = create_clone (blank_hex_id);
    $(element).addClass("tile border").css(calculate_transform (element, location.horizontal, location.vertical, 0)).click(function() {
      set_tile (location, floating_tile);
    });
    set_tile (location, {element: element, rotation: 0, border: true});
  }
  function remove_tile (location) {
    var previous = get_tile (location);
    if (previous) {
      delete previous.horizontal; delete previous.vertical;
      $(previous.element).detach();
      delete tiles ["" + location.horizontal + "_" + location.vertical];
    }
  }
  function set_tile (location, tile) {
    remove_tile (location);
    tiles ["" + location.horizontal + "_" + location.vertical] = tile
    if (tile.horizontal) {
      delete tiles ["" + tile.horizontal + "_" + tile.vertical]
      create_border_tile ({horizontal: tile.horizontal, vertical: tile.vertical});
    }
    tile.horizontal = location.horizontal; tile.vertical = location.vertical;
    $(tile.element).css(calculate_transform (tile.element, location.horizontal, location.vertical, tile.rotation));
    if (!(tile.border || tile === floating_tile)) {
      for (var direction = 0; direction <6 ;++direction) {
        var neighbor = in_direction (location, direction);
        if (!get_tile (neighbor)) {create_border_tile (neighbor);}
      }
    }
  }
  function get_tile (location) {
    return tiles ["" + location.horizontal + "_" + location.vertical]
  }
  
  function hack (horizontal, vertical, rotation) {
    var tile = create_tile(random_choice (tile_ids), rotation);
    //$(whatever).css(calculate_transform (whatever, horizontal, vertical+0.00001, rotation));
   
    $(tile.element).css(calculate_transform (tile.element, horizontal*1.3, vertical*1.3-2, rotation+0.5)).click(function() {
      draw_path(tile.horizontal, tile.vertical, 0);
    });
    //whatever.css({transform:"scale(20, 20)"});
    
    setTimeout (function() {
      set_tile ({horizontal, vertical}, tile);
      //$(whatever).css(calculate_transform (whatever, horizontal, vertical, rotation));
    }, 10);
  }
  for (var index = -5; index <=5;++index) {
    for (var terrible = index-5; terrible <=index+5;terrible+=2) {
      hack (index, terrible, random_range (0, 6));
    }
  }
  floating_tile = create_tile(random_choice (tile_ids), 0);
});
</script>
'''}
  )

