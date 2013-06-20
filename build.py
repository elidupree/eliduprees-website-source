import os
import os.path
import css

import html_pages
import top_bar
import blog

# maybe shutil.rmtree("./build")?

def putfile(path, contents):
  buildpath = "./build/"+path
  builddir = os.path.dirname(buildpath)
  if not os.path.exists(builddir):
    os.makedirs(builddir)
  f = open(buildpath, "w")
  f.write(contents)

putfile(css.filename(), css.build())

putfile("index.html", html_pages.make_page("Eli Dupree's website", "", "<body>"+top_bar.top_bar("home")+"</body>"))
putfile("blog.html", blog.show_blog())

