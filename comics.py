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
div.comic_content_warning_box {
  height: 100%; }
html.content_warnings_disabled div.comic_content_warning_box {
  height: auto; }
html.content_warning_dismissed div.comic_content_warning_box {
  height: auto; }
div.comic_content_warning_text {
  margin: 0 auto;
  padding: 6.5em 0;
  font-family: Arial, Helvetica, sans-serif;
  text-align: center; }
.content_warnings_disabled div.comic_content_warning_text {
  display: none; }
.content_warning_dismissed div.comic_content_warning_text {
  display: none; }
div.comic_content_warning_main_text {
  font-size: 120%;
  margin: 0 auto;
  max-width: 35em;
  border: 3px solid white;
  border-radius: 2em; }
div.comic_content_warning_details {
  margin: 0 auto;
  max-width: 35em; }
a.dismiss_content_warning {
  display: block;
  font-size: 200%;
  margin-top: 0.6em;
  padding: 0.15em;
  font-weight: bold; }

.metabar_content_warnings_disabled {
  display: none; }
html.content_warnings_disabled .metabar_content_warnings_disabled {
  display: inline; }
html.content_warnings_disabled .metabar_content_warnings_enabled {
  display: none; }
a.comic_disable_content_warnings {
  font-family: Arial, Helvetica, sans-serif;
  display: block;
  padding: 0.5em; }
html.content_warnings_disabled a.comic_disable_content_warnings {
  display: none; }
div.comic_box_after_content_warning {
  position: relative; }
.remove_if_content_warnings_enabled {
  display: none; }
html.content_warnings_disabled .remove_if_content_warnings_enabled {
  display: block; }
html.content_warnings_disabled .remove_if_content_warnings_disabled {
  display: none; }
  
div.comic_and_nav {
  margin: 2em auto; }
div.comic_image {
  padding-bottom: 3em;
  display: inline-block; }

div.comic_transcript_inner {
  padding: 0 '''+str(sideways_space)+'''px;
  font-family: Arial, Helvetica, sans-serif;
  font-weight: bold; }
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
  position: relative;
  display: inline-block;
  text-align: center;
  vertical-align: top;
  width: 50%; }
div.comic_nav_button a {
  display: block; }
                               div.comic_nav_button.content_warning { margin-bottom: 3em; }
html.content_warnings_disabled div.comic_nav_button.content_warning { margin-bottom: 0; }
.comic_nav_button_main {
  display: block;
  border-style: solid;
  border-color: transparent;
  border-top-width: 40px;
  border-bottom-width: 40px;
 }
span.comic_nav_button_main {
  font-size: 300%;
  font-weight: bold; }
span.comic_nav_content_warning {
  position: absolute;
  left: 9%;
  right: 9%;
  top: 100%;
  margin-top: -34px;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 110%; }
.content_warnings_disabled span.comic_nav_content_warning {
  display: none; }

div.comic_metabar {
  font-family: Arial, Helvetica, sans-serif;
  font-weight: bold;
  margin: 0.5em 0;
  text-align: center; }

div.comic_archive {
  text-align: center; }
div.comic_archive h1 {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 250%;
  padding: 0.2em; }
div.comic_archive h2 {
  font-size: 200%;
  padding: 0.2em; }
div.comic_archive_chapter {
  padding: 1em 0; }
a.comic_archive_entry {
  display: inline-block; }

div.hidden_cw_box {
  border: 1px dashed black;
  padding: 0.5em; }
html.content_warnings_disabled div.hidden_cw_box.secondary {
  display: none; }
html.hidden_cws_revealed div.hidden_cw_box.secondary {
  display: block; }
a.reveal_cw_button {
  font-size: 150%;
  font-family: Arial, Helvetica, sans-serif;
  text-align: center; }
a.reveal_cw_button { display:none; }
html.content_warnings_disabled a.reveal_cw_button { display:block; }
html.content_warnings_disabled div.hidden_cws { display:none; }
''')


javascript.do_before_body('''
window.elidupree.show_transcript = function() {
  remove_class(document.documentElement, 'transcripts_hidden');
  delete_cookie('transcripts_hidden');
};
window.elidupree.hide_transcript = function() {
  document.documentElement.className += ' transcripts_hidden';
  set_cookie('transcripts_hidden', 'true', 30);
};

window.elidupree.handle_content_warnings = function(id, default_on) {
  window.elidupree.enable_content_warnings = function() {
    remove_class(document.documentElement, 'content_warnings_disabled');
    if (default_on) {
      delete_cookie('content_warnings_disabled_'+id);
    }
    else {
      set_cookie('content_warnings_enabled_'+id, 'true', 30);
    }
  };
  window.elidupree.disable_content_warnings = function() {
    document.documentElement.className += ' content_warnings_disabled';
    if (default_on) {
      set_cookie('content_warnings_disabled_'+id, 'true', 30);
    }
    else {
      delete_cookie('content_warnings_enabled_'+id);
    }
  };
  if (default_on && read_cookie('content_warnings_disabled_'+id)) {
    window.elidupree.disable_content_warnings();
  }
  if ((!default_on) && !read_cookie('content_warnings_enabled_'+id)) {
    window.elidupree.disable_content_warnings();
  }
  if (read_cookie('transcripts_hidden')) {
    window.elidupree.hide_transcript();
  }
};

''')
javascript.do_after_body('''
var show_transcript_button   = document.getElementById('show_transcript_button'  );
var hide_transcript_button   = document.getElementById('hide_transcript_button'  );
var hide_transcript_button_2 = document.getElementById('hide_transcript_button_2');
if (show_transcript_button  ) { add_event_listener(show_transcript_button  ,'click',window.elidupree.show_transcript); }
if (hide_transcript_button  ) { add_event_listener(hide_transcript_button  ,'click',window.elidupree.hide_transcript); }
if (hide_transcript_button_2) { add_event_listener(hide_transcript_button_2,'click',window.elidupree.hide_transcript); }

var view_the_comic_p = document.getElementById('view_the_comic_p');
if (view_the_comic_p) {
  var dismiss_content_warning_a = document.createElement('a');
  dismiss_content_warning_a.className = 'dismiss_content_warning meta_controls_coloring';
  dismiss_content_warning_a.setAttribute('href','javascript:;');
  dismiss_content_warning_a.appendChild(document.createTextNode('View the comic'));
  view_the_comic_p.replaceChild(dismiss_content_warning_a, view_the_comic_p.firstChild);
  add_event_listener(dismiss_content_warning_a,'click',function() { document.documentElement.className += ' content_warning_dismissed'; });
  
  var disable_content_warnings_p = document.getElementById('disable_content_warnings_p');
  if (cookies_enabled) {
    var disable_content_warnings_a = document.createElement('a');
    disable_content_warnings_a.className = 'comic_disable_content_warnings meta_controls_coloring';
    disable_content_warnings_a.setAttribute('href','javascript:;');
    disable_content_warnings_a.appendChild(document.createTextNode('Disable content warnings'));
    disable_content_warnings_p.replaceChild(disable_content_warnings_a, disable_content_warnings_p.firstChild);
    add_event_listener(disable_content_warnings_a,'click',window.elidupree.disable_content_warnings);
  }
  else {
    disable_content_warnings_p.firstChild.nodeValue = 'You could disable content warnings if you had cookies enabled.'
  }
}

var enable_content_warnings_buttons = document.getElementsByClassName("enable_content_warnings_button");
for (i = 0; i < enable_content_warnings_buttons.length; ++i) {
  add_event_listener(enable_content_warnings_buttons[i],'click',window.elidupree.enable_content_warnings);
}
var disable_content_warnings_buttons = document.getElementsByClassName("disable_content_warnings_button");
for (i = 0; i < disable_content_warnings_buttons.length; ++i) {
  add_event_listener(disable_content_warnings_buttons[i],'click',window.elidupree.disable_content_warnings);
}
''')

print ("TODO: make the first page of VC list content warnings, give the user a choice")

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
    "html_class": "voldemorts_children",
    "url": "/voldemorts-children",
    "abbr": "VC",
    "image_width": 750,
    "dialogue_name_replacements":voldemorts_children.dialogue_name_replace,
    "image_url_offset":0,
    "page_number_offset": 0,
    "arrow_images": True,
  },
  "acobs": {
    "title": "A Couple of Badass Superheroes",
    "html_class": "acobs",
    "url": "/a-couple-of-badass-superheroes",
    "abbr": "ACOBS",
    "image_width": 545,
    "dialogue_name_replacements":{},
    "image_url_offset":1,
    "page_number_offset": 1,
  },
}

for comic_id,page_list in comics_pages.items():
  for i in range(0,len(page_list)):
    page_list[i]["comic_id"] = comic_id
    page_number = i + comics_metadata [comic_id] ["page_number_offset"]
    page_list [i ] ["page_number"] = page_number
    page_list[i]["title"] = comics_metadata [comic_id] ["title"] + (", cover page" if page_number == 0 else ", page "+ str(page_number))
    page_list[i]["list_index"] = i
    page_list[i]["height_conversion_factor"] = 1
for page_dict in comics_pages["voldemorts_children"]:
  page_dict["height_conversion_factor"] = 4

def page_url(page):
  return comics_metadata[page["comic_id"]]["url"]+('' if page["list_index"] == 0 else '/'+str(page["page_number"]))

def comic_image_url(page, ext = ''):
  meta = comics_metadata[page["comic_id"]]
  if ext:
    ext = '_'+ext
  else:
    ext = ''
  return '/media/'+meta["abbr"]+'_'+str(page["list_index"]+meta["image_url_offset"])+ext+'.png?rr'

def comic_thumbnail_url(page):
  print ("comic_thumbnail_url is deprecated")
  return '/media/'+comics_metadata[page["comic_id"]]["abbr"]+'_'+str(page["list_index"])+'_thumbnail_top.png?rr'

def last_comic_thumbnail_url():
  return comic_thumbnail_url(comics_pages["voldemorts_children"][len(comics_pages["voldemorts_children"]) - 1])

def recent_page_link(deduction):
  page = comics_pages["voldemorts_children"][len(comics_pages["voldemorts_children"]) - 1 - deduction]
  return '<a class="recent_update" href="'+page_url(page)+'"><div class="recent_update_outer"><div class="recent_update"><img src="'+comic_thumbnail_url(page)+'" alt="" /> '+page["title"]+'</div></div><div class="recent_update_end"></div></a>'


def do_css_for_comic(comic_id):
  comic_width = comics_metadata[comic_id]["image_width"]
  ancestor_str = 'html.'+comics_metadata[comic_id]["html_class"]
  transcript_at_side_width = comic_width + 3*sideways_space + min_transcript_width
  transcript_maximized_width = comic_width + 3*sideways_space + max_transcript_width
  comics_metadata[comic_id]["transcript_at_side_width"] = transcript_at_side_width
  nav_margin = comic_width // 30
  navigation_width =comic_width - nav_margin*2
  navhalf_wid = (navigation_width ) // 2
  navbut_inner_margin = comic_width // 15
  navbut_wid = navhalf_wid - navbut_inner_margin*2
  css.insert('''
'''+ancestor_str+''' div.comic_and_nav {
  width: '''+str(comic_width)+'''px; }
'''+ancestor_str+''' img.comic_image {
  width: '''+str(comic_width)+'''px; }
  
'''+ancestor_str+''' div.comic_nav_bar {
  width: 94%;
  margin: 0 3%;}

'''+ancestor_str+''' .comic_nav_button_main {
  width: '''+str(navbut_wid)+'''px;
margin: 0 auto;}


@media screen and (max-width:'''+str( comic_width - 1) +'''px) {
'''+ancestor_str+''' div.comic_and_nav {
  width: 100%; }
'''+ancestor_str+''' img.comic_image {
  width: 100%; }
'''+ancestor_str+''' .comic_nav_button_main {
  width: '''+str(navbut_wid*100//navhalf_wid )+'''%;}
}

@media screen and (min-width: '''+str(transcript_at_side_width)+'''px) {
  '''+ancestor_str+''' div.comic_and_nav {
    width: auto;
    padding-left: '''+str(sideways_space)+'''px; }
  '''+ancestor_str+''' div.comic_image {
    padding-bottom: 0;
    margin-right: -'''+str(comic_width)+'''px; }
    
  '''+ancestor_str+''' div.comic_nav_bar {
    width: '''+str(navigation_width )+'''px;
    margin: 0 '''+str(nav_margin )+'''px;}
    
  '''+ancestor_str+''' div.comic_metabar {
    width: '''+str(comic_width)+'''px; }
  '''+ancestor_str+''' div.comic_annotation_outer {
    width: '''+str(comic_width)+'''px; }

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
''')

for comic_id,page_list in comics_pages.items():
  do_css_for_comic(comic_id)

import top_bar
import bars
import html_pages
  
def content_warning_bars_wrap(info, warning, html):
  return '''<a class="skip" href="#footer">Skip to footer</a>
<div class="comic_content_warning_box">
  '''+top_bar.top_bar(info)+'''
  <section>
    <div class="comic_content_warning_text">
      <div class="comic_content_warning_main_text">
        <p>The comic below '''+warning+'''.</p>
        <p id="view_the_comic_p">Scroll down to view the comic.</p>
      </div>
      <div class="comic_content_warning_details">
        <p id="disable_content_warnings_p">You could disable content warnings if you had Javascript and cookies enabled.</p>
      </div>
    </div>
  </section>
</div>
<div class="comic_box_after_content_warning">
  <div class="bars_inner_box">
    '''+html+'''
  </div>
  '''+bars.bottom_bar(info)+'''
</div>'''

def bars_wrap(info, html, page):
  return (content_warning_bars_wrap({"comics":True}, page["content_warning"], html) if "content_warning" in page else
                     bars.bars_wrap({"comics":True},                          html))


def comic_navbar(prev_page, next_page):
  def link(string, big_string, page):
    inner_link = ''
    extra_class = ''
    if page:
      cw = ''
      extra_class = ' '+string
      if "content_warning" in page:
        cw = '<span class="comic_nav_content_warning">(content warning: '+page["content_warning"]+'.)</span>'
        extra_class = extra_class+' content_warning'
      else:
        extra_class = extra_class+' no_content_warning'
      if "arrow_images" in comics_metadata[page["comic_id"]]:
        button = '<img class="comic_nav_button_main'+extra_class+'" alt="'+big_string+'" src="/media/'+comics_metadata[page["comic_id"]]["abbr"]+'-arrow-'+string+'.png?rr">'
      else:
        button = '<span class="comic_nav_button_main'+extra_class+'">'+big_string+'</span>'
      inner_link = (
      '<a id="'+string+'" class="comic_nav_button" rel="'+string+'" href="'+page_url(page)+'">'+cw+button+'</a>')
    
    return '''<div class="comic_nav_button'''+extra_class+'''">
        '''+inner_link+'''
      </div>'''
  return '<div class="comic_nav_bar">'+link("prev","Previous",prev_page)+link("next","Next",next_page)+'</div>'

def comic_metabar(page):
  return '''
<div class="comic_metabar">
  <a class="meta_controls_coloring" href="'''+comics_metadata[page["comic_id"]]["url"]+'''">First</a>'''+utils.inline_separator+'''<a class="meta_controls_coloring" href="'''+comics_metadata[page["comic_id"]]["url"]+'''/archive">Archive</a>'''+utils.inline_separator+'''
  <span class="metabar_content_warnings_enabled'''+(" content_warning" if "content_warning" in page else "")+'''">
    ⚠ '''+(page["content_warning"] if "content_warning" in page else "none")+''' <a class="disable_content_warnings_button meta_controls_coloring" href="javascript:;">(disable content warnings)</a>
  </span>
  <span class="metabar_content_warnings_disabled">
    ⚠ disabled <a class="enable_content_warnings_button meta_controls_coloring" href="javascript:;">(enable content warnings)</a>
  </span>
</div>'''
  
  

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
  return format_transcript_recur(page, entries, wide_screen_rules_list)+'<a id="hide_transcript_button_2" class="hide_comic_transcript_button meta_controls_coloring" href="javascript:;">(hide transcript)</a>'



import blog

def page_html_and_head(page, prev_page, next_page):
  wide_screen_rules_list = []
  navbar = comic_navbar(prev_page, next_page)
  metabar = comic_metabar(page)
  metadata = blog.post_metadata(page)
  (HTML, head) =blog.post_html(page["annotation"], None, page_url(page), None, False, metadata)
  return (
    '''
<div class="comic_and_nav">'''
  +metabar+navbar+'''
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
    +navbar+metabar+'''
    <div class="comic_annotation_outer">
      <div class="comic_annotation">
        '''+ HTML +'''
      </div>
    </div>
  </main>
</div>''',


head +'''
<style type="text/css">
@media screen and (min-width: '''+str(comics_metadata[page["comic_id"]]["transcript_at_side_width"])+'''px) {
  '''+'\n'.join(wide_screen_rules_list)+'''
}
</style>''')


def add_comic_pages(page_dict):
  for comic_id,page_list in comics_pages.items():
    
    archive_entries = ['<div class="comic_archive_chapter"><h1>Archive of <span class="title">'+comics_metadata[comic_id]["title"]+'</span></h1>']
    
    for i in range(0,len(page_list)):
      page = page_list[i]
      prev_page = (page_list[i-1] if i>0 else None)
      next_page = (page_list[i+1] if i+1 < len(page_list) else None)
      html, head = page_html_and_head(page, prev_page, next_page)
      extra_scripts = "window.elidupree.handle_content_warnings('"+comic_id+"', true)\n"
      if next_page:
        head = head+'<link rel="next prefetch prerender" href="'+page_url(next_page)+'" />\n<link rel="prefetch" href="'+comic_image_url(next_page)+'" />\n'
        extra_scripts = extra_scripts + "if (document.referrer.indexOf('"+page_url(next_page)+"') !== -1) { document.documentElement.className += ' content_warning_dismissed'; }\n"
      if prev_page:
        head = head+'<link rel="prev prefetch prerender" href="'+page_url(prev_page)+'" />\n<link rel="prefetch" href="'+comic_image_url(prev_page)+'" />\n'
        extra_scripts = extra_scripts + "if (document.referrer.indexOf('"+page_url(prev_page)+"') !== -1) { document.documentElement.className += ' content_warning_dismissed'; }\n"
      utils.checked_insert(page_dict,
        page_url(page)+'.html',
        html_pages.make_page(
          ('Page '+str(page ["page_number"])+' ⊂ ' if i>0 else '')+comics_metadata[comic_id]["title"]+" ⊂ Eli Dupree's website",
          head,
          '<script>'+extra_scripts+'''</script>
  <a class="skip" href="#content">Skip to content</a>'''+bars_wrap({"comics":True}, html, page), {"html_class":comics_metadata[comic_id]["html_class"]}
        )
      )
      
      if "chapter_start" in page:
        archive_entries.append('</div><div class="comic_archive_chapter"><h2>'+page["chapter_start"]+'</h2>')
      archive_entries.append('<a class="comic_archive_entry" href="'+page_url(page)+'"><img class="comic_archive_entry" src="'+comic_image_url(page, 'thumbnail_full')+'"></a>')
    
    archive_entries.append('</div>')
    archive_html = '<main><div class="comic_archive">'+''.join(archive_entries)+'</div></main>'
    utils.checked_insert(page_dict,
      comics_metadata[comic_id]["url"]+'/archive.html',
      html_pages.make_page(
        'Archive ⊂ '+comics_metadata[comic_id]["title"]+" ⊂ Eli Dupree's website",
        head,
        '''
<a class="skip" href="#content">Skip to content</a>'''+bars.bars_wrap({"comics":True}, archive_html), {"html_class":comics_metadata[comic_id]["html_class"]}
      )
    )
    

