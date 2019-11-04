#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import os.path
import re
import subprocess
import datetime
import traceback

from weasyprint import HTML, CSS

import blog_server_shared
import utils

import ravelling_wrath.main

build_path ="./build/ravelling_wrath_book"
html_path = os.path.join (build_path, "ravelling_wrath.html")
pdf_path = os.path.join (build_path, "ravelling_wrath.pdf")
os.makedirs (build_path, exist_ok=True)

def chapter_html (chapter):
  contents = utils.auto_paragraphs (chapter ["contents"])
  contents, _, _ = blog_server_shared.postprocess_post_string (contents, None, chapter ["title"], False, False)
  contents = re.sub(r"<bigbreak>", "", contents)
  return contents

chapters = [
  chapter_html (chapter) for chapter in ravelling_wrath.main.posts
]

def wrap(html):

 return '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Ravelling Wrath</title>
    <style>
@page {
  size: 6in 9in;
  margin: 0.6in;
}
@page :left {
  margin-right: 0.9in;
}
@page :right {
  margin-left: 0.9in;
}
p {
  font: 12pt "Bitter";
  margin: 0.1em 0;
  line-height: 1.2em;
  text-indent: 2em;
  text-align: justify;
}
h2 {
  page-break-before: right;
}
    </style>
  </head>
  <body>
'''+html+'''
  </body>
</html>'''

full_html = wrap("".join (chapters))

with open (html_path, "w") as file:
  file.write (full_html)
  
print("starting rendering book at "+ datetime.datetime.now().isoformat())

weasyprint = True
if weasyprint:
  #for index, chapter in enumerate(chapters):
    #for paragraph in re.finditer(r"<p>.*</p>", chapter):
    #try:
      HTML (string = wrap(full_html)).write_pdf (pdf_path)
    #except Exception as e:
    #  print (paragraph.group(0))
    #  print(traceback.format_exc())
    #print(f"done rendering chapter {index+1} at "+ datetime.datetime.now().isoformat())
else:
  subprocess.run(["wkhtmltopdf", html_path, pdf_path])
print("done rendering book at "+ datetime.datetime.now().isoformat())
