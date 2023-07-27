#!/usr//python3
# -*- coding: utf-8 -*-

import re
import os
import os.path
from num2words import num2words


from post_contents_utils import *

import tftmuf.chapter_01
import tftmuf.definitions

# https://programmers.stackexchange.com/questions/254279/why-doesnt-python-have-a-flatten-function-for-lists
def flatten(l):
  return [x for y in l for x in y]

chapters = flatten([
  tftmuf.chapter_01.posts,
])

# quick hack to render the other chapters
for name in os.listdir("tftmuf"):
  m = re.match(r"^chapter_(.*)\.py$", name)
  if m and name != "chapter_01.py":
    with open(os.path.join("tftmuf", name), encoding="utf-8") as file:
      text = file.read().strip()
      chapter_title = m.group(1)
      chapter_lines = []
      def finish_chapter(new_title):
        global chapter_title, chapter_lines
        
        if chapter_lines:
          chapters.append ({
            "title": f"The Future They Made Us Forget, chapter {len(chapters)+1}",
            "auto_paragraphs": True,
            "head": tftmuf.definitions.head,
            "chapter_title": chapter_title,
            "contents": "\n".join(chapter_lines)
          })
        
        chapter_title = new_title
        chapter_lines = []
      lines = text.split("\n")
      for line in lines:
        c = re.match(r"\[Chapter (?:title|break): (.*)\]$", line)
        if c:
          finish_chapter(c.group(1))
        else:
          chapter_lines.append(line)
      
      finish_chapter(None)
      

for index, chapter in enumerate (chapters):
  chapter ["chapter_number"] = index + 1
    
  chapter ["contents"] = auto_paragraphs (chapter ["contents"])
  chapter ["contents"] = auto_smart_quotes (chapter ["contents"])
  
  

def chapter_to_post (chapter):
  post = chapter.copy()
  warnings = post.get ("content_warnings", None)

  post ["contents"] = f'''<h2>Chapter {num2words(post ["chapter_number"]).capitalize()}: {post ["chapter_title"]}</h2>

  '''+ ("" if warnings is None else content_warning_header ("<p>Content warnings for this chapter:</p>" + warnings)) + post ["contents"]
  return post


posts = [chapter_to_post (chapter) for chapter in chapters]



status_description ='''
<div class="novel-current-status">

Current status of this novel:

This is a web serial! I post new chapters every [whenever I feel like it].

</div>
'''



completed_chapters = 0
page_number = 0

for post in posts:
  post["contents"] = re.sub(r"\?{4,}", lambda match: "<mark>"+match.group(0)+"</mark>", post["contents"])
    
  if "don't deploy" not in post:
    completed_chapters += 1
    
short_blurb = "?????."
long_blurb = '''<p>?????</p>'''

for post in posts:
  post ["blurb"] = short_blurb

def contents_link (link, name):
  return '<div class="table_of_contents_chapter"><a class="chapter_link" href="' + link +'">' + name +'</a> [<a href="' + link +'''/discussion">author's notes</a>]</div>'''
  
last_published_chapter = posts [completed_chapters - 1]
last_published_chapter ["contents"] = status_description +'''

<bigbreak>''' + last_published_chapter ["contents"]
  
posts [0] ["contents"] = ('''
<h2>Table of Contents</h2>
<div class="table_of_contents">

'''
+contents_link("/the-future-they-made-us-forget", "Chapter 1: The ?????")
+ "".join (contents_link (
  f"/the-future-they-made-us-forget/{post ['chapter_number']}",
  f"Chapter {post ['chapter_number']}: {post ['chapter_title']}"
  ) for post in posts [1:] if "don't deploy" not in post)+'''
<div class="table_of_contents_remaining">To be continued...</div>
</div>

<bigbreak>

'''+ status_description +'''
  
  <bigbreak>
  
  <div class="main_content_warnings">
Content warnings for <cite>The Future They Made Us Forget</cite> as a whole:
'''+ content_warning_header ('''<p>?????</p>

<p>Each chapter also has a list of content warnings for that chapter specifically.</p>''')+'''

</div>

<bigbreak>''' + posts [0] ["contents"])

