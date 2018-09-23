#!/usr/bin/python3
# -*- coding: utf-8 -*-

from git import *
import os
import time

repo = Repo (os.getcwd())

commit = repo.commit ("master")

while True:
  commit_date = time.strftime ("%B %-d, %Y", time.gmtime (commit.committed_date))
  
  commit_words = 0
  for chapter_number in range (1, 20):
    print (repo.git.show ("{}:ravelling_wrath/chapter_{02}".format (commit.hexsha, chapter_number))
  
  
  if commit_date != current_date:
    if previous_words is not None:
      print (current_date + ": " + str (previous_words - commit_words))
    current_date = commit_date
    previous_words = commit_words
  break

