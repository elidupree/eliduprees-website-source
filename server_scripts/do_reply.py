#!/usr/local/bin/python

import errors
import blog_server_shared

def ajax_func():
  import os
  import re
  import forms
  import random
  import datetime
  import urllib
  import urllib2
  import secrets

  if os.environ["REQUEST_METHOD"] != "POST":
    raise error_stuff.WebsiteError("Oops! This request used a method that is not POST. Either there's a bug in my code, or you're trying to hack my website.")

  request_type = forms.ensure_presence_and_uniqueness_of_and_get_field("request_type")
  parent       = forms.ensure_presence_and_uniqueness_of_and_get_field("parent"      )
  username     = forms.ensure_presence_and_uniqueness_of_and_get_field("username"    )
  contents     = forms.ensure_presence_and_uniqueness_of_and_get_field("contents"    )
  secret_comment_identifier = forms.ensure_presence_and_uniqueness_of_and_get_field("secret_comment_identifier")
  last_secret_comment_identifier = forms.ensure_presence_and_uniqueness_of_and_get_field("last_secret_comment_identifier")
  

  preview_items = []
  
  reviewable_text = '''
{
  "parent":"'''+parent+'''",
  "username":"'''+username+'''",
  "contents":"""'''+re.sub('"""', r'\"\"\"', contents)+'''""",
  "id":"'''+hex(random.SystemRandom().getrandbits(128))[2:-1]+'''",
  "date_posted":datetime.date('''+datetime.date.today().strftime("%Y, %-m, %-d")+''')
},

Secret ID: '''+ secret_comment_identifier +'''
Last secret ID: '''+ last_secret_comment_identifier

  (postprocessed_string, scrutinies, broken_tags_marked) = blog_server_shared.postprocess_post_string(contents, None, None, True);
  if broken_tags_marked:
    preview_items.append('''<p>This post has <span class="skepticism">broken HTML tags</span>. (If you choose to leave them there, they will not be marked in the final post.)</p>''')
  if scrutinies > 0:
    preview_items.append('''<p>By the way, certain words are <span class="scrutiny">scrutinized</span> on this website. Each word links to an explanation of why I scrutinize it.</p>''')

  if request_type == "submit":
    response = urllib.urlopen ("https://maker.ifttt.com/trigger/elidupreecom_comment_posted/with/key/" + secrets.ifttt_maker_key, data = urllib.urlencode ({"value1": reviewable_text}))
    if response.getcode() != 200:
      raise WebsiteError ("Your comment failed to be delivered.")

  preview_items.append('<div class="comment_body">'+postprocessed_string+'</div>')

  return '''Content-type: text/plain; charset=utf-8

''' + "".join(preview_items)


print (errors.ajax_or_error(ajax_func))

