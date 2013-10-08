#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import css
import top_bar
import utils

css.insert('''
div.bars_outer_box {
  min-height: 100%;
  position: relative;
}
div.bars_inner_box {
  padding-bottom: 5em;
}
@media screen and (max-width: 30em) {
  div.bars_inner_box { padding-bottom: 6em; } }
@media screen and (max-width: 20em) {
  div.bars_inner_box { padding-bottom: 7em; } }
@media screen and (max-width: 14em) {
  div.bars_inner_box { padding-bottom: 8em; } }
@media screen and (max-width: 13em) {
  div.bars_inner_box { padding-bottom: 9em; } }
@media screen and (max-width: 12em) {
  div.bars_inner_box { padding-bottom: 10em; } }

div.bottom_bar {
  position: absolute;
  bottom: 0;
  width: 100%;
  font-family: Arial, Helvetica, sans-serif;
  text-align: center;
  background-color: black;
  background-image: url("/media/top-bar-background.png");
  background-size: 100% 100%; }
.voldemorts_children div.bottom_bar {
  background-image: url("/media/top-bar-background-vc.png"); }
div.bottom_bar_inner {
  padding: 0.25em;
}

address.eli_exmxaxixl {
  display: inline;
  font-style: normal; }
''')

exmxaxixl_axdxrxexsxs = 'web&#64;el&#105;dupree&#00046;&#99;om'
def exmxaxixl_a(contents):
  return '<a href="ma&#73;ltO&#58;'+exmxaxixl_axdxrxexsxs+'">'+contents+'</a>'

def bottom_bar(info):
  return '<footer><div id="footer" class="bottom_bar'+(' '+info["extra_class"] if "extra_class" in info else '')+'"><div class="bottom_bar_inner">Please share this!'+utils.inline_separator+'<address class="eli_exmxaxixl">Contact: '+exmxaxixl_a(exmxaxixl_axdxrxexsxs)+'</address>'+utils.inline_separator+'<a href="/policies">Policies</a>'+utils.inline_separator+'<a href="https://github.com/elidupree/eliduprees-website-source">Website source (code CC-0, content CC-BY-SA)</a></div></div></footer>'

def bars_wrap(info, html):
  return '''<a class="skip" href="#footer">Skip to footer</a>
<div class="bars_outer_box">
  '''+top_bar.top_bar(info)+'''
  <div class="bars_inner_box">
    '''+html+'''
  </div>
  '''+bottom_bar(info)+'''
</div>'''
