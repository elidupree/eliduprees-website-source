import os
import os.path
import shutil

import css
import html_pages
import top_bar
import utils
import blog
import voldemorts_children

def ensure_dir(d):
  if not os.path.exists(d):
    os.makedirs(d)

ensure_dir("./build/media")
media_filenames = os.listdir("./media")
for media_filename in media_filenames:
  shutil.copy("./media/"+media_filename, "./build/media/"+media_filename)

def putfile(path, contents):
  buildpath = "./build/"+path
  ensure_dir(os.path.dirname(buildpath))
  f = open(buildpath, "w")
  f.write(contents)

page_dict = {}

def put_to_dict(path, contents):
  utils.checked_insert(page_dict, path, contents)

put_to_dict(css.filename(), css.build())

put_to_dict("index.html", html_pages.make_page("Eli Dupree's website", "", "<body>"+top_bar.top_bar({"home":True})+"</body>"))
blog.add_blog_pages(page_dict)
voldemorts_children.add_vc_pages(page_dict)

for path,contents in page_dict.items():
  if False and path.endswith(".html"):
    from py_w3c.validators.html.validator import HTMLValidator
    vld = HTMLValidator()
    vld.validate_fragment(contents)
    print(vld.errors)
    print(vld.warnings)
  putfile(path,contents)
