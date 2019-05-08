#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

import ravelling_wrath.chapter_01
import ravelling_wrath.chapter_02
import ravelling_wrath.chapter_03
import ravelling_wrath.chapter_04
import ravelling_wrath.chapter_05
import ravelling_wrath.chapter_06
import ravelling_wrath.chapter_07
import ravelling_wrath.chapter_08
import ravelling_wrath.chapter_09
import ravelling_wrath.chapter_10
import ravelling_wrath.chapter_11
import ravelling_wrath.chapter_12
import ravelling_wrath.chapter_13
import ravelling_wrath.chapter_14
import ravelling_wrath.chapter_15
import ravelling_wrath.chapter_16
import ravelling_wrath.chapter_17
import ravelling_wrath.chapter_18
import ravelling_wrath.chapter_19
import ravelling_wrath.chapter_20
import ravelling_wrath.definitions

blurb = ravelling_wrath.definitions.blurb

# https://programmers.stackexchange.com/questions/254279/why-doesnt-python-have-a-flatten-function-for-lists
def flatten(l):
  return [x for y in l for x in y]

posts = flatten([
  ravelling_wrath.chapter_01.posts,
  ravelling_wrath.chapter_02.posts,
  ravelling_wrath.chapter_03.posts,
  ravelling_wrath.chapter_04.posts,
  ravelling_wrath.chapter_05.posts,
  ravelling_wrath.chapter_06.posts,
  ravelling_wrath.chapter_07.posts,
  ravelling_wrath.chapter_08.posts,
  ravelling_wrath.chapter_09.posts,
  ravelling_wrath.chapter_10.posts,
  ravelling_wrath.chapter_11.posts,
  ravelling_wrath.chapter_12.posts,
  ravelling_wrath.chapter_13.posts,
  ravelling_wrath.chapter_14.posts,
  ravelling_wrath.chapter_15.posts,
  ravelling_wrath.chapter_16.posts,
  ravelling_wrath.chapter_17.posts,
  ravelling_wrath.chapter_18.posts,
  ravelling_wrath.chapter_19.posts,
  ravelling_wrath.chapter_20.posts,
])

for post in posts:
  post["contents"] = re.sub(r"\?{4,}", lambda match: "<mark>"+match.group(0)+"</mark>", post["contents"])
