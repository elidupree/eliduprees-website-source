#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import re
import utils
import css
import blog
import javascript
from voldemorts_children_pages import vc_pages
import gimp_stuff


vc_content_margin = "4em";
comic_width = 750;
sideways_space = 20;
min_transcript_width = 320;
max_transcript_width = 500;
transcript_at_side_width = comic_width + 3*sideways_space + min_transcript_width;
transcript_maximized_width = comic_width + 3*sideways_space + max_transcript_width;

print('TODO: content_notices_disabled on the big content notices box can make the bottom bar show up in the wrong place on a very tall window')
css.insert('''
div.vc_content_notice_box {
  height: 100%; }
.content_notices_disabled div.vc_content_notice_box {
  height: auto; }
.content_notice_dismissed div.vc_content_notice_box {
  height: auto; }
div.vc_content_notice_text {
  margin: 0 auto;
  padding: 6.5em 0;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
  text-align: center; }
.content_notices_disabled div.vc_content_notice_text {
  display: none; }
.content_notice_dismissed div.vc_content_notice_text {
  display: none; }
div.vc_content_notice_main_text a {
  color: #ffc800; }
div.vc_content_notice_main_text {
  font-size: 120%;
  margin: 0 auto;
  max-width: 35em;
  border: 3px solid white;
  border-radius: 2em; }
div.vc_content_notice_details {
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
  color: #ffc800;
  padding: 0.5em; }
.content_notices_disabled a.disable_content_notices {
  display: none; }
div.vc_box_after_content_notice {
  position: relative; }
  
div.vc_comic_and_nav {
  width: '''+str(comic_width)+'''px;
  margin: 2em auto; }
div.vc_comic_and_transcript {
  margin: 5em 0; }
div.vc_comic {
  padding-bottom: 3em;
  display: inline-block;
  width: '''+str(comic_width)+'''px; }
img.vc_comic {
  width: '''+str(comic_width)+'''px; }
  
div.vc_nav_bar {
  font-family: Arial, Helvetica, sans-serif;
  width: '''+str(comic_width)+'''px; }
div.vc_nav_button {
  display: inline-block;
  color: #ffc800;
  /*background-color: #412f16;
  border-radius: 16px;*/
  width: 250px;
  text-align: center;
  vertical-align: top; }
div.vc_nav_button a {
  display: block; }
span.vc_nav_button_main {
  display: block;
  font-size: 300%;
  font-weight: bold; }
a.vc_nav_button:link{ color: #807059 /*#99994e;*/ /*#7e7e40*/ }
a.vc_nav_button:visited{ color: #804c00; /*#4d6699;*/ /*#40557f*/ }
div.vc_nav_button.content_notice a.vc_nav_button:link{ color: #ccb38f; /*#ffff82;*/ /*#7e7e40*/ }
div.vc_nav_button.content_notice a.vc_nav_button:visited{ color: #cc7900; /*#81abff;*/ /*#40557f*/ }
.content_notices_disabled div.vc_nav_button.content_notice a.vc_nav_button:link{ color: #807059 /*#99994e;*/ /*#7e7e40*/ }
.content_notices_disabled div.vc_nav_button.content_notice a.vc_nav_button:visited{ color: #804c00; /*#4d6699;*/ /*#40557f*/ }
span.vc_nav_content_notice {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 110%; }
.content_notices_disabled span.vc_nav_content_notice {
  display: none; }
div.vc_nav_button.prev {
  margin-left: 75px;
  margin-right: 50px; }
div.vc_nav_button.next {
  margin-left: 50px;
  margin-right: 75px; }

div.vc_transcript_outer {
  width: '''+str(comic_width)+'''px; }
div.vc_transcript_inner {
  /*border: 1px dashed white;*/
  padding: 0 '''+str(sideways_space)+'''px;
  font-family: Arial, Helvetica, sans-serif;
  color:white; }
div.vc_transcript_inner a {
  color: #ffc800; }
div.vc_transcript_label {
  padding-bottom: 1.1em; }
.show_transcript_button {
  display: none; }
.transcripts_hidden .show_transcript_button {
  display: inline; }
.transcripts_hidden .hide_transcript_button {
  display: none; }
  
@media screen and (min-width: '''+str(transcript_at_side_width)+'''px) {
  div.vc_comic_and_nav {
    width: auto;
    padding-left: '''+str(sideways_space)+'''px; }
  div.vc_comic {
    padding-bottom: 0;
    margin-right: -'''+str(comic_width)+'''px; }
  div.vc_transcript_outer {
    display: inline-block;
    vertical-align: top;
    width: auto;
    margin-left: '''+str(comic_width)+'''px; }
  .transcripts_hidden div.vc_comic_and_nav {
    width: '''+str((transcript_at_side_width+comic_width)/2)+'''px;
    padding-left: '''+str((transcript_at_side_width-comic_width)/2)+'''px; }
  .transcripts_hidden div.vc_transcript_outer {
    width: '''+str((transcript_at_side_width-comic_width)/2)+'''px; }
}
@media screen and (min-width: '''+str(transcript_maximized_width)+'''px) {
  div.vc_comic_and_nav {
    width: '''+str(transcript_maximized_width)+'''px; }
  div.vc_transcript_outer {
    width: '''+str(transcript_maximized_width-comic_width)+'''px; }
}

div.vc_annotation_outer {
  width: '''+str(comic_width)+'''px;
}
div.vc_annotation {
  max-width: 36.75em;
  margin: 3em auto;
}
div.vc_annotation .blog_post {
  background-color: #cccccc }
div.vc_annotation .comment_body {
  background-color: #cccccc }
div.vc_annotation div.all_comments:hover div.comment_body {
  background-color: #aaaaaa; }
div.vc_annotation div.user_comment:hover>div.comment_body_hover_marker>*>div.comment_body {
  background-color: #cccccc; }
div.vc_annotation .blog_post_metadata {
  background-color: rgba(204,204,204,.7) }''')
print ("TODO: find a better way to make modified versions of CSS rules")


javascript.do_after_body('''
var show_transcript_button   = document.getElementById('show_transcript_button'  );
var hide_transcript_button   = document.getElementById('hide_transcript_button'  );
var hide_transcript_button_2 = document.getElementById('hide_transcript_button_2');
var show_transcript = function() {
  remove_class(document.body, 'transcripts_hidden');
  delete_cookie('transcripts_hidden');
};
var hide_transcript = function() {
  document.body.className += ' transcripts_hidden';
  set_cookie('transcripts_hidden', 'true', 30);
};
var enable_content_notices = function() {
  remove_class(document.body, 'content_notices_disabled');
  delete_cookie('content_notices_disabled');
};
var disable_content_notices = function() {
  document.body.className += ' content_notices_disabled';
  set_cookie('content_notices_disabled', 'true', 30);
};
var dismiss_content_notice = function() {
  document.body.className += ' content_notice_dismissed';
};
if (read_cookie('content_notices_disabled')) {
  disable_content_notices();
}
if (read_cookie('transcripts_hidden')) {
  hide_transcript();
}
if (show_transcript_button  ) { add_event_listener(show_transcript_button  ,'click',show_transcript); }
if (hide_transcript_button  ) { add_event_listener(hide_transcript_button  ,'click',hide_transcript); }
if (hide_transcript_button_2) { add_event_listener(hide_transcript_button_2,'click',hide_transcript); }
var disable_content_notices_event = function(id) {
  var disable_content_notices_button = document.getElementById(id);
  if (disable_content_notices_button) { add_event_listener(disable_content_notices_button,'click',disable_content_notices); }
};
disable_content_notices_event('disable_content_notices_button_next'    );
disable_content_notices_event('disable_content_notices_button_previous');

var view_the_comic_p = document.getElementById('view_the_comic_p');
if (view_the_comic_p) {
  var dismiss_content_notice_a = document.createElement('a');
  dismiss_content_notice_a.className = 'dismiss_content_notice';
  dismiss_content_notice_a.setAttribute('href','javascript:;');
  dismiss_content_notice_a.appendChild(document.createTextNode('View the comic'));
  view_the_comic_p.replaceChild(dismiss_content_notice_a, view_the_comic_p.firstChild);
  add_event_listener(dismiss_content_notice_a,'click',dismiss_content_notice);
  
  var disable_content_notices_p = document.getElementById('disable_content_notices_p');
  if (cookies_enabled) {
    var disable_content_notices_a = document.createElement('a');
    disable_content_notices_a.className = 'disable_content_notices';
    disable_content_notices_a.setAttribute('href','javascript:;');
    disable_content_notices_a.appendChild(document.createTextNode('Disable content notices'));
    disable_content_notices_p.replaceChild(disable_content_notices_a, disable_content_notices_p.firstChild);
    add_event_listener(disable_content_notices_a,'click',disable_content_notices);
  }
  else {
    disable_content_notices_p.firstChild.nodeValue = 'You could disable content notices if you had cookies enabled.'
  }
}
''')

def vc_navbar(prev_page, next_page):
  def inner_link(string, big_string, page):
    if not page:
      return ''
    return (
    '<a class="vc_nav_button" rel="'+string+'" href="'+vc_page_url(page)+'">'
      +('' if "content_notice" not in page else '<span class="vc_nav_content_notice bigger">The '+big_string+' page '+page["content_notice"]+'</span>')
      +'<span class="vc_nav_button_main">'+utils.capitalize_string(big_string)+'</span></a>'
    +('' if "content_notice" not in page else '<a id="disable_content_notices_button_'+big_string+'" class="disable_content_notices" href="javascript:;">(disable content notices)</a>'))
  def link(string, big_string, page):
    return '<div class="vc_nav_button '+string+(' content_notice' if (page and ("content_notice" in page)) else '')+'">'+inner_link(string, big_string, page)+'</div>'
  return '<div class="vc_nav_bar">'+link("prev","previous",prev_page)+link("next","next",next_page)+'</div>'

def vc_comic_image_url(page):
  return '/media/VC_'+str(page["list_index"])+'.png'

def vc_comic_thumbnail_url(page):
  return '/media/VC_'+str(page["list_index"])+'_thumbnail.png'

def last_vc_comic_thumbnail_url():
  return vc_comic_thumbnail_url(vc_pages[len(vc_pages) - 1])

# these work for either page numbers or pages
def vc_webname_base(page):
  page_number = (page["list_index"] if type(page) is dict else page)
  return 'voldemorts-children'+('' if page_number == 0 else '/'+str(page_number))
def vc_page_url(page):
  return '/'+vc_webname_base(page)
def vc_page_filename(page):
  return vc_webname_base(page)+'.html'
  
def recent_page_link(deduction):
  page = vc_pages[len(vc_pages) - 1 - deduction]
  return '<a class="recent_update" href="'+vc_page_url(page)+'"><div class="recent_update_outer"><div class="recent_update"><img src="'+vc_comic_thumbnail_url(page)+'''" alt="" /> Voldemort's Children, page '''+str(page["list_index"])+'''</div></div><div class="recent_update_end"></div></a>'''

import blog

def vc_page_html_and_head(page, prev_page, next_page):
  wide_screen_rules_list = []
  navbar = vc_navbar(prev_page, next_page) #(vc_navbar(prev_page, next_page) if page["list_index"] != 0 else '')
  metadata = blog.post_metadata(page)
  return (
    '''
<div class="vc_comic_and_nav">'''
  +navbar+'''
  <main>
    <div id="content" class="vc_comic_and_transcript">
      <div class="vc_comic">
        '''+('<a tabindex="-1" href="'+vc_page_url(next_page)+'">' if next_page else '')+'''
          <img class="vc_comic" alt="A comic page; see below for a transcript" src="'''+vc_comic_image_url(page)+'''" />
        '''+('</a>'                                                if next_page else '')+'''
      </div><!--
   --><div class="vc_transcript_outer">
        <div class="vc_transcript_inner">
          '''+format_transcript(page["transcript"], wide_screen_rules_list)+'''
        </div>
      </div>
    </div>'''
    +navbar+'''
    <div class="vc_annotation_outer">
      <div class="vc_annotation">
        <div class="blog_post">
          '''+page["annotation"]+'''
        </div>
        '''+blog.metadata_and_comments_section_html(vc_page_url(page), None, True, metadata)+'''
      </div>
    </div>
  </main>
</div>''',
  '''
<style type="text/css">
@media screen and (min-width: '''+str(transcript_at_side_width)+'''px) {
  '''+'\n'.join(wide_screen_rules_list)+'''
}
</style>''')



# in place of "Disable content notices for this site",
# "You could disable content notices if you had cookies enabled for this site",
# "You could disable content notices if you had Javascript and cookies enabled for this site",

dialogue_50pct_grey = '#8c8c8c'
dialogue_name_replace = {
  "TITLE":True,
  "TONKS":True,"GRANGER":True,"HARRY":True,"VOLDEMORT":True,"DUMBLEDORE":True,"ZABINI":True,"LUNA":True,
  "WIRELESS":True,"LESTRANGE":True,"SNAPE":True,
  "PRESENT HARRY":"HARRY",
  "PRESENT GRANGER":"GRANGER",
  "FUDGE":"grey", "PAST GRANGER":"grey", "MCGONAGALL":"grey", "RON":"grey", "DRACO":"grey",
}
css.insert('''
p.vc_transcript_line {
  margin: 0;
  padding-bottom: 0.9em;
  line-height: 1.2em; }
div.vc_transcript_inner .dialogue { font-weight: bold; }
div.vc_transcript_inner .TITLE { color: #804c00; /*#412f16;*/ }
div.vc_transcript_inner .TONKS { color: #bf98af; /*#7f6574;*/ }
div.vc_transcript_inner .GRANGER { color: #8080ff; /*#6060c0;*/ }
div.vc_transcript_inner .HARRY { color: #ff0000; }
div.vc_transcript_inner .WIRELESS { color: #737373; }
div.vc_transcript_inner .VOLDEMORT { color: #80ff80; }
div.vc_transcript_inner .HARRYMORT { color: #ba823f; }
div.vc_transcript_inner .LESTRANGE { color: #c8ff00; }
div.vc_transcript_inner .SNAPE { color: #809e80; }
div.vc_transcript_inner .DUMBLEDORE { color: #8000c0; }
div.vc_transcript_inner .deep_purple { color: #8000c0; }
div.vc_transcript_inner .ZABINI { color: #eec832; }
div.vc_transcript_inner .LUNA { color: #00ff00; }
div.vc_transcript_inner .grey { color: '''+dialogue_50pct_grey+'''; }
div.vc_transcript_inner .pure_blue { color: #0000ff; }
div.vc_transcript_inner .bright_orange { color: #ffc800; }
div.vc_transcript_inner .bright_green { color: #00ff00; }
div.vc_transcript_inner .bright_red { color: #ff0000; }
div.vc_transcript_inner .cyan { color: #00ffff; }
div.vc_transcript_inner .pale_blue { color: #6483c4; }
div.vc_transcript_inner .light_pink { color: #ff80c0; }
div.vc_transcript_inner .dark_green { color: #326632; }


.transcripts_hidden div.vc_transcript_box { min-height: 0; }
.transcripts_hidden p.vc_transcript_line { display: none; }
''')

def format_transcript_line(line_text):
  classes = ['vc_transcript_line']
  match = re.match("([A-Z ]+): ", line_text)
  if match:
    classes.append("dialogue")
    if match.group(1) in dialogue_name_replace:
      entry = dialogue_name_replace[match.group(1)]
      classes.append(match.group(1) if entry is True else entry)
  return '<p class="'+(' '.join(classes))+'">'+line_text+'</p>'

def format_transcript_recur(transcript, wide_screen_rules_list):
  if len(transcript) == 0:
    return ''
  else:
    line_info = transcript[len(transcript) - 1]
    height_num_str = str(line_info[0] // 4)
    wide_screen_rules_list.append('.vc_transcript_box.px'+height_num_str+' { min-height: '+height_num_str+'px }')
    return '<div class="vc_transcript_box px'+height_num_str+'">'+format_transcript_recur(transcript[0:len(transcript) - 1], wide_screen_rules_list)+'</div>'+line_info[1]

def format_transcript(transcript, wide_screen_rules_list):
  entries = [(0, '<div class="vc_transcript_label">Transcript: <a href="javascript:;"><span id="hide_transcript_button" class="hide_transcript_button">(hide)</span><span id="show_transcript_button" class="show_transcript_button">(show)</span></a></div>')]
  entries.extend([(a, format_transcript_line(b)) for (a, b) in transcript])
  return format_transcript_recur(entries, wide_screen_rules_list)+'<a id="hide_transcript_button_2" class="hide_transcript_button" href="javascript:;">(hide transcript)</a>'



import top_bar
import bars
import html_pages
  
def vc_content_notice_bars_wrap(info, notice, html):
  return '''<a class="skip" href="#footer">Skip to footer</a>
<div class="vc_content_notice_box">
  '''+top_bar.top_bar(info)+'''
  <section>
    <div class="vc_content_notice_text">
      <div class="vc_content_notice_main_text">
        <p>The comic below '''+notice+'''</p>
        <p id="view_the_comic_p">Scroll down to view the comic.</p>
      </div>
      <div class="vc_content_notice_details">
        <p id="disable_content_notices_p">You could disable content notices if you had Javascript and cookies enabled.</p>
      </div>
    </div>
  </section>
</div>
<div class="vc_box_after_content_notice">
  <div class="bars_inner_box">
    '''+html+'''
  </div>
  '''+bars.bottom_bar(info)+'''
</div>'''

def add_vc_pages(page_dict):
  for i in range(0,len(vc_pages)):
    vc_page = vc_pages[i]
    prev_page = (vc_pages[i-1] if i>0 else None)
    next_page = (vc_pages[i+1] if i+1 < len(vc_pages) else None)
    prev_page_url = (vc_page_url(i-1) if prev_page else None)
    next_page_url = (vc_page_url(i+1) if next_page else None)
    html, head = vc_page_html_and_head(vc_page, prev_page, next_page)
    utils.checked_insert(page_dict,
      vc_page_filename(i),
      html_pages.make_page(
        ('Page '+str(i)+' ⊂ ' if i>0 else '')+"Voldemort's Children ⊂ Eli Dupree's website",
        head
+('<link rel="next prefetch prerender" href="'+next_page_url+'" />\n<link rel="prefetch" href="'+vc_comic_image_url(next_page)+'" />\n' if next_page else '')
+('<link rel="prev prefetch prerender" href="'+prev_page_url+'" />\n<link rel="prefetch" href="'+vc_comic_image_url(prev_page)+'" />\n' if prev_page else '')
,
        '<body class="voldemorts_children"><a class="skip" href="#content">Skip to content</a>'+(
           vc_content_notice_bars_wrap({"comics":True}, vc_page["content_notice"], html) if "content_notice" in vc_page else
                        bars.bars_wrap({"comics":True},                            html)
        )+'</body>'
      )
    )


def convert_vc_page(page_dict):
  gimp_stuff.generate_vc_images(page_dict["xcf_base"], page_dict["list_index"])
