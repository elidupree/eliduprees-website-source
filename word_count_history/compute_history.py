#!/usr/bin/python3
# -*- coding: utf-8 -*-

from git import *
import os
import time
import re

repo = Repo (os.getcwd())

commit = repo.commit ("master")



def word_count (string):
  return len(re. findall (r"\w[\w']*", string))

while True:
  commit_date = time.strftime ("%B %-d, %Y", time.gmtime (commit.committed_date))
  
  commit_words = 0
  for chapter_number in range (1, 20):
    try: 
      chapter = repo.git.show ("{}:ravelling_wrath/chapter_{:02}.py".format (commit.hexsha, chapter_number)))
      contents = re.search (r"contents.*?'''(.*)"'''", chapter, re.DOTALL).group (1)
      commit_words = commit_words + word_count (contents)
    except git.exc.GetCommandError:
      completed = (chapter_number == 0)
      break
    
    
  
  if completed or commit_date != current_date:
    if previous_words is not None:
      print (current_date + ": " + str (previous_words - commit_words))
    current_date = commit_date
    previous_words = commit_words
    
  if completed:
    break

