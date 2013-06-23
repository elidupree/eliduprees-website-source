
import utils
import css
import top_bar
import bars
import html_pages


vc_content_margin = "4em";

css.insert('''
div.vc_trigger_warning_box {
  height: 100%; }
div.vc_trigger_warning_text {
  margin: 2em auto;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
  text-align: center; }
div.vc_trigger_warning_text a {
  color: #ffc800; }
div.vc_trigger_warning_main_text {
  font-size: 120%;
  margin: 0 auto;
  max-width: 35em;
  border: 3px solid white;
  border-radius: 2em; }
div.vc_trigger_warning_details {
  margin: 0 auto;
  max-width: 35em; }
a.dismiss_trigger_warning {
  display: block;
  font-size: 200%;
  margin-top: 0.6em;
  padding: 0.15em;
  font-weight: bold; }
a.disable_trigger_warnings {
  display: block;
  padding: 0.5em; }
div.vc_box_after_trigger_warning {
  position: relative; }
  
div.vc_comic_and_nav {
  width: 750px;
  margin: 2em auto; }
div.vc_comic_and_transcript {
  margin: 5em 0; }
div.vc_comic {
  display: inline-block;
  width: 750px; }
img.vc_comic {
  width: 750px; }
div.vc_transcript_outer {
  width: 750px; }
  
div.vc_nav_bar {
  width: 750px; }
div.vc_nav_button {
  display: inline-block;
  color: #ffc800;
  /*background-color: #412f16;*/
  border-radius: 16px;
  width: 250px;
  text-align: center;
  font-size: 300%;
  font-weight: bold; }
div.vc_nav_button a:link{ color:#7e7e40 }
div.vc_nav_button a:visited{ color:#40557f }
div.vc_nav_button.prev {
  margin-left: 75px;
  margin-right: 50px; }
div.vc_nav_button.next {
  margin-left: 50px;
  margin-right: 75px; }
div.vc_transcript_inner {
  padding: 0.5em;
  color:white; }
  
@media screen and (min-width: 1090px) {
  div.vc_comic_and_nav {
    width: 1090px; }
  div.vc_transcript_outer {
    display: inline-block;
    width: 340px;
    vertical-align: top; }
  .vc_transcript_hidden div.vc_comic_and_nav {
    width: 920px;
    padding-left: 170px; }
  .vc_transcript_hidden div.vc_transcript_outer {
    width: 170px; }
}

div.vc_annotation_outer {
  width: 750px;
}
div.vc_annotation {
  max-width: 36.75em;
  margin: 3em auto;
}
div.vc_annotation .blog_post {
  background-color: #cccccc
}
div.vc_annotation .blog_post_metadata {
  background-color: rgba(204,204,204,.7) }''')

def vc_navbar():
  return '<div class="vc_nav_bar"><div class="vc_nav_button prev"><a rel="prev" href="prev page">Previous</a></div><div class="vc_nav_button next"><a rel="next" href="next page">Next</a></div></div>'

print("make the in-comic next page link work")
def vc_page_html(page):
  return (
    '''
<div class="vc_comic_and_nav">'''
  +vc_navbar()+'''
  <main>
    <div class="vc_comic_and_transcript">
      <div class="vc_comic">
        <a href="next comic">
          <img class="vc_comic" src="http://deqyc5bzdh53a.cloudfront.net/VC_1.png" />
        </a>
      </div>
      <div class="vc_transcript_outer">
        <div class="vc_transcript_inner">
          Transcript: <a href="javascript">(show)</a><br/><br/>Transcript transcript transcript dolor sit amet, consectetur adipistranscript <br/><br/>Transcript transcript transcript dolor sit amet, consectetur adipistranscript <br/><br/>Transcript transcript transcript dolor sit amet, consectetur adipistranscript <br/><br/>Transcript transcript transcript dolor sit amet, consectetur adipistranscript <br/><br/>
        </div>
      </div>
    </div>'''
    +vc_navbar()+'''
    <div class="vc_annotation_outer">
      <div class="vc_annotation">
        <div class="blog_post">
          <p>adipiscing elit, sed do eiusmod tempor annotation annotation annotation ut labore et dolore magna aliquannotation</p><p>adipiscing elit, sed do eiusmod tempor annotation annotation annotation ut labore et dolore magna aliquannotation</p><p>adipiscing elit, sed do eiusmod tempor annotation annotation annotation ut labore et dolore magna aliquannotation</p>
        </div>
        <div class="blog_post_metadata_outer">
          <div class="blog_post_metadata">Posted May 14, 2015'''+utils.inline_separator+'<a rel="bookmark" href="'+'foo'+'''">Permalink</a></div>
        </div>
      </div>
    </div>
  </main>
</div>''')
  
def vc_trigger_warning_bars_wrap(info, html):
  return '<div class="vc_trigger_warning_box">'+top_bar.top_bar(info)+'<section><div class="vc_trigger_warning_text"><div class="vc_trigger_warning_main_text"><p>The following page contains depictions of gratuitous faux Latin.</p><p><a class="dismiss_trigger_warning" href="javascript">View the comic</a></p></div><div class="vc_trigger_warning_details"><p><a class="disable_trigger_warnings" href="javascript">Disable content notices for this site</a></p></div></div></section></div><div class="vc_box_after_trigger_warning"><div class="bars_inner_box">'+html+'</div>'+bars.bottom_bar(info)+'</div>'

# in place of "Disable content notices for this site",
# "You could disable content notices if you had cookies enabled for this site",
# "You could disable content notices if you had Javascript and cookies enabled for this site",

vc_pages = [
  2
]

def add_vc_pages(page_dict):
  for i in range(0,len(vc_pages)):
    vc_page = vc_pages[i]
    utils.checked_insert(page_dict,
      'voldemorts-children'+('' if i == 0 else '/'+str(i))+'.html',
      html_pages.make_page(
        "Eli Dupree's website ⊃ Voldemort's Children ⊃ Page "+str(i),
        "",
        '<body class="voldemorts_children">'+vc_trigger_warning_bars_wrap({"comics":True }, vc_page_html(vc_page))+'</body>'
      )
    )
