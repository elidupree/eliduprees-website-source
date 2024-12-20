#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import os.path
import sys
import subprocess
import datetime

from ravelling_wrath.book_versions.shared import generate_html_and_linked_media_files, BookType
from ravelling_wrath.book_versions.ebook import fix_converted_epub_contents

build_path ="./build/ravelling_wrath_book"

specific_chapter = None
if len(sys.argv) > 1:
  try:
    specific_chapter = int(sys.argv[1]) - 1
  except:
    pass
    
print("starting rendering book at "+ datetime.datetime.now().isoformat())

if "epub" in sys.argv:
  generate_html_and_linked_media_files(
    os.path.join (build_path, "epub"),
    book_type = BookType.EPUB,
    specific_chapter = specific_chapter,
  )

  html_path = os.path.join (build_path, "epub", "ravelling_wrath.html")
  #opf_path = os.path.join (build_path, "epub", "content.opf")
  converted_epub_path = os.path.join (build_path, "epub", "ravelling_wrath.epub")
  final_epub_path = os.path.join (build_path, "epub", "ravelling_wrath.epub")
  epub_contents_path = os.path.join (build_path, "epub", "epub_contents")
  
  #with open(opf_path, "w") as file:
  #  file.write(content_opf)
  
  subprocess.run([
    "ebook-convert", html_path, converted_epub_path,
    "--output-profile", "tablet",
    #"--from-opf", opf_path
  ])
  
  subprocess.run(["unzip", converted_epub_path, "-d", epub_contents_path])
  fix_converted_epub_contents(epub_contents_path)
  subprocess.run(["7z", "a", final_epub_path, os.path.join (epub_contents_path, "*")])
  
  
def render_print_version (directory, book_type):
  generate_html_and_linked_media_files(
    os.path.join (build_path, directory),
    book_type = book_type,
    specific_chapter = specific_chapter,
  )
  
  html_path = os.path.join (build_path, directory, "ravelling_wrath.html")
  pdf_path = os.path.join (build_path, directory, "ravelling_wrath.pdf")
  
  # Note: pagedjs-cli seems to also require me to
  # `sudo sysctl -w kernel.unprivileged_userns_clone=1`
  subprocess.run(["pagedjs-cli", html_path, "-o", pdf_path])

if "print" in sys.argv:
  render_print_version ("print", BookType.PRINT)
  
if "compressed_pdf" in sys.argv:
  render_print_version ("print", BookType.COMPRESSED_PDF)
  
if "large_print_1" in sys.argv:
  render_print_version ("large_print_1", BookType.LARGE_PRINT_1)

if "large_print_2" in sys.argv:
  render_print_version ("large_print_2", BookType.LARGE_PRINT_2)
  
  
    
print("done rendering book at "+ datetime.datetime.now().isoformat())
