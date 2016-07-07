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
page (1,'''TITLE: PEOPLE ARE WRONG SOMETIMES <br/><br/> The title is in a thought bubble. The thought continues: ...even about things they should know closely. I don't like it when people are wrong. <br/><br/> The thought bubble is coming from Ilse. Ilse is drawn with simple shapes, straight lines, and sharp corners. Most of the page is black-and-white. The only color is a bright red item worn by Ilse. Sometimes the item is a sash, sometimes it is a shoulder pad, and sometimes it is a bracelet. In the first image, where Ilse is thinking, Ilse has closed eyes and a slight frown. Usually, none of Ilse's facial features are drawn.
<br/><br/>
Ilse closes a door behind zem.
<br/><br/>
ILSE (thinking): I'm glad I'm out of there.
<br/><br/>
Ilse begins walking away.
<br/><br/>
ILSE (thinking): Fuckin' parties.
<br/><br/>
LUCIA (yelling from off-page): ILSE!'''),

page (2,'''Lucia runs up. Lucia is done in a much more detailed style than Ilse. Ze is wearing shorts and a sports shirt with blue shoulders. (Everything except that blue, and the red on Ilse, is still black-and-white.) Lucia is usually drawn with eyes and a mouth, and often smiles.
<br/><br/>
LUCIA: I knew you'd sneak out!
<br/><br/>
ILSE: Lucia...
<br/><br/>
Lucia's speech, and Ilse's thoughts on the previous page, were drawn in a handwritten-looking style. However, when Ilse speaks to Lucia, ze speaks in a mechanical font.
<br/><br/>
LUCIA: You're my best friend... No way am I going to let you run off all by yourself!
<br/><br/>
Lucia puts a hand on Ilse's shoulder.
<br/><br/>
LUCIA: I know you don't like parties, but you should really try harder!
<br/><br/>
ILSE: I guess...
<br/><br/>
LUCIA: We're all going to be off to college in no time, and this is our only graduation party. Come back with us &ndash; you'll have lots of fun.
<br/><br/>
ILSE: Like I was having already?
<br/><br/>
ILSE: Compromise: I'll take you to the cafe downtown.
<br/><br/>
LUCIA: Alright... But you'll miss everyone...
<br/><br/>
ILSE: No. I don't care about any of them.
<br/><br/>
LUCIA: What's gotten into you?
<br/><br/>
Ilse pauses, turns around, and stares at Lucia.
<br/><br/>
ILSE: Honesty.'''),

page (3,'''Ilse walks through the doors of a café.
<br/><br/>
LUCIA: You've been quiet...
<br/><br/>
ILSE: I'd rather talk in here.
<br/><br/>
Ilse points out a booth in the café. They both sit down, facing each other. Six other people are sitting at tables in the background.
<br/><br/>
ILSE: I leave tomorrow. Someone with a cousin in Cali. I won't see most of you again...
<br/><br/>
ILSE: ...so I don't have to pretend anymore.
<br/><br/>
LUCIA: I'll be so...
<br/><br/>
Inside the speech bubble, we see Lucia sitting on a bench with a blue cloud hovering over zem. Ze is thinking sadly about Ilse. In the speech bubbles where Lucia is talking about Ilse, Ilse is drawn in a curvy style, instead of the usual straight lines and sharp corners, and ze has zir eyes and mouth visible as well.
<br/><br/>
LUCIA: And you'll be so...
<br/><br/>
Inside of the speech bubble, we see Ilse standing in front of the Golden Gate Bridge, which is drawn in bright red. Ilse is thinking sadly about Lucia.
<br/><br/>
ILSE: No. I'll find someone else to get my "good friend" fix from. I won't miss you.
<br/><br/>
LUCIA: But...!'''),

page (4,'''LUCIA: No offense, but that's absurd! Think of everything we've done together!
<br/><br/>
Three more speech bubbles come from Lussier. In each of them, we see a memory of Lucia and Ilse having fun together. In one, they are playing a board game with another two friends. In one, they win a game of doubles tennis and high-five each other. In one, they dress up as characters from Star Wars and fight with fake lightsabers.
<br/><br/>
LUCIA: We have years of shared experiences between us, and we'll keep that wherever we go. Friends don't disappear when you part with them; they become part of you. And the memory of them comes back to you, whether you want it to or not. And you miss them.
<br/><br/>
ILSE: I'm not so sure... Those memories don't excite me the way they excite you.
<br/><br/>
ILSE: We've done fun things in the same places and at the same times, yes, but does that make us connected? I don't know about you, but... I don't feel connected.'''),
page (5,''''''),
page (6,''''''),
page (7,''''''),
page (8,''''''),
page (9,''''''),
page (10,'''''','''
<h2>Author's notes</h2>

<p>I wrote this in 2011. It was my first serious graphic story, and only my second story that emphasized neurodiversity. I have mixed feelings about it now.</p>

<p>What is the point of this story?</p>

Maybe it's a moral fable? Lucia does something wrong, then suffers for it, then (perhaps) learns a lesson. The point of a moral fable is to teach the reader that they shouldn't do what Lucia does. Maybe this story does that. But that story would normally be told from Lucia's perspective, and this one is told from Ilse's perspective.

Maybe it's a revenge fantasy? Ilse feels wronged, retaliates, and feels vindicated. If the reader shares Ilse's frustrations, maybe it helps the reader feel some catharsis. But Ilse's feelings are based on my own, and <em>I</em> don't feel good about the ending at all. I really don't like the idea of this story being a revenge fantasy.

As a writer, my instinct is to make things as dramatic as possible. Here, that made me give you a snapshot of the moment when two people hurt each other the most. That might not have been a good thing. Neurotypical people often have an unreasonable fear that neurovariant people (like Ilse) will hurt them, and this story might encourage that fear. In the future, I would rather write stories about how neurotypical and neurovariant people can cooperate in a way that is good for everyone.

In fact, one of my earlier concepts for this story was much more like that. In that version, a bunch of Ilse's classmates were facing some sort of crisis. The other classmates panicked and made things worse, but Ilse &ndash; who didn't have any emotions about the crisis at all &ndash; was able to stay calm and help them get things under control. Honestly, I wish I had written that version of the story instead of this one.'''),

]

'''Note: I can't really figure out a good place to put this in the notes:

When I first showed this story to people, everyone had a completely different reaction to it. I don't mean they just <em>disagreed</em> with each other. It was less like the difference between apples and oranges, and more like the difference between apples and northwest.
'''