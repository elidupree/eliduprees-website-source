

import css

css.insert('''a.top_bar_category_link{ display:inline-block; }
a:link.top_bar_category_link{ color:yellow }
a:visited.top_bar_category_link{ color:orange }''')
css.insert('''span.top_bar_category{ position:relative; display:inline-block; width:9em; height:3em; border-right:1em solid black; text-align:center; background-color:red; background-image: url("http://deqyc5bzdh53a.cloudfront.net/biscuits_2013_06_16.jpg"); background-size: 9em 3em; margin-bottom:-1em; }''') # the negative margin-bottom is to eliminate a gutter whose origins we don't understand
css.insert("span.top_bar_category_text{ position:absolute; display:block; bottom:0; background-color:black; font-size:120%; font-weight:bold; text-decoration:underline; width:5em; right:0; }")

css.insert("div.top_bar_home{ float:left; background-color:black; color:yellow; }")
css.insert("img.top_bar_home_image{ width:3em; height:3em }")
def home_string(you_are_here):
  return '''<div class="top_bar_home"><a class="top_bar_category_link" href="/"><img class="top_bar_home_image" src="http://www.elidupree.com/main/avatars/Eli_Dupree.jpg" /> Eli Dupree's Website</a></div>'''
def games_string(you_are_here):
  return '''<a class="top_bar_category_link" href="/games"><span class="top_bar_category"><span class="top_bar_category_text">Games</span></span></a>'''
def comics_string(you_are_here):
  return '''<a class="top_bar_category_link" href="/comics"><span class="top_bar_category"><span class="top_bar_category_text">Comics</span></span></a>'''
def blog_string(you_are_here):
  return '''<a class="top_bar_category_link" href="/blog"><span class="top_bar_category"><span class="top_bar_category_text">Blog</span></span></a>'''
def shop_string(you_are_here):
  return '''<a class="top_bar_category_link" href="https://secure.elidupree.com/shop"><span class="top_bar_category"><span class="top_bar_category_text">Shop</span></span></a>'''

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
