#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import utils
import css
import exmxaxixl
import blog

css.insert('''
body.hexy .bars_outer_box {
  background-color: #878787;
  background-image: url("/media/hexy_bondage_page_background.jpg?rr"); }

div.hexy_content h1{ font-size: 200%; font-weight: bold; padding-top: 0.20em; }
div.hexy_content h2{ font-size: 150%; font-weight: bold; padding-top: 0.30em; }
div.hexy_content p,div.fake_p { margin: 0; padding: 0.5em 0; }
div.hexy_content a:link { color:blue }
div.hexy_content a:visited { color:purple }

div.hexy_content div.subtitle { font-weight: bold; font-size: 90%; padding-bottom: 0.5em;}
div.hexy_content {
  text-align: center;
  font-family: Arial, Helvetica, sans-serif;
  max-width: 50em;
  margin: 0 auto; }
div.hexy_content form,table {
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
  div.hexy_content form.paypal_stuff {
    white-space: nowrap;
  }
}
@media (min-width: 13em) {
  div.hexy_content a.lesswrap {
    white-space: nowrap;
  }
}

''')

import html_pages
import bars

def hexy_page(is_thankyou):
  return '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''<main>
  <div id="content" class="hexy_content">
'''+('''
<div class="bigbox_outer">
<div class="bigbox thankyou">
Thank you for supporting my work! Now go have some fun!
</div>
</div>
''' if is_thankyou else '')+'''
<div class="bigbox_outer">
<div class="bigbox">
  <h1>Hexy Bondage</h1>
  <div class="subtitle">A sexual board game for two or more players</div>
  <p>
Hexy Bondage is a game where in-game actions cause you to be tied up in real life.
  </p>
  <p>
Players take turns placing tiles. Each tile has an icon (hand, foot, torso, crotch, furniture...)
and some paths. The paths can be used to connect icons together. Connections cause
things to happen in real life, like tying your body parts together. A player wins
when their “opponent” is too tied up to reach the board.
  </p>
  <p><a class="lesswrap" href="/hexy/hexy-bondage-rules.pdf">Read the full rules (pdf)</a></p>
</div>
</div>
<div class="bigbox_outer">
<div class="bigbox">
  <div class="fake_p">Tiles (print them, cut them out): <a class="lesswrap" href="/hexy/hexy-bondage-tiles.pdf">Download tiles</a> and/or 
  
<!-- Notes: The PayPal button code modified as follows:
  Remove the table structure and the visible ":"
  add class="paypal_stuff" to the form element
  add class="paynowbutton" to the select and input-image elements
  add selected to the second option
  change button image alt to "Pay Now"
  remove the (probably for tracking and nothing else) pixel gif
-->
<form class="paypal_stuff" action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_s-xclick">
<input type="hidden" name="hosted_button_id" value="VR5BUZK88GMCL">
<input type="hidden" name="on0" value=":">
<select class="paynowbutton" name="os0">
        <option value="Be cool...">Be cool... $10.00 USD</option>
        <option selected value="Be awesome...">Be awesome... $20.00 USD</option>
        <option value="Be extravagant...">Be extravagant... $50.00 USD</option>
</select>
<input type="hidden" name="currency_code" value="USD">
<input class="paynowbutton" type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_paynow_SM.gif" border="0" name="submit" alt="Pay Now">
</form>


</div>
<p>(Paying supports my work, so I can keep making things available to those who can't pay.)</p>
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
<div class="bigbox_outer narrower">
<div class="bigbox narrower">
  <p>Hexy Bondage is a creation of <a class="lesswrap" href="/" xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName" rel="cc:attributionURL">Eli Dupree.</a><br />Contact Eli to report any issues, no matter how minor:<br />'''+exmxaxixl.a(exmxaxixl.axdxrxexsxs)+'''</p>
  <p><a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Hexy Bondage</span> is licensed under a<br /><a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.
  </p>
</div>
</div>
<div class="bigbox_outer narrower comments last">
<div class="bigbox narrower comments last">
  '''+blog.comments_section("hexy")+'''
</div>
</div>
  </div>
</main>''')

import random
import copy
def maze_color ():
  return hex (random.randint( 100, 255)) [2:]

menu_names = "file edit view preferences options settings help about tools history bookmarks accounts sessions messages configure filters windows new... open... create... insert format templates toolbars zoom macros language statistics debug developers"

def render_node (maze, node):
  (CSS, HTML) = render_nodes (maze, node ["children"])
  CSS.append ('''
div.maze div.node_children_'''+  str(node ["index"])  +'''{
display: none}
div.maze div.node_'''+  str(node ["index"])  +''':hover div.node_children_'''+  str(node ["index"])  +'''{
display: block}

div.maze div.node_box_'''+  str(node ["index"])   +''' {
position: absolute;
z-index:'''+str( node ["depth"]*2) +''';
left:'''+str( node ["left"]*100//maze ["width"]) +'''%;
right:'''+str( 100 - ( node ["right"] + 1)*100//maze ["width"]) +'''%;
top:'''+str( node ["top"]*100//maze ["height"]) +'''%;
bottom:'''+str(100 - ( node ["bottom"] + 1)*100//maze ["height"]) +'''%;


}

div.maze div.node_box_'''+  str(node ["index"])   +'''.shown {
background-color:#'''+ maze_color () +maze_color () +maze_color () +''';
}
div.maze div.node_box_'''+  str(node ["index"])   +'''.shadow {
z-index:'''+str( node ["depth"]*2 - 1) +''';
box-shadow: 0.5em 0.5em 1.5em 0.2em black;
}

div.maze div.node_'''+  str(node ["index"])  +''':hover div.node_box_'''+  str(node ["index"])   +'''.shown {
z-index:'''+str( node ["depth"]*2 + 2) +''';

}
div.maze div.node_'''+  str(node ["index"])  +''':hover div.node_box_'''+  str(node ["index"])   +'''.shadow {
z-index:'''+str( node ["depth"]*2 + 1) +''';

}
''')
  text = ""
  if "exit" in node:
    text = "exit"
  return (CSS, 
  '''
<div class=" node_'''+ str(node ["index"])  +'''">
  <div class= "shown node_box_'''+ str(node ["index"])  +'''">'''+ text +'''</div>
  <div class= "shadow node_box_'''+ str(node ["index"])  +'''"></div>
  <div class= "node_children_'''+ str(node ["index"])  +'''">'''+ HTML +'''</div>
</div>''')
  
def render_nodes (maze, nodes):
  (CSS, HTML) = ([], [])
  for node in nodes:
    (CSS_2, HTML_2) = render_node (maze, node)
    CSS.extend (CSS_2)
    HTML.append (HTML_2)
  HTML = "".join (HTML)
  return (CSS, HTML)
  
def render_maze (maze):
  (CSS, HTML) = render_nodes (maze, maze ["top_level"])
  CSS.append ('''
div.maze {
position: relative;
width: 80%;
margin: 0 auto;
height: 40em;}''')
  CSS = "".join (CSS)
  HTML ='''<div class="maze">'''+ HTML +'''</div>'''
  return (CSS, HTML)
  
def evaluate_maze (maze):
  search = {}
  search_levels = [[]]
  level = 0
  exit_level = - 1000
  def find (node, X, Y):
    found = probe_grid (node, X, Y)
    if found and not ("last_search" in found and found ["last_search"] == search):
      found ["last_search"] = search
      found ["search_level"] = level
      found ["search_parent"] = node
      search_levels [level].append (found)
  for X in range (maze ["width"]):
    find (maze, X, 0)
    find (maze, X, maze ["height"] - 1)
  for Y in range (maze ["height"]):
    find (maze, 0, Y)
    find (maze, maze ["width"] - 1, Y)
  while len(search_levels [level]) >0:
    last_level = level
    level += 1
    search_levels.append ([])
    for node in search_levels [last_level]:
      if "exit" in node:
        exit_level = last_level
      for X in range (node ["left"], node ["right"] + 1):
        find (node, X, node ["top"] - 1)
        find (node, X, node ["bottom"] + 1)
      for Y in range (node ["top"], node ["bottom"] + 1):
              find (node, node ["left"] - 1, Y)
              find (node, node ["right"] + 1, Y)
  maze ["evaluation"] = exit_level

def add_to_grid (grid, node):
  for X in range (node ["left"], node ["right"] + 1):
    for Y in range (node ["top"], node ["bottom"] + 1):
      grid [X*10000 + Y] = node
def probe_grid (node, X, Y):
  index = X*10000 + Y
  grid =node ["grid"]
  if grid and index in grid:
    return grid [index]
  if "parent" in node:
    return probe_grid (node ["parent"], X, Y)

def initialize_maze (width, height):
  maze = {"width": width, "height": height}
  node_rows = height//10
  maze ["nodes"] = []
  maze ["top_level"] = []
  row_top = 0
  for row in range (0, node_rows):
    row_bottom = random.randint (row*10 + 8, row*10 + 12)
    if row == node_rows - 1:
      row_bottom = height - 1
    columns = random.randint (width//12, width//8)
    column_left = 0
    for column in range (0, columns):
      column_right = (column +1)*width //columns + random.randint (-2, 2)
      if column == columns - 1:
        column_right = width - 1
      node ={"left": column_left,
        "right": column_right,
        "top": row_top,
        "bottom": row_bottom,
        "index":len( maze ["nodes"]),
        "depth": 1,
        "parent": maze,
        "children": [],
        "grid": None,}
      validate (maze, node)
      maze ["nodes"].append (node)
      maze ["top_level"].append (node)
      column_left = column_right + 1
    row_top = row_bottom + 1
  
  maze ["grid"] = {}
  for node in maze ["nodes"]:
    add_to_grid (maze ["grid"], node)
  probe_grid (maze, width//2, height//2) ["exit"] = True
  evaluate_maze (maze)
  return maze

def validate (maze, node):
  assert (node ["left"] >=0)
  assert (node ["right"] <maze ["width"])  
  assert (node ["top"] >=0)
  assert (node ["bottom"] <maze ["height"])
  assert (node ["left"] <= node ["right"])
  assert (node ["top"] <= node ["bottom"])
  
def expand (maze, node, count):
  if True:
    (top, bottom, left, right, maze_width, maze_height) = random.choice ([
      ("top", "bottom", "left", "right", maze ["width"], maze ["height"]),
      ("left", "right", "top", "bottom", maze ["height"], maze ["width"])])
    width = random.randint( max (15, node [right] - node [left] + 5), 65)
    new_left = random.randint (max(0, node [right] - width +1), min (maze_width - width, node [left]))
    below = random.choice ([True, False])
    rows = min (random.randint( 1, 3), random.randint( 1, 3))
    height = 0
    for row in range (rows):
      row_bottom = height + random.randint (7, 11)
      
      if below:
        absolute_bottom =node [bottom] + row_bottom + 1
        if absolute_bottom>= maze_height:
          break
      else:
        absolute_top =node [top] - row_bottom - 1
        if absolute_top <0:
          break
      columns = random.randint (width//20, width//5)
      column_left = new_left
      for column in range (columns):
        column_right = new_left + (column + 1)*width//columns + random.randint (-1, 1)
        if column == columns -1:
          column_right = new_left + width - 1
        new_node = {
          "parent": node,
          "index": None,
          "depth": node ["depth"] + 1,
          "children": [],
          "grid": None  }
        new_node [left] = column_left
        new_node [right] = column_right
        if below:
          new_node [top] = node [bottom] + height + 1
          new_node [bottom] = absolute_bottom
        else:
          new_node [bottom] = node [top] - height - 1
          new_node [top] = absolute_top
        node["children"].append (new_node)
        validate (maze, new_node)
        record (maze, new_node)
        column_left = column_right +1
      height = row_bottom + 1
    if height ==0:
      return expand (maze, node, count)
    node ["grid"] = {}
    for new_node in node ["children"]:
      add_to_grid (node ["grid"], new_node)

def sever (maze, node):
  children =node ["children"]
  for child in children:
    remove (maze, child)
  node ["children"] = []
  grid = node ["grid"]
  node ["grid"] = None
  return ({"children": children, "grid": grid,}, 0)
  
def remove (maze, node):
  nodes =maze ["nodes"] 
  moved = nodes [len( nodes)-1]
  moved ["index"] = node ["index"]
  nodes [moved ["index"] ] = moved
  nodes.pop ()
  for child in node ["children"]:
    remove (maze, child)
  
def record (maze, node):
  last_index =node ["index"]
  nodes =maze ["nodes"] 
  if last_index is None or len( nodes)<= last_index or nodes [last_index] != node:
    node ["index"] = len(maze ["nodes"])
    maze ["nodes"].append (node)
  for child in node ["children"]:
    record (maze, child)
    
def try_change (maze):
  node = random.choice (maze ["nodes"])
  while "exit" in node or node ["depth"] >random.randint (3, 8):
    node = random.choice (maze ["nodes"])
  (severed, count) = sever (maze, node)
  old_evaluation = maze ["evaluation"]
  if random.choice ([True, False]) and count >0:
    count -= 1
  else:
    count += 1
  expand (maze, node, count)
  evaluate_maze (maze)
  return {"evaluation": old_evaluation, "severed": severed}

def restore (maze, severed):
  maze ["evaluation"] = severed ["evaluation"]
  node =severed ["severed"] ["node"]
  sever (maze, node)
  node ["children"] = severed ["severed"] ["children"]
  node ["grid"] = severed ["severed"] ["grid"]
  record (maze, node)
  
def generate_maze (width, height):
  maze = initialize_maze (width, height)
  iterations = 1000
  for iteration in range (iterations):
    severed = try_change (maze)
    if random.randrange (iterations) <iteration and maze ["evaluation"] <severed ["evaluation"]:
      restore (maze, severed)
  return render_maze (maze)

def add_game_pages(page_dict):
  utils.checked_insert(page_dict,
    '/hexy.html',
    html_pages.make_page(
      "Hexy Bondage ⊂ Eli Dupree's website",
      '',
      hexy_page(False), {"body_class":"hexy"}
    )
  )
  utils.checked_insert(page_dict,
    '/hexy-thank-you.html',
    html_pages.make_page(
      "Hexy Bondage ⊂ Eli Dupree's website",
      '',
      hexy_page(True), {"body_class":"hexy"}
    )
  )
  (maze_CSS, maze_HTML) = generate_maze (100, 100)
  
  utils.checked_insert(page_dict,
    '/badly-designed-menus.html',
    html_pages.make_page(
      "badly Designed Menus ⊂ Eli Dupree's website",
      '<style type="text/css">\n' + maze_CSS + '</style>',
      maze_HTML, {}
    )
  )

