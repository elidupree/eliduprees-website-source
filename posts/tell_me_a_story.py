#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import re

default_barriers = [
  "violence of any kind",
  "graphic details of violence",
  "death",
  "sexuality",
  "sexual violence",
  "child abuse",
  "depression",
  "self-harm",
  "suicide",
  "bigotry of any kind",
  "nonconsent between player characters",
  "physical touch between the players as part of the roleplaying",
  "out-of-character deception, including deception that blurs the line between in-character and out-of-character"
  "telling a story at all",
]

posts = [
{
  "title":"Tell Me a Story",
  #"blurb": ???,
  "auto_paragraphs": True,
  "don't deploy": True,
  "head": '''
  <style type="text/css">

  </style>
  ''',
  "contents": f'''
  
[????? intro for RPG players, intro for theater improv players]

[????? The GM, if any, is a player; "player" can be taken either as game player or as actor]
  
<h2>Consent</h2>

Roleplaying can touch on sensitive issues. This can be both poignant and therapeutic, but it also has risks. We also want to make sure no one gets emotionally hurt.

The first line of defense is the players' own social skills. [????? brief general stuff about how to use social skills]

There are also some explicit rules to guide the process.

<h3>Barriers</h2>

A <strong>barrier</strong> represents something that <strong>will not happen</strong> during the roleplaying, such as "there will not be any torture in the story" or "?????". Any player may create a new barrier whenever they want. If the players want to explore the content locked behind a barrier, they must follow the procedure for <strong>unsealing</strong> the barrier with the unanimous consent of all players (described below).

When the game begins, there are {len(default_barriers)} <strong>default barriers</strong> already in place. These barriers prevent:

<ul>{"".join(f"<li>{barrier.capitalize()}</li>" for barrier in default_barriers)}</ul>

Naturally, the players will want to <strong>unseal</strong> some of these barriers at the beginning of gameplay.

<h4>Unsealing barriers</h4>

Unsealing a barrier always follows this protocol:

<ol>
<li>A player says "I'm interested in unsealing [one or more specific barriers]. How does everyone feel about that?"</li>
<li>The players discuss how they feel about it. During the discussion, the players may say things that indicate consent to unseal the barrier. These are the <strong>keys</strong>.</li>
<li>If everyone expresses good consent, someone will say, "I think we have all the keys needed to unseal this barrier. Everyone ready? 3, 2, 1… Alberolingarn! (Everyone says Alberolingarn together.)</li>
</ol>

At this point, the barrier(s) are now unsealed!

Here are some examples of <strong>keys</strong>:

<ul>
<li>"I'm excited to roleplay this!"</li>
<li>"It doesn't bother me to include violence in the game."</li>
<li>"Oh man, I'm so freaked out. Let's do it."</li>
<li>"I'm actually feeling a lot of discomfort about acting out gaslighting, but I definitely want to support you processing that through roleplaying, so I'm in."</li>
</ul>

And here are some things that are <strong>not</strong> keys:

<ul>
<li>"I might be okay with that."</li>
<li>"I mean, I don't want to get in the way of the story you want to tell…"</li>
<li>(Uncomfortably) "Sure, if you want."</li>
<li>(Zoned out, looking at their phone) "Yeah, sounds good."</li>
</ul>

If not everyone speaks a key, that's okay. It just means you didn't unseal the barrier that time. There are many stories



<h4>Example of barriers in action</h4>

GM: As we've discussed, I have plans to run a murder mystery with all of you. So I'm interested in unsealing the barriers against, let's see… Violence of any kind; Graphic details of violence; Death; Suicide; and Telling a story at all. How does everyone feel about that?

A: Sounds awesome!

B: Um, why suicide?

GM: A lot of murder mysteries have a murder that's made to look like suicide, or vice versa. Since it's a mystery, I can't tell you whether that's actually included in my game, but –

B (reluctantly): I guess that makes sense…

GM: Okay, it looks like we don't have the keys for Suicide. I can work with that. How do you feel about the other barriers?

B: I do love a good murder.

C: I'm confused, why did you say we don't have the keys for Suicide?

GM: I'll explain it this time, because it sounds like we have a confusion about the rules. B sounded reluctant to me, which means they weren't giving the affirmative consent needed to form a key to the barrier. In the future, let's avoid asking questions about why we don't have keys, because it can draw attention to someone who might already be feeling under pressure to be okay with something they're not.

C: Oh, sorry.

GM: It's okay, you just didn't understand. How do you feel about the barriers?

C: I'm not bothered by any of that stuff.

GM: Alright, I think we have all the keys needed to unseal Violence of any kind; Graphic details of violence; Death; and Telling a story at all. Everyone ready?

Everyone nods or says yes.

GM: 3, 2, 1…

ALL: Alberolingarn!

Later, as the story begins:

GM: It was a dark and stormy night. As the sun rose and tried to peep its way through the shadowy clouds, the old grove tender, Seotani, while making their daily round, spotted a human shape hanging upside down from a tree. As Seotani approached closer, the gruesome truth became clear. The body had one shoe missing, and more importantly, a metal spike through one eye, dripping blood onto the –

B: Eurgh!! Right in the eye?!

GM: Oh, sounds like we might have a barrier against eye trauma?

B: I was just reacting in character. This is good stuff.

GM: Okay. So, the body –

A: Actually, I think I might want that barrier…

GM: Got it. (GM writes down "Eye trauma" on the list of barriers.) I just have to think about how to tweak my plot to accommodate that… Is it cool if the spike is going through their heart instead?

In a later game session:

B: So, last night, I was thinking about how in the first session, I wasn't sure about having suicide come up in the game. I've known a lot of people who make a joke out of it. But now that I've played with you all for a few hours, I think I can trust you all to handle it respectfully. So… I guess the barrier is unsealed now?

GM: I'm glad to hear that we've made you comfortable. Technically, the barrier isn't unsealed until we go through the protocol. Want to do the honors?

B: Alright, uh… I'm interested in unsealing the barrier against suicide. How does everyone feel about that?

A, C, and GM: Sounds good to me!

B: Everyone ready? 3, 2, 1…

ALL: Alberolingarn!



<h4>?????</h4>

Sometimes when you unseal a barrier, you only want to unseal it under certain conditions. A player might say, "I'm interested in unsealing the barrier against self-harm, but only for this one character specifically. I don't want it to be something that can come up unexpectedly." When the unsealing is finished, it still has this limited scope, unless the players do the protocol again later to unseal it further.

Every unsealing has one <em>implicit</em> scope limit: It only applies to the players who were there at the time. If a new player joins, you need to unseal the barriers again.

If someone stops by to watch the game without participating, you're encouraged to include them in unsealing the barriers. However, it's not required, especially if the observers may come and go, or if you have a larger audience.

<h4>If someone violates a barrier…</h4>

Ideally, no one would ever violate a barrier. However,

????

The person who violated the barrier isn't allowed to propose unsealing it on the same day. If the other players think it wasn't a problem, one of them can propose it. If so, they need to go through the usual process for unsealing a barrier – and they shouldn't assume that the person who violated the barrier is okay with unsealing it. Violating a barrier is not a key.


''',
},
]

