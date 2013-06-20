

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
  return '<footer><div class="bottom_bar">Please share this! | <address class="eli_email">Contact: <a href="">web@elidupree.com</a></address> | <a href="">Privacy policy</a> | This website is open source; <a href="">GitHub</a></div></footer>'
