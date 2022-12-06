#!/usr/bin/python3
# -*- coding: utf-8 -*-

from post_contents_utils import *

fonts = [
    ["Literata", "normal", "400", "literata-v30-latin-regular"],
    ["Literata", "normal", "700", "literata-v30-latin-700"],
    ["Literata", "italic", "400", "literata-v30-latin-italic"],
    ["Gudea", "normal", "400", "gudea-v15-latin-regular"],
    ["Gudea", "normal", "700", "gudea-v15-latin-700"],
    ["Gudea", "italic", "400", "gudea-v15-latin-italic"],
    ["Alfa Slab One", "normal", "700", "alfa-slab-one-v17-latin-regular"],
    ["Lalezar", "normal", "700", "lalezar-v14-latin-regular"],
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
  font-family: 'Alfa Slab One', serif;
  font-size: 160%;
  text-align: center;
  padding-left: 0;
  padding-right: 0;
}
.story_content_warning_header {
  margin-top: 1.1em;
}
div.novel-current-status.novel-current-status.novel-current-status p, div.table_of_contents, div.table_of_contents p, div.hidden_cws, div.hidden_cws.hidden_cws.hidden_cws p, div.main_content_warnings p {
  font-family: Arial, Helvetica, sans-serif;
}
div.blog_post p {
  font-family: 'Literata', serif;
}
"""+fonts_css("/media/fonts/")+"""

  </style>
  """
