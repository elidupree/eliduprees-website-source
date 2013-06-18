import css

import html_pages
import top_bar

page_max_width = 75
post_content_min_width = 20
post_content_max_width = 35
text_padding_width = 0.75
post_padded_min_width = post_content_min_width + (2*text_padding_width)
post_padded_max_width = post_content_max_width + (2*text_padding_width)
post_separation = 1
max_side_space = (page_max_width - post_padded_max_width) / 2
min_side_space_for_post = 2
maximally_pinched_margin = 0.5
right_bar_padded_width = max_side_space - 2*(min_side_space_for_post)
right_bar_content_width = right_bar_padded_width - (2*text_padding_width)

min_space_for_full_post_width = min_side_space_for_post + post_padded_max_width + max_side_space
min_space_for_two_columns_and_all_margins = min_side_space_for_post + post_padded_min_width + max_side_space
min_space_for_two_columns_and_all_but_left_margin = min_space_for_two_columns_and_all_margins - min_side_space_for_post
min_space_for_two_columns_and_all_but_side_margins = min_space_for_two_columns_and_all_but_left_margin - min_side_space_for_post
min_space_for_two_columns_with_least_margins = min_space_for_two_columns_and_all_but_side_margins - min_side_space_for_post + maximally_pinched_margin

css.insert("div.blog_post { border-top:"+str(post_separation)+"em solid gray; padding:"+str(text_padding_width)+"em; background-color:white; }")
def fake_post():
  return '''<div class="blog_post"><h1>Post title</h1><p>Lorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum</p><p>dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conv</p></div>'''

css.insert('''
div.blog_right_bar {
  display:inline-block;
  vertical-align:top;
  width:'''+str(right_bar_content_width)+'''em;
  padding:'''+str(text_padding_width)+'''em;
  border:1.5em solid gray;
  border-left:0;
  border-right:'''+str(min_side_space_for_post)+'''em solid gray;
  background-color:white; }''')
right_bar = '''<div class="blog_right_bar"><a href="/403">[Random post] I foobar yesterday</a><p>something else</p></div>'''


css.insert('''
div.blog_stream { display:inline-block;
  min-width:'''+str(post_padded_min_width)+'''em;
  max-width:'''+str(post_padded_max_width)+'''em;
  border-left:''' +str(min_side_space_for_post)+'''em solid gray;
  border-right:'''+str(min_side_space_for_post)+'''em solid gray; }
div.blog_stream_and_right_bar { float:right; }
div.blog_bottom { clear:both; }
div.blog_page { margin-left:auto; margin-right:auto; min-width:'''+str(min_space_for_two_columns_with_least_margins)+'''em; max-width:'''+str(page_max_width)+'''em; background-color:gray; }

@media screen and (max-width: '''+str(min_space_for_full_post_width)+'''em) {
  div.blog_stream    { margin-right:'''+str(max_side_space-min_side_space_for_post)+'''em; }
  div.blog_right_bar { margin-left:-'''+str(max_side_space-min_side_space_for_post)+'''em; }
}
@media screen and (max-width: '''+str(min_space_for_two_columns_and_all_margins)+'''em) {
  div.blog_stream { border-left:0; width:'''+str(post_padded_min_width)+'''em; }
  div.blog_right_bar { border-right:0; }
}
@media screen and (max-width: '''+str(min_space_for_two_columns_and_all_but_left_margin)+'''em) {
  div.blog_stream_and_right_bar { float:none; }
  div.blog_stream    { margin-right:0; }
  div.blog_right_bar { margin-left:0; }
}
@media screen and (max-width: '''+str(min_space_for_two_columns_and_all_but_side_margins)+'''em) {
  div.blog_stream    { border-right:0; }
  div.blog_right_bar { float:right; }
}
''')

blog = '''<div class="blog_page"><div class="blog_stream_and_right_bar"><div class="blog_stream">
'''+fake_post()+fake_post()+fake_post()+fake_post()+fake_post()+fake_post()+'''</div>'''+right_bar+'''</div><div class="blog_bottom"></div></div>'''


def show_blog():
  return html_pages.make_page("Eli Dupree's website ⊃ Blog", "", top_bar.top_bar("blog")+blog)

