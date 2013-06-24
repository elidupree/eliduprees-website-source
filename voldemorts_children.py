
import re
import utils
import css
import top_bar
import bars
import html_pages
from voldemorts_children_pages import vc_pages


vc_content_margin = "4em";
comic_width = 750;
sideways_space = 20;
min_transcript_width = 320;
max_transcript_width = 500;
transcript_at_side_width = comic_width + 3*sideways_space + min_transcript_width;
transcript_maximized_width = comic_width + 3*sideways_space + max_transcript_width;

css.insert('''
div.vc_content_notice_box {
  height: 100%; }
div.vc_content_notice_text {
  margin: 2em auto;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
  text-align: center; }
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
a.vc_nav_button:link{ color: #99994e; /*#7e7e40*/ }
a.vc_nav_button:visited{ color: #4d6699; /*#40557f*/ }
div.vc_nav_button.content_notice a.vc_nav_button:link{ color: #ffff82; /*#7e7e40*/ }
div.vc_nav_button.content_notice a.vc_nav_button:visited{ color: #81abff; /*#40557f*/ }
span.vc_nav_content_notice {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 110%; }
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
.vc_transcript_hidden .show_transcript_button {
  display: inline; }
.vc_transcript_hidden .hide_transcript_button {
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
  .vc_transcript_hidden div.vc_comic_and_nav {
    width: '''+str((transcript_at_side_width+comic_width)/2)+'''px;
    padding-left: '''+str((transcript_at_side_width-comic_width)/2)+'''px; }
  .vc_transcript_hidden div.vc_transcript_outer {
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
  background-color: #cccccc
}
div.vc_annotation .blog_post_metadata {
  background-color: rgba(204,204,204,.7) }''')

def vc_navbar(prev_page, next_page):
  def inner_link(string, big_string, page):
    if not page:
      return ''
    return (
    '<a class="vc_nav_button" rel="'+string+'" href="'+vc_page_url(page)+'">'
      +('' if "content_notice" not in page else '<span class="vc_nav_content_notice bigger">The '+big_string+' page '+page["content_notice"]+'</span>')
      +'<span class="vc_nav_button_main">'+utils.capitalize_string(big_string)+'</span>'
      +('' if "content_notice" not in page else '<a class="disable_content_notices" href="javascript">(disable content notices)</a>')
    +'</a>')
  def link(string, big_string, page):
    return '<div class="vc_nav_button '+string+(' content_notice' if (page and ("content_notice" in page)) else '')+'">'+inner_link(string, big_string, page)+'</div>'
  return '<div class="vc_nav_bar">'+link("prev","previous",prev_page)+link("next","next",next_page)+'</div>'

print("Fix this hack:")
def vc_comic_image_url(page):
  # Hack...
  return 'http://deqyc5bzdh53a.cloudfront.net/VC_'+str(page["list_index"]+1)+'.png'

def vc_page_html_and_head(page, prev_page, next_page):
  wide_screen_rules_list = []
  navbar = (vc_navbar(prev_page, next_page) if page["list_index"] != 0 else '')
  return (
    '''
<div class="vc_comic_and_nav">'''
  +navbar+'''
  <main>
    <div id="content" class="vc_comic_and_transcript">
      <div class="vc_comic">
        '''+('<a tabindex="-1" href="'+vc_page_url(next_page)+'">' if next_page else '')+'''
          <img class="vc_comic" alt="A comic page; see below for a transcript" src="'''+vc_comic_image_url(page)+'''" />
        '''+('</a>'                         if next_page else '')+'''
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
        <div class="blog_post_metadata_outer">
          <div class="blog_post_metadata">Posted May 14, 2015</div>
        </div>
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
  
def vc_content_notice_bars_wrap(info, notice, html):
  return '<div class="vc_content_notice_box">'+top_bar.top_bar(info)+'<section><div class="vc_content_notice_text"><div class="vc_content_notice_main_text"><p>The following page '+notice+'</p><p><a class="dismiss_content_notice" href="javascript">View the comic</a></p></div><div class="vc_content_notice_details"><p><a class="disable_content_notices" href="javascript">Disable content notices for this site</a></p></div></div></section></div><div class="vc_box_after_content_notice"><div class="bars_inner_box">'+html+'</div>'+bars.bottom_bar(info)+'</div>'

# in place of "Disable content notices for this site",
# "You could disable content notices if you had cookies enabled for this site",
# "You could disable content notices if you had Javascript and cookies enabled for this site",

dialogue_50pct_grey = '#8c8c8c'
dialogue_name_replace = {
  "TITLE":True,
  "TONKS":True,"GRANGER":True,"HARRY":True,"VOLDEMORT":True,
  "WIRELESS":True,"LESTRANGE":True,
  "PRESENT HARRY":"HARRY",
  "PRESENT GRANGER":"GRANGER",
  "FUDGE":"GREY", "PAST GRANGER":"GREY", "MCGONAGALL":"GREY",
}
css.insert('''
p.vc_transcript_line {
  margin: 0;
  padding-bottom: 0.9em;
  line-height: 1.2em; }
div.vc_transcript_inner .dialogue { font-weight: bold; }
div.vc_transcript_inner .TITLE { color: #9a6f34; /*#412f16;*/ }
div.vc_transcript_inner .TONKS { color: #bf98af; /*#7f6574;*/ }
div.vc_transcript_inner .GRANGER { color: #8080ff; /*#6060c0;*/ }
div.vc_transcript_inner .HARRY { color: #ff0000; }
div.vc_transcript_inner .WIRELESS { color: #737373; }
div.vc_transcript_inner .VOLDEMORT { color: #80ff80; }
div.vc_transcript_inner .HARRYMORT { color: #ba823f; }
div.vc_transcript_inner .LESTRANGE { color: #c8ff00; }
div.vc_transcript_inner .GREY { color: '''+dialogue_50pct_grey+'''; }

.vc_transcript_hidden div.vc_transcript_box { min-height: 0; }
.vc_transcript_hidden p.vc_transcript_line { display: none; }
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
  entries = [(0, '<div class="vc_transcript_label">Transcript: <a href="javascript"><span class="hide_transcript_button">(hide)</span><span class="show_transcript_button">(show)</span></a></div>')]
  entries.extend([(a, format_transcript_line(b)) for (a, b) in transcript])
  return format_transcript_recur(entries, wide_screen_rules_list)+'<a class="hide_transcript_button" href="javascript">(hide transcript)</a>'

# these work for either page numbers or pages
def vc_webname_base(page):
  page_number = (page["list_index"] if type(page) is dict else page)
  return 'voldemorts-children'+('' if page_number == 0 else '/'+str(page_number))
def vc_page_url(page):
  return '/'+vc_webname_base(page)
def vc_page_filename(page):
  return vc_webname_base(page)+'.html'



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
        "Eli Dupree's website ⊃ Voldemort's Children ⊃ Page "+str(i),
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
