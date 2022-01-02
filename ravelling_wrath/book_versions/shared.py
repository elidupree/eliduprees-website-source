#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import os.path
import sys
import re
import shutil
from enum import Enum, auto

from num2words import num2words

import blog_server_shared
import post_contents_utils
import utils
import exmxaxixl

import ravelling_wrath.main
import ravelling_wrath.definitions

class BookType(Enum):
  PRINT = auto()
  LARGE_PRINT = auto()
  EPUB = auto()

  def is_print(self):
    return (self is BookType.PRINT or self is BookType.LARGE_PRINT)


def replace_media_path(match, rav_media_paths):
  full_path = match.group(1)
  relevant_path = os.path.basename(full_path)
  if rav_media_paths.get(relevant_path, full_path) != full_path:
    raise RuntimeError(f"multiple media named {relevant_path}")
  rav_media_paths[relevant_path] = full_path
  return relevant_path

def replace_media_paths(contents, rav_media_paths):
  return re.sub(r"/media/(.*?)\?rr", lambda match: replace_media_path(match, rav_media_paths), contents)
  
def copyright_page(book_type):
  if book_type.is_print():
    axdxrxexsxs = f"RavellingWrath{exmxaxixl.atdomain}"
  else:
    axdxrxexsxs = f"ravelling.wrath{exmxaxixl.atdomain}"
  return f'''
<div class="copyright-page">
<img class="rav-section-break watchful-eye" alt="" src="/media/ravelling-wrath/symbols/watchful-eye-section-break.png?rr" />
<p>
Ravelling Wrath © 2022 by Eli Dupree is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit: <a href="http://creativecommons.org/licenses/by-sa/4.0/">http://creativecommons.org/licenses/by-sa/4.0/</a>
</p>

<p>
Visit the author's website at: <a href="https://www.elidupree.com/">https://www.elidupree.com/</a>
</p>

<p>
For all inquires, contact: {axdxrxexsxs}
</p>

<p>
Illustrations and cover design by Sarah Fensore and Eli Dupree. To see more of Sarah Fensore's artwork, visit: <a href="http://www.sarahfensore.com/">http://www.sarahfensore.com/</a>
</p>

<table class="isbn-grid">
<tr><td>ISBN:</td><td>TODO (paperback)</td></tr>
<tr><td>ISBN:</td><td>TODO (hardcover)</td></tr>
<tr><td>ISBN:</td><td>TODO (large print)</td></tr>
<tr><td>ISBN:</td><td>TODO (ebook)</td></tr>
</table>

<p>
Library of Congress Control Number: TODO
</p>

<p>
This is a work of fiction. All names, characters, and incidents portrayed in this story are fictitious. No identification with actual persons (living or deceased), places, or events is intended or should be inferred.
</p>

<p>
This book is typeset using libre fonts, all of which are licensed under the SIL Open Font License. Specific fonts used are:
</p>

<table class="font-grid">
<tr><td>Front cover:</td><td>Alegreya Sans SC</td></tr>
<tr><td>Titles, running heads:</td><td>Alegreya SC</td></tr>
<tr><td>Main text:</td><td>Kadwa</td></tr>
<tr><td>Narration by Yali:</td><td>Kreon</td></tr>
<tr><td>This page:</td><td>Lexend</td></tr>
</table>

<img class="rav-section-break burning-heart" alt="" src="/media/ravelling-wrath/symbols/burning-heart-section-break.png?rr" />
</div>
'''
   

def chapter_html (chapter, book_type, rav_media_paths):
  ravelling_wrath.main.replace_section_breaks(chapter, "/media/ravelling-wrath/symbols")
  contents = post_contents_utils.auto_paragraphs (chapter ["contents"])
  #contents, _, _ = blog_server_shared.postprocess_post_string (contents, None, None, False, False)
  contents = ravelling_wrath.main.replace_all_emoji(contents, "/media/vendor/ravelling-wrath/emoji/black")
  
  if book_type.is_print():
    contents = re.sub("<not_print>.+?</not_print>", "", contents)
    contents = re.sub("</?print_only>", "", contents)
  else:
    contents = re.sub("<print_only>.+?</print_only>", "", contents)
    contents = re.sub("</?not_print>", "", contents)
    
  contents = replace_media_paths(contents, rav_media_paths)
  
  symbols = chapter["symbols"]
  running_symbol_filename = f'{symbols}-small.png'
  if symbols == "nonaligned":
    running_symbol_element = ''
  else:
    running_symbol_element = f'<img class="runningsymbols {symbols}" src="{running_symbol_filename}" alt="" />'
  
  rav_media_paths[running_symbol_filename] = running_symbol_filename
  
  contents = f'''
  <div class="chapter chapter_{chapter ["chapter_number"]} {chapter.get("post_class", "")}">
  <h2>Chapter {num2words(chapter ["chapter_number"]).capitalize()}</h2>
  <div class="chapter-title">{chapter ["chapter_title"]}</div>
  
  <div class="runningleft">
    {running_symbol_element}
    Ravelling Wrath
    {running_symbol_element}
  </div>
  <div class="runningright">
    {running_symbol_element}
    Chapter {num2words(chapter ["chapter_number"]).capitalize()}: {chapter ["chapter_title"]}
    {running_symbol_element}
  </div>
  
  
  {contents}</div>'''
  return contents


def generate_html_and_linked_media_files(build_path, *, book_type, specific_chapter = None):
  os.makedirs (build_path, exist_ok=True)
  rav_media_paths = {}
  chapters = ravelling_wrath.main.chapters
  if specific_chapter is not None:
    chapters = [chapters[specific_chapter]]
  chapters = [
    chapter_html (chapter, book_type, rav_media_paths) for chapter in chapters
  ]

  fonts_css = ravelling_wrath.definitions.fonts_css("", mode="book")

  for match in re.finditer(r"""url\(['"](.+?.ttf)""", fonts_css):
    rav_media_paths[match.group(1)] = "/media/fonts/"+match.group(1)

  with open("./ravelling_wrath/book_versions/shared.css") as shared_css, open("./ravelling_wrath/book_versions/print.css") as print_css, open("./ravelling_wrath/book_versions/ebook.css") as ebook_css:
    css_string = shared_css.read() + (print_css.read() if book_type.is_print() else ebook_css.read()) + fonts_css
  css_string = replace_media_paths(css_string, rav_media_paths)



  def wrap(html):
   return '''<!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="utf-8" />
      <title>Ravelling Wrath</title>
      <link rel="stylesheet" href="style.css"/>
    </head>
    <body>
  '''+html+'''
    </body>
  </html>'''

  full_html = wrap(replace_media_paths(copyright_page(book_type), rav_media_paths) + "".join (chapters))


  with open (os.path.join (build_path, "ravelling_wrath.html"), "w") as file:
    file.write (full_html)
    
  with open(os.path.join (build_path, "style.css"), "w") as file:
    file.write (css_string)
  
  #print(rav_media_paths)
  media_dir = "./media/"
  media_subdirs = os.listdir(media_dir)
  for media_subdir in media_subdirs:
    media_subdir_fullpath = os.path.join(media_dir, media_subdir)
    for root, dirs, files in os.walk(media_subdir_fullpath):
      for media_filename in files:
        source = os.path.join(root, media_filename)
        if media_filename in rav_media_paths:
          if ("color" in rav_media_paths[media_filename]) == ("color" in root):
            destination = os.path.join(build_path, media_filename)
            os.makedirs (os.path.dirname(destination), exist_ok = True)
            shutil.copy(source, destination)
    