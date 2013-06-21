
import css
import top_bar

bottom_bar_height = 1.5

css.insert('''
div.bars_outer_box {
  min-height: 100%;
  position: relative;
}
div.bars_inner_box {
  padding-bottom: '''+str(bottom_bar_height)+'''
}

div.bottom_bar {
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 0.25em 0;
  height: '''+str(bottom_bar_height - 0.5)+'''em;
  font-family: Arial, Helvetica, sans-serif;
  text-align: center;
  background-color: black;
  background-image: url("/top-bar-background.png");
  background-size: 100% 100%; }

address.eli_email {
  display: inline;
  font-style: normal; }
''')

def bottom_bar():
  return '<footer><div class="bottom_bar">Please share this! | <address class="eli_email">Contact: <a href="ma&#73;ltO&#58;web&#64;el&#105;dupree&#00046;&#99;om">web&#64;el&#105;dupree&#00046;&#99;om</a></address> | <a href="/policies">Policies</a> | <a href="https://github.com/elidupree/eliduprees-website-source">Website source (code CC-0, content CC-BY-SA)</a></div></footer>'

def bars_wrap(category, html):
  return '<div class="bars_outer_box">'+top_bar.top_bar(category)+'<div class="bars_inner_box">'+html+'</div>'+bottom_bar()+'</div>'
