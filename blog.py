#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import re
import random
import datetime
import copy
import json
import hashlib

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
import comics

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
div.blog_post h3 {
  font-size: 140%;
  font-weight: bold;
  padding: 0.1em;
  padding-left: 1em; }
div.blog_post h4 {
  font-size: 120%;
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
div.comments_section:hover>h2.comments_title:not(:hover) {
  border-left: '''+comment_hover_border_width+''' solid red;
  margin-left: -'''+comment_hover_border_width+''';
  border-top-left-radius: 5% 100%; }
div.comment_body_outer {
  padding-top:0.5em;
  padding-left: '''+str(comment_indent_width)+'''em; }
div.user_comment>div.comment_hover_box {
  margin-left: '''+str(comment_indent_width)+'''em; }
div.comment_body {
  font-size: 125%;
  text-align: left;
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
div.comment_header {
  padding-bottom: 0.5em; }
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
textarea.make_reply_input {
  width: 90%; }

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
  padding: 0.2em 0.6em; }
a.sidebar_standalone_link {
  padding: 0.4em 0;
  display: block; }
a.random_post {
  display: none; }
a.random_post.enabled {
  display: block; }
  
  
div.blog_post q { border: 1px inset white; color: #606060; }
blockquote { border-left: 2px solid #c0c0c0; padding: 0.25em; color: #606060; margin-left: 2.5em; margin-right: 2.5em; margin-top: 0; margin-bottom: 1em; }
p.reply_input_info { padding-left: 0.5em; }
span.big_quote_mark_outer { width: 2em; height: 0; float: left; margin-left: 0.5em; margin-top: -0.5em; }
span.big_quote_mark_inner { font-size: 5em; color: #c0c0c0; }
div.footnotes { margin-top: 2em; }
a.footnote_link { color: black; }

.scrutiny { background-color: #c0ffff; color: black; text-decoration: underline; }
.skepticism { background-color: #ffc0c0; }
''')

javascript.do_after_body(r'''
var comments = document.getElementsByName("user_comment");
var all_comments_divs = document.getElementsByName("all_comments");
var random_post_link = document.getElementById("random_post");
var index_entries = document.getElementsByName("index_entry");
var random_entry;
var i;

function expand_reply_box(elem, id) {
  elem.innerHTML = ''+
    '<div id="preview_space_'+id+'" class="preview_space"></div>'+
    '<p class="reply_input_info">'+
      'You may use &lt;em&gt;<em>emphasized text</em>&lt;/em&gt;, &lt;strong&gt;<strong>strongly emphasized text</strong>&lt;/strong&gt;, <br/>&lt;q&gt;<q>Quoted text</q>&lt;/q&gt;, and &lt;blockquote&gt;longer, indented quotes&lt;/blockquote&gt;.'+
    '</p>'+
    'Your name: <input id="reply_username_'+id+'" type="text">'+
    '<textarea id="reply_contents_'+id+'" class="make_reply_input" cols="60" rows="7"></textarea><br/>';
  var preview_space = document.getElementById('preview_space_'+id);
  var username_input = document.getElementById('reply_username_'+id);
  var contents_input = document.getElementById('reply_contents_'+id);
  username_input.value = read_cookie('username');
  var preview_button = document.createElement("button");
  preview_button.innerHTML = 'Preview your reply';
  var submit_button = document.createElement("button");
  submit_button.innerHTML = 'Submit your reply';
  var previewed = false;
  action = function(request_type) {
    return function() {
      preview_button.setAttribute('disabled', 'disabled');
      submit_button.setAttribute('disabled', 'disabled');
      set_cookie('username', username_input.value, 30);
      AjaxRequest.post({
        'url':'TODO',
        'parameters': {
          'request_type': request_type,
          'parent': id,
          'username': username_input.value,
          'contents': contents_input.value,
        },
        'timeout':10000, 'onTimeout':function () {
          alert('Oops! The server didn\'t reply in time. Maybe trying again will help.');
          preview_button.removeAttribute('disabled');
          submit_button.removeAttribute('disabled');
        },
        'onError': function (req) {
          alert('Oops! The request returned status "'+req.statusText+'". I don\'t know what\'s going on.');
          preview_button.removeAttribute('disabled');
          submit_button.removeAttribute('disabled');
        },
        'onSuccess': function(req) {
          preview_space.innerHTML = req.responseText;
          if (request_type == 'preview') {
            if (!previewed) {
              previewed = true;
              elem.appendChild(submit_button);
            }
            preview_button.removeAttribute('disabled');
            submit_button.removeAttribute('disabled');
          }
          else {
            alert ('You\'ve submitted your comment! It\'s not visible to other users yet, but it probably will be soon, after I notice it and confirm that it\'s not obvious spam or harassment or something.')
          }
        }
      });
    }
  }
  add_event_listener(preview_button, 'click', action('preview'));
  add_event_listener(submit_button, 'click', action('submit'));
  elem.appendChild(preview_button);
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

def date_to_string(d):
  return d.strftime("%Y-%m-%d")
def string_to_date(d):
  return datetime.datetime.strptime(d, "%Y-%m-%d").date()

def convert_for_json(posts_metadata, modify_date):
  result = copy.deepcopy(posts_metadata)
  for k in result:
    if "date_modified" in result[k]:
      result[k]["date_modified"] = modify_date(result[k]["date_modified"])
    if "date_posted" in result[k]:
      result[k]["date_posted"] = modify_date(result[k]["date_posted"])
  return result

def encode_for_json(posts_metadata):
  return convert_for_json(posts_metadata, date_to_string)
def decode_for_json(posts_metadata):
  return convert_for_json(posts_metadata, string_to_date)


comment_ids_by_parent = {}
comments_by_id = {}
posts_metadata = {}
try:
  with open("posts_metadata.json", "r", encoding='utf-8') as p:
    posts_metadata = decode_for_json(json.load(p))
except(IOError):
  posts_metadata = {}

def hash_for_testing_equality(x):
  return hashlib.sha384(
    json.dumps(x, sort_keys=True, separators=(',', ':')).encode('utf-8')
  ).hexdigest()

def remember_post_dict_entry(index, metadata, post_dict):
  """
  Returns True if we had to change the metadata to
  update it for new or changed post_dict data.
  """
  if index in post_dict:
    remembered_data_hash = None
    if "remembered_"+index in metadata:
      remembered_data_hash = metadata["remembered_"+index]
    current_data_hash = hash_for_testing_equality(post_dict[index])
    if current_data_hash != remembered_data_hash:
      metadata["remembered_"+index] = current_data_hash
      metadata["date_modified"] = datetime.date.today()
      return True
  return False

print("TODO: only update date posted(/modified?) when actually deploying the page, not building previews")

def post_metadata(post_dict):
  changed_metadata = False
  if post_dict["title"] not in posts_metadata:
    posts_metadata[post_dict["title"]] = {
      "id": (post_dict["force_id"] if ("force_id" in post_dict) else hex(random.SystemRandom().getrandbits(128))[2:-1]),
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
  if ("force_id" in post_dict) and (metadata["id"] != post_dict["force_id"]):
    metadata["id"] = post_dict["force_id"]
    changed_metadata = True
  if ("force_date" in post_dict) and (metadata["date_posted"] != post_dict["force_date"]):
    metadata["date_posted"] = post_dict["force_date"]
    changed_metadata = True
  
  if changed_metadata:
    json.dump(
      encode_for_json(posts_metadata),
      open("posts_metadata.json", "w", encoding='utf-8'),
      indent=True,
      sort_keys=True
      )
  
  return metadata


for comment in comments.comments:
  comments_by_id[comment["id"]] = comment
for comment in comments.comments:
  if comment["parent"] not in comment_ids_by_parent:
    comment_ids_by_parent[comment["parent"]] = []
  comment_ids_by_parent[comment["parent"]].append(comment["id"])

def date_posted (post):
  return post_metadata (post) ["date_posted"]
  
def post_permalink(post_dict):
  if "parent_story" in post_dict:
    return "/stories/"+utils.format_for_url(post_dict["parent_story"])+"/discussion"
  return post_dict["path_prefix"]+url_formatted_title(post_dict)

def date_stringify(d):
  #d.strftime("%B %-d, %Y")
  # %- isn't available on Windows, so:
  return re.sub('(?<= )0(?=[0-9])', '', d.strftime("%B %d, %Y"))

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
          <div class="comment_header"><strong>'''+child["username"]+'</strong>'+utils.inline_separator+date_stringify(child["date_posted"])+utils.inline_separator+'<a href="#'+child_id+'">Permalink</a><span class="reply_to_comment">'+utils.inline_separator+'''<a href="javascript:;" id="make_reply_button_'''+child_id+'''">Reply</a></span></div>
          '''+blog_server_shared.postprocess_post_string(child["contents"], child_id, None, False)[0]+'''
        </div>
        <div class="make_reply_box" id="make_reply_box_'''+child_id+'''"></div>
      </div>
    </div>
    '''+chtml+'''
  </div>
</article>''')
  return (num, put_in_hover_boxes(html_list))

def comments_section(parent):
  (cnum, chtml) = do_comments(parent, True)
  return '''
<section>
  <div class="comments_section" id="comments">
    '''+('<h2 class="comments_title">Comments</h2>' if (cnum > 0) else '')+'''
    <div class="all_comments" name="all_comments" id='''+parent+'''>'''+chtml+'''</div>
  </div>
  <a href="javascript:;" class="direct_comment" id="make_reply_button_'''+parent+'''">Leave a comment</a>
  <div class="make_reply_box" id="make_reply_box_'''+parent+'''"></div>
</section>'''

def hidden_cw_box(contents):
  return '''<div class="hidden_cw_box">
    <a href="javascript:;" name="enable_content_notices_button" class="reveal_cw_button">Reveal content warnings</a>
    <div class="hidden_cws">
      '''+contents+'''
      <a name="disable_content_warnings_button" href="javascript:;" >(disable content warnings)</a>
    </div>
  </div>'''

def secondary_hidden_cw_box(contents):
  return '''<div class="hidden_cw_box secondary">
    '''+contents+'''
    <a name="disable_content_warnings_button" href="javascript:;" >(disable content warnings)</a>
  </div>'''

def post_dict_html(post_dict, stream_only = False):
  return post_html(post_dict["contents"], post_dict["title"], post_permalink(post_dict), post_dict["tags"] if "tags" in post_dict else None, "story" if post_dict["category"] == "stories" else stream_only, post_metadata(post_dict), post_dict["category"] != "stories")

def stream_entry (post):
  if "contents" in post:
    if post ["category"] == "stories":
      return '''
<div class="blog_post">
  <div class="post_content_section">New story: <a href="'''+ post_permalink (post) + '">' + post ["title"] + '''</a></div>
</div>'''
    else:
      return post_dict_html (post, True)
  else:
    return '''
<div class="blog_post">
  <div class="post_content_section">New comic page: <a href="'''+ comics.page_url  (post) + '">' + post ["title"] + '''</a></div>
</div>'''


def post_html(contents, title, permalink, taglist, stream_only, metadata, scrutinize = True):
  post_content = blog_server_shared.postprocess_post_string(contents, metadata["id"], title, False, scrutinize)[0]
  
  
  content_warning_header_regex = re.compile(r"<content_warning_header"+blog_server_shared.grouped_string_regex("content_warning_header_contents")+">", re.DOTALL)
  post_content = content_warning_header_regex.sub(lambda match: ('''

<div class="story_content_warning_header">
  <p>This story contains:</p>
  '''+hidden_cw_box('''
  <ul>
    '''+match.group("content_warning_header_contents")+'''
  </ul>
  <p>Notices will also appear in-context in the story, just before the material appears.</p>
  <p>If you see other material that should be marked (such as common triggers or phobias), '''+exmxaxixl.a('e-mail me')+'''. I am serious about web accessibility, and I will respond to your concerns as soon as I can manage.</p>
  ''')+'''
</div>'''), post_content)

  content_warning_p_regex = re.compile(r"<content_warning_p"+blog_server_shared.grouped_string_regex("content_warning_p_contents")+">", re.DOTALL)
  post_content = content_warning_p_regex.sub(lambda match: secondary_hidden_cw_box('This section depicts '+match.group("content_warning_p_contents")+'.'), post_content)
  
  if stream_only == True:
    cutter = re. compile ( r"<cut>.*?</p>.*$", re.DOTALL)
    post_content = cutter.sub ('''[...]</p>
<a class="continue_reading" href="'''+ permalink +'''">Continue reading<span class="invisible"> '''+ title +'''</span></a>''', post_content)
  else:
    post_content = re.sub ("<cut>", "", post_content)
  
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
</div>'''+metadata_and_comments_section_html(permalink, taglist, stream_only, metadata)

def metadata_and_comments_section_html(permalink, taglist, stream_only, metadata):
  comments_stuff = ""
  if stream_only == "story":
    comments_stuff = '''<a href="'''+permalink+'''/discussion" class="direct_comment">Author's notes and comments</a>'''
  elif stream_only == False:
    comments_stuff = comments_section(metadata["id"])
  else:
    (cnum, chtml) = do_comments(metadata["id"], True)
    comments_stuff = utils.inline_separator+'<a href="'+permalink+'#comments">Comments&nbsp;('+str(cnum)+')</a>'
  
  tags_str = ''
  if taglist:
    tags_str = 'Tags: '+(", ".join(tags.tag_link(tag) for tag in taglist))+utils.inline_separator
  date_str = date_stringify(metadata["date_posted"])+utils.inline_separator
  if metadata["date_modified"] != metadata["date_posted"]:
    date_str = 'Posted '+date_stringify(metadata["date_posted"])+utils.inline_separator+'Last updated '+date_stringify(metadata["date_modified"])+utils.inline_separator
  
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
  <div class="comments_section">
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
  <div><img role="presentation" alt="" class="background" src="/media/colorful-background.jpg?rr" /></div>
  '''+bars.bars_wrap({"blog":True}, '''
    <main>
      <div id="content" class="blog_page">
        <div class="blog_page_limits">
          <div class="blog_margin blog_left_margin"></div>
          <div class="blog_stream">'''+main_contents+'''</div>
          <div class="blog_margin blog_middle_margin"></div>
          <div id="blog-sidebar" class="blog_right_bar"><div class="blog_right_bar_inner"><nav>'''+sidebar_contents+'''</nav></div></div>
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

posts_by_tag = {}
for tag in tags.tags:
  posts_by_tag[tag] = []
for post_dict in blog_posts.posts ["blog"]:
  if "tags" in post_dict:
    for tag in post_dict["tags"]:
      posts_by_tag[tag].append(post_dict)

page_lists = {}
def make_page_list (posts):
  result = []
  fixed_pages = max (0, (len (posts) - latest_page_max_posts + page_length - 1)//page_length)
  for page_number in range (0, fixed_pages):
    result.append ([posts [i] for i in range (page_number*page_length, page_number*page_length + page_length - 1)])
  if len(posts) >0:
    result.append ([posts [i] for i in range (fixed_pages*page_length, len(posts))])
  return result
  
page_lists ["blog"] = make_page_list (blog_posts.posts ["blog"])
for tag in tags.tags:
  page_lists [tag] = make_page_list (posts_by_tag [tag])

def sidebar_with_entries (index_entries, header):
  index = ('<div class="blog_index">'
      + header
      +("\n".join(index_entries))
      +'</div>')
  return '<a class="random_post sidebar_standalone_link" id="random_post"></a>'+index

def page_list_sidebar (page_list, header, tags_string = ""):
  index_entries = []
  for page_number in range (len(page_list) - 1,-1,-1):
    page = page_list [page_number]
    if page_number <len( page_list) - 1:
      index_entries.append('<div class="index_page_entry"><a href="/blog'+tags_string+'/page/'+str(page_number + 1 )+'">'+ date_stringify (post_metadata (page [0]) ["date_posted"]) + ' &ndash; ' + date_stringify (post_metadata (page [len( page) - 1]) ["date_posted"]) +'</a></div>')
    for i in range (len(page) - 1, - 1, - 1):
      post_dict = page [i]
      index_entries.append(index_entry_html(post_dict))
  return sidebar_with_entries (index_entries, header)

sidebars = {}
sidebars [""] = ""
sidebars ["stories"] = sidebar_with_entries ([index_entry_html (post) for post in blog_posts.posts ["stories"]],'<a href="/stories">All stories</a>:')
sidebars ["blog"] = page_list_sidebar (page_lists ["blog"], '<a href="/blog">All blog posts</a>:')
for tag in tags.tags:
  tags_string ='/tags/'+utils.format_for_url(tag)
  sidebars [tag] = page_list_sidebar (page_lists[tag], '<a href="/blog'+tags_string+'">'+ tags.tags [tag] +'</a>:', tags_string)
#for category, posts in blog_posts.posts.items ():

current_blog_page = page_lists ["blog"] [len (page_lists ["blog"])-1]
current_blog_page_extras = []
def consider_list_for_current_page (list):
  for index in range (1, min (8, 1 + len( list))):
    post = list [len( list) - index]
    if date_posted (post) >= date_posted (current_blog_page [0]):
      current_blog_page_extras.append (post)
      
for list in comics.comics_pages.values ():
  consider_list_for_current_page (list)
consider_list_for_current_page (blog_posts.posts ["stories"])
current_blog_page_extras.reverse ()
current_blog_page = sorted (current_blog_page_extras + current_blog_page, key = date_posted)
page_lists ["blog"] [len (page_lists ["blog"])-1] = current_blog_page

def add_list_pages (page_dict, page_list, prefix, title, identifier):
  for page_number in range (0,len( page_list)):
    page = page_list [page_number]
    if page_number ==len( page_list) - 1:
      url_pagenum_string = ''
    else:
      url_pagenum_string = '/page/'+str(page_number + 1)
      
    for page_order in ('','/chronological'):
          end_links = ''
          if page_number > 0:
            end_links = (end_links+'<a href="'+ prefix+'/page/'+str(page_number)+page_order+
              '" rel="prev" class="blog_end_link nav">Older posts</a>')
          if page_number <len( page_list) - 1:
            end_links = (end_links+'<a href="'+ prefix +('/page/'+str(page_number+2)+page_order if (page_number <len( page_list) - 2) else page_order)+
              '" rel="next" class="blog_end_link nav right">Newer posts</a>')
          
          if (page_number >0) or ((page_order != '/chronological') and (len(page) > 1)):
            page_string = ""
            if len (page_list) >1:
              page_string = "/page/1"            
            label = "Read in chronological order"
            
            if page_number > 0:
              label = "Go back to the beginning and read in chronological order"
            end_links = end_links+'''
  <div class="blog_end_links_2">
    <a class="blog_end_link" href="'''+ prefix + page_string +'''/chronological">''' + label + '''</a>
  </div>'''

          utils.checked_insert(page_dict,
            prefix +url_pagenum_string+page_order+'.html',
            html_pages.make_page(
              title +" ⊂ Eli Dupree's website",
              "",
              make_blog_page_body("\n".join(['<article>'+ stream_entry (post_dict)+'</article>' for post_dict in (page if page_order == "/chronological" else reversed(page))]) +end_links, sidebars [identifier])
            )
          )

def add_individual_post_pages (page_dict, post_dict):
      category =post_dict ["category"]
      specific_sidebar_contents = sidebars [category]
      if category == "stories":
        specific_sidebar_contents = '''<a class="sidebar_standalone_link" href="'''+post_permalink(post_dict)+'''/discussion">Author's notes and comments for '''+post_dict["title"]+'''</a>'''+ specific_sidebar_contents
      
      utils.checked_insert(page_dict,
        post_dict["path_prefix"]+url_formatted_title(post_dict)+'.html',
        html_pages.make_page(
          title_formatted_title(post_dict)+("" if (category == "") else " ⊂ "+utils.capitalize_string(category))+" ⊂ Eli Dupree's website",
          "",
          "<script>window.elidupree.handle_content_warnings('"+post_dict["title"]+"', false)</script>"+make_blog_page_body(post_dict_html(post_dict), specific_sidebar_contents)
        )
      )
        
      if category == "stories":
        disc_specific_sidebar_contents = '''<a class="sidebar_standalone_link" href="'''+post_permalink(post_dict)+'''">Return to '''+post_dict["title"]+'''</a>'''+sidebars [category]
        discussion_post = {
          "title": post_dict["title"]+": Discussion",
          "contents": '''<p>If you haven't read <a href="'''+post_permalink(post_dict)+'''">'''+post_dict["title"]+'''</a> yet, you should do that before reading further.</p>'''+(post_dict["authors_notes"] if "authors_notes" in post_dict else "<p>There are no author's notes yet.</p>"),
          "parent_story": post_dict["title"],
          "category": "" # Not treated as a story.
        }
        utils.checked_insert(page_dict,
          post_dict["path_prefix"]+url_formatted_title(post_dict)+'/discussion.html',
          html_pages.make_page(
            title_formatted_title(discussion_post)+" ⊂ "+utils.capitalize_string(category)+" ⊂ Eli Dupree's website",
            "",
            make_blog_page_body(post_dict_html(discussion_post), disc_specific_sidebar_contents)
          )
        )

#hack: this is supposed to appear at the end of blog_posts.py
for cat,post_list in blog_posts.posts.items():
  for post_dict in post_list:
    post_dict["category"] = cat
    
def add_pages(page_dict):
  add_list_pages(page_dict, page_lists ["blog"], "/blog", "Blog", "blog")
  for tag in tags.tags:
    tags_string ='/tags/'+utils.format_for_url(tag)
    add_list_pages (page_dict, page_lists [tag], "/blog" + tags_string, tags.tags [tag], tag)


  for cat,post_list in blog_posts.posts.items():
    for post_dict in post_list:
      add_individual_post_pages (page_dict, post_dict)

