#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import hashlib
#import scss

global all_scss
all_scss = '''@charset "UTF-8";
article,aside,figure,footer,header,hgroup,menu,nav,section{display:block;}
body,div,dl,dt,dd,ol,ul,li,h1,h2,h3,h4,h5,h6,pre,code,form,fieldset,legend,input,button,textarea,select,p,blockquote,th,td{margin:0;padding:0}
h1,h2,h3,h4,h5,h6{font-size:100%;font-weight:inherit;}
img{color:transparent;border:0;vertical-align:middle;-ms-interpolation-mode:bicubic;}
iframe {border:0;}

html,body {
  color:black; background-color:black;
  font-family: Times New Roman, Times, serif;
  height: 100%;
}
h1 { font-size: 300%; padding: 0.2em }
p { margin: 0.9em 0; line-height:1.35em; }
li { margin-left: 1.2em; }
.big_list>li { margin: 0.9em; margin-left: 1.2em; }
a:link { color:blue }
a:visited { color:purple }
.restore_link {text-decoration: underline;}
a:link .restore_link { color:blue }
a:visited .restore_link { color:purple }
img.background {
/* Using an img rather than "background-image:" because more browsers
render progressive JPEGs progressively for non-background images */
  position: absolute;
  position: fixed;
  display: block;
  top: 0;
  width: 100%;
  height: 100%;
  left: 0;
  right: 0;
}
a.skip {
  position: absolute;
  left: 0; top: 0;
  z-index: -1;
}
/* for things that should be apparent to screen readers, but are unnecessarily verbose for using the page visually; refer to
  http://adaptivethemes.com/using-css-clip-as-an-accessible-method-of-hiding-content */
.invisible {
  position: absolute !important;
  clip: rect(1px 1px 1px 1px); /* IE6, IE7 */
  clip: rect(1px, 1px, 1px, 1px);
}

span.title,cite { font-style: italic; }

html.javascript_enabled .noscript {display: none;}
html.javascript_disabled .script_required {display: none;}
'''

# previously   p { margin-top: 0.75em; margin-bottom: 0.75em; }

def insert(scss_snippet):
  global all_scss
  all_scss = all_scss + "\n" + scss_snippet
  
#global old_scss_hash
#old_scss_hash = None
def domain_relative_url():
  # for now, not changing anything about the filename:
  return "/media/style.css"
  #global old_scss_hash
  #scss_hash = hashlib.md5(all_scss).hexdigest()
  #if old_scss_hash is None:
  #  old_scss_hash = scss_hash
  #else:
  #  if scss_hash != old_scss_hash:
  #    raise Exception("Whoops! The CSS filename includes a hash of the file's contents, but the filename was queried twice, with more CSS having been added in between. That breaks the system.")
  #return "media/style-"+scss_hash+".css"

def build():
  return all_scss
  #return scss.parser.parse(all_scss)
