#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import os.path
import sys
import subprocess
import datetime

import ravelling_wrath.book_versions.shared

build_path ="./build/ravelling_wrath_book"
if os.path.exists(build_path):
  #
  for root, dirs, files in os.walk(build_path):
    for filename in files:
      os.remove(os.path.join(root, filename))

specific_chapter = None
if len(sys.argv) > 1:
  specific_chapter = int(sys.argv[1]) - 1
  
ravelling_wrath.book_versions.shared.generate_html_and_linked_media_files(os.path.join (build_path, "print"), is_print = True, specific_chapter = specific_chapter)
ravelling_wrath.book_versions.shared.generate_html_and_linked_media_files(os.path.join (build_path, "ebook"), is_print = False, specific_chapter = specific_chapter)
      
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
  # Note: pagedjs-cli seems to also require me to
  # `sudo sysctl -w kernel.unprivileged_userns_clone=1`
  
  html_path = os.path.join (build_path, "print/ravelling_wrath.html")
  pdf_path = os.path.join (build_path, "print/ravelling_wrath.pdf")
  
  subprocess.run(["pagedjs-cli", html_path, "-o", pdf_path])
    
print("done rendering book at "+ datetime.datetime.now().isoformat())
