#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import re
import random
import datetime
import copy
import json
import hashlib
import html

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
comment_indent_width = 1.8
nice_narrow_margin = 2
narrowest_margin = 0.5
post_vertical_separation = 1
post_padded_min_width = 27 #post_content_min_width + (2*text_padding_width)
post_padded_max_width = 45.5 #post_content_max_width + (2*text_padding_width)
right_bar_padded_width = 15 #right_bar_content_width + (2*text_padding_width)
#max_side_space = (page_max_width - post_padded_max_width) / 2
#right_bar_padded_width = max_side_space - 2*(min_side_space_for_post)
#right_bar_content_width = right_bar_padded_width - (2*text_padding_width)

min_space_for_full_post_width = post_padded_max_width+3*nice_narrow_margin+right_bar_padded_width
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

div.stream_media_reference_outer {
  margin-top:'''+str(post_vertical_separation)+'''em;
  text-align: center; }
div.stream_media_reference_outer + div.stream_media_reference_outer {
  margin-top: 0.125em; }
a.stream_media_reference {
  display: block;
  font-weight: bold;
  text-decoration: none;
  background-color: '''+metacontent_color_IE8+''';
  background-color: '''+metacontent_color+''';
  text-align: center;
  display: inline-block;
  padding:0 0.6em;
  border-radius:0.7em;
  height: 1.2em;
  overflow: hidden;
  vertical-align: top; }
a.stream_media_reference img {
  width: 8.2em;

  vertical-align: top; }
a.stream_media_reference:hover {text-decoration: underline;}

div.post_content_section {
  margin-top:'''+str(post_vertical_separation)+'''em;
  padding:'''+str(text_padding_width)+'''em;
  background-color: white; }

div.skip_to_demoted_sidebar {display: none;
  background-color: '''+metacontent_color_IE8+''';
  background-color: '''+metacontent_color+''';
  margin-top:'''+str(post_vertical_separation)+'''em;
  padding:0.6em;
font-weight: bold;
margin-left: 1.5em;
margin-right: 1.5em;
  text-align: center;}

@media screen and (max-width: '''+str(post_padded_max_width+4*nice_narrow_margin+2*right_bar_padded_width)+'''em) {
  div.blog_page_limits { width: 100%; }
}
@media screen and (max-width: '''+str(min_space_for_full_post_width)+'''em) {
  div.blog_stream      { width: auto; }
  div.blog_left_margin { width: '''+str(nice_narrow_margin)+'''em; }
  
  div.blog_post h1 { font-size: 200%;}
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
  
  div.skip_to_demoted_sidebar {display: block;}
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
  font-size: 90%;
  padding: 0.75em;
  background-color:'''+metacontent_color_IE8+''';
  background-color:'''+metacontent_color+'''; }

a.continue_reading {
  display: block;
  text-indent: 2em;
  padding-bottom: 1.2em; }

h2.comments_title {
  font-size: 200%;
  font-weight: bold;
  padding-top: 0.2em;
  text-align: center; }
div.comment_body_outer {
  padding-top:0.5em;
  /*padding-left: '''+str(comment_indent_width)+'''em;*/ }

div.user_comment.indent_children>div.comment_hover_box {  border-left:0.2em solid #333333;
  padding-left:0.4em;
  margin-left: '''+str(comment_indent_width-0.6)+'''em; }
div.comment_body {
  font-size: 111%;
  text-align: left;
  background-color: white;
  padding:0.5em 0.9em; }
div.comment_header {
  padding-bottom: 0.5em; }
span.reply_to_comment {
  display: none; }
html.javascript_enabled span.reply_to_comment {
  display: inline; }
div.make_reply_box {
  padding-left: '''+str(comment_indent_width)+'''em; }
a.direct_comment {
  display: none;
  font-size: 150%;
  font-weight: bold;
  padding-top: 0.4em;
  text-align: center; }
html.javascript_enabled a.direct_comment {
  display: block; }
textarea.make_reply_input {
  width: 90%; }
  
/*div.comments_section:hover>h2.comments_title:not(:hover) {
  border-left: '''+comment_hover_border_width+''' solid red;
  margin-left: -'''+comment_hover_border_width+''';
  border-top-left-radius: 5% 100%; }
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
  margin-left: -'''+str(comment_indent_width)+'''em; }*/

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
  font-size: 90%;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis; }
div.blog_right_bar a {

  text-decoration: none; }
div.blog_right_bar a:hover {
  text-decoration: underline; }
div.index_page_entry {
  font-weight: bold;
  font-family: Arial, Helvetica, sans-serif;
  padding-top: 0.8em; 
  padding-left:0.4em;
padding-bottom:0.1em;   }
a.sidebar_standalone_link {
  padding: 0.4em 0;
  display: block; }
a.random_post {
  display: none; }
a.random_post.enabled {
  display: block; }

a.Patreon_link,.MailChimp_form {
padding: 0.6em 0.8em;

background-color: white;
border-radius:0.6em;
border:0.15em solid #555;
position: relative;}
.blog_right_bar a.Patreon_link, .blog_right_bar .MailChimp_form {
  margin:0.5em -0.65em;}

a.Patreon_link img {
display: inline-block;
margin-right:-2em;
vertical-align: middle;
width:2em; }
a.Patreon_link span {
display: inline-block;
vertical-align: middle;
padding-left:2.4em;}
a.Patreon_link:hover {
background-color:#ff7;
border-color:#442;}
a.Patreon_link:hover span {text-decoration: underline;}

a.blog_Patreon_appeal {
  display: block;
  padding-top: 0.2em;
  padding-bottom: 1.0em;
  padding-left: 1.4em;
  padding-right: 1.4em;
  font-size: 111%;
}

.MailChimp_form input {width: 100%; margin: 0.2em 0;}
.MailChimp_form .button {border: 0 none; border-radius:0.25em; height:  2em; cursor: pointer; transition: all 0.23s ease-in-out 0s; background-color: #777; color: white;}
.MailChimp_form .button:hover {background-color: #444;}

.long_story_navbar {display: flex; justify-content: space-around; align-items: center; padding: 0.2em 0; }
.long_story_navbar>.button {
  font-size: 160%;
  color: #777;
  background-color: #ddd;
  background-image: linear-gradient(to bottom,#fff,#bbb);
  background-repeat: repeat-x;
  padding: 0.1em 0.45em;
  border: 0.05em solid black;
  border-color:#aaa #888 #555 #aaa;
  border-radius: 0.25em;
}
.long_story_navbar>a.button {
  color: black;
  text-decoration: none;
}
.long_story_navbar>a.button:hover {
  background-color: #bbb;
  background-image: linear-gradient(to top,#ddd,#999);
  border-color:#888 #777 #555 #888;
}
@media screen and (max-width: '''+str(min_space_for_full_post_width)+'''em) {
  .long_story_navbar>.button { font-size: 100%; }
}

div.transcript_block {border: 1px solid black;}
div.transcript_header {padding:0.5em;}
div.transcript_content {padding:0.5em; border-top:1px dashed black;}
  
span.inline_quote {background-color:#f0f0f0; color:#404040; border-radius:0.5em; }
a:link span.inline_quote { background-color:#f0f0ff; color:#4040ff; }
a:visited span.inline_quote { background-color:#f8f0f8; color:#804080; }
div.block_quote_outer {margin:0.9em 0;}
blockquote {padding: 0.25em; background-color:#f0f0f0; color:#404040;  margin-left: 2.5em; margin-right: 2.8em; margin-top: 0; margin-bottom: 1em; }
p.reply_input_info { padding-left: 0.5em; }
span.big_quote_mark_outer { width: 2.5em; height: 0; float: left; margin-top: -0.5em; }
span.big_quote_mark_inner { font-size: 5em; color: #d0d0d0; }
div.footnotes { margin-top: 2em; }
a.footnote_link { color: black; }

.scrutiny { background-color: #c0ffff; color: black; text-decoration: underline; }
.skepticism { background-color: #ffc0c0; }

html.restricted_user .hidden_from_restricted_users {display: none;}
''')

javascript.do_before_body (r'''
window.elidupree.transcripts = [];
window.elidupree.handle_transcript = function (ID) {
  var show = function () {
    remove_class (document.documentElement, 'transcript_hidden_' + ID);
    set_cookie ('transcript_shown_' + ID, 'true', 30);
  };
  var hide = function () {
    document.documentElement.className += ' transcript_hidden_'+ ID;
    delete_cookie ('transcript_shown_'+ ID);  
  };
  if (!read_cookie ('transcript_shown_' + ID)) {
    hide ();
  }
  window.elidupree.transcripts.push ([ID, show, hide]);
};
if (read_cookie ('restricted')) {
  document.documentElement.className += ' restricted_user';
}  
''')
javascript.do_after_body(r'''
var comments = document.getElementsByClassName("user_comment");
var all_comments_divs = document.getElementsByClassName("all_comments");
var random_post_link = document.getElementById("random_post");
var randomable_index_entries = document.getElementsByClassName("randomable_index_entry");
var random_entry;
var i;

function handle_transcript (stuff) {
  if (document.getElementById('show_transcript_button_'+ stuff [0])) {
    add_event_listener (document.getElementById('show_transcript_button_'+ stuff [0]), 'click', stuff [1]);
    add_event_listener (document.getElementById('hide_transcript_button_'+ stuff [0]), 'click', stuff [2]);
  }
}
for (i = 0; i < window.elidupree.transcripts.length; ++i) {
  handle_transcript (window.elidupree.transcripts [i]);
}


var do_secret_comment_identifiers = window.cookies_enabled && JSON && window.crypto;
var replace_secret_comment_identifier = function () {
  var array = new Uint32Array(4);
  window.crypto.getRandomValues(array);
  set_cookie ("secret_comment_identifier", JSON.stringify (array), 30);
};
if (do_secret_comment_identifiers &&!read_cookie ("secret_comment_identifier")) {replace_secret_comment_identifier ();}

function expand_reply_box(elem, id) {
  elem.innerHTML = ''+
    '<p class="reply_input_info">'+
      'You may use &lt;em&gt;<em>emphasized text</em>&lt;/em&gt;, &lt;strong&gt;<strong>strongly emphasized text</strong>&lt;/strong&gt;, <br/>&lt;q&gt;<q>Quoted text</q>&lt;/q&gt;, and &lt;blockquote&gt;longer, indented quotes&lt;/blockquote&gt;.'+
    '</p>'+
    'Your name: <input id="reply_username_'+id+'" type="text">'+
    '<textarea id="reply_contents_'+id+'" class="make_reply_input" cols="60" rows="7"></textarea><br/>'+
    '<div id="preview_space_'+id+'" class="preview_space"></div>'+
'';
  var preview_space = document.getElementById('preview_space_'+id);
  var username_input = document.getElementById('reply_username_'+id);
  var contents_input = document.getElementById('reply_contents_'+id);
  username_input.value = read_cookie('username');
  var preview_button = document.createElement("button");
  preview_button.innerHTML = 'Preview your reply';
  var submit_button = document.createElement("button");
  submit_button.innerHTML = 'Submit your reply';
  var previewed = false;
  var action = function(request_type) {
    return function() {
      preview_button.setAttribute('disabled', 'disabled');
      submit_button.setAttribute('disabled', 'disabled');
      set_cookie('username', username_input.value, 30);
      preview_space.innerHTML = "Processing...";
      var secret_string = "unavailable";
      var last_secret_string = "also unavailable";
      if (do_secret_comment_identifiers && request_type === 'submit') {
        last_secret_string = read_cookie ("secret_comment_identifier");
        replace_secret_comment_identifier (); 
        secret_string = read_cookie ("secret_comment_identifier");
      }
      $.post({
        'url': '/_services/comments',
        'timeout':10000,
        'headers': {
          'X-Not-A-Simple-Crossdomain-Request': 'yes',
        },
        'data': {
          'request_type': request_type,
          'parent': id,
          'username': username_input.value,
          'contents': contents_input.value,
          'secret_comment_identifier': secret_string,
          'last_secret_comment_identifier': last_secret_string,
        },
        'error': function (request, status, error) {
          if (status === 'timeout') {
            preview_space.innerHTML ='<p>Oops! The server didn\'t reply in time. Maybe trying again will help.</p>';
          } else {
            preview_space.innerHTML =' <p>Oops! The request returned "'+ status +'", "' + error + '". I regret that I have not prepared a good explanation for this error message.</p>';
          }
          preview_button.removeAttribute('disabled');
          submit_button.removeAttribute('disabled');
        },
        'success': function(text) {
          if (request_type === 'preview') {
            preview_space.innerHTML = ' <p>This is a preview. Your comment is not yet visible to other users.</p>' + text;
            if (!previewed) {
              previewed = true;
              elem.appendChild(submit_button);
            }
            preview_button.removeAttribute('disabled');
            submit_button.removeAttribute('disabled');
          }
          else {
            preview_space.innerHTML = ' <p>You\'ve submitted your comment! It\'s not visible to other users yet, but it probably will be soon, after I notice it and confirm that it\'s not obvious spam or harassment or something.</p>' + text;
          }
        }
      });
    };
  };
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
  setup_reply_box(comments[i].id);
}
for (i = 0; i < all_comments_divs.length; ++i) {
  setup_reply_box(all_comments_divs[i].id);
}
if (random_post_link) {
  random_entry = randomable_index_entries[Math.floor(Math.random()*randomable_index_entries.length)];
  random_post_link.setAttribute("href", random_entry.getAttribute("href"));
  random_post_link.innerHTML = random_post_link.dataset.itemname+random_entry.innerHTML;
  random_post_link.className = random_post_link.className+" enabled";
}

''')

def url_formatted_title(post_dict):
  return utils.format_for_url(post_dict["title"])
def title_formatted_title(post_dict):
  return utils.strip_tags(post_dict["title"])

def date_to_string(d):
  return d.strftime("%Y-%m-%d")
def string_to_date(d):
  return datetime.datetime.strptime(d, "%Y-%m-%d").date()

def convert_for_json(posts_metadata, modify_date):
  result = copy.deepcopy(posts_metadata)
  for k in result:
    result[k]["date_posted"] = modify_date(result[k]["date_posted"])
    result[k]["date_modified"] = modify_date(result[k]["date_modified"])
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


def post_metadata(post_dict):
  changed_metadata = False
  if post_dict["title"] not in posts_metadata:
    date_posted =(post_dict["force_date"] if ("force_date" in post_dict) else datetime.date.today())
    posts_metadata[post_dict["title"]] = {
      "id": (post_dict["force_id"] if ("force_id" in post_dict) else hex(random.SystemRandom().getrandbits(128))[2:-1]),
      "date_posted": date_posted,
      "date_modified": date_posted,
    }
    changed_metadata = True
  metadata = posts_metadata[post_dict["title"]]
  
  import sys
  if "--deploy" in sys.argv: 
    if remember_post_dict_entry("contents", metadata, post_dict):
      changed_metadata = True
    if remember_post_dict_entry("transcript", metadata, post_dict):
      changed_metadata = True
    if remember_post_dict_entry("annotation", metadata, post_dict):
      changed_metadata = True
    if "deployed" not in metadata:
      if "force_date" not in post_dict:
        metadata ["date_posted"] = datetime.date.today ()
        metadata ["date_modified"] = datetime.date.today ()
      else:
        metadata ["date_modified"] = (datetime.date.today () if "edited_significantly_from_old_website" in post_dict else post_dict ["force_date"])
      metadata ["deployed"] = True
      changed_metadata = True
  
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
  if "date_posted" in post:
    return post ["date_posted"]
  return post_metadata (post) ["date_posted"]
  
def post_permalink(post_dict):
  if "stream_entry" in post_dict:
    return post_dict ["stream_entry"] [0]
  if "parent_story" in post_dict:
    return post_permalink(post_dict["parent_story"])+"/discussion"
  if "long_story_name" in post_dict:
    index = post_dict["long_story_index"]
    return blog_posts.long_stories[post_dict["long_story_name"]]["url"]+("" if index == 1 else "/"+str (index))
  return post_dict["path_prefix"]+ (post_dict ["title_url_override"] if "title_url_override" in post_dict else url_formatted_title(post_dict))


def story_discussion_post (post_dict):
  return {
          "title": post_dict["title"]+": Discussion",
          "contents": '''<p>If you haven't read <a href="'''+post_permalink(post_dict)+'''">'''+post_dict["title"]+'''</a> yet, you should do that before reading further.</p>'''+(post_dict["authors_notes"] if "authors_notes" in post_dict else "<p>There are no author's notes yet.</p>"),
          "parent_story": post_dict,
          "category": "" # Not treated as a story.
        }



comment_is_on = {
#hack: these names should probably not be hardcoded here
"hexy":{"canonical_link": "/hexy", "title": "Hexy Bondage"},
"pac_asteroids":{"canonical_link": "/games/pac-asteroids", "title": "Pac-Asteroids"},
"green_caves":{"canonical_link": "/games/green-caves", "title": "the green caves game"},
}
for cat, post_list in blog_posts.posts.items ():
  for post in post_list:
    comment_is_on [post_metadata (post) ["id"]] = {"canonical_link": post_permalink (post), "title": post ["title"]}
    if cat == "stories":
      post = story_discussion_post (post)
      comment_is_on [post_metadata (post) ["id"]] = {"canonical_link": post_permalink (post), "title": post ["title"]}

for cat, post_list in comics.comics_pages.items ():
  for post in post_list:
    comment_is_on [post_metadata (post) ["id"]] = {"canonical_link": comics.page_url (post), "title": post ["title"]}

def comment_stream_entry (comment):
  ancestor = comment
  while ancestor["parent"] in comments_by_id:
    ancestor = comments_by_id [ancestor["parent"] ]
  info = comment_is_on [ancestor["parent"] ]
  return (info ["canonical_link"] + "#" + comment ["id"], comment ["username"] + " posted a new comment on " + info ["title"])
  
def date_stringify(d):
  #d.strftime("%B %-d, %Y")
  # %- isn't available on Windows, so:
  return re.sub('(?<= )0(?=[0-9])', '', d.strftime("%B %d, %Y"))

def put_in_hover_boxes(comment_list):
  if len(comment_list) == 0:
    return ''
  return '<div class="comment_hover_box"><div class="whole_comment_hover_marker">'+comment_list[0]+'</div>'+put_in_hover_boxes(comment_list[1:])+'</div>'

def do_comments(parent, top_level):
  child_ids = comment_ids_by_parent[parent] if parent in comment_ids_by_parent else []
  html_list = []
  num = 0
  for child_id in child_ids:
    (cnum, chtml) = do_comments(child_id, False)
    child = comments_by_id[child_id]
    num = num + cnum + 1
    html_list.append('''
  <div class="user_comment'''+ (' hidden_from_restricted_users' if child ["username"] == "UntamableSpirit" else '') + (' indent_children' if len(child_ids) >1 or (child_id in comment_ids_by_parent and len(comment_ids_by_parent [child_id]) >1) else '') +'''" id="'''+child_id+'''">
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
''')
  return (num, put_in_hover_boxes(html_list))

def comments_section(parent):
  (cnum, chtml) = do_comments(parent, True)
  return '''
  <div class="comments_section" id="comments">
    '''+('<h2 class="comments_title">Comments</h2>' if (cnum > 0) else '')+'''
    <div class="all_comments" id='''+parent+'''>'''+chtml+'''</div>
    <a href="javascript:;" class="direct_comment" id="make_reply_button_'''+parent+'''">Leave a comment</a>
    <div class="make_reply_box" id="make_reply_box_'''+parent+'''"></div>
  </div>
'''


def post_dict_html(post_dict, stream_only = False):
  contents =post_dict["contents"]
  if "long_story_name" in post_dict:
    bar = long_story_navbar (post_dict)
    contents = bar + "<bigbreak>"+ contents + "<bigbreak>"+  bar
  (body, head) = post_html(contents, post_dict["title"], post_permalink(post_dict), post_dict["tags"] if "tags" in post_dict else None, "story" if post_dict["category"] == "stories" else stream_only, post_metadata(post_dict), post_dict["category"] != "stories", allow_comments = ("disallow_comments" not in post_dict), Patreon_type = ("story" if (post_dict["category"] == "stories" or "parent_story" in post_dict) else "blog"))
  if "head" in post_dict:
    head = head + post_dict ["head"]
  return (body, head)  

def very_stream_entry (post):
  if "stream_entry" in post:
    (URL, contents) = post ["stream_entry"]
  elif "username" in post:
    (URL, contents) = comment_stream_entry (post)
  elif "contents" in post:
    (URL, contents) = (post_permalink (post), 'New ' + ("story" if post ["category"] == "stories" else "blog post") + ': ' + post ["title"]) 
  else:
    (URL, contents) = (comics.page_url(post), '<img src="'+ comics.comic_image_url (post, "thumbnail_full") +'" alt=""> New comic: ' + post ["title"] )
  return '''
<div class="stream_media_reference_outer">
  <a class="stream_media_reference" href="'''+ URL + '">'+ contents + '''</a>
</div>'''

def stream_entry (post):
  if "category" in post and post ["category"] == "blog":
    (body, head) = post_dict_html (post, True)
    return ('<article>'+ body +'</article>', head)
  else:
    return (very_stream_entry (post), "")

def long_story_navbar(post):
  metadata = post_metadata (post)
  index = post["long_story_index"]
  story = blog_posts.long_stories [post["long_story_name"]]
  previous = "&lt; Previous"
  page = story ["pages"] [0]
  first = '<a class="long_story_adjacent button first" href="'+ post_permalink (page)+'">&lt;&lt; First</a>'
  archive = '<a class="long_story_adjacent button" href="'+ post_permalink (page)+'">Archive</a>'
  page = story ["pages"] [len(story ["pages"])-1]
  latest = '<a class="long_story_adjacent button latest" href="'+ post_permalink (page)+'">Latest >></a>'
  
  if index > 1:  
    page = story ["pages"] [index - 2]
    previous = '<a class="long_story_adjacent button previous" href="'+ post_permalink (page)+'">'+previous+'</a>'
  else:
    previous = '<div class="previous button">'+previous+'</div>'
  
  if index < len(story ["pages"]):
    page = story ["pages"] [index]
    next = '<a class="long_story_adjacent next button" href="'+ post_permalink (page)+'">Next ></a>'
  else:
    next = '''<div class="complete_comic">This story is complete. </div>''' if "complete" in metadata else MailChimp_form_labeled ("This is the last chapter so far! Follow elidupree.com by email for future updates:")
    
  page = story_discussion_post (post)
  commentary = '<a class="long_story_adjacent commentary" href="'+ post_permalink (page)+'''">Author's notes and comments for this chapter</a>'''
  
  return '''<div class="long_story_navbar">
  '''+ first +previous +archive+next +latest+'''
</div>'''

def post_html(contents, title, permalink, taglist, stream_only, metadata, scrutinize = True, allow_comments = True, Patreon_type = "blog"):
  head = []
  post_content = blog_server_shared.postprocess_post_string(contents, metadata["id"], title, False, scrutinize)[0]
  
  head.append ("<script>window.elidupree.handle_content_warnings ('"+ metadata ["id"]+"', false)</script>" )

  next_transcript_number = 1
  while True:
    transcript_generator = re.search(r"<transcript"+ blog_server_shared.grouped_string_regex("transcript_text")+">", post_content, re.DOTALL)
    if transcript_generator is None:
      break
    transcript_identifier_string = str(next_transcript_number)+'_'+ metadata ["id"]
    post_content = post_content [0: transcript_generator.start(0)]+'<div id="transcript_'+ transcript_identifier_string+'" class="transcript_block"><div class="transcript_header">Transcript: <a id="show_transcript_button_'+ transcript_identifier_string+'" href="javascript:;">(show)</a><a id="hide_transcript_button_'+ transcript_identifier_string+'" href="javascript:;">(hide)</a></div><div class="transcript_content id'+ transcript_identifier_string+'">'+ transcript_generator.group("transcript_text")+'</div></div>' + post_content [transcript_generator.end(0):]
    head.append('''<style> 
html.transcript_hidden_'''+ transcript_identifier_string +''' div.transcript_content.id'''+ transcript_identifier_string +''' {display: none;}
#show_transcript_button_'''+ transcript_identifier_string +''' {display: none;}
html.transcript_hidden_'''+ transcript_identifier_string +''' #show_transcript_button_'''+ transcript_identifier_string +''' {display: inline;}
html.transcript_hidden_'''+ transcript_identifier_string +''' #hide_transcript_button_'''+ transcript_identifier_string +''' {display: none;}
    </style> 
    <script>
    window.elidupree.handle_transcript ("'''+ transcript_identifier_string +'''");
    </script>''')
    next_transcript_number = next_transcript_number + 1

  if stream_only == True:
    cutter = re. compile ( r"<cut>.*?</p>.*$", re.DOTALL)
    post_content = cutter.sub ('''[...]</p>
<a class="continue_reading" href="'''+ permalink +'''">Continue reading<span class="invisible"> '''+ title +'''</span>...</a>''', post_content)
    #this sometimes cuts off anchors, so make sure fragments point at the canonical URL
    post_content = re.sub ('href="#','href="' + permalink + '#', post_content)
  else:
    post_content = re.sub ("<cut>", "", post_content)
  
  calculate_readability = (stream_only != True)
  if calculate_readability:
    #using the automated readability index
    reference = re.sub(r"\s+", " ", html.unescape (utils.strip_tags (post_content)))
    sentences = len(re.findall (r"\w\w\w.*?[.?!]", reference))
    words = utils.word_count (reference)
    characters = len(re.findall (r"\w", reference))
    if words >0 and sentences >0:
      readability = 4.71*characters/words +0.5 *words/sentences -21.43
      post_content = '<em class="debug"> Approximate readability: ' + "{:.2f}".format (readability) + " ("+ str (characters) + " characters, " + str (words) +  " words, " + str (sentences)  + " sentences, " + "{:.2f}".format (characters/words) + " characters per word, " + "{:.2f}".format (words/sentences) + " words per sentence)</em>" + post_content
  
  post_content_sections = post_content.split("<bigbreak>")
  id_str = ''
  if title:
    id_str = 'id="'+utils.format_for_url(title)+'"'
    post_content_sections[0] = '<h1><a class="post_title_link" href="'''+permalink+'">'+title+'</a></h1>'+post_content_sections[0]
  for i in range(0, len(post_content_sections)):
    post_content_sections[i] = '<div class="post_content_section">'+post_content_sections[i]+'</div>'
  return ('''
<div '''+id_str+''' class="blog_post">
  '''+(''.join(post_content_sections))+'''
</div>'''+metadata_and_comments_section_html(title, permalink, taglist, stream_only, metadata, allow_comments = allow_comments, Patreon_type = Patreon_type), "".join (head))


def metadata_and_comments_section_html(title, permalink, taglist, stream_only, metadata, allow_comments = True, Patreon_type = "blog"):
  specifier = ""
  if title:
    specifier = '<span class="invisible"> for '+ title +'</span>'
  
  comments_stuff = ""
  Patreon_stuff = ""
  
  if allow_comments == False:
    pass
  elif stream_only == "story":
    Patreon_stuff = '''<a class="hidden_from_restricted_users blog_Patreon_appeal" href="https://www.patreon.com/EliDupree"><img class="small_inline_image" src="/media/patreon-logo.png?rr" alt=""> Did you like this story? Consider pledging a few $$$ on Patreon so I can keep putting cool things online for free.</a>'''
    comments_stuff = '''<a href="'''+permalink+'''/discussion" class="direct_comment">Author's notes and comments</a>'''
  elif stream_only == False:
    comments_stuff = comments_section(metadata["id"])
    Patreon_stuff = '''<a class="hidden_from_restricted_users blog_Patreon_appeal" href="https://www.patreon.com/EliDupreeBlog"><img class="small_inline_image" src="/media/patreon-logo.png?rr" alt=""> Are my blog posts helpful to you? Consider pledging a few $$$ on Patreon so I can keep putting cool things online for free.</a>'''
  else:
    (cnum, chtml) = do_comments(metadata["id"], True)
    comments_stuff = utils.inline_separator+'<a href="'+permalink+'#comments">Comments' + specifier + '&nbsp;('+str(cnum)+')</a>'
    
  if stream_only == True or allow_comments == False:
    # note: all disallow-comments posts are metacontent where it also makes sense not to have a Patreon appeal
    pass
  else:
    question = "Are my blog posts helpful to you?"
    which = "EliDupreeBlog"
    if Patreon_type == "story":
      question = '''Did you like this story?'''
      which = "EliDupree"
    elif Patreon_type == "comic":
      question = '''Do you like this comic?'''
      which = "EliDupree"
    elif Patreon_type == "art":
      question = '''Do you like this artwork?'''
      which = "EliDupree"
      
    Patreon_stuff = '''<a class="hidden_from_restricted_users blog_Patreon_appeal" href="https://www.patreon.com/'''+which+'''"><img class="small_inline_image" src="/media/patreon-logo.png?rr" alt=""> '''+question+''' Consider pledging a few $$$ on Patreon so I can keep putting cool things online for free.</a>'''
  
  tags_str = ''
  if taglist:
    tags_str = 'Tags: '+(", ".join(tags.tag_link(tag) for tag in taglist))+utils.inline_separator
  date_str = date_stringify(metadata["date_posted"])+utils.inline_separator
  if metadata["date_modified"] != metadata["date_posted"]:
    date_str = 'Posted '+date_stringify(metadata["date_posted"])+utils.inline_separator+'Last updated '+date_stringify(metadata["date_modified"])+utils.inline_separator
  
  return ('''
<div class="blog_post_metadata_outer">
  <div class="blog_post_metadata">
    '''+ Patreon_stuff +'''
    '''+tags_str+date_str+'<a rel="bookmark" href="'+permalink+'">Permalink' + specifier + '</a>'+
    comments_stuff+'''
  </div>
</div>''')
  
  




def index_entry_html(post_dict):
  # hack so that this can apply to long stories
  if "url" in post_dict:
    url = post_dict["url"]
  else:
    url = post_permalink(post_dict)
  return '<div class="index_entry"><a class="index_entry_link'+("" if "ignore_for_random_post" in post_dict else " randomable_index_entry")+ '" href="'+url+'" title="'+post_dict["title"]+'">'+post_dict["title"]+'</a></div>'


def make_blog_page_body(main_contents, sidebar_contents):
  return '''
  <a class="skip" href="#content">Skip to content</a><a class="skip" href="#blog-sidebar">Skip to blog sidebar</a>
  <div><img role="presentation" alt="" class="background" src="/media/colorful-background.jpg?rr" /></div>
  '''+bars.bars_wrap({"blog":True}, '''
    <div class="skip_to_demoted_sidebar"> <a href="#blog-sidebar"> Skip to index</a> </div>
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

  

def latest_post_preview_text():
  return blog_posts.posts["blog"][-1]["title"]

page_length = 10
latest_page_max_posts = page_length + 5

posts_by_tag = {}
for tag in tags.tags:
  posts_by_tag[tag] = []
for post_dict in blog_posts.posts ["blog"]:
  if "tags" in post_dict:
    for tag in post_dict["tags"]:
      posts_by_tag[tag].append(post_dict)

page_lists = {}
def make_page_list (posts):
  if len(posts) == 0:
    return []
  result = []
  strong_count = 0
  for post in posts:
    if "ignore_for_page_numbering" not in post:
      strong_count = strong_count + 1
  fixed_pages = max (0, (strong_count - latest_page_max_posts + page_length - 1)//page_length)
  index = 0;
  for page_number in range (0, fixed_pages):
    page = []
    page_strong_count = 0
    while True:
      post = posts [index]
      if "deleted" not in post:
        page.append (post)
      # Note: deleted posts DO count in the page numbering so that the pages don't lose their place when I delete old posts
      if "ignore_for_page_numbering" not in post:
        page_strong_count = page_strong_count + 1
      index = index + 1
      if page_strong_count == page_length:
        break
    result.append(page)
  result.append ([posts [i] for i in range (index, len(posts))])
  return result

def MailChimp_form_labeled (label):
  return '''
  <!-- Begin MailChimp Signup Form -->
<div class="MailChimp_form hidden_from_restricted_users">
<form action="//elidupree.us13.list-manage.com/subscribe/post?u=4d65283e4a6612f93da4514e2&amp;id=122f9e2af8" method="post" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
<label>'''+ label +'''	<input type="email" placeholder="Email address…" value="" name="EMAIL" class="required email"></label>
<!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_4d65283e4a6612f93da4514e2_122f9e2af8" tabindex="-1" value=""></div>
    <input type="submit" value="Subscribe" name="subscribe" class="button">
</form>
</div>

<!--End mc_embed_signup-->

'''

MailChimp_form = MailChimp_form_labeled ("Follow elidupree.com by email:")
Patreon_link ='''<a class="sidebar_standalone_link Patreon_link hidden_from_restricted_users" href="https://www.patreon.com/EliDupree"><img src="/media/patreon-logo.png?rr" alt="" /><span>$$$ Encourage me to make more cool stuff! </span></a>'''

page_lists ["blog"] = make_page_list (blog_posts.posts ["blog"])
for tag in tags.tags:
  page_lists [tag] = make_page_list (posts_by_tag [tag])

def sidebar_with_entries (index_entries, header, random_itemname):
  index = ('<div class="blog_index">'
      + header
      +("\n".join(index_entries))
      +'</div>')
  return '''
  <a class="random_post sidebar_standalone_link" id="random_post" data-itemname="''' + random_itemname +'''"></a>
    
  '''+ MailChimp_form + Patreon_link +index

def tag_index_entry(tag):
  text = tag [1]+' ('+str(len(posts_by_tag[tag[0]]))+')'
  return '<div class="index_entry"><a href="'+ tags.tag_url (tag [0]) +'" title="'+ text +'">'+ text + '</a></div>'
tag_index = '<div class="index_page_entry">All tags</div>' + "\n".join ([tag_index_entry(tag) for tag in tags.tags_list])

def page_list_sidebar (page_list, header, tags_string = ""):
  index_entries = []
  for page_number in range (len(page_list) - 1,-1,-1):
    page = page_list [page_number]
    if page_number <len( page_list) - 1:
      index_entries.append('<div class="index_page_entry"><a href="/blog'+tags_string+'/page/'+str(page_number + 1 )+'">'+ date_stringify (post_metadata (page [0]) ["date_posted"]) + ' &ndash; ' + date_stringify (post_metadata (page [len( page) - 1]) ["date_posted"]) +'</a></div>')
    for i in range (len(page) - 1, - 1, - 1):
      post_dict = page [i]
      index_entries.append(index_entry_html(post_dict))
  index_entries.append (tag_index)
  return sidebar_with_entries (index_entries, header, "[Random post] ")

sidebars = {}
sidebars [""] = MailChimp_form + Patreon_link
sidebars ["stories"] = sidebar_with_entries ([blog_posts.stories_index (False)],'<div class=" index_page_entry"><a href="/stories">Stories</a></div>', "[Random story] ")
sidebars ["blog"] = page_list_sidebar (page_lists ["blog"], '<div class=" index_page_entry"><a href="/blog">Latest blog posts</a></div>')
for tag in tags.tags:
  tags_string ='/tags/'+utils.format_for_url(tag)
  sidebars [tag] = page_list_sidebar (page_lists[tag], '<div class=" index_page_entry"><a href="/blog'+tags_string+'">'+ tags.tags [tag] +'</a></div>', tags_string)
#for category, posts in blog_posts.posts.items ():

current_blog_page = page_lists ["blog"] [len (page_lists ["blog"])-1]
current_blog_page_extras = [
{"title": "New online tool for voice practice!", "stream_entry": ("/voice-practice-tool", "New online tool for voice practice!")},
{"title": "New collection of drawings from a studio art class!", "stream_entry": ("/ap-studio-art", "New collection of drawings from a studio art class!")},
{"title": "No blog post today", "stream_entry": ("/", "No blog post today. I have a sore in my mouth, so I can't dictate and/or type enough. I MIGHT post one on Friday if it gets better soon.")},
{"title": "No blog post today-2", "stream_entry": ("/", "No blog post today. I have a sore in my mouth, so I can't dictate and/or type enough.")},
{"title": "No blog post today-3", "stream_entry": ("/", "No blog post AGAIN today. This time I've had throat problems for days. :-(.")},
{"title": "[NSFW] The web version of Hexy Bondage is finished!", "stream_entry": ("/hexy", "[NSFW] The web version of Hexy Bondage is finished!")},
{"title": "No blog post today-4", "stream_entry": ("/", "Today's blog post partially written, but delayed by annoying health issues.")},
{"title": "New online game: The Path!", "stream_entry": ("/games/the-path", "New online game: The Path!")},
]
def consider_list_for_current_page (list, limit = 8):
  for index in range (1, min (1 + limit, 1 + len( list))):
    post = list [len( list) - index]
    ignore = (list == blog_posts.posts ["stories"]) and ("listed" not in post)
    if date_posted (post) >= date_posted (current_blog_page [0]) and not ignore:
      current_blog_page_extras.append (post)
      
#Hack: this code puts comments (and other stuff) AFTER everything else, because a comment on the same day as another post is likely to be a comment ON that post. In the future, maybe we should have a more precise ordering system for recent stream entries, although we never want to store exact times posted, for privacy reasons.
consider_list_for_current_page (comments.comments, 4)
for comic_id, list in comics.comics_pages.items():
  if comic_id != "studio_art":
    consider_list_for_current_page (list)
consider_list_for_current_page (blog_posts.posts ["stories"])
current_blog_page_extras.reverse ()
current_blog_page = sorted (current_blog_page + current_blog_page_extras, key = date_posted)
page_lists ["blog"] [len (page_lists ["blog"])-1] = current_blog_page

def recent_updates (how_many):
  return "".join ([very_stream_entry (post) for post in reversed (current_blog_page)] [0: how_many]);

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

          entries = [stream_entry (post_dict ) for post_dict in (page if page_order == "/chronological" else reversed(page))]
          if page_order != "/chronological" or len (page_list) >1 or len (page) >1:
            utils.make_page (page_dict,
            prefix +url_pagenum_string+page_order,
              title +" ⊂ Eli Dupree's website",
              "".join ([entry [1] for entry in entries]),
              make_blog_page_body("\n".join([entry [0] for entry in entries]) +end_links, sidebars [identifier])
          )

def add_individual_post_pages (page_dict, post_dict):
      category =post_dict ["category"]
      specific_sidebar_contents = sidebars [category]
      if category == "stories":
        specific_sidebar_contents = '''<a class="sidebar_standalone_link" href="'''+post_permalink(post_dict)+'''/discussion">Author's notes and comments for '''+post_dict["title"]+'''</a>'''+ specific_sidebar_contents
      
      (HTML, head) = post_dict_html(post_dict)
      extras = {}
      if "after_body" in post_dict:
        extras ["after_body"] = post_dict ["after_body"]
      if "blurb" in post_dict:
        extras ["blurb"] = post_dict ["blurb"]
      if "blurb_image" in post_dict:
        extras ["blurb_image"] = post_dict ["blurb_image"]
      utils.make_page (page_dict,
        post_permalink(post_dict),
          title_formatted_title(post_dict)+("" if (category == "") else " ⊂ "+utils.capitalize_string(category))+" ⊂ Eli Dupree's website",
          head, make_blog_page_body(HTML, specific_sidebar_contents), extras
      )
        
      if category == "stories":
        disc_specific_sidebar_contents = '''<a class="sidebar_standalone_link" href="'''+post_permalink(post_dict)+'''">Return to '''+post_dict["title"]+'''</a>'''+sidebars [category]
        
        discussion_post = story_discussion_post(post_dict)
        (HTML, head) = post_dict_html(discussion_post)
        utils.make_page (page_dict,
          post_permalink(discussion_post),
            title_formatted_title(discussion_post)+" ⊂ "+utils.capitalize_string(category)+" ⊂ Eli Dupree's website",
            head, make_blog_page_body(HTML, disc_specific_sidebar_contents)
        )
    
def add_pages(page_dict):
  add_list_pages(page_dict, page_lists ["blog"], "/blog", "Blog", "blog")
  for tag in tags.tags:
    tags_string ='/tags/'+utils.format_for_url(tag)
    add_list_pages (page_dict, page_lists [tag], "/blog" + tags_string, tags.tags [tag], tag)


  for cat,post_list in blog_posts.posts.items():
    for post_dict in post_list:
      if "deleted" not in post_dict:
        add_individual_post_pages (page_dict, post_dict)

