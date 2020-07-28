#!/usr/bin/python3
# -*- coding: utf-8 -*-

from post_contents_utils import *

head = '''<style>

.table_of_contents_chapter {
  text-indent: 2em;
}
.table_of_contents_chapter .chapter_link {
  margin-right: 0.3em;
}
.table_of_contents_remaining {
  text-indent: 2em;
  font-style: italic;
}
div.blog_post h1 {
  text-align: center;
  padding-left: 0;
  padding-right: 0;
}
div.blog_post h2 {
  text-align: center;
  padding-left: 0;
  padding-right: 0;
}
div.blog_post p {
  clear: both;
}
div.blog_post img {
  display: block;
  margin: 2.8em auto;
  max-width: 100%;
}
div.blog_post div.clear {
  clear: both;
}
div.blog_post p.text {
  border-radius: 1.3em;
  max-width: 60%;
  text-indent: 0;
  padding: 6px 12px;
  margin: 1px 0;
  font-family: Arial, Helvetica, sans-serif;
}
p.text.right {
  background-color: #87e520;
  float: right;
}
p.text.left {
  background-color: #e5e4e4;
  float: left;
}
.story_content_warning_header {
  margin-top: 1.1em;
}
.novel-current-status {
  font-family: Arial, Helvetica, sans-serif;
}
.yali-narration {
  /*font-family: Georgia, serif;*/
  font-style: italic;
}
.yali-narration em {
font-weight: bold;
}

/* For the emoji graphics, we currently use twemoji (https://github.com/twitter/twemoji). */
div.blog_post img.emoji {
  display: inline-block;
  width: 1em;
  height: 1em;
  margin: 0;
  vertical-align: middle;
}
  </style>'''
