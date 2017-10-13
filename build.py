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
import time

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
      source = os.path.join(media_dir, media_subdir, media_filename)
      destination = os.path.join(build_dir, "media", media_filename)
      if os.path.isdir (source):
        shutil.copytree(source, destination)
      else:
        shutil.copy(source, destination)
  shutil.copy(
    os.path.join(build_dir, "media/favicon.ico"),
    os.path.join(build_dir, "favicon.ico"))
  shutil.copytree(
    os.path.join("./media/hexy"),
    os.path.join(build_dir, "hexy"))
  page_dict = {}

  utils.checked_insert(page_dict, css.domain_relative_url(), css.build())
  utils.checked_insert(page_dict, "/robots.txt", '''''')

  bars.add_home_page(page_dict)
  blog.add_pages(page_dict)
  javascript.add_files(page_dict)
  category_pages.add_category_pages(page_dict)
  game_pages.add_game_pages(page_dict)
  comics.add_comic_pages(page_dict)
  rss.add_feed(page_dict)
  redirects.add_redirects(page_dict)
  
  reached_pages = {}
  orphaned_pages = {}
  orphaned_pages_display = [
    
    ("/stories/the-console-of-the-time-cops", "The Console of the Time Cops, a short story"),
    ("/2013-04-29-lasercake-talk-script", "The script for my 2013-04-29 Lasercake talk"),
    
    ("/some-thoughts-about-undyne-the-character-from-the-game-undertale", "Some thoughts about Undyne, the character from the game Undertale"),
    ("/the-morality-of-legend-of-korra", "A post about the morality of Legend of Korra"),
  ]
  def reach_page (path):
    if path in page_dict and path not in reached_pages:
      reached_pages [path] = True
      for destination in re.finditer ('href="(.+?)"', page_dict [path]):
        reach_page (destination.group (1) + ".html")
  reach_page ("/index.html")
  for (path, _) in orphaned_pages_display:
    reach_page (path+".html")
  def find_orphaned_pages ():
    for path,contents in page_dict.items():
      if path.endswith (".html") and path not in reached_pages:
        reach_page (path)
        orphaned_pages [path [0:-5]] = True
        orphaned_pages_display.append ((path [0:-5], path [0:-5]))
  find_orphaned_pages ()
  print ("Orphaned pages:")
  print (orphaned_pages)
  category_pages.add_secrets (page_dict, orphaned_pages_display)
  
  for path,contents in page_dict.items():
    if False and path.endswith(".html"):
      from py_w3c.validators.html.validator import HTMLValidator
      vld = HTMLValidator()
      vld.validate_fragment(contents)
      print(vld.errors)
      print(vld.warnings)
    assert(path[0] == '/')
    if path .endswith (".301") and contents [0] == '/' and contents != "/" and "." not in contents and contents + ".html" not in page_dict:
      print (path + " redirects to nonexistent " + contents)
    buildpath = build_dir + path
    ensure_dir(os.path.dirname(buildpath))
    with open(buildpath, "w", encoding='utf-8') as f:
      f.write(contents)
    if "--no-jshint" not in sys.argv and path.endswith (".js"):
      print('jshinting ' +buildpath)
      subprocess.run(['jshint', buildpath])
    if "--accessibility" in sys.argv and path.endswith (".html"):
      subprocess.run(['pa11y', "--ignore", 'warning;notice', "file://" + os.path.abspath (buildpath)])

  # TODO real cmdline processing
  if '--no-idupree-websitepy' not in sys.argv:
    import idupree_websitepy.build
    import idupree_websitepy.tests

    config = idupree_websitepy.build.Config(
      site_source_dir = build_dir,
      build_output_dir = './build/idupree_websitepy_output/',
      doindexfrom = ['/', "/harry-potter-and-the-methods-of-rationality-commentary", "/the-morality-of-legend-of-korra", "/some-thoughts-about-undyne-the-character-from-the-game-undertale","/stories/the-console-of-the-time-cops","/2013-04-29-lasercake-talk-script", ],
      butdontindexfrom = [],
      error_on_missing_resource = False,
      error_on_broken_internal_link = False,
      canonical_scheme_and_domain = utils.canonical_scheme_and_domain,
      list_of_compilation_source_files = ['build.py'],
      published_as_is = (lambda path:
        bool(re.search(r'\.(txt|asc|pdf|rss|atom|zip|tar\.(gz|bz2|xz)|appcache|cpp|hs|js\.mem)$|'+
          r'^/favicon.ico$|^/atom\.xml$|^/media/affirmative-consent-poster\.png$|^/media/colby_comic.*\.png$|^/media/interval_optimized_1_hour.ogg$',
          path))),
      test_host = 'localhost',
      test_port = 84,
      test_host_header = 'www.elidupree.com',
      test_canonical_origin = utils.canonical_scheme_and_domain,
      test_status_codes = {
        '/': 200,
        "/blog": 200,
        "/comics": 200,
        "/stories": 200,
        "/games": 200,
        "/voldemorts-children": 200,
        "/voldemorts-children/archive": 200,
        "/voldemorts-children/5": 200,
        "/games/green-caves": 200,
        "/blog/tags/gender": 200,
        "/blog/page/3": 200,
        "/blog/page/3/chronological": 200,
        "/stories/not-what-i-am": 200,
        "/stories/not-what-i-am/discussion": 200,
        "/games/pac-asteroids": 200,
        '/blog/happy-tau-day': 200,
        '/hexy': 200,
        "/main/blog": 301,
        "/main/posts/1-the-epic-first-post": 301,
        "/EoHS": 301,
        '/sdhofhnkfjdsdsf': 404,
        "/blog/gibberish-gibberish": 404,
        "/404": 404,
      }
      )
    idupree_websitepy.build.build(config)
    subprocess.check_call(['/usr/bin/sudo', '/bin/systemctl',
      'reload-or-try-restart', 'nginx.service'])
    time.sleep(1)
    if '--no-idupree-websitepy-tests' not in sys.argv:
      # tests not working?
      # sudo systemctl restart validatornu.service
      # and wait 3 minutes
      idupree_websitepy.tests.test(config)
      if "--deploy" in sys.argv:
        with open(build_dir + "/deploy_ready", 'w') as deploy_file:
          deploy_file.write ("yes")

if __name__ == '__main__':
  main()


