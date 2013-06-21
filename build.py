import os
import os.path
import css

import html_pages
import top_bar
import blog
import utils

# maybe shutil.rmtree("./build")?

def putfile(path, contents):
  buildpath = "./build/"+path
  builddir = os.path.dirname(buildpath)
  if not os.path.exists(builddir):
    os.makedirs(builddir)
  f = open(buildpath, "w")
  f.write(contents)

page_dict = {}

def put_to_dict(path, contents):
  utils.checked_insert(page_dict, path, contents)

put_to_dict(css.filename(), css.build())

put_to_dict("index.html", html_pages.make_page("Eli Dupree's website", "", "<body>"+top_bar.top_bar("home")+"</body>"))
blog.add_blog_pages(page_dict)

for path,contents in page_dict.items():
  putfile(path,contents)
