#!/usr/bin/python3
# -*- coding: utf-8 -*-

from post_contents_utils import *

yali_font = "Kreon" #"Roboto Slab"
rinn_font = "Kadwa" #"Arvo" #"Inika" #"Crete Round"
chapter_font = "Alegreya SC"

def who_tells_the_story(who):
  return f'''
  <table class="who-tells-the-story-box">
    <tr>
      <td class="who-tells-the-story-sidepoint"><img src="/media/ravelling-wrath/symbols/section-break-left-point.png?rr" alt="" /></td>
      <td class="who-tells-the-story">{who} tells the story</td>
      <td class="who-tells-the-story-sidepoint"><img src="/media/ravelling-wrath/symbols/section-break-right-point.png?rr" alt="" /></td>
    </tr>
  </table>'''


fonts = [
    ["Kadwa", "normal", "400", "kadwa-v5-latin-regular"],
    ["Kadwa", "normal", "700", "kadwa-v5-latin-700"],
    ["Kreon", "normal", "400", "kreon-v24-latin-regular"],
    ["Kreon", "normal", "700", "kreon-v24-latin-700"],
    ["Alegreya Sans", "normal", "400", "alegreya-sans-v14-latin-regular"],
    ["Alegreya Sans", "normal", "800", "alegreya-sans-v14-latin-800"],
    ["Alegreya SC", "normal", "400", "alegreya-sc-v15-latin-regular"],
    ["Alegreya SC", "normal", "800", "alegreya-sc-v15-latin-800"],
    ["Alegreya Sans SC", "normal", "800", "alegreya-sans-sc-v13-latin-800"],
    ["Lexend", "normal", "400", "lexend-v12-latin-regular"],
    ["Lexend", "normal", "700", "lexend-v12-latin-700"],
    ["Lexend", "normal", "900", "lexend-v12-latin-900"],
  ]

def fonts_css(fonts_path, mode="web"):
  return "\n\n".join(
    font_face(family, style, weight, fonts_path+name_style, mode)
    for family, style, weight, name_style
    in fonts
  )


head = """<style>

.table_of_contents_chapter {
  text-indent: 2em;
}
.table_of_contents_chapter .chapter_link {
  margin-right: 0.3em;
}
.table_of_contents_remaining {
  text-indent: 2em;
  font-style: italic;
}
div.blog_post h1 {
  text-align: center;
  padding-left: 0;
  padding-right: 0;
}
div.blog_post h2 {
  text-align: center;
  padding-left: 0;
  padding-right: 0;
  font-weight: 800;
  font-family: '"""+chapter_font+"""', serif;
}
div.blog_post p {
  clear: both;
}
div.blog_post img {
  display: block;
  margin: 2.8em auto;
  max-width: 100%;
}
div.blog_post div.end-of-texts {
  clear: both;
}
div.blog_post p.text {
  border-radius: 1.3em;
  max-width: 60%;
  text-indent: 0;
  padding: 6px 12px;
  margin: 1px 0;
  font-family: Arial, Helvetica, sans-serif;
}
p.text.right {
  background-color: #87e520;
  float: right;
}
p.text.left {
  background-color: #e5e4e4;
  float: left;
}
.story_content_warning_header {
  margin-top: 1.1em;
}
div.blog_post p {
  font-family: '"""+rinn_font+"""', serif;
}
div.blog_post.yali-narration p, .yali-narration.yali-narration.yali-narration p {
  /*font-family: Georgia, serif;*/
  font-family: '"""+yali_font+"""', serif;
  font-size: 112%;
  /*font-style: italic;*/
  line-height: 1.3em;
}
/*.yali-narration em {
font-weight: bold;
}*/
div.novel-current-status.novel-current-status.novel-current-status p, div.table_of_contents, div.table_of_contents p, div.hidden_cws, div.hidden_cws.hidden_cws.hidden_cws p, div.main_content_warnings p {
  font-family: Arial, Helvetica, sans-serif;
}
.prayer {
  text-align: center;
}
div.blog_post .prayer p {
  text-indent: 0;
}

div.blog_post img.emoji {
  display: inline-block;
  width: 1.5em;
  height: 1.5em;
  margin: 0 -.125em;
  vertical-align: middle;
}

div.blog_post img.rav-section-break {
  width: 90%;
  height: auto;
  margin: 2em auto;
}
div.blog_post img.rav-section-break.nonaligned {
  width: 80%;
}

div.blog_post .who-tells-the-story-box {
  width: 95%;
  margin: 0 auto;
  margin-top: 3em;
}
div.blog_post .who-tells-the-story-sidepoint {
  padding: 0;
  width: 50%;
}
div.blog_post .who-tells-the-story {
  font-family: '"""+rinn_font+"""', serif;
  font-size: 158%;
  font-variant-caps: small-caps;
  text-align: center;
  white-space: nowrap;
  padding: 0 0.6em;
}
div.blog_post .who-tells-the-story-box img {
  margin: 0;
  max-width: 100%;
}

div.blog_post.yali-narration who-tells-the-story {
  font-family: '"""+yali_font+"""', serif;
}

html.debug_mode div.blog_post p.unnecessary_page_number {
  display: block;
  text-align: center;
  font-size: smaller;
  font-family: Arial, Helvetica, sans-serif;
  padding-bottom: 1.5em;
}

"""+fonts_css("/media/fonts/")+"""


  </style>
  """
