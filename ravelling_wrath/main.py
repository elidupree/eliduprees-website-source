#!/usr//python3
# -*- coding: utf-8 -*-

import re
from num2words import num2words


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
  chapter ["contents"] = auto_paragraphs (chapter ["contents"])
  # Smart quotes cases:
  # Standard apostrophes:
  chapter ["contents"] = re.sub(r"\b'\b", "’", chapter ["contents"])
  
  def apply_quotes(match):
    # Single-quotes within standard quotes
    return re.sub(r"(?<!\w)'(?! )([^'\n]*?)(?<! )'(?!\w)", lambda match2: f"‘{match2.group(1)}’", match.group (1))
    
  # Standard quotes:
  chapter ["contents"] = re.sub(r'(?<![\w=])"(?![ >])([^"\n]*?)(?<![ =])"(?![\w>])', lambda match: f"“{apply_quotes(match)}”", chapter ["contents"])
  # Unmatched quotes indicating continued dialogue
  chapter ["contents"] = re.sub(r'(?<![\w=])"(?![ >])([^"\n]*?)(?=</p>)', lambda match: f"“{apply_quotes(match)}", chapter ["contents"])
  
  # Word-start apostrophes:
  chapter ["contents"] = re.sub(r"\B'\b", "’", chapter ["contents"])
  # Word-end apostrophes:
  chapter ["contents"] = re.sub(r"\b'\B", "’", chapter ["contents"])
  
  # Emoji:
  # We currently use twemoji (https://github.com/twitter/twemoji),
  # but may change this in the future.
  def replace_emoji(match):
    emoji = match.group(0)
    hex_string = hex(ord(emoji))[2:]
    return f'<img class="emoji" alt="{emoji}" src="/media/ravelling-wrath/emoji/{hex_string}.svg?rr" />'
  chapter ["contents"] = re.sub(r"😡|😂|❤|😝", replace_emoji, chapter ["contents"])
  

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

All twenty-one chapters have been written! I haven't posted them yet – there is still editing work left to do – but I can now commit to a <strong>regular schedule</strong>. I will post one chapter a week, on Wednesday evenings. By this schedule, the entire novel will be available on September 23, 2020!

Meanwhile, Sarah Fensore and I are hard at work on making illustrations! Most of them aren't complete yet, but I'm including our sketches in the story for now, and I'll replace them with the completed drawings as we complete them.

I'm also working on significant edits to the earlier chapters (which aren't <em>quite</em> up to my standards after everything I've learned by writing the rest). So the existing chapters may change unexpectedly. I know some of you may want to read (or reread) the story after it's no longer in flux, so I'll update this message with the current status as I make progress.

</div>
'''



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
  
last_published_chapter = posts [completed_chapters - 1]
last_published_chapter ["contents"] = status_description +'''

<bigbreak>''' + last_published_chapter ["contents"]
  
posts [0] ["contents"] = ('''
<h2>Table of Contents</h2>
<div class="table_of_contents">

'''
+contents_link("/ravelling-wrath", "Chapter 1: Blood Child")
+ "".join (contents_link (
  f"/ravelling-wrath/{post ['chapter_number']}",
  f"Chapter {post ['chapter_number']}: {post ['chapter_title']}"
  ) for post in posts [1:] if "don't deploy" not in post)+'''
<div class="table_of_contents_remaining">To be continued…</div>

Many thanks to <a href="http://www.sarahfensore.com/">Sarah Fensore</a>, who I've talked out my story plans with since the beginning, and who continues to help me edit the individual chapters.
</div>

<bigbreak>

'''+ status_description +'''
  
  <bigbreak>
  
  <div class="main_content_warnings">
Content warnings for Ravelling Wrath as a whole:
'''+ content_warning_header ('''<p>Ravelling Wrath is a fantasy adventure where the characters face deadly dangers. It also goes deep into their emotional struggles, including issues of abuse, sexual assault, self-harm, and depression. (Or, it will. Not all of those issues are in the chapters I've completed so far.) It also touches on heterosexism and classism.</p>

<p>Each chapter also has a list of content warnings for that chapter specifically.</p>''')+'''

</div>

<bigbreak>''' + posts [0] ["contents"])


# note: partly duplicated language from the chapter 12 content warnings
extra_posts = [
{
  "title":"Summary of Ravelling Wrath, chapter 12",
  "title_url_override": "12-summary",
  "auto_paragraphs": True,
  "contents":'''

The majority of <a href="/ravelling-wrath/12">Ravelling Wrath, chapter 12</a> is an explicit, detailed narration of an experience of depression, including anhedonia, dissociation, negative self-talk, and being coerced into obeying authority. From my personal experience with depression, I know that it's sometimes valuable to avoid exposure to content like this. Thus, I've prepared this summary, so that you can read the summary instead of the chapter if needed.

Skipping chapter 12 and reading this summary instead is an <strong>officially supported</strong> way of reading Ravelling Wrath.

Chapter 12 isn't the only chapter which contains details of depression, but it's the most severe one. I don't have summaries for the others, because they're less self-contained (they have occasional details of depression mixed in with other important story details that are harder to summarize).

<h2>The summary</h2>

As soon as Rinn enters the Stern God's layer, Rinn is severely depressed, and feels like Yali will be unreachable forever. It's not clear whether the Blood God is causing this. When Rinn listens for the Blood God, it doesn't have the same angry thoughts as usual, only gloom. Rinn doesn't want to get up, but soon, the Stern God also starts influencing Rinn's mind, which makes Rinn feel a sense of duty to get up and try to find Yali.

The Stern God's layer is a grid of white marble corridors. Each corridor is made for a specific Raveller, and has challenges for them. During the chapter, Rinn realizes that each path forces the intended walker to sacrifice the thing most important to them. The Blood Child's Path requires the walker to show deference to the guardian statues, thus sacrificing their pride. The Imminent's Path requires the walker to ignore distracting sensations, thus sacrificing their curiosity. The Alchemist's Path requires the walker to speak decisively, thus sacrificing their indecisiveness. Finally, the Farseer's Path requires the walker to walk along it without thinking about what will come next.

Rinn wouldn't normally obey the Stern God's rules. But, because of the depression and the Stern God's influence, Rinn obeys. As the chapter goes on, Rinn gets less and less alert, and starts thinking about trying to find "the Farseer" instead of "Yali".

When Rinn finally gets to Yali, Rinn hardly has any feelings about Yali at all. Alchemist is also there; Yali and Alchemist have been preparing for what's about to happen. As the chapter ends, Rinn "remembers" what to do, summons a Blood Blade, and stabs Yali with it.

''',
},

]

