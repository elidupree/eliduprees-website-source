import css

import html_pages
import bars
import blog_posts

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

background_color = "#000000";

css.insert('''
div.blog_page_limits {
  position: relative;
  margin-left:auto; margin-right:auto;
  min-width:'''+str(min_space_for_two_columns_with_least_margins)+'''em;
  max-width:'''+str(page_max_width)+'''em; }

div.blog_stream_and_right_bar { float:right; }
div.blog_stream { display:inline-block;
  min-width:'''+str(post_padded_min_width)+'''em;
  max-width:'''+str(post_padded_max_width)+'''em;
  margin-left:''' +str(min_side_space_for_post)+'''em;
  margin-right:'''+str(min_side_space_for_post)+'''em; }
div.blog_bottom { clear:both; }

div.blog_right_bar {
  display:inline-block;
  vertical-align:top;
  width:'''+str(right_bar_content_width)+'''em;
  padding:'''+str(text_padding_width)+'''em;
  margin-top:1.5em;
  margin-right:'''+str(min_side_space_for_post)+'''em;
  background-color:white; }

@media screen and (max-width: '''+str(min_space_for_full_post_width)+'''em) {
  div.blog_stream    { margin-right:'''+str(max_side_space)+'''em; }
  div.blog_right_bar { margin-left:-'''+str(max_side_space-min_side_space_for_post)+'''em; }
}
@media screen and (max-width: '''+str(min_space_for_two_columns_and_all_margins)+'''em) {
  div.blog_stream { margin-left:0; width:'''+str(post_padded_min_width)+'''em; }
  div.blog_right_bar { margin-right:0; }
}
@media screen and (max-width: '''+str(min_space_for_two_columns_and_all_but_left_margin)+'''em) {
  div.blog_stream_and_right_bar { float:none; }
  div.blog_stream    { margin-right:'''+str(min_side_space_for_post)+'''em; }
  div.blog_right_bar { margin-left:0; }
}
@media screen and (max-width: '''+str(min_space_for_two_columns_and_all_but_side_margins)+'''em) {
  div.blog_stream    { margin-right:0; }
  div.blog_right_bar { float:right; }
}
  
div.blog_post {
  min-width:'''+str(post_content_min_width)+'''em;
  max-width:'''+str(post_content_max_width)+'''em;
  margin-top:'''+str(post_separation)+'''em;
  padding:'''+str(text_padding_width)+'''em;
  background-color:white; }
a.post_title_link { color:black; text-decoration:none; }

a:link.blog_end_link { color:yellow; }
a:visited.blog_end_link { color:orange; }
div.blog_end_links_2 {
  clear:both;
  margin-top:'''+str(post_separation/4)+'''em;
  margin-bottom:'''+str(post_separation+min_side_space_for_post)+'''em;
  text-align:center; }
a.blog_end_link.nav {
  display: inline-block;
  font-size: 200%;
  padding:'''+str(text_padding_width/4)+'''em;
  margin:'''+str(text_padding_width/4)+'''em; }
a.blog_end_link.nav.right {
  float:right; }
''')

def post_permalink(post_dict):
  return ""

def post_html(post_dict):
  return '<div class="blog_post"><h1><a class="post_title_link" href="'+post_permalink(post_dict)+'">'+post_dict["title"]+'</a></h1>'+post_dict["contents"]+'</div>'

def index_entry_html(post_dict):
  return '<div class="dict_entry"><a href="">'+post_dict["title"]+'</a></div>'

def fake_post():
  return '''<div class="blog_post"><h1>Post title</h1><p>Lorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum</p><p>dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conv</p></div>'''
  
def end_links():
  return '''
  <a href="" class="blog_end_link nav">Older posts</a>
  <a href="" class="blog_end_link nav right">Newer posts</a>
<div class="blog_end_links_2">
  <a class="blog_end_link" href="">Go back to the beginning and read in chronological order</a>
</div>'''
  
right_bar = '''<div class="blog_right_bar"><nav><a href="/403">[Random post] I foobar yesterday</a>'''+("\n".join([index_entry_html(p) for p in blog_posts.posts]))+'''</nav></div>'''

blog = '''<main><div class="blog_page"><div class="blog_page_limits"><div class="blog_stream_and_right_bar"><div class="blog_stream">
'''+("\n".join(['<article>'+post_html(p)+'</article>' for p in blog_posts.posts]))+end_links()+'''</div>'''+right_bar+'''</div><div class="blog_bottom"></div></div></div></main>'''


def show_blog():
  return html_pages.make_page("Eli Dupree's website ⊃ Blog", "", '<body><div><img role="presentation" alt="" class="background" src="/blog-background.jpg"></img></div>'+bars.bars_wrap("blog", blog)+'</body>')

