#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import os.path
import re
import subprocess
import datetime
import traceback

from num2words import num2words

import weasyprint
print("WeasyPrint version:", weasyprint.__version__)
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
  #contents, _, _ = blog_server_shared.postprocess_post_string (contents, None, None, False, False)
  contents = f"""
  <h2>Chapter {num2words(chapter ["chapter_number"]).capitalize()}</h2>
  <div class="chapter-title">{chapter ["chapter_title"]}</div>
  
  <span style="string-set: runningleft '';"></span>
  <span style="string-set: runningright '';"></span>
  <span style="string-set: runningleft 'Ravelling Wrath';"></span>
  <span style="string-set: runningright 'Chapter {num2words(chapter ["chapter_number"]).capitalize()}: {chapter ["chapter_title"]}';"></span>
  
  """ + re.sub(r"<bigbreak>", '<div class="bigbreak"></div>', contents)
  return contents

chapters = [
  chapter_html (chapter) for chapter in ravelling_wrath.main.chapters
]

def wrap(html):

 return '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Ravelling Wrath</title>
    <style>
body {
  counter-reset: page;
}
@page {
  size: 6in 9in;
  margin: 0.6in;
  counter-increment: page;
  @bottom-center {
    content: counter(page);
  }
}
@page :left {
  margin-right: 0.9in;
  @top-center {
    content: "Bar";
    content: string(runningleft);
  }
}
@page :right {
  margin-left: 0.9in;
  @top-center {
    content: "Foo";
    content: string(runningright);
  }
}
p {
  font: 12pt "Bitter";
  margin: 0;
  margin-bottom: 1pt;
  line-height: 1.25;
  text-indent: 2em;
  text-align: justify;
}
h2 {
  font: 16pt "Bitter";
  page-break-before: right;
  text-align: center;
}
.chapter-title {
  font: bold 24pt "Bitter";
  text-align: center;
  margin-bottom: 1.3em;
}
.bigbreak {
  height: 12pt;
}



p,div.clear {
  clear: both;
}
p.text {
  border-radius: 1.3em;
  max-width: 60%;
  text-align: left;
  text-indent: 0;
  padding: 6px 12px;
  margin-top: 6px;
  margin-bottom: 8px;
  font-family: Arial, Helvetica, sans-serif;
}
p.text.right {
  background-color: #87e520;
  float: right;
}
p.text+p.text {
  margin-top: -6px;
}
p.text.left {
  background-color: #e5e4e4;
  float: left;
}

    </style>
  </head>
  <body>
'''+html+'''
  </body>
</html>'''

full_html = wrap("".join (chapters[:]))

with open (html_path, "w") as file:
  file.write (full_html)
  
content_opf = '''
<?xml version="1.0" encoding="UTF-8">
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="uuid_id" version="2.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf"
    <dc:title>Ravelling Wrath</dc:title>
    <dc:creator opf:role="aut" opf:file-as="Dupree, Eli">Eli Dupree</dc:creator>
    <dc:publisher>Eli Dupree</dc:publisher>
    <dc:date>'''+datetime.date.today().isoformat()+'''</dc:date>
    <dc:contributor opf:role="cov" opf:file-as="Fensore, Sarah">Sarah Fensore</dc:contributor>
    <dc:identifier id="uuid_id" opf:scheme="uuid">c0b3ea68-aced-4746-966b-7b0fc27ba1fc</dc:identifier>
    <dc:subject>Healthy relationships</dc:subject>
    <dc:subject>Consent</dc:subject>
    <dc:subject>Mental health</dc:subject>
    <dc:description>'''+ravelling_wrath.main.full_blurb+'''</dc:description>
    <dc:language>en</dc:language>
    <dc:identifier opf:scheme="ISBN">TODO</dc:identifier>
    <meta name="cover" content="cover"/>
    <meta name="dcterms:modified">'''+datetime.datetime.now().isoformat()+'''</meta>
  </metadata>
  <manifest>
  
  </manifest>
  <spine>
  
  </spine>
</package>
'''
  
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
