#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime



posts = [
{
  "title":"Policies",
  "disallow_comments": True,
  "contents":'''<ul class="big_list">
    
<li>If you comment on a post, <strong>no one else will see it until I approve it</strong>. I make no promises, but I will probably approve anything that's not spam or harassment (or illegal). I may even approve bigoted comments in order to respond to them. It's OK to be misinformed about social issues here, and I hope that this site will educate people. I check incoming comments at least once a day.</li>
    
<li>I am serious about web accessibility. If part of my website is incompatible with an assistive technology, <strong>contact me and I'll try to fix it</strong>. If you see a way I could be more accommodating to people with a certain disability or trait, contact me and I'll try to improve it.</li>

<li>If you sign up for email notifications, I use <a href=" http://mailchimp.com/">MailChimp</a> to send you emails, so your email address can be used as described in <a href=" http://mailchimp.com/legal/privacy/">MailChimp's privacy policy</a>. Other than that, I think your privacy is important, so I won't frivolously share your email address with anyone else. </li>

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

<p>I'm agender. I've never felt female or male, not even a little bit. I prefer for people to refer to me by gender-neutral terms and <a href="/blog/scrutinized-words-she-he">pronouns</a>. People often assume I'm male, which annoys me, but it doesn't annoy me much more than any other time that people are wrong about something.</p>

<p>I grew up on the Internet. Physically, I grew up in a suburban town in the US Northeast. I was raised by parents who nurtured most of my interests. I went to high-quality public schools, where many of the adults (and some children) mistreated me for my autistic traits and gender expression.</p>

<p>I have a hand injury that limits how much I can type. I do most of my work using speech recognition software if I can.</p>

<p>I'm not religious. I'm middle-class. I'm white. I have no romantic or sexual attraction to people of any gender, but I do have sexual desires.</p>''',
},
{
  "title":"Some thoughts about Undyne, the character from the game Undertale",
  "contents":'''<p>(Spoilers ahoy.)</p>
<p>I was inspired to write this because I saw one of those "D&D alignment charts" that had Undyne as the representative for Chaotic Good. If you Google "Undertale alignment", you can also find her listed as Lawful Good or Lawful Neutral.</p>
<p>Undyne is super confident, brave, loyal, and honest. She despises weakness and mercy. She feels a sense of duty to her weaker allies, but also physically hurts them whenever she feels like it<footnote((Throwing a spear at you while trying to befriend you; roughhousing with Papyrus in some of the phone conversations, with no indication that Papyrus is okay with it; punting Alphys into a trashcan in the dating sequence. In Pacifist, even the way she drags off Monster Kid probably counts (although if you've killed anyone, it's justified to protect Monster Kid from you).))>. She hates humans, but refuses to let a monster child come to harm. In one route, she heroically sacrifices herself trying to stop the most horrible person ever. She's on a mission to kill 7 kids on the orders of her rightful monarch so that he can gain power (supposedly for the greater good).</p>
<p>All of this is 100% by-the-book Lawful Evil<footnote((Mind you, I don't think it's generally a good idea to label people as Evil in real life, but she fits <a href="http://www.d20srd.org/srd/description.htm">the D&D definition of Lawful Evil</a> perfectly.))>. In fact, she's a very specific brand of evil: a leader who everyone admires so much that they don't consider how much she might be hurting people. The game even points this out through the dialogue of Monster Kid and Papyrus. She's a brilliant example of the logic of abuse.</p>
<p>And yet, even though I've had these thoughts about her, my FEELINGS about Undyne still say, "Undyne is so cool!" There are some important lessons here: Really cool people can still do evil things, heroic people can still do evil things, and it is better to befriend a person who does evil things (if you have the chance to) than to kill them. But, given how people drew the alignment charts, I guess most people sidestep these lessons by simply concluding that she is Good (or at least Neutral) and ignoring how many of her actions and motivations are evil. Undertale tried to fight against the idea, "they're the bad guys, so we should kill them" &ndash; but maybe it didn't fully beat that idea, if people still see the Undertale monsters and think "we befriended them instead of killing them, so I guess they must not be bad guys."</p>''',
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
  "title":"Harry Potter and the Methods of Rationality",
  "auto_paragraphs": True,
  "contents":'''(Spoilers ahoy.)

Even before seeing how the end played out, it seemed ridiculous that Voldemort would leave Harry holding his wand when he took away all Harry's other stuff and instructed the Death Eaters to restrict his moves so carefully. Why would Voldemort leave him the wand? As he says, "To fathom a plot, look at the consequences and ask if they might be intended." Perhaps Voldemort, or someone controlling him, intended that Harry use the wand to defeat Voldemort and the Death Eaters.

Tom Riddle #1 is worried about a prophecy that says Harry Potter-Evans-Verres has the power to vanquish a Dark Lord. A person seeking eternal life would prefer to avoid staking their existence on winning a prophecied 1-vs-1. So he tries to subvert it at "every point of intervention" - by making sure the prophesied Dark Lord is not him.

The very first thing he does is to abandon Quirrel's body and possess another hapless victim. He then subdues the original Quirrel and he imprints himself upon Quirrel, creating Tom Riddle #3. One Quirinus-Quirrel-possessed-by-Tom-Riddle enters; one Quirinus-Quirrel-possessed-by-Tom-Riddle leaves.

Using a minion (Sprout, perhaps), #1 forces #3 to make an Unbreakable Vow. The vow stipulates:
#3 will fully take on the role of Lord Voldemort. #3 will resurrect Hermione and coerce Harry into making the Vow about the world's destruction. #3 will also find an excuse to waste an entire hour on something, so that no one suspects Polyjuice Potion. After that, #3 must ensure being vanquished by Harry. He will not kill Harry under any circumstances, and he will reveal himself to Harry as the Dark Lord. If Harry fails to vanquish him, he must continue giving Harry more resources (the wand) and motivation (torture threats) until Harry does it. Lastly, #3 will obey the commands of anyone who gives the code phrase Recommend-Performance-Humble-Horizon-251, in case the plan fails, Harry gets killed, and #1 has to stop #3 from Dark Lording all over the place.

#1's minion erases #3's memory of making the Vow, and instead gives #3 false memories that he is actually #1 and has just taken most of Hogwarts hostage. (No need to risk detection by actually doing it. All he needs is the ability to claim it's true in Parseltongue, which only requires him to believe it.)

Then #1 Obliviates all minions involved (except the one involved in the fake hostage scheme), releases #3 to do his work, and retires to a quiet home in the country until this all blows over. He decides to abandon the role of Lord Voldemort and never act too much like a Dark Lord again until Harry is perma-dead. Thus, he maximizes his chances that the prophecy and Dumbledore's conditions think of #3 as the only relevant Dark Lord Voldemort.

Most everything else happens as the story says. #3, not knowing he's being controlled by an Unbreakable Vow, rationalizes his decisions, and is able to report that false motivation in Parseltongue because he believes it.

I find this theory *more believable* than the story where #1 willingly exposes himself to a prophecied opponent who is holding a wand, knows #1's true identity, and even has an hour left on his Time-Turner. The biggest weakness of the theory is that the imprinting might not work as smoothly as I describe. Still, #1 had plenty of time to experiment and perfect the plan before executing it, since there was nothing crucial about the exact moment he pulled it off.

That's about the size of it.

One last thing: In the "do not mess with time" incident, Harry didn't really get intimidated by the force of Time itself. It was just a false memory implanted by Dumbledore in accordance with the prophecies, to make sure Harry didn't learn too much about time travel too soon.''',
},
]

