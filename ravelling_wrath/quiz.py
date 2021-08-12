#!/usr/bin/python3
# -*- coding: utf-8 -*-

waiting = '''
I spend lots of time planning out things I'm going to do or say in the future.
If I know I will get something good in the future, that's almost as good as having it right now.
I spend lots of time thinking about things from the past.
If someone helped or hurt me a long time in the past, it strongly affects how I treat them in the present, even if they've changed since then.
I have a strong sense of what I want my future (or legacy) to be.
'''
seeking = '''
I'm only satisfied with life if I'm always learning new things.
When I see something unfamiliar, my first thought is to wonder how it works.
I would rather jump into a risky opportunity than stick to something boring and effective.
I like to solve problems in unexpected ways rather than well-known, practical ways.
When I think of a terrible idea, I'm tempted to do it just to see what would happen.
'''
stern = '''
I have principles I would not violate for any reward or threat.
I work hard to accomplish the things I believe in.
I like it when there is a strong system of rules about how things should be done.
Even if someone will get hurt because I stick to my principles, it is still better to stick to them.
Lying to make someone feel better is always wrong.
It bothers me when people do things the wrong way, even when it doesn't personally affect me.
'''
broken = '''
I'm more motivated by habits and immediate desires than by goals or principles.
I often can't make sense of the things people say they have strong opinions about.
When a problem is hard to solve, I tend to let go and leave it unsolved.
I don't have a strong sense of identity or purpose in life.
I can easily admit to myself when I'm unable to accomplish something.
'''
blood = '''
I'm happy to be the person I am.
I take my own needs seriously, even when other people are having worse problems.
Logic and emotion aren't opposites. I am both emotional and logical, and they work well together.
It is inherently injust for one social group to have higher status than another, even if it happened as a natural result of people's choices.
Everyone, including children, should have the freedom to make choices that risk getting themselves hurt.
'''

multiple = '''
I spend a lot of time pursuing knowledge. (Waiting, Seeking)
I keep my promises even when they end up being much harder than I expected when I made them. (Waiting, Stern)
Even when something makes me angry, I often wait for a better moment rather than trying to do something about it immediately. (Waiting, Broken)
I have a strong sense of what my life story is. (Waiting, Blood)
When there's something I don't understand, I won't be content until I've figured it out. (Seeking, Stern)
I'm more interested in how things <em>are</em> than how they <em>should</em> be. (Seeking, Broken)
When I act on my momentary desires, I'm usually satisfied with how it turns out. (Seeking, Blood)
I've accepted that there will always be some suffering in my life. (Stern, Broken)
I don't let other people push me around. (Stern, Blood)
I like to enjoy simple pleasures without thinking about them very hard. (Broken, Blood)
'''

def convert_multiple (match):
  return match.group(1), match.group(2).split(", ")

# https://programmers.stackexchange.com/questions/254279/why-doesnt-python-have-a-flatten-function-for-lists
def flatten(l):
  return [x for y in l for x in y]

questions = flatten([
  [(q, ["Waiting"]) for q in waiting],
  [(q, ["Seeking"]) for q in seeking],
  [(q, ["Stern"]) for q in stern],
  [(q, ["Broken"]) for q in broken],
  [(q, ["Blood"]) for q in blood],
  [convert_multiple(match) for match in re.finditer(r"(.*) \((.*)\)", multiple)],
])

symbols = {
  "Waiting": "watchful-eye",
  "Seeking": "endless-maze",
  "Stern": "dauntless-gate",
  "Broken": "cloven-earth",
  "Blood": "burning-heart",
}