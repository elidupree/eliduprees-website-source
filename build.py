#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division


import os
import os.path
import sys
import shutil
import locale

# always UTF-8, even on windows
# the exec line seemingly didn't work, so:
# doing it in the batch script instead
#if locale.getpreferredencoding() != 'UTF-8':
#  if 'PYTHONIOENCODING' in os.environ:
#    # make sure any bugs here don't turn into infinite loops
#    sys.stderr.write("encoding issue\n")
#    exit(1)
#  os.environ['PYTHONIOENCODING'] = 'UTF-8'
#  os.execvpe(sys.argv[0], sys.argv, os.environ)
# We gave up on getting even this to work:
#if locale.getpreferredencoding() != 'UTF-8':
#  sys.stderr.write(
#    "encoding needs to be UTF-8\n" +
#    "set PYTHONIOENCODING=UTF-8 environment variable to fix it\n" +
#    "Currently: locale.getpreferredencoding() is " + str(locale.getpreferredencoding()) + "\n" +
#    "and PYTHONIOENCODING is " + str(os.environ.get('PYTHONIOENCODING')))
#  exit(1)

# for now, change to the directory of this script
# so that the relative paths in the website source
# are relative to this script

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import css
import rss
import javascript
import html_pages
import top_bar
import bars
import utils
import blog
import category_pages
import game_pages
import comics
import redirects

def ensure_dir(d):
  if not os.path.exists(d):
    os.makedirs(d)

def putfile(path, contents):
  buildpath = "./build/"+path
  ensure_dir(os.path.dirname(buildpath))
  f = open(buildpath, "w", encoding='utf-8')
  f.write(contents)


def main():
  ensure_dir("./build/media")
  media_dir = "./media/"
  media_subdirs = os.listdir(media_dir)
  for media_subdir in media_subdirs:
    media_filenames = os.listdir(os.path.join(media_dir, media_subdir))
    for media_filename in media_filenames:
      shutil.copy(
        os.path.join(media_dir, media_subdir, media_filename),
        "./build/media/"+media_filename)
  shutil.copy("./build/media/favicon.ico", "./build/favicon.ico")
  page_dict = {}

  utils.checked_insert(page_dict, css.filename(), css.build())

  # for test builds:
  utils.checked_insert(page_dict, "robots.txt", '''User-agent: *
Disallow: /''')

  bars.add_home_page(page_dict)
  blog.add_pages(page_dict)
  javascript.add_files(page_dict)
  category_pages.add_category_pages(page_dict)
  game_pages.add_game_pages(page_dict)
  comics.add_comic_pages(page_dict)
  rss.add_feed(page_dict)
  redirects.add_redirects(page_dict)

  for path,contents in page_dict.items():
    if False and path.endswith(".html"):
      from py_w3c.validators.html.validator import HTMLValidator
      vld = HTMLValidator()
      vld.validate_fragment(contents)
      print(vld.errors)
      print(vld.warnings)
    putfile(path,contents)

if __name__ == '__main__':
  main()


