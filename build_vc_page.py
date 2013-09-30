#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import sys
import gimp_stuff
import voldemorts_children

voldemorts_children.convert_vc_page(voldemorts_children.vc_pages[int(sys.argv[1])])

