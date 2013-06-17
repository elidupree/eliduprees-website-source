import css

import html_pages
import top_bar

css.insert('''div.blog_post { border-top:1em solid gray; min-width:20em; max-width:35em; padding:0.75em; background-color:white; }''')
def fake_post():
  return '''<div class="blog_post"><h1>Post title</h1><p>Lorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum</p><p>dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conv</p></div>'''

css.insert("div.blog_right_bar { display:inline-block; vertical-align:top; width:14em; padding:0.75em; border:1.5em solid gray; border-left: 2em solid gray; border-right:2.5em solid gray; background-color:white; }")
right_bar = '''<div class="blog_right_bar"><a href="/403">[Random post] I foobar yesterday</a><p>something else</p></div>'''

css.insert("div.blog_left_padding { display:inline-block; max-width:12.75em; padding:0.75em; border:1.5em solid gray; background-color:white; }")
left_padding = '''<div class="blog_left_padding">dfjkdf kdfkjfdjkdfkj dfjkdf jkdf dfjk dfjk dfjkdf jkdf djfk dfkjdf kjdf jkfd dfkj dfjk dfjkdf jkdf kdfj dfjk</div>'''


css.insert('''div.blog_stream { display:inline-block; min-width:20em; max-width:35em; }
@media screen and (min-width: 40em) and (max-width: 65em) {
  div.blog_stream { position:absolute; right:20em; }
}''')
css.insert('''div.blog_stream_and_right_bar { float:right; }''')
css.insert('''div.blog_bottom { clear:both; }''')
css.insert('''div.blog_page { margin-left:auto; margin-right:auto; max-width:75em; background-color:gray; }''')
blog = '''<div class="blog_page"><div class="blog_stream_and_right_bar"><div class="blog_stream">
'''+fake_post()+fake_post()+fake_post()+fake_post()+fake_post()+fake_post()+'''</div>'''+right_bar+'''</div><div class="blog_bottom"></div></div>'''


def show_blog():
  return html_pages.make_page("Eli Dupree's website ⊃ Blog", "", top_bar.top_bar("blog")+blog)

