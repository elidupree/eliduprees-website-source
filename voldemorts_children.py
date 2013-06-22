
import utils
import css
import bars
import html_pages



css.insert('''
div.vc_comic_and_nav {
  width: 750px;
  margin: 2em auto; }
div.vc_comic {
  display: inline-block;
  width: 750px; }
img.vc_comic {
  width: 750px; }
div.vc_nav {
  display: inline-block;
  color: #ffc800;
  width: 375px;
  text-align: center;
  font-size: 300%; }

@media screen and (min-width: 1150px) {
  div.vc_comic_and_nav {
    width: 1150px; }
  div.vc_nav {
    width: 200px; }
  div.vc_nav.top.next {
    display: none; }
  div.vc_nav.bottom.prev {
    display: none; }
}
''')
print("make the in-comic next page link work")
def vc_page_html(page):
  return '<main><div class="vc_comic_and_nav"><div class="vc_nav top prev">Previous</div><div class="vc_nav top next">Next</div><div class="vc_comic"><a href="next comic"><img class="vc_comic" src="http://deqyc5bzdh53a.cloudfront.net/VC_1.png" /></a></div><div class="vc_nav bottom prev">Previous</div><div class="vc_nav bottom next">Next</div></div></main>'

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
