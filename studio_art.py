#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import css


css.insert('''

html.studio_art div.bars_outer_box {
  background-color: #ffffff; }
html.studio_art div.comic_content_warning_text {
  color: black; }
html.studio_art .meta_controls_coloring {
  color: #55f; }
html.studio_art .comic_metabar {color:#555;}
html.studio_art div.comic_toggle_content_warnings {
  color: black; }

html.studio_art div.comic_transcript_inner {
  color: black; }
html.studio_art .complete_comic {color:#999;}
''')

pages = [

{"source": "postage_stamp.jpg", "chapter_start": "Breadth", "annotation":'''Pencil on paper. This is a self-portrait as a postage stamp, at the actual size of a postage stamp, drawn on an actual envelope.

I used a mechanical pencil for this, as I do for almost all my pencil drawings. When I draw with mechanical pencil, I alternate drawing with scribbling at an angle on a piece of scrap paper, to wear down the lead in a specific pattern. One side of the lead becomes a wide flat surface, suitable for shading. The other side becomes a very fine point. This fine point was what I used to make the tiny, precise lines of this drawing.'''},
{"source": "fiery_stuff.jpg", "annotation":'''Oil pastel on black paper, if I remember right. (I have the original artwork stored somewhere in my house, but I'm only looking at the digital versions as I write this.)

This artwork was inspired by a dream. In the dream, there was an infinite grid of glass furnaces in space. To get between the furnaces, there were walkways (to go side-to-side) and ladders (to go up and down). This artwork doesn't quite do justice to it, because I only focused on one furnace. I didn't find a nice way to fit the others in the background. I probably should have done a sketch first, so that I could express the absurdly large scale of the space.

To get a sense of the scale, the tiny white ladders I drew on the sides of the furnace are intended to be sized for a human to climb.
'''},
{"source": "coat.jpg", "annotation":'''Pencil on paper.

I usually draw from my imagination, but it's also useful to be able to draw things that you see in real life.'''},
{"source": "watch.jpg", "annotation":'''Vine charcoal on paper. This was a broken wristwatch that I used to carry around.

Vine charcoal was fun to work with. It's very easy to smudge, but unlike a lot of drawing materials, it's actually possible to erase. I was even able to erase it with my <em>breath</em>. Whenever I drew part of the picture and it didn't look exactly right, I carefully blew away the problem area and redrew it.'''},
{"source": "escher.jpg", "annotation":'''Pencil on paper. Imitate the style of the famous artist, they said. So I do a self-portrait based on an Escher drawing.

It took me a long time to draw this and I didn't end up having time to finish it, but I think it got the main point across.'''},
{"source": "devil_phone.jpg", "annotation":'''Watercolor on some sort of paper. This isn't exactly my best work. I've never had much mastery of watercolors.

I don't even agree with the message that much anymore! I've always found it hard to communicate over the phone myself. But nowadays, we have much higher-quality phones and even video chat. Electronic communication is way better than it used to be. I think this picture was more motivated by my personal annoyance with telephones than by a real criticism of society.'''},
{"source": "conte_figure.jpg", "annotation":'''Conté crayon on newsprint. Another student modeled for some of us to draw. Ze ended up with an elongated face in my version, but otherwise I think I did it pretty accurately.'''},
{"source": "rosebush.jpg", "annotation":'''Pencil on paper.

I drew this from a photograph of an old rosebush that grows next to my driveway. I don't feel like this was a successful drawing. I wanted to make the various vines and branches show up as clearly as in the photograph, but I worked at a long time and didn't succeed.'''},
{"source": "negative_space.jpg", "annotation":'''Charcoal on paper. One of our assignments was to draw using negative space &ndash; they stacked several schools on a table, and we drew everything <em>except</em> the stools.

We were all given the same size of paper to use, but told we could orient it however we wanted. Naturally, I took this instruction literally.'''},
{"source": "light_switch.jpg", "annotation":'''Pencil on an index card. This is one of the light switches from my house, viewed from above.

It can be hard to shade with pencil, because pencil strokes inherently have a direction to them. But this also makes pencil excellent for drawing wood grain. There's something very pleasing about a drawing that looks like actual wood.'''},
{"source": "landscape.jpg", "annotation":'''Chalk pastel on gray paper.

Drawing on gray paper is interesting because the original color can be both darkened <em>and</em> lightened. On white paper, you color in all the shadows and leave the highlights untouched. On black paper, you color in the highlights and leaves the shadows untouched. On gray paper, you have to draw both.

I didn't really have a plan in mind for this picture when I started it. I just started drawing a landscape and added in whatever came to mind. I added the Eye of Sauron in the corner, casting a dark cloud over everything, when I decided the rest of the page was too boring. The dark cloud really helps make the sun stand out, as well.

You may recognize this as the background image from other parts of this website. Because this picture was deliberately blurry, unlike most of my work, it made a good background image. I did have to crop out the Eye, though.'''},
{"source": "seascape.jpg", "annotation":'''Scratchboard.

I love scratchboard drawings. It's one of the few media where both white and black are so vivid. Subtlety is nice and all, but BAM! Bright white! BAM! Solid black! It's great.

This particular scratchboard started weight, and we had to add the ink layer ourselves. I deliberately left the ink off of the moon, and made the edges irregular. That way, the borders of the clouds over the moon aren't actually scratched, so they have a different look than the rest of the image.'''},
{"source": "looking_down.jpg", "chapter_start": "Concentration", "annotation":'''Scratchboard.

This drawing was practically the inspiration of my concentration, "bringing meaning to empty spaces". What's down the stairs? What is the person seeing? Nobody knows, but yet, it's the most important part of the image.'''},
{"source": "pastel_gateway.jpg", "annotation":''''''},
{"source": "flashlight.jpg", "annotation":''''''},
{"source": "st_lukes_tower.jpg", "annotation":''''''},
{"source": "5_pillars.jpg", "annotation":''''''},
{"source": "scratchboard_gateway.jpg", "annotation":''''''},
{"source": "stupid_slogan.jpg", "annotation":''''''},
{"source": "hand_reaching.jpg", "annotation":''''''},
{"source": "1_pillar.jpg", "annotation":''''''},
{"source": "red_shirt.jpg", "annotation":''''''},
{"source": "buddha.jpg", "annotation":''''''},
{"source": "candle.jpg", "annotation":''''''},


]

for page in pages:
  page ["auto_paragraphs"] = True
