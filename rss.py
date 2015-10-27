#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

import datetime
import cgi
import os
import utils
import exmxaxixl
import blog
import blog_posts
import comics
import voldemorts_children_pages

def atom_time(dt):
  return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

def add_feed(page_dict):
  author = '''<author>
    <name>Eli Dupree</name>
    <'''+'e'+'m'+'a'+'i'+'l'+'>'+exmxaxixl.axdxrxexsxs+'</'+'e'+'m'+'a'+'i'+'l'+'''>
    <uri>'''+utils.canonical_website_base+'''/</uri>
  </author>'''
  
  print ("TODO: include stories, non-VC comics in feed")
  entries = []
  blog_idx = len(blog_posts.posts["blog"]) - 1
  vc_idx = len(voldemorts_children_pages.vc_pages) - 1
  while len(entries) < 10:
    blog_post = blog_posts.posts["blog"][blog_idx]
    vc_post = voldemorts_children_pages.vc_pages[vc_idx]
    if blog.post_metadata(blog_post)["date_posted"] > blog.post_metadata(vc_post)["date_posted"]:
      post_dict = blog_post
      title = post_dict["title"]
      post_string = post_html(post_dict, True)
      link = blog.post_permalink(post_dict)
      # make internal links work in the feed
      post_string = re.sub(r'( href=")/', lambda match: match.group(1)+utils.canonical_website_base+'/', post_string)
      blog_idx = blog_idx - 1
    else:
      post_dict = vc_post
      title = 'Voldemort\'s Children, Page '+str(vc_idx)
      link = comics.page_url(post_dict)
      post_string = '<a href="'+utils.canonical_website_base+link+'">New page of Voldemort\'s Children</a>'
      vc_idx = vc_idx - 1
    metadata = blog.post_metadata(post_dict)
    
    entries.append('''
    <entry>
      <id>'''+utils.canonical_website_base+link+'''</id>
      <title type="html">'''+cgi.escape(title)+'''</title>
      <updated>'''+atom_time(metadata["date_modified"])+'''</updated>
      '''+author+'''
      <link rel="alternate" href="'''+utils.canonical_website_base+link+'''" />
      <content type="html">'''+cgi.escape(post_string)+'''</content>
    </entry>
    ''')
  
  utils.checked_insert(page_dict,
    '/atom.xml',
    '''<?xml version="1.0" encoding="utf-8"?>

<feed xmlns="http://www.w3.org/2005/Atom">
  <id>http://www.elidupree.com/</id>
  <title>Eli Dupree's website</title>
  <updated>'''+atom_time(datetime.datetime.utcnow())+'''</updated>
  '''+author+'''
  <link rel="self" href="/atom.xml" />
  '''+''.join(entries)+'''
</feed>'''
  )

