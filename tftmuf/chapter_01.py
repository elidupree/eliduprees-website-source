#!/usr/bin/python3
# -*- coding: utf-8 -*-

from post_contents_utils import *
from tftmuf.definitions import *

posts = [
{
  "title":"The Future They Made Us Forget, chapter 1",
  "auto_paragraphs": True,
  "head":head,
  "chapter_title": "Your Mind Control Is No Match for My Cloud Computing",
  "contents": '''
  
Before I start telling you what I remember, I'd like to be clear about one thing. I don't want you to think of me as "<em>the real</em> Marvin Fitzroy", or "<em>the original</em> Marvin Fitzroy", or anything like that. Your brain will want to, because I'm the one you know about – the one telling you the story. But time travel doesn't make those distinctions. Even the Marvins that don't exist anymore, they were just as real as I am.

And because this is <em>my</em> version of the story, I can only tell you the part I know. For Kayla, it started six years earlier, when the scientists first started using her. For the scientists, it started another seven years before that, when they published the paper they didn't realize was about time travel. For Ontoh and Nochli, it started at a time that's harder to explain – several months in the future, or thousands of years in the past, depending how you look at it.

But for me, it started when I was hired by the Whitney University Neuroscience Department.

Even then, they were obviously more than just an academic department. My office wasn't on-campus – it was in the old Riker Hospital building, which I'd thought was abandoned when Riker moved to a new, modernized facility four years earlier. But now, my new employers owned the entire building. And my paycheck came from a company called NeuroSci Innovations, which no one had ever heard of. I should have known there was something underhanded going on. But I was in a hurry to get a new job – I'd just been laid off at a dying tech startup. I was short on cash, and my new pay was good. <em>Suspiciously</em> good. Even a prestigious research university like Whitney wouldn't normally have the budget to pay competitive, market rates for a computer graphics engineer. But that's what they were paying me. And I didn't say no to it.

An abandoned hospital wasn't a normal workplace for a software engineer. Even the commute was desolate – this part of ?????city [something-burg?] had never really recovered from the hurricane a few years back. People had lived in these destroyed homes once, but after the evacuation, most of them had seen the writing on the wall. Or in this case, the writing by the state scientific commission, about the severe flooding that would soon be commonplace, in these low-lying zones close to the ocean. Just about the only people left were the old-timers who would rather die in the homes they'd grown up in… and the few poor souls who were still in denial about climate change.

The hospital was as dismal as its surroundings. In the parking lot, a power pole sported a ragged flyer from the City Council, asking residents to report any sightings of urban coyotes or coyote scat, and warning them not to leave food out in the open. The building itself towered seven stories above, square and anonymous. The brick face could've been anything – a hospital, an office building, a prison.

Inside, it had only been partly re-colonized by its new owners. Shiny new surveillance cameras were retrofitted onto aging walls; new electronic locks put the upper levels tantalizingly off-limits.  The wide-open lobby, our only view of all seven floors, revealed scattered bits of activity upstairs. Some of the upper hallways saw the bustle of doctors and grad students, doing their unknown research; other halls sat dark and unused, as abandoned as they'd ever been. On the second floor, where I worked, a respectable attempt had been made to clean up the treatment rooms and convert them into offices, but in many places, racks of unused medical equipment had simply been pushed into back corners to gather dust.

Getting set up in the makeshift office was an adventure in itself. First of all, every single computer in the office had a physical blue-green color filter glued over the monitor. My new boss told me we were working on making an animated color pattern for some kind of psychology research, and the color filters were for "ethics". The pattern could theoretically have psychological effects on anyone who saw it, so the scientists didn't want to expose anyone except the intended test subjects. At least, that's what they'd told my boss. So we were doing all the prototyping using color-swapped versions of the actual pattern.

"What happens if you look at it?" I asked, curious.

"I don't know, probably nothing. But they're huge sticklers for ethics. I thought they had to be joking, but some of the other guys looked at it, and they were fired before I got back from my lunch break. And they put the blue things on the screens the same day, so now you can't see it even if you put the right color codes in. <em>Ethics</em>…" He smiled and shook his head. And at the time, I laughed along with him. But in hindsight, it hits differently. It feels silly to have scoffed at that level of caution, given the much stricter precautions we needed later. And even though I'd thought he was charmingly cynical, neither of us had caught the actual lie: These scientists had never cared about ethics. To them, "ethics" was just a convenient excuse – an excuse that they could use whenever it meant doing what they wanted to do anyway, and put away whenever it didn't.

The Pattern itself didn't mean much to me at first. It was just some wavy stripes, almost like a bar code but curvy and irregular, all in blue and green – although of course those weren't the real colors. My programming work was about making the waves move around in various patterns. Sure, I sometimes got distracted watching the motion – but it was less "hypnotic spiral" and more "1990s screensaver".

"What are the real colors?" I asked him once.

He chuckled. "Don't forget, I'm a programmer too. I know how programmers are. If I tell you the real colors, you'll want to look at it yourself. Call me a killjoy, but I'd rather keep my job." His smile wavered, as he glanced at the surveillance camera watching over us. Quietly, he added, "Pro tip, this Dr. Fuller doesn't know how to work with programmers. If he gives you something easy that he doesn't know is easy, just say 'I'll work on it' and make it take two days. Then you can use the time to work on the hard things he doesn't know are hard. Don't do anything too fast, he'll just raise his standards. Just keep your head down and give him what he expects, and it'll be a cushy job."

<bigbreak> 

But if I have one flaw, it's this: Once I get curious about something, I can't look away from it. Maybe if they had never installed all the locks, they could have kept their secrets. Maybe I would have treated it like any other boring job. But if there were locks, there was something to keep hidden. What was all this security for? What was the Pattern, really? What were they researching? I couldn't resist the mystery of the scientists secluding themselves on the locked-off upper floors. Even more intriguingly, the basement levels were secured with full steel security doors, greeting you as soon as you got out of the elevator. What was so important to hide?

So, to look inside, I hacked the cameras.

I wasn't a genius hacker, but in truth, very few security breaches are works of genius. The typical breach starts with a careless mistake – a company cutting corners to save a quick buck, a programmer writing a bug that <em>usually</em> doesn't break anything, a sysadmin leaving a secret in a public-access folder. And it ends with someone noticing.

I started by googling the brand name of the security company. It was easy to find: Every lock and camera proudly displayed their logo, <em>PanoptiLock</em>. They sold expensive, high-tech security equipment, and their marketing looked pretty impressive. They had police chiefs recommending them; they had videos where people tried to break their locks with sledgehammers and hacksaws, and failed. If you were a normal person, and you suddenly had a million dollars and needed to secure a building, you would find PanoptiLock.

But I wasn't a normal person. I was plugged into the security community. Before long, I had found the YouTube videos – reviews by people who <em>actually</em> knew security, amateur teardowns of PanoptiLock products. And the reviews… well, they weren't terrible. PanoptiLock hadn't made every mistake in the book. But they had made enough.

Every PanoptiLock camera shipped with the same default password. At work, after I'd seen the reviews, I idly tried that default password. I didn't really expect it to work – whoever installed them should have changed the password before connecting them to the network. But they hadn't. It worked.

With very little fanfare, I was "in".

When you find a vulnerability like this, you have two choices. What you're <em>supposed</em> to do is report it to whoever is responsible, so they can fix it. What you're <em>not</em> supposed to do – what I did do – is exploit it yourself. But I couldn't resist. I wasn't trying to be some sort of citizen-investigator, finding what they were up to, I was just doing it because I was curious. Because I <em>could</em>. What Reginald would later call "a profoundly amoral decision".

I didn't dare look at the cameras on work time, at first. Instead, I wrote a little script to download all of the recordings and save them on a terabyte USB drive. At home, in my studio apartment, I had plenty of time to review them, on the big screen of my gaming PC. I skipped back and forth in the videos, trying to find the interesting parts, conversations that would reveal the juicy details.

But no matter how much data you have, the hard part is always "how to understand it". And despite hours of looking, I was little closer. The upstairs cameras saw workers and offices and medical equipment, chemistry labs where I overheard technical work beyond my understanding; the basement cameras saw a huge, concrete-floored workshop, with bulky construction equipment, even a forklift parked near one wall. But what was the purpose of it all? I hadn't seen the Pattern a single time; had anyone even mentioned it?

Little did I know that I had already seen the Pattern, already been affected by it.

I thought I just had to make my search more systematic. I made a spreadsheet, and started writing down what was happening in each room, so I could get a sense of the big picture. Over the coming days, I made it a whole little project, using motion-detection software to find the interesting parts of the videos, and image classifiers to write down what was there. If you don't know what an image classifier is, it's one of those AI tools that they use at places like Google – you put in an image, and it gives you a bad guess about what it's a picture of. Nowadays, if you know a bit of programming, you can just <em>download</em> a "pre-trained model" and classify thousands of images overnight. And if you have a bit of money, you can pay a "cloud service" to run the same program on dozens of computers at once, in a datacenter somewhere, to get it done much faster. So that's what I did.

Image classifiers sometimes give weird outputs, but what I learned was a different kind of weird than I expected. First of all, they caught Reggie, one of the doctors, being in two places at once. I thought the cameras must have had a glitch. Go ahead and laugh – you already know it was time travel. But at the time, my brain refused to make the connection.

But second… they told me about the children.

If it wasn't for the image classifiers, I would never have noticed. I would have just glanced past those rooms and assumed there wasn't anything there. Even after they said "child on bed", I still just assumed the classifiers were wrong, like they often are. But the spreadsheet made the difference. I had planned to write a few words of summary for every camera; only those dozen rooms were still blank. I told myself it should be easy to finish; I sat at home staring at the images, wondering what made them get classified as children, when there obviously weren't any children in the pictures. Or, as I eventually began to wonder – why my brain couldn't explain what they were instead.

[I was afraid/distressed that my brain was failing]. In desperation, I sent one of the photos to a friend – a gaming buddy who always answered my messages right away – to ask him what he thought it was. But he never replied. He couldn't see it either. I was on my own.

My project became an obsession. What <em>was</em> this place? Belatedly, I began to do my due diligence about my new employer. I searched for news on "NeuroSci Innovations"; there was almost nothing. I searched the address of the building, but all the results were from when it was still Riker Hospital. I searched the name of Dr. Fuller, the man in charge, but I didn't find much besides a profile of him winning some accolade at the University, sixteen years ago. Whatever this place was, I sure couldn't find any <em>innocent</em> reason why they might have a dozen "children in beds" upstairs, children you never saw leaving the building. And indeed, I was getting more and more suspicious that those were actually children up there. Was this some kind of secret, evil mental hospital? Was it human trafficking?

But still, I hesitated. I didn't want to believe that could be happening – not <em>here</em>, right in the city where I'd grown up. And what could I do, anyway, if I was right? Report them to the police? How could I explain it?

I don't know what I would have done, if things had gone on this way – if Kayla hadn't made her move first. I wish I could say that I was a hero, that I would have kept trying until I figured out a way to do something. It hurts to admit what was more likely: I would have kept agonizing about what to do, putting off the decision, until the sense of mystery wore off and I found a way to rationalize inaction to myself. I would have gone on with my life, telling myself there was nothing I could have done.

If that was one of my moral failings, I'm grateful that I was never tested on it. For better or for worse, I became a hero the other way: by being in the right place at the right time.

When I came in for work that Saturday, I didn't know how important that day was going to be – how it was the day we would later call <em>Day One</em>, the day that would change the course of human history. I was still just there to do my job. There was a bug in my code that I couldn't stop thinking about, and I'd come in for overtime to work on fixing it. Maybe it wasn't good for my work-life balance, but it was too stuck in my brain for me to have a nice weekend otherwise. Plus, it was nice to be alone in the office. No one would notice if I took some time to check how far I could hack the security equipment – which I'd been getting bolder and bolder about.

Coming in on a quieter day changed something else, too. Normally, the lobby was bustling in the morning, as [various workers came in, Dr. Fuller greeting the important ones and generally working the lobby, with his authoritative smile (smile that put you at ease, but made it clear he was in charge?), close-trimmed beard, crisp button-down shirt, the epitome of "business casual". But with fewer people there, I became conspicuous enough to receive his attention.

["Ah there, enjoying your work?" Before I had got my brain organized to answer [put on the spot because he was so important],, with a chuckle, he continued, "Of course you are, of course you are. You're contributing to <em>very</em> important research, you know." His tone made me feel appreciated; it wasn't until I rewatched it that I noticed he had only congratulated himself, and maybe didn't even know my name.]

[This was an opportunity; I worked up my courage. Trying to sound innocently curious, I said, "remind me, what exactly are we researching?"]

["It's very cutting-edge research you're supporting. Very technical"]

"Try me. I'm a tech guy, I can understand a lot of things."

[He rattled off an explanation, but it went right over my head ("my eyes glazed over", but the internal version of that?) I found myself [switching back in from being zoned out, just as he was finishing the explanation] He clapped me on the shoulder. "Keep up the good work."]

But as I got up to my office, I had the presence of mind to check the camera recordings. [I had really wanted to learn the thing, I shouldn't have just zoned out; now I looked back because I wanted to get a second chance to understand it] [The sound quality wasn't good/there was background noise, but I got a good view of his face. In hindsight, I re-watched it more times than I thought; eventually picked up the awareness of the] ????? brazenly smug smile [that I could barely remember from the first time] ????? He <em>knew</em>. He knew full well that his words would be deleted from my memory. He had told me the truth, practically laughing in my face, knowing I still wouldn't be able to do anything about it.

My heart pounded. [seized with horror at the proof that this wasn't just something weird going on with my brain – he actually knew about it and was using it against me.] Frantically, I scanned through the other cameras near the lobby, seeing if any of them had a closer view.

And that's how I saw Kayla for the first time.

<bigbreak>

This is what happened on Day One.

The ?????phorin Experiment was scheduled for 11:00 AM. An hour in advance, at 9:56, two assistants unlocked the room where Kayla was being held, and told her she was to be taken to the experiment room. She complied.

Kayla was already physically weak and stumbling, and the assistants knew this. This gave her the excuse she needed. At 10:01, as they escorted her into the experiment room, she "accidentally" bumped into one of them, knocking them sideways into a medical cart. Their lapse of control was brief but impactful. The cart, with its wheels already locked, toppled; vials of medicine shattered on the floor.

Once the assistants had strapped Kayla into the fMRI machine, there was a hasty discussion. Dr. Fuller would be very angry, they agreed; it was imperative that this mess be gone before he learned of it. At 10:05, they agreed to split up – one to fetch replacements, the other to stay and clean. But as soon as the second assistant was alone, he realized he had no broom or dustpan to clear the broken glass. He glanced at Kayla; he must have known it would break protocol to leave her unattended. But she was fully restrained, lying motionless in the machine. Surely nothing would happen in just a few minutes. Surely Dr. Fuller's anger was a more urgent concern. This resulted in Kayla being left unattended for a total of six minutes, starting at 10:07. Only the room's security cameras could see her, and no one was monitoring them at the time – at least, not in the first timeline.

26 seconds from the moment the door closed, Kayla had fully freed herself from the restraints. Over the next 18 seconds, she scanned through the shelves, taking what she needed with frantic but efficient motions. By 10:09 AM, she was out the door. She didn't know the full layout of the building, but she knew what she was looking for: she sprinted down the hall, following the exit signs, knowing they would lead her to the stairs.

And that's where I came in. By sheer luck, the moment she ran past the fifth-floor lobby camera was the moment I was watching it, while looking for a camera with a better view of Fuller. Of course, at the time, I had no idea of what had just happened before that. All I knew was what I could see on the camera. And what I saw – the way I first interpreted it – was a frightened, teenage girl, wearing nothing but a hospital gown, holding a scalpel in front of her like a weapon. In the twelve seconds she was in view, she entered the lobby on the fifth floor, looked quickly around her, and crept to the nearest stairs, then disappeared downwards. My mind jumped to an explanation: she was a captive, trying to escape the building. I was almost right. Right in the ways that mattered.

I've done a lot of things I'm not proud of, but I'm proud of how I reacted in that moment. My worst fears about this place were realized, and I knew that if I didn't take action – immediately – then I would never forgive myself. The girl couldn't see where Dr. Fuller was standing, and if she tried to exit on the ground floor, she'd be in plain view of him and two security guards. She would be recaptured, and God-knows what else. I couldn't just let that happen.

I didn't dare let myself be seen on the cameras. At 10:10 AM, I turned off every security camera in the building, stood up, and sprinted for the stairs.

It was lucky that Kayla couldn't take the stairs at full speed. I wasn't exactly athletic, and I just barely got there ahead of her, panting as I reached second-floor door to the stairwell. By the time I cracked open the door, she was just half a flight above me.

"This way, quick!" I gasped, trying to keep my voice gentle. "I can help you."

And then I looked up, and saw her properly.

Her face was gaunt, barely more than skin and bone. One arm clutched a tablet computer to her chest, with a few smaller objects bundled in a closed fist. At her other side, a bony, trembling hand still gripped the scalpel, as she stood poised on the steps above me, ready to fight or run the moment I proved to be a threat. But if I'd been expecting her to panic when I approached, my expectations were soon disproven. She held still, quickly calculating how much to trust me. My first glimpse of the ruthless intelligence that defined her.

"Why are you helping me?" she asked. Not disbelief. A demand for information.

"I – I only just realized this place is holding people against their will!" I hissed. "Of course I want to do something about that!" I was starting to panic myself. Kayla still wasn't moving, and I had no idea what to do if she wouldn't trust me. "Listen, someone's going to come up the stairs anytime now, I saw it on the cameras! Come with me, I can hide you in my office – then we'll have time to figure out –"

Kayla let out a short breath, coming to a decision. She climbed down the stairs – not fast, but as fast as she could, balancing on unsteady feet while she held the tablet tight to her chest.

When I watched that moment again in the security footage, the contrast was striking. Me, the slightly pudgy, thirty-five-year-old white man in a t-shirt, completely out of his depth, awkwardly holding open the door; and Kayla, a head shorter, the gown drooping over her emaciated shoulders, squeezing uncomfortably close to get past me. I remember looking down, seeing her fist clenched tightly around the handle of the scalpel, realizing that I might meet a very bloody end if I betrayed her.

I talked quickly as we hurried back to my office. "You need to get out of the building, right? I can look at all the security cameras – we can see if anyone's watching, so we can get out without anyone seeing us – and then I can call the police –" But something in her eyes told me she didn't think the police would save her. "Or, I mean, I could call someone you trust – or I could drive you anywhere you want, I have my car –"

"It won't work," she said.

"What?"

Her words came quickly, low and urgent. "None of that would work! I can't run, they're always waiting for me, as soon as I get away. I need to find their…"

Kayla kept explaining, for ten seconds, then twenty, before I noticed what was happening. If it hadn't been for what I'd already seen, I would have just let her keep talking, not realizing anything weird was going on. But I was starting to recognize it. Her words were plain English, they fit together in order – but my brain simply wasn't making sense of them. Just like with Dr. Fuller.

"I'm sorry," I interrupted, "I can't understand what you're saying –"

I had been afraid that she wouldn't know what I meant – afraid that I would have to spend precious minutes explaining. But the instant I spoke, I knew that she had understood. The look that blossomed on her face wasn't confusion or frustration – it was <em>fear</em>. She knew what was coming. No matter how long she explained these things – no matter how desperately she needed me to know them – I would never understand them. And then her time would run out.

Or, as I would soon understand, she knew that her only choice was to commit a terrible violation.

"You – you're really not in on it," she said.

"In on what?!"

"On the –!!" A rush of words flooded through my head, with no more meaning than before. And she knew instantly that it wasn't working. She couldn't answer my questions; she could only steel herself to do what she was about to do. "Damn it! I didn't bring this to use it on an innocent person!" she said tightly. "But I need you to understand!"

And then the purpose of the tablet she'd brought was revealed. With a lurching motion, she laid it on my office desk, the screen facing me, showing a grid of buttons. Before I could read them all, her fingers reached out and tapped the button labeled OVERSTIM.

The next few minutes were a horrifying blur.

On some level, deep in my mind, I understood what my eyes were staring at. It was the animation I'd been working on. The only difference was the color, no longer blue and green, but purple and white. But somehow, the colors reached deep into my brain, gripping my deepest instincts, holding me in a dreamlike state where I couldn't form a coherent thought. I only remember a few fragments – the waves of color speaking to me in voices of infinite authority and reassurance, my mind scramblieng to obey but the rules turning to mush when I tried to understand them. I felt like a small child again, teachers yelling at me for forgetting my work, trying to follow but getting lost every moment I looked away. The Pattern whisphered on and on, noise layering over noise, every moment blotting out the last.

I do remember what it felt like as I "woke up" – my head spinning, still half in the nightmare, a stinging sensation in my arm, my brain frantically digging through half-formed memories for any idea of where I was, what had happened to me. I found myself sitting in my chair – had Kayla put me there? – the Pattern still swirling on the screen, I could see it normally now – Kayla crouching beside me, speaking quickly – the injector still in her hand – I looked back at my stinging arm –

"Is this some kind of mind control?! Did you <em>inject</em> me with something?!!" My voice rose into a shriek – I shoved myself away from her –

But then, my mind caught up with the words she had been saying.

"– a time machine, they have a time machine. Tell me when you can understand me. They have a time machine. They have a time machine. Tell me when you can understand –"

And it all fell into place. Images I'd seen on the cameras flooded back into my mind, as if I was seeing them the first time. The purple-and-white Pattern painted all over the holding-cell walls, commanding my brain to forget what it saw – Fuller gloating about how he could use it – Reggie being in two places at once – "A time machine –" I gasped "– the machine in the basement –"

Kayla explained as quickly as she could. "You were already being mind controlled. Everyone here is, everyone but the doctors in charge. What I did is, I broke the control. The overstim, the ?????cyanosol injections, they're what they tested on me, they're why I can resist it. Everyone else, you can talk about time travel right in front of them and they just stare past you –"

<em>Biiiing!</em>

I jumped – but it was just a message arriving on my work computer, an awful coincidence of timing. Except, of course, it wasn't a coincidence, because time travel was involved.

<em>Hey Marvin, it's me, Marvin. You need to download this and watch the first video, ASAP.</em>

"Uhhh…" I said, glancing between the message and Kayla.

"Open it!" hissed Kayla, comprehending faster than I did. "It's from you, right? You trust him, right?"

"…Right!" With shaking fingers, I clicked to download the attached zip file.

When your body is in fight-or-flight mode, the time it takes a computer to unpack an archive feels like forever. It was only 18 seconds, but I spent those 18 seconds with my eyes glued to the screen, cursing progress bars everywhere. The moment it was done, I jumped straight to the first file I saw, 01_WATCH_THIS_FIRST.mp4.

Like many an unedited, amateur video, it began with an awkward close-up of the person making it, as she clicked the record button and then backed away to position herself better for the camera. The people in the video were us: Kayla standing, Marvin sitting next to her. They were in an office not-so-different from my own, no doubt somewhere in this very building. But a small window behind them revealed a night sky. When I later checked the file's "Date Created", I learned that they had begun recording at 3:56 AM – over 6 hours ago.

The Kayla in the video was dramatically changed from the Kayla beside me. The desperate look was gone from her eyes, a bit of fat back in her cheeks, standing tall and proud, with an honest-to-God <em>rifle</em> on a sling over one shoulder. She was dressed in an oversized men's jacket and jeans, marred only by splatters of dried blood, which I could only assume were not her own. But despite her pride, there was still a look of deep exhaustion on her face.

"Oh God, how do we say this to them?" muttered the Kayla in the video, dead tired, a voice of resignation. She glanced to the side, at my own double – the glance of someone hoping someone else will take charge, so they won't have to explain things themselves.

But my double could not help her. Whatever our duplicates had been through, Kayla had endured it, but Marvin had been emotionally destroyed by it. He had a hollow, haunted look; he hadn't shaved in days; and the moment Kayla looked to him, he broke down completely. He sank down in his seat, sobbing into his hands, unable to speak.

Video-Kayla let out a short breath and pulled her eyes away from Marvin, a quiet acknowledgment that she was on her own. Reluctantly, she looked back at the camera – at us.

"Listen," she said. "We messed up. We caused a paradox, and pretty soon, we're going to cease to exist. And if you don't want the same thing to happen to you, here's what you have to do."


''',
},
]
