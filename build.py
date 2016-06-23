#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division


import os
import os.path
import sys
import shutil
import subprocess
import locale
import re

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

import idupree_websitepy.build
import idupree_websitepy.tests

def ensure_dir(d):
  if not os.path.exists(d):
    os.makedirs(d)

def main():
  build_dir = "./build/initial"
  # clear old build products:
  if os.path.exists(build_dir):
    shutil.rmtree(build_dir)
  ensure_dir(os.path.join(build_dir, "media"))
  media_dir = "./media/"
  media_subdirs = os.listdir(media_dir)
  for media_subdir in media_subdirs:
    media_filenames = os.listdir(os.path.join(media_dir, media_subdir))
    for media_filename in media_filenames:
      shutil.copy(
        os.path.join(media_dir, media_subdir, media_filename),
        os.path.join(build_dir, "media", media_filename))
  shutil.copy(
    os.path.join(build_dir, "media/favicon.ico"),
    os.path.join(build_dir, "favicon.ico"))
  shutil.copytree(
    os.path.join("./media/hexy"),
    os.path.join(build_dir, "hexy"))
  page_dict = {}

  utils.checked_insert(page_dict, css.domain_relative_url(), css.build())

  # for test builds:
  utils.checked_insert(page_dict, "/robots.txt", '''User-agent: *
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
    assert(path[0] == '/')
    if path .endswith (".301") and contents [0] == '/' and contents + ".html" not in page_dict:
      print (path + " redirects to nonexistent " + contents)
    buildpath = build_dir + path
    ensure_dir(os.path.dirname(buildpath))
    with open(buildpath, "w", encoding='utf-8') as f:
      f.write(contents)
    if "--no-jshint" not in sys.argv and path.endswith (".js"):
      print('jshinting ' +buildpath)
      subprocess.run(['jshint', buildpath])

  # TODO real cmdline processing
  if '--no-idupree-websitepy' not in sys.argv:
    config = idupree_websitepy.build.Config(
      site_source_dir = build_dir,
      build_output_dir = './build/idupree_websitepy_output/',
      doindexfrom = ['/'],
      butdontindexfrom = [],
      error_on_missing_resource = False,
      error_on_broken_internal_link = False,
      canonical_scheme_and_domain = utils.canonical_scheme_and_domain,
      list_of_compilation_source_files = ['build.py'],
      published_as_is = (lambda path:
        bool(re.search(r'\.(txt|asc|pdf|rss|atom|zip|tar\.(gz|bz2|xz)|appcache|cpp|hs|js\.mem)$|'+
          r'^/favicon.ico$|/atom\.xml$|',
          path))),
      test_host = 'localhost',
      test_port = 84,
      test_host_header = 'www.elidupree.com',
      test_canonical_origin = utils.canonical_scheme_and_domain,
      test_status_codes = {
        '/': 200,
        '/blog/happy-tau-day': 200,
        '/hexy': 200,
        '/sdhofhnkfjdsdsf': 404,
      }
      )
    idupree_websitepy.build.build(config)
    subprocess.check_call(['/usr/bin/sudo', '/bin/systemctl',
      'reload-or-try-restart', 'nginx.service'])
    idupree_websitepy.tests.test(config)

if __name__ == '__main__':
  main()


