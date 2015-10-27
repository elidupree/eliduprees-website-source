#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division


import sys
import gimp_stuff
import voldemorts_children
import comics

def do_page(num):
  voldemorts_children.convert_vc_page(comics.comics_pages["voldemorts_children"][num])

if len(sys.argv) > 2:
  for i in range(int(sys.argv[1]), int(sys.argv[2])+1):
    do_page(i)
else:
  do_page(int(sys.argv[1]))
