#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division



bar_height = 3
category_button_width = 9
category_text_width_regular_ems = 6
category_text_width_modified_ems = category_text_width_regular_ems / 1.2
num_categories = 5
category_border_width = .65
all_categories_width = category_button_width * num_categories + category_border_width * (num_categories - 1)
category_button_height = bar_height - category_border_width
home_image_width = bar_height * 2 / 3
home_image_padding_on_each_side = home_image_width / 4
home_image_padded_width = home_image_width + 2*home_image_padding_on_each_side
home_text_width_twolines = 7
home_width = home_image_padded_width + home_text_width_twolines
text_parts_compressed_height = 1.5
categories_hit_home_width = all_categories_width + 2*home_width
categories_hit_right_width = all_categories_width + home_width + category_border_width
categories_hit_home_image_width = all_categories_width + home_image_padded_width + category_border_width
categories_get_squished_width = all_categories_width + category_border_width + home_image_padded_width/2
categories_get_very_squished_width = category_text_width_regular_ems * num_categories * 1.2 + home_image_padded_width/2

button_border_radius = 0.5

import css
import blog
import comics

css.insert('''
div.top_bar {
  position: relative;
  display: inline-block;
  width: 100%; min-height:'''+str(bar_height)+'''em;
  font-family: Arial, Helvetica, sans-serif;
  background-color: black;
  background-image: url("/media/top-bar-background.png?rr");
  background-size: 100% 100%; }
.voldemorts_children div.top_bar {
  background-image: url("/media/top-bar-background-vc.png?rr"); }

div.top_bar_home {
  position:absolute;
  width:'''+str(home_width)+'''em; height:'''+str(bar_height)+'''em; }
img.top_bar_home_image {
  vertical-align:top;
  display:inline-block;
  width:'''+str(home_image_width)+'''em; height:'''+str(bar_height)+'''em;
  padding:0 '''+str(home_image_padding_on_each_side)+'''em }
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
.voldemorts_children a:link.top_bar_category_link{ color:#b3921c }
.voldemorts_children a:visited.top_bar_category_link{ color:#9a5419 }
span.top_bar_category {
  position:relative; display:inline-block;
  width:'''+str(category_button_width)+'''em; height:'''+str(category_button_height)+'''em;
  text-align:center;
  background-color: #444444;
  border-radius:'''+str(button_border_radius)+'''em;
  vertical-align: bottom; } /* since it's an inline-block, we need this to stop it from creating a gutter for potential descenders */
span.top_bar_category.games {
  background-image: url("/media/green-caves-thumbnail.png?rr");
  background-size:'''+str(category_button_width)+'''em '''+str(category_button_height)+'''em; }
span.top_bar_category.stories {
  background-image: url("/media/NWIA_thumbnail.png?rr");
  background-size:'''+str(category_button_width)+'''em '''+str(category_button_height)+'''em; }
span.top_bar_category.comics {
  background-image: url("'''+comics.last_comic_thumbnail_url()+'''");
  background-size:'''+str(category_button_width)+'''em '''+str(category_button_height)+'''em; }
span.top_bar_category.misc  {
  background-image: url("/media/voice-practice-tool-screenshot.png?rr");
  background-size:'''+str(category_button_width)+'''em '''+str(category_button_height)+'''em; }

span.top_bar_category_text {
  position:absolute; display:block;
  bottom:0; right:0; width:'''+str(category_text_width_modified_ems)+'''em;
  background-color:black;
  border-bottom-right-radius:'''+str(button_border_radius)+'''em;
  border-top-left-radius:'''+str(button_border_radius)+'''em;
  font-size:120%; font-weight:bold; text-decoration:underline; }
span.top_bar_blog_preview_text {
  border-radius:'''+str(button_border_radius)+'''em;
  display:block;
  height: 100%;
  width: 100%;
  padding: 0.1em 0.25em;
  box-sizing: border-box;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  font-weight:bold;
  overflow: hidden;
  text-align: left;
  background-color: #ddb;
  border-top: 0.25em solid #886;
  border-left: 0.25em solid #886;
  color: #886; }
.voldemorts_children span.top_bar_blog_preview_text {
  background-color: #777060;
  border-top: 0.25em solid #432;
  border-left: 0.25em solid #432;
  color: #432;
  }

@media screen and (max-width: '''+str(categories_hit_home_width)+'''em) {
  div.top_bar_categories {
    margin-left:'''+str(home_width)+'''em; margin-right:auto;
  }
}
@media screen and (max-width: '''+str(categories_hit_right_width)+'''em) {
  div.top_bar_categories {
    margin-left:auto; margin-right:'''+str(category_border_width)+'''em;
  }
  div.top_bar_home {
    width: '''+str(home_image_padded_width)+'''em; }
  span.top_bar_home_text {
    display: none; }
}
@media screen and (max-width: '''+str(categories_hit_home_image_width)+'''em) {
  img.top_bar_home_image {
    width:'''+str(home_image_width/2)+'''em; height:'''+str(bar_height/2)+'''em;
    padding:'''+str(bar_height/4)+'''em '''+str(home_image_padding_on_each_side/2)+'''em }
}
@media screen and (max-width: '''+str(categories_get_squished_width)+'''em) {
  div.top_bar_categories {
    margin-left:'''+str(home_image_padded_width/2)+'''em;
    margin-right:0;
    max-width:none; }
  a.top_bar_category_link {
    width:'''+str(100 / (num_categories))+'''%;
    border-right:0 }
  span.top_bar_category {
    width:'''+str(100 * category_button_width / (category_button_width + category_border_width))+'''%; }
}
@media screen and (max-width: '''+str(categories_get_very_squished_width)+'''em) {
  span.top_bar_category_text {
    font-size: 100%;
    font-size: '''+ str(24/num_categories) +'''vw;
    width: 100%;
    border-top-left-radius:0;
    border-bottom-left-radius:'''+str(button_border_radius)+'''em;
  }
}
''')

def home_string(you_are_here):
  return '''<div class="top_bar_home"><a href="/"><img alt="The website icon, a smiling face with a wizard hat and a broken version of the 'male' and 'female' symbols." class="top_bar_home_image" src="/media/site-logo-transparent-nosides.png?rr" /><span class="top_bar_home_text">Eli Dupree's website</span></a></div>'''
def games_string(you_are_here):
  return '''<a class="top_bar_category_link" href="/games"><span class="top_bar_category games"><span class="top_bar_category_text">Games</span></span></a>'''
def comics_string(you_are_here):
  return '''<a class="top_bar_category_link" href="/comics"><span class="top_bar_category comics"><span class="top_bar_category_text">Comics</span></span></a>'''
def stories_string(you_are_here):
  return '''<a class="top_bar_category_link" href="/stories"><span class="top_bar_category stories"><span class="top_bar_category_text">Stories</span></span></a>'''
def blog_string(you_are_here):
  return '''<a class="top_bar_category_link" href="/blog"><span class="top_bar_category blog"><span class="top_bar_blog_preview_text">'''+blog.latest_post_preview_text()+'''</span><span class="top_bar_category_text">Blog</span></span></a>'''
def misc_string(you_are_here):
  return '''<a class="top_bar_category_link far_right" href="/misc"><span class="top_bar_category misc"><span class="top_bar_category_text">Misc</span></span></a>'''

def shop_string(you_are_here):
  return '''<a class="top_bar_category_link far_right" href="https://secure.elidupree.com/shop"><span class="top_bar_category"><span class="top_bar_category_text">Shop</span></span></a>'''

def categories_wrap(contents):
  return '<div class="top_bar_categories">'+contents+'</div>'
  
def top_bar_contents(info):
  home    =    home_string(   "home" in info)
  games   =   games_string(  "games" in info)
  comics  =  comics_string( "comics" in info)
  stories = stories_string("stories" in info)
  blog    =    blog_string(   "blog" in info)
  misc    =    misc_string(   "misc" in info)
  shop    =    shop_string(   "shop" in info)
  return home+categories_wrap(games+comics+stories+blog+misc+(shop if False else ""))
  
def top_bar(info):
  return '<header><div class="top_bar'+(' '+info["extra_class"] if "extra_class" in info else '')+'">'+top_bar_contents(info)+'</div></header>'
