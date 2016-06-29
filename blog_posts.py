#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import re
import utils
import css

import posts.blog_01
import posts.blog_02
import posts.blog_03
import posts.blog_04
import posts.blog_05
import posts.blog_06
import posts.blog_07
import posts.blog_08
import posts.blog_09
import posts.blog_10
import posts.blog_11
import posts.not_what_i_am
import posts.stories_01
import posts.uncategorized_01

# https://programmers.stackexchange.com/questions/254279/why-doesnt-python-have-a-flatten-function-for-lists
def flatten(l):
  return [x for y in l for x in y]

blog_posts = flatten([
  posts.blog_01.posts,
  posts.blog_02.posts,
  posts.blog_03.posts,
  posts.blog_04.posts,
  posts.blog_05.posts,
  posts.blog_06.posts,
  posts.blog_07.posts,
  posts.blog_08.posts,
  posts.blog_09.posts,
  posts.blog_10.posts,
  posts.blog_11.posts,
])

stories = flatten([
  posts.not_what_i_am.posts,
  posts.stories_01.posts,
])
stories_map = {}
for story in stories:
  stories_map [story ["title"]] = story

uncategorized_posts = flatten([
  posts.uncategorized_01.posts,
])

posts = {
  "blog": blog_posts,
  "stories": stories,
  "": uncategorized_posts,
}

signature = "<p> &ndash; Eli</p>"

for cat,post_list in posts.items():
  for post_dict in post_list:
    post_dict["path_prefix"] = "/" if cat=="" else "/"+cat+"/"
    post_dict["category"] = cat
    if cat == 'blog':
      post_dict['contents'] += signature

css.insert ('''
a.small_story {display: block; padding: 0.8em 0; text-decoration: none;}
a.small_story h2 {font-weight: bold; color: black;}
a.small_story .blurb {color: black;}
a.small_story .continue_reading {text-decoration: underline;}
.big_story .index_entry {padding-top: 0.8em; padding-bottom: 0.1em; font-weight: bold; font-size: 100%;}
''')

def stories_index (full):
  import blog
  import category_pages
  
  def info (story):
    words = utils.word_count (story ["contents"])
    return " [" + str(((words + 50)//100)*100) + " words]"
  
  def big_story (story):
    return category_pages.exhibit (blog.post_permalink (story), "", None, '<h1>' + story ["title"] + '</h1>' + story ["blurb"] + info (story), "Start reading") if full else '<div class=" big_story">' + blog.index_entry_html (story) + '</div>'
  
  def small_story (story):
    return '<a class="small_story" href="' + blog.post_permalink (story) +'"><h2>' + story ["title"]+ info (story) + ": "  + '</h2><span class="blurb">' + story ["blurb"] + ' </span><span class=" continue_reading">Continue reading</span>' if full else blog.index_entry_html (story)
    
  def group (name, contents):
    return category_pages.exhibit (None, "", None, '<h1>' + name + '</h1>' + contents, None) if full else '<div class="index_page_entry">' + name +'</div>' + contents
  
  return (big_story (stories_map ["Not What I Am"]) + group ("Short stories",
    small_story (stories_map ["Capitalism Sat"])
  ))