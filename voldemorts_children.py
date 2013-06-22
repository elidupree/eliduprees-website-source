
import utils
import css
import bars
import html_pages



css.insert('''
div.vc {
  width: 750px;
  margin: 2em auto; }
img.vc {
  width: 750px; }
''')

def vc_page_html(page):
  return '<main><div class="vc"><img class="vc" src="http://deqyc5bzdh53a.cloudfront.net/VC_1.png" /></div></main>'

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
        '<body>'+bars.bars_wrap("comics", vc_page_html(vc_page))+'</body>'
      )
    )
