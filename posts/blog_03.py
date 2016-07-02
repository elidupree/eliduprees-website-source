#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime



posts = [
{
  "title":"""C++ vs. Haskell: ROUND ONE: What's a programming language, anyway?""",
  "force_id":"7a295e9565a6d296278c3cbd6db6ebba",
  "force_date":datetime.date(2011, 6, 15),
  "tags":["programming"],
  "contents":'''

<p>This post is intended to be accessible to people who don't know anything about computer programming. If you already know a lot about computer programming, you might want to <a href="#cppvhaskell1_into_the_personal">skip to the last section of this post</a> where I talk about what I'm doing now.</p>

<p>Computers calculate things. They're very good at it. But to get a computer to calculate something, you need to know how to control the computer. If you're a computer programmer, that means having a program called a "compiler" or "interpreter" that takes things you write in "programming languages" and converts them into a form that the computer can use. C++ and Haskell are both programming languages, but they work in significantly different ways.</p>

<p>I can't just say "Computer, tell me all the prime numbers between 2 and 100", because the computer doesn't understand English. But I CAN open up a Haskell prompt and say:</p>

<pre class="code">[x | x &lt;- [2..100], not . any (\y -&gt; x `mod` y == 0) $ [2..(x-1)]]</pre>

<p>That's valid Haskell code. It says "Get me the list of all numbers between 2 and 100 which are not divisible by any of the numbers less than them", and it pretty much says it in that order, too. This is a really short program because <cut>Haskell is designed to be a very "high level" language. I'll get to what that means in the next paragraph. But first, let's look at how I could do the same thing in C++:</p>

<pre class="code">std::vector&lt;int&gt; primes;
for (int x = 2; x &lt;= 100; ++x) {
  bool x_is_prime = true;
  for (int y = 2; y &lt; x; ++y) {
    if ((x % y) == 0) {
      x_is_prime = false;
      break;
    }
  }
  if (x_is_prime) {
    primes.push_back(x);
  }
}
return primes;</pre>

<p>Augh! It's fourteen lines instead of one! It's more than three times as long even if you only count letters in the most generous way! At this point you should be saying <q><abbr title="What the fuck?">WTF?</abbr> Why would anyone use C++?</q>.</p>

<p>Well, C++ is a "low level" language. There's a low-to-high continuum, with different languages falling in different places; Haskell is at the extreme high end, and C++ is mid-to-low. High level languages are designed to be a lot like human languages; they're supposed to be natural ways to express ideas. Low level languages, on the other hand, are designed to be a lot like the underlying machine code; they're supposed to give you better control over how the computer processes the information. That's very important if you're writing a program that's going to take a lot of processing power, because if you write high-level code that doesn't consider how it's going to be computed, then you may end up doing things in a very inefficient way. So it makes sense that the code I've written is more verbose in C++; when I compile either of those pieces of code into the underlying "machine language", the Haskell code becomes just as long as the C++ code &ndash; I could write it more concisely, at the cost of having less control over exactly what it became.</p>

<p>On the other hand, what if I don't care? In the last ten years, computers have gotten ridiculously fast. Like, RIDICULOUSLY fast. I feel like as long as I don't write an advanced physics simulator, or graphics code, or pointlessly waste calculations, then everything I write will execute in less than a millisecond without me having to do anything about it.</p>

<p>There's another important difference between C++ and Haskell: C++ is an "imperative" language and Haskell is a "functional" language. Imperative languages are essentially a series of commands for the computer: Go here, add these numbers together, stop, display it on the screen, go back and compute some more numbers. This makes sense for low-level languages because that's exactly how a computer works: It has a processing unit that executes simple commands, one after the other.<footnote((Well, modern computers often have multiple processors that work in parallel. And the computers of the future will probably embrace parallel processing even more. But the basic idea is still pretty similar.))> (There are also some high-level imperative languages, but in general, imperative languages are lower-level than functional languages.)</p>

<p>Functional languages like Haskell are different: They don't say "Do this to that". They say "This <strong>is</strong> that". If you want to put it in English terms, my C++ code says "Compute the list of all primes from 2 to 100 and return it", while the Haskell code just says "The list of all primes from 2 to 100". Of course, that can be kind of confusing because, hey, the computer does stuff, doesn't it? Like, right now, your computer is showing you this blog post. It hadn't always showed you this blog post, so if I never told the computer to do something, then how would you ever see anything? I mean, C++ can say "Draw a window, then display stuff until the user quits, then close the window", but what can Haskell do?</p>

<p>Well, the answer is that a Haskell program says something like "The output of this program <strong>is</strong> to draw a window on the screen and display the input the user asks for until the user quits". And I think that's pretty awesome. I don't have to worry "Do these commands make the computer do what I want it to do?" because in Haskell, I didn't write "do these commands", I wrote "this is what I want". And that's in addition to the fact that Haskell code is so much shorter, which makes it easier to read and makes there be fewer opportunities to mess up.</p>

<h2 id="cppvhaskell1_into_the_personal">Into the personal...</h2>

<p>A while ago, I wrote a 2D collision detection library in C++. That's a piece of code that simulates a bunch of objects moving around, and detects when they crash into each other. This is an important thing for computer games. Unfortunately, there's no simple way of doing it that doesn't waste lots of processor power when there are a lot of objects. So, without going into too much detail for the moment &ndash; this piece of code was <em>really complicated</em>.</p>

<p>In the last couple of days, I've been trying to rewrite it in Haskell, with varied success. Some parts of it translate over really easily and are much, much more readable in Haskell than they were in C++. Other parts aren't so easy to deal with. Because writing in Haskell is so much about getting your conceptual understanding right, and the C++ version really was too complicated for me to get a good conceptual understanding, I'm having trouble rebuilding it. And it would take a huge, epic blog post just to explain how it works, much less explain the issues with rewriting it. I'm not even sure if it would have the speed it needs if I wrote it in Haskell; I was mainly doing it as an exercise, and it was a good exercise, even if I got stuck on it.</p>

<p>Well, not to worry. I've only ever written one complete program in Haskell, or in <em>any</em> functional language, and it takes a lot of practice to get into functional programming when you're only familiar with imperative programming. I was lucky to have written this website in Python, which has a bunch of functional-programming-like features, even some that it borrows directly from Haskell. That made me familiar with some of the concepts before I jumped in, but still, it's not really that easy to write an extremely sophisticated program after only a few days!</p>

<p>So, for the moment, I'm going to step back and write a cute little game in Haskell instead.</p>

''',
},
{
  "title":"""Nudity""",
  "force_id":"ccf81c1d873dede7e5944f93638240b1",
  "force_date":datetime.date(2011, 6, 17),
  "tags":["gender","sex"],
  "edited_significantly_from_old_website": True,
  "contents":'''

<p>So, I was thinking about this game I'm writing. I mostly only have vague ideas at this point, but it's going to be one of those games where you control a human and explore the world and fight various enemies. And maybe you'll find various equipment &ndash; different weapons and armor that you can switch around.</p>

<p>I'm a mathematician, so I love generalizing things. So I looked at the switching-around system and said "How much can I generalize this?" And so I immediately thought of allowing you, the player, to switch off your arms and legs and replace them with robot arms and legs, or use cool bio-technology to give yourself tentacles instead. And you can't really have a "switch one thing for another" system unless you can switch one thing for nothing. Maybe you could take off your arms and sell them in a shop? Sounds ridiculous, but I've definitely played games where you can do things like that!</p>

<p>But anyway, the real thing I want to talk about isn't taking off your arms, it's just taking off your <em>clothing</em>, which has a lot of different social implications, for some damn reason.</p>

<p>So I've got a choice. Do I allow the player to have zir character take off all zir clothes,<footnote((Assuming ze was wearing any in the first place. I think it's pretty cool to give the player complete freedom of choice by not sending them into the game with clothes already chosen for them, but that's a different issue.))> or don't I?</p>

<p>Suppose I do. Then I take a nice walk into the <cut>wonderful world of sexual exploitation! According to the stereotype, the people who will use this feature are mostly horny teenage male people who are sexually attracted to female people.<footnote((Well, that wouldn't happen if the character never looks female. But if the character is always male, that's just the same old male-as-default sexism that's been around for ages; I'm not going to do it. I suppose I could make the character always be androgynous, but recently, I've been deciding that it's a better idea to show diversity than to gloss over it.))> Most people from the real world would be creeped out by the idea of a super-powerful being from another reality staring at them when they're naked, so it would be reasonable to assume that the character doesn't like it either.<footnote((Well, not really. There's plenty of people in real life who are totally okay with other people looking at them in a sexual way, so it wouldn't be reasonable to assume that everybody isn't. But saying "Maybe the character is okay with it!" is a pedantic excuse.))> Which means that the player who does that is taking advantage of zir character; it's simulated voyeurism, and voyeurism is pretty icky.</p>

<p>Okay, that sounds bad. Suppose I don't do it. Then I enter the wonderful world of prudishness! I live in a society where nudity is a taboo; that social norm applies to most of the developed world, so statistically, since you're using the Internet, it's probably true where you are too. And it's really bad. Suppressing nudity, and suppressing depictions of nudity, makes people uncomfortable with their bodies. <em>The fact that I am writing this post in the first place</em> is because we think it's a big deal when someone isn't wearing any clothes. If people didn't think that being naked was inherently sexual, then the "sexual exploitation" thing wouldn't even be an issue. So if I design a game that could easily have the characters be naked, but <em>doesn't</em>, then I'm actively contributing to our taboos, and making the problem even worse &ndash; including the very problem that I described in the last paragraph!</p>

<p>Aaaaaaarrrrrrrgggggggghhhhhhh!!!!!</p>

<p>Okay, time to settle down a bit.</p>

<p>The two opinions I just wrote are pretty standard opinions that apply to a lot of things. Look at advertisements on TV and the Internet. A lot of them have sexually suggestive pictures of female people who aren't wearing very much clothing. It's pretty terrible, because of the way it makes female bodies into something that's for sale, which makes some people look at female people more as objects than people, and so on. So there's a strong temptation to look at it, say "This is pretty terrible; let's fix it by doing the exact opposite!", and then try to fix it by going on a crusade to eliminate all female nudity. Which is equally terrible, because when you do <em>that</em>, you're suppressing the sexuality of a lot of female people, and making them just as self-conscious about their bodies as they were when they were exposed to the mass of supposedly-perfect-looking images of their gender on TV and the Internet!<footnote((I'm being a bit careless about the exact boundaries of gender here. For instance, these things can also hurt people who are <em>not</em> female but are assumed to be female by others. I regret that I haven't found a way to describe it better. A previous version of this post tried to be more inclusive by making distinctions between people's gender, their bodies, and their gender presentation, but I have since realized that I was making the <em>wrong</em> distinctions.))> Oh, and it makes people who think they're perceived as male be totally uncomfortable about expressing <em>their</em> sexual attraction, too.</p>

<p>There's a lot of issues that have similar temptations. Here's another example: Suppose I'm writing a story with a powerful, evil, controlling character. Suppose the character is male, cis, and generally gender-comforming. That's annoying because it's the cultural default &ndash; big surprise, it's another male person in control. I'm representing male people as being in control and female people (assuming there are female characters ze's manipulating) as being weak or powerless. So, suppose I decide I'll make the evil character be female instead. Then it gets worse! Because there are <em>also</em> stereotypes about female people being evil and controlling. Instead of being an "Oh jeez a man is in charge" story, it's a "You'd better watch out &ndash; don't put a woman in charge!" story. And if I make the character be androgynous, or a robot, or whatever, then it becomes an anti-androgyne or anti-robot story.</p>

<p>That's not a unique example. That kind of thing happens basically whenever you write a story that has people with genders in it. This sounds like a job for...<footnote((<q>Sounds like a job for</q> is a cultural reference to the line "This sounds like a job for... Superman!". I said I'd avoid unnecessary cultural references, but in this case, the line has the same meaning regardless of whether you get the reference. On the other hand, most people will probably read this footnote, which wastes lots of extra time, and maybe therefore means that making the reference had a bad effect after all!))></p>

<p>DIVERSITY!</p>

<p>Yeah, you can have the same story, except put a lot of other characters in it that contradict the same stereotypes. Like I could have the evil male dominator, and also have an evil female dominator. Or I could have just the evil female dominator and have a secondary female character who has a lot of authority and uses it well. Or I could make there be a lot going on in the character's life that makes you sympathize with zem and not think of zem as a stereotype, even if you still don't like the way ze's all evil and stuff.</p>

<p>On the other hand, that doesn't solve my original problem from this post.</p>

<p>On the third hand, my original problem is easy to solve. If I write the game in a way where it fits,<footnote((Which I probably won't, because I don't have nearly enough time to write the whole game before my tablet arrives and I start doing the graphics stuff instead.))> then I'll have the nudity in it. Problem solved!</p>

<p>All we need is a slightly different perspective on the objectification issue. A game is just a way for you to imagine stuff, and it's ridiculous to say that a person can't imagine all the naked, sexually available people ze wants to, within the privacy of zir own head. A game isn't responsible for people's sexual objectification of female people, unless the game is designed in a way that especially encourages it. In fact, by having the characters in my game appear with a variety of different human body types, I could be <em>improving</em> the overall social justice of their sexual fantasies!</p>

<p>Plus, there are lots of good reasons to allow naked characters. Like, because it's totally awesome to go around kicking ass without wearing anything, regardless of your gender or sex, and games are a vehicle for imagining that you <em>are</em> the character in the game. And because it's a challenge, if the clothing in the game is actually useful for anything. In the game <i>Nethack</i>, one of the fun ways to restrict your play is the "naked" challenge &ndash; try to win the game without ever wearing any clothing or equipment.<footnote((Of course, <i>Nethack</i> doesn't have a graphical display, just text, so it avoids the issue of whether to <em>display</em> nudity.))></p>

<p>That's one difficult question answered, I guess. I like having answers to difficult questions!</p>

''',
},
{
  "title":"""Release early, release often""",
  "force_id":"5bcd8590c7d8d7cf20c146b730923b54",
  "force_date":datetime.date(2011, 6, 18),
  "tags":["programming"],
  "edited_significantly_from_old_website": True,
  "contents":"""

<p>(Note from the future: This post was about an older version of <a href="/games/green-caves">this game</a>.)</p>

<p>Yesterday, I spent all day working hard on my Haskell game &ndash; I was so busy that I didn't have time to blog about it!</p>

<p>Luckily, this has been very productive. If you can compile Haskell code, check out <a href="/media/green-caves-game-release-1.tar.gz?rr">the current version of my game</a>! </p>

<p>Right now, the game is about flying around as a green circle in an infinitely large world, and shooting out the walls. Use the arrow keys to move, and click (and hold) the mouse to shoot lasers.</p>

<img alt="A screenshot of the Haskell game: a green circle drilling a hole in green walls with green lasers" src="/media/green-caves-screenshot-1.png?rr" />

<p>So far, the trickiest part of this project was making an infinite world that would remember all the changes you made to it, without making the game get really slow as the world got bigger.</p>

<p>Amusingly, after I said I wasn't going to keep working on my collision detection stuff, most of the work of this project has been on collision detection stuff. There's a lot of things that could be improved about it (like the fact that I've duplicated a lot of work between ZOrderCollisions.hs and ZTree.hs), but there you go; I'm going to make those improvements next, anyway!</p>

<p>I've released the game under the GNU General Public License (GPL), which means that you can freely copy it, modify it, and release modified versions, as long as you make all the code you add to it available under the same license.</p>

""",
},
{
  "title":"""C++ vs. Haskell: ROUND TWO: But I want it to be fast!""",
  "force_id":"a0dd163e9656f581c3b748350509a55e",
  "force_date":datetime.date(2011, 6, 20),
  "tags":["programming"],
  "edited_significantly_from_old_website": True,
  "contents":"""

<p>(Note from the future: This post was about an older version of <a href="/games/green-caves">this game</a>.)</p>

<p>In the last two days, I've entirely rewritten <a href="/blog/release-early-release-often">my game</a> from Haskell into C++! As much as I love the expressive power of Haskell, it just isn't a suitable language for writing things that need to push the boundaries of computers' processing power. This is partially because of the way the languages are designed, and partially because a lot more work has gone into optimizing C++ compilers because it's a more popular language. On the plus side, by writing my game in Haskell first, I feel like I understand the structure of the program a lot better.</p>

<p>On my computer, this version runs smoothly at 100 frames per second, even when you have hundreds of bullets (laser bullets?) flying around in the infinite(!) world.</p>

<p>I've also added a few new features - there's now an infinite, randomly generated cave system, and the bullets last forever instead of disappearing when they leave the screen. I'd post a new screenshot, but it doesn't look much different than before... it's just that it's FIVE TIMES AS AWESOME when you play it.</p>

<p>As before, you can download <a href="/media/green-caves-game-release-2.tar.gz?rr">the C++ source code</a>.</p>""",
},
{
  "title":"""Tablet received!""",
  "force_id":"fb40cdb2da1d335e53fc3c0d0c85d1e4",
  "force_date":datetime.date(2011, 6, 20),
  "tags":["the graphics editing project"],
  "contents":'''

<p>I just received my graphics tablet! I might not be very talkative (blog-ative?) over the next few days while I figure out how to use it and do awesome stuff.</p>

''',
},
{
  "title":"""Two days later: EVERYTHING IS A PIECE OF SHIT""",
  "force_id":"56c3c3e69573f203bc519a00dc73aa16",
  "force_date":datetime.date(2011, 6, 22),
  "tags":["programming","the graphics editing project"],
  "contents":'''

<p>(This post is mostly a long rant about my computing woes. Feel free to skim over it.)</p>

<p>The linuxwacom project website says most modern Linux distributions come with Wacom tablet input drivers already enabled. Ubuntu is supposed to be included in this. So I look around on my system, and sure enough, there's already a package installed that's called xserver-xorg-input-wacom. So I plug in my tablet and try using it. Does it work? Nope!</p>

<p>So I download the linuxwacom drivers manually. I have to install a lot new stuff that they rely on. That's pretty normal. One of the things they need is the latest version of xorg-macros. I check on my system, and I have 1.3. I check my package manager, and sure enough, there's an update available, so I update to 1.5. Wait a minute... linuxwacom needs 1.8! And Ubuntu's "current version" is 1.5!</p>

<p>PIECES OF SHIT COUNTER</p><ol><li>Ubuntu</li></ol>

<p>So I download and install that, manually, which isn't very difficult, just annoying. And I finish installing linuxwacom, and then restart my computer and... YES! The tablet actually works at giving input equivalent to mouse cursor input. So I go and open up some graphics-editing programs that I know are supposed to accept tablet input &ndash; GIMP and Inkscape &ndash; and sure enough, they also accept tablet input for themselves. Nice!</p>

<p>ACTUALLY DECENT SOFTWARE COUNTER</p><ol><li>linuxwacom</li></ol>

<p>And then I spend about 15 minutes messing around in GIMP.</p>

<img alt="A stylized drawing of a person charging with a sword or something, out of a bright, open doorway." src="/media/15_minutes_of_messing_around_with_my_new_tablet_in_GIMP.png?rr" style="width:100%" />

<p>Messing around in GIMP is pretty nice. GIMP is a bit like a canvas: You can draw on it with a variety of "tools", and you have the extra advantage of being able to undo your actions, but <cut>the internal substance is just that: The pixels on the screen. Inkscape is different: Inkscape records ideal approximations of the paths you draw, and you can go back and edit those paths later. So, essentially, GIMP is for <em>drawing</em> pictures and Inkscape is for <em>designing</em> pictures. But I want to be able to draw <em>and</em> design pictures, so neither really has the feature-set that I want, and since I'm probably going to be using this medium a lot, for a long time, I want to have absolute control over my own abilities; both Inkscape and GIMP have a lot of configuration options, but they aren't nearly as versatile as they could be if I had direct control at the source level. I need to write my own programs.</p>

<p>So I look at the source code of GIMP and Inkscape, to see how they use tablet input. Their source code is incredibly complicated and confusing, and doesn't have good documentation. Both of them are built using GTK, a graphical-user-interface library. I ask the Internet about GTK tablet input, and it says that GTK has some long-standing, significant bugs relating to tablet input, which haven't been fixed for some reason. Plus, what I <em>want</em> to do (for the moment) is just add tablet input to an existing program, and using GTK for that would be like buying a giant toolbox just to use a screwdriver.</p>

<p>PIECES OF SHIT COUNTER</p><ol><li>Ubuntu</li><li>GTK</li></ol>

<p>So I go to Google and search for information about how to use tablet input in C++ programs. I use a lot of combinations of the following search terms: tablet, wacom, input, c++, programming, linux... But if you search for "tablet" you get information about tablet PCs, and if you don't search for "linux" then you only get info about how to do it on Windows, and if you <em>do</em> search for "linux" then you only get information about linuxwacom, which is just the driver. And if you search for "c" or "c++" then you get information about parts of linuxwacom that are written in C, and if you search for "input" then you get lots of pages about how to set up Wacom tablet input from the user-end perspective, which I've already done, but if you don't search for "input" then you don't get the right information! I did discover that there's, apparently, a fairly simple system for getting tablet input in Haskell, but I don't want to use Haskell for this stage of the project; I'll be saying "Go screw with this" and Haskell will say "Excuse me, I'm sure you mean 'Please show me the results of executing this list of screwing operations'". Haskell just isn't a good language for doing stupid stuff in!</p>

<p>You know what's another interesting thing about a Google search for Haskell tablet input? <em>This website is in the first page of Google results.</em> Which is... kinda flattering, but completely useless to me!</p>

<p>PIECES OF SHIT COUNTER</p><ol><li>Ubuntu</li><li>GTK</li><li>Google</li></ol>

<p>Okay, so I've been using SDL. SDL has its own event system, which gives you mouse and keyboard input and stuff; let's see if it has a way to get tablet input. So I go to Google again and ask it about SDL tablet input. Turns out, SDL has no built-in way of accepting tablet input. Yuck! On the other hand, it is supposed to have a way to ask the X Window Manager for its own events. And I know X is receiving my tablet events, because X is the entity that makes it function as a mouse. (Also I checked with the utility program "xev".) So I spend another few hours looking up what X events are and how they're stored, and I finally find some convenient example code that reads the X events directly. And so I compile that code, and IT WORKS. YES!</p>

<p>So then I go back and try to include that in my SDL code, by using SDL's "SYSWMEVENT" construct (short for system window manager event; it is supposed to cover every kind of event that SDL doesn't cover by default). I successfully enable SYSWMEVENTS... but it doesn't work at all, because SDL only reports MOUSEMOTION events for my tablet input, not any SYSWMEVENTS.</p>

<p>PIECES OF SHIT COUNTER</p><ol><li>Ubuntu</li><li>GTK</li><li>Google</li><li>SDL</li></ol>

<p>Okay, that doesn't seem like TOO much of a setback, because I already have this code that takes the input, so I can just use it <em>and</em> SDL, even if that seems kind of stupid. So I try that. It seems to work pretty well! The only problem is, the position of the cursor in the window isn't the same as the coordinates that the tablet gives. SDL mouse motion events give you coordinates based in the window &ndash; the top left corner of the window is (0, 0) &ndash; but X events give you coordinates based on the screen size, where the top left corner of the <em>screen</em> is (0, 0). That shouldn't be too hard to deal with, though, because all I have to do is subtract the window's position within the screen, and then I get the position I want.</p>

<p>It turns out that SDL has no way of knowing where its window is.</p>

<p>PIECES OF SHIT COUNTER</p><ol><li>Ubuntu</li><li>GTK</li><li>Google</li><li>SDL</li><li>SDL</li></ol>

<p>(And I can't compute it based on the difference between the SDL event coordinates and the X event coordinates, because the events don't come at exactly the same times.)</p>

<p>I guess I'm gonna ditch SDL. But first, I think I'm going to take a break. I've spent the better part of two days trying to work around the fact that I have to deal with shitty, badly documented systems, and that's pretty stressful, so I should probably take a break from it. (Be glad it didn't take you two days to read this rant!)</p>

<p>Maybe I'll work on my little game some more, or start cutting into my TODO list for this website.</p>

''',
},
]
