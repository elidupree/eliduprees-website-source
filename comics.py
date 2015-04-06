#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

import re
import utils
import css
import javascript

sideways_space = 20
min_transcript_width = 320
max_transcript_width = 500

css.insert('''
div.comic_content_notice_box {
  height: 100%; }
body.content_notices_disabled div.comic_content_notice_box {
  height: auto; }
body.content_notice_dismissed div.comic_content_notice_box {
  height: auto; }
div.comic_content_notice_text {
  margin: 0 auto;
  padding: 6.5em 0;
  font-family: Arial, Helvetica, sans-serif;
  text-align: center; }
.content_notices_disabled div.comic_content_notice_text {
  display: none; }
.content_notice_dismissed div.comic_content_notice_text {
  display: none; }
div.comic_content_notice_main_text {
  font-size: 120%;
  margin: 0 auto;
  max-width: 35em;
  border: 3px solid white;
  border-radius: 2em; }
div.comic_content_notice_details {
  margin: 0 auto;
  max-width: 35em; }
a.dismiss_content_notice {
  display: block;
  font-size: 200%;
  margin-top: 0.6em;
  padding: 0.15em;
  font-weight: bold; }

a.disable_content_notices {
  font-family: Arial, Helvetica, sans-serif;
  display: block;
  padding: 0.5em; }
body.content_notices_disabled a.disable_content_notices {
  display: none; }
div.comic_box_after_content_notice {
  position: relative; }
div.comic_toggle_content_notices {
  margin-top: 1em;
  text-align: center; }
.remove_if_content_notices_enabled {
  display: none; }
body.content_notices_disabled .remove_if_content_notices_enabled {
  display: block; }
body.content_notices_disabled .remove_if_content_notices_disabled {
  display: none; }
  
div.comic_and_nav {
  margin: 2em auto; }
div.comic_and_transcript {
  margin: 5em 0; }
div.comic_image {
  padding-bottom: 3em;
  display: inline-block; }

div.comic_transcript_inner {
  padding: 0 '''+str(sideways_space)+'''px;
  font-family: Arial, Helvetica, sans-serif; }
div.comic_transcript_label {
  padding-bottom: 1.1em; }
.show_comic_transcript_button {
  display: none; }
.transcripts_hidden .show_comic_transcript_button {
  display: inline; }
.transcripts_hidden .hide_comic_transcript_button {
  display: none; }
  
.transcripts_hidden div.comic_transcript_box { min-height: 0; }
.transcripts_hidden p.comic_transcript_line { display: none; }
p.comic_transcript_line {
  margin: 0;
  padding-bottom: 0.9em;
  line-height: 1.2em; }

div.comic_annotation {
  max-width: 36.75em;
  margin: 3em auto;
}
  
div.comic_nav_bar {
  font-family: Arial, Helvetica, sans-serif; }
div.comic_nav_button {
  display: inline-block;
  text-align: center;
  vertical-align: top; }
div.comic_nav_button a {
  display: block; }
span.comic_nav_button_main {
  display: block;
  font-size: 300%;
  font-weight: bold; }
span.comic_nav_content_notice {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 110%; }
.content_notices_disabled span.comic_nav_content_notice {
  display: none; }
''')


javascript.do_before_body('''
window.elidupree.show_transcript = function() {
  remove_class(document.body, 'transcripts_hidden');
  delete_cookie('transcripts_hidden');
};
window.elidupree.hide_transcript = function() {
  document.body.className += ' transcripts_hidden';
  set_cookie('transcripts_hidden', 'true', 30);
};
window.elidupree.enable_content_notices = function() {
  remove_class(document.body, 'content_notices_disabled');
  delete_cookie('content_notices_disabled');
};
window.elidupree.disable_content_notices = function() {
  document.body.className += ' content_notices_disabled';
  set_cookie('content_notices_disabled', 'true', 30);
};
if (read_cookie('content_notices_disabled')) {
  window.elidupree.disable_content_notices();
}
if (read_cookie('transcripts_hidden')) {
  window.elidupree.hide_transcript();
}
''')
javascript.do_after_body('''
var show_transcript_button   = document.getElementById('show_transcript_button'  );
var hide_transcript_button   = document.getElementById('hide_transcript_button'  );
var hide_transcript_button_2 = document.getElementById('hide_transcript_button_2');
if (show_transcript_button  ) { add_event_listener(show_transcript_button  ,'click',window.elidupree.show_transcript); }
if (hide_transcript_button  ) { add_event_listener(hide_transcript_button  ,'click',window.elidupree.hide_transcript); }
if (hide_transcript_button_2) { add_event_listener(hide_transcript_button_2,'click',window.elidupree.hide_transcript); }
var disable_content_notices_event = function(id) {
  var disable_content_notices_button = document.getElementById(id);
  if (disable_content_notices_button) { add_event_listener(disable_content_notices_button,'click',window.elidupree.disable_content_notices); }
};
var enable_content_notices_event = function(id) {
  var enable_content_notices_button = document.getElementById(id);
  if (enable_content_notices_button) { add_event_listener(enable_content_notices_button,'click',window.elidupree.enable_content_notices); }
};
disable_content_notices_event('disable_content_notices_button_next'    );
disable_content_notices_event('disable_content_notices_button_previous');
disable_content_notices_event('disable_content_notices_button_toggle'  );
 enable_content_notices_event( 'enable_content_notices_button_toggle'  );

var view_the_comic_p = document.getElementById('view_the_comic_p');
if (view_the_comic_p) {
  var dismiss_content_notice_a = document.createElement('a');
  dismiss_content_notice_a.className = 'dismiss_content_notice meta_controls_coloring';
  dismiss_content_notice_a.setAttribute('href','javascript:;');
  dismiss_content_notice_a.appendChild(document.createTextNode('View the comic'));
  view_the_comic_p.replaceChild(dismiss_content_notice_a, view_the_comic_p.firstChild);
  add_event_listener(dismiss_content_notice_a,'click',function() { document.body.className += ' content_notice_dismissed'; });
  
  var disable_content_notices_p = document.getElementById('disable_content_notices_p');
  if (cookies_enabled) {
    var disable_content_notices_a = document.createElement('a');
    disable_content_notices_a.className = 'comic_disable_content_notices meta_controls_coloring';
    disable_content_notices_a.setAttribute('href','javascript:;');
    disable_content_notices_a.appendChild(document.createTextNode('Disable content notices'));
    disable_content_notices_p.replaceChild(disable_content_notices_a, disable_content_notices_p.firstChild);
    add_event_listener(disable_content_notices_a,'click',window.elidupree.disable_content_notices);
  }
  else {
    disable_content_notices_p.firstChild.nodeValue = 'You could disable content notices if you had cookies enabled.'
  }
}
''')

import voldemorts_children_pages
import voldemorts_children
import acobs_pages
import acobs

comics_pages = {
  "voldemorts_children":voldemorts_children_pages.vc_pages,
  "acobs":acobs_pages.acobs_pages,
}
comics_metadata = {
  "voldemorts_children": {
    "title": "Voldemort's Children",
    "body_class": "voldemorts_children",
    "url": "/voldemorts-children",
    "abbr": "VC",
    "image_width": 750,
    "dialogue_name_replacements":voldemorts_children.dialogue_name_replace,
    "image_url_offset":0,
  },
  "acobs": {
    "title": "A Couple of Badass Superheroes",
    "body_class": "acobs",
    "url": "/a-couple-of-badass-superheroes",
    "abbr": "ACOBS",
    "image_width": 545,
    "dialogue_name_replacements":{},
    "image_url_offset":1,
  },
}

for comic_id,page_list in comics_pages.items():
  for i in range(0,len(page_list)):
    page_list[i]["comic_id"] = comic_id
    page_list[i]["title"] = comic_id+"_page_"+str(i) # hack only used by post_metadata() as a unique identifier
    page_list[i]["list_index"] = i
    page_list[i]["height_conversion_factor"] = 1
for page_dict in comics_pages["voldemorts_children"]:
  page_dict["height_conversion_factor"] = 4

def page_url(page):
  return comics_metadata[page["comic_id"]]["url"]+('' if page["list_index"] == 0 else '/'+str(page["list_index"]))

def comic_image_url(page):
  meta = comics_metadata[page["comic_id"]]
  return '/media/'+meta["abbr"]+'_'+str(page["list_index"]+meta["image_url_offset"])+'.png'

def comic_thumbnail_url(page):
  return '/media/'+comics_metadata[page["comic_id"]]["abbr"]+'_'+str(page["list_index"])+'_thumbnail.png'

def last_comic_thumbnail_url():
  return comic_thumbnail_url(comics_pages["voldemorts_children"][len(comics_pages["voldemorts_children"]) - 1])

def recent_page_link(deduction):
  page = comics_pages["voldemorts_children"][len(comics_pages["voldemorts_children"]) - 1 - deduction]
  return '<a class="recent_update" href="'+page_url(page)+'"><div class="recent_update_outer"><div class="recent_update"><img src="'+comic_thumbnail_url(page)+'" alt="" /> '+comics_metadata[page["comic_id"]]["title"]+', page '+str(page["list_index"])+'</div></div><div class="recent_update_end"></div></a>'


def do_css_for_comic(comic_id):
  comic_width = comics_metadata[comic_id]["image_width"]
  ancestor_str = 'body.'+comics_metadata[comic_id]["body_class"]
  transcript_at_side_width = comic_width + 3*sideways_space + min_transcript_width
  transcript_maximized_width = comic_width + 3*sideways_space + max_transcript_width
  comics_metadata[comic_id]["transcript_at_side_width"] = transcript_at_side_width
  navbut_outer_margin = comic_width // 10
  navbut_inner_margin = comic_width // 15
  navbut_wid = (comic_width - navbut_outer_margin*2 - navbut_inner_margin*2) // 2
  css.insert('''
'''+ancestor_str+''' div.comic_and_nav {
  width: '''+str(comic_width)+'''px; }
'''+ancestor_str+''' div.comic_image {
  width: '''+str(comic_width)+'''px; }
'''+ancestor_str+''' img.comic_image {
  width: '''+str(comic_width)+'''px; }
  
'''+ancestor_str+''' div.comic_nav_bar {
  width: '''+str(comic_width)+'''px; }

'''+ancestor_str+''' div.comic_transcript_outer {
  width: '''+str(comic_width)+'''px; }
  
@media screen and (min-width: '''+str(transcript_at_side_width)+'''px) {
  '''+ancestor_str+''' div.comic_and_nav {
    width: auto;
    padding-left: '''+str(sideways_space)+'''px; }
  '''+ancestor_str+''' div.comic_image {
    padding-bottom: 0;
    margin-right: -'''+str(comic_width)+'''px; }
  '''+ancestor_str+''' div.comic_transcript_outer {
    display: inline-block;
    vertical-align: top;
    width: auto;
    margin-left: '''+str(comic_width)+'''px; }
  '''+ancestor_str+'''.transcripts_hidden div.comic_and_nav {
    width: '''+str((transcript_at_side_width+comic_width)/2)+'''px;
    padding-left: '''+str((transcript_at_side_width-comic_width)/2)+'''px; }
  '''+ancestor_str+'''.transcripts_hidden div.comic_transcript_outer {
    width: '''+str((transcript_at_side_width-comic_width)/2)+'''px; }
}
@media screen and (min-width: '''+str(transcript_maximized_width)+'''px) {
  '''+ancestor_str+''' div.comic_and_nav {
    width: '''+str(transcript_maximized_width)+'''px; }
  '''+ancestor_str+''' div.comic_transcript_outer {
    width: '''+str(transcript_maximized_width-comic_width)+'''px; }
}

'''+ancestor_str+''' div.comic_annotation_outer {
  width: '''+str(comic_width)+'''px;
}
'''+ancestor_str+''' div.comic_nav_button {
  width: '''+str(navbut_wid)+'''px; }
'''+ancestor_str+''' div.comic_nav_button.prev {
  margin-left: '''+str(navbut_outer_margin)+'''px;
  margin-right: '''+str(navbut_inner_margin)+'''px; }
'''+ancestor_str+''' div.comic_nav_button.next {
  margin-left: '''+str(navbut_inner_margin)+'''px;
  margin-right: '''+str(navbut_outer_margin)+'''px; }
''')

for comic_id,page_list in comics_pages.items():
  do_css_for_comic(comic_id)

import top_bar
import bars
import html_pages
  
def content_notice_bars_wrap(info, notice, html):
  return '''<a class="skip" href="#footer">Skip to footer</a>
<div class="comic_content_notice_box">
  '''+top_bar.top_bar(info)+'''
  <section>
    <div class="comic_content_notice_text">
      <div class="comic_content_notice_main_text">
        <p>The comic below '''+notice+'''</p>
        <p id="view_the_comic_p">Scroll down to view the comic.</p>
      </div>
      <div class="comic_content_notice_details">
        <p id="disable_content_notices_p">You could disable content notices if you had Javascript and cookies enabled.</p>
      </div>
    </div>
  </section>
</div>
<div class="comic_box_after_content_notice">
  <div class="bars_inner_box">
    '''+html+'''
  </div>
  '''+bars.bottom_bar(info)+'''
</div>'''

def bars_wrap(info, html, page):
  return (content_notice_bars_wrap({"comics":True}, page["content_notice"], html) if "content_notice" in page else
                    bars.bars_wrap({"comics":True},                         html))


def comic_navbar(prev_page, next_page):
  def inner_link(string, big_string, page):
    if not page:
      return ''
    return (
    '<a id="'+string+'" class="comic_nav_button" rel="'+string+'" href="'+page_url(page)+'">'
      +('' if "content_notice" not in page else '<span class="comic_nav_content_notice bigger">The '+big_string+' page '+page["content_notice"]+'</span>')
      +'<span class="comic_nav_button_main">'+utils.capitalize_string(big_string)+'</span></a>'
    +('' if "content_notice" not in page else '<a id="disable_content_notices_button_'+big_string+'" class="comic_disable_content_notices meta_controls_coloring" href="javascript:;">(disable content notices)</a>'))
  def link(string, big_string, page):
    return '<div class="comic_nav_button '+string+(' content_notice' if (page and ("content_notice" in page)) else '')+'">'+inner_link(string, big_string, page)+'</div>'
  return '<div class="comic_nav_bar">'+link("prev","previous",prev_page)+link("next","next",next_page)+'</div>'



def format_transcript_line(page, line_text):
  dialogue_name_replace = comics_metadata[page["comic_id"]]["dialogue_name_replacements"]
  classes = ['comic_transcript_line']
  match = re.match("([A-Z ]+): ", line_text)
  if match:
    classes.append("dialogue")
    if match.group(1) in dialogue_name_replace:
      entry = dialogue_name_replace[match.group(1)]
      classes.append(match.group(1) if entry is True else entry)
  return '<p class="'+(' '.join(classes))+'">'+line_text+'</p>'

def format_transcript_recur(page, entries, wide_screen_rules_list):
  if len(entries) == 0:
    return ''
  else:
    line_info = entries[len(entries) - 1]
    height_num_str = str(line_info[0] // page["height_conversion_factor"])
    wide_screen_rules_list.append('.comic_transcript_box.px'+height_num_str+' { min-height: '+height_num_str+'px }')
    return '<div class="comic_transcript_box px'+height_num_str+'">'+format_transcript_recur(page, entries[0:len(entries) - 1], wide_screen_rules_list)+'</div>'+line_info[1]

def format_transcript(page, wide_screen_rules_list):
  entries = [(0, '<div class="comic_transcript_label">Transcript: <a href="javascript:;" class="meta_controls_coloring"><span id="hide_transcript_button" class="hide_comic_transcript_button">(hide)</span><span id="show_transcript_button" class="show_comic_transcript_button">(show)</span></a></div>')]
  entries.extend([(a, format_transcript_line(page, b)) for (a, b) in page["transcript"]])
  return format_transcript_recur(page, entries, wide_screen_rules_list)+'<a id="hide_transcript_button_2" class="hide_comic_transcript_button" href="javascript:;">(hide transcript)</a>'



import blog

def page_html_and_head(page, prev_page, next_page):
  wide_screen_rules_list = []
  navbar = comic_navbar(prev_page, next_page)
  metadata = blog.post_metadata(page)
  return (
    '''
<div class="comic_and_nav">'''
  +navbar+'''
  <div class="comic_toggle_content_notices remove_if_content_notices_disabled">
    Content notices are enabled. <a id="disable_content_notices_button_toggle" class="comic_toggle_content_notices meta_controls_coloring" href="javascript:;">(disable)</a>
  </div>
  <div class="comic_toggle_content_notices remove_if_content_notices_enabled">
    Content notices are disabled. <a id="enable_content_notices_button_toggle" class="comic_toggle_content_notices meta_controls_coloring" href="javascript:;">(enable)</a>
  </div>
  <main>
    <div id="content" class="comic_and_transcript">
      <div class="comic_image">
        '''+('<a tabindex="-1" href="'+page_url(next_page)+'">' if next_page else '')+'''
          <img class="comic_image" alt="A comic page; see below for a transcript" src="'''+comic_image_url(page)+'''" />
        '''+('</a>'                                             if next_page else '')+'''
      </div><!--
   --><div class="comic_transcript_outer">
        <div class="comic_transcript_inner">
          '''+format_transcript(page, wide_screen_rules_list)+'''
        </div>
      </div>
    </div>'''
    +navbar+'''
    <div class="comic_annotation_outer">
      <div class="comic_annotation">
        '''+blog.post_html(page["annotation"], None, page_url(page), None, True, metadata)+'''
      </div>
    </div>
  </main>
</div>''',


  '''
<style type="text/css">
@media screen and (min-width: '''+str(comics_metadata[page["comic_id"]]["transcript_at_side_width"])+'''px) {
  '''+'\n'.join(wide_screen_rules_list)+'''
}
</style>''')


def add_comic_pages(page_dict):
  for comic_id,page_list in comics_pages.items():
    for i in range(0,len(page_list)):
      page = page_list[i]
      prev_page = (page_list[i-1] if i>0 else None)
      next_page = (page_list[i+1] if i+1 < len(page_list) else None)
      prev_page_url = (page_url(prev_page) if prev_page else None)
      next_page_url = (page_url(next_page) if next_page else None)
      html, head = page_html_and_head(page, prev_page, next_page)
      extra_scripts = ''
      if next_page:
        head = head+'<link rel="next prefetch prerender" href="'+next_page_url+'" />\n<link rel="prefetch" href="'+comic_image_url(next_page)+'" />\n'
        extra_scripts = extra_scripts + "if (document.referrer.indexOf('"+page_url(next_page)+"') !== -1) { document.body.className += ' content_notice_dismissed'; }"
      if prev_page:
        head = head+'<link rel="prev prefetch prerender" href="'+prev_page_url+'" />\n<link rel="prefetch" href="'+comic_image_url(prev_page)+'" />\n'
        extra_scripts = extra_scripts + "if (document.referrer.indexOf('"+page_url(prev_page)+"') !== -1) { document.body.className += ' content_notice_dismissed'; }"
      utils.checked_insert(page_dict,
        page_url(page)+'.html',
        html_pages.make_page(
          ('Page '+str(i)+' ⊂ ' if i>0 else '')+comics_metadata[page["comic_id"]]["title"]+" ⊂ Eli Dupree's website",
          head,
          '<script>'+extra_scripts+'''</script>
  <a class="skip" href="#content">Skip to content</a>'''+bars_wrap({"comics":True}, html, page), {"body_class":comics_metadata[comic_id]["body_class"]}
        )
      )

