#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime

from post_contents_utils import *
import html

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




{
  "title":"Some thoughts about liches",
  "auto_paragraphs": True,
  "contents":'''<p>(Content warning: descriptions of gender-based oppression.)</p>
  
The archetype of a lich is a powerful white man who sought immortality due to excessive ambition. Perhaps this is not, in itself, a bad moral. But must fantasy fiction always tell the stories of powerful men (whether good or evil), rather than fleshing out the other parts of society?

What is lichdom, after all, in a material sense? A one-time ritual reduces you to a miserable unlife, but makes you permanently able to tolerate deadly dangers. You no longer die if deprived of food or shelter. And you probably can't reproduce anymore. I ask you: Which members of society have need of these blessings?

Consider this: A world where mainly lower-class women are economically coerced into becoming liches. The society values sons more highly than daughters, so when a family doesn't have enough food to go around, the sons eat first, and the daughters are expected to be the ones to endure lichdom for the family's survival. They become efficient undead servants who can be asked to do even the most dangerous and unsanitary jobs.

Millennia later, a tech startup develops a more pleasant liching process, and tries to market it as a way for the wealthy to achieve eternal life. But they never manage to attract many customers because, ha ha, what self-respecting man would want to become a lich, like a woman?

''',
},




{
  "title":"2013-04-29 Lasercake talk script",
  "auto_paragraphs": True,
  "contents":'''
<p>(This is the script that I used to give a talk about Lasercake. <a href="https://www.youtube.com/watch?v=ocNckedfP6g">You can watch a video of the talk here.</a> This isn't an exact transcript, but it's pretty much the same as the body of the talk as I actually gave it.)</p>
  
I titled this talk, "What is Lasercake", but I'm going to start out with a harder question: What is a game? Suppose you're looking at Wikipedia, and you use your mouse and keyboard to <em>navigate</em> in order to reach an article with the information you want, that's your <em>goal</em> – hardly anybody thinks of that as a game. But now, let's say that instead of a mouse cursor, there's a little icon of a plumber, (is it a game yet?) and you use the arrow keys to move the plumber around (is it a game yet?), and instead of reading encyclopedia articles you are dodging evil mushrooms (is it a game yet?), and instead of looking for information you're looking for a page where there is an icon of a princess – <em>then</em>, everyone agrees that it is a game. But when did it become a game? Both activities have objectives and challenges, and both of them can be fun. But in one of them, a designer intentionally created the obstacles solely to make the player have fun – while on Wikipedia they were just trying to deliver information in the most efficient way. It's not all about fun, though – in a game that tells a story, you can act out a really sad scene, and that's intended to convey an emotion different than fun – and it's not all about challenges and objectives – there are some games that are just an activity, like playing catch, and some that have no clear end goal, like tag. So the definition I'll use is, "A game is an interactive system that where the ways you interact with the system were intentionally designed to have a purpose unto themselves." It's pretty broad, but it'll do.

So, how many of you have played with LEGO bricks? Now, are LEGO bricks a game? By my definition, they are: with LEGOs, you have fun and learn through the <em>process</em> of building with them. By comparison, the process of reading the Wikipedia article is only to convey the denotative meaning of the sentences on it. You can have fun and learn from reading them the sentences, but that's more like the delivery of a product than like an interactive process.
  
I envision my game, Lasercake, being like LEGO bricks – I'll get back to that comparison in a moment. This is just a prototype of the game – there'll be a lot more stuff to play with as I develop it more this summer, not to mention that it will look more like the actual Earth, instead of this blocky grey ground and black sky. When you start the game, you start out looking at a view from the point of view of a "robot" – you're playing the role of the robot, and you can move around and build things.

Everyone has some tricky practical dilemmas in their life – for example, a lot of people ask "Do I go for the healthy diet or the cheap diet?". But the reason we have to ask that question at all is because of our utter failure as a society to provide all people with food that is both healthy and affordable. I believe that the question "Should I do my homework or should I play games?" is the exact same thing, and the future of education will BE games. Think about how we teach science – science is cool, but the way we teach science is profoundly uncool. Telling someone that they need to memorize facts in order to write them down again on a test and get a numerical grade is extremely uncool! There's been some good research on the effects of external judgments like that – children are naturally curious about how the world works, but when you give them external rewards, it actually causes a long-term decrease in their intrinsic motivation. There's an old joke – an old man has a problem with a bunch of kids who come by his house every day and harass him. So one day, he says, “if you come back and taunt me tomorrow, I'll pay you each a quarter”. So the kids all come back the next day and taunt him for a while, and then he hands out a quarter to each of them, and says “And tomorrow, if you come back and taunt me again, I'll pay you each a dime”. And then they come back the next day and taunt him and jeer at him, and he hands out a dime to each of them, and says, “Tomorrow if you come back, I'll pay you each a nickel”. And all the kids say, “Come on, man! Not worth it!” and they never bother him again. And that is essentially what most schools are doing! It's terrible! But now, imagine that children could learn all of the science on their own time by playing around with it at their own initiative. Of course, it would be irresponsible to give them all science labs and let them blow themselves up, so I want to give them something even better – a virtual science lab where you can build entire industrial projects, and if you blow them up by accident then only virtual people get hurt by it.
  
Now, the power of games is already being used – it's just that this power is being used for evil. In 2001, the US Army released the game America's Army, and it quickly became one of its most effective recruiting tools. It was praised for depicting combat realistically, but it's deceptively realistic, because in real life it's not a good idea to go around shooting people in foreign countries. Now, don't get me wrong – there's a lot of people who think that violent video games in general are ruining our country, and that's not true – children have played violent games throughout history, just in different forms – but when you have enough credibility to pretend that something is actually realistic, then it can be dangerous. You can't always influence people's conscious beliefs, but you can sure influence their assumptions and their ways of thinking. For example, most people don't really think about all of the environmental damage done by mining. And all of our games that depict mining – I've played a lot of games where you dig in the ground to find gems and stuff – <em>all</em> of them depict it as a basically clean process where you just drill the rock into nonexistence in front of you – and so people can just keep assuming that real-life mining is kind of like that. Lasercake doesn't do that – in Lasercake, when you dig in the ground, you have to take the rubble and dump it somewhere – you can see that now – and as I develop the game further, the rubble will also pollute the surrounding land, it'll kill the plants that are living there, and the soil will be more prone to erosion – all those environmental consequences that you don't see playing traditional games. And when a game does depict those things, it can be really powerful. I remember one day in middle school where I was talking to someone who played Civilization 2 – that's a computer game where you build cities all over the Earth, and you build armies and try to capture other people's cities. And in that game, if you build too much stuff, you cause pollution, and if you don't clean up the pollution, then you get global warming, and you end up with most of the world's vegetation dying – you actually see most of the landmass turn to desert. And the person I was talking to said that when he saw that in the game, he was just overwhelmed with the fear that we were going to see that happen in real life. Of course, fear isn't the most productive emotion, but I can work with that. When you see something with your own senses, that came out of something you built yourself – that has a lot of impact, and you remember it.
  
So, with Lasercake, we're trying to make a game where the things you remember are actually <em>correct</em>.
  
So we're using a lot of real-life science. When you build and move things, that's going to take energy that's measured in the same units we use in real life, and we're actually going to have conservation of energy. You'll have solar panels, wind turbines, and stuff – and they're going to produce the same amount of energy they would in real life. Quick, which takes more energy – pumping a bathtubful of water up three stories, or leaving a 60-watt light bulb on for 20 minutes? You probably have no idea – I'd have no idea either if I didn't do the math when I was writing this. Even if you study it in the kind of class where you get numerical grades, you still won't get an intuitive sense of the relative magnitude of those things. You have to actually work with it. Games are great for practicing resource management, because they give you virtual resources, and if you mess it up, it only hurts you in the game. But we have a lot of games where you manage money to buy weapons, and not a lot of games where you manage the resources that human life is relying on. Of course, there's SimCity, a game where you take on the role of a city manager, choose tax rates, and spend money on city infrastructure – and that game has actually been used to help train people for city-management roles in real life, although it's obviously not a complete training all by itself. And it still uses money – I think we're better off not thinking of everything in terms of money, because money makes it easy to ignore if something you're buying was built in a way that's extremely wasteful and destructive. In Lasercake, you'll actually be seeing the sources of all the resources you're using.
  
So that's the <strong>mission</strong>. Now I'm going to move on to the part of my talk where I tell you about the process for actually doing this. It all started about two years ago – I was playing a game called Dwarf Fortress, where you play as a colony of dwarves who build things, and the game has flowing water in it that you can pump to different places and use to power water wheels. But if you pour out a lot of water, the game gets very slow. There are other games with flowing water that are very fast, but the water is limited or unrealistic. So I decided to try to make a water flow simulation that was both fast and at least somewhat realistic – but I didn't succeed at that. Until winter of last year, when my sibling and I worked on the problem together for more than a week, and came up with something that actually worked pretty well. And then we said "Well we have a cool water simulation – now let's build an entire game with robots!" And thus Lasercake was born. And then pretty soon we realized that it would work to bring in the educational mission. It was a bit more complicated than that, but that is basically what happened.
  
My sibling and I work together closely on almost every part of the project – the programming parts, the mission, the philosophy – though there are some bits that belong to one of us more than to the other. We both believe in the Free Software philosophy – that's free as in freedom, not price; we think that when a person has a piece of software, they have the right to see how it works, the right to share it, and the right to modify it and share their changes if they have the relevant skills. With most commercial software, you only buy a black-box version of the program, where it does its job but you can't look inside to see how it works or change it; to do that, you need the program's source code. We use the website "GitHub" to make all our source code publicly available as we develop it. With Free software, programmers can look at each other's work and collaborate, and there's a very large, robust Free Software community that our project fits into. Once the Lasercake project is more public, it's very likely that people from the community will volunteer to help improve it. We like volunteers, and there's a lot of different skills that we can use, like art, sustainable design, computer programming, geology, physics, sound design, gender studies, and many other things besides. Volunteers can contact us through <a href="mailto:lasercake@googlegroups.com">email</a>, our <a href="https://groups.google.com/d/forum/lasercake">Google Group</a>, <a href="https://webchat.freenode.net/?channels=lasercake">IRC</a>, or <a href="https://github.com/Lasercake/Lasercake/issues">GitHub</a>.
  
So, what goes into designing a game? A lot of it is arcane computer stuff, and this description is intended for laypeople. But it's not just about creating the literal program – it's also about figuring out how people will interact with it. For instance, rubble – that's the orange stuff in the game – can be moved around by clicking on it. If you click on the bits of rubble in the right way, they get pushed away from you. But a lot of people who play the game assume they can click and drag – pick up the rubble and move it somewhere else and put it down. That doesn't work, and so they fail to move it where they want it. Whose fault is it that this failure happened? It's all my fault! I'm the one who designed an system that doesn't work how people expect it to work. Of course, this is just a prototype, and that was the simplest way to move rubble I could think of – my real plan is to use exactly the "click and drag" system that seems natural to people. As a game designer, I'm putting a lot of work into a product that lots of people are going to use, and so I bear the whole responsibility for communicating as clearly as possible. And that means a lot of back-and-forth with people who play the game. I need to learn exactly how people perceive it so that I can have the best control over those perceptions. That goes especially for people who don't play many computer games, and for children – Lasercake is fairly complicated, and I want to make it as accessible to the widest audience possible, not just people who already know a lot of games.
  
When you play the game, you'll start out walking around digging up things like you see here – but as you start doing more and more stuff, you'll want to build more robots to do the tasks for you. So you'll have to have a way to tell them what to do – and for that, you'll write "robot plans". For example, one plan could be "Walk forward ten meters, then build a solar panel, then walk forward another ten meters, then build another solar panel, and so on"; you'll write that plan, then assign it to a robot, and then that robot will build a lot of solar panels while you go and work on something else. And eventually you'll want to automate it more, and you'll write more complicated plans – and the beauty of it is that these plans are actually simple computer programs within the program! Computers are very important in today's society, so computer programming knowledge is extremely valuable – but a lot of people are too intimidated to learn it, and for good reason, because programming tools are mostly designed by people who already know a lot about programming and don't think very much about education. And there's a huge gender issue there too – female people have an extra burden, because even the most hippie-ish Free Software groups still have a lot of casual sexism in them. But by rolling it into the robot plans, we can introduce people to programming in a way that's not intimidating – we call them "plans" rather than "programs" for exactly that reason. It's also a situation that can appeal to intrinsic motivations, since the plans will be immediately available to save their time and effort and make their robots do cool things. That's in contrast to a programming class, where you have to decide to take it – that's a big decision for someone who doesn't know what it will involve – and even then, it takes a while before you can do anything with much practical usefulness. But within the world of Lasercake, the basics will be useful immediately. And we're doing our best to make Lasercake, like LEGOs, transcend the boundaries of gender. Well, LEGOs in their heyday, anyway. Recently, the LEGO Group has produced a bunch of terrible gender-stereotyped sets. But I'll complain about that more some other time.
  
And that's Lasercake! I hope that it will help teach people things and move forward our understanding of education and sustainability. And I guess it would also be pretty nice if that knowledge can save the entire human race from rushing cheerfully into their own destruction. 
  ''',
}, 


{
  "title":"You Don't Know Jack about Performance: the Game Show",
  "head":'''<style>
#you-dont-know-jack-about-performance-the-game-show pre {
  overflow: auto;
  border: 1px dashed black;
  padding: 1.2em;
  margin: 1.8em 0;
}
  </style>''',
  "contents":auto_paragraphs('''
  
ANNOUNCER: Welcome, gentle viewers, to day 2 of <em>You Don't Know Jack about Performance</em>! First question: Suppose we iterate through ten million items, divided into linked lists of length L, with the heads in one large array. How will the performance change as we change L?

CONTESTANT: Well, for very short lists, the processor will be able to prefetch all of the elements. But for long lists, the cost will be dominated by memory latency. Therefore, larger L means more time taken.

ANNOUNCER: An excellent answer! Let's see what the Data have to say about it!

THE DATA: <span style="font-family: monospace">*sad trombone*</span>

''')+'''
<pre>
Time taken for list length 1: 1.26s (125.66 ns/item, 125 ns/list)
Time taken for list length 2: 575.71ms (57.57 ns/item, 115 ns/list)
Time taken for list length 3: 1.34s (134.27 ns/item, 402 ns/list)
Time taken for list length 4: 1.08s (107.76 ns/item, 431 ns/list)
Time taken for list length 6: 926.16ms (92.62 ns/item, 555 ns/list)
Time taken for list length 8: 784.97ms (78.50 ns/item, 627 ns/list)
Time taken for list length 12: 621.95ms (62.20 ns/item, 746 ns/list)
Time taken for list length 16: 569.39ms (56.94 ns/item, 911 ns/list)
Time taken for list length 24: 465.72ms (46.57 ns/item, 1117 ns/list)
Time taken for list length 32: 418.11ms (41.81 ns/item, 1337 ns/list)
Time taken for list length 48: 350.14ms (35.01 ns/item, 1680 ns/list)
Time taken for list length 64: 320.25ms (32.02 ns/item, 2049 ns/list)
Time taken for list length 96: 277.97ms (27.80 ns/item, 2668 ns/list)
Time taken for list length 128: 270.64ms (27.06 ns/item, 3464 ns/list)
Time taken for list length 192: 224.83ms (22.48 ns/item, 4316 ns/list)
Time taken for list length 256: 222.18ms (22.22 ns/item, 5687 ns/list)
Time taken for list length 384: 201.32ms (20.13 ns/item, 7730 ns/list)
Time taken for list length 512: 196.19ms (19.62 ns/item, 10044 ns/list)
Time taken for list length 768: 192.77ms (19.28 ns/item, 14806 ns/list)
Time taken for list length 1024: 190.29ms (19.03 ns/item, 19487 ns/list)
Time taken for list length 1536: 192.33ms (19.23 ns/item, 29543 ns/list)
Time taken for list length 2048: 187.04ms (18.71 ns/item, 38312 ns/list)
Time taken for list length 3072: 184.54ms (18.46 ns/item, 56695 ns/list)
Time taken for list length 4096: 112.18ms (11.22 ns/item, 45955 ns/list)
Time taken for list length 6144: 111.45ms (11.15 ns/item, 68498 ns/list)
</pre>
  '''+auto_paragraphs('''
  
ANNOUNCER: Contestant #2, do you have anything to add to Contestant #1's analysis?

CONTESTANT #2: Well, in your test code, you allocated each list all at once. That could have made each list be allocated in contiguous memory, making them easier to iterate. And we might be seeing some effects from the order the tests were done in, like yesterday, although I'm guessing not, because this time all the node allocations are the same size.

ANNOUNCER: Beautiful! Let's rerun the tests, but this time, add nodes to the linked lists one at a time, like a dealer dealing out a pack of cards! And we'll run them in the opposite order, just in case. So, Contestant #2, what do you expect to see?

CONTESTANT #2: Everything will be slower – and the long-list advantage will be reduced, but not eliminated.

ANNOUNCER: A bold conjecture! Let's see what the Data have to say about it!

THE DATA: <span style="font-family: monospace">*victory music*</span>
  
  ''')+'''
<pre>
Time taken for list length 6144: 832.84ms (83.32 ns/item, 511888 ns/list)
Time taken for list length 4096: 861.68ms (86.18 ns/item, 353004 ns/list)
Time taken for list length 3072: 1.90s (189.66 ns/item, 582645 ns/list)
Time taken for list length 2048: 1.92s (191.92 ns/item, 393042 ns/list)
Time taken for list length 1536: 1.94s (193.88 ns/item, 297796 ns/list)
Time taken for list length 1024: 1.96s (196.17 ns/item, 200881 ns/list)
Time taken for list length 768: 1.97s (196.74 ns/item, 151094 ns/list)
Time taken for list length 512: 2.04s (203.90 ns/item, 104395 ns/list)
Time taken for list length 384: 1.98s (198.49 ns/item, 76220 ns/list)
Time taken for list length 256: 2.10s (210.16 ns/item, 53799 ns/list)
Time taken for list length 192: 2.12s (212.06 ns/item, 40714 ns/list)
Time taken for list length 128: 2.05s (205.00 ns/item, 26239 ns/list)
Time taken for list length 96: 2.03s (203.29 ns/item, 19515 ns/list)
Time taken for list length 64: 2.09s (208.87 ns/item, 13367 ns/list)
Time taken for list length 48: 2.08s (207.92 ns/item, 9980 ns/list)
Time taken for list length 32: 2.12s (211.83 ns/item, 6778 ns/list)
Time taken for list length 24: 2.22s (221.79 ns/item, 5323 ns/list)
Time taken for list length 16: 2.22s (221.66 ns/item, 3546 ns/list)
Time taken for list length 12: 2.31s (230.64 ns/item, 2767 ns/list)
Time taken for list length 8: 2.43s (242.64 ns/item, 1941 ns/list)
Time taken for list length 6: 2.55s (254.67 ns/item, 1528 ns/list)
Time taken for list length 4: 2.82s (282.44 ns/item, 1129 ns/list)
Time taken for list length 3: 3.09s (308.62 ns/item, 925 ns/list)
Time taken for list length 2: 3.61s (360.83 ns/item, 721 ns/list)
Time taken for list length 1: 2.20s (219.54 ns/item, 219 ns/list)
</pre>
  '''+auto_paragraphs('''
  
ANNOUNCER: And now for the million CPU cycle question: why?

CONTESTANT #2: Total memory loaded. The jump from L=1 to L=2 can be explained by the effect Contestant #1 described, but the system isn't smart enough to benefit from prefetching over more than one link. From L=2 to L=3072, the per-item cost goes down by 47%, but the linked list implementation we're using doesn't store the head item directly in the array – the array stores structs containing head, tail, and len, which adds a fixed overhead equal to one item at the beginning of every list. With this overhead considered, the cost per byte only goes down by 22% over that range.

ANNOUNCER: What about the jump between L=3072 and L=4096?

CONTESTANT #2: Nothing to do with the list length, and everything to do with the number of lists in the array. With a constant array size, there's no jump. And I can't help but notice that L=3072 to L=4096 is the threshold where the array allocation size crosses 65536 bytes.

ANNOUNCER: Maybe you're onto something there! Let's run tests with a constant list length, and varying number of lists, concentrating on numbers of lists that make the array close to 65536 bytes. What do you expect to see?

CONTESTANT #2: Array sizes smaller than 65536 will run the test about twice as fast.

ANNOUNCER: A fascinating theory! Let's see what the Data have to say about it!

THE DATA: <span style="font-family: monospace">*victory music*</span>
  
  ''')+'''
<pre>
Time taken for 2727 lists of length 4096: 946.69ms (84.75 ns/item, 3.53 ns/byte, 347153 ns/list)
Time taken for 2728 lists of length 4096: 949.64ms (84.99 ns/item, 3.54 ns/byte, 348106 ns/list)
Time taken for 2729 lists of length 4096: 974.79ms (87.21 ns/item, 3.63 ns/byte, 357196 ns/list)
Time taken for 2730 lists of length 4096: 2.06s (184.16 ns/item, 7.67 ns/byte, 754323 ns/list)
Time taken for 2731 lists of length 4096: 2.06s (183.99 ns/item, 7.66 ns/byte, 753624 ns/list)
Time taken for 2732 lists of length 4096: 2.07s (184.66 ns/item, 7.69 ns/byte, 756348 ns/list)
</pre>
  '''+auto_paragraphs('''  

ANNOUNCER: Well, then, perhaps we'll have to revise some of our earlier analysis! Let's run the tests again, but this time, store the linked lists in an array of arrays – so that each individual allocation holds only the square root of the number of lists, rather than the full number of lists. Contestant #2, what do you expect to see then?

CONTESTANT #2: Everything will be faster than last time - with shorter lists getting more of a bonus. With the large-allocation disadvantage gone, there won't be a jump between L=3072 and L=4096, and everything will have a similar per-byte cost, except L=1, which will be faster for the same reason as before.

ANNOUNCER: Beautiful! Let's see what the Data have to say about it!

THE DATA: <span style="font-family: monospace">*sad trombone*</span>
  
  ''')+'''
<pre>
Time taken for 9998244 lists of length 1: 85.44ms (8.55 ns/item, 0.18 ns/byte, 8 ns/list)
Time taken for 4999696 lists of length 2: 60.53ms (6.05 ns/item, 0.17 ns/byte, 12 ns/list)
Time taken for 3330625 lists of length 3: 50.76ms (5.08 ns/item, 0.16 ns/byte, 15 ns/list)
Time taken for 2499561 lists of length 4: 47.81ms (4.78 ns/item, 0.16 ns/byte, 19 ns/list)
Time taken for 1664100 lists of length 6: 43.88ms (4.39 ns/item, 0.16 ns/byte, 26 ns/list)
Time taken for 1249924 lists of length 8: 43.26ms (4.33 ns/item, 0.16 ns/byte, 34 ns/list)
Time taken for 624100 lists of length 16: 49.64ms (4.97 ns/item, 0.19 ns/byte, 79 ns/list)
Time taken for 416025 lists of length 24: 53.63ms (5.37 ns/item, 0.21 ns/byte, 128 ns/list)
Time taken for 312481 lists of length 32: 75.01ms (7.50 ns/item, 0.30 ns/byte, 240 ns/list)
Time taken for 207936 lists of length 48: 313.08ms (31.37 ns/item, 1.28 ns/byte, 1505 ns/list)
Time taken for 156025 lists of length 64: 311.63ms (31.21 ns/item, 1.28 ns/byte, 1997 ns/list)
Time taken for 103684 lists of length 96: 363.19ms (36.49 ns/item, 1.50 ns/byte, 3502 ns/list)
Time taken for 77841 lists of length 128: 357.48ms (35.88 ns/item, 1.48 ns/byte, 4592 ns/list)
Time taken for 38809 lists of length 256: 369.60ms (37.20 ns/item, 1.54 ns/byte, 9523 ns/list)
Time taken for 19321 lists of length 512: 408.02ms (41.25 ns/item, 1.72 ns/byte, 21117 ns/list)
Time taken for 9604 lists of length 1024: 436.45ms (44.38 ns/item, 1.85 ns/byte, 45444 ns/list)
Time taken for 4761 lists of length 2048: 489.26ms (50.18 ns/item, 2.09 ns/byte, 102764 ns/list)
Time taken for 3249 lists of length 3072: 524.33ms (52.53 ns/item, 2.19 ns/byte, 161382 ns/list)
Time taken for 2401 lists of length 4096: 492.44ms (50.07 ns/item, 2.09 ns/byte, 205096 ns/list)
Time taken for 1600 lists of length 6144: 814.67ms (82.87 ns/item, 3.45 ns/byte, 509168 ns/list)
</pre>
  '''+auto_paragraphs('''  
ANNOUNCER: Contestant #3, do you have anything to add to Contestant #2's analysis?

CONTESTANT #3: Would you look at that – very similar per-byte cost for everything from L=1 up to L=16. Our test machine has 64-bit-width, 1333-1600 MT/s memory, meaning that the minimum POSSIBLE ns/byte would be around 0.094 ns/byte - faster if you can use all 3 memory modules in parallel, but also slower, because for each node, we have to fetch a whole cache line of 64 bytes instead of just the 24 bytes the node actually takes up. Multiplying 0.094 by 64/24 gets us 0.25, nearly twice as long as it actually took – and we can't keep nearly all of the 240MB in our 6MiB L3 cache, so it follows that the operations are memory-throughput-bound, and the tests are using the throughput of multiple memory modules. It follows that anywhere up to the 16-32 range, the processor IS able to prefetch enough links in parallel that latency is not the bottleneck. On the other hand, as we reach very high list lengths, we bottleneck on memory latency at about 81.6ns per cache line. A very encouraging result for balanced-tree data structures, which are traditionally questioned because of their chained memory accesses, but rarely have a depth greater than 32 – so they can make use of full memory throughput as long as you can know which search will come next before the first search finishes.

ANNOUNCER: How do you explain the jump between L=32 and L=48?

CONTESTANT #3: That's a good question. I would expect to see a more uniform dropoff, as it reaches the limits of how far ahead the processor will prefetch. But, given that the length is known ahead of time – maybe the compiler gives a hint about whether to prefetch the head of the next list, and if we're going to do more than 32 sequential lookups first, it thinks there's no point?

ANNOUNCER: So if we looked at the results for all lengths between L=32 and L=48, what would you expect to see?

CONTESTANT #3: A sharp dropoff somewhere – perhaps right after 32 – followed by uniform results near the same 31 ns/item mark that it hits at L=48.

ANNOUNCER: Let's see what the Data have to say about it!

THE DATA: <span style="font-family: monospace">*sad trombone*</span>
  
  ''')+'''
<pre>
Time taken for 312481 lists of length 32: 77.20ms (7.72 ns/item, 0.31 ns/byte, 247 ns/list)
Time taken for 302500 lists of length 33: 322.55ms (32.31 ns/item, 1.31 ns/byte, 1066 ns/list)
Time taken for 293764 lists of length 34: 130.13ms (13.03 ns/item, 0.53 ns/byte, 442 ns/list)
Time taken for 285156 lists of length 35: 322.30ms (32.29 ns/item, 1.31 ns/byte, 1130 ns/list)
Time taken for 277729 lists of length 36: 274.03ms (27.41 ns/item, 1.11 ns/byte, 986 ns/list)
Time taken for 269361 lists of length 37: 136.09ms (13.66 ns/item, 0.55 ns/byte, 505 ns/list)
Time taken for 262144 lists of length 38: 381.62ms (38.31 ns/item, 1.56 ns/byte, 1455 ns/list)
Time taken for 256036 lists of length 39: 238.72ms (23.91 ns/item, 0.97 ns/byte, 932 ns/list)
Time taken for 250000 lists of length 40: 200.26ms (20.03 ns/item, 0.81 ns/byte, 801 ns/list)
Time taken for 243049 lists of length 41: 294.21ms (29.52 ns/item, 1.20 ns/byte, 1210 ns/list)
Time taken for 237169 lists of length 42: 300.78ms (30.20 ns/item, 1.23 ns/byte, 1268 ns/list)
Time taken for 232324 lists of length 43: 141.42ms (14.16 ns/item, 0.58 ns/byte, 608 ns/list)
Time taken for 226576 lists of length 44: 331.91ms (33.29 ns/item, 1.36 ns/byte, 1464 ns/list)
Time taken for 221841 lists of length 45: 303.29ms (30.38 ns/item, 1.24 ns/byte, 1367 ns/list)
Time taken for 217156 lists of length 46: 341.57ms (34.19 ns/item, 1.39 ns/byte, 1572 ns/list)
Time taken for 212521 lists of length 47: 288.47ms (28.88 ns/item, 1.18 ns/byte, 1357 ns/list)
Time taken for 207936 lists of length 48: 332.36ms (33.30 ns/item, 1.36 ns/byte, 1598 ns/list)
</pre>
  '''+auto_paragraphs('''  

ANNOUNCER: And there you have it, folks! No matter how much you know, you can still find a way to be wrong. Every night, on <em>You Don't Know Jack about Performance</em>.
  

<bigbreak> 

Notes:

I'm sure there's a bunch of interesting follow-ups I could do on this post. Unfortunately, at the time of this writing, I'm having a lot of fatigue due to my cyclic depression. I'm handling it okay, but I don't think I can afford to spend more energy on this, so this will have to be its final form for now.

Here's the final test code (written in Rust):''') +'''

<pre>'''+html.escape('''
use rand::prelude::*;
use std::time::Instant;
use std::collections::{HashSet, BTreeSet, LinkedList};

fn benchmark_array_of_lists(size: usize, buckets: Option <usize>) {
  let array_size = (buckets.unwrap_or (10_000_000/size) as f64).sqrt().floor() as usize;
  let num_buckets = array_size*array_size;
  let num_items = num_buckets *size;
  let num_bytes = num_buckets *24 + num_items*24;
  let mut buckets: Vec<Vec<LinkedList <u64>>> = (0..array_size).map (|_| (0..array_size).map (|_| (0..1u64).collect()).collect()).collect();
  
  for i in 0..size {
    for bucket in &mut buckets {
      for list in bucket {
        list.push_back(i as u64);
      }
    }
  }
  buckets.shuffle (&mut rand::thread_rng());

  let before = Instant::now();
  
  let mut result: u64 = 0;
  for bucket in &buckets {
    for list in bucket {
      for value in list {
        result += value;
      }
    }
  }
  
  let elapsed = before.elapsed();
  let nanos = elapsed.as_nanos();
  println!( "Time taken for {} lists of length {}: {:.2?} ({:.2} ns/item, {:.2} ns/byte, {} ns/bucket) {}", num_buckets, size, elapsed, nanos as f64/num_items as f64, nanos as f64/num_bytes as f64, nanos/num_buckets as u128, result);
}


fn main() {
  for x in (0..32).rev() {
    benchmark_array_of_lists(((1<<((x+1)>>1)) + (1<<((x+2)>>1)))>>1, None);
  }
  
  /*(for x in (32..=48).rev() {
    benchmark_array_of_lists(x, None);
  }*/
  
  /*for x in (2727..2733) {
    benchmark_array_of_lists(4096, Some(x));
  }*/
}
''')+'''
</pre>

''' ,
}, 
]

