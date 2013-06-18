

import css

category_width = 10
num_categories = 4
all_categories_width = category_width * num_categories
category_border_width = 1
category_image_width = category_width - category_border_width
bar_height = 3
home_width = bar_height*3
categories_hit_home_width = all_categories_width + 2*home_width

css.insert('''

div.top_bar {
  display:inline-block;
  width:100%;
  background-color:black;
  background-image: url("/top-bar-background.png");
  background-size: 100% '''+str(bar_height)+'''em; }

div.top_bar_home {
  position:absolute;
  width:'''+str(home_width)+'''em; height:'''+str(bar_height)+'''em;
  background-color:black; color:yellow; }
img.top_bar_home_image{
  width:'''+str(home_width)+'''em; height:'''+str(bar_height)+'''em }

div.top_bar_categories {
  margin-left:auto; margin-right:auto;
  width:'''+str(all_categories_width)+'''em; height:'''+str(bar_height)+'''em;
  background-color:orange; }
a.top_bar_category_link{ display:inline-block; }
a:link.top_bar_category_link{ color:yellow }
a:visited.top_bar_category_link{ color:orange }
span.top_bar_category{
  position:relative; display:inline-block;
  width:'''+str(category_image_width)+'''em; height:'''+str(bar_height)+'''em;
  border-right:'''+str(category_border_width)+'''em solid black;
  text-align:center;
  background-color:red;
  background-image: url("http://deqyc5bzdh53a.cloudfront.net/biscuits_2013_06_16.jpg");
  background-size: '''+str(category_image_width)+'''em '''+str(bar_height)+'''em;
  margin-bottom:-1em; } /* the negative margin-bottom is to eliminate a gutter whose origins we don't understand */
span.top_bar_category_text{
  position:absolute; display:block;
  bottom:0; right:0; width:5em;
  background-color:black;
  font-size:120%; font-weight:bold; text-decoration:underline; }
  
div.top_bar_login{
  position:absolute;
  right:0; top:0;
  height:'''+str(bar_height)+'''em;
  background-color:black; color:yellow; }

@media screen and (max-width: '''+str(categories_hit_home_width)+'''em) {
  div.top_bar_categories {
    display: inline-block;
    margin-left:'''+str(home_width)+'''em; margin-right:0;
  }
  div.top_bar_home {
    float: none;
  }
}
''')

def home_string(you_are_here):
  return '''<div class="top_bar_home"><a class="top_bar_category_link" href="/"><img class="top_bar_home_image" src="/site-logo.png" /></a></div>'''
def games_string(you_are_here):
  return '''<a class="top_bar_category_link" href="/games"><span class="top_bar_category"><span class="top_bar_category_text">Games</span></span></a>'''
def comics_string(you_are_here):
  return '''<a class="top_bar_category_link" href="/comics"><span class="top_bar_category"><span class="top_bar_category_text">Comics</span></span></a>'''
def blog_string(you_are_here):
  return '''<a class="top_bar_category_link" href="/blog"><span class="top_bar_category"><span class="top_bar_category_text">Blog</span></span></a>'''
def shop_string(you_are_here):
  return '''<a class="top_bar_category_link" href="https://secure.elidupree.com/shop"><span class="top_bar_category"><span class="top_bar_category_text">Shop</span></span></a>'''

def categories_wrap(contents):
  return '<div class="top_bar_categories">'+contents+'</div>'

css.insert('''div.top_bar{ background-color:black; display:inline-block; width:100%; padding:0; margin:0 }''')
def bar_wrap(contents):
  return '<div class="top_bar">'+contents+'</div>'

def top_bar(category):
  home   =   home_string(category ==   "home")
  games  =  games_string(category ==  "games")
  comics = comics_string(category == "comics")
  blog   =   blog_string(category ==   "blog")
  shop   =   shop_string(category ==   "shop")
  login  = '''<div class="top_bar_login">Login repr</div>'''
  return bar_wrap(home+categories_wrap(games+comics+blog+shop)+login)
