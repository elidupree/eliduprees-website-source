#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

import utils

auto = {}
tags_list = [
  
  ("announcements", "Major announcements about Eli's life"),
  
  ("neurodiversity", auto),
  ("gender", auto),
  ("ageism", auto),
  ("sex", "Posts about sex and sexuality"),
  ("philosophical", "Posts about other philosophical stuff"),
  
  ("visual art", auto),
  ("writing", auto),
  ("math", "Posts about mathematics"),
  ("programming", "Posts about computer programming"),
  ("game design", auto),
  ("crass physical reality", auto),
  
  ("story ideas", "Story ideas"),
  ("Lasercake", auto),
  ("the graphics editing project", auto),
  ("this website", "Posts about this website itself"),
  ("other websites", "Recommendations of other websites"),
]

for index in range (len (tags_list)):
  tag = tags_list [index]
  if tag [1] == auto:
    tags_list [index] = (tag [0], "Posts about "+ tag [0])

tags = {}
for tag in tags_list:
  tags [tag [0]] = tag [1]

def validate(tag_string):
  if tag_string not in tags:
    raise "Error: Using an undefined tag"

def tag_url(tag_string):
  validate(tag_string)
  return "/blog/tags/"+utils.format_for_url(tag_string)

def tag_link(tag_string, use_rel=False):
  validate(tag_string)
  return '<a '+('rel="tag" ' if use_rel else '')+'href="'+tag_url(tag_string)+'">'+tag_string+'</a>'
