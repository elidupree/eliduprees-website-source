
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
  /*background-color: #412f16;
  border-radius: 16px;*/
  width: 250px;
  text-align: center; }
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
div.vc_transcript_inner {
  /*border: 1px dashed white;*/
  padding: 0.5em;
  font-family: Arial, Helvetica, sans-serif;
  color:white; }
div.vc_transcript_inner a {
  color: #ffc800; }
div.vc_transcript_label {
  padding-bottom: 1.1em; }
  
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
    <div class="vc_comic_and_transcript">
      <div class="vc_comic">
        '''+('<a href="'+vc_page_url(next_page)+'">' if next_page else '')+'''
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
  
def vc_content_notice_bars_wrap(info, notice, html):
  return '<div class="vc_content_notice_box">'+top_bar.top_bar(info)+'<section><div class="vc_content_notice_text"><div class="vc_content_notice_main_text"><p>The following page '+notice+'</p><p><a class="dismiss_content_notice" href="javascript">View the comic</a></p></div><div class="vc_content_notice_details"><p><a class="disable_content_notices" href="javascript">Disable content notices for this site</a></p></div></div></section></div><div class="vc_box_after_content_notice"><div class="bars_inner_box">'+html+'</div>'+bars.bottom_bar(info)+'</div>'

# in place of "Disable content notices for this site",
# "You could disable content notices if you had cookies enabled for this site",
# "You could disable content notices if you had Javascript and cookies enabled for this site",

dialogue_50pct_grey = '#8c8c8c'
dialogue_name_replace = {
  "FUDGE":"GREY", "PAST GRANGER":"GREY",
  "PRESENT HARRY":"HARRY",
}
css.insert('''
p.vc_transcript_line {
  margin-top: 0;
  line-height: 1.2em; }
div.vc_transcript_inner .dialogue { font-weight: bold; }
div.vc_transcript_inner .TITLE { color: #9a6f34; /*#412f16;*/ }
div.vc_transcript_inner .TONKS { color: #bf98af; /*#7f6574;*/ }
div.vc_transcript_inner .GRANGER { color: #8080ff; /*#6060c0;*/ }
div.vc_transcript_inner .HARRY { color: #ff0000; }
div.vc_transcript_inner .WIRELESS { color: #737373; }
div.vc_transcript_inner .VOLDEMORT { color: #80ff80; }
div.vc_transcript_inner .GREY { color: '''+dialogue_50pct_grey+'''; }
''')

def format_transcript_line(line_text):
  classes = ['vc_transcript_line']
  match = re.match("([A-Z ]+): ", line_text)
  if match:
    classes.append("dialogue")
    if match.group(1) in dialogue_name_replace:
      classes.append(dialogue_name_replace[match.group(1)])
    else:
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
  entries = [(0, '<div class="vc_transcript_label">Transcript: <a href="javascript">(hide)</a></div>')]
  entries.extend([(a, format_transcript_line(b)) for (a, b) in transcript])
  return format_transcript_recur(entries, wide_screen_rules_list)

vc_pages = [
  {
    "transcript": [
      (0, 'A cover page.'),
      (500, '''TITLE: Voldemort's Children'''),
      (1700, 'Three people stand, lit harshly by bright orange light. In the center is Harry Potter: heavyset, hunched over, zir black hair wild. To the right, Luna Lovegood: very thin, with long loose blond hair, with zir wand tucked behind zir ear and an exaggerated expression of interest. On the left, Draco Malfoy: also thin, reserved, with zir arms behind zir back, zir hair short and neat, and zir face slightly flushed.'),
      (3200, 'TITLE: A Harry Potter fanfic by Eli Dupree')],
      "annotation": '''<p>And so it begins.</p>

<p>I've been planning <i>Voldemort's Children</i> since September of last year, when I started analyzing the original series from a neurodiversity perspective. <i>Voldemort's Children</i> is an "Alternate Universe" fanfic - a reimagining of the story in which I explore one possibility of how events could happen in a world where we don't gloss over the implications of neurological difference in general and Harry's abuse as a child in particular.</p>

<p>I'm going to leave it at that for the moment, but I'll sometimes use these annotations to talk more about the purpose and structure of the story.</p>

<p> &ndash; Eli</p>'''
  },
  {
    "content_notice": 'contains depictions of gratuitous faux Latin.',
    "transcript": [
      (0, '''<span class="dialogue GRANGER">Hermione Granger</span> stands in a room labeled "Auror Offices". There are bookshelves along the wall. Granger has zir hair tied back, wears a long dark coat, and has very reserved mannerisms. <span class="dialogue TONKS">Nymphadora Tonks</span> enters the room. Tonks is more easygoing than Granger, wears a shorter, lighter coat, and has short spiky pink hair. Tonks's speech is drawn somewhat messily in a mild purple color, and Granger's is more formal and drawn in a mild blue.'''),
      (55, 'TONKS: Granger, you called?'),
      (980, 'GRANGER: Yes... I will speak with the prisoner &ndash; Attend me.'),
      (1655, '''TONKS: I can't get over it...'''),
      (2000, 'They go to a long spiral staircase. Tonks walks down the stairs, while Granger flies down by magic, leaving a blue trail of magical energy.'),
      (2000, 'TONKS: All those people outside are yelling for his head... and we just go down...'),
      (3600, 'TONKS: and ask him questions.')],
    "annotation": '''<p>By the way, I have a built-in way to mark pages with content notices, to warn users about content that might be triggering &ndash; or content that they might want to avoid for any other reason. (If you're unsure what trigger warnings are about, <a href="http://fuckyeahtriggerwarnings.tumblr.com/">this tumblr is an excellent introduction</a>.) I'm going to try to mark any page that has potentially triggering material, but I'm not a very good judge of what might be triggering, because I don't get triggered myself (in fact, I basically never get <em>any</em> undesirable emotional effect from seeing <em>any</em> visual image). So if you see a potential trigger that I haven't marked, please tell me.</p>

<p>The same goes for any other web accessibility issue. I care about this stuff, so if you e-mail me with an issue, I <strong>will</strong> do my best to fix it.</p>'''
  },
  {
    "transcript": [
      (0, 'A partial map of the Ministry of Magic Department of Magical Law Enforcement shows Granger and Tonks descending from the Auror Offices to the Interrogation Cells.'),
      (0, '''TONKS: I've got everything in order... The prisoner in cell 5...'''),
      (340, '''There's a barred cell door and a window blocked by cyan magic.'''),
      (900, 'TONKS: The truth potion...'),
      (900, 'There is a table with two bottles of a whitish liquid on it.'),
      (1080, 'TONKS: The warrant to use it...'),
      (1080, 'There are two sheets of paper on the table, with writing on them. One of them has the seal of the Ministry of Magic on it.'),
      (1250, '''GRANGER: You know I don't like to use that unless it is necessary.'''),
      (1680, 'TONKS: Better safe than sorry! The glass is just waiting for your tap. Then he can see and hear us.'),
      (2530, 'GRANGER: Good.'),
      (2990, '''Granger taps the cell's magical window, and the cyan magic clears away from the middle of the window, so it can be seen through.'''),
      (3690, 'GRANGER: And now... Harry Potter...'),
    ],
    "annotation": '''<p>If you're a <i>Harry Potter</i> fan, you might be thinking <q>Aha, ze wrote 'truth potion' for the benefit of people who aren't familiar enough with the series to know the name 'Veritaserum'</q>. If you're a bigger fan, you might be thinking "But Veritaserum is as clear as water, and that potion isn't!" That's right! The real reason I don't say "Veritaserum" is because this is actually a modified version of Veritaserum that Granger invented - it is similar, but its action is unaffected by the Veritaserum antidote, which is a distinct tactical advantage.</p><p>A more cynical person might speculate that Granger invented it to circumvent legal restrictions on the use of Veritaserum, but the law usually refers to truth potions in general, and as the head of the Auror Office, Granger can get the necessary warrants easily.</p>'''
  },
  {
    "transcript": [
      (1000, '''A single large image of <span class="dialogue HARRY">Harry Potter</span>, in a rigid chair. Harry's arms are bound to the arms of the chair by metal bands. Ze is barefoot and wearing a ragged grey tunic, zir hands are clenched, and zir hair is in disarray. Ze has a zigzag scar on zir forehead, and another, vertical scar at the left edge of zir mouth. There are dark shadows around zir eyes, and ze looks angry. Harry's speech is drawn almost as a scribble, with many jagged lines, in bright red.'''),
      (1000, '''HARRY: Ge' on wi' it... Grangeuh. { Get on with it, Granger. }'''),
      (3100, '''TITLE: Chapter One'''),
      (3450, 'TITLE: The Boy Who Killed'),
    ],
    "annotation": '''<p>Ah, Harry Potter.</p>

<p>How do you represent the speech of a character who pronounces words in a non-standard way? I hesitate to say <q>mispronounces</q>; if ze physically can't make the sounds that other people can make, is ze making an <em>error</em> by speaking?</p>

<p>I've chosen to represent it with a jagged, irregular writing style.</p>

<p>On this page, I've also chosen to misspell the words Harry speaks. Imagine if I did that on every page. The culture around us is full of prejudice against people who don't speak words the way they <q>should</q> be spoken. Others often mock them and disregard their opinions. But <i>Voldemort's Children</i> will not allow the reader to disregard Harry's opinion. I could put my readers in the position of taking someone seriously when they spoke misspelled words, which could be a good thing.</p>

<p>However, it would also make the comic harder to read. Ultimately, I decided that it wouldn't be worth the cost. As an author, I want my work to be as easy to read as possible. But as a viewer, if you only view things that have been made easy for you, you should be mindful of what you're missing.</p>''',
  },
  {
    "transcript": [
      (0, '''Granger and Tonks are looking down into Harry's cell.'''),
      (0, '''GRANGER: I'm not here to force tactical information out of you this time, Harry. I just want to learn about you. To understand you.'''),
      (682, '''HARRY: Rubbish! You think you understand me bloody well enough already. Don't think I've forgotten your answer to that speech Fudge made...'''),
      (1386, '''We enter a <span class="dialogue HARRY">narrative frame</span> in which Harry describes past events. In the past, Harry is sitting with two silhouetted figures, listening to a magical wireless radio.'''),
      (1600, 'HARRY: I was on the run then, but I still had a wizarding wireless...'),
      (1722, 'WIRELESS: &ndash;terrupt with an important message from the Minister of Magic, I repeat, the Minister of Magic himself will now address&ndash;'),
      (2660, '''We enter a <span class="dialogue WIRELESS">narrative frame</span> in which we have a direct view of the Minister of Magic, Cornelius Fudge, making zir speech. Fudge is standing at a podium on a raised platform, addressing an audience of at least 50 people, and probably more that we can't see. Fudge speaks in an excessively formal way.'''),
      (3090, 'FUDGE: Witches and wizards of Britain... It is my most regretful duty to inform you of the events of this morning... *ahem*... The notorious killer, Harry Potter, has made an attack on Hogwarts School of Witchcraft and Wizardry.')],
    "annotation": '''<p>You know you're reading an Eli Dupree comic when you enter two nested narrative frames on the same page.</p>''',
  },
  {
    "transcript": [
      (0, 'Fudge continues zir speech.'),
      (0, 'FUDGE: Potter and an unknown number of his allies invaded Hogwarts Castle just after midnight last night, massacring students and releasing Fiendfyre in the Hogwarts dungeon.'),
      (0, 'FUDGE: The following students are missing and presumed dead, their bodies destroyed in the cursed fire: Millicent Bulstrode, Vincent Crabbe, Daphne Greengrass, Draco Malfoy, Graham Montague, Pansy Parkinson, Charles Warrington, Blaise Zabini.'),
      (1400, 'FUDGE: The headmaster is injured by alive. We will now observe a moment of silence for the deceased.'),
      (1850, 'Time passes in silence, represented by an hourglass in a spiral.'),
      (2233, '''FUDGE: Potter and his allies, whoever they may be, have made themselves the enemy of wizarding society &ndash; an enemy such as we have not seen since the downfall of the self-styled Lord Voldemort over ten years ago. The older generations among us remember the name of Harry Potter as our salvation, but today, we have seen that Potter and his allies... are Voldemort's children.'''),
    ],
    "annotation":'''<p>When Fudge says <q>The downfall of the self-styled Lord Voldemort</q>, ze is referring to events when Harry was an infant.</p><p><i>Harry Potter</i> fans might find it strange that Fudge is willing to casually use the name <q>Voldemort</q>. I decided that the convention of being afraid to say zir name out loud didn't add to the themes I'm trying to push forward, and it's a bit of a confusing distraction. (By comparison, in the original series, that convention <em>does</em> add to a major theme &ndash; namely, the theme of overcoming one's fear. <i>Voldemort's Children</i> sneers at that theme.)</p>''',
  },
  {
    "transcript": [
      (0, 'Fudge continues zir speech.'),
      (0, 'FUDGE: A representative from the Auror Office will now brief you on our progress against this Dark enemy.'),
      (0, 'PAST GRANGER: Thank you, Mr Fudge. Sonorus!'),
      (0, '''{ "Sonorus" is the incantation for a spell that makes the caster's voice loud, as one would use to make a speech. }'''),
      (760, '''PRESENT HARRY: You weren't Head of Office yet, but everyone knew you would be.'''),
      (891, '''PAST GRANGER: With all respect to the Minister... The Auror Office believes that Potter is not a Dark Lord, but merely a self-aggrandizing serial killer motivated by petty revenge against those he believes have wronged him. Have we become so content since Voldemort's fall that <em>this</em> is what we imagine it must be like to live in a Dark Lord's shadow? Potter is running to hide from our Aurors even as we speak. In Voldemort's time...'''),
      (2550, '''We enter a <span class="dialogue GREY">narrative frame</span> in which Granger describes a time farther in the past, when <span class="dialogue VOLDEMORT">Voldemort</span> was in power. Voldemort is a tall person in dark robes, with no distinguishing features except that zir mouth is always a flat, expressionless line. The top of zir head is obscured in shadow, so that zir eyes cannot be seen. Ze wears a spiral object on a band around zir neck. Ze is followed by two animal companions: a bright green snake and a black cat with bright orange eyes. Zir wand is white, possibly bone or ivory. Zir speech is drawn in a very rigid style, with lots of straight lines and sharp corners.'''),
      (2728, 'VOLDEMORT: Avada kedavra.'),
      (2728, 'Voldemort is pointing zir wand at two other people and casting the Killing Curse, illuminating them with green light. One of them is hit. The other is running away.'),
      (3256, 'VOLDEMORT: Ha. Ha.'),
      (3762, '<span class="dialogue GREY">PAST GRANGER</span> { continuing zir speech }: <span class="dialogue GREY">...Aurors ran from <em>him</em>.</span>'),
    ],
    
    "annotation":'''<p>I'm pretty sure I've made Voldemort creepy enough.</p><p>The timeline here can be a bit confusing. Fiendfyre is an advanced spell, so the students must be relatively old, but the presumed-dead ones are all still at Hogwarts, so the most likely time for the attack is in (what would be) Harry's sixth year. So how is Granger an Auror already? When did Harry leave Hogwarts to become a notorious killer? Why didn't Voldemort return when ze did in the books? These questions will be answered in time.</p>''',
  },
]
for i in range(0,len(vc_pages)):
  vc_pages[i]["list_index"] = i

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
        '<body class="voldemorts_children">'+(
           vc_content_notice_bars_wrap({"comics":True}, vc_page["content_notice"], html) if "content_notice" in vc_page else
                        bars.bars_wrap({"comics":True},                            html)
        )+'</body>'
      )
    )
