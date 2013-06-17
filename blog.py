import css

import html_pages
import top_bar

css.insert("div.blog_post { margin-left:auto; margin-right:auto; border-top:1em solid gray; min-width:20em; max-width:35em; padding:0.75em; background-color:white; }")
def fake_post():
  return '''<div class="blog_post"><h1>Post title</h1><p>Lorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum</p><p>dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conv</p></div>'''

css.insert("div.blog_leftbar_thingy { float:right; width:13.75em; padding:0.75em; border:1.5em solid gray; background-color:white; }")
leftbar_thingy = '''<div class="blog_leftbar_thingy"><a href="/403">[Random post] I foobar yesterday</a><p>something else</p></div>'''

css.insert("div.blogstream { margin-left:auto; margin-right:auto; max-width:75em; background-color:gray; }")
blog = '''<div class="blogstream">
'''+leftbar_thingy+fake_post()+fake_post()+fake_post()+fake_post()+fake_post()+fake_post()+'''</div>'''


def show_blog():
  return html_pages.make_page("Eli Dupree's website ⊃ Blog", "", top_bar.top_bar("blog")+blog)

