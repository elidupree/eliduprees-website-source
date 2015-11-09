#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime

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

for cat,post_list in posts.items():
  for post_dict in post_list:
    post_dict["path_prefix"] = "/" if cat=="" else "/"+cat+"/"
    post_dict["category"] = cat
    if cat == 'blog':
      post_dict['contents'] += signature

