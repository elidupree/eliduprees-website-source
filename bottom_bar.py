

import css

bar_height = 1.5

css.insert('''

div.bottom_bar {
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 0.25em 0;
  height: '''+str(bar_height - 0.5)+'''em;
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
  return '<footer><div class="bottom_bar">Please share this! | <address class="eli_email">Contact: <a href="ma&#73;ltO&#58;web&#64;el&#73;dupree&#00046;&#99;om">web&#64;el&#73;dupree&#00046;&#99;om</a></address> | <a href="/policies">Policies</a> | This website is open source; <a href="https://github.com/elidupree/eliduprees-website-source">GitHub</a></div></footer>'
