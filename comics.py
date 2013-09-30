#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import html_pages
import bars
import utils


def add_comics_page(page_dict):
  utils.checked_insert(page_dict,
    'comics.html',
    html_pages.make_page(
      "Comics ⊂ Eli Dupree's website",
      '',
      '<body><a class="skip" href="#content">Skip to content</a>'+bars.bars_wrap({"comics":True}, '<main></main>')+'</body>'
    )
  )
