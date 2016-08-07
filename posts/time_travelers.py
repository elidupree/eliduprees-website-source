#!/usr/bin/python3
# -*- coding: utf-8 -*-


import re
import utils


posts = [
{
  "title":"Time Travelers and How to Kill Them: a Practical Guide",
  "blurb": "A fictional book written in a world with many forms of time travel.",
  "don't deploy": True,
"authors_notes":'''

<p>There are a lot of stories with time travel in them, but very few that try to establish a consistent set of rules about how time travel works. I enjoy designing fictional systems, so I decided to do something about that. It was quite a challenge to design systems that behave <em>similarly</em> to the inconsistent systems from stories, while still being consistent themselves. I think I did a pretty good job, though.</p>



<p>Another common thing in stories with time travel is that it's usually the protagonists who have time travel. Their enemies usually don't have any time travel powers, or, at worst, they have the same amount as the protagonists do. I decided to amuse myself by writing this document from the opposite perspective: you have to fight against time travelers without having any time travel powers yourself. That makes for a much bigger challenge. It also helped force me to think out all the details of how each power worked.</p>



''',
  "head":'''<style>
  .small_print {font-size: 90%;}
  .small_print p {text-indent: 0; margin-top: 0; margin-bottom: 0;}
  .table_of_contents { display: block; margin:0.2em 0;}
  .table_of_contents_3 { padding-left:1.5em;}
  .table_of_contents_4 { padding-left:3em;}
  pre {overflow: scroll;}
 </style>''', 
},
]

    
contents ='''
<div class="small_print">
Copyright © 2015, 2016, 2078, 664, 8981 BC, 7474+2i, International Time Travel Defense Research Consortium
All rights reserved under the Atemporal Copyright Convention.
Time Travelers and How to Kill Them: a Practical Guide.
Revision f017f23, based on parent revisions 7eefc88, 0930966, and 5e83d8c.
A full revision history of this book, including alternate timelines and possible lost versions, is on display at the Time Travel Historical Society in Vancouver.
</div>

<h2>Table of Contents</h2>
<TOC>


<h2>Preamble</h2>

We all know the quote from William Shakespeare, "The only way to stop a time traveler / is to be a more skillful time traveler". In some ways, this is true: among all supernatural powers, time travel has always been one of the most difficult to fight against, and in some cases, the most dangerous to the entire world. However, Shakespeare does not tell the entire story. If you have to fight a time traveler, don't despair. Despite their reputation, time travelers are human like the rest of us, and they have weaknesses that can be exploited.

No better than Shakespeare's cynicism is the cheerful subservience of the modern mass media, which typically tells stories of ordinary people being empowered by the force of time travel. They portray time travel as exciting, adventurous, and ultimately harmless. Make no mistake: time travel is power, and power attracts the most corrupt among us. The sheer scale of tyranny and abuse that has been enabled by time travel far outweighs any good it could possibly do.

We recognize that not all time travelers are evil, and not all non-time-travelers are good. If this book helps people to fight against time travelers, it may not always result in the triumph of good over evil. However, we do hope that the advice in this book can, in some small way, even the playing field between the powerful and the powerless.

And lastly, if you are a time traveler yourself, don't even bother trying to go back and prevent this book's publication. You will not only fail, but even make things worse for yourself in the process.

<h2>A Note on the Morality of Killing</h2>

When it comes to fighting against time travelers, there are three main schools of thought.

<strong>Regulationists</strong> believe in treating time travel like any other supernatural power. In regulationist thought, there are "good time travelers", with whom we should cooperate, and "evil time travelers", against whom we should fight. Regulationists generally believe that we should not kill any time traveler unless it is proven that they have greatly abused their power.

<strong>Exterminationists</strong> believe that the idea of "good time travelers" is naïve. Even if a time traveler has no intention of using their powers for evil, they may still be manipulated by evil, or their powers may fall into the wrong hands. Therefore, exterminationists believe that all time travel must be destroyed, even if it requires the killing of innocent people. Some even believe in killing people who merely have the <em>possibility</em> of being time travelers, although even the most hard-line exterminationist must admit that unnecessary killing will harm their organization's ability to cooperate with ordinary people.

Finally, <strong>futilists</strong> believe that it is counterproductive to try to fight against <em>any</em> time traveler, even the most evil ones. If we fight against time travelers, they say, we will not only fail, but also encourage them to take preemptive action against us. Futilists would no doubt oppose the entire premise of this book, so we need not give any serious consideration to their perspective.

This book does not take a position in the debate between regulationists and exterminationists. Instead, it merely documents techniques which either faction might use, <em>when</em> they determine that the time has come to fight.


<h2>Part one: General principles</h2>

Although there are many types of time travel, they have enough in common that much of the same advice is useful for almost all types of time travel.

<h3>1.1: Countering time travel</h3>

<h4>Destroy the source</h4>

All time travel abilities have a specific source &ndash; usually a machine, a spirit, or a human being. If you want to stop the time travel, you have to destroy the source.

If the source is a human, that means the human has to die. Other methods, like drugging them or imprisoning them, can theoretically work, but have very low success rates. All types of time traveler have unique abilities to escape ordinary imprisonment. This is why our title reads "How to Kill Them", not "How to Stop Them". Even the most merciful regulationist will not usually be able to stop a human time traveler without killing, if the human is not relying on a machine or spirit that can be destroyed separately.

If you destroy a time machine, it is sometimes safe to spare the human or humans who were using it. However, it is still somewhat less reliable. An enemy who knows a lot about time travel, even if they can't use it themselves, might be able to contact another time traveler and convince (or trick) them into undoing the events that made them lose their powers. They may even be able to build another time machine themselves. That said, if you are the more merciful type of regulationist, or if you have a special reason not to kill them, you may be willing to take this risk. (And, indeed, there will always be some risk from other time travelers, even if you kill your enemy outright.)


The unique concerns of time travel are the reason why time travel defense organizations are not simply divisions of general security groups. This is exemplified by the American Superpower Defense Force handling of the Kellianne Grory case. The ASDF held Grory in a special cell that suppressed all supernatural abilities. This would have been sufficient to contain almost any power user, but not the specific type of time traveler that Grory had become. Grory escaped the cell with help from outside &ndash; then went back in time to provide that outside help to herself.

A word of caution: although killing time travelers is often <em>necessary</em> to stop them, it is not always <em>sufficient</em>. We will list a few of the caveats here: If a human time traveler is using a non-human source, the source may be able to reset the situation even after the human is killed. If a human time traveler is killed with ordinary weapons, they may have a few moments before death when they can reflexively reverse time. And in the rare case that multiple time travelers work together, the survivors may be able to undo the death of one of their allies. The most pragmatic attack &ndash; especially if you are an exterminationist &ndash; is to simultaneously kill the time travelers and destroy their devices, instantaneously, before they have any opportunity to realize the danger.

<h4>Act In Secret</h4>

Time travelers make incredible investigators. If they even begin to suspect what you're planning, they might go back and spy on you for the entire time. Therefore, you must keep them completely unaware of your plans until the moment of your triumph, and you only get one chance to strike. Occasionally, this means "Only one chance in each timeline they create", but usually, it means only one chance total.

<h4>Spy On Them</h4>

To defeat a time traveler, you need to know how their powers work and what their habits are. Using human spies is risky, but hidden cameras can be effective. Time travelers are generally no more likely to notice such things than anyone else.

A word of warning: if your time traveler can go back and try different actions, they may notice that you behave differently depending on what they do while in front of the cameras. Depending on the situation, it may be wise to save up the camera recordings for a while without watching them, so that your responses don't give anything away.

<h4>Trick Them</h4>

Using time travel usually has far-ranging effects, many of which the time travelers themselves do not intend. It is often possible to manipulate the unintended effects to gain an advantage against them.

Of particular interest is the possibility of sending messages back in time to <em>yourself</em>, using the time traveler as an unwitting messenger. If your enemy carries a smartphone on their time journeys, compromising it should be a top priority. It can be programmed to report to you every time its internal clock disagrees with the time servers. With sufficient planning, lower-tech methods are possible as well.

<h4>Know Their Limits</h4>

Some time travelers can't go back more than a certain amount of time. Suppose that your enemy cannot go back farther than one hour. Now suppose also that you know they will be attending a two-hour lecture. If you secretly lock the doors behind them at the beginning of the lecture, then wait until the end of the lecture to strike, they won't be able to go back to before they were locked in. (Don't make the mistake of relying on a trap like this to keep them contained in the long-term, though. Only use a technique like this as part of a larger plan to destroy the source of the time travel.)

Those who can go back much more than one hour usually have other limitations. Some have to <em>wait</em> a certain amount of time before they can use their power again, making certain attacks possible during the cooldown period. Some abilities can only be used a certain number of times in total, making it possible to force (or trick) the time traveler and using up their ability.


<h3>1.2: Spotting time travelers</h3>

Most time travelers try to hide the fact that they are time travelers. If one of your enemies is a time traveler, it is crucial for you to figure that out as soon as possible. With equal importance, you must not let the time traveler realize that you have discovered them.

Each type of time travel has its own telltale signs. (See Part Three, "Specific Types of Time Travel".) However, there are also signs that are common to all types of time travel.

Firstly, all time travelers run the risk of getting confused about the passage of time as others experience it. Especially careless time travelers might act confused about time in ordinary conversations, or even reveal that they remember events that haven't happened yet. With smart time travelers, don't rely too much on obvious giveaways, since they are likely to keep close track of time themselves. In that case, you can sometimes spot the time traveler when they display an unusually accurate memory of when things happened. This is, of course, merely circumstantial evidence, since many people possess unusually good or bad memories naturally.

You can gather evidence not only from the time traveler themselves, but also from the time traveler's possessions. If a time traveler carries a wristwatch or cell phone while reversing time, it may report an incorrect time afterwards. Don't let a time traveler catch you looking at their watch, though. Perhaps the safest way is to use a high quality hidden camera and review the footage later.

Secondly, many time travelers can appear to be in two places at once, or at least to move unusually fast. Keep track of your enemy's location as much as possible, and see if you can catch them in two places at once, or catch them traveling between two distant locations almost instantly. However, these feats may be the result of other supernatural powers, not time travel. Consider them in combination with the other signs, and look for evidence that what you observed isn't simply the result of shapeshifters or teleportation.

Thirdly, many time travelers undo or avoid any significant bad events that occur in their lives. If you have the chance to observe a potential time traveler for a long time, watch for suspicious patterns. Most people occasionally experience a bad thing happening to their family, friends, or themselves &ndash; bad enough that they worry about it for a long time afterwards. If a person doesn't have anything like this in their life, they may be a time traveler. If your time traveler isn't especially careful about being detected, they may even reverse minor bad things, and thereby appear to lead a charmed life.

Like the other signs, this one has false-positives as well. If a person seems very fortunate, they may still be a luck manipulator rather than a time traveler. This requires different strategies. For instance, if you shoot a gun at a time traveler, they are fairly likely to die, but if you shoot a gun at a luck manipulator, you will almost certainly miss. Since luck manipulators require very different techniques to fight against than time travelers, this book will not attempt to discuss anti-luck-manipulator strategy.


<h3>1.3: Using other supernatural powers against time travelers</h3>

<h4>Time Travel</h4>

Time travel is undoubtedly a useful power for fighting against time travelers. However, using time travel against other time travelers is outside the scope of this book.

<h4>Mind Control</h4>

If you are fighting against one opponent, mind control is a suitable weapon. Once you control them, you can make them stand still while you kill them. With the right type of mind control, you can also force them to reveal anything they know that the source of their abilities. Those two ways of using mind control should be sufficient. Trying any cleverer techniques is usually an unnecessary risk.

If you have multiple opponents, you might be able to control one of them and use that one against the others. This includes when you are up against multiple copies of the same time traveler. Special strategies for using mind control against certain types of time travelers will be covered in the sections on those types.

You can also, of course, use your control to take advantage of their time travel powers yourself, but using time travel against other time travelers is outside the scope of this book.

<h4>Memory Modification</h4>

Like mind control, this can be used as a weapon directly against your enemy: give them false memories that lead them to their death. However, there are additional uses.

If you can permanently erase a person's memories of using time travel, that is almost as effective as killing them. However, people almost always try to investigate their missing memories. If you use this strategy, make sure that you also destroy any physical evidence, or prevent them from investigating in some way.

Normally, it's not safe to ask around or interrogate other people about the time traveler, because the time traveler might hear about it. If you can erase the memories afterwards, it becomes much safer to question possible witnesses. Also, erasing parts of your own memory (after recording them in a safe place) may occasionally be useful to prevent a time traveler from discovering what you know. 

Be wary of giving false memories to other people in the hope of deceiving the time traveler. Smart time travelers make sure to investigate things in detail before acting, and complicated schemes like this may leave evidence of your involvement. (Imagine if the time traveler goes back to examine how the person got the memories they claimed to have…)

<h4>Shapeshifting</h4>

Theoretically, by impersonating a time traveler, you could trick them into believing that you are delivering a message from themselves from the future. However, impersonating a person to themselves is extraordinarily difficult, especially if they have already talked to themselves a lot. It could possibly work, but if the time traveler becomes suspicious, they will be much more careful after that.

Although the International Time Travel Defense Research Consortium no longer works directly with any time traveler, we did originally employ a team of time travelers whose mission was to hunt other time travelers. At one point, they experimented with using a doppelgänger, and tested the strategy by sending the doppelgänger to trick each other. They concluded that the strategy was too unreliable to use.

That said, the team had access to many other, more reliable powers. If shapeshifting is your main ability, it may be your best bet. It may also be worthwhile if you have a second ability that can make your enemy less likely to detect you, such as by making them unlucky or clouding their mind in some way.

<h4>Luck Manipulation</h4>

Although this is a useful power, it is not wise to try anything too clever. If a time traveler notices how lucky you are, they might suspect you have a power and consider you a possible threat. However, it's always good to have extra luck to make sure that the time traveler doesn't notice you in any way. Concentrate your power on that.

Also note that some time travelers have a unique way to resist luck manipulation: if they go back in time far enough, they can make plans and gather resources before you got your luck manipulation power in the first place.

<h4>Power Suppression</h4>

Temporarily suppressing a time traveler's powers is no better than putting the time traveler in a prison. To be blunt, it won't work.

If you have access to an ability that permanently removes an enemy's powers, it is possible to use that as a substitute for killing them, with the usual caveats. 

<h4>Flight, Invisibility, Teleportation, Super Strength, Bulletproof, Telekinesis, etc.</h4>

Lesser powers like these are occasionally useful for combat or spying, but they are generally much too conspicuous. Yes, even invisibility. If your enemy catches you spying normally, they might still think you're just a snoopy muggle. If they catch you spying while invisible, you become an obvious threat.

If you're already known for having powers like these, you may be worse off than if you didn't have them at all. In this case, your enemy is probably already keeping an eye on you. The best way to avoid their attention is to keep playing the role of a naïve superhero who does things like saving children, stopping petty criminals, and so forth. If you don't show an interest in finding the man-behind-the-man, you may be able to stay beneath their notice.



<h2>Part two: Specific Types of Time Travel</h2>

<h3>2.1: Personal Time Reversal</h3>

We cover this type of time travel first because it is the easiest to understand: it is the smallest departure from conventional reality. Reversers, unlike other time travelers, can never be in two places at once, and cannot even attempt to cause paradoxes. However, they are every bit as dangerous.

A typical reverser has the power to "undo" their own actions, causing everything in the universe to return to its previous state, except for their own memories of what happened. Outside observers never experience the undone actions. Instead, from an outside perspective, the reverser appears to have a series of "replacement events": moments when their mind is replaced by a mind that has experienced one or more possible futures.

Reversers can be divided into several types, depending on the scope of their abilities. "Short-term reversers" can go back by a few seconds to an hour as many times as they want, and repeat a task until they succeed. "Long-term reversers" can go back and repeat days, months, or even years at a time. The most powerful reversers can use both long-term and short-term reversals with ease. Theoretically, most long-term reversers can also function as short-term reversers. Fortunately, most long-term reversers find their power very difficult or unpleasant to use, so they only use it occasionally, and only for important things. Also, a long-term reverser's power may take a long time to activate, meaning that they can't necessarily use it to escape immediate danger.

Reversers can often use their abilities as a purely mental action, not relying on a specific time machine or device. Even if they do use a device, it can be hard to find, because you will never actually remember seeing them use it. In the case of short-term reversers, it's worthwhile to check whether they have an object that they always carry but never seem to use. For long-term reversers, it's more likely to be an unusual, large object that they keep at their home, workplace, or childhood hiding place. (Obviously, you shouldn't ask them any questions about it yourself. Simply notice how they respond to questions from other people.)

<h4>Strengths and Distinctive Traits</h4>

<blockquote>
"I know about you and Sally!"
"What are you talking about?"
Reverse.
"I know about you and James!"
"What are you talking about?"
Reverse.
"I know about you and Cameron!"
"What are you talking about?"
Reverse.
"I know about you and Kate!"
"Hey! Who told you?"
Reverse.
<p>- A typical conversation with a short-term reverser</p>
</blockquote>

The power of a reverser is the power to gather any information and succeed at any task on the "first" try. Short-term reversers can travel anywhere they want, bypass almost any security, and practically read people's minds with without them ever being aware that it happened (as illustrated by the quote above). Long-term reversers are much less effective at gathering information in the short term, but they have an information-related ability that is potentially even more dangerous: if there is any information that they will <em>ever</em> learn, they might already know it. 

Short-term reversers usually display enormous skill in manipulating people. Because they gain so much experience with how people respond to different actions, they often know just the right thing to say without even using their powers.

A careless short-term reverser is easy to identify by the fact that they succeed at everything they try. Of course, you shouldn't rely on this, because a short-term reverser can easily hide by intentionally failing at certain things. Fortunately, another part of their ability is less easy to hide: they tend to stumble or become disoriented during their replacement events, because the body they return to isn't in the same position as the body they return from. A person who is very fortunate and can easily get help from others might only be a luck manipulator, but if they also stumble frequently, it is strong evidence of a short-term reverser.

Some short-term reversers are a rare variation who can bring back not only their mind and memories, but also their body and possessions. Such reversers can essentially teleport any distance in an instant, and instantly acquire objects from almost anywhere. Since they can't duplicate objects, any object they bring back disappears from its original location. This gives them additional special strategies: they can remove supports from structures, or even break an object and then take pieces of it back to make it break spontaneously in the past. This type of reverser is theoretically much more dangerous: imagine falling into a pit as the ground disappears under you, or walking past a building and having a ton of bricks fall from the roof onto your head. However, in practice, any short-term reverser who wants to kill a non-time-traveler can do so. And having these extreme abilities makes it much more difficult for the time traveler to hide. They can't avoid getting a reputation for teleporting and having objects move strangely around them, and they must eat enormous quantities of food to replenish the energy their body spends in their alternate futures.

Long-term reversers can't be spotted in the same ways that short-term reversers can, because they have too few replacement events to be recognizable as a pattern. Instead, you can identify long-term reversers by the fact that they have unusual knowledge of future events and spend lots of time and effort planning for them. Long-term reversers collect so much knowledge and so many experiences that, even if they're very careful, they can't always keep track of which knowledge came from the current timeline and which knowledge came from their alternate futures. This is especially evident in their relationships with other people: they may treat someone they just met as an old friend.

<h4>Counter-Strategy</h4>

For short-term reversers, the most important question is how well you can resist their "mind reading" abilities. If their limit is only a few seconds, then at least you will know when they have had the chance to interrogate you. If their limit is longer than that, it gives them enough time to step out from behind a corner, say something to you, observe your reaction, and reverse back to before you even saw them.

Theoretically, you could just hold a poker face no matter what they say to you. However, you not only need to hide your thoughts &ndash; you need hide the fact that you have something to hide. If an experienced short-term reverser starts investigating you in earnest, you have already lost. Your best bet is to develop a consistent cover story that is as uninteresting to your enemy as possible. For instance, you could spend most of your time complaining about something that your enemy doesn't care about, and use that as a response to almost any question. If the reverser has never met you before, you might be able to make them think that you show everyone a poker face normally, but you must remember that the reverser can also learn about you by questioning other people who already knew you. Anything you plan to fake in front of the reverser, you should also fake in front of everyone who might interact with the reverser.

Never answer emails promptly. Always wait out your enemy's time limit before responding. It doesn't matter who the emails say they're from &ndash; your enemy can easily access other people's email accounts if they want to. Don't write down any of your plans, and don't reveal them to anyone who your enemy might have contact with. Don't store any weapons in any place that your enemy would even think of looking, and remember that your enemy can search an entire room in a single instant without anybody noticing.

Short-term reversers quickly learn that they can do any unreasonable thing they want, just to find out what happens. For instance, a short-term reverser might jump off a cliff just to see what's over it. If you see your enemy doing something like this, make sure you act just as shocked as you normally would be. If you're an especially good actor, this can even be an opportunity to trick your enemy. You could rush into danger to "save" them, knowing that it's all going to be reversed anyway. However, it's generally better to simply make yourself as inconspicuous as possible.

When it comes to your actual attack, there are two possible strategies. The first one, and almost always the correct one, is to kill them instantly before they are even aware of your presence, such as while they are asleep. The second is to wait until they use their abilities to the limit, which makes them momentarily vulnerable because they can't go back any further. In order to pull this off, you not only must notice one of your enemy's replacement events, but you must also correctly guess that your enemy has returned from their maximum distance into the future, not only partway. This second strategy is never the one you want to plan on, but it may sometimes be useful if you don't realize that your enemy is a reverser until the middle of a complex battle.

In the case of long-term reversers, try to estimate how many timelines they have experienced previously. You're never in the first timeline; in that one, the reverser is indistinguishable from anyone else. If you're lucky enough to be in the second timeline, your chances are very good. In the second timeline, the worst-case scenario is that you already attacked the reverser in the first timeline and they are expecting it. But even in this case, you probably didn't use the same <em>kind</em> of attacks that you would use against a known time traveler.

The more timelines they've seen, the more likely it is that they've already seen you attack them, probably multiple times. If they were your enemy since before their first replacement event, the likelihood is almost certain. If you only decided to attack them because of an action they took after their first replacement event, you could be so lucky that this is the first time they've tried that action, and thus the first time that you attack them.

Generally, a time traveler who knows you're coming is an almost unbeatable foe. However, against a long-term reverser, you have a special advantage: you get multiple attempts. If you win in any of the timelines, you win for good. The main difficulty lies in making sure that you don't use the same strategy every time, since you don't remember your previous attempts (and your enemy does). You need to change your strategy a lot based on your enemy's slightly different actions. To do this, take advantage of the butterfly effect by rolling dice or flipping coins as an important part of your planning process. (Don't use a deck of cards. It's too easy to shuffle them in a nonrandom way.) Keep using the dice to refine your plan all the way up until the moment you strike &ndash; to avoid the case where your enemy keeps returning to the moment after you finalize your plan, but before you strike.

Needless to say, against a luck manipulator, this is the worst thing you could possibly do. Investigate first and make sure you know all of your enemy's powers before making plans to attack them. You will usually (but not always) have plenty of time for your investigation. After all, if your enemy intends to take action against you first, they will usually do it by going back as far as possible and making their move when you're not prepared for a time traveler yet.

If that does happen, the only thing you will observe is that you are being attacked by someone who suddenly gained great future knowledge. However, even though they have prepared for you, this is often a fight that you <em>can</em> win &ndash; they would only choose to do this if you were a serious threat to them in the future. If you survive a fight like this, things may become much more urgent. The person who attacked you may only be an agent of the time traveler, rather than the actual time traveler, so there may soon be follow-up attacks.

As with short-term reversers, there are some special strategies that you can use if you already know that your enemy is going to reverse some things that happened. In the case of long-term reversers, these strategies can be much more sophisticated. If a long-term reverser is unsuccessful at one of their major goals, they will eventually go back and try again, but they may continue the failed timeline for a while to gather information. If you discover that your enemy is doing this, consider planting information that may mislead the time traveler and give you an advantage in the next timeline, in case they go back before you succeed in killing them. If this timeline has turned out badly for you, you might even be better off abandoning your attack and focusing entirely on influencing the next timeline.

There is an often-retold legend of a time-traveler-hunter who killed a long-term reverser through an especially elaborate scheme. On the day he met the reverser, she gave him a message that she had memorized. She claimed that he had told this to her in the future, and that he had promised that it would convince his past self to cooperate with her plans. The message did seem very convincing &ndash; until he noticed that it contained a personal duress phrase that he had never told to anyone else. When he examined the wording closer, he found a coded message from his future self, listing her vulnerabilities and instructing himself to play along until he found an opportunity to kill her.

This story, though it may potentially be true, is not meant as a model to be repeated, but as an inspiration to what strategies may be possible. The same trick is unlikely to work twice, but if you are always thinking of new ideas, you just may come up with something that will work.



<h3>2.2: Paradox Cloners</h3>

What happens if you go back in time by two minutes and tell yourself not to get in the time machine? For paradox cloners, the answer is simple: neither of them gets in the time machine, and both of them continue existing.

Anyone who has learned basic world history knows how dangerous paradox cloners can be. As we all know, the entire scientific colony on the asteroid Ceres was destroyed in an instant by a single cloner. If a cloner of the same type were to appear on Earth, Earth's population could be destroyed as well &ndash; or worse. Any sign of paradox clones should be treated with the greatest possible caution. Fortunately, most paradox cloners have limitations that would prevent them from causing such a destructive event. 

This form of time travel most commonly functions as follows: Suppose a cloner attempts to return from time Beta to time Alpha. If there's something in the way at time Alpha, nothing happens. Otherwise, the universe resets to time Alpha, and a clone appears at time Alpha. This general process has many variations. Before you confront a cloner, there are some important questions to ask. 

Question one: Where can the clones appear? "Device-bound cloners" must create some type of "receiver device" before any clones can appear. In some cases, each receiver device can only receive one clone. In other cases, a receiver device can receive many clones, but the rate is still limited by the fact that each clone has to step out before the next one can appear. "Free-moving cloners" can return from any location they reach in the future, and arrive at the same location in the past. (Don't ask how "same location" interacts with relativity and so on. The physicists are still working on that.) "Teleporting cloners", the rarest type, can return to any location they choose, no matter where they started.

Question two: When can the clones appear? Some cloners, like most reversers, have a limited total distance they can go back in time. Others are "keyed" to a specific moment, so they can go back to that moment no matter how much time passes after that. In both variations, it is sometimes (but not always) possible for the cloner to use more power to force themselves back further than normal.

Question three: What happens when the cloner tries to appear inside a solid object? All cloners can displace a certain amount of matter (e.g. air) when they return, but they don't all behave the same way when that limit is exceeded. "Safe arrival" cloners who attempt this find that their power simply doesn't function. "Weak arrival" cloners still disappear from the future, but fail to reappear in the past. "Forced arrival" cloners always appear in the past, possibly causing an explosion when two objects are forced into the same space.

<p>(In the special case where the original cloner <em>does</em> still try to go back and become the second clone even in the second timeline where the clone was already there, the original cloner disappears without changing the past. Effectively, it behaves as a "weak arrival" cloner, regardless of what type it is normally.)</p>

The Ceres cloner was of the free-moving, time-keyed, and forced-arrival types. Historians still disagree on exactly what happened, but the most widely accepted theory is as follows: While the cloner was still experimenting with her power, she accidentally cloned herself into the same place as one of the other scientists, killing both of them. Unwilling to accept what happened, she repeatedly tried to go back in time again and prevent it, but she had already gone back to the earliest possible time, so it wasn't possible to reverse the arrival of the fatal clone. Each time, she failed, and only ended up creating more clones and more problems. When the colony was crowded with hundreds of clones, the scientists started realizing the danger, but by then, the task of convincing each and every clone to stop trying was impossible. The only thing that could stop the runaway clone pile-up was for every clone to die before they had the chance to use their powers. This happened, just as we observed from Earth: the moment she got her powers, the asteroid colony exploded under the pressure of many overlapping bodies, and millions of dead clones went spiraling into space. The only mercy was that the destruction was confined to the asteroid, because no shuttle to return to Earth was available at the time.

<h4>Strengths and Distinctive Traits</h4>

Paradox cloners are, naturally, the most likely type of time traveler to be seen in many places at once. It is very difficult for them to use their power without leaving large numbers of duplicates around.

Logistics quickly become an issue. They can clone food and water, but their power does not provide for waste disposal. Beginner paradox cloners usually create huge batches of clones initially, but after realizing the issues involved, they go back as far as possible and strictly limit the number of clones they make after that. They often kill or imprison any previous versions of themselves when they go back, either to hide the existence of clones or to prevent the older version from creating more clones without the newer version's knowledge. Cloners who choose this path are very similar to long-term reversers.

The most difficult type of cloner to fight against, however, is a cloner who efficiently cooperates with their clones. Smart cooperative cloners keep dozens of "backups" &ndash; clones that hide and don't use their powers unless the main group is attacked in some way. A single cooperative cloner can become like an entire community of long-term reversers who not only watch out for each other, but also have unlimited material resources.

<h4>Counter-Strategy</h4>

There are no surefire techniques for dealing with smart cooperative cloners, <em>in general</em>. However, among all types of time traveler, they are also the most likely to have specific limitations or weaknesses to their power. 

If you can track down all of the clones, killing them all simultaneously is sufficient. This may be difficult, but backup clones have at least one special weakness when it comes to hiding: they all have the same habits, so if you find one, it may be easier to find the others.

If the cloners are a type that can supercharge their power to go back to before the times when any of the current clones appeared, then any of them can go back and prevent the creation of any of the others. In this case, it may be possible to trick at least one of the clones into doing so. There are countless ways to do this, but we list a few possibilities below.

1. Make it look like some of the clones have secretly betrayed the others. When the others learn of this, they will go back to prevent the creation of the traitors &ndash; the hope is that they won't investigate too long, for fear that the traitors will go back first. This won't destroy the whole group, but they will be more cautious about creating extra clones next time, which will give you an advantage in the next timeline.

2. Make it look like an important event happened just after the first appearance of any clones &ndash; an event that they would want to go back and a change in some way. Identify which clone is chosen to go back and fix it, then plant a bomb on that clone. If you're lucky, the bomb will explode in the past and kill all the clones who are alive at that time.

If you can't use any of the strategies above, this is the one case where futilist thinking is arguably justifiable: if you don't attack, the clone community may remain stable, but if you attack and miss even a single backup clone, that clone may expand into a bigger and more dangerous community just to protect itself. However, provoking the group may still be useful, from a certain point of view. The larger and more active a group becomes, the more likely it is to attract the hostility of powerful organizations with their own time travelers and other abilities.


<h3>2.3: Consistent Coilers</h3>

We have left this, the most mind-bending form of time travel, for last.

<h4>Strengths and Distinctive Traits</h4>

If a consistent coiler never encounters any of the counter-strategies this book discusses, their abilities are mind-bogglingly powerful. A consistent coiler can, for instance, carry out an elaborate mission, then go back and give themselves a report before they even set out, giving themselves every detail that they need in order to be successful. Having received such a report, the coiler knows their plan cannot fail &ndash; else, why would they have reported that it succeeded? 

As if unlimited future knowledge and the guarantee of success weren't enough, the coiler can even provide assistance to themselves along the way. If they ever end up in trouble, which is unlikely, they can return to bail themselves out later. Unlike any other type of time traveler, they have a built-in way to take safeguards against their own death: they can habitually rendezvous with themselves in an obscure location, and only set out from there if they see themselves return safely.

If you suspect that your enemy is a consistent coiler, don't even think about fighting them yourself unless you have already established the defenses described later in this book (or otherwise been specifically trained to fight consistent coilers). Report the matter to someone who is already trained, and keep a low profile. Training yourself when you already have some involvement with a consistent coiler should be a last resort.

<h4>How It Works</h4>

<div style="position: relative; left:-0.5em; float: left; width: 30%; margin:0.9em; padding: 0.5em;box-shadow:0.3em 0.3em 1em black;"> Eli's note: This warning is for the fictional audience, who lives in a world where time travel exists. You, who live in the real world, can safely continue reading. </div>

Detailed knowledge about this type of time travel can literally be a memetic hazard.

<strong>DO NOT CONTINUE READING THIS BOOK UNLESS YOU ARE WILLING TO RISK YOUR LIFE IN THE FIGHT AGAINST CONSISTENT COILERS.</strong> If you stop reading now, your existing misconceptions may protect you.

<strong>If you do decide to continue, DO NOT STOP READING UNTIL YOU REACH THE END OF THIS SECTION.</strong> If you read only partway, you will learn how to attract the enmity of consistent coilers, but not how to protect yourself against them. The longer you hold only partial knowledge, the greater the risk that you will use the techniques incorrectly by mistake.

Reversers and paradox cloners, although they defy our conventional concept of <em>time</em>, do not defy our concept of <em>causation</em>. With those powers, causation is <strong>acyclic</strong> &ndash; an event in the "future" can influence an event in the "past", but no two events can influence <em>each other</em>. There are no loops.

Because of this, we can sort all events based on which ones can cause which other ones. This puts all events in an order which we call <strong>causal time</strong>. Causal time cannot be reversed. Our conventional notion of time, which <em>can</em> be reversed by powers, we will now call <strong>historical time</strong>. When a reverser uses their powers, historical time goes backwards, but causal time continues going forwards.

For centuries, physicists believed that consistent coilers function based on a form of <strong>cyclic</strong> causation. The theory claimed that somehow, outside of time, the universe forms stable time loops, which allow for events to cause each other without paradoxes. Many versions of this theory were debated. However, none provided a satisfying explanation of how the universe would choose <em>which</em> of the possible loops to use.

Today, we know that consistent coilers do <em>not</em> have cyclic causation, just as a coil is not a closed loop. The power of a consistent coiler, one could say, is the power to coerce the universe to behave <em>as if</em> causation could be cyclic.

In order for this to be possible, the power of a coiler is more complicated to activate than most other supernatural powers. Most powers are activated by a mental action, either consciously or unconsciously. The user mentally specifies the target, then the power takes effect immediately.

The coiler power is also activated mentally, but unlike other powers, it must be activated twice, in two separate ways. The moment when a coiler seems to travel back in time is actually the <em>second</em> activation, and does not work except to carry out a "time loop" that was created by the other ability. Because of this, we call the second ability the <strong>actualization power</strong>.

The first ability is the <strong>imagination power</strong>. Whenever a consistent coiler imagines a way they may use their ability, it creates a possible future. One may think of this possible future as a sort of computer simulation of what might happen. The simulation functions exactly like real life, with two exceptions. One, it contains one or more <strong>arrival events</strong>, corresponding to the ways the coiler imagined themselves arriving from the future. The copies who arrive do not yet have any actual future knowledge &ndash; they have only experienced what the coiler first <em>imagined</em> they might have experienced. Two, if any copy of the coiler (including the original) uses the actualization power in the simulation, that copy does actually disappear into the "past", which records a <strong>departure event</strong>.

The "past" that they disappear to is not actually the past of the same simulation. Instead, after the first simulation, there is a <em>second</em> simulation, which is where they arrive. This process repeats many times. In each subsequent simulation, the arrival events are based on the departure events from the previous simulation.

In order for the imagination power to ultimately be successful, the simulations must <strong>converge</strong>. The idea is that each simulation refines the previous one, based on the additional details that the coiler brings back in time each simulation. After a certain number of simulations, the departure events must (almost) exactly match the arrival events from the <em>same</em> simulation. If this happens, the final simulation becomes real. Otherwise, the imagination power simply fails to do anything.

<h4>How Coilers Use Their Powers</h4>

"It should be possible to form a complete theory of human behavior, i.e., to predict from the hereditary and environmental givens what a person will do. However, if a mischievous person learns of this theory, he can act in a way so as to negate it. Hence I conclude that such a theory exists, but that no mischievous person will learn of it. In the same way, time travel is possible, but no person will ever manage to kill his past self." &ndash; Kurt Gödel

No mischievous person can be a consistent coiler &ndash; or rather, no person can use the imagination power without first making themselves sufficiently non-mischievous. The key to understanding how coilers can use their abilities is to understand what it means to be "sufficiently non-mischievous".

Consider Jane, a hypothetical inexperienced coiler. Jane is sitting alone in a room at 10:00, watching TV. Jane says to herself, "I'm going to wait until 11 o'clock, then go back to right now and tell myself what was the last thing I saw on TV." Jane looks to see if a copy of herself is going to show up, but nothing happens.

Jane didn't think through the plan well enough. She did activate the imagination power, but in the first simulation, she got curious about what would happen if she didn't go back. There were no departure events in the first simulation, so the process ended with no effect. Or maybe she did go back in each simulation, but always got curious about what would happen if she didn't repeat what she remembered herself saying from the first time around. The simulations ran out without ever becoming similar enough.

Later, after learning more about her powers, Jane says to herself, "I'm going to see a copy of myself arrive from the future, listen to her tell me what's going to be on TV in an hour, wait quietly with her for an hour, go back to right now, tell myself the same thing I told myself, then wait quietly for another hour until she goes back." This time, a copy of Jane arrives right on schedule.

In the second example, Jane had a specific plan and was willing to stick to it. As a result, minor variations between the simulations did not cause Jane to do anything significantly different in each simulation. Thus, they were able to able to converge, so Jane was able to create a "time loop".

Ironically, the easiest way to be able to use coiler powers is to completely misunderstand them. The majority of coilers believe that they are somehow "obligated" to avoid creating paradoxes, and they are scared that the universe will do bad things to them if they don't try to keep time consistent. As a result, they play along with almost <em>any</em> variation that ends up appearing in one of the simulations, so they are very likely to reach convergence. However, even though they try to use the powers to benefit themselves, they are just as likely to converge to a result that is bad for them. They are even likely to carelessly imagine themselves using very bad plans, then feel obligated to go through with them. We call this type of coilers "time worshipers", and they are easy to defeat.

Coilers are much more effective if they don't assume they have to make everything consistent. They don't necessarily understand all the rules, but in effect, they are content to allow some simulations to fail, if they don't accomplish their goals in those simulations. When they do find that their goals are being accomplished, <em>then</em> they try to keep things consistent. That way, they can keep imagining different strategies until they come up with one that works, and then that one becomes real.

The most dangerous of all coilers are the ones who understand the system, and can manipulate the system to let them gather information in the first few simulations, then apply it to create a consistent plan in the later ones. When a coiler appears to pull information out of thin air, by receiving it from themselves and then returning to tell it to themselves, it is often this type of coiler. The information did not come from thin air, but instead, it came from the forgotten earlier simulations. However, this is a tricky strategy. When amateur coilers try to do this, they often <em>imagine</em> themselves receiving specific information that is not actually accurate, and so they end up trusting information that just came from their own imagination rather than from actual investigations.

Although most coilers are time worshipers, it is never safe to assume that your enemy is a time worshiper, even if they seem to be one.

<h4>Basic Counter-Strategy</h4>

The most basic counter-strategy is to disrupt the simulations, so that they never converge. Imagine that a soldier is spying on Jane through a window. The soldier intends to watch and see if the second Jane appears, and if one does, to shoot the original one at 10:30. In this scenario, each simulation will always be different from the last, so they can never converge. When Jane notices that it isn't working, she might try imagining various other things, and might eventually succeed by imagining that the second Jane would appear hidden behind the dresser. At that point, Jane could infer that the cause of the failure came from someone watching at the window.

Note that most coilers aren't aware of how this process works. Coilers cannot recognize that their imagination has succeeded until they observe its physical consequences. If it fails, they gain no information about why it failed. However, if they understand the process well enough, they can still gain a great deal of information by imagining a variety of strategies to see which ones work and which don't.

By making the right plans, you can be like the soldier, but disrupt a much wider variety of possible simulations. If you are planning to respond to a coiler's actions by causing a paradox on purpose, you will cause the failure of any imagination that would lead to you noticing the coiler do those actions. The most severe disruption would be if you planned to cause a paradox if you noticed any time travel at all. DO NOT DO THIS. Although it would hinder coilers a great deal, it would not stop them from finding success by imagining that they will kill you before you cause any paradoxes.

Causing a paradox on purpose can be done in many ways, not just by killing the coilers. It is wise to collect future knowledge that can be used to cause paradoxes. For instance, if a coiler brings back a photo of a unique object in the future, destroying that object in the present would cause a paradox (unless the coiler used their future knowledge to bring back a falsified photo on purpose). The ideas that in any simulation where they bring back the photo, you destroy the object, so they don't have the photo when they depart &ndash; and in any simulation where they don't bring it back, you don't destroy the object, so they do depart with the photo. If possible, gather your future knowledge from less experienced instances of the coiler, who are more likely to give away reliable future knowledge carelessly.

It is sometimes possible for the coiler to tell themselves about the earlier iterations, figure out that you're trying to cause a paradox, and circumvent your attempt in some way. If possible, it is best to create inconsistencies that the coiler won't notice.

Note that you can never actually cause a paradox in the main timeline. However, you could think of it this way: you never really know whether you are in the main timeline or in one of the simulations. Your choice of whether to cause paradoxes in the simulations determines whether the imagination power succeeds. 

I can now explain the reason for the memetic hazard warning above. Reading this book increases the chance that, in some alternate future, you will attempt to cause paradoxes. A very smart coiler might be able to identify you as the source of the paradoxes and kill you on purpose. A less smart coiler would just try different plans until one succeeds, and might stumble upon one that succeeds because it kills you by accident. 

The key to fighting against consistent coilers is to cause paradoxes for actions that harm you, while tricking your enemies into taking non-paradoxical actions that help you.

<h4>Consistent Coiler Defense Networks</h4>

This book cannot hope to give a full description of how to organize or operate a Consistent Coiler Defense Network, given that most existing networks have a policies-and-procedures document that is longer than this book in its entirety. However, a basic overview is as follows.

A Consistent Coiler Defense Network is a loose-knit organization where no one, not even members, knows the entire membership list. Each member stays in regular contact with a dozen or so other members. If any member stops reporting in &ndash; perhaps because they were killed by a coiler &ndash; their contacts raise an alert and investigate. If they conclude that the disappearance was caused by a consistent coiler, they attempt to cause paradoxes. Thus, any attempt by a coiler to kill a network member is much more likely to cause a paradox, and thus much less likely to be possible.

<p>(If the system has too many false-positives, by reacting to disappearances that are not caused by coilers, it becomes more like the dangerous "always cause paradoxes" strategy. If it has too many false-negatives, by allowing coilers to kill members in a way that doesn't look like murder, the network risks being slowly wiped out. Choosing the right investigation rules is crucial, and each network does it in a slightly different way.)</p>

Establishing a new network is a risky process that should only be undertaken by someone who doesn't currently have the ill-will of any coilers. An active enemy coiler would find it much easier to simply kill the founding member(s) before they start recruiting.

A network spends most of its time in "defense mode", only reacting to threats against its members and not attempting to disrupt time travel on a larger scale. Once network members identify an enemy coiler, they watch that coiler closely, study their goals and behaviors, and start planning for their next move. Eventually, the members may go into "attack mode". In "attack mode", they start causing paradoxes selectively to steer the coiler into a trap.

<h4>Trapping a Consistent Coiler</h4>

The difficulty of setting a trap depends on how defensive the coiler is.

A low-defense coiler goes on missions without even checking in with their future self first. Low-defense coilers can be killed normally. They imagine going on the mission, the simulations converge quickly because they die in a non-paradoxical way, and then it happens.

A medium-defense coiler always checks in with themselves. If you use the same tactics against them, they just choose not to go on any of the missions where you would succeed in killing them. Against a medium-defense coiler, an effective strategy is to poison them just before they return, using a poison that has no antidote. They will be able to report in, but unable to imagine any strategy that leaves them alive after that.

A high-defense coiler checks in with multiple future versions of themselves on a staggered basis, including ones from weeks in their subjective future, if not months or years. Using a poison that takes months to show its effects might work, but usually, allowing a coiler to remain active for that long is unacceptable. The weakness of a high-defense coiler is that making all the required simulations converge is extremely difficult, and attacking a Consistent Coiler Defense Network while using high-defense coiler strategy is essentially impossible. The counter-strategy is to start causing more and more paradoxes until the coiler is forced down to a medium-defense level.

If you have access to very good mind control, a special strategy is available. Ambush the coiler and control them, then send them back to give a false report that their mission was successful. In the case of high-defense coilers, send them back however many times your enemy's protocol requires. Then have them return to you and submit to being killed. If you don't have mind control, it may be possible to approximate this strategy using shapeshifting or false memories, but not if your enemy has prepared for them.

If you use mind control, make sure you know whether you can maintain your control after the target goes back in time. If you can't, don't waste your advantage for nothing.



<h3>2.4: Long-Leaping Time Travelers</h3>

Neither paradox cloners nor consistent time travelers can go back in time by more than a decade, except under extremely rare circumstances. Any time traveler from that far in the future is almost certainly one of a special category: Long-leapers.

Long-leapers are technically the most similar to paradox cloners, in that they reverse time and then create a copy of their future self. However, they have special rules that have more in common with consistent coilers.

When a long-leaper attempts to travel into the past, the process begins with a series of simulations. Each simulation begins at the time the long-leaper intends to arrive, and continues until the present (the time when the long-leaper is attempting to depart). The only simulation that will become real is one where the end result is almost identical to the world the long-leaper is departing from originally.

The only difference between the simulations is that random events happen differently in each one. The total number of simulations is <em>very</em> large, so it creates the possibility that at least one simulation will have a great many coincidences allowing history to reach the same result, even with the interference of the long-leaper. In effect, a long-leaper is surrounded by a powerful luck-manipulation field that suppresses the butterfly effect and influences the universe to reach the same present that the long-leaper set out from. If the long-leaper's plans are especially disruptive to history, the most likely result is that they will suffer an improbable accidental death as soon as they arrive. (For instance, "let's go back 70 million years and look at some dinosaurs" is safe, but "I'm going to bring back this bomb and blow up the Earth in 1980" would likely result in the bomb malfunctioning, or worse.) Long-leapers can return from the past, but they must return to just after they embarked, not before.

<h4>Counter-Strategy</h4>

If you find yourself fighting against a long-leaper in the long-leaper's <em>present</em>, you have an ordinary opponent. They have a few special abilities, but none of them are exceptional. Depending on the exact rules of their ability, they may have any of the following options:
<ol> <li>To gain extensive, accurate knowledge of history and geography without leaving any evidence.</li>
<li>To spend days developing plans in the past without taking any time to plan in the present.</li>
<li>To teleport from place to place instantly, by going back in time and then returning in a different place.</li>
<li>To travel into the future, making themselves vanish (and thus be impossible to attack) for a period of time.</li></ol>

If, on the other hand, you are in a long-leaper's past, the strategic considerations are much different. Go ahead and fight the long-leaper &ndash; it is usually an easy task. Since the long-leaper cannot do anything that would change the future too much, their actions are very limited. The more they antagonize people, the more they disrupt history. If a long-leaper has picked a fight with you, the most likely result is that they are swiftly defeated and escape back to the future (or die). Their luck manipulation actually works in your favor. You are free to make complex schemes and use risky strategies, just as if you had a normal luck manipulator on your side. (However, you must consider the usual caveats of that ability as well.)

Your one disadvantage is that your enemy may have powerful technology and weapons from the future. Consider trying to steal them and use them to your advantage. Don't bother trying to keep them too long after your encounter, however: The luck manipulation will make sure that they soon stop working and are forgotten. Similarly, if you want to make sure that the long-leaper dies rather than simply escaping, you need a foolproof plan, because the luck-manipulation field will prefer that the dead body isn't left in the past as evidence. One possibility is to poison them, so that they only die after returning to the future.

Being attacked by a long-leaper is normally extremely rare, but if you find yourself being repeatedly attacked by misguided long-leapers, you can take an additional preventative measure. For instance, you can decide to start attempting to cause "paradoxes" when they attack you. This type of paradox is much easier to create than the ones for consistent coilers. After all, in the original timeline, no long-leapers attacked you. So all you need to do is to make grand announcements and permanent records about each long-leaper who attempts to attack you. If this is your plan, the most likely result of any attack by a long-leaper is that the long-leaper fails before you even become aware of them.

The most well-known example of this, of course, is Adolf Hitler. Although he was attacked by many time travelers in his youth, he mysteriously stopped being attacked by time travelers near the height of his power, so it is likely that he used this strategy.

One might ask, "if they can't actually change how things turn out, how do we know that they attacked at all?" We can know about it under two circumstances: firstly, some long-leapers over the last century have left journals of their plans to go back and stop Hitler, then disappeared. Presumably, the reason they disappeared is because they were executing their plans, although of course, we have no proof dating from Hitler's time. Secondly, we have hard evidence of attacks by long-leapers from the distant future. We must assume that we will eventually lose all records of this evidence, so that none will be left by the time those attackers came from.

Certain time travel historical societies have a policy of only keeping long-term records of long-leapers who die while trying to kill Hitler, and not of those who survive and return to the future, in order to make the luck manipulation more likely to let them survive. Other societies, particularly exterminationist ones, only keep records of the ones who <em>survive</em>, to make them more likely to die. However, these societies occasionally change leadership, and the new leaders often expunge the records kept by the old ones, rendering the decision moot.


<h3>2.5: A Brief Note on Oracles</h3>

The power to predict the future has many similarities to the power to travel into the past. Time travelers, like oracles, often have knowledge of possible futures. Oracles, like time travelers, are rarely seen taking actions that have bad results.

Oracles come in two types. Those who can see many possible futures are similar to personal time reversers. Those who see only one future, the one which will actually happen, are similar to consistent coilers. Oracles have no counterpart to paradox cloners, since oracles can never duplicate themselves.

Oracles are typically less dangerous than time travelers, because oracles can make mistakes, their planning time is not unlimited, and they can never be in two places at once. (Take note, of course, that "less dangerous than time travelers" is a very weak statement.) Consistent-oracles, compared with consistent coilers, have no other advantages to make up for these weaknesses. Reverser-like oracles, on the other hand, have a major advantage over true reversers: they have no difficulty at all in predicting and avoiding their own deaths. If you make any normal attempt to kill a reverser-like oracle, the oracle will have already predicted alternate futures until they find one in which they survive.

Most reverser-like oracles have a limit to how far they can see into the future. Like with most types of time traveler, this may allow you to trap or poison them, so that they wouldn't be aware of the attack until after they can no longer do anything about it.

Some reverser-like oracles have another weakness as well: they are unable to predict their own future predictions. That is, in each potential future such an oracle sees, the oracle never makes another prediction. Thus, one way to kill them is to wait until you see them using their power, then strike immediately. Since you only kill them immediately after they make a prediction, they never see you kill them in any of their earlier predictions &ndash; only the last one, which hopefully doesn't give them enough time to react.

If the oracle is aware of this strategy, they could theoretically make a habit of predicting what happens if they <em>pretend</em> to receive further predictions. If you suspect that your oracle would do this, you must fall back to a different strategy, such as leading the oracle into a trap. However, unlike a short-term reverser, an oracle must spend a certain amount of real time to make each prediction. Thus, they are much less likely to take obscure defensive measures such as this.

<h2>Appendix: Time as a computer program</h2>

We here provide an approximate implementation of the time travel rules in JavaScript. It is not intended to run on any <em>actual</em> computer, but it serves to illustrate the exact rules and potential interactions of various time travel powers.

This implementation also simplifies physics by using a series of simulation steps ("ticks") rather than a continuum, and gives no consideration to relativity.

'''

program ='''

<pre> <code class="language-javascript">

function present (history) { return history [history.length - 1];}

function tick (history) {
  history.push (deepcopy (present (history)));
  /* Do physics on the new moment of history,
  possibly calling some of the time travel functions below. */
}

function reverse (history, person, target_time) {
  var transferred_mind = person.mind;
  while (history.length > target_time + 1) {history.pop();}
  history [target_time].find_person (person).mind = transferred_mind;
}

function paradox_clone (history, person, target_time, destination, ability_info) {
  var area = history [target_time].find_area (destination);
  if (area.density() > ability_info.density_limit
       && ability_info.arrival_type === "safe") {return;}
  if (area.density() > ability_info.density_limit
       && ability_info.arrival_type === "weak") {
    present (history).erase_person (person);
    return;
  }
  while (history.length > target_time + 1) {history.pop();}
  if (area.density() > ability_info.density_limit) {area.insert (person);}
  else {area.replace (person);}
}

function imagine (history, person, ability_info, imagined_arrivals) {
  /* In our current model, the imagination power cannot be nested.
  That is, you cannot use it during your own simulations.
  If you could, it wouldn't be clear how the actualization power
  decides which simulation to apply to.
  
  However, that would imply that many consistent coilers have a
  moment of vulnerability at the end of each successful simulation,
  because they can't have any duplicates or future knowledge if they
  haven't been able to imagine further than that yet.
  
  We have not observed such moments of weakness, so further research
  is clearly needed. */
  if (person.current_coil_simulation) {return;}
  
  var start = history.length - 1;
  function simulate (arrivals) {
    /* Note: it's not technically correct that these arrivals
    are only a local variable in this function.
    They need to be recorded in the history state instead.
    Otherwise, if (for instance) a reverser goes back 
    to before one of the arrivals,
    the arrival doesn't happen the second time.
    We write it this way for now for ease of understanding. */
    arrivals.sort_by (when);
    person.current_coil_simulation.next_arrivals = [];
    for (var which = 0; which < arrivals.length; ++which) {
      var arrival = arrivals [which];
      while (history.length <= arrival.when) {
        tick (history);
      }
      var area = present (history).find_area (arrival.where);
      if (area.density() <= ability_info.density_limit) {
        area.insert (arrival.who);
      }
    }
    while (history.length <= start + ability_info.time_limit) {
      tick (history);
    }
  }
  person.current_coil_simulation = {next_arrivals: imagined_arrivals};
  for (var which = 0; which < ability_info.max_simulations; ++which) {
    var last_result = present (history);
    while (history.length > start + 1) {history.pop();}
    simulate (person.current_coil_simulation.next_arrivals);
    if (difference (present (history), last_result)
         < ability_info.inconsistency_limit) {
      present (history).find_person (person).current_coil_simulation = null;
      return;
    }
  }
  while (history.length > start + 1) {history.pop();}
}

function actualize (history, person, target_time, destination) {
  if (person.current_coil_simulation) {
    present (history).erase_person (person);
    person.current_coil_simulation.next_arrivals.push ({
      who: person, when: target_time, where: destination});
  }
}

function long_leap (history, person, target_time, destination, ability_info) {
  var area = history [target_time].find_area (destination);
  if (area.density() > ability_info.density_limit) {return;}
  var start = history.length - 1;
  var old_history = deepcopy (history);
  while (history.length > target_time + 1) {history.pop();}
  
  /* Like the coiler implementation, this arrival can be erased by a reverser.
  We don't believe this should be possible, but further research is needed
  to determine the exact interaction. */
  area.replace (person);
  
  /* For this to find a working result, max_simulations needs to be HUGE,
  somewhere between a googol and a googolplex. For simplicity, we will assume
  that JavaScript's numeric type can handle such numbers. */
  for (var which = 0; which < ability_info.max_simulations; ++which) {
    history [target_time].random_seed = which;
    while (history.length <= start) {tick (history);}
    if (difference (present (history), present (old_history))
         < ability_info.inconsistency_limit) {
      return;
    }
  }
  
  /* If no possible simulation was found,
  the time travel attempt simply fails. */
  history = old_history;
}



</code> </pre>
'''

table_of_contents = []
used = {}
def thing (match):
  fragment =utils.format_for_url (match.group (2))
  while fragment in used: fragment = fragment +"i"
  used [fragment] = True
  table_of_contents.append ('<a class="table_of_contents table_of_contents_' + match.group (1) + '" href="#' + fragment + '">' + match.group (2) + '</a>')
  return ("<bigbreak>" if match.group (1) == "2" else "") +'<a id="' + fragment + '">' + match.group (0)+ "</a>" 
contents = re.sub(r"<h(.)>(.*?)</h.>", thing, contents)
contents =re.sub(r"<TOC>", "".join (table_of_contents), contents)
contents = utils.auto_paragraphs (contents) + program

posts [0] ["contents"] = contents
