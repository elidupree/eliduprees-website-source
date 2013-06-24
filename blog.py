import css

import html_pages
import bars
import blog_posts
import utils
import tags

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
metacontent_color_IE8 = "#bbbbbb"
metacontent_color = "rgba(255,255,255,.7)"

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
  background-color:'''+metacontent_color_IE8+''';
  background-color:'''+metacontent_color+'''; }

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
  background-color: white; }
a.post_title_link { color:black; text-decoration:none; }
div.blog_post p {
  text-indent: 2em; }
div.blog_post_metadata_outer {
  min-width:'''+str(post_content_min_width)+'''em;
  max-width:'''+str(post_content_max_width)+'''em;
  padding: 0 0.8em;
  margin-bottom:'''+str(post_separation)+'''em; }
div.blog_post_metadata {
  font-size: 80%;
  padding:'''+str(text_padding_width)+'''em;
  background-color:'''+metacontent_color_IE8+''';
  background-color:'''+metacontent_color+'''; }

a:link.blog_end_link { color:yellow; }
a:visited.blog_end_link { color:orange; }
div.blog_end_links_2 {
  clear:both;
  margin-top:'''+str(post_separation/4)+'''em;
  text-align:center; }
a.blog_end_link.nav {
  display: inline-block;
  font-size: 200%;
  padding:'''+str(text_padding_width/2)+'''em '''+str(text_padding_width/4)+'''em; }
a.blog_end_link.nav.right {
  float:right; }

div.blog_index {
  padding: 0.8em 0; }
''')

def post_permalink(post_dict):
  return "/blog/"+url_formatted_title(post_dict)
def post_div_id(post_dict):
  return url_formatted_title(post_dict)
  
def post_html(post_dict):
  return '<div id="'+post_div_id(post_dict)+'" class="blog_post"><h1><a class="post_title_link" href="'+post_permalink(post_dict)+'">'+post_dict["title"]+'</a></h1>'+post_dict["contents"]+'</div><div class="blog_post_metadata_outer"><div class="blog_post_metadata">'+('Tags: '+(", ".join(tags.tag_link(tag) for tag in post_dict["tags"]))+utils.inline_separator if "tags" in post_dict else "")+'Posted May 14, 2015'+utils.inline_separator+'<a rel="bookmark" href="'+post_permalink(post_dict)+'">Permalink</a>'+utils.inline_separator+'<a href="">Comments&nbsp;(14)</a>'+'</div></div>'

def index_entry_html(post_dict):
  return '<div class="index_entry"><a href="">'+post_dict["title"]+'</a></div>'


def make_blog_page_body(main_contents, sidebar_contents):
  return '<body><a class="skip" href="#content">Skip to content</a><a class="skip" href="#blog-sidebar">Skip to blog sidebar</a><div><img role="presentation" alt="" class="background" src="/media/blog-background.jpg"></img></div>'+bars.bars_wrap({"blog":True}, '<main><div id="content" class="blog_page"><div class="blog_page_limits"><div class="blog_stream_and_right_bar"><div class="blog_stream">'+main_contents+'</div><div id="blog-sidebar" class="blog_right_bar">'+sidebar_contents+'</div></div><div class="blog_bottom"></div></div></div></main>')+'</body>'

  
def url_formatted_title(post_dict):
  return utils.format_for_url(post_dict["title"])
def title_formatted_title(post_dict):
  return utils.strip_tags(post_dict["title"])

def add_blog_pages(page_dict, tag_specific = None):
  if tag_specific:
    posts = tag_specific["post_list"]
  else:
    posts = blog_posts.posts
    posts_by_tag = {}
    for tag in tags.tags:
      posts_by_tag[tag] = []
  
  current_page_number = 1
  current_page = []
  index = ('<div class="blog_index">'
    +('Posts tagged &quot;'+tag_specific["tagname"]+'&quot;:' if tag_specific else 'All posts:')
    +("\n".join([index_entry_html(p) for p in reversed(posts)]))
    +'</div>')
  for i in range(0,len(posts)):
    post_dict = posts[i]
    current_page.append('<article>'+post_html(post_dict)+'</article>')
    
    page_length = 10
    latest_page_max_posts = page_length + 5
    remaining_posts = len(posts) - i
    on_latest_page = (len(current_page) + remaining_posts <= latest_page_max_posts)
    print_older_page = ((len(current_page) >= page_length) and not on_latest_page)
    print_latest_page = (i == len(posts) - 1)
    if print_older_page and print_latest_page:
      raise "This code is messed up somehow"
    
    if on_latest_page:
      url_pagenum_string = ''
    else:
      url_pagenum_string = '/page/'+str(current_page_number)
      
    if tag_specific:
      tags_string = '/tags/'+tag_specific["tagname"]
    else:
      tags_string = ''
    
    if print_older_page or print_latest_page:
      for page_order in ('','/chronological'):
        end_links = ''
        if current_page_number > 1:
          end_links = (end_links+'<a href="/blog'+tags_string+'/page/'+str(current_page_number-1)+page_order+
            '" rel="prev" class="blog_end_link nav">Older posts</a>')
        if print_older_page:
          end_links = (end_links+'<a href="/blog'+tags_string+('/page/'+str(current_page_number+1)+page_order if (remaining_posts > latest_page_max_posts) else page_order)+
            '" rel="next" class="blog_end_link nav right">Newer posts</a>')
        if current_page_number > 1:
          end_links = end_links+'''
<div class="blog_end_links_2">
  <a class="blog_end_link" href="/blog'''+tags_string+'''/page/1/chronological">Go back to the beginning and read in chronological order</a>
</div>'''
        elif (page_order != '/chronological') and (len(posts) > 1):
          end_links = end_links+'''
<div class="blog_end_links_2">
  <a class="blog_end_link" href="/blog'''+tags_string+'''/page/1/chronological">Read in chronological order</a>
</div>'''

        utils.checked_insert(page_dict,
          'blog'+tags_string+url_pagenum_string+page_order+'.html',
          html_pages.make_page(
            "Eli Dupree's website ⊃ Blog",
            "",
            make_blog_page_body("\n".join(current_page if page_order == "/chronological" else reversed(current_page))+end_links, '<nav><a href="/403">[Random post] I foobar yesterday</a>'+index+'</nav>')
          )
        )
      current_page = []
      current_page_number += 1
    
    if not tag_specific:
      if "tags" in post_dict:
        for tag in post_dict["tags"]:
          posts_by_tag[tag].append(post_dict)
      utils.checked_insert(page_dict,
        'blog/'+url_formatted_title(post_dict)+'.html',
        html_pages.make_page(
          "Eli Dupree's website ⊃ Blog ⊃ "+title_formatted_title(post_dict),
          "",
          make_blog_page_body(post_html(post_dict), '<a href="/blog'+url_pagenum_string+'#'+post_div_id(post_dict)+'">View this post in context</a>')
        )
      )
  
  if not tag_specific:
    for tagname,posts in posts_by_tag.items():
      add_blog_pages(page_dict, {
        "tagname":tagname,
        "post_list":posts,
      })
  
