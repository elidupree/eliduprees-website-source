#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import re
import random
import datetime
import pickle

import css
import javascript

import html_pages
import bars
import blog_server_shared
import blog_posts
import comments
import utils
import tags
import exmxaxixl

#page_max_width = 75
#post_content_min_width = 18.5
#post_content_max_width = 35
#right_bar_content_width = 13.5
text_padding_width = 1.3 #0.75
text_padding_width_narrow = 0.9
comment_indent_width = 0.75
nice_narrow_margin = 2
narrowest_margin = 0.5
post_vertical_separation = 1
post_padded_min_width = 20 #post_content_min_width + (2*text_padding_width)
post_padded_max_width = 36.5 #post_content_max_width + (2*text_padding_width)
right_bar_padded_width = 15 #right_bar_content_width + (2*text_padding_width)
#max_side_space = (page_max_width - post_padded_max_width) / 2
#right_bar_padded_width = max_side_space - 2*(min_side_space_for_post)
#right_bar_content_width = right_bar_padded_width - (2*text_padding_width)

#min_space_for_full_post_width = min_side_space_for_post + post_padded_max_width + max_side_space
#min_space_for_two_columns_and_all_margins = min_side_space_for_post + post_padded_min_width + max_side_space
#min_space_for_two_columns_and_all_but_left_margin = min_space_for_two_columns_and_all_margins - min_side_space_for_post
#min_space_for_two_columns_and_all_but_side_margins = min_space_for_two_columns_and_all_but_left_margin - min_side_space_for_post
#min_space_for_two_columns_with_least_margins = min_space_for_two_columns_and_all_but_side_margins - min_side_space_for_post + maximally_pinched_margin



background_color = "#000000"
metacontent_color_IE8 = "#bbbbbb"
metacontent_color = "rgba(255,255,255,.7)"
comment_hover_border_width = "2px"

# NOTE: There's a slight issue with the @media queries. Browsers usually include scrollbar width in them, which makes them trigger 
# at a slightly wrong size, causing there to be some jerky transitions and/or making the page content overflow the page a bit.
# I could use https://github.com/stowball/mqGenie/ , but I don't consider it important enough to spend a script on.

css.insert('''
div.blog_page_limits {
  position: relative;
  display: table;
  table-layout: fixed;
  margin-left:auto; margin-right:auto;
  width:'''+str(post_padded_max_width+4*nice_narrow_margin+2*right_bar_padded_width)+'''em; }


div.blog_left_margin {
  display: table-cell; }

div.blog_stream {
  display: table-cell;
  width: '''+str(post_padded_max_width)+'''em; }

div.blog_middle_margin {
  display: table-cell;
  width: '''+str(nice_narrow_margin)+'''em; }
  
div.blog_right_bar {
  display: table-cell;
  vertical-align: top;
  width: '''+str(right_bar_padded_width)+'''em; }
div.blog_right_bar_inner {
  margin-top: 1.5em;
  padding: '''+str(text_padding_width)+'''em;
  background-color: '''+metacontent_color_IE8+''';
  background-color: '''+metacontent_color+'''; }

div.blog_right_margin {
  display: table-cell;
  width: '''+str(nice_narrow_margin)+'''em; }
  
div.post_content_section {
  margin-top:'''+str(post_vertical_separation)+'''em;
  padding:'''+str(text_padding_width)+'''em;
  background-color: white; }

@media screen and (max-width: '''+str(post_padded_max_width+4*nice_narrow_margin+2*right_bar_padded_width)+'''em) {
  div.blog_page_limits { width: 100%; }
}
@media screen and (max-width: '''+str(post_padded_max_width+3*nice_narrow_margin+right_bar_padded_width)+'''em) {
  div.blog_stream      { width: auto; }
  div.blog_left_margin { width: '''+str(nice_narrow_margin)+'''em; }
}
@media screen and (max-width: '''+str(post_padded_min_width+3*nice_narrow_margin+right_bar_padded_width)+'''em) {
  div.blog_left_margin { width: auto; }
  div.blog_stream      { width: '''+str(post_padded_min_width)+'''em; }
}
@media screen and (max-width: '''+str(post_padded_min_width+2*nice_narrow_margin+right_bar_padded_width)+'''em) {
  div.blog_left_margin { display: none; }
  div.blog_right_margin { width: auto; }
}
@media screen and (max-width: '''+str(post_padded_min_width+1*nice_narrow_margin+right_bar_padded_width)+'''em) {
  div.blog_right_margin { display: none; }
  div.blog_middle_margin { width: auto; }
}
@media screen and (max-width: '''+str(post_padded_min_width+narrowest_margin+right_bar_padded_width)+'''em) {
  div.blog_middle_margin { display: none; }
  div.blog_page_limits   { display: block; }
  div.blog_stream        { display: block; width: auto; }
  div.blog_right_bar     { display: block; width: auto; }
  div.post_content_section { padding:'''+str(text_padding_width_narrow)+'''em; }
  div.blog_right_bar_inner { padding:'''+str(text_padding_width_narrow)+'''em; }
}
  
a.post_title_link { color:black; text-decoration:none; }
div.blog_post h2 {
  font-size: 180%;
  font-weight: bold;
  padding: 0.1em;
  padding-left: 1em; }
div.blog_post p {
  text-indent: 2em; }
div.blog_post_metadata_outer {
  padding: 0 0.8em;
  margin-bottom:'''+str(post_vertical_separation)+'''em; }
div.blog_post_metadata {
  font-size: 80%;
  padding: 0.75em;
  background-color:'''+metacontent_color_IE8+''';
  background-color:'''+metacontent_color+'''; }

h2.comments_title {
  font-size: 200%;
  font-weight: bold;
  padding-top: 0.2em;
  text-align: center; }
div.blog_post_comments:hover>h2.comments_title:not(:hover) {
  border-left: '''+comment_hover_border_width+''' solid red;
  margin-left: -'''+comment_hover_border_width+''';
  border-top-left-radius: 5% 100%; }
div.comment_body_outer {
  padding-top:0.5em;
  padding-left: '''+str(comment_indent_width)+'''em; }
div.user_comment>div.comment_hover_box {
  margin-left: '''+str(comment_indent_width)+'''em; }
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
  border-left: '''+str(comment_indent_width)+'''em solid red;
  margin-left: -'''+str(comment_indent_width)+'''em; }
span.reply_to_comment {
  display: none; }
body.javascript_enabled span.reply_to_comment {
  display: inline; }
div.make_reply_box {
  padding-left: '''+str(comment_indent_width)+'''em; }
a.direct_comment {
  display: none;
  font-size: 150%;
  font-weight: bold;
  padding-top: 0.4em;
  text-align: center; }
body.javascript_enabled a.direct_comment {
  display: block; }

a:link.blog_end_link { color:yellow; }
a:visited.blog_end_link { color:orange; }
div.blog_end_links_2 {
  clear:both;
  margin-top:'''+str(post_vertical_separation/4)+'''em;
  text-align:center; }
a.blog_end_link.nav {
  display: inline-block;
  font-size: 200%;
  padding: 0.4em 0.2em; }
a.blog_end_link.nav.right {
  float:right; }

div.blog_index {
  padding: 0.4em 0; }
div.index_entry {
  padding: 0 0.6em; }
a.random_post {
  display: none;
  padding: 0.4em 0; }
a.random_post.enabled {
  display: block; }
  
q { border: 1px inset white; color: #606060; }
blockquote { border-left: 2px solid #c0c0c0; padding: 0.25em; color: #606060; margin-left: 2.5em; margin-right: 2.5em; margin-top: 0; margin-bottom: 1em; }
p.reply_input_info { padding-left: 0.5em; }
span.big_quote_mark_outer { width: 2em; height: 0; float: left; margin-left: 0.5em; margin-top: -0.5em; }
span.big_quote_mark_inner { font-size: 5em; color: #c0c0c0; }
div.footnotes { margin-top: 2em; }
a.footnote_link { color: black; }
''')

javascript.do_after_body('''
var comments = document.getElementsByName("user_comment");
var all_comments_divs = document.getElementsByName("all_comments");
var random_post_link = document.getElementById("random_post");
var index_entries = document.getElementsByName("index_entry");
var random_entry;
var i;

function expand_reply_box(elem, id) {
  elem.innerHTML = '<div class="preview_space"></div><p class="reply_input_info">'+'You may use &lt;em&gt;<em>emphasized text</em>&lt;/em&gt;, &lt;strong&gt;<strong>strongly emphasized text</strong>&lt;/strong&gt;, <br/>&lt;q&gt;<q>Quoted text</q>&lt;/q&gt;, and &lt;blockquote&gt;longer, indented quotes&lt;/blockquote&gt;.'+'</p>Name: <input type="text"><textarea class="make_reply_input" cols="60" rows="7"></textarea><br/>';
  var preview_button = document.createElement("button")
  preview_button.innerHTML = 'Preview your reply'
  add_event_listener(preview_button, function() {
    
  })
  elem.appendChild(preview_button)
}

function setup_reply_box(id) {
  var make_reply_box = document.getElementById("make_reply_box_"+id);
  var make_reply_button = document.getElementById("make_reply_button_"+id);
  var expanded = false;
  add_event_listener(make_reply_button,'click',function() {
    if (!expanded) {
      expanded = true;
      expand_reply_box(make_reply_box, id);
    }
  });
}
for (i = 0; i < comments.length; ++i) {
  setup_reply_box(comments[i].id)
}
for (i = 0; i < all_comments_divs.length; ++i) {
  setup_reply_box(all_comments_divs[i].id)
}
if (random_post_link) {
  random_entry = index_entries[Math.floor(Math.random()*index_entries.length)];
  random_post_link.setAttribute("href", random_entry.getAttribute("href"))
  random_post_link.innerHTML = "[Random post] "+random_entry.innerHTML
  random_post_link.className = random_post_link.className+" enabled"
}
''')
print ('TODO: say "random story" instead on stories pages')

comment_ids_by_parent = {}
comments_by_id = {}
posts_metadata = {}
try:
  with open("posts_metadata.pkl", "rb") as p:
    posts_metadata = pickle.load(p)
except(IOError):
  posts_metadata = {}

def remember_post_dict_entry(index, metadata, post_dict):
  if (index in post_dict) and (("remembered_"+index not in metadata) or (post_dict[index] != metadata["remembered_"+index])):
    metadata["remembered_"+index] = post_dict[index]
    metadata["date_modified"] = datetime.date.today()
    return True
  return False
  

print("TODO: only update date posted(/modified?) when actually deploying the page, not building previews")

def post_metadata(post_dict):
  changed_metadata = False
  if post_dict["title"] not in posts_metadata:
    posts_metadata[post_dict["title"]] = {
      "id": hex(random.SystemRandom().getrandbits(128))[2:-1],
      "date_posted": (post_dict["force_date"] if ("force_date" in post_dict) else datetime.date.today()),
    }
    changed_metadata = True
  metadata = posts_metadata[post_dict["title"]]
  
  if remember_post_dict_entry("contents", metadata, post_dict):
    changed_metadata = True
  if remember_post_dict_entry("transcript", metadata, post_dict):
    changed_metadata = True
  if remember_post_dict_entry("annotation", metadata, post_dict):
    changed_metadata = True
  
  # allow me to set force_date later
  if ("force_date" in post_dict) and (metadata["date_posted"] != post_dict["force_date"]):
    metadata["date_posted"] = post_dict["force_date"]
    changed_metadata = True
  
  if changed_metadata:
    pickle.dump(posts_metadata, open("posts_metadata.pkl", "wb"))
  
  return metadata


for comment in comments.comments:
  comments_by_id[comment["id"]] = comment
for comment in comments.comments:
  if comment["parent"] not in comment_ids_by_parent:
    comment_ids_by_parent[comment["parent"]] = []
  comment_ids_by_parent[comment["parent"]].append(comment["id"])

def post_permalink(post_dict):
  return "/"+post_dict["path_prefix"]+url_formatted_title(post_dict)

def do_comments(parent, top_level):
  child_ids = comment_ids_by_parent[parent] if parent in comment_ids_by_parent else []
  html_list = []
  num = 0
  for child_id in child_ids:
    (cnum, chtml) = do_comments(child_id, False)
    child = comments_by_id[child_id]
    num = num + cnum + 1
    html_list.append('''
<article>
  <div class="user_comment" name="user_comment" id="'''+child_id+'''">
    <div class="comment_body_hover_marker">
      <div class="comment_body_outer">
        <div class="comment_body">
          <div><strong>'''+child["username"]+'</strong>'+utils.inline_separator+child["date_posted"].strftime("%B %-d, %Y")+utils.inline_separator+'<a href="#'+child_id+'">Permalink</a><span class="reply_to_comment">'+utils.inline_separator+'''<a href="javascript:;" id="make_reply_button_'''+child_id+'''">Reply</a></span></div>
          '''+blog_server_shared.postprocess_post_string(child["contents"], child_id, None, False)[0]+'''
        </div>
        <div class="make_reply_box" id="make_reply_box_'''+child_id+'''"></div>
      </div>
    </div>
    '''+chtml+'''
  </div>
</article>''')
  return (num, put_in_hover_boxes(html_list))

def post_dict_html(post_dict, expand_comments):
  return post_html(post_dict["contents"], post_dict["title"], post_permalink(post_dict), post_dict["tags"] if "tags" in post_dict else None, expand_comments, post_metadata(post_dict), post_dict["path_prefix"] != "stories/")

def post_html(contents, title, permalink, taglist, expand_comments, metadata, scrutinize = True):
  post_content = blog_server_shared.postprocess_post_string(contents, metadata["id"], title, False, scrutinize)[0]
  
  
  content_notice_header_regex = re.compile(r"<content_notice_header"+blog_server_shared.grouped_string_regex("content_notice_header_contents")+">", re.DOTALL)
  post_content = content_notice_header_regex.sub(lambda match: ('''

<div class="story_content_notice_header remove_if_content_notices_disabled">
  <p><mark>Note: You are reading this story with content notices. <a id="disable_content_notices_button_toggle" href="javascript:;">(disable content notices)</a></mark></p>
  <p>This story contains:</p>
  <ul>
    '''+match.group("content_notice_header_contents")+'''
  </ul>
  <p><mark>Notices will also appear in-context in the story, just before the material appears.</mark></p>
  <p><mark>If you see other material that should be marked (such as common triggers or phobias), '''+exmxaxixl.a('e-mail me')+'''. I am serious about web accessibility, and I will respond to your concerns as soon as I can manage.</mark></p>
</div>
<div class="story_content_notice_header remove_if_content_notices_enabled">
  <p><mark>Note: You are reading this story without content notices. <a id="enable_content_notices_button_toggle" href="javascript:;">(enable content notices)</a></mark></p>
</div>'''), post_content)

  content_notice_p_regex = re.compile(r"<content_notice_p"+blog_server_shared.grouped_string_regex("content_notice_p_contents")+">", re.DOTALL)
  post_content = content_notice_p_regex.sub(lambda match: '''
     <p class="content_notice remove_if_content_notices_disabled"><mark>This section depicts '''+match.group("content_notice_p_contents")+'''.</mark></p>''', post_content)
  
  
  post_content_sections = post_content.split("<bigbreak>")
  id_str = ''
  if title:
    id_str = 'id="'+utils.format_for_url(title)+'"'
    post_content_sections[0] = '<h1><a class="post_title_link" href="'''+permalink+'">'+title+'</a></h1>'+post_content_sections[0]
  for i in range(0, len(post_content_sections)):
    post_content_sections[i] = '<div class="post_content_section">'+post_content_sections[i]+'</div>'
  return '''
<div '''+id_str+''' class="blog_post">
  '''+(''.join(post_content_sections))+'''
</div>'''+metadata_and_comments_section_html(permalink, taglist, expand_comments, metadata)

def metadata_and_comments_section_html(permalink, taglist, expand_comments, metadata):
  (cnum, chtml) = do_comments(metadata["id"], True)
  comments_stuff = ""
  if expand_comments:
    comments_stuff = '''
<section>
  <div class="blog_post_comments" id="comments">
    '''+('<h2 class="comments_title">Comments</h2>' if (cnum > 0) else '')+'''
    <div class="all_comments" name="all_comments" id='''+metadata["id"]+'''>'''+chtml+'''</div>
  </div>
  <a href="javascript:;" class="direct_comment" id="make_reply_button_'''+metadata["id"]+'''">Leave a comment</a>
  <div class="make_reply_box" id="make_reply_box_'''+metadata["id"]+'''"></div>
</section>'''
  else:
    comments_stuff = utils.inline_separator+'<a href="'+permalink+'#comments">Comments&nbsp;('+str(cnum)+')</a>'
  
  tags_str = ''
  if taglist:
    tags_str = 'Tags: '+(", ".join(tags.tag_link(tag) for tag in taglist))+utils.inline_separator
  date_str = metadata["date_posted"].strftime("%B %-d, %Y")+utils.inline_separator
  if metadata["date_modified"] != metadata["date_posted"]:
    date_str = 'Posted '+metadata["date_posted"].strftime("%B %-d, %Y")+utils.inline_separator+'Last updated '+metadata["date_modified"].strftime("%B %-d, %Y")+utils.inline_separator
  
  return '''
<div class="blog_post_metadata_outer">
  <div class="blog_post_metadata">
    '''+tags_str+date_str+'<a rel="bookmark" href="'+permalink+'">Permalink</a>'+comments_stuff+'''
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
  return '<div class="index_entry"><a name="index_entry" href="'+post_permalink(post_dict)+'">'+post_dict["title"]+'</a></div>'


def make_blog_page_body(main_contents, sidebar_contents):
  return '''
  <a class="skip" href="#content">Skip to content</a><a class="skip" href="#blog-sidebar">Skip to blog sidebar</a>
  <div><img role="presentation" alt="" class="background" src="/media/colorful-background.jpg" /></div>
  '''+bars.bars_wrap({"blog":True}, '''
    <main>
      <div id="content" class="blog_page">
        <div class="blog_page_limits">
          <div class="blog_margin blog_left_margin"></div>
          <div class="blog_stream">'''+main_contents+'''</div>
          <div class="blog_margin blog_middle_margin"></div>
          <div id="blog-sidebar" class="blog_right_bar"><div class="blog_right_bar_inner">'''+sidebar_contents+'''</div></div>
          <div class="blog_margin blog_right_margin"></div>
        </div>
      </div>
    </main>''')+'''
  '''

  
def url_formatted_title(post_dict):
  return utils.format_for_url(post_dict["title"])
def title_formatted_title(post_dict):
  return utils.strip_tags(post_dict["title"])

def latest_post_preview_text():
  return blog_posts.posts["blog"][-1]["title"]

page_length = 10
latest_page_max_posts = page_length + 5
def post_is_on_latest_page(list_index, posts):
  first_on_this_page = list_index - (list_index % page_length)
  return len(posts) - first_on_this_page <= latest_page_max_posts

def add_category_pages(page_dict, posts, category, tag_specific = None):
  if tag_specific:
    tags_string = '/tags/'+tag_specific
    list_desc = tags.tags[tag_specific]
  else:
    tags_string = ''
    list_desc = "All "+category+" posts" if category == "blog" else "All "+category
    posts_by_tag = {}
    for tag in tags.tags:
      posts_by_tag[tag] = []
  
  current_page_number = 1
  current_page = []
  index_entries = []
  if category == "":
    sidebar_contents = ''
  else:
    for i in range(0,len(posts)):
      list_index = len(posts)-i-1
      post_dict = posts[list_index]
      if category == "blog" and list_index % page_length == page_length - 1 and not post_is_on_latest_page(list_index, posts):
        page = (list_index+1)//page_length
        index_entries.append('<div class="index_page_entry"><a href="/blog'+tags_string+'/page/'+str(page)+'">Page '+str(page)+'</a></div>')
      index_entries.append(index_entry_html(post_dict))
    index = ('<div class="blog_index">'
      +'<a href="/'+category+tags_string+'">'+list_desc+'</a>:'
      +("\n".join(index_entries))
      +'</div>')
    sidebar_contents = '<nav><a class="random_post" id="random_post"></a>'+index+'</nav>'
  
  for i in range(0,len(posts)):
    post_dict = posts[i]
    current_page.append('<article>'+post_dict_html(post_dict, False)+'</article>')
    
    if category == "blog":
      remaining_posts = len(posts) - i
      on_latest_page = post_is_on_latest_page(i, posts)
      print_older_page = ((len(current_page) >= page_length) and not on_latest_page)
      print_latest_page = (i == len(posts) - 1)
      if print_older_page and print_latest_page:
        raise "This code is messed up somehow"
      
      if on_latest_page:
        url_pagenum_string = ''
      else:
        url_pagenum_string = '/page/'+str(current_page_number)
      
      if print_older_page or print_latest_page:
        for page_order in ('','/chronological'):
          end_links = ''
          if current_page_number > 1:
            end_links = (end_links+'<a href="/'+category+tags_string+'/page/'+str(current_page_number-1)+page_order+
              '" rel="prev" class="blog_end_link nav">Older posts</a>')
          if print_older_page:
            end_links = (end_links+'<a href="/'+category+tags_string+('/page/'+str(current_page_number+1)+page_order if (remaining_posts > latest_page_max_posts) else page_order)+
              '" rel="next" class="blog_end_link nav right">Newer posts</a>')
          if current_page_number > 1:
            end_links = end_links+'''
  <div class="blog_end_links_2">
    <a class="blog_end_link" href="'''+category+tags_string+'''/page/1/chronological">Go back to the beginning and read in chronological order</a>
  </div>'''
          elif (page_order != '/chronological') and (len(posts) > 1):
            end_links = end_links+'''
  <div class="blog_end_links_2">
    <a class="blog_end_link" href="/blog'''+tags_string+'''/page/1/chronological">Read in chronological order</a>
  </div>'''

          utils.checked_insert(page_dict,
            'blog'+tags_string+url_pagenum_string+page_order+'.html',
            html_pages.make_page(
              (tags.tags[tag_specific]+' ⊂ ' if tag_specific else '')+utils.capitalize_string(category)+" ⊂ Eli Dupree's website",
              "",
              make_blog_page_body("\n".join(current_page if page_order == "/chronological" else reversed(current_page))+end_links, sidebar_contents)
            )
          )
        current_page = []
        current_page_number += 1
    
    if not tag_specific:
      if "tags" in post_dict:
        for tag in post_dict["tags"]:
          posts_by_tag[tag].append(post_dict)
      utils.checked_insert(page_dict,
        category+'/'+url_formatted_title(post_dict)+'.html',
        html_pages.make_page(
          title_formatted_title(post_dict)+" ⊂ "+utils.capitalize_string(category)+" ⊂ Eli Dupree's website",
          "",
          make_blog_page_body(post_dict_html(post_dict, True), sidebar_contents)
        )
      )
        
  if category == "blog" and not tag_specific:
    for tagname,posts in posts_by_tag.items():
      add_category_pages(page_dict, posts, "blog", tagname)

def add_pages(page_dict):
  for cat,posts in blog_posts.posts.items():
    add_category_pages(page_dict, posts, cat)