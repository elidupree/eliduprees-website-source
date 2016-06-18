#!/usr/local/bin/python

import errors
import blog_server_shared

def ajax_func():
  import os
  import re
  import forms

  if os.environ["REQUEST_METHOD"] != "POST":
    raise error_stuff.WebsiteError("Oops! This request used a method that is not POST. Either there's a bug in my code, or you're trying to hack my website.")

  request_type = forms.ensure_presence_and_uniqueness_of_and_get_field("request_type")
  parent       = forms.ensure_presence_and_uniqueness_of_and_get_field("parent"      )
  username     = forms.ensure_presence_and_uniqueness_of_and_get_field("username"    )
  contents     = forms.ensure_presence_and_uniqueness_of_and_get_field("contents"    )

  preview_items = []
  
  dict_entry_text = '''
{
  "parent":"'''+parent+'''",
  "username":"'''+username+'''",
  "contents":"""'''+re.sub('"""', r'\"\"\"', contents)+'''""",
  "id":"'''+hex(random.SystemRandom().getrandbits(128))[2:-1]+'''",
  "date_posted":datetime.date('''+datetime.date.today().strftime("%Y, %-m, %-d")+''')
},'''

  (postprocessed_string, scrutinies, broken_tags_marked) = blog_server_shared.postprocess_post_string(contents, None, None, True);
  if broken_tags_marked:
    preview_items.append('''<p>This post has <span class="skepticism">broken HTML tags</span>. (If you choose to leave them there, they will not be marked in the final post.)</p>''')
  if scrutinies > 0:
    preview_items.append('''<p>By the way, certain words are <span class="scrutiny">scrutinized</span> on this website. Each word links to an explanation of why I scrutinize it.</p>''')

  preview_items.append('<div class="comment_body">'+postprocessed_string+'</div>')

  return '''Content-type: text/plain; charset=utf-8

''' + "".join(preview_items)


print errors.ajax_or_error(True, ajax_func)

