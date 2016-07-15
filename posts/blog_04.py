#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime



posts = [
{
  "title":"""Recommended website: Harry Potter and the Methods of Rationality""",
  "force_id":"aafa66a9e73a67747f4436dd0176ac51",
  "force_date":datetime.date(2011, 6, 27),
  "tags":["other websites"],
  "contents":'''

<p>I had to take a break from my coding and blogging for the last few days because of a hurting thumb. It still hurts somewhat, but I've become proficient at typing without using that thumb. In the meantime, I spent my two-day break reading <i>Harry Potter and the Methods of Rationality</i>, a work of fan fiction based on the <i>Harry Potter</i> series.</p>

<p>(The rest of this post will assume general knowledge of the plot of <i>Harry Potter</i>, but does not contain spoilers.)</p>

<p>The TV Tropes Wiki describes <i>Harry Potter and the Methods of Rationality</i> (abbreviated HP:MoR) as "an Alternate Universe story, where Petunia married a scientist." Instead of being completely awestruck by the wizarding world after <cut>having been abused<footnote((Although I hesitated to use the term. The way Harry's aunt and uncle treat zem in the <i>Harry Potter</i> series, if taken literally, is abusive, but the series treats it as a joke or caricature, and Harry is depicted more as a blank slate than as someone dealing with the aftermath of that kind of treatment. I explored this more when I wrote <a href="/voldemorts-children">Voldemort's Children</a>.))> at the hands of zir relatives, Harry Potter has been raised in a healthy environment and taught the virtues of the scientific method, and walks into the wizarding world intending to apply science to magic and transform the world. To put it a different way, ze tries all the things that made me frustrated at the original Harry when ze <em>didn't</em> try them. It also answers a lot of the annoying questions that the original series overlooks in order to write a morally-unambiguous<footnote((Yes, the good guys are not always good and the bad guys are not always bad, and Harry has to discover that. None of that changes the fact that it's written as a story where good guys fight bad guys and the good guys win.))> adventure story. In short, it's a beautiful work of deconstruction, and <strong>also</strong> a great attempt to educate the reader about the scientific method and common fallacies. And also a hilarious parody of the original.</p>

<p>However, I do have some reservations about recommending it. Like any work of deconstruction, it still has all the flaws of the original story <em>except</em> for the ones it specifically takes away. Like the fact that Harry Potter, the character, is a white, male, cis, able-bodied, heterosexual, upper-class, neurotypical person, in a way that treats all those attributes as the default, the "normal" attribute, and the opposite as unusual.<footnote((A brief note about the original series &ndash; trans people and non-heterosexual people don't exist in the story as written, and for the few neurodivergent people (Voldemort, Luna, Trelawney...) we only get the outsider's perspective that they're "weird" or "cool" or "completely evil", rather than seeing their own perspectives or challenges. Like Hermione, and like Rowling's public claim that Dumbledore is gay, they're A Lesson for members of the dominant class (<q>Hey you! You'd better believe it's okay for people to be Different!</q>) but they are not role models and they do not tell our stories. J. K. Rowling also seems to believe that Love is the most important thing in the world and it's everyone's deepest emotion, which is (guess what?) not true in the real world.))> HP:MoR Harry is not quite as much like that &ndash; ze's arguably not neurotypical, and the story treats adults' age-discrimination as a serious issue &ndash; but the rest is still there, and I'm a little tired of the "genius protagonist" being always male. In general, HP:MoR has upgraded a lot of the male characters from <i>Harry Potter</i> while leaving female characters the same, downgrading them, or putting them in victim roles. It does seem to be trying in some places to deliver a feminist message, but it fails horribly. I wouldn't normally recommend something with that much sexism. And Harry treats the 17th-century European "Enlightenment" as the only source of rationality in the world, or of belief in human rights, which is kinda unfair to all the philosophers of the rest of the world.</p>

<p>And finally &ndash; if you have triggers, READ THE TRIGGER WARNINGS. Unlike the original series, HP:MoR does NOT gloss over the more horrible things in the world.</p>

<p><a href="http://www.fanfiction.net/s/5782108/1/Harry_Potter_and_the_Methods_of_Rationality">The story begins here</a>, and the (somewhat incomplete, be warned) <a href="http://wiki.lesswrong.com/wiki/MethodsOfRationality/TriggerWarnings">trigger warnings page is here</a>.</p>

''',
},
{
  "title":"""A few concepts I need""",
  "force_id":"519bd2c2951fe72ff2c96e6c816c5bc8",
  "force_date":datetime.date(2011, 6, 27),
  "tags":["visual art","the graphics editing project"],
  "contents":'''

<p>I made progress again on my graphics editing stuff; I have a program that takes tablet input and converts it into individual lines/strokes. That task was surprisingly easy; once again, I'm a bit unsure of what to do next.</p>

<p>So I just set myself a specific task: <em>Create the software that I would want to use to write <a href="/people-are-wrong-sometimes">People Are Wrong Sometimes</a> if I'd written it with this instead of on paper.</em></p>

<p>Which of course raises the question "What do I need for that?". So I looked over <i>People Are Wrong Sometimes</i> from a conceptual perspective, turning the question into <cut>"What are the things in it?".</p><ol><li>Lines (straight or curved), of varying colors.</li><li>Fields bounded by straight/curved lines, of varying colors.</li><li>Text</li></ol>

<p>I already have the concept of <strong>lines</strong>.</p>

<p>One interesting thing that I notice about the lines is that they almost <em>never</em> cross; usually, one line is cut off by another (e.g. panel borders cut off the image, speech bubbles obscure objects in the panel, and some objects or people are in front of others...). In my pencil and pen drawings, I had to carefully end each line where the next began. In my computer programs, I should have a way to automatically have one line cut off another, which means I need the concept of <strong>where lines cross</strong>. And, on a related note, I should have a way to automatically detect when I've surrounded a region completely, so that region can be filled with color.</p>

<p>For the moment, I'm going to ignore the text. I like the way I used a variety of different typefaces in <i>People Are Wrong Sometimes</i>, but I don't like the way I was relying on pre-existing typefaces that didn't necessarily fit the overall visual style of the piece, and I don't like the fact that I didn't have precise control over the size and flow of the text. On the other hand, I definitely wouldn't like to write all the text myself; my hands hurt if I write for long periods of time, and my handwriting isn't very good. I've heard that some artists draw their own typefaces (where since you only have to draw each letter once or twice, you can spend a lot of time getting it right); I might want to do that, but it's something for later.</p>

<p>In the writing process of <i>People Are Wrong Sometimes</i>, I drew a lot of sketches; I sketched out everything in pencil first, with a lot of experimenting and erasing, then drew over it in pencil to decide exactly what I wanted, then drew over it in pen and erased the pencil marks before scanning it. In the computer, I'll need that same leeway to draw and redraw, so I need a concept of <strong>selective erasing</strong>. And I'm going to need to be able to erase one line without erasing another that's very close to it. Internally, the lines are all going to be numbered, but in my user-interface, I'm going to need a way to refer to them without typing in numbers all the time. Maybe that could be accomplished just by zooming in (and having a mode<footnote((And when I say "mode", I probably mean a key that I hold down while drawing. Holding a key with one hand while drawing with the other might be inconvenient, but it's a lot less inconvenient than accidentally leaving the mode on and then trying to draw a real line. The book <i>The Humane Interface</i> calls hold-down-a-key modes "quasimodes", and recommends them highly.))> where I use the tablet-pen as an eraser.)</p>

<p>I'm also going to want a really sophisticated <strong>undo</strong> system, for when I make mistakes &ndash; INCLUDING mistakenly undoing things. My current plan is to store a complete record of all operations (like drawing a line or changing a line's color) on an image, including undo operations, and have it be theoretically possible to re-construct the image from nothing just by going through all the operations. And have them be discrete/separable enough that you could go back and "undo" individual long-ago operations without having it interfere with the rest of the chain. But of course, doing that would be simply adding an "undo" instruction to the <em>end</em> of the chain. The advantage of this system is that it makes me automatically able to go back to <em>any</em> version of the image, even dead-end versions that I didn't like at the time and undid. I'm going to want to have the operation-log be displayed on-screen, along with the actual image, and have various features that let you mess with the image from that perspective.</p>

<p>I also need to be able to move, zoom, and rotate the drawing field.</p>

<p>Some things that I could have used, but (deliberately) didn't use in <i>People Are Wrong Sometimes</i> are: Continuous shading, texture/pattern, significantly-varied line weight... it was, very explicitly, constructed out of the concepts of line and field, rather than being constructed as marks on paper. I like drawing in that way; remind me to make a post about how drawing can be done from an abstract/conceptual communication perspective, just as much as writing can.</p>

''',
},
{
  "title":"""Happy Tau Day!""",
  "force_id":"9b5e383fd8165a4b6cba1e01ff5fab20",
  "force_date":datetime.date(2011, 6, 28),
  "tags":["math","other websites"],
  "contents":'''

<p>(This post assumes a certain amount of knowledge about math.)</p>

<p>I think it's really cheesy to do something on June 28 just because the decimal expansion of &tau; begins "6.28...", but well, I might as well do it today as any day.</p>

<p>If you've studied mathematics in the modern world, you've probably run into a number called <em>pi</em>, or &pi;, which represents the ratio of a circle's circumference to its diameter. That's weird and confusing, because pretty much every other mathematical concept about circles is based on the <em>radius</em> of the circle, not its diameter. The diameter is exactly twice the radius, so lots of formulas involving &pi; end up referring to the quantity 2&pi;.</p>

<p>This is pretty silly, becuase the "2" in "2&pi;" doesn't really mean anything. It's just a correction factor to make up for the fact that the number we're calling "&pi;" is exactly half of what the natural value for the circle constant is. That leads to confusing things like the fact that rotating by &pi; radians is a <em>half</em>-rotation, not a full rotation... and if you want to rotate by three-quarters of a circle, you have to rotate by 3&pi;/2, which is completely confusing.</p>

<p>So, a lot of mathematicians, including myself, are now using a new name for the quantity "2&pi;" &ndash; namely, <em>tau</em>, or &tau;. Its value is approximately 6.283185307..., hence the cheesy date of June (the sixth month) 28.</p>

<p>More information at <a href="http://tauday.com/">http://tauday.com/</a>.</p>

''',
},
{
  "title":"""Sex""",
  "force_id":"4c683100e139533812ade5a882129d77",
  "force_date":datetime.date(2011, 6, 29),
  "tags":["ageism","sex"],
  "edited_significantly_from_old_website": True,
  "contents":'''

<p>(This post will contain straightforward descriptions of sexual stuff. If you think that's obscene, now is the time for you to stop reading... and reconsider your sense of morality.)</p>

<p>In this post, I'm going to talk about what sex is, as in "to have sex" or "to be sexually active". Like a lot of other things I've talked about, our society thinks this is really important, but can't agree on what it means!</p>

<p>Society is full of myths and lies about sex &ndash; about what it means to have sex, about when you should have sex, about who should be having sex, about how many people you should have sex with, and so forth. In fact, there are <em>so many</em> myths and lies that I can't possibly address them all in one post. There are the traditional, Puritanical lies, like <q>You should never do anything sexual except with your spouse in a heterosexual marriage</q>. Lots of people disagree with that now, you say? Well, yes. But plenty of them have their own myths and lies, like "You should always have sex by your third date"<footnote((Which assumes that relationships only happen by dating, which I could write an entire rant about separately.))>. No matter who you ask, someone is going to tell you how <em>they</em> think <em>you</em> should live your life.</p>

<p>All these myths cause a lot of problems. But there are too many problems for me to discuss one at a time. If I pointed out any <em>three</em> of them individually, I'd feel guilty for not pointing out all the rest.<footnote((Actually, I wouldn't feel guilty; I'm not sure "guilt" is a feeling I ever experience. But I would feel like my essay wasn't doing a good enough job.))> So I'm going to throw that all out and start over from the beginning.</p>

<h2>What the fuck is sex, anyway?</h2>

<p>Humans are strange creatures with strange feelings. I could <cut>mention a bunch of terms like "sexual attraction", "sexual arousal", "sexual release", "lust", "orgasm"... But if I tried to describe sex in terms of those things, I'd be writing a circular definition. Suppose you don't know what any of those terms mean, but still have sexual feelings yourself: How would you know which word matches which feeling? After all, a person can enjoy looking at someone else in a non-sexual way; ze can be physically excited in a non-sexual way, satisfied in a non-sexual way...</p>

<p>We could say it has something to do with your genitals, but would that really work? There are plenty of ways to be sexual that don't involve genitals, and plenty of things to do with your genitals that aren't sexual, like peeing. And there are people who don't even <em>have</em> genitals who still have sexual feelings. We can get a vague idea of what it is by talking about genitals and touching and arousal and stuff, but how do we <strong>define </strong> it?</p>

<p>I propose a novel solution:</p>

<h2>Don't.</h2>

<p>I'm going to take a step sideways here.</p>

<p>Some people say that <strong>consent</strong> is an important concept when talking about sex and sexuality. The first rule is "No means no": If a person says "no" to a sexual activity, then it's bad to push them into doing that activity. The stronger rule is "Yes means yes": Unless a person <em>actively agrees</em> to do a sexual thing, then they have not consented, so it's not okay to do it.</p>

<p>Look at the above paragraph. <em>There is no reason for the word "sexual" to appear in it.</em></p>

<p>Suppose you and a friend are hanging out and you want to play a board game. You suggest playing the game. Your friend shrugs. You go and get the board game and set it up, then hand your friend the dice so that ze can take zir first turn. Ze hesitates. "Come on," you say, "I already set it up and everything." Then ze rolls the dice and makes a move.</p>

<p>You've just pushed your friend into doing something ze did not want. <strong>Compliance is not consent</strong>, so you're now nonconensually playing a board game. That's a bad thing that you shouldn't have done.</p>

<p>Certainly, this is <em>less</em> bad than pushing someone into sex. People usually have much stronger feelings about sexual stuff, and many sexual things have some risk of physical harm. But the principle is the same. One of them is worse than the other, but they're both bad for the same reason. Humans are supposed to cooperate with each other to do things that help everyone. And because humans are often very different from each other, it's impossible to cooperate without clear communication. In the example with the board game, instead of deciding what <em>you</em> wanted and then trying to get your friend to want it too, you should have asked zem what ze was interested in and tried to find something you'd both like.</p>

<h2>A personal story</h2>

<p>I enjoy tying myself up for sexual pleasure. I can (when I want to) get very sexually aroused by the idea of being helpless, of being immobile, of having other people beat me at games or contests, of being held or touched or hurt against my will. I'm also <em>extremely</em> hostile to anyone who tries to do any of these things to me, or even play at doing them to me, without my consent.<footnote(a(I'd be somewhat interested in doing it consensually with other people I trust, but coordinating with other people is too much of an inconvenience for me to try very hard at that. If you're reading this and you know me... you interested? :-))a)></p>

<p>Most of that has been true since I was in elementary school (ages 5-9, for non-US people). I didn't have a "sexually aroused" feeling until after puberty, but I enjoyed tying myself up, with as little clothes on as my family would allow. I also associated my thoughts about that with a feeling in my genitals (which, in my case, are a penis and testicles). I liked reading books that talked about medieval torture methods, because I was fascinated with that feeling. I didn't talk about it much, because other people, both at school and at home, had discouraged me from touching my genitals, talking about my genitals, or, basically, doing anything that <em>acknowledged the existence</em> of my genitals. In this way, adults prevented my child self from enjoying zir sexuality. Adults should not do this; it's a bad, harmful thing to do, although it's hardly the worst thing that anyone did to me in my childhood.</p>

<p>(There's also a complicating factor: Throughout my life, my <em>non-sexual</em> daydreams and fantasies have also often been about traumatic experiences that I haven't personally had. I remember, around age 9, reading a book about some real-life heroes who suffered severe injuries, not because I liked heroism, but because I liked injury. I don't know why I'm so fascinated with pain and suffering, but it's something that is pretty much innate and constant for me.)</p>

<p>I remember that I was always unwilling to play a lot of physical games, like <a href="http://en.wikipedia.org/wiki/Tag_(game)">Tag</a> and <a href="http://en.wikipedia.org/wiki/Capture_the_Flag">Capture the Flag</a>, with other children. When people <em>did</em> force me to play the games, I cheated at them. I'm beginning to suspect that that's because I associated losing at games with sexuality, especially when the games involved physical touch. I am <em>not okay</em> with anyone doing anything sexual with me unless I have complete trust in them as a friend, and there are less than a dozen people in the world whom I trust that much (although it's been going up now that I've been at college). Of course, it was <em>extremely not okay</em> for anyone to be forcing me into playing those games in the first place. I think some adults did it because they falsely believed that it would help me socialize with other children. Or maybe they just did it because that was how they normally do things. If they had paid attention, or <em>asked</em> me, they would have realized it wasn't helping anything. I didn't want to socialize with groups of other children, anyway.</p>

<p>While I'm talking about myself, I might as well mention that I'm not sexually attracted to humans, regardless of their sex or gender, and I don't particularly like orgasms. I masturbate to orgasm sometimes, but that's really only <em>in order to stop</em> feeling aroused. There's a stereotype about men as being only interested in sticking their penises in things until they orgasm; although I am not male, I arguably still count as a counterexample, because that whole system of stereotypes would assume that I am male, too. But anyway, I much prefer slow and deliberate touch, over all my body, rather than excessively genitals-focused, goal-focused stuff (and I think that stereotype connects to a lot of other male stereotypes. Ugh.).</p>

<p>All of those attributes of me are perfectly normal, and not unhealthy in any way. (Adults mistreating me was unhealthy for me, but my preferences weren't unhealthy by themselves.) And if, on the other hand, you <em>don't</em> have any of the attributes that I've just described, that's <em>also</em> perfectly normal, and not unhealthy in any way.</p>

<h2>Back to the big picture</h2>

<p>By now, you probably get the main point I'm trying to make: Different people like different things, and that's exactly how it should be. Some of those things are sexual, but it doesn't really matter <em>too</em> much to figure out which ones are sexual and which aren't. Since people aren't all the same, they don't instantly know how other people feel. However, it's possible to deal with that by communicating in a clear, honest, cooperative way. And you shouldn't listen to other people telling you what you should like &ndash; you should figure out what you like for yourself.</p>

<p>All of that should be <em>obvious</em>.</p>

<p>(Oh right, there's a cultural norm that says it's bad to just enjoy yourself for the sake of enjoying yourself &ndash; especially in a sexual way, but also in general, becuase it's more important to do what's culturally acceptable than to do what you like! And there's this whole notion that what two (or more, or just one) consenting people<footnote((Yes, PEOPLE. I only just noticed that people usually say "consenting adults" when they say this. Now that I thought about it, I'll have to be a little skeptical whenever I see someone write it in that way.))> do in private is anybody else's business. And there's the belief that&mdash; ...but all those beliefs are stupid and ridiculous and I have no idea why anyone believes them<footnote((Actually, I do have a lot of ideas about why people believe those things. It's just that they don't make any <em>sense</em>.))> and I should have stuck to my plan to not try to talk about them in this post! Clearly I should stop now before I accidentally dignify those notions with a <em>response</em>.)</p>

<p>If you liked this post, <a href="/blog/pornography">join me again in a few <del>days</del> <ins>weeks</ins> when I rant about pornography</a>.</p>

''',
},
{
  "title":"""Recommended website: Fugitivus""",
  "force_id":"7c36c699e644ea692cb69274bdd37901",
  "force_date":datetime.date(2011, 7, 2),
  "tags":["other websites"],
  "edited_significantly_from_old_website": True,
  "contents":'''

<p>So, there's a blog. A <em>feminist</em> blog. On the <em>Internet</em>. And it's really good. If you like feminism, you should probably read it. If you dislike feminism, you should <em>definitely</em> read it.</p>

<p>Its name is Fugitivus.</p>

<p>The writing at Fugitivus informs a lot of the way I think about interpersonal abuse. Which means it informs a lot of the way I think about how people interact with each other in general, because I think there's a lot of subtle abusive behaviors in almost every interaction between two or more people. (For that matter, there's a lot of subtle abusive behaviors in most people's interactions with themselves.) A year and a half ago, I read essentially the entire blog archive, and it has seriously changed how I think about other humans, especially in relation to gender (it is a <em>feminist</em> blog, after all). Harriet J, the author, has good ideas, and ze is a really, really good writer.<footnote((For me, at least. Different kinds of writing appeal to different people, and it would be foolish to say that there's a single standard for "good writing". That said, there are a lot of things I think Harriet J does well &ndash; ze gets to the point, has a clear flow from idea to idea... but instead of writing you an extensive footnote about these nuances, I invite you to just go and read zir blog.))></p>

<p>I recommend Fugitivus without reservation. However, since it contains a lot of discussion about rape and abuse, you might not want to read it at a time when you're going to need to feel good about the world in the near future.</p>

<p><del>Fugitivus is at (surprise!) www.fugitivus.net.</del> UPDATE: fugitivus.net is dead now. An older version of the blog, with most of the posts still visible, still exists at <a href="https://fugitivus.wordpress.com/">fugitivus.wordpress.com</a>. The "Top Posts" in the right sidebar are a good place to start.</p>

''',
},
]
