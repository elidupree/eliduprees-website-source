#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import re
import utils
import css
import sys

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
import posts.blog_12
import posts.blog_13
import posts.blog_14
import posts.blog_15
import posts.not_what_i_am
import posts.time_travelers
import posts.the_23_days_cult
import posts.ravelling_wrath_01
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
  posts.blog_12.posts,
  posts.blog_13.posts,
  posts.blog_14.posts,
  posts.blog_15.posts,
])

stories = flatten([
  posts.not_what_i_am.posts,
  posts.time_travelers.posts,
  posts.the_23_days_cult.posts,
  posts.ravelling_wrath_01.posts,
  posts.stories_01.posts,
])

uncategorized_posts = flatten([
  posts.uncategorized_01.posts,
])

posts = {
  "blog": blog_posts,
  "stories": stories,
  "": uncategorized_posts,
}

signature = "<p> &ndash; Eli</p>"

if "--deploy" in sys.argv:
  for category in posts:
    posts [category] = [post for post in posts [category] if "don't deploy" not in post]

stories_map = {}
for story in posts ["stories"]:
  stories_map [story ["title"]] = story

for cat,post_list in posts.items():
  for post_dict in post_list:
    post_dict["path_prefix"] = "/" if cat=="" else "/"+cat+"/"
    post_dict["category"] = cat
    if "auto_paragraphs" in post_dict:
      post_dict ["contents"] = utils.auto_paragraphs (post_dict ["contents"])
    if cat == 'blog':
      post_dict['contents'] += signature

css.insert ('''
a.small_story {display: block; padding: 0.8em 0; color: black; text-decoration: none;}
a.small_story h2 {font-weight: bold; color: black;}
a.small_story .blurb {font-size:71%;}
.big_story .index_entry {padding-top: 0.8em; padding-bottom: 0.1em; font-weight: bold; font-size: 100%;}
''')

def stories_index (full):
  import blog
  import category_pages
  
  def info (story):
    words = utils.word_count (story ["contents"])
    return " [" + (story ["word_count_override"] if "word_count_override" in story else str(((words + 50)//100)*100) + " words") + "]"
  
  def big_story (story):
    if story not in stories_map:
      return category_pages.exhibit (None, "", None, '<h1>' + story + '</h1>', "Coming Soon...") if full else ''
    story = stories_map [story]
    return category_pages.exhibit (blog.post_permalink (story), "", None, '<h1>' + story ["title"] + '</h1>' + story ["blurb"] + info (story), "Start reading") if full else '<div class=" big_story">' + blog.index_entry_html (story) + '</div>'
  
  def small_story (story):
    if story not in stories_map:
      return '<a class="small_story"><h2>' + story + ": "  + '</h2><span class="blurb"> Coming soon... </span></a>' if full else ''
    story = stories_map [story]
    return '<a class="small_story" href="' + blog.post_permalink (story) +'"><h2 class=" restore_link">' + story ["title"]+ info (story) + ": "  + '</h2><span class="blurb">' + story ["blurb"] + '</span></a>' if full else blog.index_entry_html (story)
    
  def group (name, contents):
    return category_pages.exhibit (None, "", None, '<h1>' + name + '</h1>' + contents, None) if full else '<div class="index_page_entry">' + name +'</div>' + contents
  
  return (
  big_story ("Not What I Am") +
  big_story ("Time Travelers and How to Kill Them: a Practical Guide") +
  group ("Short stories",
    small_story ("Capitalism Sat") + 
    small_story ("Will You Try to Escape?") +
    small_story ("The Sieve") +
    small_story ("Nothing Is Wrong In This World") +
    ""
  ) +
  big_story ("The 23 Days Cult") +
  (category_pages.exhibit ("/blog/tags/story-ideas", "", None, '''<p>Finally, I share <span class="restore_link">additional story ideas on my blog</span> when they are clever enough to be worth sharing, but not compelling enough that I want to write them up in full.</p>''', None) if full else '<div class=" big_story"><div class=" index_entry"> <a href="/blog/tags/story-ideas">Story ideas</a> </div> </div> ')
  )
