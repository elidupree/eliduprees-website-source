#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import re
import utils
import css
import blog
import comics
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

body.voldemorts_children div.comic_toggle_content_notices {
  color: #808080; }
body.voldemorts_children a.comic_toggle_content_notices {
  color: #ffc800; }
body.voldemorts_children a.comic_disable_content_notices {
  color: #ffc800; }
  
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
div.vc_annotation .post_content_section {
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


def vc_navbar(prev_page, next_page):
  def inner_link(string, big_string, page):
    if not page:
      return ''
    return (
    '<a id="'+string+'" class="vc_nav_button" rel="'+string+'" href="'+vc_page_url(page)+'">'
      +('' if "content_notice" not in page else '<span class="vc_nav_content_notice bigger">The '+big_string+' page '+page["content_notice"]+'</span>')
      +'<span class="vc_nav_button_main">'+utils.capitalize_string(big_string)+'</span></a>'
    +('' if "content_notice" not in page else '<a id="disable_content_notices_button_'+big_string+'" class="comic_disable_content_notices" href="javascript:;">(disable content notices)</a>'))
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
  <div class="comic_toggle_content_notices remove_if_content_notices_disabled">
    Content notices are enabled. <a id="disable_content_notices_button_toggle" class="comic_toggle_content_notices" href="javascript:;">(disable)</a>
  </div>
  <div class="comic_toggle_content_notices remove_if_content_notices_enabled">
    Content notices are disabled. <a id="enable_content_notices_button_toggle" class="comic_toggle_content_notices" href="javascript:;">(enable)</a>
  </div>
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
        '''+blog.post_html(page["annotation"], None, vc_page_url(page), None, True, metadata)+'''
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
    extra_scripts = ''
    if next_page:
      head = head+'<link rel="next prefetch prerender" href="'+next_page_url+'" />\n<link rel="prefetch" href="'+vc_comic_image_url(next_page)+'" />\n'
      extra_scripts = extra_scripts + "if (document.referrer.indexOf('"+vc_page_url(next_page)+"') !== -1) { document.body.className += ' content_notice_dismissed'; }"
    if prev_page:
      head = head+'<link rel="prev prefetch prerender" href="'+prev_page_url+'" />\n<link rel="prefetch" href="'+vc_comic_image_url(prev_page)+'" />\n'
      extra_scripts = extra_scripts + "if (document.referrer.indexOf('"+vc_page_url(prev_page)+"') !== -1) { document.body.className += ' content_notice_dismissed'; }"
    utils.checked_insert(page_dict,
      vc_page_filename(i),
      html_pages.make_page(
        ('Page '+str(i)+' ⊂ ' if i>0 else '')+"Voldemort's Children ⊂ Eli Dupree's website",
        head,
        '<script>'+extra_scripts+'''</script>
<a class="skip" href="#content">Skip to content</a>'''+comics.bars_wrap({"comics":True}, html, vc_page), {"body_class":"voldemorts_children"}
      )
    )


def convert_vc_page(page_dict):
  gimp_stuff.generate_vc_images(page_dict["xcf_base"], page_dict["list_index"])
