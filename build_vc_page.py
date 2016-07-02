#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division


import sys
import gimp_stuff
import comics

def convert_vc_page(page_dict):
  gimp_stuff.generate_vc_images(page_dict["xcf_base"], page_dict["list_index"])

def do_page(num):
  convert_vc_page(comics.comics_pages["voldemorts_children"][num])

if len(sys.argv) > 2:
  for i in range(int(sys.argv[1]), int(sys.argv[2])+1):
    do_page(i)
else:
  do_page(int(sys.argv[1]))
