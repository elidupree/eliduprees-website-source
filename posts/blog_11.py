#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime



posts = [
{
  "title":"""Game theory, contracts, altruism""",
  "force_id":"4155fdd076353a7f996f160d2663fa06",
  "force_date":datetime.date(2013, 9, 28),
  "tags":["math","philosophical"],
  "contents":'''

<p>In my story <a href="/stories/capitalism-sat">Capitalism Sat</a>, "Mathematics" says a few things about game theory that I've worked on myself. I'll discuss them here. Knowing some game theory helps, but you might be able to understand without any prior background.</p>

<p>The classic paradox from game theory is the <a href="https://en.wikipedia.org/wiki/Prisoner%27s_dilemma">Prisoner's Dilemma</a>, or the more general <a href="https://en.wikipedia.org/wiki/Tragedy_of_the_commons">tragedy of the commons</a> &ndash; a situation where players can either cooperate or betray each other, and benefit from betraying, but are better off if everyone cooperates instead of everyone betraying. There are a lot of attempts to "solve" the Prisoner's Dilemma &ndash; that is, to find a reason why purely self-interested players should cooperate. <a href="https://en.wikipedia.org/wiki/Superrational">Superrationality</a> is one of them, but it only works for a limited set of situations. A more effective solution would be <cut>to allow contracts.</p>

<h2>Contracts</h2>

<p>If there is an independent contract enforcer, then the players will cooperate. Purely self-interested players can't make contracts without an independent enforcer, because they will (by the definition of their self-interest) break the contracts. But a self-interested player can enter a contract if it will benefit them, and since the enforcer will penalize them if they break it, it's in their self-interest to keep the contract. Formally, just as a <a href="https://en.wikipedia.org/wiki/Nash_equilibrium">Nash equilibrium</a> is a set of choices where no <em>individual player</em> can gain by changing their choice, I define a <strong>contract equilibrium</strong> as a set of choices where no <em>group of players</em> can all gain by collectively changing their choices.<footnote((The idea of a contract equilibrium seems like such an obvious extension of game theory that I assume plenty of people have thought of it already, so there's probably already a phrase to describe it so that I don't have to invent my own. However, I couldn't find any writing about game theory that describes it.))> With a finite collection of choices, there is always at least one contract equilibrium.</p>

<p>The contract equilibria have desirable results for the Prisoner's Dilemma, the <a href="https://en.wikipedia.org/wiki/Centipede_game_(game_theory)">centipede game</a>, the <a href="https://en.wikipedia.org/wiki/Stag_hunt">Stag hunt</a>, and a lot of other simple games. Contract equilibria have one desirable attribute: if I define <strong>strictly worse</strong> to mean "worse for every player", then they will never produce a result that's strictly worse than another possible result (because then all the players would form a contract to get the other result instead). Nash equilibria, on the other hand, can produce results that are strictly worse than contract equilibria.</p>

<p>"Strictly worse" isn't a very good way to judge, of course. What about a situation where one player benefits a little, but all other players are much worse off? To judge those situations, we need a <a href="https://en.wikipedia.org/wiki/Social_welfare_function">social welfare function</a> &ndash; in short, if you represent each person's happiness as a number, a social welfare function is a way to get a single number for the whole society<footnote((Technically, these "numbers" don't have to be numbers; they can be any <a href="https://en.wikipedia.org/wiki/Total_order">totally ordered</a> set. And perhaps it's better if they are only an ordering; I find it much easier to say "I prefer X rather than Y" than to assign a number to how much I prefer it.))>. There are lots of different proposed social welfare functions, and I don't really want to say that one of them is better than the others. Here's a few examples:</p>
<ul><li><strong>minimum</strong>: "A society is only worth as much as it gives to its most disadvantaged member"</li><li><strong>sum</strong> or <strong>average</strong><footnote((Sum and average are equivalent if the number of people is fixed. I'm not considering variable numbers of people in this post; that leads to annoying questions like "If we use the average function, does killing unhappy people improve society?" and "If we use the sum function, does spawning 1000 unhappy babies who will soon die improve society?".))>: "Any person being 1 point happier is as good as any other"</li><li>a <strong>weighted average</strong> with the worse-off having more weight (a generalized compromise between the above positions)</li></ul>

<p>Fortunately, I don't need to pick a specific function. I can prove counterintituive results with <em>any</em> social welfare function that obeys a few simple conditions:</p>
<ul><li><strong>Impartiality</strong>: An arbitrary reordering of the people must produce the same result.</li><li><strong>Weak <a href="https://en.wikipedia.org/wiki/Pareto_efficiency">Pareto optimality</a></strong>: If every individual person is better off, society is better off.</li></ul>

<p>There are a lot of other reasonable conditions you could add, but as it turns out, this is all I need. Now I can demonstrate a game where the contract equilbrium is worse than the Nash equilibrium.</p>

<p><strong>The Two Exploiters scenario</strong>: There are five players. The first two are in a Prisoner's Dilemma situation; if they both cooperate, they both score 3, if they both betray, they both score 2, and if only one betrays, that player score 4 and the other scores 1. The rest of the players have no choices and they score equal to their player number. But the first two players' option is actually to cooperate in exploiting the rest, so if the first two cooperate, the rest score their player number minus three instead. In the Nash equilibrium, they betray each other, and the scores are as follows:</p>
<ol><li>2</li><li>2</li><li>3</li><li>4</li><li>5</li></ol>
<p>In the contract equilibrium, they cooperate, and the scores are:</p>
<ol><li>3</li><li>3</li><li>0</li><li>1</li><li>2</li></ol>
<p>By Impartiality, I can swap the conspirators to the end and get the same social welfare:</p>
<ol><li>0</li><li>1</li><li>2</li><li>3</li><li>3</li></ol>
<p>Each entry is lower than the corresponding one in the Nash equilbrium, so by weak Pareto optimality, the social welfare of the contract equilibrium is lower.</p>

<h2>The non-aggression principle</h2>

<p>Cooperating to exploit everyone doesn't sound nice. We can solve that with the other concept I mentioned in <i>Capitalism Sat</i>: the <a href="https://en.wikipedia.org/wiki/Non-aggression_principle">"non-aggression principle"</a>, which says that regardless of your self-interest or contracts, you must not take certain actions &ndash; specifically, you must not initiate violence against others. If we ban the first two players from conspiring, everything is better again. Of course, it's not clear how these numbers correspond to real life; maybe players 1 and 2 work together to violently extort from everybody, which is clearly aggression, but maybe they're rival business owners conspiring to raise prices (which is illegal in at least the United States, but is hard to describe as initiating violence). Once again, I don't have to decide, because I can prove that <strong>no possible</strong> non-aggression principle leads to desirable results in all cases. The key weakness is that the principle is required to ban the same actions for every player; if two players have the same set of choices, it can't regulate their behavior differently.</p>

<p>I'll start with one that shows it without contracts (which is simpler). This scenario is a cross between the <a href="https://en.wikipedia.org/wiki/Tragedy_of_the_commons">tragedy of the commons</a> and the <a href="https://en.wikipedia.org/wiki/Volunteer%27s_dilemma">Volunteer's dilemma</a>, so I'll call it <strong>the Tragedy of the Volunteers scenario</strong>. There are 102 players, and each player chooses whether to "participate" or "ignore", and scores as follows: +1 if ze participated, +100 if any player participated, -1 for each other player who participated. (Imagine it's a task that benefits everyone and is fun to do, but gets messed up if too many people try to help at the same time.) Since each player benefits from participating, the Nash equilibrium has them all participating, scoring a total of zero. Adding a non-aggression principle cannot do anything except ban one of the options for all players... and forcing them all to chose "ignore" <em>also results in a score of zero for all players</em>. The best result is for exactly one player to participate and score 101 while everyone else scores 99. Contracts almost achieve this; they might end up with two people participating for two 100s and a hundred 98s, which I'd generally say is worse, but isn't necessarily worse by just Impartiality and weak Pareto optimality.</p>

<p>Now I'll break it with contracts, too. Just like in the Two Exploiters scenario, I have to make two different categories of players.<footnote((Proof sketch: If the players are identical, then Impartiality is irrelevant, and weak Pareto optimality is just the "strictly worse" condition.))> This one is based on a task that requires a skill and is good for all, but messes up if more than one person tries to do it at the same time.<footnote((There are lots of examples of such tasks in real life. For instance, organizing and leading a group of workers: lots of people like leading, and one person taking charge can make the work more organized, but it's less efficient if two people try to do it at the same time.))> There are 2 skilled players, who choose "participate" or "ignore" as above, and 2 unskilled players, who choose nothing<footnote((Alternatively, all the players have the same skills, but the first two enjoy doing the task and the second two don't enjoy it.))>. All players benefit on the basis of the work: if one skilled player participates but the other doesn't, everyone gets +3. The skilled players also enjoy participating and get +4 for participating; the unskilled players also have a base score of 2.</p>

<p>With <em>or</em> without contracts, the skilled players act in their own (individual or collective) self-interest by all participating, resulting in a payoff of 4 for themselves and nothing extra for everyone else, which gives the distribution [4,4,2,2]. This compares unfavorably to the distribution when exactly one participates: [7,3,5,5] (reordered, [7,5,5,3]). And the non-aggression principle can't change the Nash equilibrium except by banning participation, leading to the even worse [2,2,0,0].</p>

<p>None of these clever extra rules can avoid the basic fact that, if we are willing to harm others for our own self-interest, we will probably end up doing so. Instead, we should act for the benefit of both ourselves and others. We should learn to think in cooperative ways, rather than competitive ways, and teach others to do so as well. By giving up just one point, one of the skilled players earns three points for everyone else. There is a world where almost anyone would do that, and I believe we can reach that world.</p>

<h2>Rational altruism</h2>

<p>But wait!</p>

<p>I would be doing my own craft a disservice if I didn't turn its glare upon the idea of altruism as well. I define a <b>rational altruist</b> as a person who acts to maximize a specific social welfare function, just as the players in a Nash equilibrium act to maximize their own score. I will show that every counterintuitive behavior of game theory also occurs between rational altruists who use different social welfare functions!</p>

<p>A simple example, with two players. Player A uses the <strong>minimum</strong> function. Player B uses the <strong>average</strong> function. They can either do nothing, or take one of two actions: Action A improves the worst-off member by 1 point, but harms everyone else by 2 points. Action B harms the worst-off member by 2 points, but improves everyone else by 1 point. Player A takes action A to improve the minimum function by 1, and player B takes action B to improve the average function by (almost) 1. As a result, literally everyone in the society is worse off by one point, despite the fact that the actions were taken by purely rational altruists!</p>

<p>There's a few ways to convert an arbitrary game-theoretic game to a game between rational altruists. (The above example is a conversion of the Prisoner's Dilemma.) Unfortunately, the best ways to do it require a lot more math, so I won't show them here, and the simple ways use social welfare functions that aren't very realistic. The simplest way that I know is this: The altruist players use the functions "minimum", then "as good as the second-worst-off person", then "as good as the third-worst-off person", and so forth. We'll make the players of the original game correspond to those positions in the ordering: Their score after the altruists' decisions is the score from the original game, plus a large constant factor so that their scores don't change the ordering. (e.g. the first one is score+0, the second is score+1000, the third score+2000, and so forth, if no two scores possible in the original game differed by as much as 1000.)</p>

<p>And as if all the problems from game theory weren't bad enough, enforcing contracts between altruists is harder too. How many people would agree to intentionally harm society as a whole in order to penalize someone for breaking a contract?</p>

<h2>Oh crap, what do we do?</h2>

<p>I really have no idea!</p>

<p>But don't despair yet. There's some good news. First, although the ethics of "benefit yourself by harming others" are very <em>interesting</em> to talk about, I like to think of those situations as the rare ones. Most of our interactions rely on shared physical and social infrastructure, so an action that harms another person also harms yourself, and an action that helps another person also helps yourself. Obviously, stealing physical objects from total strangers is an exception, but if you steal from a friend, the theft will stress them out (or worse) and that stress will harm everyone in their social circle &ndash; and if you steal from someone in the same geographical area, it's likely that they were a friend of a friend. Abusers divide and damage their own communities, even if they don't understand how. Selfish motivations are aligned with each other more often than not.</p>

<p>Second, altruistic motivations are aligned even <em>more</em> often. Helping out the most disadvantaged members of society doesn't hurt the rest of society, it helps the rest of society. People who can't get medical treatment are more likely to spread diseases that can affect anyone. People are more productive if they have a social safety net than if they constantly have to worry about their physical safety, or where to get their next meal. And people who find that there's a community ready to help them, are more likely to want to help give back to that community once they have the ability to do so.</p>

<p>It is possible to make this world into a good world. It's just a matter of whether we will succeed.</p>

''',
},

{
"title": "I'm back, and with new treasures!",
"tags": ["this website", "announcements"],
"auto_paragraphs": True,
"contents":'''
The story of the last three years isn't very interesting. My hand problems got better, but then they came back again. Then they got better again, then they came back again, and so on. They're still not entirely recovered, and I'm still trying to see different doctors to figure out what the real issue is. It's no fun.

<p><em>However!</em></p>

Since last June, I have had working speech-recognition software. I can now do most of my work by voice, even computer programming. I've been making a bunch of interesting things this way, I just haven't shared them on this website yet.

That's because this website was hard for me to use.

<p><em>However!</em></p>

I started redesigning this website in 2013, and now it's finally, <em>finally</em> finished. All of the old posts are still here, but I rebuilt everything else from scratch. There are so many improvements that I can't possibly list them all. Here are some of the big <cut>ones:

<h2>Big design changes!</h2>
<ul class="big_list">
<li>The whole website is easier to navigate. The old design had a mess of different index pages that were hard to find. Now, the links in the top bar will let you find everything on the website efficiently. The comics have better archive pages as well.</li>

<li>The new design is usable on small screens, like cell phones.</li>

<li class="hidden_from_restricted_users">You can now get email updates directly, without creating a username/password. (Just look in the right sidebar, or further down the page if you're on a mobile device.) You can also post comments without logging in. In fact, I have destroyed the user accounts entirely. Making you log in was overkill for a website like this one.</li>

<li class="hidden_from_restricted_users"> <a href="https://www.patreon.com/EliDupree"> I now have a Patreon page!</a> If you have spare $$$, you can pledge a certain amount for each major new work I create. That'll encourage me to post more awesome stuff! (On Patreon, you can choose your own pledge amount, set a monthly maximum, and cancel your pledge whenever you want. So it's completely up to you how much you're willing to part with. You can see more details <a href="https://www.patreon.com/EliDupree">on the actual page</a>.)</li>
</ul>

<p class="hidden_from_restricted_users"> A few things were lost in the transition. The old website had more precise control of email notifications. Unfortunately, I had to replace the email system, because it was bad and it tended to end up in people's spam folders. The new system just notifies you of each thing I post, but not user comments. Currently, if you want to keep track of new comments, you have to visit <a href="/">the main page</a> or <a href="/blog">the blog page</a>.</p>

<h2>New and improved content!</h2>
<ul class="big_list">


<li>I have edited a lot of the old posts! Because I <a href="/blog/this-is-a-child-friendly-website">don't want to exclude anybody</a>, I used a formula to estimate the reading difficulty of each post. Then I edited some of the ones that were too difficult. I especially focused on the neurodiversity post, because it's very important and I want it to be readable.</li>

<li>I edited most of the annotations of Voldemort's Children! Especially the early ones. Later in the comic, as I got more experienced, I developed a consistent style for the annotations. The earlier ones were more random. So I changed them to use the new, better style, and I added a bunch of new interesting notes as well. I also fixed a few typos in the comic itself, and changed the colors of some things that were the wrong color. I still won't be able to finish <em>drawing</em> the comic for a while yet, because of my hand problems.</li>
<li>I finally wrote a transcript for People Are Wrong Sometimes, and added some author's notes at the end as well.</li>


<li>I've made a new <a href="/about-eli">about me page</a>.</li>

<li>The <a href="/games/green-caves">green caves game</a> now has time travel in it!</li>
</ul>
<h2>The future is looking awesome!</h2>

In the past, I haven't had a very good record of sticking to consistent updates. However, I've been consistently working on this redesign almost every day of the last month. That's a pretty good sign. And the new design is much easier for <em>me</em> to use, as well. There's a bunch of things that I haven't posted here because I couldn't think of a good way to bake them into my website. Now, the good way is almost automatic.

Also, I have plans! I have planned out more than a dozen new blog posts. I also have more than a dozen old stories and other things that I haven't posted here yet, and I plan to edit those things and post them as well.

Here's my plan for a schedule: I'll be posting about two new things each week. I'll definitely post one thing on each <strong>Wednesday</strong>, like clockwork. Between each Wednesday and the next, I'll post zero-to-two additional things, whenever I feel like it. I will also try to loosely alternate between blog posts and other works.

<p>(UPDATE: A couple of days after I wrote this post, a nearby lightning strike caused a power surge that damaged my main computer. I'm still going to try to keep the same schedule, but I might choose slightly less ambitious projects than I was planning to.)</p>

Get ready for an Eli Dupree-filled future!

''',
},

{
"title": "Story idea: The legendary monster hunter",
"tags": ["story ideas"],
"auto_paragraphs": True,
"contents":'''
A legendary monster hunter arrives from another world.

In zir own world, people are generally good to each other, but they can be transformed into monsters by curses. Some monsters are huge and grotesque, but others look a lot like humans. When people turn into monsters, monster hunters have to stop them &ndash; sometimes by killing the monsters, but usually by ending the curses that caused the problem in the first place.

When the legendary monster hunter appears in our world, ze is shocked by how often people hurt each other here. But ze quickly comes to a conclusion: our soldiers, our tyrants, our child abusers, are not human. Instead, they are human-like monsters who have been transformed by curses. So ze starts doing the work of stopping them &ndash; sometimes by killing the monsters, but usually by ending the curses that caused the problem in the first place.

<h2> Explanation</h2>

This is basically a fantastical version of my <cut>real-life beliefs about justice. Sometimes, fighting and punishment are necessary. But usually, we should focus on fixing the <strong>causes</strong> of abuse.

This story could also have a pretty funny side. It would have a high-fantasy character showing up in the modern world.

<blockquote>
"You see, sometimes, when a person grows up in an abusive household, they can end up repeating those behaviors towards their own children &ndash;"
Finally, something was starting to make sense. "Oh! So they're like vampires!"

"Er &ndash; not exactly &ndash;"
</blockquote> 

I'm imagining zem wearing a lot of leather belts, to carry lots of magic potions and powders that ze uses for monster hunting. Ze'd also have a very friendly and sincere personality. Ze'd be very sincere when real-life people would normally just be polite. That would not only be funny, but also set a good example.

I like this story idea a lot. I don't feel inspired to write it, though. Usually, when I have an idea I like, I leave it in the back of my mind for a while, to see if I come up with ways to develop it further. But I had this idea long time ago, and I haven't really come up with anything.

Maybe one of <strong>you</strong> could write it, though! If you do, I'll even put a link to it here. Any volunteers?



''',
},

{
"title": "My 0-10 pain scale",
"tags": ["neurodiversity"],
"auto_paragraphs": True,
"blurb":'''When someone asks me, "rate your pain on a scale from 0 to 10", I now have a good way to do it.''',
"contents":'''


If a person goes to a doctor because something hurts, the doctor sometimes asks, "rate your pain on a scale from 0 to 10" (or 1 to 10). This can be frustrating if you don't know what number to give it. If your pain is moderately intense, how do you know whether it's a four or a six?

I thought about this for a while. Eventually, I realized that I wanted to make a pain scale that I could use for myself. Since I <a href="/blog/imagining-pain">have trouble remembering pain sensations</a>, it's hard for me to know whether a pain that I feel today is stronger or weaker than a pain I felt last week. A scale could help with that.

I came up with a <strong>reference point</strong> for each number on the scale. These reference points are based on how my brain works, so they might not work for everybody. They are useful to me. Your own pain scale might put them in a different order, or use different reference points altogether.
<strong>0.</strong> There is no pain, and no uncomfortable sensation at all.

<strong>0.5.</strong> There is no pain, but there is some sensation that makes me worry anyway. Maybe a muscle feels stiff or overworked, so that I expect it might start hurting if I used it more.
<strong>1.</strong> There is some pain, but not enough to be unpleasant. It's just a curiosity. If I had a magic switch that could turn the pain on and off, I usually wouldn't even bother to turn it off. (I might still worry, because the pain could get worse if I do the wrong thing, but the pain itself is not a problem.)

<strong>2.</strong> The pain is enough that I would usually choose to turn it off, but not enough to be distracting.

<strong>3.</strong> The pain is distracting. If it goes on for a long time, I eventually <cut>have trouble concentrating on my work. I can still keep working if I want to, though. (When I say "work", I mean mental work, like writing stories or computer programming. If I'm only doing a boring physical task, I can handle much more pain.)

<strong>4.</strong> The pain becomes distracting very quickly. It's very hard to work for more than a few minutes.

<strong>5.</strong> The pain basically stops me from working at all. I can still do complex thinking if I know it's urgent, but I'm too focused on dealing with the pain, so I don't want to do anything else.

<strong>6.</strong> I start using <strong>coping behaviors</strong>.

Let me explain this a bit more. At six and above, I want to moan, scream, clench my muscles, pound on a wall, or other stuff like that. These are "coping behaviors". When I use them, it actually feels like the pain is less bad.

Below six, I might say "Ow!", or moan, or complain, but those just express my surprise or frustration. They don't actually change how painful it feels. Below six, it's easy for me to stay still and remain silent if I want to.

At six, it's not hard to suppress the coping behaviors. I just don't want to.

<strong>7.</strong> My desire to use coping behaviors becomes overwhelming. If I want to suppress them, I can do it, but it takes most of my effort and concentration. At seven, I usually end up collapsed on the floor. I can get up if I need to, but it's hard.

I haven't decided on anything for 8, 9, and 10. That's because a seven is the worst pain I've felt in my life. I left three numbers unused at the top of the scale on purpose. That way, if I ever feel more pain than I have before, I'll be able to add it to my scale.

<h2>Pain vs. distress</h2>

Pain and distress aren't the same thing. This scale measures how <em>intense</em> the feeling is, but not how much I <em>dislike</em> feeling it. When I talk about "distress", I'm talking about a separate feeling of unpleasantness. Pain often causes distress, but not always.

There are a lot of reasons someone might cause pain to themself on purpose. They might do it for the endorphin rush. They might get sexual pleasure from it. They might do it to distract themself from worse feelings. At various points in my life, I have done all of these things.

Generally, pain causes distress for me if it's at least a 6 (for sudden pain) or a 3 (for ongoing pain). In terms of distress, an ongoing pain is about equivalent to a sudden pain about 3 points higher. A pain I caused myself on purpose is equivalent to an unwanted pain about 2 points <em>lower</em>.

I used to think, "I don't always want to avoid pain, but I always want to avoid distress." But one day, I was on a car ride through a city, inhaling a bunch of car exhaust. It made me feel a bunch of nausea and distress. I used a mental technique to make the distress go away, but that made the nausea worse. So I <em>brought back the distress on purpose</em> to help suppress the nausea. As it turns out, even "bad" feelings can have worthwhile uses. I still generally say "pain isn't a bad feeling, distress is", but that doesn't mean distress is completely bad all the time.

<h2>Using the scale in practice</h2>

I invented this scale a little more than a year ago. Since then, I've been using it quite a bit. I can quickly and easily tell where my pain fits on the scale, within at least one point. For instance, I might say "this is a 3 or 4, I'm not sure".

This has been very helpful for keeping track when I have a pain that comes and goes over a day or two. Also, when I have significant health problems, I write down the pain value in my daily notes. That way, I can refer to it if the problem happens again.

I can also use the same scale to measure some other feelings, like nausea and anxiety.

It's hard to pin down exactly how <em>useful</em> this has been. There's nothing I can point to and say, "See, knowing more about my pain has given me this material benefit". But it definitely feels good to know that I understand myself a little better.

''',
},
]

"""

#A template for new posts, which I copy each time I start one.
{
"title": "
"tags": [],
"auto_paragraphs": True,
"don't deploy": True,
"contents":'''

''',
},

"""
