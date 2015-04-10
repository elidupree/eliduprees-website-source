#!/usr/local/bin/python

import errors
import blog_server_shared

def ajax_func():
  import os
  import forms

  if os.environ["REQUEST_METHOD"] != "POST":
    raise error_stuff.WebsiteError("Oops! This request used a method that is not POST. Either there's a bug in my code, or you're trying to hack my website.")

  request_type = forms.ensure_presence_and_uniqueness_of_and_get_field("request_type")
  parent       = forms.ensure_presence_and_uniqueness_of_and_get_field("parent"      )
  username     = forms.ensure_presence_and_uniqueness_of_and_get_field("username"    )
  contents     = forms.ensure_presence_and_uniqueness_of_and_get_field("contents"    )

  preview_items = ["<p><strong>This is a preview. Your post has not yet been posted.</strong></p>"]

  (postprocessed_string, scrutinies, broken_tags_marked) = blog_server_shared.postprocess_post_string(contents, None, None, True);
  if broken_tags_marked:
    preview_items.append('''<p>This post has broken HTML tags. In this preview, I have drawn them with a <span class="skepticism">mark of my skepticism</span>. If you choose to leave them there, they will not be marked in the final post.</p>''')
  if scrutinies > 0:
    preview_items.append('''<p>By the way, I'm having my website <span class="scrutiny">scrutinize</span> certain words. They're perfectly reasonable words, but I'm keeping an eye on them because I think they go unquestioned a little too often. I've put a <span class="scrutiny">mark of my scrutiny</span> on each of them, and also made each of them a link to a blog post where I talk about why I'm scrutinizing it. If you leave the scrutinized words there, they'll still be marked in your final post, unless you put them in quotes using &lt;q&gt; or &lt;blockquote&gt;.</p>''')

  preview_items.append('<div class="comment_body">'+postprocessed_string+'</div>')

  return '''Content-type: text/plain; charset=utf-8

''' + "".join(preview_items)


print errors.ajax_or_error(True, ajax_func)

