#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

import datetime

def page (number, transcript, annotation = ""):
  return {
    "xcf_base": "thorough_p" + str (number),
    "force_date": datetime.date (2011, 1, 26),
    "auto_paragraphs": True,
    "transcript": transcript, "annotation": annotation}
    

pages = [
page (1,''''''),
page (2,''''''),
page (3,''''''),
page (4,''''''),
page (5,''''''),
page (6,''''''),
page (7,''''''),
page (8,''''''),
page (9,''''''),
page (10,'''''','''
<h2>Author's notes</h2>

<p>I wrote this in 2011. It was my first serious graphic story, and only my second story that emphasized neurodiversity. I have mixed feelings about it now.</p>

<p>What is the point of the story?</p>

Maybe it's a moral fable? Lucia does something wrong, then suffers for it, then (perhaps) learns a lesson. The point of a moral fable is to teach the reader that they shouldn't do what Lucia does. Maybe this story does that. But that story would normally be told from Lucia's perspective, and this one is told from Ilse's perspective.

Maybe it's a revenge fantasy? Ilse feels wronged, retaliates, and feels vindicated. If the reader shares Ilse's frustrations, maybe it helps the reader feel some catharsis. But Ilse's feelings are based on my own, and <em>I</em> don't feel good about the ending at all. I really don't like the idea of this story being a revenge fantasy.

As a writer, my instinct is to make things as dramatic as possible. Here, that made me give you a snapshot of the moment when two people hurt each other the most. That might not have been a good thing. Neurotypical people often have an unreasonable fear that neurovariant people (like Ilse) will hurt them, and this story might encourage that fear. In the future, I would rather write stories about how neurotypical and neurovariant people can cooperate in a way that is good for everyone.

In fact, one of my earlier concepts for this story was much more like that. In that version, a bunch of Ilse's classmates were facing some sort of crisis. The other classmates panicked and made things worse, but Ilse &ndash; who didn't have any emotions about the crisis at all &ndash; was able to stay calm and help them get things under control. Honestly, I wish I had written that version of the story instead of this one.'''),

]

'''Note: I can't really figure out a good place to put this in the notes:

When I first showed this story to people, everyone had a completely different reaction to it. I don't mean they just <em>disagreed</em> with each other. It was less like the difference between apples and oranges, and more like the difference between apples and northwest.
'''