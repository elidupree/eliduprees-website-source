#!/usr/bin/python3
# -*- coding: utf-8 -*-

from git import *
import git
import os
import time
import datetime
from datetime import date
import re
import html

repo = Repo (os.getcwd())

commit = repo.commit ("master")


def strip_tags(string):
  return re.sub(r"<.+?>","",string)

def word_count (string):
  return len(re. findall (r"\w[\w']*", html.unescape (strip_tags (string))))

current_date = None
previous_words = None
previous_drawn_date = None
while True:
  commit_date = date.fromtimestamp (commit.committed_date - 5*60*60).toordinal ()
  
  commit_words = 0
  for chapter_number in range (1, 100):
    try: 
      chapter = repo.git.show ("{}:ravelling_wrath/chapter_{:02}.py".format (commit.hexsha, chapter_number))
      contents = re.search (r"contents.*?'''(.*)'''", chapter, re.DOTALL).group (1)
      commit_words = commit_words + word_count (contents)
    except git.exc.GitCommandError:
      completed = (chapter_number == 1)
      break
  
  if completed or (commit_date != current_date):
    if previous_words is not None:
      change = previous_words - commit_words
      if change != 0:
        #print (current_date + ": " + str (previous_words - commit_words))
        marks = (change + 25)//50
        if previous_drawn_date is not None:
          date_change = previous_drawn_date - current_date
          if date_change < 7:
            for ordinal in range (previous_drawn_date - 1, current_date, -1):
              print (date.fromordinal (ordinal).strftime("%b %d, %Y") + ":    0")
          else:
            print ("\n...\n")
        print (date.fromordinal (current_date).strftime("%b %d, %Y") + ": {:4} ".format (change) + ("#"*marks))
        previous_drawn_date = current_date
    
    current_date = commit_date
    previous_words = commit_words
      
  if completed:
    break
    
  commit = commit.parents[0]

