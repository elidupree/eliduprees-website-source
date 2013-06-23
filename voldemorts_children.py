
import re
import utils
import css
import top_bar
import bars
import html_pages


vc_content_margin = "4em";
transcript_at_side_width = 1090;
comic_width = 750;

css.insert('''
div.vc_trigger_warning_box {
  height: 100%; }
div.vc_trigger_warning_text {
  margin: 2em auto;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
  text-align: center; }
div.vc_trigger_warning_text a {
  color: #ffc800; }
div.vc_trigger_warning_main_text {
  font-size: 120%;
  margin: 0 auto;
  max-width: 35em;
  border: 3px solid white;
  border-radius: 2em; }
div.vc_trigger_warning_details {
  margin: 0 auto;
  max-width: 35em; }
a.dismiss_trigger_warning {
  display: block;
  font-size: 200%;
  margin-top: 0.6em;
  padding: 0.15em;
  font-weight: bold; }
a.disable_trigger_warnings {
  display: block;
  padding: 0.5em; }
div.vc_box_after_trigger_warning {
  position: relative; }
  
div.vc_comic_and_nav {
  width: '''+str(comic_width)+'''px;
  margin: 2em auto; }
div.vc_comic_and_transcript {
  margin: 5em 0; }
div.vc_comic {
  display: inline-block;
  width: '''+str(comic_width)+'''px; }
img.vc_comic {
  width: '''+str(comic_width)+'''px; }
div.vc_transcript_outer {
  width: '''+str(comic_width)+'''px; }
  
div.vc_nav_bar {
  width: '''+str(comic_width)+'''px; }
div.vc_nav_button {
  display: inline-block;
  color: #ffc800;
  /*background-color: #412f16;*/
  border-radius: 16px;
  width: 250px;
  text-align: center;
  font-size: 300%;
  font-weight: bold; }
div.vc_nav_button a:link{ color:#7e7e40 }
div.vc_nav_button a:visited{ color:#40557f }
div.vc_nav_button.prev {
  margin-left: 75px;
  margin-right: 50px; }
div.vc_nav_button.next {
  margin-left: 50px;
  margin-right: 75px; }
div.vc_transcript_inner {
  padding: 0.5em;
  color:white; }
div.vc_transcript_inner a {
  color: #ffc800; }
  
@media screen and (min-width: '''+str(transcript_at_side_width)+'''px) {
  div.vc_comic_and_nav {
    width: '''+str(transcript_at_side_width)+'''px; }
  div.vc_transcript_outer {
    display: inline-block;
    width: '''+str(transcript_at_side_width-comic_width)+'''px;
    vertical-align: top; }
  .vc_transcript_hidden div.vc_comic_and_nav {
    width: '''+str((transcript_at_side_width+comic_width)/2)+'''px;
    padding-left: '''+str((transcript_at_side_width-comic_width)/2)+'''px; }
  .vc_transcript_hidden div.vc_transcript_outer {
    width: '''+str((transcript_at_side_width-comic_width)/2)+'''px; }
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

def vc_navbar(prev_page, next_page, prev_page_url, next_page_url):
  return '<div class="vc_nav_bar">'+('<div class="vc_nav_button prev"><a rel="prev" href="'+prev_page_url+'">Previous</a></div>' if prev_page else '')+('<div class="vc_nav_button next"><a rel="next" href="'+next_page_url+'">Next</a></div>' if next_page else '')+'</div>'
  
def vc_comic_image_url(page):
  return 'http://deqyc5bzdh53a.cloudfront.net/VC_2.png'

def vc_page_html_and_head(page, prev_page, next_page, prev_page_url, next_page_url):
  wide_screen_rules_list = []
  navbar = vc_navbar(prev_page, next_page, prev_page_url, next_page_url)
  return (
    '''
<div class="vc_comic_and_nav">'''
  +navbar+'''
  <main>
    <div class="vc_comic_and_transcript">
      <div class="vc_comic">
        '''+('<a href="'+next_page_url+'">' if next_page else '')+'''
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
          <div class="blog_post_metadata">Posted May 14, 2015'''+utils.inline_separator+'<a rel="bookmark" href="'+'foo'+'''">Permalink</a></div>
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
  
def vc_trigger_warning_bars_wrap(info, html):
  return '<div class="vc_trigger_warning_box">'+top_bar.top_bar(info)+'<section><div class="vc_trigger_warning_text"><div class="vc_trigger_warning_main_text"><p>The following page contains depictions of gratuitous faux Latin.</p><p><a class="dismiss_trigger_warning" href="javascript">View the comic</a></p></div><div class="vc_trigger_warning_details"><p><a class="disable_trigger_warnings" href="javascript">Disable content notices for this site</a></p></div></div></section></div><div class="vc_box_after_trigger_warning"><div class="bars_inner_box">'+html+'</div>'+bars.bottom_bar(info)+'</div>'

# in place of "Disable content notices for this site",
# "You could disable content notices if you had cookies enabled for this site",
# "You could disable content notices if you had Javascript and cookies enabled for this site",

css.insert('''
p.vc_transcript_line {
  margin-top: 0;
  line-height: 1.2em; }
p.vc_transcript_line.dialogue {
  font-weight: bold; }
p.vc_transcript_line.TONKS {
  color: #bf98af; /*#7f6574;*/ }
p.vc_transcript_line.GRANGER {
  color: #8080ff; /*#6060c0;*/ }
''')

def format_transcript_line(line_text):
  classes = ['vc_transcript_line']
  match = re.match("([A-Z]+): ", line_text)
  if match:
    classes.append("dialogue")
    classes.append(match.group(1))
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
  entries = [(0, 'Transcript: <a href="javascript">(hide)</a>')]
  entries.extend([(a, format_transcript_line(b)) for (a, b) in transcript])
  return format_transcript_recur(entries, wide_screen_rules_list)

vc_pages = [
  {
    "transcript": [
      (0, 'Hermione Granger stands in a room labeled "Auror Offices". There are bookshelves along the wall. Granger has zir hair tied back, wears a long dark coat, and has very reserved mannerisms. Nymphadora Tonks enters the room. Tonks is more easygoing than Granger, wears a shorter, lighter coat, and has short spiky pink hair.'),
      (55, 'TONKS: Granger, you called?'),
      (980, 'GRANGER: Yes... I will speak with the prisoner &ndash; Attend me.'),
      (1655, 'TONKS: I can&apos;t get over it...'),
      (2000, 'They go to a long spiral staircase. Tonks walks down the stairs, while Granger flies down by magic.'),
      (2000, 'TONKS: All those people outside are yelling for his head... and we just go down...'),
      (3600, 'TONKS: and ask him questions.')],
    "annotation": '''<p>By the way, I have a built-in way to mark pages with trigger warnings. (If you're unsure what trigger warnings are about, <a href="http://fuckyeahtriggerwarnings.tumblr.com/">this tumblr is an excellent introduction</a>.) I'm going to try to mark any page that has potentially triggering material, but <strong>I'm not a very good judge of what might be triggering</strong>, because I don't get triggered myself (in fact, I basically never get <em>any</em> undesirable emotional effect from seeing <em>any</em> visual image). So if you see a potential trigger that I haven't marked, please tell me.</p>

<p>The same goes for any other web accessibility issue. I care about this stuff, so if you e-mail me with an issue, I <strong>will</strong> do my best to fix it.</p>'''
  },
]

def vc_webname_base(page_number):
  return 'voldemorts-children'+('' if page_number == 0 else '/'+str(page_number))
def vc_page_url(page_number):
  return '/'+vc_webname_base(page_number)
def vc_page_filename(page_number):
  return vc_webname_base(page_number)+'.html'


def add_vc_pages(page_dict):
  for i in range(0,len(vc_pages)):
    vc_page = vc_pages[i]
    next_page = (vc_pages[i-1] if i>0 else None)
    prev_page = (vc_pages[i+1] if i+1 < len(vc_pages) else None)
    next_page_url = (vc_page_url(i+1) if next_page else None)
    prev_page_url = (vc_page_url(i-1) if prev_page else None)
    html, head = vc_page_html_and_head(vc_page, prev_page, next_page, prev_page_url, next_page_url)
    utils.checked_insert(page_dict,
      vc_page_filename(i),
      html_pages.make_page(
        "Eli Dupree's website ⊃ Voldemort's Children ⊃ Page "+str(i),
        head
+('<link rel="next prefetch prerender" href="'+next_page_url+'" />\n<link rel="prefetch" href="'+vc_comic_image_url(next_page)+'" />\n' if next_page else '')
+('<link rel="prev prefetch prerender" href="'+prev_page_url+'" />\n<link rel="prefetch" href="'+vc_comic_image_url(prev_page)+'" />\n' if prev_page else '')
,
        '<body class="voldemorts_children">'+vc_trigger_warning_bars_wrap({"comics":True }, html)+'</body>'
      )
    )
