#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

import datetime

def page (number, transcript, annotation = ""):
  return {
    "xcf_base": "thorough_p" + str (number),
    "force_date": datetime.date (2011, 1, 26),
    "transcript": transcript, "annotation": annotation}
    

pages = [
page (1,''''''),
page (2,''''''),

]
