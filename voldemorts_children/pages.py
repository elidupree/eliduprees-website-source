#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

import voldemorts_children.pages_01
import voldemorts_children.pages_02
import voldemorts_children.pages_03
import voldemorts_children.pages_04
import voldemorts_children.pages_05
import voldemorts_children.pages_06
import voldemorts_children.pages_07

# https://programmers.stackexchange.com/questions/254279/why-doesnt-python-have-a-flatten-function-for-lists
def flatten(l):
  return [x for y in l for x in y]

vc_pages = flatten([
  voldemorts_children.pages_01.pages,
  voldemorts_children.pages_02.pages,
  voldemorts_children.pages_03.pages,
  voldemorts_children.pages_04.pages,
  voldemorts_children.pages_05.pages,
  voldemorts_children.pages_06.pages,
  voldemorts_children.pages_07.pages,
])
