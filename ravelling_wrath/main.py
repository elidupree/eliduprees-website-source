#!/usr/bin/python3
# -*- coding: utf-8 -*-

import ravelling_wrath.chapter_01
import ravelling_wrath.chapter_02
import ravelling_wrath.definitions

blurb = ravelling_wrath.definitions.blurb

# https://programmers.stackexchange.com/questions/254279/why-doesnt-python-have-a-flatten-function-for-lists
def flatten(l):
  return [x for y in l for x in y]

posts = flatten([
  ravelling_wrath.chapter_01.posts,
  ravelling_wrath.chapter_02.posts,
])
