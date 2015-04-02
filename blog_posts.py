#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


signature = "<p> &ndash; Eli</p>"


posts = [
{
  "title":"F1rst p0st",
  "contents":'''<p>This is a test post where I say lots of things, because why not.</p>'''+signature,
  "tags":["lol","omg"],
},
{
  "title":"Post title",
  "contents":'''<p>Lorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum</p><p>dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conv</p>'''+signature,
},









]

other_posts = [
{
  "title":"Policies",
  "contents":'''<ul class="big_list"><li>If you <a href="fixme">sign up for e-mail notifications</a>, I won't share your e-mail address with anyone else.</li>
    
<li>If you comment on a post, <strong>no one else will see it until I approve it</strong>. I make no promises, but I will probably approve anything that's not spam or harassment (or illegal). I may even approve bigoted comments in order to respond to them. It's OK to be misinformed about social issues here, and I hope that this site will educate people. I check incoming comments at least once a day.</li>
    
<li>I am serious about web accessibility. If part of my website is incompatible with an assistive technology, <strong>contact me and I'll try to fix it</strong>. If you see a way I could be more accommodating to people with a certain disability or trait, contact me and I'll try to improve it.</li></ul>''',
},
{
  "title":"About Eli",
  "contents":'''
    
<h2>What's important to me</h2>

<p>I am compelled to invent stories, and sometimes I write them as <a href="/stories">prose</a> or <a href="/comics">comics</a>. I enjoy figuring out how things work, then messing with them. I produce an unlimited supply of imagination, music, and philosophical thoughts. I like to design and play <a href="/games">games</a>. I use computers for most of the things I do.</p>
    
<p>The world can be a pretty awful place. My main <strong>objective</strong> is to make the world a good place. If the world becomes a good place, I win. If it stays awful until the end of all sentient life, I lose.</p>

<p>I'm somewhere on the autism spectrum, and my brain has a bunch of uncommon traits besides that. It's mostly awesome. I have a lot of mental abilities that most people don't.</p>
    
<h2>Other details</h2>

<p>A few of my mental traits can be disabling (e.g. oversensitivity to noise and other sensations), so I do consider myself a "person with a disability", but I don't think of my autism as a disability overall.</p>

<p>I'm agender. I've never felt female or male, not even a little bit. I prefer for people to refer to me by gender-neutral terms and <a href="fixme">pronouns</a>. People often assume I'm male, which annoys me, but it doesn't annoy me much more than any other time that people are wrong about something.</p>

<p>I grew up on the Internet. Physically, I grew up in a suburban town in the US Northeast. I was raised by parents who nurtured most of my interests. I went to high-quality public schools, where many of the adults (and some children) mistreated me for my autistic traits and gender expression.</p>

<p>I'm able-bodied. I'm not religious. I'm middle-class. I'm white. (I know there are times and places where I wouldn't be considered white, but I haven't been to any of those times and places, so that doesn't count.) I have no romantic or sexual attraction to people of any gender, but I do have sexual desires.</p>''',
},
      
]


for i in range(0,50):
  posts.append({
    "title":'Post '+str(i),
    "tags":['omg'],
    "contents":'''<p>she "she" <footnote((lalal neurodiversity))> <footnote((lalal))> "Neurodiversity" Neurodiversity Lorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum</p><blockquote>Lorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conv</blockquote><p>dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conLorem ipsum dolor sit amet, conv</p>'''+signature,
  })

for post_dict in posts:
  post_dict["path_prefix"] = "blog/"
for post_dict in other_posts:
  post_dict["path_prefix"] = ""

"""
{
  "title":""
  "contents":''''''+signature
}
"""
