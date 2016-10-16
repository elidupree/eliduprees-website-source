#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import utils
import blog
import pac_asteroids
import hexy
import green_caves
import the_path


import html_pages
import bars

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
  text = "" +str (node ["search_level"] if "search_level" in node else "inaccessible") + "," +str( "grid".join ([str(index) for index in node ["grid"]]) if node ["grid"] else "no grid")
  if "exit" in node:
    text = text + "exit"
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

search = 0
def evaluate_maze (maze):
  global search
  search = search + 1
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
  elif "parent" in node:
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
  #evaluate_maze (maze)
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
    for child in node ["children"]:
      add_to_grid (node ["grid"], child)

def sever (maze, node):
  children =node ["children"]
  for child in children:
    remove (maze, child)
  node ["children"] = []
  grid = node ["grid"]
  node ["grid"] = None
  return ({"node": node,"children": children, "grid": grid,}, 0)
  
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
      print ("what") #restore (maze, severed)
  return render_maze (maze)

def add_game_pages(page_dict):
  pac_asteroids.add_game (page_dict)
  hexy.add_game (page_dict)
  green_caves.add_game (page_dict)
  the_path.add_game (page_dict)
  
  import voice_practice_tool
  voice_practice_tool.add_page (page_dict)
  import neural_music_generator
  neural_music_generator.add_page (page_dict)
  import codecophony 
  codecophony.add_page (page_dict)
  
  return
  (maze_CSS, maze_HTML) = generate_maze (100, 100)
  
  utils.checked_insert(page_dict,
    '/badly-designed-menus.html',
    html_pages.make_page(
      "badly Designed Menus ⊂ Eli Dupree's website",
      '<style type="text/css">\n' + maze_CSS + '</style>',
      maze_HTML, {}
    )
  )

