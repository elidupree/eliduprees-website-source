#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

import exmxaxixl

bright_orange = '<span class="dialogue bright_orange">bright orange</span>'
bright_red = '<span class="dialogue bright_red">bright red</span>'
bright_green = '<span class="dialogue bright_green">bright green</span>'
dark_green = '<span class="dialogue dark_green">dark green</span>'
pure_blue = '<span class="dialogue pure_blue">pure blue</span>'
pale_blue = '<span class="dialogue pale_blue">pale blue</span>'
light_pink = '<span class="dialogue light_pink">light pink</span>'
deep_purple = '<span class="dialogue deep_purple">deep purple</span>'
cyan = '<span class="dialogue cyan">cyan</span>'

vc_pages = [
  {
    "xcf_base": "title-2",
    "transcript": [
      (0, 'A cover page.'),
      (500, '''TITLE: Voldemort's Children'''),
      (1700, 'Three people stand, lit harshly by '+bright_orange+' light. In the center is Harry Potter: heavyset, hunched over, zir black hair wild. To the right, Luna Lovegood: very thin, with long loose blond hair, with zir wand tucked behind zir ear and an exaggerated expression of interest. On the left, Draco Malfoy: also thin, reserved, with zir arms behind zir back, zir hair short and neat, and zir face slightly flushed.'),
      (3200, 'TITLE: A Harry Potter fanfic by Eli Dupree')],
      "annotation": '''<p>And so it begins.</p>

<p>I've been planning <i>Voldemort's Children</i> since September of last year, when I started analyzing the original series from a neurodiversity perspective. <i>Voldemort's Children</i> is an "Alternate Universe" fanfic - a reimagining of the story in which I explore one possibility of how events could happen in a world where we don't gloss over the implications of neurological difference in general and Harry's abuse as a child in particular.</p>

<p>I'm going to leave it at that for the moment, but I'll sometimes use these annotations to talk more about the purpose and structure of the story.</p>

<p> &ndash; Eli</p>'''
  },
  {
    "xcf_base": "ch1_p1_2",
    "chapter_start": 'Chapter One: The Boy Who Killed',
    "transcript": [
      (0, '''Hermione Granger stands in a room labeled "Auror Offices". {The Aurors are elite law enforcement agents.} There are bookshelves along the wall. Granger has zir hair tied back, wears a long dark coat, and has very reserved mannerisms. Nymphadora Tonks enters the room. Tonks is more easygoing than Granger, wears a shorter, lighter coat, and has short spiky pink hair. Tonks's speech is drawn somewhat messily in a <span class="dialogue TONKS">mild purple</span> color, and Granger's is more formal and drawn in a <span class="dialogue GRANGER">mild blue</span>.'''),
      (55, 'TONKS: Granger, you called?'),
      (980, 'GRANGER: Yes... I will speak with the prisoner &ndash; Attend me.'),
      (1695, '''TONKS: I can't get over it...'''),
      (2000, 'They go to a long spiral staircase. Tonks walks down the stairs, while Granger flies down by magic, leaving a trail of '+pure_blue+' magical energy.'),
      (2000, 'TONKS: All those people outside are yelling for his head... and we just go down...'),
      (3640, 'TONKS: and ask him questions.')],
    "annotation": '''<p>By the way, I have a built-in way to mark pages with content warnings, to warn users about content that might be triggering &ndash; or content that they might want to avoid for any other reason. (If you're unsure what trigger warnings are about, <a href="http://fuckyeahtriggerwarnings.tumblr.com/">this tumblr is an excellent introduction</a>.) I'm going to try to mark any page that has potentially triggering material, but I'm not a very good judge of what might be triggering, because I don't get triggered myself (in fact, I basically never get <em>any</em> undesirable emotional effect from seeing <em>any</em> visual image). So if you see a potential trigger that I haven't marked, please tell me.</p>

<p>The same goes for any other web accessibility issue. I care about this stuff, so if you '''+exmxaxixl.a('e-mail me')+''' with an issue, I <strong>will</strong> do my best to fix it.</p>'''
  },
  {
    "xcf_base": "ch1_p2_1",
    "transcript": [
      (0, 'A partial map of the Ministry of Magic Department of Magical Law Enforcement shows Granger and Tonks descending from the Auror Offices to the Interrogation Cells.'),
      (0, '''TONKS: I've got everything in order... The prisoner in cell 5...'''),
      (340, '''There's a barred cell door and a window blocked by '''+cyan+' magic.'),
      (900, 'TONKS: The truth potion...'),
      (900, 'There is a table with two bottles of a whitish liquid on it.'),
      (1080, 'TONKS: The warrant to use it...'),
      (1080, 'There are two sheets of paper on the table, with writing on them. One of them has the seal of the Ministry of Magic on it.'),
      (1250, '''GRANGER: You know I don't like to use that unless it is necessary.'''),
      (1680, 'TONKS: Better safe than sorry! The glass is just waiting for your tap. Then he can see and hear us.'),
      (2570, 'GRANGER: Good.'),
      (2990, '''Granger taps the cell's magical window, and the '''+cyan+''' magic clears away from the middle of the window, so it can be seen through.'''),
      (3730, 'GRANGER: And now... Harry Potter...'),
    ],
    "annotation": '''<p>If you're a <i>Harry Potter</i> fan, you might be thinking <q>Aha, ze wrote 'truth potion' for the benefit of people who aren't familiar enough with the series to know the name 'Veritaserum'</q>. If you're a bigger fan, you might be thinking "But Veritaserum is as clear as water, and that potion isn't!" That's right! The real reason I don't say "Veritaserum" is because this is actually a modified version of Veritaserum that Granger invented - it is similar, but its action is unaffected by the Veritaserum antidote, which is a distinct tactical advantage.</p><p>A more cynical person might speculate that Granger invented it to circumvent legal restrictions on the use of Veritaserum, but the law usually refers to truth potions in general, and as the head of the Auror Office, Granger can get the necessary warrants easily.</p>'''
  },
  {
    "xcf_base": "ch1_p3_2",
    "transcript": [
      (1000, '''A single large image of Harry Potter, in a rigid chair. Harry's arms are bound to the arms of the chair by metal bands. Ze is barefoot and wearing a ragged grey tunic, zir hands are clenched, and zir hair is in disarray. Ze has a zigzag scar on zir forehead, and another, vertical scar at the left edge of zir mouth. There are dark shadows around zir eyes, and ze looks angry. Harry's speech is drawn almost as a scribble, with many jagged lines, in <span class="dialogue HARRY">bright red</span>.'''),
      (1000, '''<span class="dialogue HARRY">HARRY: Ge' on wi' it... Grangeuh.</span> {Get on with it, Granger.}'''),
      (3130, '''TITLE: Chapter One'''),
      (3480, 'TITLE: The Boy Who Killed'),
    ],
    "annotation": '''<p>Ah, Harry Potter.</p>

<p>How do you represent the speech of a character who pronounces words in a non-standard way? I hesitate to say <q>mispronounces</q>. If ze physically can't make the sounds that other people can make, is ze making an <em>error</em> by speaking?</p>

<p>I've chosen to represent it with a jagged, irregular writing style.</p>

<p>On this page, I've also chosen to misspell the words Harry speaks. Imagine if I did that on every page. The culture around us is full of prejudice against people who don't speak words the way they <q>should</q> be spoken. Others often mock them and disregard their opinions. But <i>Voldemort's Children</i> makes it natural to pay attention to what Harry says. I could put my readers in the position of taking someone seriously when they spoke misspelled words, which could be a good thing.</p>

<p>However, misspelling things would also make the comic harder to read. Ultimately, I decided that it wouldn't be worth the cost. As an author, I want my work to be as easy to read as possible. But I'd like to take this moment to remind you, as a viewer, that if you only view things that have been made easy for you, you may be missing things that are important.</p>''',
  },
  {
    "xcf_base": "ch1_p4_1",
    "transcript": [
      (0, '''Granger and Tonks are looking down into Harry's cell.'''),
      (0, '''GRANGER: I'm not here to force tactical information out of you this time, Harry. I just want to learn about you. To understand you.'''),
      (682, '''HARRY: Rubbish! You think you understand me bloody well enough already. Don't think I've forgotten your answer to that speech Fudge made...'''),
      (1480, '''We enter a <span class="dialogue HARRY">narrative frame</span> in which Harry describes past events. In the past, Harry is sitting with two silhouetted figures, listening to a magical wireless radio.'''),
      (1600, 'HARRY: I was on the run then, but I still had a wizarding wireless...'),
      (1722, 'WIRELESS: &ndash;terrupt with an important message from the Minister of Magic, I repeat, the Minister of Magic himself will now address&ndash;'),
      (2700, '''We enter a <span class="dialogue WIRELESS">narrative frame</span> in which we have a direct view of the Minister of Magic, Cornelius Fudge, making zir speech. Everything in this narrative frame is black-and-white. Fudge is standing at a podium on a raised platform, addressing an audience of at least 50 people, and probably more that we can't see. Fudge speaks in an excessively formal way.'''),
      (3090, 'FUDGE: Witches and wizards of Britain... It is my most regretful duty to inform you of the events of this morning... *ahem*... The notorious killer, Harry Potter, has made an attack on Hogwarts School of Witchcraft and Wizardry.')],
    "annotation": '''<p>You know you're reading an Eli Dupree comic when you enter two nested narrative frames on the same page.</p>''',
  },
  {
    "xcf_base": "ch1_p5_1",
    "transcript": [
      (0, 'Fudge continues zir speech. Everything on this page is in black-and-white.'),
      (0, 'FUDGE: Potter and an unknown number of his allies invaded Hogwarts Castle just after midnight last night, massacring students and releasing Fiendfyre in the Hogwarts dungeon.'),
      (0, 'FUDGE: The following students are missing and presumed dead, their bodies destroyed in the cursed fire: Millicent Bulstrode, Vincent Crabbe, Daphne Greengrass, Draco Malfoy, Graham Montague, Pansy Parkinson, Charles Warrington, Blaise Zabini.'),
      (1400, 'FUDGE: The headmaster is injured by alive. We will now observe a moment of silence for the deceased.'),
      (1850, 'Time passes in silence, represented by an hourglass in a spiral.'),
      (2233, '''FUDGE: Potter and his allies, whoever they may be, have made themselves the enemy of wizarding society &ndash; an enemy such as we have not seen since the downfall of the self-styled Lord Voldemort over ten years ago. The older generations among us remember the name of Harry Potter as our salvation, but today, we have seen that Potter and his allies... are Voldemort's children.'''),
    ],
    "annotation":'''<p>When Fudge says <q>The downfall of the self-styled Lord Voldemort</q>, ze is referring to when Voldemort tried to kill Harry as an infant.</p>
    
<p><i>Harry Potter</i> fans will remember Fudge being afraid to say <q>Voldemort</q> out loud. In <i>Voldemort's Children</i>, I'm not including the issue of being afraid to say the name. Why not? Because it doesn't add to the themes I'm trying to develop. (By comparison, in <i>Harry Potter</i>, that convention <em>does</em> add to a major theme &ndash; namely, the theme of overcoming one's fear. <i>Voldemort's Children</i> sneers at that theme.)</p>''',
  },
  {
    "xcf_base": "ch1_p6_1",
    "transcript": [
      (0, 'Fudge continues zir speech. The scene is still black-and-white.'),
      (0, 'FUDGE: A representative from the Auror Office will now brief you on our progress against this Dark enemy.'),
      (0, '''<span class="dialogue grey">PAST GRANGER: Thank you, Mr Fudge. Sonorus!</span> {"Sonorus" is the incantation for a spell that makes the caster's voice loud, as one would use to make a speech. The spell glows '''+pure_blue+'''.}'''),
      (760, '''PRESENT HARRY: You weren't Head of Office yet, but everyone knew you would be.'''),
      (891, '''PAST GRANGER: With all respect to the Minister... The Auror Office believes that Potter is not a Dark Lord, but merely a self-aggrandizing serial killer motivated by petty revenge against those he believes have wronged him. Have we become so content since Voldemort's fall that <em>this</em> is what we imagine it must be like to live in a Dark Lord's shadow? Potter is running to hide from our Aurors even as we speak. In Voldemort's time...'''),
      (2620, '''We enter a <span class="dialogue grey">narrative frame</span> in which Granger describes a time farther in the past, when Voldemort was in power. Voldemort is a tall person in dark robes, with no distinguishing features except that zir mouth is always a flat, expressionless line. The top of zir head is obscured in shadow, so that zir eyes cannot be seen. Ze wears a '''+pale_blue+''' spiral object on a band around zir neck. Ze is followed by two animal companions: a '''+bright_green+''' snake and a black cat with '''+bright_orange+''' eyes. Zir wand is white, possibly bone or ivory. Zir speech is drawn in a very rigid style, with lots of straight lines and sharp corners, in a <span class="dialogue VOLDEMORT">pale green</span> color.'''),
      (2728, 'VOLDEMORT: Avada kedavra.'),
      (2728, 'Voldemort is pointing zir wand at two other people and casting the Killing Curse, illuminating them with '+bright_green+' light. One of them is hit. The other is running away.'),
      (3256, 'VOLDEMORT: Ha. Ha.'),
      (3762, '<span class="dialogue grey">PAST GRANGER</span> {continuing zir speech}: <span class="dialogue grey">...Aurors ran from <em>him</em>.</span>'),
    ],
    
    "annotation":'''<p>I'm pretty sure I've made Voldemort creepy enough.</p>
    
    <p>The timeline here can be a bit confusing. The presumed-dead students - who were in Harry's year or one year above - were still at Hogwarts. But Fiendfyre is an advanced spell, so the most likely time for the attack is in (what would be) Harry's sixth year. So how is Granger an Auror already? When did Harry leave Hogwarts to become a notorious killer? Why didn't Voldemort return at the same time ze did in the books? These questions will be answered in time.</p>''',
  },
  {
    "xcf_base": "ch1_p7_1",
    "transcript": [
      (0, 'PAST GRANGER: Voldemort sometimes killed more in one day than Potter has in his entire life. He did whatever he wanted, and no-one could stop him. He had torn his own soul into seven pieces and hidden them in the dark corners of the earth so that he could never be killed. The Killing Curse did nothing to him.'),
      (0, '''Voldemort stands with zir cat and snake, holding a black sphere, with seven white wedges surrounding zem. In all the images of Voldemort on this page, ze is still wearing the spiral object and still has zir face obscured.'''),
      (900, '''PAST GRANGER: He tortured innocent people for his own amusement...'''),
      (900, '''Voldemort stands over a person who is lying on the ground.'''),
      (900, '''<span class="dialogue VOLDEMORT">VOLDEMORT: Crucio.</span> {The incantation of the torture curse. The torture curse glows '''+bright_orange+'''.}'''),
      (900, '''<span class="dialogue grey">PERSON TORTURED: AAAAAAAAAAAAAAAAAAAAAAA</span>'''),
      (1050, '''PAST GRANGER: He had a Time-Twister and he pushed it to its limit. He did more damage to the flow of time than any witch or wizard since Merlin...'''),
      (1050, '''We get a closer look at the spiral object Voldemort has been wearing around zir neck. It is a small hourglass in a clockwise-as-you-move-inwards spiral. Part of the band is yellowish, but closer to the hourglass, it fades to '''+pale_blue+'''. Voldemort's hand is reaching down to manipulate it.'''),
      (1200, '''PAST GRANGER: Even his own followers were afraid of him. He had no mercy for the slightest failure or irritation.'''),
      (1200, '''Bellatrix Lestrange kneels before Voldemort. Lestrange has long shiny black hair and speaks in a jagged, <span class="dialogue LESTRANGE">yellowish-green</span> color.'''),
      (1200, '''<span class="dialogue LESTRANGE">LESTRANGE: Master, I've killed half the Wizengamot.</span> {The Wizengamot is the high court of magical Britain. }'''),
      (1200, '''VOLDEMORT: Half live? Crucio.'''),
      (1200, '''LESTRANGE: AAAAAAAAAAAAAAAAAAAAAAA'''),
      (2134, '''PAST GRANGER: And worst of all, no one knew what made him do it. He was an event without reason or cause. Even when a great Legilimens tried to look into his mind... {Legilimency is, approximately, the power to read minds. You usually need to be looking into the target's eyes to do it.}'''),
      (2134, '''Illustration: An unnamed Legilimens and Voldemort face each other. A ray of '''+light_pink+''' magical energy joins their eyes. The Legilimens is blasted by the energy.'''),
      (2134, '''PAST GRANGER: The resulting psychic backlash left her unconscious for weeks, and when she woke, she did not remember anything she'd seen.'''),
      (2629, '''VOLDEMORT: Ha. Ha.'''),
      (2950, '''The narrative frame of Past Granger describing Voldemort closes, and we see Past Granger on the platform giving the speech again, in black-and-white.'''),
      (2950, '''PAST GRANGER: Potter is none of those things! We know his motivations, and his weaknesses! We will apprehend him and he will stand trial like any other common crimin&ndash;'''),
      (3250, '''<span class="dialogue HARRY">PAST HARRY: Confringo!!</span> {The incantation of the Blasting Curse, which glows '''+bright_red+'''.}'''),
      (3250, '''The narrative frame of the wireless playing the speeches closes as Harry blows up the wireless. We are back with Harry and the two silhouettes. The silhouettes dive out of the way of the explosion.'''),
    ],
    "annotation": '''<p>Ah, the Time-Twister.</p>
    
<p>In the original series, there is a device called a <q>Time-Turner</q> that can magically transport you back in time by one hour. That has huge implications about the nature of the universe, and the books never specify its limitations. Logically, you'd expect them to be a huge issue &ndash; the Aurors would all have them, Voldemort would probably have one, and every important battle would be based on tricky uses of time travel.</p>

<p>I had three choices: I could justify Time-Turners, I could eliminate them entirely, or I could change them into something else. <a href="/blog/recommended-website-harry-potter-and-the-methods-of-rationality"><i>Harry Potter and the Methods of Rationality</i></a> takes the first option; it creates a consistent set of rules for how Time-Turners work and how they handle temporal paradoxes. I didn't want to do that, because this isn't a story about time shenanigans; it's more of a story about characters and their emotional interactions. So it was between eliminating Time-Turners and changing them.</p>

<p>I didn't want to eliminate them because I <em>really really liked</em> the symbolism of Hermione using the Time-Turner to take extra classes &ndash; it shows a lot of dedication to be willing to warp the very fabric of time in order to study harder. So I kept the object, but changed it. The Time-Twister doesn't send you back in time by an hour... it just gives you an extra hour, somehow, and no one's exactly sure how it works. You can use it go to two classes that are at the same time, but if you do, you won't remember which order you went to them in, and if someone follows you around, they'll come to both classes with you &ndash; so the Time-Twister doesn't just affect you, it affects everyone around you.</p>

<p>(Another reason I made Time-Twisters is that it means I don't have to worry too much about keeping a consistent timeline. If things seem inconsistent or anachronistic, they are! It's canon!)</p>''',
  },
  {
    "xcf_base": "ch1_p8_2",
    "transcript": [
      (0, '''The last narrative frame closes. We are back with Harry in the cell.'''),
      (0, '''HARRY: I heard what you said. Don't try to tell me one thing and everyone else another. You just want me to prove you right.'''),
      (700, '''GRANGER: Perhaps I was mistaken. It would not be the first time I have said or done something that I have come to regret. Tell me &ndash; why <em>did</em> you kill those Slytherin students?'''),
      (1340, '''HARRY: I won't tell.'''),
      (1463, '''We enter a <span class="dialogue GRANGER">narrative frame</span> in which Granger describes past events.'''),
      (1650, '''PRESENT GRANGER: You left messages with the bodies of your other victims.'''),
      (1650, '''Two scenes show dead bodies that Harry has labeled with bright magical writing. One says "TORTURED MUGGLES FOR SPORT &ndash; TORTURERS WILL DIE". The other says <q>TRAPPED AND SOLD ELVES &ndash; SLAVERS WILL</q> and a past version of Harry is busy finishing the sentence.'''),
      (1650, '''PRESENT GRANGER: Why not with these?'''),
      (2167, '''PRESENT HARRY: I won't tell!'''),
      (2288, '''PRESENT GRANGER: Your former professors say that many of these students had bullied you in classes...'''),
      (2500, '''Past Harry sits in class with two students casting nasty spells at Harry in class, while Professor Minerva McGonagall looks the other way and continues lecturing. McGonagall wears '''+dark_green+''' robes.'''),
      (2700, '''<span class="dialogue grey">DAPHNE GREENGRASS: Densaugeo! Ha ha ha!</span> {The incantation of a spell that makes the target's teeth grow unnaturally large.}'''),
      (2700, '''<span class="dialogue grey">GRAHAM MONTAGUE: Ha ha! Langlock!</span> {The incantation of a spell that makes the target's tounge stick to the roof of zir mouth.}'''),
      (2700, '''MCGONAGALL: The precise study of Transfiguration requires a departure from naive physical...'''),
      (2700, '''The narrative frame closes.'''),
      (3250, '''GRANGER: It seems natural to think&ndash;'''),
      (3250, '''HARRY: You think I killed them for revenge! I don't kill for revenge. I did it because I <em>had to</em>. And that's all I'm gonna say. Unless...'''),
      (3880, '''The "unless" fades into a yellowish color uncharacteristic of Harry's speech.'''),
    ],
    "annotation": '''
<p>You'd have to be a real <i>Harry Potter</i> scholar to remember what those spells do, but I've written their effects down in the transcript.</p>

<p>Transcripts serve the purpose of making the story accessible to as many people as possible. The most obvious use is for people who are vision-impaired and can't see the image at all, or people who can see the image but can't read the text in it. But that's not the only group who can benefit from transcripts. They are also helpful to people who have trouble interpreting the language of comics that I'm using &ndash; e.g. which things happen in which timeframe, what is dialogue and what is thoughts, and so forth. You could have trouble because you're unfamilar with the medium, or because of cognitive differences, or because I drew things in a confusing way (which I can't deny will happen sometimes).</p>

<p>Given all these different possible uses, I try to make the transcript explain all the relevant information from the image. A lot of websites have transcripts that repeat the words drawn in the image, but don't describe the pictures; I believe that's insufficient.</p>

<p>Of course, since this is a work of fan fiction, it has a lot of implicit references to things from the <i>Harry Potter</i> universe. I can't reasonably explain all of them. I will generally try to explain things in the transcript if they're obscure enough that a fair chunk of <i>Harry Potter</i> readers won't know them (e.g. if they're from the later books in the series). I'm not trying to make the story <em>entirely</em> accessible to people who haven't read <i>Harry Potter</i> at all, but luckily, most information from the <i>Harry Potter</i> universe is also on the Internet.</p>''',
  },
  {
    "xcf_base": "ch1_p9_2",
    "content_warning": "depicts physical bullying",
    "transcript": [
      (0, '''A shadowy metaphorical image of Voldemort looms behind Harry. Voldemort is grabbing Harry by the hair. Most of Harry's hair has fallen over zir face, so zir eyes are hidden. Voldemort and Harry speak in unison, in a mix of their graphical styles. (Physically, we're still in the interrogation cell, and Harry is speaking alone.)'''),
      (150, '''<span class="dialogue HARRYMORT">HARRY AND VOLDEMORT: Hey, listen. If you want to know about me. I'll tell you. I'll tell you things nobody but me knows. Things nobody but me should ever know. Just three rules... One, I tell it how I want. Don't you try to twist my story with your questions. Two, if you use that truth potion to get more out of me, it's over. Three... Give me back my god damn glasses.</span>'''),
      (3140, '''GRANGER: ...I accept your rules.'''),
      (3350, '''Granger transports Harry's glasses back onto Harry's face, using '''+pure_blue+''' magic.'''),
      (3320, '''HARRY: Now... maybe it starts when Lily Evans and James Potter died... or maybe it starts long before I was born... but I'm going to start with when I went to Hogwarts.'''),
    ],
    "annotation": '''<p>Thus ends chapter 1. I suppose I could have come up with a nice way to indicate the end of the chapter, like <a href="http://gunnerkrigg.com/">Gunnerkrigg Court</a> does, but I guess I didn't.</p>
    
    <p>I wanted to give Granger a more nuanced line to accept Harry's rules with, but I couldn't make it fit with the flow of the piece. Sure, I could have made the upper text smaller, but I don't think the atmosphere of this page would benefit from the level of nuance that Granger would try to introduce to the situation.</p>''',
  },
  {
    "chapter_start": 'Chapter Two: Castle of Gloss and Fear',
    "xcf_base": "ch2_cover_1",
    "transcript": [
      (0, '''We see a large image of Hogwarts Castle in relative darkness. It has many towers, but is not adorned or colorful.'''),
      (0, '''At the top is a banner which reads <q>DRACO DORMIENS TITILLARE COACTUS SUM</q>, which is Latin for <q>I am compelled to tickle a sleeping dragon</q>. (The motto of Hogwarts in the original series is <q>Draco dormiens titillandus numquam</q>, which means <q>Never tickle a sleeping dragon</q>.) The Latin verb <q>titillo</q> can also mean <q>provoke</q> or <q>sexually stimulate</q>.'''),
      (0, '''An huge image of Voldemort hovers over the castle, holding puppet strings which attach to the towers, as if the entire castle is Voldemort's puppet.'''),
      (870, '''Hermione Granger is flying on a broomstick over the castle, with zir wand out, shooting some kind of magic in Voldemort's general direction.'''),
      (2755, '''Rubeus Hagrid &ndash; a huge person, but very small next to the castle &ndash; is standing in front of the castle's main doors, awaiting the arrival of the first-years. In front of Hagrid is a large lake. A boat approaches across the lake, propelled by '''+pure_blue+''' magic. In the boat are the even smaller figures of Draco Malfoy and Harry Potter, facing away from each other.'''),
      (3350, '''TITLE: Chapter Two'''),
      (3650, '''TITLE: Castle of Gloss and Fear'''),
    ],
    "annotation": '''<p>My stylus once drew the windows of this castle. They felt wrong, somehow. Now you see only a blank facade and a sky empty of stars, and although you see the lights reflected in the water, they are absent. Perhaps this is Hogwarts as Harry sees it now &ndash; and as for the Hogwarts that an eleven-year-old saw, not knowing what was to come, you will not see it until the very end.</p>''',
  },
  {
    "xcf_base": "ch2_p1_1",
    "transcript": [
      (0, '''HARRY: Hogwarts was...'''),
      (410, '''We enter a <span class="dialogue HARRY">narrative frame</span> in which Harry describes past events.'''),
      (1055, '''PRESENT HARRY: Beautiful...'''),
      (2350, '''A younger Harry and younger Granger sit in a classroom, along with other students. Harry is staring out a window, where a brightly colored daytime scene is visible. Granger is working dutifully. There are books and papers on the desks, but Harry doesn't have any.'''),
      (3140, '''<span class="dialogue grey">MCGONAGALL:</span> {from off-page} <span class="dialogue grey">Potter, are you starting out the window again? Two points from Gryffindor, and next time, it will be ten!</span>'''),
    ],
    "annotation": '''<p>Returning by choice to look at a time and place where ze chose only to look elsewhere. I enjoyed building this page.</p>''',
  },
  {
    "xcf_base": "ch2_p2_1",
    "transcript": [
      (0, '''We see a view of the classroom where Professor McGonagall and some other students are visible. One of them is Ron Weasley. The others are indistinct. Harry is still staring out the window, and Granger is still dutifully working.'''),
      (0, '''RON: Aw, McGonagall, he's always doing that! Don't you want us to win the House Cup?'''),
      (440, '''MCGONAGALL: Weasley, <em>if</em> we win the House Cup, I want it to be won <em>fairly</em>, not through favoritism. I might remind you that Potter is not the only one who could stand to improve his behaviour in my class. That concludes class for today. Homework will be chapter two of the Switch book and five inches of parchment on the basic properties of glass in transfiguration.'''),
      (1754, '''PRESENT HARRY: I didn't know what she meant by five inches of parchment, and I didn't know a way to get someone to tell me. It wouldn't have helped anyway, because I could barely read or write.'''),
      (2733, '''The scene changes. We see McGonagall and Harry facing each other across a desk. McGonagall is pointing at a parchment on the desk, which has only a few words written on it.'''),
      (2850, '''MCGONAGALL: Is this all you have? Five points will be taken from Gryffindor for your lack of effort, young man!'''),
      (3380, '''PRESENT HARRY: But one professor was different from the rest.'''),
      (3380, '''We see Professor Severus Snape, standing next to a cauldron of '''+bright_green+''' liquid. Snape's eyes, hair, and robes are varying shades of dark gray, and zir skin is somewhat grayish as well. Ze looks worried.'''),
    ],
    "annotation": '''<p>Some people would say that Professor McGonagall is "strict, but fair".</p>
    
<p>What does it mean to be "strict, but fair"? People think that you can be "strict, but fair" by holding every student to the same standard... but with any standard, there will be some students that don't have the physical, mental, or social capability of living up to that standard. To those students, it is profoundly <em>un</em>fair.</p>

<p>Can you fix that by tailoring your demands to each individual student? Is anyone so skilled that they can identify the abilities of hundreds of people? Is anyone's judgment unclouded by classism, neurelitism, racism, sexism?</p>

<p>If those things are difficult or impossible, is this a task that is "difficult, but necessary"? Is it <em>necessary</em> for education to be a series of demands that adults impose upon children who have never consented to them?</p>''',
  },
  {
    "xcf_base": "ch2_p3_1",
    "transcript": [
      (0, '''In Professor Snape's classroom, Snape questions Harry. Draco Malfoy, Vincent Crabbe, and Gregory Goyle sit in a row near Snape, pointing and laughing when Harry fails to answer. All the students so far have had unadorned dark gray robes; Draco's robes, however, have a visible, '''+dark_green+''' collar &ndash; the signature color of Slytherin house. Granger sits nearby and raises zir hand fruitlessly. Snape is smirking, and ze speaks in a somewhat harsh visual style; the past Harry speaks with the same jagged, irregular shapes as the present Harry, but zir speech is colorless instead of of bright red. Harry is skinny in this moment.'''),
      (0, '''<span class="dialogue grey">DRACO, CRABBE, AND GOYLE: Ha Ha Ha Ha</span>'''),
      (0, '''NOTE: dialogue is from Harry Potter and the Sorceror's Stone, pp. 136-138'''),
      (88, '''SNAPE: Ah, yes, Harry Potter. Our new &ndash; celebrity. Potter, what would I get if I added powdered root of asphodel to an infusion of wormwood?'''),
      (490, '''PAST HARRY: I don't know.'''),
      (620, '''SNAPE: That will be "I don't know, <em>sir</em>." Let's try again. Where would you look if I told you to find me a bezoar?'''),
      (912, '''PAST HARRY: I don't know!'''),
      (1044, '''SNAPE: Tut, tut. What's the difference, Potter, between monkshood and wolfsbane?'''),
      (1372, '''Past Harry's voice becomes tinted with the '''+light_pink+''' color of Legilimency (colloquially, the power to read minds).'''),
      (1372, '''PAST HARRY: That's...'''),
      (2666, '''PAST HARRY: That's a trick question. They're... the same thing.'''),
      (2966, '''Snape glares at Harry, or maybe looks at Harry with an expression of concern.'''),
      (3214, '''The scene changes. We see Snape in a nondescript room, talking to an unseen person. Snape looks worried.'''),
      
      (3432, '''SNAPE: Albus... the boy is a natural Legilimens.'''),
    ],
    "annotation": '''<p>This is one of 4-6 times (depending how strictly you count) when I will replicate a specific scene from the books. This is basically the same as the original until Harry uses Legilimency to read the correct answer from Snape's mind. Snape could easily have blocked it, but ze wasn't expecting a student to have that power.</p>
    
    <p>There's no particular pattern to when I modify existing scenes and when I invent my own. For some of them, I use them to critique or comment on how the scene plays out in the books, but it's mostly just a matter of which ones I came up with good uses for. </p>''',
  },
  {
    "xcf_base": "ch2_p4_1",
    "transcript": [
      (0, '''Snape continues talking to the Headmaster, Albus Dumbledore. Dumbledore speaks in a soft, smooth cursive style, in a <span style="dialogue DUMBLEDORE">deep purple</span> color. However, only Snape is visible; Dumbledore and zir office are hidden in shadow.'''),
      (0, '''DUMBLEDORE: Legilimency... that is not a happy power for one so young.'''),
      (360, '''SNAPE: You will allow me to train him, I hope.'''),
      (440, '''DUMBLEDORE: You know Hogwarts has not taught Legilimency since...'''),
      (588, '''SNAPE: And the worse off I have been for it. Do you object to my training the boy?'''),
      (850, '''DUMBLEDORE: I hoped we could spare the poor boy that suffering for a while longer...'''),
      (1045, '''SNAPE: <em>Albus!</em> The longer we avoid training him, the more he will discover his abilities on his own, and the more damage he will do to both himself and others!'''),
      (2400, '''DUMBLEDORE: I remember like it was yesterday... Myself in Headmaster Dippet's office, telling him of Tom Riddle's uncanny skills... and with the prophecy and the twinned wands, are you not afraid that Harry will grow to become Voldemort's equal? {"Lord Voldemort" is an assumed name; that person was formerly known as Tom Riddle.}'''),
      (3072, '''SNAPE: Albus, please...'''),
      (3072, '''Snape looks a bit sad. Ze closes zir eyes.'''),
      (3700, '''SNAPE: I value your wisdom above all things, but about Tom Riddle, you will never understand.'''),
      (3822, '''DUMBLEDORE: That I cannot deny.'''),
    ],
    "annotation": '''<p>Our first glimpse of Albus Dumbledore...</p> ''',
  },
  {
    "xcf_base": "ch2_p5_1",
    "transcript": [
      (0, '''PRESENT HARRY: So my Legilimency lessons begain... finally something I could succeed at among all my failures. I could barely even find my way around the castle...
'''),
      (0, '''This page is a partial map of Hogwarts, as an Escheresque network of hallways and impossible staircases. Various doors and passages lead off into darkness at the edges. The hallways aren't colored like wood or stone, but are an unnatural spectrum from '''+deep_purple+''' to '''+bright_orange+'''. There are little icons of characters scattered around the map: McGonagall; Snape; the trio of Draco, Crabbe, and Goyle; and Peeves the poltergeist.'''),
      (1766, '''PRESENT HARRY: And then there were the slowly growing number of hallways I was too afraid to pass...'''),
      (1766, '''Some intersections on the map are crossed out with a '''+bright_red+''' X mark similar to present Harry's speech.'''),
      (3338, '''SNAPE: And the worse off I have been for it. Do you object to my training the boy?'''),
      (3729, '''PRESENT HARRY: Shut the hell up. You know the rules.'''),
    ],
    "annotation": '''<p>How to draw the moving halls of Hogwarts in a single, still image? It seemed so natural that it should be Escher Castle. You could go upstairs to class and then get lost and go upstairs to return. Or you could take a wrong turn and go downstairs to the top of a tower, from which you could only return by a long upward climb. Rumor says the castle has its own opinions about who should travel freely and who should be tripped and trapped every step of the way. What would Dumbledore think?</p>''',
  },
  {
    "xcf_base": "ch2_p6_1",
    "transcript": [
      (0, '''PRESENT HARRY: All the other Gryffindors hated me. I lost loads of house points... I sometimes woke everyone up screaming in the middle of the night, without knowing why.'''),
      (0, '''Past Harry sits up in a four-poster bed, screaming, the picture's outlines glaring '''+bright_orange+''' to represent zir mental/emotional state. Ron Weasley and two other students are awake, with a mix of groggyness and anger directed at Harry. Harry is fat in this moment.'''),
      (0, '''<span style="dialogue grey">PAST HARRY: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA</span>'''),
      (1190, '''PRESENT HARRY: Hufflepuff won the House Cup that year. We were in last place by more than a hundred points, even with your last-minute heroics.'''),
      (1600, '''Granger stands and smiles while a bunch of other people celebrate Granger by shooting off magical fireworks around zem. Nearby, two Slytherin students, Blaise Zabini and Draco Malfoy, are watching. The Slytherins speak in a curvy but fairly formal style; Draco speaks in <span style="dialogue grey">grey</span> and Zabini in <span style="dialogue ZABINI">pale orange</span>.'''),
      (1677, '''ZABINI: It's that same Mudblood who got on the front page of the Prophet {the Daily Prophet, a wizarding newspaper} last fall for getting lucky and beating a troll. Someone should teach her a <em>lesson</em>.'''),
      (2178, '''DRACO: Zabini, that's Hermione <em>Granger</em>! You can't fight her &ndash; she'll turn us all into chinchillas and report us straight to the Headmaster!'''),
      (2505, '''PRESENT HARRY: It was almost a relief to go back to the Dursleys for the summer.'''),
      (2880, '''Harry &ndash; now fat and with wild hair &ndash; grinning savagely as zir adoptive family, the Dursleys, face in the other direction. Vernon Dursley and Petunia Dursley are wearing stiff business suits and ties; Dudley Dursley, their child, is in a wheelchair. All of them are looking down and have grim expressions. Vernon and Dudley have relatively light skin and hair, while Petunia is slightly darker, like Harry (after all, Petunia is Harry's closest genetic relation in the family).'''),
      (3547, '''PRESENT HARRY: They knew there were rules against me using magic, but they knew I didn't follow rules very much when I was angry. It was the first time <em>other people</em> were afraid of <em>me</em>. It felt <em>good</em>.'''),
    ],
    "annotation": '''<p>You will see more of Blaise Zabini. Ze's not a main character, but ze will be important.</p>
    
    <p>In the books, Zabini's gender wasn't revealed until the sixth book, so fan-fiction versions of zem have a variety of genders. In this story, I'm going to ignore zir belated canon gender and simply choose not to reveal zir gender at all. (Technically speaking, I haven't revealed the genders of <em>any</em> of my characters, but with Zabini, I'm not even going to reveal what gender other characters think ze is.) I'm constructing a fairly gender-egalitarian world here, so it won't cause any trouble for understanding the plot &ndash; and I really dislike picking genders for characters in the role Zabini will play. I invite you to imagine Zabini as male, and imagine Zabini as female, and examine whether you feel differently about the story based on that.</p>
    
    <p>Actually, I invite you to do that with every character. And in every story you read, not just <i>Voldemort's Children</i>.</p>
    
    <p>On another note, I'd originally been planning to make the Slytherins' lettering (Zabini is in Slytherin) use a small-caps style with lots of serifs like the one McGonagall uses, but decided against it because that style is both tiring to write and hard to read, and I needed to put a bunch of text in a small area on this page. I'm pretty happy with the style I settled on; to me at least, it's very readable, and it still has a certain amount of formality and elegance to it, without taking lots of extra effort to draw.</p>''',
  },
  {
    "xcf_base": "ch2_p7_1",
    "transcript": [
      (0, '''PRESENT HARRY: But it still felt like I was starving at the Dursleys. They didn't actually starve me anymore, but it was nothing like Hogwarts food... so I was glad to come back...'''),
      (418, '''Harry returns on the Hogwarts Express &ndash; an old-fashioned train &ndash; sitting alone and pressing zir face against a window.'''),
      (846, '''PRESENT HARRY: And I felt the cloak of fear descend over me as soon as I got there.'''),
      (846, '''A metaphorical Voldemort stands behind Harry and drapes a '''+bright_orange+''', hooded cloak over Harry's shoulders. Voldemort's snake coils around both their legs.'''),
      (1826, '''PRESENT HARRY: But then I saw... one of the new first-years...'''),
      (2000, '''LUNA: Don't eat it!'''),
      (2000, '''Harry sits at a dining table in Hogwarts. Several students are sitting at another table, with food, but Luna Lovegood is standing up and yelling at them; one is intimidated by Luna, and one is looking back at Luna angrily. Harry looks at Luna curiously. Luna has the same pale skin and blond hair as Draco Malfoy, but zir hair is very long and loose while Draco's is very short and organized. Luna carries zir wand behind zir ear, and zir gestures and facial expressions are very un-self-conscious. Luna's speech is rendered in a very rounded, friendly style, in '''+bright_green+'''.'''),
      (3542, '''<span class="dialogue LUNA">LUNA: Don't you know? All the Hogwarts food is made by a secret slave race hidden in the heart of the castle!</span> {The house-elves. In the second Harry Potter book, Harry learns that the castle's food is prepared by diminuitive creatures called "house-elves" who have innate magical powers and human-level intelligence, and who, with few exceptions, desire only to serve the needs of wizards.}'''),
    ],
    "annotation": '''<p>Finally, Luna appears!</p>
    
    <p>Luna is the one character I haven't gotten straight in my head yet. In canon, ze's handled in a similar way to everyone else &ndash; ze gets the "cute weird girl" role, and might very well be neurodivergent (we certainly see that ze's socially oblivious), but wizarding society behaves in a generally tolerable way towards zem. In short, ze's another case of the story glossing over problematic real-life issues in order to become a nicer work of escape literature.</p>
    
    <p>As I delve into the horror of our world, I have to come up with a sensitive way of handling Luna. My goal with most of the characters is to preserve their sense of agency while also condemning the ways they're mistreated &ndash; a tricky task, because the simplest way to give agency to a character is to give zem power over the story, and people who are powerful tend to have less trouble with being mistreated.</p>
    
    <p>There's an extra problem with Luna in particular: ze's relatively content to ignore the problems around zem. (I could have changed that in my adaptation of Luna, but I've decided not to; I think it fits well with the direction I'm taking zem.) That runs the risk of either (1) making it seem like the problems actually <em>aren't</em> that bad, when they would be for many people, or (2) sending the message that the proper solution to being mistreated is to accept it. And it also means that, while I can use Granger and Harry to voice some of my own opinions about what is injust, I cannot use Luna in the same way.</p>
    
    <p>So, how do I handle all these issues? I have a lot of answers to that, and also a lot of thinking I still have to do. You'll see soon enough; I leave it to you, the reader, to judge whether I am successful or not.</p>''',
  },
  {
    "xcf_base": "ch2_p8_1",
    "transcript": [
      (0, '''PRESENT HARRY: She found me a few days later.'''),
      (500, '''Luna crouches barefoot on top of a post that's part of a staircase handrail. Harry is walking up the staircase. Luna is smiling down at Harry.'''),
      (1050, '''LUNA: Hello, Harry! Want to come and study with me?'''),
      (3184, '''Luna and Harry sit in a room with a nice round rug in the middle and bookshelves all around. Harry is on the floor; Luna is sitting on a table, which is currently barricading a door.'''),
      (3333, '''LUNA: I study in empty classrooms because it's distracting when people throw things at me. I like you! You haven't thrown stuff at me yet.'''),
    ],
    "annotation": '''<p>I have nothing to say except that I love this page.</p>''',
  },
]
  


"""
  {
    "transcript": [
      (0, ''''''),
    ],
    "annotation": '''''',
  },
"""
