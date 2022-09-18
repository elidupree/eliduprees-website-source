#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

import datetime
import html
import os
import re

import utils
import exmxaxixl
import blog
import blog_posts
import comics

def atom_time(dt):
  return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

def add_feed(page_dict):
  author = '''<author>
    <name>Eli Dupree</name>
    <'''+'e'+'m'+'a'+'i'+'l'+'>'+exmxaxixl.axdxrxexsxs+'</'+'e'+'m'+'a'+'i'+'l'+'''>
    <uri>'''+utils.canonical_scheme_and_domain+'''/</uri>
  </author>'''
  
  entries = []  
  for post in reversed ([post for post in blog.current_blog_page if "username" not in post]):
    if "comic_id" not in post:
      link = blog.post_permalink(post)
    else:
      link = comics.page_url(post)
    title = post ["title"]
    (body, head) = blog.stream_entry (post)
    post_string = head + body
    metadata = blog.post_metadata(post)
    # make internal links work in the feed
    post_string = re.sub(r'( (?:href|src)=")/', lambda match: match.group(1)+utils.canonical_scheme_and_domain+'/', post_string)
    
    entries.append('''
    <entry>
      <id>'''+utils.canonical_scheme_and_domain+link+'''</id>
      <title type="html">'''+html.escape(title)+'''</title>
      <published>'''+atom_time(metadata["date_posted"])+'''</published>      
      <updated>'''+atom_time(metadata["date_modified"])+'''</updated>
      '''+author+'''
      <link rel="alternate" href="'''+utils.canonical_scheme_and_domain+link+'''" />
      <content type="html">'''+html.escape(post_string)+'''</content>
    </entry>
    ''')
  
  utils.checked_insert(page_dict,
    '/atom.xml',
    '''<?xml version="1.0" encoding="utf-8"?>

<feed xmlns="http://www.w3.org/2005/Atom">
  <id>'''+utils.canonical_scheme_and_domain+'''/</id>
  <icon>'''+utils.canonical_scheme_and_domain +'''/site-logo.png</icon>
  <title>Eli Dupree's website</title>
  <updated>'''+atom_time(datetime.datetime.utcnow())+'''</updated>
  '''+author+'''
  <link rel="self" href="/atom.xml" />
  '''+''.join(entries)+'''
</feed>'''
  )

