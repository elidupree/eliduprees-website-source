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
  LARGE_PRINT_1 = auto()
  LARGE_PRINT_2 = auto()
  EPUB = auto()
  COMPRESSED_PDF = auto()

  def is_print(self):
    return (self in [BookType.PRINT, BookType.LARGE_PRINT_1, BookType.LARGE_PRINT_2, BookType.COMPRESSED_PDF])
  def is_large_print(self):
    return (self in [BookType.LARGE_PRINT_1, BookType.LARGE_PRINT_2])


def replace_media_path(match, rav_media_paths):
  full_path = match.group(1)
  relevant_path = os.path.basename(full_path)
  if rav_media_paths.get(relevant_path, full_path) != full_path:
    raise RuntimeError(f"multiple media named {relevant_path}")
  rav_media_paths[relevant_path] = full_path
  return relevant_path

def replace_media_paths(contents, rav_media_paths):
  return re.sub(r"/media/(.*?)\?rr", lambda match: replace_media_path(match, rav_media_paths), contents)
  
def title_page(book_type):
  volume = ''
  if book_type is BookType.LARGE_PRINT_1:
    volume = '<div class="volume">Large print volume 1</div>'
  if book_type is BookType.LARGE_PRINT_2:
    volume = '<div class="volume">Large print volume 2</div>'
  
  return f'''
<div class="title-page">
<h1>Ravelling Wrath</h1>
{volume}
<div class="author">Eli Dupree</div>
<div class="illustrator">Illustrated by Sarah Fensore and Eli Dupree</div>

</div>
'''
  
def copyright_page(book_type):
  if book_type.is_print():
    axdxrxexsxs = f"RavellingWrath{exmxaxixl.atdomain}"
  else:
    axdxrxexsxs = f"ravelling.wrath{exmxaxixl.atdomain}"
  
  fonts = [
    ("Front cover", "Alegreya Sans SC"),
  ]
  if book_type.is_large_print():
    fonts += [
      ("Titles", "Alegreya Sans"),
      ("Main text", "Lexend"),
    ]
  else:
    fonts += [
      ("Titles, running heads", "Alegreya SC"),
      ("Main text", "Kadwa"),
      ("Narration by Yali", "Kreon"),
      ("This page", "Lexend"),
    ]
  
  fonts = "\n".join(f"<tr><td>{purpose}:</td><td>{font}</td></tr>" for purpose, font in fonts)
    
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

<p class="before-font-grid">
This book is typeset using libre fonts, all of which are licensed under the SIL Open Font License. Specific fonts used are:
</p>

<table class="font-grid">
{fonts}
</table>

<img class="rav-section-break burning-heart" alt="" src="/media/ravelling-wrath/symbols/burning-heart-section-break.png?rr" />
</div>
'''

def table_of_contents(book_type, chapters):
  html_entries = [
    f'<a class="toc-row" href="#chapter_{chapter["chapter_number"]}_start"><span class="toc-chapter-number">{chapter["chapter_number"]}.</span><span class="toc-title">{chapter["chapter_title"]}</span><span class="toc-dots">.................................................................................................................................................</span><span class="toc-page-number" data-href="#chapter_{chapter["chapter_number"]}_start"></span></a>'
    for chapter in chapters
  ]

  return f'''
<div class="table-of-contents">
<div class="chapter-title">Contents</div>
<table>
{"".join(html_entries)}
</table>
</div>
'''

content_warning_notice = '''
<div class="content-warning-notice">
<h2>Content warnings for this novel</h2>

<p>
We believe that readers have a right to choose when and how they engage with sensitive topics. Thus, we provide this short summary of how this book addresses sensitive topics, with minimal spoilers:
</p>

<p>
<cite>Ravelling Wrath</cite> attempts to take an empowering approach to issues of trauma and abuse. Topics include child abuse, sexual assault, self-harm, and depression, but the story avoids narrating prolonged scenes of abuse "on-camera", and focuses on how the characters cope, form healthy relationships, and try to do better in the present. The two main characters face traumatic and life-threatening situations, but they survive and get a relatively happy ending.
</p>

<p>
More-detailed content warnings (with slightly more spoilers) are <a href="#content_warnings" class="crosslink">available on page </a>.
</p>
</div>
'''

content_warnings = f'''
<div id="content_warnings" class="content-warnings">

<div class="runningleft">
  Ravelling Wrath
</div>
<div class="runningright">
  Appendix: Content warnings
</div>
  
<h2>Appendix: Detailed content warnings</h2>

<h3>Things that are shown in detail, "on-camera"</h3>
<ul>
<li>Characters fight for their lives and get stabbed with swords. There are some graphic descriptions of physical injuries and death. (The two main characters don't die, though.)</li>
<li>A narrator has strange and unpleasant experiences in their brain due to supernatural forces.</li>
<li>A narrator has depressed thoughts, including dissociation, anhedonia, negative self-talk, and being coerced into obeying authority. The worst part of this is a single chapter, which can be skipped (see <a href="#chapter_12_summary_start" class="crosslink">"summary of chapter 12" on page </a>).</li>
<li>A narrator with PTSD copes with strong feelings, especially guilt and hatred.</li>
<li>A narrator copes with anger about another character being sexually assaulted.</li>
<li>A character engages in self-harm and makes suicidal statements.</li>
</ul>

<h3>Significant things that happen "off-camera"</h3>
<ul>
<li>Characters experience child abuse and neglect, including physical, verbal, and sexual abuse; an abusive "troubled teen" school; homelessness and survival sex work; and adults denying that the abuse happened. A few lines of verbally abusive dialogue are shown, but very few physical details of the abuse are shown. Some characters who have been abused deny how bad the abuse was, or make justifications for it.</li>
<li>Characters have to interact with the police, who are sometimes violent or corrupt.</li>
</ul>

<h3>Things that appear only briefly</h3>

<ul>
<li>Anti-gay attitudes</li>
<li>Animal abuse</li>
<li>Misogynistic thoughts</li>
</ul>


</div>

<div id="chapter_12_summary" class="chapter-12-summary">
<h2 id="chapter_12_summary_start">Summary of chapter 12</h2>

{post_contents_utils.auto_paragraphs(ravelling_wrath.main.chapter_12_summary('chapter 12'))}

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
  
  if book_type is BookType.COMPRESSED_PDF:
    contents = re.sub(r"(-left|-right).png", r"\1-lossy.png", contents)
  #if book_type is BookType.EPUB:
  #  contents = re.sub(r"(<|</)em", r"\1i", contents)
  
  contents = replace_media_paths(contents, rav_media_paths)
  
  title_class = 'chapter-title'
  if 'class="chapter-header"' in contents:
    title_class += ' before-header-image'
  
  symbols = chapter["symbols"]
  running_symbol_filename = f'{symbols}-small.png'
  if symbols == "nonaligned":
    running_symbol_element = ''
  else:
    running_symbol_element = f'<img class="runningsymbols {symbols}" src="{running_symbol_filename}" alt="" />'
  
  rav_media_paths[running_symbol_filename] = running_symbol_filename
  
  contents = f'''
  <div id="chapter_{chapter ["chapter_number"]}" class="chapter chapter_{chapter ["chapter_number"]} {chapter.get("post_class", "")}">
  <h2 id="chapter_{chapter ["chapter_number"]}_start" class="chapter-number">Chapter {num2words(chapter ["chapter_number"]).capitalize()}</h2>
  <div class="{title_class}">{chapter ["chapter_title"]}</div>
  
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
  if os.path.exists(build_path):
    for root, dirs, files in os.walk(build_path):
      for filename in files:
        os.remove(os.path.join(root, filename))
  os.makedirs (build_path, exist_ok=True)
  
  rav_media_paths = {}
  chapters = ravelling_wrath.main.chapters
  large_print_split_chapter = 12;
  if specific_chapter is not None:
    chapters = [chapters[specific_chapter]]
  elif book_type is BookType.LARGE_PRINT_1:
    chapters = chapters[:large_print_split_chapter]
  elif book_type is BookType.LARGE_PRINT_2:
    chapters = chapters[large_print_split_chapter:]
  
  chapters[0]["post_class"] = chapters[0].get("post_class", "") + " first-chapter-in-volume"
  if book_type is BookType.LARGE_PRINT_1:
    chapters[-1]["contents"] += '''
<div class="continued-in-volume-2">Continued in Volume 2…</div>'''
  
  toc_html = table_of_contents(book_type, chapters)
  chapters = [
    chapter_html (chapter, book_type, rav_media_paths) for chapter in chapters
  ]

  fonts_css = ravelling_wrath.definitions.fonts_css("", mode="book")

  for match in re.finditer(r"""url\(['"](.+?.ttf)""", fonts_css):
    rav_media_paths[match.group(1)] = "/media/fonts/"+match.group(1)

  css_pieces = [fonts_css]
  with open("./ravelling_wrath/book_versions/shared.css") as file:
    css_pieces.append(file.read())
  if book_type.is_print():
    with open("./ravelling_wrath/book_versions/print_shared.css") as file:
      css_pieces.append(file.read())
    if book_type.is_large_print():
      with open("./ravelling_wrath/book_versions/large_print.css") as file:
        css_pieces.append(file.read())
    else:
      with open("./ravelling_wrath/book_versions/regular_print.css") as file:
        css_pieces.append(file.read())
  else:
    with open("./ravelling_wrath/book_versions/ebook.css") as file:
      css_pieces.append(file.read())
  css_string = replace_media_paths("".join(css_pieces), rav_media_paths)



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
  
  copyright = replace_media_paths(copyright_page(book_type), rav_media_paths)
  
  html_parts = [
    title_page(book_type),
    copyright,
  ]
  
  if book_type.is_print():
    html_parts.append(toc_html)
  
  if book_type is not BookType.LARGE_PRINT_2:
    html_parts.append(content_warning_notice)
    
  html_parts += chapters
  
  if book_type is not BookType.LARGE_PRINT_2:
    html_parts.append(content_warnings)

  full_html = wrap("".join (html_parts))


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
    