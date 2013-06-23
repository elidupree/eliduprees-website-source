
import utils
import css
import bars
import html_pages


vc_content_margin = "4em";

css.insert('''
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
''')

def vc_navbar():
  return '<div class="vc_nav_bar"><div class="vc_nav_button prev"><a rel="prev" href="prev page">Previous</a></div><div class="vc_nav_button next"><a rel="next" href="next page">Next</a></div></div>'

print("make the in-comic next page link work")
def vc_page_html(page):
  return '<main><div class="vc_comic_and_nav">'+vc_navbar()+'<div class="vc_comic_and_transcript"><div class="vc_comic"><a href="next comic"><img class="vc_comic" src="http://deqyc5bzdh53a.cloudfront.net/VC_1.png" /></a></div><div class="vc_transcript_outer"><div class="vc_transcript_inner">Transcript: <a href="javascript">(show)</a><br/><br/>Transcript transcript transcript dolor sit amet, consectetur adipistranscript <br/><br/>Transcript transcript transcript dolor sit amet, consectetur adipistranscript <br/><br/>Transcript transcript transcript dolor sit amet, consectetur adipistranscript <br/><br/>Transcript transcript transcript dolor sit amet, consectetur adipistranscript <br/><br/></div></div></div>'+vc_navbar()+'</div></main>'

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
        '<body class="voldemorts_children">'+bars.bars_wrap({"comics":True }, vc_page_html(vc_page))+'</body>'
      )
    )
