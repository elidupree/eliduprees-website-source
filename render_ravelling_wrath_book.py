#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import os.path
import re
import subprocess
import datetime
import traceback
import shutil

from num2words import num2words

import blog_server_shared
import post_contents_utils
import utils

import ravelling_wrath.main
import ravelling_wrath.definitions

build_path ="./build/ravelling_wrath_book"
if os.path.exists(build_path):
  #
  for root, dirs, files in os.walk(build_path):
    for filename in files:
      os.remove(os.path.join(root, filename))
html_path = os.path.join (build_path, "ravelling_wrath.html")
pdf_path = os.path.join (build_path, "ravelling_wrath.pdf")
os.makedirs (build_path, exist_ok=True)

def ensure_dir(d):
  if not os.path.exists(d):
    os.makedirs(d)

rav_media_paths = {}
def replace_media_path(match):
  full_path = match.group(1)
  relevant_path = os.path.basename(full_path)
  if rav_media_paths.get(relevant_path, full_path) != full_path:
    raise RuntimeError(f"multiple media named {relevant_path}")
  rav_media_paths[relevant_path] = full_path
  return relevant_path

def chapter_html (chapter):
  ravelling_wrath.main.replace_section_breaks(chapter, "/media/ravelling-wrath/symbols")
  contents = post_contents_utils.auto_paragraphs (chapter ["contents"])
  #contents, _, _ = blog_server_shared.postprocess_post_string (contents, None, None, False, False)
  contents = ravelling_wrath.main.replace_all_emoji(contents, "/media/vendor/ravelling-wrath/emoji/black")
  contents = re.sub(r"/media/(.*?)\?rr", replace_media_path, contents)
  
  contents = re.sub("<not_print>.+?</not_print>", "", contents)
  contents = re.sub("</?print_only>", "", contents)
  
  symbols = chapter["symbols"]
  running_symbol_filename = f'{symbols}-small.png'
  rav_media_paths[running_symbol_filename] = running_symbol_filename
  
  contents = f'''
  <div class="chapter {chapter.get("post_class", "")}">
  <h2>Chapter {num2words(chapter ["chapter_number"]).capitalize()}</h2>
  <div class="chapter-title">{chapter ["chapter_title"]}</div>
  
  <div class="runningleft">
    <img class="runningsymbols {symbols}" src="{running_symbol_filename}" alt="" />
    Ravelling Wrath
    <img class="runningsymbols {symbols}" src="{running_symbol_filename}" alt="" />
  </div>
  <div class="runningright">
    <img class="runningsymbols {symbols}" src="{running_symbol_filename}" alt="" />
    Chapter {num2words(chapter ["chapter_number"]).capitalize()}: {chapter ["chapter_title"]}
    <img class="runningsymbols {symbols}" src="{running_symbol_filename}" alt="" />
  </div>
  
  
  {contents}</div>'''
  return contents

chapters = [
  chapter_html (chapter) for chapter in ravelling_wrath.main.chapters
]

fonts_css = ravelling_wrath.definitions.fonts_css("", mode="print")

for match in re.finditer(r"url\('(.+?.ttf)", fonts_css):
  rav_media_paths[match.group(1)] = "/media/fonts/"+match.group(1)

print(rav_media_paths)
media_dir = "./media/"
media_subdirs = os.listdir(media_dir)
for media_subdir in media_subdirs:
  media_subdir_fullpath = os.path.join(media_dir, media_subdir)
  for root, dirs, files in os.walk(media_subdir_fullpath):
    for media_filename in files:
      source = os.path.join(root, media_filename)
      if media_filename in rav_media_paths:
        if ("color" in rav_media_paths[media_filename]) == ("color" in root):
          destination = os.path.join(build_path, media_filename)
          ensure_dir(os.path.dirname(destination))
          shutil.copy(source, destination)

css_string = '''body {
  counter-reset: page;
}
@page {
  size: 6in 9in;
  margin: 0.6in;
  counter-increment: page;
  @bottom-center {
    content: counter(page);
    font: 12pt "Alegreya SC";
  }
  @top-left {
    content: element(runningsymbols);
    width: 0.45in;
  }
  @top-right {
    content: element(runningsymbols);
    width: 0.45in;
  }
}
@page :left {
  margin-right: 0.9in;
  @top-center {
    content: element(runningleft);
    font: 12pt "Alegreya SC";
  }
}
@page :right {
  margin-left: 0.9in;
  @top-center {
    content: element(runningright);
    font: 12pt "Alegreya SC";
  }
}
@page chapter :first {
  @top-center {
    content: none;
  }
  @top-left {
    content: none;
  }
  @top-right {
    content: none;
  }
}
@page full_page_image {
  margin: 0;
  @top-center {
    content: none;
  }
  @top-left {
    content: none;
  }
  @top-right {
    content: none;
  }
  @bottom-center {
    content: none;
  }
}
.runningleft {
  position: running(runningleft);
}
.runningright {
  position: running(runningright);
}
.runningsymbols {
  /*position: running(runningsymbols);*/
  max-height: 0.12in;
  max-width: 0.21in;
  vertical-align: -5%;
  margin: 0 0.5em;
  /*display: block;
  margin: 0 auto;*/
}
.runningsymbols.burning-heart {
  max-height: 0.14in;
}
.chapter {
  page: chapter;
  break-before: right;
}
p {
  font: 12pt "Kadwa";
  margin: 0;
  margin-bottom: 1pt;
  line-height: 1.25;
  text-indent: 2em;
  text-align: justify;
}
.yali-narration p {
  font-family: "Kreon", serif;
  font-size: 112%;
  line-height: 1.2em;
}
.before-forced-mid-paragraph-page-break {
  text-align-last: justify;
}
.after-forced-mid-paragraph-page-break {
  text-indent: 0;
}
h2 {
  font: 16pt "Alegreya SC";
  font-weight: 800;
  text-align: center;
}
.chapter-title {
  font: 24pt "Alegreya SC";
  font-weight: 800;
  text-align: center;
  margin-bottom: 1.3em;
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
.prayer {
  margin: 1.9em 0;
}
.prayer p {
  text-align: center;
  text-indent: 0;
}
img.full-page {
  max-width: 6in;
  max-height: 9in;
  display: block;
  margin: 0 auto;
  page: full_page_image;
}
img.chapter-header {
  max-height: 5in;
  max-width: 4.5in;
  display: block;
  margin: 0 auto;
  margin-top: -1.3em; 
  margin-bottom: 1.3em; 
}
img.bottom,img.top {
  width: 5.7in;
  height: auto;
  margin: 2.8em -0.6in;
}
img.bottom {
  margin-bottom: 0;
}
img.top {
  margin-top: 0;
}
img.ending {
  margin-top: 4em;
  width: 4.5in;
  display: block;
}
img.emoji {
  display: inline-block;
  width: 1.5em;
  height: 1.5em;
  margin: 0 -.125em;
  vertical-align: middle;
}
img.rav-section-break {
  display: block;
  margin: 0 auto;
  width: 100%;
  height: auto;
  margin: 2em auto;
}
img.rav-section-break.nonaligned {
  width: 80%;
}

'''+fonts_css

def wrap(html):

 return '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Ravelling Wrath</title>
    <link rel="stylesheet" href="style.css"/>
  </head>
  <body>
'''+html+'''
  </body>
</html>'''

full_html = wrap("".join (chapters[:1]))

with open (html_path, "w") as file:
  file.write (full_html)
  
with open(os.path.join (build_path, "style.css"), "w") as file:
  file.write (css_string)
  
tags = "Fiction, Young Adult, Fantasy, Urban Fantasy, Adventure, Consent, Healthy Relationships, Mental Health, Coming of Age, LGBT, Lesbian,"
tags = [match.group (1) for match in re.finditer (r"([^,\s][^,]*)", tags)]

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
    '''+'''
    '''.join(f'''<dc:subject>{tag}</dc:subject>''' for tag in tags) + '''
    <dc:description>'''+utils.strip_tags(ravelling_wrath.main.long_blurb)+'''</dc:description>
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

#converter = "weasyprint"
#converter = "wkhtmltopdf"
converter = "pagedjs-cli"

if converter == "weasyprint":
  import weasyprint
  print("WeasyPrint version:", weasyprint.__version__)
  from weasyprint import HTML, CSS
  from weasyprint.fonts import FontConfiguration

  if True:
  #for index, chapter in enumerate(chapters):
    #for paragraph in re.finditer(r"<p>.*</p>", chapter):
    #try:
      font_config = FontConfiguration()
      #print(css_string)
      #print(full_html)
      css = CSS(string=css_string, font_config=font_config)
      document = HTML (string = full_html, base_url = build_path).render (stylesheets=[css], font_config=font_config)
      print(dir(document))
      document.write_pdf(pdf_path)
    #except Exception as e:
    #  print (paragraph.group(0))
    #  print(traceback.format_exc())
    #print(f"done rendering chapter {index+1} at "+ datetime.datetime.now().isoformat())
    
if converter == "wkhtmltopdf":
  subprocess.run(["wkhtmltopdf", html_path, pdf_path])
  
if converter == "pagedjs-cli":
  subprocess.run(["pagedjs-cli", html_path, "-o", pdf_path])
    
print("done rendering book at "+ datetime.datetime.now().isoformat())
