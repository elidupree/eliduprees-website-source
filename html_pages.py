
import css

def make_page(title, head_stuff, body_stuff):
  return '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>'''+title+'''</title>
    <link rel="stylesheet" type="text/css" href="/'''+css.filename()+'''">
    '''+head_stuff+'''
  </head>
  <body>
    '''+body_stuff+'''
  </body>
</html>'''
