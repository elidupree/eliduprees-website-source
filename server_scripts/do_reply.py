#!/usr/local/bin/python3

import re
import errors
import blog_server_shared


html_tags_allowed_for_everyone = set(["q","blockquote","em","strong"])

chars_to_html_escapements = {
  "&":"&amp;",
  ">":"&gt;",
  "<":"&lt;",
  "\n":"<br/>",
}

# Unfortunately this function is NOT idempotent, so the user should not normally be shown its string output (though we can surely show them how it displays in HTML !)
# It escapes any tag that a normal poster isn't allowed to use.
# My own posting abilities allow me to post arbitrary HTML that does NOT go through this function.
def cleanup_post(post_string):
  # Use a only-this-is-okay model rather than an only-this-is-not-okay model so that the user can't throw me for a loop with a clever input
  open_tags = []
  approved_angle_brackets = set() # Only string indices that land in this set will allow angle brackets to remain on them unescaped.
  for matchinfo in re.finditer(r"</?([a-zA-Z]+)>", post_string):
    if matchinfo.group(0)[1] != "/":
      # we have an opening tag
      if matchinfo.group(1) in html_tags_allowed_for_everyone:
        open_tags.append(matchinfo)
    else:
      # we have a closing tag
      if len(open_tags) > 0:
        opened_tag = open_tags[len(open_tags) - 1]
        if matchinfo.group(1) == opened_tag.group(1):
          # Holy crap, we're actually closing the same tag, and that means we have a winnar!!!
          open_tags.pop()
          approved_angle_brackets.add(opened_tag.start(0))
          approved_angle_brackets.add(opened_tag.end(0)-1)
          approved_angle_brackets.add(matchinfo.start(0))
          approved_angle_brackets.add(matchinfo.end(0)-1)

  pieces = []
  for i in range(len(post_string)):
    c = post_string[i]
    if i in approved_angle_brackets:
      pieces.append(c)
    elif c in chars_to_html_escapements:
      pieces.append(chars_to_html_escapements[c])
    else:
      pieces.append(c)

  # We've now escaped all the things that need to be escaped.
  # We also take a moment to stop the user from doing something pointless that circumvents the word scrutiny.
  return re.sub(r"<em></em>|<strong></strong>|</em><em>|</strong><strong>", "", "".join(pieces))

def ajax_func():
  import os
  import sys
  import json
  import forms
  import random
  import datetime
  import urllib.request
  import urllib.parse
  import secrets

  if os.environ["REQUEST_METHOD"] != "POST":
    raise errors.WebsiteError("Oops! This request used a method that is not POST. Either there's a bug in my code, or you're trying to hack my website.")

  request_type = forms.ensure_presence_and_uniqueness_of_and_get_field("request_type")
  parent       = forms.ensure_presence_and_uniqueness_of_and_get_field("parent"      )
  username     = forms.ensure_presence_and_uniqueness_of_and_get_field("username"    )
  contents     = forms.ensure_presence_and_uniqueness_of_and_get_field("contents"    )
  secret_comment_identifier = forms.ensure_presence_and_uniqueness_of_and_get_field("secret_comment_identifier")
  last_secret_comment_identifier = forms.ensure_presence_and_uniqueness_of_and_get_field("last_secret_comment_identifier")
  
  contents = cleanup_post(contents)

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
  
  if sys.getsizeof(reviewable_text) > 100000:
    raise errors.WebsiteError("Oops! I don't support comments larger than about 100 kB.")

  (postprocessed_string, scrutinies, broken_tags_marked) = blog_server_shared.postprocess_post_string(contents, None, None, True);
  if broken_tags_marked:
    preview_items.append('''<p>This post has <span class="skepticism">broken HTML tags</span>. (If you choose to leave them there, they will not be marked in the final post.)</p>''')
  if scrutinies > 0:
    preview_items.append('''<p>By the way, certain words are <span class="scrutiny">scrutinized</span> on this website. Each word links to an explanation of why I scrutinize it.</p>''')

  if request_type == "submit":
    with open ("/home/public/secrets/recent_comments.txt", "a") as file:
      file.write (reviewable_text)
    response1 = urllib.request.urlopen(secrets.slack_incoming_webhook_url, data =
        urllib.parse.urlencode({"payload": json.dumps({
            "text": "@elidupree There is a new comment!"
        })}).encode("utf-8"))
    response2 = urllib.request.urlopen ("https://maker.ifttt.com/trigger/elidupreecom_comment_posted/with/key/" + secrets.ifttt_maker_key, data = urllib.parse.urlencode ({"value1": reviewable_text}).encode("utf-8"))
    if response1.getcode() != 200 and response2.getcode() != 200:
      raise errors.WebsiteError ("Your comment failed to be delivered.")

  preview_items.append('<div class="comment_body">'+postprocessed_string+'</div>')

  return '''Content-type: text/plain; charset=utf-8

''' + "".join(preview_items)


print (errors.ajax_or_error(ajax_func))

