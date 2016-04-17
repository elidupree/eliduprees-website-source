#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

import utils
print ("TODO: have at least one page include an index of all tags")
auto = {}
tags = {
#  "lol":"Posts about laughing out loud",
#  "omg":"Posts about my goodness",
  
  
  "announcements": "major announcements about Eli's life",
  
  "neurodiversity": auto,
  "gender": auto,
  "ageism": auto,
  "sex": "Posts about sex and sexuality",
  "philosophical": "Posts about other philosophical stuff",
  
  "visual art": auto,
  "writing": auto,
  "math": "Posts about mathematics",
  "programming": "Posts about computer programming",
  "crass physical reality": auto,
  
  "Lasercake": auto,
  "the graphics editing project": auto,
  "this website": "Posts about this website itself",
  "other websites": "Recommendations of other websites",
}
for k in tags:
  if tags[k] == auto:
    tags[k] = "Posts about "+k

def validate(tag_string):
  if tag_string not in tags:
    raise "Error: Using an undefined tag"

def tag_url(tag_string):
  validate(tag_string)
  return "/blog/tags/"+utils.format_for_url(tag_string)

def tag_link(tag_string, use_rel=False):
  validate(tag_string)
  return '<a '+('rel="tag" ' if use_rel else '')+'href="'+tag_url(tag_string)+'">'+tag_string+'</a>'
