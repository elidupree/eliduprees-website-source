

import css

bar_height = 1.5

css.insert('''

div.bottom_bar {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 1.5em;
  font-family: Arial, Helvetica, sans-serif;
  text-align: center;
  background-color: black;
  background-image: url("/top-bar-background.png");
  background-size: 100% 100%; }

address.eli_email {
  display: inline;
  font-style: italic; }
''')

def bottom_bar():
  return '<footer><div class="bottom_bar"><address class="eli_email"><a href="">Contact</a></address> | <a href="">Privacy policy</a> | This website is open source; <a href="">GitHub</a></div></footer>'
