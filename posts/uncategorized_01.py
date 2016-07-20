#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime



posts = [
{
  "title":"Policies",
  "disallow_comments": True,
  "contents":'''<ul class="big_list">
    
<li>If you comment on a post, <strong>no one else will see it until I approve it</strong>. I make no promises, but I will probably approve anything that's not spam or harassment (or illegal). I may even approve bigoted comments in order to respond to them. It's OK to be misinformed about social issues here, and I hope that this site will educate people. I typically check incoming comments at least once a day.</li>
    
<li>I am serious about web accessibility. If part of my website is incompatible with an assistive technology, <strong>contact me and I'll try to fix it</strong>. If you see a way I could be more accommodating to people with a certain disability or trait, contact me and I'll try to improve it.</li>

<li class="hidden_from_restricted_users">I think your privacy is important, so if you sign up for email notifications, I promise I won't sell your email address to advertisers or anything. Currently, I use <a href=" http://mailchimp.com/">MailChimp</a> to send you emails, so your email address can be used as described in <a href=" http://mailchimp.com/legal/privacy/">MailChimp's privacy policy</a>. </li>

<li><a href="/blog/this-is-a-child-friendly-website"> This is a "child-friendly website", but that doesn't mean what you think it means.</a></li>

<li>Certain words are <strong>scrutinized words</strong> on this website &ndash; particularly <a href="/blog/scrutinized-words-she-he">gendered pronouns</a> and <a href="/blog/scrutinized-words-man-woman-boy-girl">other gendered terms</a>. You're allowed to use them, but they will be marked wherever they appear.</li>
</ul>''',
},
{
  "title":"About Eli",
  "disallow_comments": True,
  "contents":'''
    
<h2>What's important to me</h2>

<p>I am compelled to invent stories, and sometimes I write them as <a href="/stories">prose</a> or <a href="/comics">comics</a>. I enjoy figuring out how things work, then messing with them. I produce a lot of imagination, music, and philosophical thoughts. I like to design and play <a href="/games">games</a>. I use computers for most of the things I do.</p>
    
<p>The world can be a pretty awful place. My main <strong>objective</strong> is to make the world a good place. If the world becomes a good place, I win. If it stays awful until the end of all sentient life, I lose.</p>

<p>I'm somewhere on the autism spectrum, and my brain has a bunch of uncommon traits besides that. It's mostly awesome. I have a lot of mental abilities that most people don't.</p>
    
<h2>Other details</h2>

<p>A few of my mental traits can be disabling (e.g. oversensitivity to noise and other sensations), so I do consider myself a "person with a disability", but I don't think of my autism as a disability overall.</p>

<p>I'm agender. I've never felt female or male, not even a little bit. I prefer for people to refer to me by <a href="/blog/scrutinized-words-she-he">gender-neutral pronouns</a> and <a href="/blog/scrutinized-words-man-woman-boy-girl">other terms</a>. People often assume I'm male, which annoys me, but it doesn't annoy me much more than any other time that people are wrong about something.</p>

<p>I grew up on the Internet. Physically, I grew up in a suburban town in the US Northeast. I was raised by parents who nurtured most of my interests. I went to high-quality public schools, where many of the adults (and some children) mistreated me for my autistic traits and gender expression.</p>

<p>I have a hand injury that limits how much I can type. I do most of my work using speech recognition software if I can.</p>

<p>I'm not religious. I'm middle-class. I'm white. I have no romantic or sexual attraction to people of any gender, but I do have sexual desires.</p>''',
},
{
  "title":"Some thoughts about Undyne, the character from the game Undertale",
  "contents":'''<p>(Spoilers ahoy.)</p>
<p>I was inspired to write this because I saw one of those "D&D alignment charts" that had Undyne as the representative for Chaotic Good. If you Google "Undertale alignment", you can also find zem listed as Lawful Good or Lawful Neutral.</p>
<p>Undyne is super confident, brave, loyal, and honest. Ze despises weakness and mercy. Ze feels a sense of duty to zir weaker allies, but also physically hurts them whenever ze feels like it<footnote((Throwing a spear at you while trying to befriend you; roughhousing with Papyrus in some of the phone conversations, with no indication that Papyrus is okay with it; punting Alphys into a trashcan in the dating sequence. In Pacifist, even the way ze drags off Monster Kid probably counts (although if you've killed anyone, it's justified to protect Monster Kid from you).))>. Ze hates humans, but refuses to let a monster child come to harm. In one route, ze heroically sacrifices zemself trying to stop the most horrible person ever. Ze's on a mission to kill 7 kids on the orders of zir rightful monarch so that the monarch can gain power (supposedly for the greater good).</p>
<p>All of this is 100% by-the-book Lawful Evil<footnote((Mind you, I don't think it's generally a good idea to label people as Evil in real life, but ze fits <a href="http://www.d20srd.org/srd/description.htm">the D&D definition of Lawful Evil</a> perfectly.))>. In fact, ze's a very specific brand of evil: a leader who everyone admires so much that they don't consider how much ze might be hurting people. The game even points this out through the dialogue of Monster Kid and Papyrus. Ze's a brilliant example of the logic of abuse.</p>
<p>And yet, even though I've had these thoughts about zem, my FEELINGS about Undyne still say, "Undyne is so cool!" There are some important lessons here: Really cool people can still do evil things, heroic people can still do evil things, and it is better to befriend a person who does evil things (if you have the chance to) than to kill them. But, given how people drew the alignment charts, I guess most people sidestep these lessons by simply concluding that ze is Good (or at least Neutral) and ignoring how many of zir actions and motivations are evil. Undertale tried to fight against the idea, "they're the bad guys, so we should kill them" &ndash; but maybe it didn't fully beat that idea, if people still see the Undertale monsters and think "we befriended them instead of killing them, so I guess they must not be bad guys."</p>''',
},
{
  "title":"The Morality of Legend of Korra",
  "contents":'''<p>I wrote this just after I finished watching Legend of Korra. I wanted to like this show, because it does a bunch of cool things, especially having multiple nuanced, badass female protagonists. So it was extra frustrating when it kept including some of the same old shit.</p>
<ul>
<li>A man being horrible to women is an amusing quirk. Don't worry about it! Even the women he mistreats will probably be happy to get with him after he does one or two nice things. And if your young son keeps saying extremely sexist things, there's no reason to talk him out of it.</li>
<li>If your friend tells you that his girlfriend threatened to kill him, don't worry about it. He just needs to assert himself more!.</li>
<li>No good guy would ever torture someone on-screen. Torturing someone for 13 years is just fine if you do it off-screen, though. Plus, threatening to torture or kill someone is fine even if you're on-screen. No good guy would question it..</li>
<li>On the other hand, killing people is completely abhorrent. If a dictator is enslaving your people, only an evil mastermind would even consider assassinating them. A good guy would always try to save their life instead. It's okay if you kill someone in a fight, though, as long as they're not very important..</li>
<li>Incidentally, if you DO assassinate a hated dictator, ordinary people will immediately set fires and burn down their own city. Then a worse dictator will take charge. The main way democracy happens is if a monarch decides to allow it. Even a social movement for equality can't exist unless it has a single charismatic leader..</li>
<li>One good thing that I didn't expect: if a teacher forces a student into a form of training that the student hates, and the student defies the teacher, the teacher is the one who is making a mistake..</li>
</ul>
<p>I'm going to hold off on complaining about any of the inconsistencies with the plot or physics, because the moral stuff is more important. And this show is supposedly progressive/"subversive". Compared to other TV shows, it might be? It's really terrible that we have set such a low bar.</p>''',
},
{
  "title":"Harry Potter and the Methods of Rationality: Commentary",
  "auto_paragraphs": True,
  "contents":'''<p>(Spoilers ahoy.)</p>
<h2>Notes on Chapter 30</h2>

"Girls can win by tricking boys who don't take girls seriously" is not a feminist message.

<h2>Notes on Chapter 33</h2>

Given that Quirrell had specifically avoided having a points system so that Harry couldn't exploit it, I was rather disappointed when Harry didn't think of the best way to exploit the points system they use here.

If Dragon and Chaos really want to shut Sunshine out of the game, they shouldn't go towards Sunshine at all. Instead, they should charge full-speed at <em>each other</em>, and fight very aggressively. After the fight, the winning team will be ahead of Sunshine by at least 23 points. And since Dragon and Chaos are close to evenly matched, the winning team will probably lose most of its members as well. That way, Sunshine will never be able to get back in the game, because there simply won't be enough opponents to shoot in order to gain points.

<p>(I'm ignoring traitors here, but if Sunshine has enough traitors to accumulate nearly 23 points on top of their initial lead, it's practically impossible for them to lose anyway.)</p>

I don't think they would actually <em>use</em> this strategy &ndash; Draco would be too proud to agree to it, even if it does technically win. But Harry should have at least <em>thought</em> of the idea.

<h2>A theory about the ending</h2>

Even before seeing how the end played out, it seemed ridiculous that Voldemort would leave Harry holding zir wand when ze took away all Harry's other stuff and instructed the Death Eaters to restrict zir moves so carefully. Why would Voldemort leave zem the wand? As ze says, "To fathom a plot, look at the consequences and ask if they might be intended." Perhaps Voldemort, or someone controlling zem, intended that Harry use the wand to defeat Voldemort and the Death Eaters.

Tom Riddle #1 is worried about a prophecy that says Harry Potter-Evans-Verres has the power to vanquish a Dark Lord. A person seeking eternal life would prefer to avoid staking their existence on winning a prophecied 1-vs-1. So ze tries to subvert it at "every point of intervention" - by making sure the prophesied Dark Lord is not zemself, but someone else.

The very first thing ze does is to abandon Quirrel's body and possess another hapless victim. Ze then subdues the original Quirrel and ze imprints zemself upon Quirrel, creating Tom Riddle #3. One Quirinus-Quirrel-possessed-by-Tom-Riddle enters; one Quirinus-Quirrel-possessed-by-Tom-Riddle leaves.

Using a minion (Sprout, perhaps), #1 forces #3 to make an Unbreakable Vow. The vow stipulates:
<p>#3 will fully take on the role of Lord Voldemort. #3 will resurrect Hermione and coerce Harry into making the Vow about the world's destruction. #3 will also find an excuse to waste an entire hour on something, so that no one suspects Polyjuice Potion. After that, #3 must ensure being vanquished by Harry. Ze will not kill Harry under any circumstances, and ze will reveal zemself to Harry as the Dark Lord. If Harry fails to vanquish zem, ze must continue giving Harry more resources (the wand) and motivation (torture threats) until Harry does it. Lastly, #3 will obey the commands of anyone who gives the code phrase Recommend-Performance-Humble-Horizon-251, in case the plan fails, Harry gets killed, and #1 has to stop #3 from Dark Lording all over the place.</p>

<p>#1's minion erases #3's memory of making the Vow, and instead gives #3 false memories that ze is actually #1 and has just taken most of Hogwarts hostage. (No need to risk detection by actually doing it. All ze needs is the ability to claim it's true in Parseltongue, which only requires zem to believe it.)</p>

Then #1 Obliviates all minions involved (except the one involved in the fake hostage scheme), releases #3 to do zir work, and retires to a quiet home in the country until this all blows over. Ze decides to abandon the role of Lord Voldemort and never act too much like a Dark Lord again until Harry is perma-dead. Thus, ze maximizes zir chances that the prophecy and Dumbledore's conditions think of #3 as the only relevant Dark Lord Voldemort.

Most everything else happens as the story says. #3, not knowing ze's being controlled by an Unbreakable Vow, rationalizes zir decisions, and is able to report that false motivation in Parseltongue because ze believes it.

I find this theory <em>more believable</em> than the story where #1 willingly exposes zemself to a prophecied opponent who is holding a wand, knows #1's true identity, and even has an hour left on zir Time-Turner. The biggest weakness of the theory is that the imprinting might not work as smoothly as I describe. Still, #1 had plenty of time to experiment and perfect the plan before executing it, since there was nothing crucial about the exact moment ze pulled it off.

That's about the size of it.

One last thing: In the "do not mess with time" incident, Harry didn't really get intimidated by the force of Time itself. It was just a false memory implanted by Dumbledore in accordance with the prophecies, to make sure Harry didn't learn too much about time travel too soon.''',
},
]

