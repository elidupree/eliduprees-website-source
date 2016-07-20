# Eli Dupree's website source

This is the code I use to generate elidupree.com. It's not necessarily useful for anyone else.

## Usage

`build.py` builds a test version all of the static pages, which are most of the website. I run a local instance of nginx that allows me to view the built version before deploying it.

`build.py --deploy` builds a version ready for deployment. It also automatically updates the "date posted" and "date modified" of posts, with the assumption that the website will actually be deployed on the same day the deploy build is made.

`deploy.py --future` deploys the built version to a test URL. `deploy.py --prod` deploys it to the production URL.

The scripts in server_scripts/, along with blog_server_shared.py, run on a separate server. When someone makes a request to `/_services/comments`, it should invoke `server_scripts/do_reply.py` with the given parameters. These scripts also need a sibling `secrets.py`, which is not included in this repository, and contains only an IFTTT Maker key.

`render_comic_pages.py comic_ID first [last]` has been used to generate the files in `/media/generated_from_source_files`. Currently, it uses hard-coded paths from my own filesystem. The source files are not yet publicly available, although I intend to publish them eventually.

## Dependencies

jshint, if you want to check the generated JavaScript files. You can also run `build.py --no-jshint`.

idupree-websitepy, to generate a script used by nginx, and to test the generated website in various ways. It is also possible to run `build.py --no-idupree-websitepy` and still have a mostly-working local version by pointing nginx at `build/initial/`.

pa11y, to test the accessibility of the generated pages. Because this is slow, it must be specifically invoked with `build.py --accessibility`.

pngquant and optipng, for rendering the comic pages. This repository contains the rendered versions, so these are not necessary for the main build process.

## License

The green caves game is part of the [Lasercake project](https://github.com/elidupree/Lasercake), and it is licensed under the GNU AGPL. It was compiled as of [this commit](https://github.com/elidupree/Lasercake/commit/38117543a3f4d864d8544980c317eb311b4b83ba).

All artwork and prose works (including all stories and blog posts) in this repository are licensed under a [Creative Comments Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

Much of the code is just to do a job, and isn't any kind of extraordinary work in its own right. This applies to all the code in acobs.py, bars.py, blog.py, blog_posts.py, blog_server_shared.py, build.py, category_pages.py, comics.py, css.py, exmxaxixl.py, gimp_stuff.py, hexy.py, html_pages.py, javascript.py, paws.py, redirects.py, render_comic_images.py, rss.py, tags.py, top_bar.py, utils.py, server_scripts/do_reply.py, server_scripts/errors.py, server_scripts/forms.py. You may use this code, modify it, distribute modified versions, etc., however you like.
