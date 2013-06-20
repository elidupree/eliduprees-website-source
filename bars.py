
import css
import top_bar
import bottom_bar

css.insert('''
div.bars_outer_box {
  min-height: 100%;
  position: relative;
}
div.bars_inner_box {
  padding-bottom: '''+str(bottom_bar.bar_height)+'''
}
''')

def bars_wrap(category, html):
  return '<div class="bars_outer_box">'+top_bar.top_bar(category)+'<div class="bars_inner_box">'+html+'</div>'+bottom_bar.bottom_bar()+'</div>'
