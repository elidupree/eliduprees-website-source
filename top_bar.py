

import css

bar_height = 3
category_button_width = 9
num_categories = 5
category_border_width = .7
all_categories_width = category_button_width * num_categories + category_border_width * (num_categories - 1)
category_button_height = bar_height - category_border_width
home_image_width = bar_height
home_text_width_twolines = 7
home_width = home_image_width + home_text_width_twolines
login_width = 5
categories_hit_home_width = all_categories_width + 2*home_width
categories_hit_login_width = all_categories_width + home_width + login_width
categories_hit_home_image_width = all_categories_width + 2*home_image_width

button_border_radius = 0.5

css.insert('''

div.top_bar {
  display:inline-block;
  width:100%;
  font-family: Arial, Helvetica, sans-serif;
  background-color:black;
  background-image: url("/top-bar-background.png");
  background-size: 100% 100%; }

div.top_bar_home {
  position:absolute;
  width:'''+str(home_width)+'''em; height:'''+str(bar_height)+'''em; }
img.top_bar_home_image {
  vertical-align:top;
  display:inline-block;
  width:'''+str(home_image_width)+'''em; height:'''+str(bar_height)+'''em; }
span.top_bar_home_text {
  padding: 0.25em 0em;
  display:inline-block;
  width:'''+str(home_text_width_twolines - 1)+'''em; height:'''+str(bar_height - 0.5)+'''em;
  color:black; }

div.top_bar_categories {
  margin-left:auto; margin-right:auto;
  max-width:'''+str(all_categories_width)+'''em;
  background-color: transparent; }
a.top_bar_category_link {
  display:inline-block;
  border-top:'''    +str(category_border_width / 2)+'''em solid transparent;
  border-bottom: '''+str(category_border_width / 2)+'''em solid transparent;
  border-right:'''+str(category_border_width)+'''em solid transparent; }
a.top_bar_category_link.far_right {
  border-right:0; }
a:link.top_bar_category_link{ color:yellow }
a:visited.top_bar_category_link{ color:orange }
span.top_bar_category {
  position:relative; display:inline-block;
  width:'''+str(category_button_width)+'''em; height:'''+str(category_button_height)+'''em;
  text-align:center;
  background-color: #444444;
  background-image: url("http://deqyc5bzdh53a.cloudfront.net/biscuits_2013_06_16.jpg");
  background-size:'''+str(category_button_width)+'''em '''+str(category_button_height)+'''em;
  border-radius:'''+str(button_border_radius)+'''em;
  vertical-align: bottom; } /* since it's an inline-block, we need this to stop it from creating a gutter for potential descenders */
span.top_bar_category_text{
  position:absolute; display:block;
  bottom:0; right:0; width:5em;
  background-color:black;
  border-bottom-right-radius:'''+str(button_border_radius)+'''em;
  border-top-left-radius:'''+str(button_border_radius)+'''em;
  font-size:120%; font-weight:bold; text-decoration:underline; }
  
div.top_bar_login {
  position:absolute;
  right:0; top:0;
  width:'''+str(login_width - 1)+'''em; height:'''+str(bar_height - 0.5)+'''em;
  padding: 0.25em 0.5em;
  text-align: right; }
a.top_bar_login_link {
  color:black; text-decoration:underline; }

@media screen and (max-width: '''+str(categories_hit_home_width)+'''em) {
  div.top_bar_categories {
    margin-left:'''+str(home_width)+'''em; margin-right:0;
  }
}
@media screen and (max-width: '''+str(categories_hit_login_width)+'''em) {
  div.top_bar_categories {
    
    margin-left:auto; margin-right:auto;
    margin-top: 1.5em; }
  div.top_bar_home {
    width: 20em; }
  span.top_bar_home_text {
    width: 15em; }
  div.top_bar_login {
    width: 20em; }
}
@media screen and (max-width: '''+str(categories_hit_home_image_width)+'''em) {
  img.top_bar_home_image {
    vertical-align:top;
    display:inline-block;
    width:1.5em; height:1.5em; }
}
''')

def home_string(you_are_here):
  return '''<div class="top_bar_home"><a href="/"><img class="top_bar_home_image" src="/site-logo.png" /><span class="top_bar_home_text">Eli Dupree's website</span></a></div>'''
def games_string(you_are_here):
  return '''<a class="top_bar_category_link" href="/games"><span class="top_bar_category"><span class="top_bar_category_text">Games</span></span></a>'''
def comics_string(you_are_here):
  return '''<a class="top_bar_category_link" href="/comics"><span class="top_bar_category"><span class="top_bar_category_text">Comics</span></span></a>'''
def pacman_string(you_are_here):
  return '''<a class="top_bar_category_link" href="/pacman"><span class="top_bar_category"><span class="top_bar_category_text">Pacman</span></span></a>'''
def blog_string(you_are_here):
  return '''<a class="top_bar_category_link" href="/blog"><span class="top_bar_category"><span class="top_bar_category_text">Blog</span></span></a>'''
def shop_string(you_are_here):
  return '''<a class="top_bar_category_link far_right" href="https://secure.elidupree.com/shop"><span class="top_bar_category"><span class="top_bar_category_text">Shop</span></span></a>'''

def categories_wrap(contents):
  return '<div class="top_bar_categories">'+contents+'</div>'

css.insert('''div.top_bar{ background-color:black; display:inline-block; width:100%; padding:0; margin:0 }''')
def bar_wrap(contents):
  return '<div class="top_bar">'+contents+'</div>'

def top_bar(category):
  home   =   home_string(category ==   "home")
  games  =  games_string(category ==  "games")
  comics = comics_string(category == "comics")
  pacman = pacman_string(category == "pacman")
  blog   =   blog_string(category ==   "blog")
  shop   =   shop_string(category ==   "shop")
  login  = '''<div class="top_bar_login"><a class="top_bar_login_link" href="">Login / Register</a></div>'''
  return bar_wrap(home+categories_wrap(games+comics+pacman+blog+shop)+login)
