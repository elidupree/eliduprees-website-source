#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

import css
import javascript

css.insert('''
div.comic_content_notice_box {
  height: 100%; }
body.content_notices_disabled div.comic_content_notice_box {
  height: auto; }
body.content_notice_dismissed div.comic_content_notice_box {
  height: auto; }
div.comic_content_notice_text {
  margin: 0 auto;
  padding: 6.5em 0;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
  text-align: center; }
.content_notices_disabled div.comic_content_notice_text {
  display: none; }
.content_notice_dismissed div.comic_content_notice_text {
  display: none; }
div.comic_content_notice_main_text a {
  color: #ffc800; }
div.comic_content_notice_main_text {
  font-size: 120%;
  margin: 0 auto;
  max-width: 35em;
  border: 3px solid white;
  border-radius: 2em; }
div.comic_content_notice_details {
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
  padding: 0.5em; }
body.content_notices_disabled a.disable_content_notices {
  display: none; }
div.comic_box_after_content_notice {
  position: relative; }
div.comic_toggle_content_notices {
  margin-top: 1em;
  text-align: center; }
.remove_if_content_notices_enabled {
  display: none; }
body.content_notices_disabled .remove_if_content_notices_enabled {
  display: block; }
body.content_notices_disabled .remove_if_content_notices_disabled {
  display: none; }
  
''')

javascript.do_before_body('''
window.elidupree.show_transcript = function() {
  remove_class(document.body, 'transcripts_hidden');
  delete_cookie('transcripts_hidden');
};
window.elidupree.hide_transcript = function() {
  document.body.className += ' transcripts_hidden';
  set_cookie('transcripts_hidden', 'true', 30);
};
window.elidupree.enable_content_notices = function() {
  remove_class(document.body, 'content_notices_disabled');
  delete_cookie('content_notices_disabled');
};
window.elidupree.disable_content_notices = function() {
  document.body.className += ' content_notices_disabled';
  set_cookie('content_notices_disabled', 'true', 30);
};
if (read_cookie('content_notices_disabled')) {
  window.elidupree.disable_content_notices();
}
if (read_cookie('transcripts_hidden')) {
  window.elidupree.hide_transcript();
}
''')
javascript.do_after_body('''
var show_transcript_button   = document.getElementById('show_transcript_button'  );
var hide_transcript_button   = document.getElementById('hide_transcript_button'  );
var hide_transcript_button_2 = document.getElementById('hide_transcript_button_2');
if (show_transcript_button  ) { add_event_listener(show_transcript_button  ,'click',window.elidupree.show_transcript); }
if (hide_transcript_button  ) { add_event_listener(hide_transcript_button  ,'click',window.elidupree.hide_transcript); }
if (hide_transcript_button_2) { add_event_listener(hide_transcript_button_2,'click',window.elidupree.hide_transcript); }
var disable_content_notices_event = function(id) {
  var disable_content_notices_button = document.getElementById(id);
  if (disable_content_notices_button) { add_event_listener(disable_content_notices_button,'click',window.elidupree.disable_content_notices); }
};
var enable_content_notices_event = function(id) {
  var enable_content_notices_button = document.getElementById(id);
  if (enable_content_notices_button) { add_event_listener(enable_content_notices_button,'click',window.elidupree.enable_content_notices); }
};
disable_content_notices_event('disable_content_notices_button_next'    );
disable_content_notices_event('disable_content_notices_button_previous');
disable_content_notices_event('disable_content_notices_button_toggle'  );
 enable_content_notices_event( 'enable_content_notices_button_toggle'  );

var view_the_comic_p = document.getElementById('view_the_comic_p');
if (view_the_comic_p) {
  var dismiss_content_notice_a = document.createElement('a');
  dismiss_content_notice_a.className = 'dismiss_content_notice';
  dismiss_content_notice_a.setAttribute('href','javascript:;');
  dismiss_content_notice_a.appendChild(document.createTextNode('View the comic'));
  view_the_comic_p.replaceChild(dismiss_content_notice_a, view_the_comic_p.firstChild);
  add_event_listener(dismiss_content_notice_a,'click',function() { document.body.className += ' content_notice_dismissed'; });
  
  var disable_content_notices_p = document.getElementById('disable_content_notices_p');
  if (cookies_enabled) {
    var disable_content_notices_a = document.createElement('a');
    disable_content_notices_a.className = 'comic_disable_content_notices';
    disable_content_notices_a.setAttribute('href','javascript:;');
    disable_content_notices_a.appendChild(document.createTextNode('Disable content notices'));
    disable_content_notices_p.replaceChild(disable_content_notices_a, disable_content_notices_p.firstChild);
    add_event_listener(disable_content_notices_a,'click',window.elidupree.disable_content_notices);
  }
  else {
    disable_content_notices_p.firstChild.nodeValue = 'You could disable content notices if you had cookies enabled.'
  }
}
''')

import top_bar
import bars
import html_pages
  
def content_notice_bars_wrap(info, notice, html):
  return '''<a class="skip" href="#footer">Skip to footer</a>
<div class="comic_content_notice_box">
  '''+top_bar.top_bar(info)+'''
  <section>
    <div class="comic_content_notice_text">
      <div class="comic_content_notice_main_text">
        <p>The comic below '''+notice+'''</p>
        <p id="view_the_comic_p">Scroll down to view the comic.</p>
      </div>
      <div class="comic_content_notice_details">
        <p id="disable_content_notices_p">You could disable content notices if you had Javascript and cookies enabled.</p>
      </div>
    </div>
  </section>
</div>
<div class="comic_box_after_content_notice">
  <div class="bars_inner_box">
    '''+html+'''
  </div>
  '''+bars.bottom_bar(info)+'''
</div>'''

def bars_wrap(info, html, page):
  return (content_notice_bars_wrap({"comics":True}, page["content_notice"], html) if "content_notice" in page else
                    bars.bars_wrap({"comics":True},                         html))



