#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division



#import scss

global all_scss
all_scss = '''
article,aside,figure,footer,header,hgroup,menu,nav,section{display:block;}
body,div,dl,dt,dd,ul,li,h1,h2,h3,h4,h5,h6,pre,code,form,fieldset,legend,input,button,textarea,select,p,blockquote,th,td{margin:0;padding:0}
h1,h2,h3,h4,h5,h6{font-size:100%;font-weight:inherit;}
img{color:transparent;border:0;vertical-align:middle;-ms-interpolation-mode:bicubic;}

html,body {
  color:black; background-color:black;
  font-family: Times New Roman, Times, serif;
  height: 100%;
}
ol { margin: 0; }
h1 { font-size: 300%; padding: 0.2em }
p { margin: 0.9em 0; line-height:1.35em; }
a:link { color:blue }
a:visited { color:purple }
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
'''

# previously   p { margin-top: 0.75em; margin-bottom: 0.75em; }

def insert(scss_snippet):
  global all_scss
  all_scss = all_scss + "\n" + scss_snippet
  
def filename():
  return "media/style.css"
def build():
  return all_scss
  #return scss.parser.parse(all_scss)
