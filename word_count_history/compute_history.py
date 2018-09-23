#!/usr/bin/python3
# -*- coding: utf-8 -*-

from git import *
import git
import os
import time
import datetime
from datetime import date
import re

repo = Repo (os.getcwd())

commit = repo.commit ("master")



def word_count (string):
  return len(re. findall (r"\w[\w']*", string))

current_date = None
previous_words = None
while True:
  commit_date = date.fromtimestamp (commit.committed_date).to_ordinal ()
  
  commit_words = 0
  for chapter_number in range (1, 20):
    try: 
      chapter = repo.git.show ("{}:ravelling_wrath/chapter_{:02}.py".format (commit.hexsha, chapter_number))
      contents = re.search (r"contents.*?'''(.*)'''", chapter, re.DOTALL).group (1)
      commit_words = commit_words + word_count (contents)
    except git.exc.GitCommandError:
      completed = (chapter_number == 1)
      break
  
  if completed or (commit_date != current_date and commit_words != 0):
    if previous_words is not None:
      change = previous_words - commit_words
      #print (current_date + ": " + str (previous_words - commit_words))
      marks = (change + 25)//50
      date_change = current_date - commit_date
      if date_change < 5:
        for ordinal in range (current_date - 1, commit_date, -1):
          print (date.fromordinal (ordinal).strftime("%b %-d, %Y") + ": (0)"))
      else:
        print ("\n...\n")
      print (date.fromordinal (current_date).strftime("%b %-d, %Y") + ": " + ("#"*marks) + " (" + str (change) + ")")
      
    current_date = commit_date
    previous_words = commit_words
      
  if completed:
    break
    
  commit = commit.parents[0]

