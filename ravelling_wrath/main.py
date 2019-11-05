#!/usr//python3
# -*- coding: utf-8 -*-

import re

from post_contents_utils import *

import ravelling_wrath.chapter_01
import ravelling_wrath.chapter_02
import ravelling_wrath.chapter_03
import ravelling_wrath.chapter_04
import ravelling_wrath.chapter_05
import ravelling_wrath.chapter_06
import ravelling_wrath.chapter_07
import ravelling_wrath.chapter_08
import ravelling_wrath.chapter_09
import ravelling_wrath.chapter_10
import ravelling_wrath.chapter_11
import ravelling_wrath.chapter_12
import ravelling_wrath.chapter_13
import ravelling_wrath.chapter_14
import ravelling_wrath.chapter_15
import ravelling_wrath.chapter_16
import ravelling_wrath.chapter_17
import ravelling_wrath.chapter_18
import ravelling_wrath.chapter_19
import ravelling_wrath.chapter_20
import ravelling_wrath.chapter_21
import ravelling_wrath.definitions

# https://programmers.stackexchange.com/questions/254279/why-doesnt-python-have-a-flatten-function-for-lists
def flatten(l):
  return [x for y in l for x in y]

chapters = flatten([
  ravelling_wrath.chapter_01.posts,
  ravelling_wrath.chapter_02.posts,
  ravelling_wrath.chapter_03.posts,
  ravelling_wrath.chapter_04.posts,
  ravelling_wrath.chapter_05.posts,
  ravelling_wrath.chapter_06.posts,
  ravelling_wrath.chapter_07.posts,
  ravelling_wrath.chapter_08.posts,
  ravelling_wrath.chapter_09.posts,
  ravelling_wrath.chapter_10.posts,
  ravelling_wrath.chapter_11.posts,
  ravelling_wrath.chapter_12.posts,
  ravelling_wrath.chapter_13.posts,
  ravelling_wrath.chapter_14.posts,
  ravelling_wrath.chapter_15.posts,
  ravelling_wrath.chapter_16.posts,
  ravelling_wrath.chapter_17.posts,
  ravelling_wrath.chapter_18.posts,
  ravelling_wrath.chapter_19.posts,
  ravelling_wrath.chapter_20.posts,
  ravelling_wrath.chapter_21.posts,
])

for index, chapter in enumerate (chapters):
  chapter ["chapter_number"] = index + 1

def chapter_to_post (chapter):
  post = chapter.copy()
  warnings = post.get ("content_warnings", None)
  post ["contents"] = f'''<h2>Chapter {post ["chapter_number"]}: {post ["chapter_title"]}</h2>

  '''+ ("" if warnings is None else content_warning_header ("<p>Content warnings for this chapter:</p>" + warnings)) + post ["contents"]
  return post


posts = [chapter_to_post (chapter) for chapter in chapters]

completed_chapters = 0
for post in posts:
  post["contents"] = re.sub(r"\?{4,}", lambda match: "<mark>"+match.group(0)+"</mark>", post["contents"])
  if "don't deploy" not in post:
    completed_chapters += 1
    
blurb = f"A pair of teenagers get caught up in a conflict between the gods. ({completed_chapters} out of {len (chapters)} chapters completed so far.)"

for post in posts:
  post ["blurb"] = blurb

def contents_link (link, name):
  return '<div class="table_of_contents_chapter"><a class="chapter_link" href="' + link +'">' + name +'</a> [<a href="' + link +'''/discussion">author's notes</a>]</div>'''
  
posts [0] ["contents"] = ('''
<h2>Table of Contents</h2>


'''
+contents_link("/ravelling-wrath", "Chapter 1: Blood Child")
+ "".join (contents_link (
  f"/ravelling-wrath/{post ['chapter_number']}",
  f"Chapter {post ['chapter_number']}: {post ['chapter_title']}"
  ) for post in posts [1:] if "don't deploy" not in post)+'''
<div class="table_of_contents_remaining">To be continued...</div>

Many thanks to <a href="http://www.sarahfensore.com/">Sarah Fensore</a>, who I've talked out my story plans with since the beginning, and who continues to help me edit the individual chapters.
  
  <bigbreak>
  
Content warnings for Ravelling Wrath as a whole:
'''+ content_warning_header ('''<p>Ravelling Wrath is a fantasy adventure where the characters face deadly dangers. It also goes deep into their emotional struggles, including issues of abuse, sexual assault, self-harm, and depression. (Or, it will. Not all of those issues are in the chapters I've completed so far.) It also touches on heterosexism and classism.</p>

<p>Each chapter also has a list of content warnings for that chapter specifically.</p>''')+'''

<bigbreak>

<p>(Eli's note: this story is supposed to have more pictures in it, but I haven't been in good shape for drawing. Since I'm not sure when I <em>will</em> be in good shape again, I'm posting it anyway. I've included the one sketch I managed to do last time I was up to it.)</p>

<bigbreak>''' + posts [0] ["contents"])


