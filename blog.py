#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import re
import random
import datetime
import pickle

import css

import html_pages
import bars
import blog_posts
import comments
import utils
import tags

page_max_width = 75
post_content_min_width = 20
post_content_max_width = 35
text_padding_width = 0.75
post_padded_min_width = post_content_min_width + (2*text_padding_width)
post_padded_max_width = post_content_max_width + (2*text_padding_width)
post_separation = 1
max_side_space = (page_max_width - post_padded_max_width) / 2
min_side_space_for_post = 2
maximally_pinched_margin = 0.5
right_bar_padded_width = max_side_space - 2*(min_side_space_for_post)
right_bar_content_width = right_bar_padded_width - (2*text_padding_width)

min_space_for_full_post_width = min_side_space_for_post + post_padded_max_width + max_side_space
min_space_for_two_columns_and_all_margins = min_side_space_for_post + post_padded_min_width + max_side_space
min_space_for_two_columns_and_all_but_left_margin = min_space_for_two_columns_and_all_margins - min_side_space_for_post
min_space_for_two_columns_and_all_but_side_margins = min_space_for_two_columns_and_all_but_left_margin - min_side_space_for_post
min_space_for_two_columns_with_least_margins = min_space_for_two_columns_and_all_but_side_margins - min_side_space_for_post + maximally_pinched_margin

background_color = "#000000";
metacontent_color_IE8 = "#bbbbbb"
metacontent_color = "rgba(255,255,255,.7)"
comment_hover_border_width = "2px";

css.insert('''
div.blog_page_limits {
  position: relative;
  margin-left:auto; margin-right:auto;
  min-width:'''+str(min_space_for_two_columns_with_least_margins)+'''em;
  max-width:'''+str(page_max_width)+'''em; }

div.blog_stream_and_right_bar { float:right; }
div.blog_stream { display:inline-block;
  min-width:'''+str(post_padded_min_width)+'''em;
  max-width:'''+str(post_padded_max_width)+'''em;
  margin-left:''' +str(min_side_space_for_post)+'''em;
  margin-right:'''+str(min_side_space_for_post)+'''em; }
div.blog_bottom { clear:both; }

div.blog_right_bar {
  display:inline-block;
  vertical-align:top;
  width:'''+str(right_bar_content_width)+'''em;
  padding:'''+str(text_padding_width)+'''em;
  margin-top:1.5em;
  margin-right:'''+str(min_side_space_for_post)+'''em;
  background-color:'''+metacontent_color_IE8+''';
  background-color:'''+metacontent_color+'''; }

@media screen and (max-width: '''+str(min_space_for_full_post_width)+'''em) {
  div.blog_stream    { margin-right:'''+str(max_side_space)+'''em; }
  div.blog_right_bar { margin-left:-'''+str(max_side_space-min_side_space_for_post)+'''em; }
}
@media screen and (max-width: '''+str(min_space_for_two_columns_and_all_margins)+'''em) {
  div.blog_stream { margin-left:0; width:'''+str(post_padded_min_width)+'''em; }
  div.blog_right_bar { margin-right:0; }
}
@media screen and (max-width: '''+str(min_space_for_two_columns_and_all_but_left_margin)+'''em) {
  div.blog_stream_and_right_bar { float:none; }
  div.blog_stream    { margin-right:'''+str(min_side_space_for_post)+'''em; }
  div.blog_right_bar { margin-left:0; }
}
@media screen and (max-width: '''+str(min_space_for_two_columns_and_all_but_side_margins)+'''em) {
  div.blog_stream    { margin-right:0; }
  div.blog_right_bar { float:right; }
}
  
div.blog_post {
  min-width:'''+str(post_content_min_width)+'''em;
  max-width:'''+str(post_content_max_width)+'''em;
  margin-top:'''+str(post_separation)+'''em;
  padding:'''+str(text_padding_width)+'''em;
  background-color: white; }
a.post_title_link { color:black; text-decoration:none; }
div.blog_post p {
  text-indent: 2em; }
div.blog_post_metadata_outer {
  min-width:'''+str(post_content_min_width)+'''em;
  max-width:'''+str(post_content_max_width)+'''em;
  padding: 0 0.8em;
  margin-bottom:'''+str(post_separation)+'''em; }
div.blog_post_metadata {
  font-size: 80%;
  padding:'''+str(text_padding_width)+'''em;
  background-color:'''+metacontent_color_IE8+''';
  background-color:'''+metacontent_color+'''; }

h2.comments_title {
  font-size: 200%;
  font-weight: bold;
  padding-top:'''+str(text_padding_width/4)+'''em;
  text-align: center; }
div.blog_post_comments:hover>h2.comments_title:not(:hover) {
  border-left: '''+comment_hover_border_width+''' solid red;
  margin-left: -'''+comment_hover_border_width+''';
  border-top-left-radius: 5% 100%; }
div.comment_body_outer {
  padding-top:0.5em;
  padding-left: '''+str(text_padding_width)+'''em; }
div.user_comment>div.comment_hover_box {
  margin-left: '''+str(text_padding_width)+'''em; }
div.comment_body {
  background-color: white;
  padding:0.5em '''+str(text_padding_width)+'''em; }
div.comment_hover_box:hover>div.whole_comment_hover_marker:not(:hover) {
  border-left: '''+comment_hover_border_width+''' solid red;
  margin-left: -'''+comment_hover_border_width+'''; }
div.user_comment:hover>div.comment_body_hover_marker {
  border-left: '''+comment_hover_border_width+''' solid red;
  margin-left: -'''+comment_hover_border_width+'''; }
div.all_comments:hover div.comment_body {
  background-color: #dddddd; }
div.user_comment:hover>div.comment_body_hover_marker>*>div.comment_body {
  background-color: white;
  border: '''+comment_hover_border_width+''' solid red;
  margin: -'''+comment_hover_border_width+''';
  border-left: '''+str(text_padding_width)+'''em solid red;
  margin-left: -'''+str(text_padding_width)+'''em; }
span.reply_to_comment {
  display: none; }
body.javascript_enabled span.reply_to_comment {
  display: inline; }

a:link.blog_end_link { color:yellow; }
a:visited.blog_end_link { color:orange; }
div.blog_end_links_2 {
  clear:both;
  margin-top:'''+str(post_separation/4)+'''em;
  text-align:center; }
a.blog_end_link.nav {
  display: inline-block;
  font-size: 200%;
  padding:'''+str(text_padding_width/2)+'''em '''+str(text_padding_width/4)+'''em; }
a.blog_end_link.nav.right {
  float:right; }

div.blog_index {
  padding: 0.8em 0; }
''')

comment_ids_by_parent = {}
comments_by_id = {}
posts_metadata = {}
try:
  with open("posts_metadata.pkl", "rb") as p:
    posts_metadata = pickle.load(p)
except(IOError):
  posts_metadata = {}
  
def post_metadata(post_dict):
  if post_dict["title"] not in posts_metadata:
    posts_metadata[post_dict["title"]] = {
      "id": hex(random.SystemRandom().getrandbits(128))[2:-1],
      "date_posted": (post_dict["force_date"] if ("force_date" in post_dict) else datetime.date.today()),
    }
    pickle.dump(posts_metadata, open("posts_metadata.pkl", "wb"))
  return posts_metadata[post_dict["title"]]

for post in blog_posts.posts:
  comment_ids_by_parent[post["title"]] = []
for comment in comments.comments:
  comments_by_id[comment["id"]] = comment
  comment_ids_by_parent[comment["id"]] = []
for comment in comments.comments:
  comment_ids_by_parent[comment["parent"]].append(comment["id"])

def post_permalink(post_dict):
  return "/blog/"+url_formatted_title(post_dict)
def post_div_id(post_dict):
  return url_formatted_title(post_dict)

def do_comments(parent, top_level):
  child_ids = comment_ids_by_parent[parent]
  html_list = []
  num = 0
  for child_id in child_ids:
    (cnum, chtml) = do_comments(child_id, False)
    child = comments_by_id[child_id]
    num = num + cnum + 1
    html_list.append('''
<article>
  <div class="user_comment" id="'''+child_id+'''">
    <div class="comment_body_hover_marker">
      <div class="comment_body_outer">
        <div class="comment_body">
          <div><strong>'''+child["username"]+'</strong>'+utils.inline_separator+child["date_posted"].strftime("%B %-d, %Y")+utils.inline_separator+'<a href="#'+child_id+'">Permalink</a><span class="reply_to_comment">'+utils.inline_separator+'''<a href="javascript:;">Reply</a></span></div>
          '''+child["contents"]+'''
        </div>
      </div>
    </div>
    '''+chtml+'''
  </div>
</article>''')
  return (num, put_in_hover_boxes(html_list))

def post_html(post_dict, expand_comments):
  metadata = post_metadata(post_dict)
  (cnum, chtml) = do_comments(post_dict["title"], True)
  comments_stuff = ""
  if expand_comments:
    comments_stuff = '''
<section>
  <div class="blog_post_comments" id="comments">
    <h2 class="comments_title">Comments</h2>
    <div class="all_comments">'''+chtml+'''</div>
  </div>
</section>'''
  else:
    comments_stuff = utils.inline_separator+'<a href="'+post_permalink(post_dict)+'#comments">Comments&nbsp;('+str(cnum)+')</a>'
  return '''
<div id="'''+post_div_id(post_dict)+'''" class="blog_post">
  <h1><a class="post_title_link" href="'''+post_permalink(post_dict)+'">'+post_dict["title"]+'</a></h1>'+post_dict["contents"]+'''
</div>
<div class="blog_post_metadata_outer">
  <div class="blog_post_metadata">
    '''+('Tags: '+(", ".join(tags.tag_link(tag) for tag in post_dict["tags"]))+utils.inline_separator if "tags" in post_dict else "")+metadata["date_posted"].strftime("%B %-d, %Y")+utils.inline_separator+'<a rel="bookmark" href="'+post_permalink(post_dict)+'">Permalink</a>'+comments_stuff+'''
  </div>
</div>'''

global fake_comment_id
fake_comment_id = ''
def put_in_hover_boxes(comment_list):
  if len(comment_list) == 0:
    return ''
  global fake_comment_id
  fake_comment_id = fake_comment_id+'i'
  return '<div class="comment_hover_box"><div class="whole_comment_hover_marker">'+comment_list[0]+'</div>'+put_in_hover_boxes(comment_list[1:])+'</div>'

def fake_comments(tree_structure):
  return put_in_hover_boxes(['<article><div class="user_comment" id='+fake_comment_id+'><div class="comment_body_hover_marker"><div class="comment_body_outer"><div class="comment_body"><h3>SomeUser5098 <a href="#'+fake_comment_id+'">wrote</a>:</h3>I GOT STUFF TO SAY</div></div></div>'+fake_comments(foo)+'</div></article>' for foo in tree_structure])

fake_comment_html = '''<section>
  <div class="blog_post_comments">
    <h2 class="comments_title">Comments</h2>
    <div class="all_comments">'''+fake_comments([[[],[[[],[[[]],[]],[]]]],[],[[[],[[[],[[[]],[]],[]]]]]])+'''</div>
  </div>
</section>'''
  
def add_fake_comments(html):
  return re.sub(re.escape(utils.inline_separator+'<a href="">Comments&nbsp;(14)</a>'), fake_comment_html, html)

def index_entry_html(post_dict):
  return '<div class="index_entry"><a href="">'+post_dict["title"]+'</a></div>'


def make_blog_page_body(main_contents, sidebar_contents):
  return '''
<body><a class="skip" href="#content">Skip to content</a><a class="skip" href="#blog-sidebar">Skip to blog sidebar</a>
  <div><img role="presentation" alt="" class="background" src="/media/blog-background.jpg" /></div>
  '''+bars.bars_wrap({"blog":True}, '''
    <main>
      <div id="content" class="blog_page">
        <div class="blog_page_limits">
          <div class="blog_stream_and_right_bar">
            <div class="blog_stream">'''+main_contents+'''</div>
            <div id="blog-sidebar" class="blog_right_bar">'''+sidebar_contents+'''</div>
          </div>
          <div class="blog_bottom"></div>
        </div>
      </div>
    </main>''')+'''
</body>'''

  
def url_formatted_title(post_dict):
  return utils.format_for_url(post_dict["title"])
def title_formatted_title(post_dict):
  return utils.strip_tags(post_dict["title"])

def latest_post_preview_text():
  return blog_posts.posts[-1]["title"]

def add_blog_pages(page_dict, tag_specific = None):
  if tag_specific:
    posts = tag_specific["post_list"]
  else:
    posts = blog_posts.posts
    posts_by_tag = {}
    for tag in tags.tags:
      posts_by_tag[tag] = []
  
  current_page_number = 1
  current_page = []
  index = ('<div class="blog_index">'
    +('Posts tagged &quot;'+tag_specific["tagname"]+'&quot;:' if tag_specific else 'All posts:')
    +("\n".join([index_entry_html(p) for p in reversed(posts)]))
    +'</div>')
  for i in range(0,len(posts)):
    post_dict = posts[i]
    current_page.append('<article>'+post_html(post_dict, False)+'</article>')
    
    page_length = 10
    latest_page_max_posts = page_length + 5
    remaining_posts = len(posts) - i
    on_latest_page = (len(current_page) + remaining_posts <= latest_page_max_posts)
    print_older_page = ((len(current_page) >= page_length) and not on_latest_page)
    print_latest_page = (i == len(posts) - 1)
    if print_older_page and print_latest_page:
      raise "This code is messed up somehow"
    
    if on_latest_page:
      url_pagenum_string = ''
    else:
      url_pagenum_string = '/page/'+str(current_page_number)
      
    if tag_specific:
      tags_string = '/tags/'+tag_specific["tagname"]
    else:
      tags_string = ''
    
    if print_older_page or print_latest_page:
      for page_order in ('','/chronological'):
        end_links = ''
        if current_page_number > 1:
          end_links = (end_links+'<a href="/blog'+tags_string+'/page/'+str(current_page_number-1)+page_order+
            '" rel="prev" class="blog_end_link nav">Older posts</a>')
        if print_older_page:
          end_links = (end_links+'<a href="/blog'+tags_string+('/page/'+str(current_page_number+1)+page_order if (remaining_posts > latest_page_max_posts) else page_order)+
            '" rel="next" class="blog_end_link nav right">Newer posts</a>')
        if current_page_number > 1:
          end_links = end_links+'''
<div class="blog_end_links_2">
  <a class="blog_end_link" href="/blog'''+tags_string+'''/page/1/chronological">Go back to the beginning and read in chronological order</a>
</div>'''
        elif (page_order != '/chronological') and (len(posts) > 1):
          end_links = end_links+'''
<div class="blog_end_links_2">
  <a class="blog_end_link" href="/blog'''+tags_string+'''/page/1/chronological">Read in chronological order</a>
</div>'''

        utils.checked_insert(page_dict,
          'blog'+tags_string+url_pagenum_string+page_order+'.html',
          html_pages.make_page(
            "Blog ⊂ Eli Dupree's website",
            "",
            make_blog_page_body("\n".join(current_page if page_order == "/chronological" else reversed(current_page))+end_links, '<nav><a href="/403">[Random post] I foobar yesterday</a>'+index+'</nav>')
          )
        )
      current_page = []
      current_page_number += 1
    
    if not tag_specific:
      if "tags" in post_dict:
        for tag in post_dict["tags"]:
          posts_by_tag[tag].append(post_dict)
      utils.checked_insert(page_dict,
        'blog/'+url_formatted_title(post_dict)+'.html',
        html_pages.make_page(
          title_formatted_title(post_dict)+" ⊂ Blog ⊂ Eli Dupree's website",
          "",
          make_blog_page_body(post_html(post_dict, True), '<a href="/blog'+url_pagenum_string+'#'+post_div_id(post_dict)+'">View this post in context</a>')
        )
      )
  
  if not tag_specific:
    for tagname,posts in posts_by_tag.items():
      add_blog_pages(page_dict, {
        "tagname":tagname,
        "post_list":posts,
      })
  
