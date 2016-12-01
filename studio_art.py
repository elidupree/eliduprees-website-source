#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import css

blurb = "A collection of drawings I did for a studio art class."
blurb_big = '''<p>In AP Studio Art, each student makes a portfolio of 24 drawings. 12 are "breadth" drawings, where you try to show your expertise with as many different materials and subjects as you can. The other 12 are "concentration" drawings. You pick a single concept to focus on, and make 12 drawings exploring that theme, whatever it is.</p>

<p>For my concentration, I chose "bringing meaning to empty spaces". I felt like it would help me learn the craft of arranging an image on a page &ndash; so that I could draw attention to a space and make it meaningful, even if there was nothing there.</p>

<p>Click on each image to get a closer view, and see my notes on each one.</p>'''

css.insert('''

html.studio_art div.comic_image {padding-bottom: 0;}

html.studio_art div.bars_outer_box {
  background-color: #dddddd; }
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

For this picture, I hung someone's winter coat from a doorknob and drew it just as it looked. I usually draw from my imagination, but it's also useful to be able to draw things that you see in real life.'''},
{"source": "watch.jpg", "annotation":'''Vine charcoal on paper. This was a broken wristwatch that I used to carry around.

Vine charcoal was fun to work with. It's very easy to smudge, but unlike a lot of drawing materials, it's actually possible to erase. I was even able to erase it with my <em>breath</em>. Whenever I drew part of the picture and it didn't look exactly right, I carefully blew away the problem area and redrew it.

Once you finish a charcoal drawing, you can spray it with a <a href="https://en.wikipedia.org/wiki/Fixative_(drawing)">fixative</a> to protect it from blowing away or smudging.'''},
{"source": "escher.jpg", "annotation":'''Pencil on paper. Imitate the style of the famous artist, they said. So I do a self-portrait based on an Escher drawing.

It took me a long time to draw this and I didn't end up having time to finish it, but I think it got the main point across.'''},
{"source": "devil_phone.jpg", "annotation":'''Watercolor on some sort of paper. This isn't exactly my best work. I've never had much mastery of watercolors.

I don't even agree with the message that much anymore! I've always found it hard to communicate over the phone myself. But nowadays, we have much higher-quality phones and even video chat. Electronic communication is way better than it used to be. I think this picture was more motivated by my personal annoyance with telephones than by a real criticism of society.'''},
{"source": "conte_figure.jpg", "annotation":'''Conté crayon on newsprint. Another student modeled for some of us to draw. Ze ended up with an elongated face in my version, but otherwise I think I did it pretty accurately.'''},
{"source": "rosebush.jpg", "annotation":'''Pencil on paper.

I drew this from a photograph of an old rosebush that grows next to my driveway. I don't feel like this was a successful drawing. I wanted to make the various vines and branches show up as clearly as in the photograph, but I worked at a long time and didn't succeed.'''},
{"source": "negative_space.jpg", "annotation":'''Charcoal on paper. One of our assignments was to draw using negative space &ndash; they stacked several stools on a table, and we drew everything <em>except</em> the stools.

We were all given the same size of paper to use, but told we could orient it however we wanted. Naturally, I took this instruction literally.'''},
{"source": "light_switch.jpg", "annotation":'''Pencil on an index card. This is one of the light switches from my house, viewed from above.

It can be hard to shade with pencil, because pencil strokes inherently have a direction to them. But this also makes pencil excellent for drawing wood grain. There's something very pleasing about a drawing that looks like actual wood.'''},
{"source": "landscape.jpg", "annotation":'''Chalk pastel on gray paper.

Drawing on gray paper is interesting because the original color can be both darkened <em>and</em> lightened. On white paper, you color in all the shadows and leave the highlights untouched. On black paper, you color in the highlights and leave the shadows untouched. On gray paper, you have to draw both.

I didn't really have a plan in mind for this picture when I started it. I just started drawing a landscape and added in whatever came to mind. I added the Eye of Sauron in the corner, casting a dark cloud over everything, when I decided the rest of the page was too boring. The dark cloud really helps make the sun stand out, as well.

You may recognize this as the background image from other parts of this website. Because this picture was deliberately blurry, unlike most of my work, it made a good background image. I did have to crop out the Eye, though.'''},
{"source": "seascape.jpg", "annotation":'''Scratchboard.

I love scratchboard drawings. It's one of the few media where both white and black are so vivid. Subtlety is nice and all, but BAM! Bright white! BAM! Solid black! It's great.

This particular scratchboard started white, and we had to add the ink layer ourselves. I deliberately left the ink off of the moon, and made the edges irregular. That way, the borders of the clouds over the moon aren't actually scratched, so they have a different look than the rest of the image.'''},
{"source": "looking_down.jpg", "chapter_start": "Concentration", "annotation":'''Scratchboard.

This drawing was practically the inspiration of my concentration, "bringing meaning to empty spaces". What's down the stairs? What is the person seeing? Nobody knows, but yet, it's the most important part of the image.

Unfortunately, scratchboard doesn't photograph very well, because the ink is very reflective. The bluish area in the bottom right is just an artifact of how we photographed the original drawing.'''},
{"source": "pastel_gateway.jpg", "annotation":'''Chalk pastel on black paper.

One of my favorite historical paintings is van Gogh's "Wheatfield with Crows". The warm colors of the ground, the cool colors of the sky, and the black crows &ndash; which are neither warm nor cool &ndash; crossing the boundary. I tried to create a similar effect in this picture.

Chalk pastel on black paper is one of my favorite ways to draw (with physical media, anyway). A dark image with a few bright highlights looks much more vivid to me than most things with a white background can be.

The "archway going to nowhere" is a cool fantasy trope. I'm not quite satisfied with this one, though. Because the black paper is actually less dark than the archway itself, it feels more like "I just didn't draw anything there" than "That's spooky, I wonder what's past the archway?"'''},
{"source": "flashlight.jpg", "annotation":'''Scratchboard.

This drawing didn't come out quite as intended. Per my concentration, your eye is supposed to be drawn to the vast empty space the person is looking into. Instead, the person takes up too much of the space. I should've made the person much smaller, squeezed way into the bottom corner of the picture &ndash; only about one-tenth as tall as the full picture, instead of one-third as tall. Then it really <em>would</em> call attention to the 99% of the surface that I left in darkness.'''},
{"source": "st_lukes_tower.jpg", "annotation":'''Colored pencil on index card. This is a church tower I can see from the window of my art classroom.

I bet there's loads of symbolism you can read into my swapping the church texture with the sky texture. Making up symbolism is a fun pastime. All I was doing was having fun playing with textures.'''},
{"source": "5_pillars.jpg", "annotation":'''White colored pencil on black paper.

There's a lot of different ways to "bring meaning to empty spaces". Here, I did it by creating a <em>pattern</em>. I drew the four pillars to create the <em>expectation</em> of a fifth pillar, so the fact that it isn't there becomes meaningful.

White colored pencil is a much softer white than white chalk pastel. The more subtle coloring worked well for this picture.'''},
{"source": "scratchboard_gateway.jpg", "annotation":'''Scratchboard.

This is a much simpler interpretation of the "empty gateway" concept. The lines imply that there's a bright light from behind the wall, so why can't you see the light in the gateway itself?'''},
{"source": "stupid_slogan.jpg", "annotation":'''Chalk pastel on black paper.

Looking back on this picture now, I'm not sure it fulfills the concentration very well. The dark half could just be a background. The viewer's eye is drawn to the action on the left and the Statue-of-Liberty-ish figure in the middle.

Maybe the figure should have been facing <em>towards</em> the darkness, instead of away from it. Or maybe something more subtle &ndash; like ze could be walking away in one direction, but turning to look back in the other.

'''},
{"source": "hand_reaching.jpg", "annotation":'''Chalk pastel on white paper.

Another way to "bring meaning to empty spaces" is to put an empty space where the viewer knows something <em>should</em> be. In this case, the viewer knows that there's supposed to be a reflection in the water.

I made the hand dark brown so that it would make the most vivid contrast with the sky and water. If you want that to symbolize something else, like black people not seeing their real life stories reflected in the mainstream media, that's cool too.

Making the watery reflections was fun. First, I drew the blue sky on the blank page. Then, I drew both versions of the trees/sleeve, so that the upper versions are drawn <em>over</em> the blue sky. Then, I took a white chalk pastel and dragged it horizontally over the lower versions, smudging them and creating the ripple effect. I didn't have to purposefully draw a single ripple myself.'''},
{"source": "1_pillar.jpg", "annotation":'''White chalk pastel on black paper.

This is a very simple one. <em>Why</em> an infinitely wide flat empty space has an infinitely tall pillar right next to a lightbulb, is left as an exercise to the viewer.'''},
{"source": "red_shirt.jpg", "annotation":'''Chalk pastel on black paper.

In this one, I actually did some symbolism on purpose. Having someone's <em>head</em> be hidden has special meanings. Hiding someone's head makes them look less human. If you hide your own head with a mask &ndash; let's say, to go and fight in the resistance without having your identity be known &ndash; you take away your human vulnerability. If you hide someone <em>else's</em> head, you take away their human <em>agency</em>. Here, the viewer is supposed to be disturbed by the objectification of the person in the picture.

I think I was in a hurry when I drew this one. I think the thing in the middle was supposed to be a plaque, as if the person was a museum exhibit, but it's not obvious what it is, and its perspective isn't correct compared with the rest of the picture.'''},
{"source": "buddha.jpg", "annotation":'''Charcoal on white paper.

I don't want to spoil this one with words.'''},
{"source": "candle.jpg", "annotation":'''Chalk(?) on black paper. (I'm pretty sure one of these pictures used regular chalk rather than white chalk pastel, but I'm not sure which one. I think it might've been this one. Regardless, I didn't like it as much, so I only used it once.)

This picture was originally inspired by the H.P. Lovecraft story "The Music of Erich Zann". I made a couple of attempts to sketch the scene of all the pages of music blowing out through the mysterious window. I never managed to arrange it in a way that I liked, though. In the end, I went with only a single candle, which has a drama all of its own.

'''},


]

for page in pages:
  page ["auto_paragraphs"] = True
