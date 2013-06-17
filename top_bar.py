

import css

css.insert("div.top_bar_category{ display:inline-block; width:10em; text-align:center; background-color:red; }")

css.insert("div.top_bar_home{ float:left; background-color:black; color:yellow; }")
css.insert("img.top_bar_home_image{ width:3em; height:3em }")
def home_string(you_are_here):
  return '''<div class="top_bar_home"><a href="/"><img class="top_bar_home_image" src="http://www.elidupree.com/main/avatars/Eli_Dupree.jpg" /> Eli Dupree's Website</a></div>'''
def games_string(you_are_here):
  return '''<div class="top_bar_category"><a href="/games">Games</a></div>'''
def comics_string(you_are_here):
  return '''<div class="top_bar_category"><a href="/comics">Comics</a></div>'''
def blog_string(you_are_here):
  return '''<div class="top_bar_category"><a href="/blog">Blog</a></div>'''
def shop_string(you_are_here):
  return '''<div class="top_bar_category"><a href="https://secure.elidupree.com/shop">Shop</a></div>'''

css.insert("div.top_bar_categories{ margin-left:auto; margin-right:auto; max-width:40em; background-color:orange; height:3em; }")
def categories_wrap(contents):
  return '<div class="top_bar_categories">'+contents+'</div>'

css.insert("div.top_bar{ background-color:yellow; color:black; display:inline-block; width:100%; padding:0; margin:0 }")
def bar_wrap(contents):
  return '<div class="top_bar">'+contents+'</div>'

css.insert("div.top_bar_login{ float:right; height:3em; background-color:black; color:yellow; }")
def top_bar(category):
  home   =   home_string(category ==   "home")
  games  =  games_string(category ==  "games")
  comics = comics_string(category == "comics")
  blog   =   blog_string(category ==   "blog")
  shop   =   shop_string(category ==   "shop")
  login  = '''<div class="top_bar_login">Login repr</div>'''
  return bar_wrap(home+login+categories_wrap(games+comics+blog+shop))
