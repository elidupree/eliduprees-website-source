#!/usr/bin/python3
# -*- coding: utf-8 -*-

from post_contents_utils import *

yali_font = "Kreon" #"Roboto Slab"
rinn_font = "Kadwa" #"Arvo" #"Inika" #"Crete Round"
chapter_font = "Alegreya SC"

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
div.blog_post div.clear {
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
  /*font-style: italic;*/
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

/* For the emoji graphics, we currently use twemoji (https://github.com/twitter/twemoji). */
div.blog_post img.emoji {
  display: inline-block;
  width: 1em;
  height: 1em;
  margin: 0;
  vertical-align: middle;
}

html.debug_mode div.blog_post p.unnecessary_page_number {
  display: block;
  text-align: center;
  font-size: smaller;
  font-family: Arial, Helvetica, sans-serif;
  padding-bottom: 1.5em;
}

/* kadwa-regular - latin */
@font-face {
  font-family: 'Kadwa';
  font-style: normal;
  font-weight: 400;
  src: url('/media/fonts/kadwa-v5-latin-regular.eot?rr'); /* IE9 Compat Modes */
  src: local(''),
       url('/media/fonts/kadwa-v5-latin-regular.eot?#iefix?rr') format('embedded-opentype'), /* IE6-IE8 */
       url('/media/fonts/kadwa-v5-latin-regular.woff2?rr') format('woff2'), /* Super Modern Browsers */
       url('/media/fonts/kadwa-v5-latin-regular.woff?rr') format('woff'), /* Modern Browsers */
       url('/media/fonts/kadwa-v5-latin-regular.ttf?rr') format('truetype'), /* Safari, Android, iOS */
       url('/media/fonts/kadwa-v5-latin-regular.svg#Kadwa?rr') format('svg'); /* Legacy iOS */
}

/* kadwa-700 - latin */
@font-face {
  font-family: 'Kadwa';
  font-style: normal;
  font-weight: 700;
  src: url('/media/fonts/kadwa-v5-latin-700.eot?rr'); /* IE9 Compat Modes */
  src: local(''),
       url('/media/fonts/kadwa-v5-latin-700.eot?#iefix?rr') format('embedded-opentype'), /* IE6-IE8 */
       url('/media/fonts/kadwa-v5-latin-700.woff2?rr') format('woff2'), /* Super Modern Browsers */
       url('/media/fonts/kadwa-v5-latin-700.woff?rr') format('woff'), /* Modern Browsers */
       url('/media/fonts/kadwa-v5-latin-700.ttf?rr') format('truetype'), /* Safari, Android, iOS */
       url('/media/fonts/kadwa-v5-latin-700.svg#Kadwa?rr') format('svg'); /* Legacy iOS */
}

/* kreon-regular - latin */
@font-face {
  font-family: 'Kreon';
  font-style: normal;
  font-weight: 400;
  src: url('/media/fonts/kreon-v24-latin-regular.eot'); /* IE9 Compat Modes */
  src: local(''),
       url('/media/fonts/kreon-v24-latin-regular.eot?#iefix?rr') format('embedded-opentype'), /* IE6-IE8 */
       url('/media/fonts/kreon-v24-latin-regular.woff2?rr') format('woff2'), /* Super Modern Browsers */
       url('/media/fonts/kreon-v24-latin-regular.woff?rr') format('woff'), /* Modern Browsers */
       url('/media/fonts/kreon-v24-latin-regular.ttf?rr') format('truetype'), /* Safari, Android, iOS */
       url('/media/fonts/kreon-v24-latin-regular.svg#Kreon?rr') format('svg'); /* Legacy iOS */
}

/* kreon-700 - latin */
@font-face {
  font-family: 'Kreon';
  font-style: normal;
  font-weight: 700;
  src: url('/media/fonts/kreon-v24-latin-700.eot?rr'); /* IE9 Compat Modes */
  src: local(''),
       url('/media/fonts/kreon-v24-latin-700.eot?#iefix?rr') format('embedded-opentype'), /* IE6-IE8 */
       url('/media/fonts/kreon-v24-latin-700.woff2?rr') format('woff2'), /* Super Modern Browsers */
       url('/media/fonts/kreon-v24-latin-700.woff?rr') format('woff'), /* Modern Browsers */
       url('/media/fonts/kreon-v24-latin-700.ttf?rr') format('truetype'), /* Safari, Android, iOS */
       url('/media/fonts/kreon-v24-latin-700.svg#Kreon?rr') format('svg'); /* Legacy iOS */
}

/* alegreya-sc-800 - latin */
@font-face {
  font-family: 'Alegreya SC';
  font-style: normal;
  font-weight: 800;
  src: url('/media/fonts/alegreya-sc-v15-latin-800.eot?rr'); /* IE9 Compat Modes */
  src: local(''),
       url('/media/fonts/alegreya-sc-v15-latin-800.eot?#iefix?rr') format('embedded-opentype'), /* IE6-IE8 */
       url('/media/fonts/alegreya-sc-v15-latin-800.woff2?rr') format('woff2'), /* Super Modern Browsers */
       url('/media/fonts/alegreya-sc-v15-latin-800.woff?rr') format('woff'), /* Modern Browsers */
       url('/media/fonts/alegreya-sc-v15-latin-800.ttf?rr') format('truetype'), /* Safari, Android, iOS */
       url('/media/fonts/alegreya-sc-v15-latin-800.svg#AlegreyaSC?rr') format('svg'); /* Legacy iOS */
}


  </style>
  """
