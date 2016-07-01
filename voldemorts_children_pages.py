#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

import datetime
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
  "force_id":"fd9df785961f7dd11e22f4de97d6eb84",
  "force_date":datetime.date(2012, 2, 7),
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
  "force_id":"233d5959d0182a0d64d5e3a8e5030cf2",
  "force_date":datetime.date(2012, 2, 8),
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
  "force_id":"d316393474b43267fd8397fcefddce53",
  "force_date":datetime.date(2012, 2, 10),
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
  "force_id":"5cc17d5b1a29dfbd2b5d7c25f0fe78b5",
  "force_date":datetime.date(2012, 2, 11),
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
  "force_id":"fd65d0ecdd8bc1804f7a6ca6c8d16231",
  "force_date":datetime.date(2012, 2, 12),
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
  "force_id":"e33e643891721489e95870fcd346ade4",
  "force_date":datetime.date(2012, 2, 13),
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
  "force_id":"337c549d08c334049e92e66b61c916a5",
  "force_date":datetime.date(2012, 2, 13),
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
  "force_id":"5eb5724de96c953c7765147493f1963e",
  "force_date":datetime.date(2012, 2, 14),
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
  "force_id":"4f99267d6e2bb733d88617fb6b16f488",
  "force_date":datetime.date(2012, 2, 15),
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
  "force_id":"b53b82ea055eb8ba7ce4197a9e05f6d5",
  "force_date":datetime.date(2012, 2, 16),
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
  "force_id":"345812f70ff5905489aa63140962253f",
  "force_date":datetime.date(2012, 2, 18),
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
  "force_id":"6a285be71fc5528e98511fd50f677c0e",
  "force_date":datetime.date(2012, 2, 18),
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
  "force_id":"20b43baa61dce7ca4d4a7d7d069c22d5",
  "force_date":datetime.date(2012, 2, 19),
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
  "force_id":"8b6a5d2c46bc9ce88e965dc67e8dbe7d",
  "force_date":datetime.date(2012, 2, 20),
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
  "force_id":"e0040898f63d8a38325ff7f8983c9372",
  "force_date":datetime.date(2012, 2, 21),
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
  "force_id":"9cb00c54b1f00064ee7b825786ac1218",
  "force_date":datetime.date(2012, 2, 23),
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
  "force_id":"fb7cb28198c58a585c9d2075e303b217",
  "force_date":datetime.date(2012, 2, 24),
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
  "force_id":"175bfbb7429673cb831c540ead4a7c23",
  "force_date":datetime.date(2012, 2, 25),
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
  "force_id":"cff035d83f8aa77b8b3ac8d8425c3dae",
  "force_date":datetime.date(2012, 2, 26),
    "transcript": [
      (0, '''PRESENT HARRY: She found me a few days later.'''),
      (500, '''Luna crouches barefoot on top of a post that's part of a staircase handrail. Harry is walking up the staircase. Luna is smiling down at Harry.'''),
      (1050, '''LUNA: Hello, Harry! Want to come and study with me?'''),
      (3184, '''Luna and Harry sit in a room with a nice round rug in the middle and bookshelves all around. Harry is on the floor; Luna is sitting on a table, which is currently barricading a door.'''),
      (3333, '''LUNA: I study in empty classrooms because it's distracting when people throw things at me. I like you! You haven't thrown stuff at me yet.'''),
    ],
    "annotation": '''<p>I have nothing to say except that I love this page.</p>''',
  },
{
  "force_id":"e102cd5515c3c3f7be89c990370a565e",
  "force_date":datetime.date(2012, 2, 27),

  "transcript":"""LUNA: Professor Binns told us to read this. Isn't it fascinating?<br/>
Luna tries to hand Harry a large book.<br/>
PAST HARRY: I can't read that well.<br/>
LUNA: Oh. Oh! Membrana relecto! { Spoken as a spell. It's not a canon spell. The incantation "membrana relecto" is bad Latin for "re-read this parchment" or maybe "with this parchment having been re-read". }<br/>
The book starts to read itself aloud, in a voice similar to Luna's.<br/>
BOOK: The Great Discontinuity was a catastrophic temporal event coincidi...<br/>
LUNA: That spell repeats the voice of the last person who read the book aloud! My mum invented it to keep me busy when I was younger. She was a great experimenter, you know. Then she died! Isn't it funny how things happen?<br/>
PAST HARRY: My mum and dad were killed by Voldemort too.<br/>
LUNA: It wasn't Voldemort...<br/>
PAST HARRY: Oh... I didn't think...<br/>
LUNA: You could've aske&ndash;<br/>
Luna is interrupted by an image of Uncle Vernon yelling "Don't ask questions" at Harry.<br/>
<br/>
We see Lun and Harry sitting together, looking at the book that is still reading itself.<br/>
LUNA: Are you sad about it? About your folks dying?<br/>
BOOK: ...ith the defeat of Lord Voldemort. Claims of events "at the same time as" his death span up to six years in either direction, according to Ministry Common Time...<br/>
PAST HARRY: Not really... I was one year old when it happened. I don't remember or feel anything about it.<br/>
PRESENT HARRY: <em>Yet.</em><br/>
LUNA: Cool! Other people say I'm weird because I'm not sad about it. But being sad was too tiring so I stopped.<br/>""",
  "annotation":"""<p>What does Luna mean when ze says "being sad was too tiring so I stopped"? Lots of people in real life find it very tiring to be sad, and would love to stop, but can't. Clearly Luna isn't one of those people!</p>

<p>Luna's description might not be exactly understandable or reliable. Ze's only doing the best ze can to express what ze's felt; it's hard to describe subjective experiences, especially when your language evolved in a neurelitist society that assumes human emotions are universal.</p>""",
},
{
        
  "content_warning":""""bullying, ableism""",
  "force_id":"29b5951598d4b304f8f7cbf96293482c",
  "force_date":datetime.date(2012, 2, 28),

  "transcript":"""PRESENT HARRY: I studied with Luna whenever I could... and when I couldn't, I tried to use her spell to teach myself to read... but they hardly ever let me study in peace...<br/>
We see Past Harry sitting with a book and using Luna's "membrana relecto" spell on it. A staircase descends nearby.<br/>
BOOK: ...is theorized that the Memory Charm does not truly modify the victim's memories, but rather, simply creates a false proxy memory that obstructs access...<br/>
Draco, Crabbe, and Goyle show up.<br/>
CRABBE: Hey fatso!<br/>
PAST HARRY: Bugger off!<br/>
DRACO: Cute, the retard learned a bad word! Why don't we have Goyle show him how it's done?<br/>
Goyle goes to physically mess with Harry. An image of Voldemort appears.<br/>
VOLDEMORT { in a voice like Harry's }: Not this time.<br/>
Harry grabs Goyle violently. Harry's glasses go flying. Another image of Voldemort holds up, as if in a demonstration, an iconic image of Harry throwing Goyle down the stairs. Then we see Harry, Crabbe, and Draco looking down the stairs to where Goyle lies at the bottom. The voice of Snape comes from below.<br/>
SNAPE { unseen }: Excuse me.<br/>
Harry, Crabbe, and Draco look down in horror.""",
  "annotation":"""<p>Oh shiiiiiii&mdash;</p>""",
},
{
  "force_id":"19410d5746cc18b3ac2f23de8322b675",
  "force_date":datetime.date(2012, 2, 29),

  "transcript":"""Snape kneels over the unconscious Goyle, while Harry, Crabbe, and Draco stand still at the top of the stairs.<br/>
SNAPE: Vulnera indico. { A non-canon spell; Latin for "Reveal the injuries". }<br/>
Magical energy appears on Goyle's body on the head, one arm, and one leg, as well as near Snape's wand.<br/>
SNAPE: He will recover... with time...<br/>
Snape turns to look up the stairs.<br/>
SNAPE: Potter! Return to your dormitory immediately. I will know if you do not. The Headmaster will see you as soon as he is available. Malfoy, Crabbe, come with me. It goes without saying that both your houses will be penalized for this incident.<br/>
We see Harry climbing through the portrait hole into the Gryffindor common room. This is one of the most well-lit rooms we've seen yet, although it is still shadowy. A fire burns in a hearth. There are two round tables with plush chairs around them, and a couch of a similar style across from the portrait hole. At one of the tables, Granger is breezing through a Transfiguration assignment involving turning glass marbles into beetles and writing about it (although it's probably too small for the average viewer to see that's exactly what's going on). Granger is facing away from Harry; at the other table, George Weasley and Angelina Johnson are standing and facing Harry angrily as ze enters the room. George is very pale and has short-cropped red hair; Angelina is quite dark and has more-than-shoulder-length black hair.<br/>
ANGELINA: Well, if it isn't the prat who just lost us fifty points!""",
  "annotation":"""<p>That's Angelina Johnson, by the way (and George Weasley near zem). I originally had planned to make the two jerks here be Fred and George, but then I remembered how much Angelina had badgered Harry in the fifth book about getting in trouble by standing up to Umbridge, so I figured ze'd be perfect for this role.</p>

<p>I'm slightly concerned that none of my darker-skinned characters so far have been friendly ones. Lily Evans will be dark-skinned and friendly, though, or at least as friendly as you can get in a story as <em>metaphorically</em> dark as this one. (I don't know if Angelina's race is ever specificed in the books, but ze's black in the movies, and I consider the movies to be canon when they don't contradict the books &ndash; and I saw no particular reason to change it, since whitewashing my characters would be a jerk move too.)</p>

<p>On another note, I'd ask, "Do you think Snape is doing the right thing in this situation?", but I think it's the wrong question. How about: Are Snape's actions here <em>sufficient</em> to address the wrongs we've seen? And what kinds of things could Snape have done earlier, to stop this situation from having happened in the first place?</p>""",
},
{
  "force_id":"884b8beb960ac75f15e549b541224a01",
  "force_date":datetime.date(2012, 3, 1),

  "transcript":"""George and Angelina tower over Harry.<br/>
GEORGE: You think you can just saunter in here like nothing happened? Levicorpu&ndash; { "Levicorpus" is the incantation of a spell that lifts a person into the air, usually for the purpose of bullying. }<br/>
PAST GRANGER: Finite! { A spell that ends an enchantment. }<br/>
Past Granger has looked up from zir Transfiguration work and is leaning forward in zir chair, countering George's spell. Past Granger speaks in approximately the same way as present Granger; zir speech has slightly less color than present Granger's, but isn't gray like the other students'. On this page, some details of the room are drawn around Granger, but not near the other characters.<br/>
PAST GRANGER: I've earned more points than he's lost, and I say if you want to fight him, you'll have to fight me too.<br/>
ANGELINA: You? A second-year against the two of us? It wouldn't be a fair f&ndash;<br/>
Granger rolls zir eyes and sends the two of them flying with a multicolored barrage of spells, without getting up from zir chair. Harry cowers from the action with zir hands over zir face.<br/>
PAST GRANGER: Er... Potter? I heard you're supposed to see Dumbledore? I just came from meeting him in his office, actually; I'd go there now if I were you. The password is "Aspartame".""",
  "annotation":"""<p>Why do you think Granger declared zir status as an earner of lots of points? Ze could have just defended Harry without saying that. Would that have been a better decision? Worse?</p>

<p>And to follow up on the previous page's annotation, do you think it's ethical for Snape to be participating in the "house points" system at all, when it leads to the kind of intra-house bullying that we're seeing here?</p>""",
},
{
  "force_id":"e01042ce989e4040b4b4050bf9578360",
  "force_date":datetime.date(2012, 3, 2),

  "transcript":"""Harry approaches the gargoyle that guards Dumbledore's office. The gargoyle has bat-like wings, twisted horns, and claws on its feet. It is grinning widely.<br/>
PAST HARRY: Aspartame.<br/>
The gargoyle steps aside with a bow and Harry climbs the spiral stairs.<br/>
We see Harry approaching the door to Dumbledore's office.<br/>
We see Harry putting zir hand on the doorknob.""",
  "annotation":"""<p>Thus ends chapter two of <i>Voldemort's Children</i>.</p>""",
},
{
  "force_id":"db73782233bdf40ea79867809df20422",
  "force_date":datetime.date(2012, 3, 4),

  "transcript":"""The right half of this image is the title:<br/>
CHAPTER THREE<br/>
Seats of Influence<br/>
<br/>
The left half is a complicated metaphorical image. Albus Dumbledore is sitting in a plain chair; behind zem, Voldemort is standing, putting one hand on Dumbledore's shoulder. Dumbledore has a long gray/white beard and wears purple robes. Both of them have the top halves of their heads concealed in shadow, and Dumbledore has the same flat expression that Voldemort always has. Voldemort's wand, as we've seen before, is nearly white; Dumbledore's is nearly black. Both Dumbledore and Voldemort are pointing their wands downwards, working together to conjure an elliptical pool of magical energy, which is half Dumbledore's characteristic color and half Voldemort's. The pool is also divided into three parts by a spiral design, and the three sections are occupied by tiny versions of Harry, Draco, and Luna. Luna is sitting in a plain chair, looking serene; Harry is sitting in a very jagged chair that must be painful to sit in; Draco is lying on zir back next to a chair that has broken in half, and looks slightly panicked.""",
  "annotation":"""<p>It took me all day to come up with the right visual metaphor to use here, but I did it! Feel free to analyze the crap out of this image.</p>

<p>I don't know if Dumbledore's wand is the Elder Wand; it doesn't matter in this story.</p>

<p>The triskelion on the floor definitely <em>isn't</em> the <a href="https://en.wikipedia.org/wiki/BDSM#Symbols">BDSM emblem</a> (parts of linked page NSFW); BDSM is consensual by definition, and the relationships between these characters... aren't. So I deliberately made the arms spiral in the opposite direction from the emblem.</p>""",
},
{
  "force_id":"545037a8c4798174e133db95242df7dd",
  "force_date":datetime.date(2012, 3, 5),

  "transcript":"""PAST HARRY: I still wonder what might have happened if we had not crossed paths... if I had not come to an empty office...<br/>
Harry walks into Dumbledore's office, but Dumbledore isn't there. Portraits of silhouetted people, presumably former Headmasters and Headmistresses, line the back wall. On one table are several delicate devices made of a bronze-ish metal. One is a set of scales with nothing in it; another has a roll of paper and is making a continuous mark on it, like certain types of seismograph. Another desk has a chair in front of it and a basin full of magic the color of Legilimency on it; this is the Pensieve. In the foreground, Fawkes the phoenix, a very brightly-colored magical bird, faces away from Harry and turns up its beak; Harry is looking unexcitedly towards the main desk. The whole scene is lit by a candelabra hanging on a chain from above.<br/>
PAST HARRY: I think Snape wanted me to see that Dumbledore was kind and forgiving... and if he'd been there to meet me, I might have come to respect that man... Not knowing...<br/>
PAST HARRY: But instead...""",
  "annotation":"""<p>As it turns out, the tiredness that delayed me recently was actually a symptom of me being physically sick. I've managed to write a page today and a page yesterday because it was the weekend and I had no other obligations, but until I'm healthier, I'm not actually going to be able to keep up a rate like this. The most important thing is for me to get enough rest that I can be back on schedule as soon as possible.</p>

<p>I ought to have a buffer ready for this kind of thing, but, well, I already used it up. (Hey, it's my first time doing this!) I should be able to build the buffer back up again in a couple of weeks when I'll have a 9-day break from college. Until then, I'll do my best, but my updates might be a bit inconsistent.</p>""",
},
{
  "force_id":"a12d4d8790ec29e9e10c1f29a85fa78c",
  "force_date":datetime.date(2012, 3, 8),

  "transcript":"""Large text; only one image on this page.<br/>
PRESENT HARRY: I found myself in front of...<br/>
Past Harry is looking down into the Pensieve.<br/>
PRESENT HARRY: ...the basin where he keeps his <em>memories</em>.<br/>
We will enter a narrative frame where we see the memories Harry is seeing in the Pensieve.""",
  "annotation":"""<p>In the books, the Pensieve makes you feel like you're actually in the memory, but are a powerless observer. The magic of comics will allow me to just show you the memories directly.</p>

<p>In the books, the Pensieve is silvery, but here it's pink/purple like Legilimency because I wanted a distinctive color for mind-based magic in general, and because it fits into my general color symbolism better.</p>

<p>Other than that, the Pensieve works the same way it does in the books.</p>""",
},
{
  "force_id":"8c400c2522e0a40972d7305d6765856c",
  "force_date":datetime.date(2012, 3, 13),

  "transcript":"""One of Dumbledore's memories. Dumbledore and McGonagall stand in front of the Dursleys' home. It is a generic middle-class house, with shrubs arond the door. Dumbledore still has the same face concealment and flat expression of Voldemort; McGonagall is wearing a pointed hat with zir robes. A note says, "This page's dialogue is mostly from HP&tSS, pp. 13-14."<br/>
DUMBLEDORE: I've come to bring Harry to his aunt and uncle. They're the only family he has left now.<br/>
MCGONAGALL: You don't mean &ndash; you <em>can't</em> mean the people who live <em>here</em>? Any wizarding family in Britain would take him in &ndash; he'll be famous &ndash; a legend &ndash; there will be books written about him&ndash;<br/>
DUMBLEDORE: Exactly. It would be enough to turn any child's head. Can't you see how much better off he'll be, growing up away from all that until he's ready to take it?<br/>
MCGONAGALL: Yes &ndash; yes, you're right, of course, but how is the<br/>
McGonagall is cut off by the narrative frame closing. We see Harry in front of the Pensieve again. Harry is upset, crying.""",
  "annotation":"""<p>It's possible, at this point in history, that Dumbledore and McGonagall don't know the Dursleys' attitude towards magic, or if they did, they could plausibly rationalize it away by saying that they'll still treat Harry well because Harry is family to them. (Dumbledore would say "still love Harry" instead of "still treat Harry well", but there are plenty of people who love their children and still behave abusively towards them. Dumbledore thinks love is sufficient, but it isn't.)</p>

<p>Parents who send their teenage children to WWASP schools (TRIGGER WARNING for child abuse if you even do a web search for "WWASP") sometimes don't know about the abuses there, either. Does this mean Dumbledore is like those parents? (In short, WWASP is an organization that runs schools that keep teens in isolation and use extremely abusive "behavior modification" tactics, while denying everything and presenting a clean face as a program for "troubled teens". Tranquility Bay was a well-known one that got shut down, but there are many others, such as Cross Creek Programs and Horizon Academy.)</p>

<p>What about McGonagall, though? Ze resists the idea of placing Harry here for a moment. I could imagine zem as a person who's aware of the issue, but knows ze won't be able to argue Dumbledore out of it and so gives in easily... But is it true?</p>

<p>In the movie, McGonagall describes the Dursleys as "the worst kind of Muggles"; in the book, ze doesn't say that outright, but says "You couldn't find two people who are less like us" &ndash; and I infer that "us" means "wizards". Ze goes on, "These people will never understand him! He'll be famous!"... So it seems like zir objection is to a person of high status (a wizard, a child of a prestigious family, a legend) being placed with a family of low status (muggles, people with outwardly distasteful behavior by wizarding standards). McGonagall isn't thinking about child abuse here &ndash; ze opposes the placement because ze's <em>racist</em>.</p>""",
},
{
        
  "content_warning":""""a little blood""",
  "force_id":"b594261f7fadae0b98b1b86aaf97bc06",
  "force_date":datetime.date(2012, 3, 18),

  "transcript":"""We are viewing the memory again.<br/>
PRESENT HARRY: I saw lots of painful memories in the Pensieve, but that one hit me harder than any of the others.<br/>
In the memory, Hagrid arrives on an obviously magical motorcycle, carrying the infant Harry wrapped in blankets. Dumbledore and McGonagall are still standing in front of the Dursley home, waiting for zir arrival. Hagrid is huge; ze looks fully twice as tall as either of the others, although ze's also closer to the viewpoint, so the effect is somewhat more exaggerated than the reality. A note says "the remembered dialogue is from HP&tSS, pp. 14-15"<br/>
DUMBLEDORE: Hagrid. At last.<br/>
HAGRID: House was almost destroyed, but I got him out alright before the muggles started swarming around.<br/>
PRESENT HARRY: It was Hagrid. The same person who rescued me ten years later...<br/>
Hagrid reaches out zir hand, offering the infant Harry to Dumbledore. Harry is barely wider than Hagrid's hand. Ze is sleeping, apparently peacefully, although there is a jagged cut on zir forehead, where the scar will be. A trickle of blood touches one of zir eyes. Ze doesn't have a scar at the corner of zir mouth; this is the first time we've seen Harry without that scar.<br/>
PRESENT HARRY: He had no idea. He had no idea...<br/>
DUMBLEDORE: Well &ndash; give him here, Hagrid &ndash; we'd better get this over with.""",
  "annotation":"""<p>I'm writing a fanfic of a fantasy series, and I have to draw a motorcycle? DAMN YOU, J.K. ROWLING!</p>

<p>On a more serious note, look at the way Hagrid refers to "muggles" as "swarming around" &ndash; I think it's rather dehumanizing. If I lived in this world, I'd probably be careful to use the phrase "non-magical people" instead, because "muggles" is used in a dehumanizing way so much.</p>

<p>I think I might start using "non-magical people" and "magical people" in these annotations anyway, because "witch/wizard" is gendered. (As a side note, I insist that in general usage, "wizard" is gender-neutral. The main reason I insist upon that is because I enjoy claiming to be a wizard even though I'm not male, but it does have the support of some existing authorities, such as <i>Dungeons & Dragons</i>. However, this is a <i>Harry Potter</i> fanfic, and in the <i>Harry Potter</i> universe, "wizard" is definitely gendered.)</p>""",
},
{
  "force_id":"1d2557f11297ffd08e30c1cb9c5eb7f6",
  "force_date":datetime.date(2012, 3, 19),

  "transcript":"""Harry shoves the Pensieve away and it falls off the table and spills. Harry ignores that and runs out of the Headmaster's office, down the stairs, through Hogwarts, and out to Hagrid's hut. Ze knocks on the door.<br/>
PAST HARRY: Hagrid, open up! It's me, Harry!<br/>
Harry enters Hagrid's hut. Hagrid is literally about twice as tall as Harry, and is sitting on the floor, with zir huge dog, Fang, lying on zir lap with its eyes closed and its tongue hanging out. Hagrid and all zir stuff (home, dog, etc) are drawn with thicker lines than everything else.<br/>
HAGRID: What's got yeh in such a rush?""",
  "annotation":"""<p>How would this story flow differently if I had just written "So I ran to Hagrid's hut" instead of including this page?</p>

<p>For one thing, it would have been quicker and easier for me to write. That's one of my motivations, obviously; in fact, I want to get this story done as quickly as is possible without sacrificing quality, so if drawing something and just summarizing it are equally effective in the narrative, I'll go with the summary. If I draw something, it means that either it was quicker to draw it than to explain it (which sometimes happens), or it had an important effect that I couldn't achieve with a summary.</p>

<p>I can't actually be certain why I chose drawing instead of summary here; there are a few specific reasons I can think of, but I really made the decision based on instinct rather than logic.</p>

<p>Anyway, the first reason is that it establishes the setting &ndash; this way, you get a view of the outside of Hagrid's hut, and so you have more of a sense of where the action is than if you just saw the image of Harry inside the hut to begin with.</p>

<p>The second reason is that it dramatizes what's about to happen. What made Harry feel strongly enough that ze ran all the way to Hagrid's hut at a stretch? And what's going to happen when ze gets there? These are questions that you wouldn't have time to ponder if I skipped over the action of this page. (And we're going to be in Hagrid's hut for about three pages after this, so the hype is worth it &ndash; I wouldn't write a page-long setup to an event that was over in one page, unless it was REALLY important. But writing setup pages for sections that are larger or more important helps establish a structure for the story.)</p>""",
},
{
        
  "content_warning":""""child abuse""",
  "force_id":"ae39a500f0d0b85158ee73270a8da43f",
  "force_date":datetime.date(2012, 3, 20),

  "transcript":"""In Hagrid's hut. Harry faces Hagrid and Fang.<br/>
PAST HARRY: Dumbledore never told you what the Dursleys did to me!<br/>
HAGRID: I'm sure it was none of my business.<br/>
PAST HARRY: Then I'll tell you now... because you <em>deserve</em> to know...<br/>
We enter a narrative frame in which past Harry describes past events.<br/>
PAST HARRY: From the moment you left me there, my aunt and uncle trained their son Dudley to hate me. They told him that he was good and I was worthless. They praised him every time he broke something that I liked.<br/>
There is an illustration of those three people. Dudley is grinning nastily. Petunia and Vernon have their hands on Dudley's shoulders, but aren't looking at zem; they both look concerned with something outside the view.<br/>
PAST HARRY: Dudley had a gang of boys who liked to beat me and anyone who tried to be my friend.<br/>
There is an illustration of Harry facedown on the ground with Dudley sitting on zem, with three other children standing around, laughing. Harry doesn't have the scar next to zir mouth in this image, and zir speech is drawn in a less jagged style. That Harry is saying, "Yow! Geroff!" Dudley replies "Okay, I will... when I want to!"<br/>
PAST HARRY: There was nowhere I could escape from them, not at school, not at home, except inside my own head. But I hardly needed to tell you that one... because...""",
  "annotation":"""<p>What makes a person keep their experiences bottled up, and what makes a person shout out loud about them?</p>""",
},
{
        
  "content_warning":""""child abuse, blood""",
  "force_id":"626fd7ad3d81b6cde73fa41e7ddaed70",
  "force_date":datetime.date(2012, 3, 21),

  "transcript":"""A rainwater drain pipe sticks off the side of a building, near the ground. A bit of water trickles down.<br/>
Dudley and another child grab Harry and drag zem to the pipe, and jam zir head against it.<br/>
We see a closeup of Harry's mouth &ndash; a simplified drawing, reminiscent of Voldemort. There is a nasty cut next to zir mouth, where the scar will be. There is also blood on the edge of the drain pipe.<br/>
We see Harry in a car with Petunia; Harry is in the back seat, staring out the window, trying to cover zir cut with one hand, but still bleeding. Petunia speaks in a rigid style, but slightly irregular, as opposed to the precise formality of characters like Snape and Fudge.<br/>
PETUNIA: I had to leave work to pick you up. That's more of <em>my</em> money you're costing, useless brat. And don't you dare get your blood on the seats. They were just reupholstered.<br/>
We see Petunia ordering Harry through a cupboard door under some stairs. After Harry goes in, Petunia locks the cupboard shut with a large padlock.<br/>
PAST HARRY (continuing the monologue from the previous page): ...because the story of what they did to me is written on my face where anyone can read it.""",
  "annotation":"""<p>I have a hard time remembering all the things I need to draw on Harry's face in any given scene. There's the zigzag scar, obviously (although when I draw zem as a baby before Voldemort attacks, I'll have to omit that). There's the mouth scar, which exists in things chronologically after the events of this page, but not before. There's the black blotches under zir eyes that indicate constant fatigue, which mainly appear when ze's at Hogwarts. And there's the glasses.</p>

<p>I don't think I've forgotten to include the glasses yet - they're often missing, but for a reason. In the current narrative layer, Harry doesn't have glasses because the Dursleys never bought zem any. Hagrid noticed Harry's bad vision and brought Harry to a magical eye doctor in Diagon Alley when they went to shop for books &ndash; and the sudden ability to see properly was yet another of the things that seemed wonderful about the magical world to Harry, before the more painful realities reached zem.</p>

<p>The Dursleys might not even have known that Harry had vision problems; it interfered with zir performance in school, and zir ability to do everyday tasks, but they assumed Harry was lazy and incompetent anyway.</p>""",
},
{
        
  "content_warning":""""child abuse, blood""",
  "force_id":"739293bb358461bb32c147a038ba1d0c",
  "force_date":datetime.date(2012, 3, 27),

  "transcript":"""PAST HARRY: The wound was infected before they let me out... Doctors had to take apart half my face to fix me.<br/>
We see Harry in the cupboard under the stairs, with very little light. Zir hands and arms are covered in blood, and zir face is messed up.<br/>
The narrative frame closes; we're back with past Harry in Hagrid's hut.<br/>
PAST HARRY: And now I have this... { ze points to zir mouth scar } The living proof of what they did... of what <em>Dumbledore</em> did to me.<br/>
Hagrid looks angry. All the characters' eyes are slightly reddish on this page. Hagrid's speech is drawn much larger than Harry's.<br/>
HAGRID: Harry...<br/>
PAST HARRY: Dumbledore used you! He made you bring me there and never let you see what you'd really done!<br/>
HAGRID: Maybe he jes' &ndash; jes' wanted &ndash;<br/>
PAST HARRY: I don't care what he wanted! He kept me there for ten years and hid it from everyone so that no one could&ndash;<br/>
HAGRID: <em>Yeh're not ter talk about Albus Dumbledore like that in my house!</em><br/>
Past Harry leaves Hagrid's hut and closes the door behind zem.<br/>
PAST HARRY: Then I'll do it outside of your house!!!""",
  "annotation":"""<p>The virtue of Loyalty.</p>""",
},
{
  "force_id":"35271e0c4603cfd4a05456a8ba8aaba6",
  "force_date":datetime.date(2012, 3, 28),

  "transcript":"""Past Harry stands outside Hagrid's hut, facing away from it.<br>
PRESENT HARRY: I should have destroyed that hut. I should have burnt it to the ground! that place where one man's good name is more important than ten years of abuse! { pause } I was too weak. { pause } Instead, I ran and hid, in an unused room I'd found where there as a strange mirror that reflected everything except for me.<br/>
Past Harry stands in a dark room, facing a tall, ornate, tinted mirror. There is an unreadable inscription on its frame. There's a table nearby, which is reflected in the mirror. Harry is touching the mirror with two fingers, but those fingers are not reflected.<br/>
PRESENT HARRY: And then...<br/>
DUMBLEDORE'S VOICE { from off-page }: Ah, Harry, I thought I might find you here.<br/>
PAST HARRY: You!!!""",
  "annotation":"""<p>Usually, if a character destroyed a building in a fit of rage, we'd consider that to be a character flaw. Here, present Harry considers the fact that past Harry <em>didn't</em> do that to be a character flaw!</p>

<p>If a character does something that you think is a bad idea, but they disagree and think it was fine, then it's not "a character flaw", it's just "somebody doing something you don't like".</p>

<p>I personally don't find the concept of "character flaws" to be a useful concept, in general &ndash; categorizing people's attributes into "good" and "bad" is an oversimplification that doesn't really help me understand either the attributes or the people. I sometimes use such simplifications to decide <em>what to do</em> in real life, but when I'm building a story, the important thing to do is to understand deeply.</p>""",
},
{
        
  "content_warning":""""suicide""",
  "force_id":"28d29ef3f41cfa016d703c6782c7d115",
  "force_date":datetime.date(2012, 3, 29),

  "transcript":"""We see a large image of past Harry looking directly towards the viewer, upwards, as if the viewer is Dumbledore. The rest of the page content surrounds that figure.<br/>
PAST HARRY: You can't hide the truth from me anymore. How you kept me trapped for ten years... watching over me...<br/>
PAST HARRY: The stray animals that found me when I ran away from home... you sent them.<br/>
We see a memory from the Pensieve: A younger Harry lying on the ground between rows of unmarked boxes. A black cat is pawing at Harry's face. The cat is identical to Voldemort's cat except that the color of its glowing eyes is Dumbledore's color.<br/>
PAST HARRY: The knives in the house, too blunt to cut my skin... you blunted them.<br/>
We see a memory from the Pensieve. A younger Harry kneels next to a refrigerator and some cabinets, trying to cut zir own throat with a knife. The knife is glowing Dumbledore's color.<br/>
PAST HARRY: You... with your magic... in your castle... you took away every possible way for me to escape... carefully... from safety... I hate you. <em>I hate you! <strong>I hate you!!</strong></em><br/>
DUMBLEDORE { from off-page }: Oh, Harry... It was a different time...""",
  "annotation":"""<p>Harry learned those things from the Pensieve, along with a lot of other things we didn't specifically see. In another instance, a memory from the Pensieve is the reason Harry can tell us the events of <a href="http://www.elidupree.com/main/posts/173-voldemort's-children-page-14">this page</a>.</p>

<p>I'm not sure exactly how Dumbledore blunted the knives in the Dursley house; maybe it's just one of the effects of a general anti-suicide jinx that ze placed on the house.</p>""",
},
{
  "force_id":"34937efe071db43cf40b952555b142d1",
  "force_date":datetime.date(2012, 3, 30),

  "transcript":"""DUMBLEDORE: It was a different time... Voldemort's followers were everywhere, and no-one was sure if he had truly been defeated. Anyone could have been the next target. The Dark Lord tore families apart... I didn't want that to happen again. And if you had not lived with your aunt, you might have lost your mother's lingering protection... I was trying to keep you alive, Harry. You could have been killed... as so many others had been...<br/>
The above monologue is spoken by two Dumbledores: One in reality, and one in the mirror. Harry is standing next to the mirror, facing towards it, looking down; Dumbledore is standing behind zem, reaching out one hand, which Harry ignores. Dumbledore is reflected in the mirror, but Harry isn't, so the real Harry is alone and surrounded by two Dumbledores &ndash; and both Dumbledores are much bigger than Harry. The mirror-Dumbledore is reaching zir hand towards empty space, or towards the real Harry, depending how you look at it. Dumbledore's eyes are still hidden in shadow.<br/>
PAST HARRY: Then you should have let me die. It would be better than what you gave me.""",
  "annotation":"""<p>Dumbledore seems to believe in keeping biological families together. In this case, zir belief in the concept of biological family has caused zem to come to a wrong conclusion. Not all biological families are true families. (And not all true families are biological families.)</p>

<p>What do you think makes a true family? What kinds of relationships should we celebrate or defend?</p>

<p>Or, is that the wrong question to be asking? In what circumstances is it necessary for an outsider to make assumptions, or judgments, about the nature of a person's relationships?</p>""",
},
{
  "force_id":"f38dd5a863484a4cb7ac05f3c8be73f1",
  "force_date":datetime.date(2012, 3, 31),

  "transcript":"""PRESENT HARRY: He kept me there for a long time, talking at me. I don't want to remember much of what he said. He could have expelled me for what I did to Goyle. He didn't. Nothing I could do would change where he wanted to put me.<br/>
Dumbledore stands over Harry. The phrases ze's saying angle radially into Harry's head. Harry is covering zir ears and has zir eyes closed tightly.<br/>
DUMBLEDORE: No one regrets more than I ... One day you will understand ... No one can change the past ... It pains me to have to tell you ...<br/>
PRESENT HARRY: After he let me leave, I swore to myself that I would <em>kill him</em>. But I couldn't. I had no power. My rage was useless. { pause } I stopped caring. { pause } I didn't talk much for the rest of that year. Not even to Luna. I told her everything at first, but after that I couldn't talk to her without thinking of it again. I wanted to forget.<br/>
Another scene. Luna looks towards Harry with concern. Harry is facing away from Luna, with a flat expression on zir face. The next line is drawn right in the middle of the scene:<br/>
PRESENT HARRY: Just finish this meaningless course he put me on, and forget.<br/>
PRESENT HARRY: But as I returned for my third year, things began to change...""",
  "annotation":"""<p><q>This meaningless course he put me on</q> is pretty fancy language, for Harry.</p>

<p>It makes sense that Harry's vocabulary is rather idiosyncratic, since ze was barely able to read before entering Hogwarts, but then started reading (using Luna's spell) lots of wizard books, which tend to be... sesquipedalian.</p>""",
},
{
  "force_id":"c1ea47422fe32732b3d2ae17d3391053",
  "force_date":datetime.date(2012, 4, 1),

  "transcript":"""PRESENT HARRY: After the Sorting... before the first meal...<br/>
Harry is sitting at a table, with other students, and dishes set out, but no food. Draco Malfoy has come to stand next to Harry.<br/>
DRACO: Well, well &ndash; Look who's back for another round.<br/>
A Legilimency effect points from Harry's eyes to Draco's.<br/>
PRESENT HARRY: I happened to look in his eyes... and I learned something... something <em>interesting...</em><br/>
Close-up of Harry's face and Draco's face, facing each other, close together. A beam of Legilimency connects their eyes. Past Harry's speech takes on the color of Legilimency.<br/>
PAST HARRY: Draco Malfoy... you're afraid of me.<br/>
Draco looks back with a shocked expression.<br/>
PRESENT HARRY: Suddenly, everything about him made <em>sense</em>. The glance toward the Slytherin table, hoping they hadn't noticed his moment of weakness...<br/>
Draco glances towards the Slytherin gable. Zabini, Crabbe, and Goyle are all looking towards Draco. Zabini has risen from the table.<br/>
PRESENT HARRY: And when he saw that they had, the turn back to me...<br/>
Draco faces Harry with a furious expression. Harry's face is mostly concealed in shadow.<br/>
DRACO: You'll pay for this!""",
  "annotation":"""<p>Legilimency.</p>

<p>Magic, in stories, has two semi-conflicting roles. One, it's there to be awesome, for the drama and the spectacle. And two, it's there to represent something from real life &ndash; to function as <em>heightened reality</em>. An individual story can exist anywhere on this spectrum; sometimes, like in <a href="/main/posts/109-a-couple-of-badass-superheroes-page-1"><i>A Couple of Badass Superheroes</i></a>, I write fantastic powers entirely because they're awesome and hilarious. <i>Voldemort's Children</i> is the opposite; the purpose of the magical elements is to talk about things that exist in real life.</p>

<p>The ability to intuitively judge what other people might be thinking and feeling, after all, is something that exists in real life. So Legilimency isn't really something that's new or unheard-of. But compared with its real-life counterpart, Legilimency is more powerful and more reliable... and most importantly, it has a <em>name</em>. So it can be an explicit element of the story &ndash; an issue at stake &ndash; a thing that you can point to, think about, and ask questions about.</p>""",
},
{
  "force_id":"aa6dcb072361313a18d0d624b6086465",
  "force_date":datetime.date(2012, 4, 6),

  "transcript":"""PRESENT HARRY: But reading fears is the first thing you learn in Legilimency. It was so easy to play on what I saw...<br/>
PAST HARRY { in Voldemort's voice }: I think not. You would not want to anger me.<br/>
Draco sweats.<br/>
Zabini comes up next to Draco and puts zir hand on Draco's shoulder. With zir other hand, ze blasts Harry backwards with a spell, knocking Harry's stool over as well. Another student next to Harry looks shocked. But Zabini isn't even looking at Harry; ze's looking at Draco.<br/>
ZABINI: Was this half-blood giving you trouble, Malfoy?<br/>
Draco is startled.<br/>
DRACO: AAH<br/>
PRESENT HARRY: He walked away while it was easy. But he would not forget this moment.<br/>
The page ends with a view of Zabini and Draco walking away, from a low angle, maybe Harry's perspective. Zabini is looking towards Draco with a frown; Draco is farther away, but ze's looking over zir shoulder back down towards the viewer.""",
  "annotation":"""<p><q>Harry Potter? Who's that? All I saw was the noble scion of the Malfoy family and some half-blood.</q></p>

<p>Dedicated blood-purists like Blaise Zabini don't always hate half-bloods, but they particularly hate Harry because Harry is the offspring of James Potter (the last descendant of a highly respected pure-blood family) and Lily Evans (whose parents weren't even magical). So, to them, Harry represents the destruction of an entire lineage.</p>

<p>(Most people in this society don't hold quite such extreme attitudes, but they still look down on Harry because ze was raised by muggles.)</p>""",
},
{
  "force_id":"fedd6c185536a1e17d6b7d0bdbb7245d",
  "force_date":datetime.date(2012, 4, 6),

  "transcript":"""PRESENT HARRY: I was in Snape's office a day later for my first Legilimency lesson for that year.<br/>
Harry and Snape are in Snape's office. Each is standing next to a chair, and there is a desk between them. Harry is looking towards Snape, but Snape is looking in the other direction.<br/>
SNAPE: I cannot help but observe that you have been using Legilimency on one of my students, in the unsubtle manner I have come to expect of you, Potter. Of course, I cannot stop you. But you must understand that there will be trouble if the public learns that we are allowing you to violate their children's minds. In this case, I believe it will go unreported where it has not gone unnoticed, but you must learn to be more subtle.<br/>
Snape turns and points to a chair.<br/>
SNAPE: Sit down. We will proceed as usual. You will attempt to read my memories; I will attempt to resist you.""",
  "annotation":"""<p>Past Harry doesn't talk very often.</p>""",
},
{
  "force_id":"8db14984a33472526b30ef0f73c987b9",
  "force_date":datetime.date(2012, 4, 9),

  "transcript":"""Harry and Snape face each other. Their eyes are joined by a beam of Legilimency. The beam opens into a narrative frame that shows one of Snape's memories. A note says "This page's dialogue is mostly from Harry Potter and the Order of the Phoenix, p. 646"<br/>
In the memory, a younger Snape, as a Hogwarts student, is lying on the grass near the lake, surrounded by three people who are taunting and laughing at zem: James Potter, Sirius Black, and Peter Pettigrew. James Potter has light skin and light brown hair, and green eyes, like Harry's. Ze has a relatively smooth appearance. Ze's pointing a wand at Snape, and sitting in a chair. The speech of James and Sirius, who are both in Gryffindor, is similar to the Slytherin students' speech we've seen, but less curvy, more upright.<br/>
JAMES: How'd the exam go, Snivelly?<br/>
SIRIUS: I was watching him, his nose was touching the parchment. There'll be great grease marks&ndash;<br/>
SNAPE: ..... ... { Snape actually says "....." and "..." as normal dialogue. }<br/>
JAMES: Wash out your mouth! Scourgify! { "Scourgify" is the incantation of a spell that cleans something with soap. }<br/>
Pink soap bubbles come out of Snape's mouth.<br/>
Lily Evans is standing nearby, leaning against a tree, arms crossed. Lily looks a lot like Harry; zir hair is a bit messy, and ze has a generally rough sort of appearance. Ze also has the darkest skin of any character we've seen so far, and dark eyes, unlike Harry's. Ze's wearing a baseball cap. Zir voice, like present Harry's, is drawn in red and is fairly rough, but is a less intense shade of red, and somewhat smoother, than Harry's.<br/>
LILY: Aw, leave him alone, Potter.""",
  "annotation":"""<p>Lily Evans didn't see any reason why being a wizard should stop you from wearing a baseball cap.</p>""",
},
{
        
  "content_warning":""""blood""",
  "force_id":"c567fac4bcbbd7eca4a1a259a72c68ab",
  "force_date":datetime.date(2012, 4, 14),

  "transcript":"""Still in Snape's memory:<br/>
Lily stands over James in zir chair, and James looks up at Lily.<br/>
LILY: How would you feel if you were in his place? If you were poor? If people hated you? He feels that way every day, Potter! And if you were on the ground and he was in that chair, how would you like it if I stood here and said, "Go on, Serverus, keep hexing Potter &ndash; it's hilarious &ndash;"<br/>
We see an image illustrating the hypothetical situation Lily describes. The young Snape is sitting on the chair, pointing zir wand down at James, who is lying on the ground. Some other people stand around. Lily stands by the chair and smiles at Snape.<br/>
Back in Snape's memory, the younger Snape has gotten up. Ze lunges at James, casting a curse which causes some cuts to appear on James's face.<br/>
SNAPE: Yah!<br/>
James looks back towards Snape angrily.<br/>
JAMES: Levicorpus! { The incantation of a spell that lifts a person into the air, usually for the purpose of bullying. }<br/>
Snape is levitated, upside down.<br/>
LILY { right behind James }: You're not listening to me! Let him go!<br/>
JAMES: Fine. Liberacorpus. { The counter-jinx to Levicorpus. }<br/>
JAMES: You're lucky Evans was here, Snivellus.<br/>
SNAPE { walking away }: Bah. Thanks, Evans.<br/>
The narrative frame of Snapes's memory closes. Back in Snape's office, Snape is breaking the Legilimency link with a hand.<br/>
SNAPE: That will do. Now...""",
  "annotation":"""<p>James is from a rich pure-blood family, and ze's very popular, so ze's basically at the top of wizarding society. Lily is not only a muggle-born, but also makes no attempt to hide it or conform to wizarding social norms. At any moment, people could start making fun of James for zir obvious interest in Lily.</p>

<p>So, to avoid that, James constantly reasserts zir dominant position by attacking Snape, who's unpopular and, not coincidentally, has a muggle parent.</p>

<p>Lily and James actually like each other, but their relationship is slightly cramped by James's refusal to acknowledge zir pure-blood privilege.</p>""",
},
{
  "force_id":"61bb5c3e5350aed7f4a25f089fde5b8d",
  "force_date":datetime.date(2012, 4, 21),

  "transcript":"""SNAPE: Tell me. What did you see?<br/>
PAST HARRY: Potter... James Potter... he was hexing you... with his friends... and that girl... my mother...<br/>
SNAPE: What did I say?<br/>
PAST HARRY: Uh... you asked me what I saw...<br/>
SNAPE: In the memory, Potter. What did I say while your father was hexing me?<br/>
PAST HARRY: You didn't say much. Just "thanks, Evans" there at the end.<br/>
SNAPE { angrily }: Then you saw nothing, because I modified that memory! You only saw what I wanted you to see. Subtlety, Potter. Subtlety!<br/>
Harry doesn't seem to be intimidated by Snape.<br/>
PAST HARRY: But I learned this too: You showed me that because you think I'm a proxy for James Potter. You're stupid. He means nothing to me.<br/>
SNAPE: How can you say such a thing about your own father?<br/>
PAST HARRY: YOu taught me how to dig through memories. You didn't tell me it would work on my own memories... but I had a lot of time to dig, this summer. And I found something I'd thought was buried forever.<br/>
We enter a narrative frame in which Harry describes a memory ze dug up. In the memory are Lily and James, with Harry, as a baby, in a cradle nearby. The scene is lit sharply by a candle lantern. By its light, Lily is grimly studying a large book. Lily is sitting in a chair while doing this; behind zem, James looks on with concern. James's appearance is relatively clean, while Lily's is relatively unkempt.<br/>
JAMES: You're not seriously still looking up spells.<br/>
LILY { without looking up from the book }: Put a sock in it. This one could be useful.""",
  "annotation":"""<p>In the last two pages, Snape conveniently omitted the parts where ze swore at James and called Lily a "filthy little Mudblood".</p>

<p>On an unrelated note, Harry knows the word "proxy" because spellbooks use it a lot.</p>""",
},
{
  "force_id":"4c2e37c9f44763fac556b59d04721d0f",
  "force_date":datetime.date(2012, 5, 6),

  "transcript":"""Still in Harry's description of zir memory.<br/>
JAMES: This is turning into an obsession for you! You can't&ndash;<br/>
LILY: Voldemort is hunting us, James! Do you know what that <em>means?</em> He could attack us at any moment&ndash;<br/>
BABY HARRY: WAAH! WAAAAAAAAAA<br/>
JAMES: Silencio! { The incantation of the Sliencing Charm. }<br/>
The baby Harry becomes silent.<br/>
JAMES: Dumbledore wants us to be living our lives, Lily, this isn't right&ndash;<br/>
LILY: Right? Of course it isn't right! It isn't right that we have to fight the fuckin'... <em>Wizard IRA</em> in the first place, but we have to!<br/>
JAMES: But&ndash;but&ndash;<em>no!</em> We <em>don't</em> have to! The Fidelius Charm&ndash;<br/>
LILY: Do you think that charm is invincible? Voldemort can probably rip the knowledge straight from Peter's mind if they catch him!<br/>
Lily looks rather dishevelled, and is clenching a scrap of parchment in one hand.<br/>
LILY { continuing zir monologue }: Or do you think we can fight him? The Boneses thought so too, do you remember them? Do you think I'm a better duellist than Dorcas Meadowes? She blasted his arm off before he got her, and <strong>he has a new arm now!</strong> He's not like other dark wizards, we'll need something more powerful, something he won't expect&ndash;<br/>
JAMES: Merlin's beard, just show me the spell if you care so much.<br/>
Lily hands James a scrap of parchment. James looks the other way while ze reaches zir hand out to accept it. Lily is looking down and brushing some hair off zir face with zir other hand.""",
  "annotation":"""<p>Every few years, there's a story in the <i>Daily Prophet</i> about a baby that died because its parent(s) left it silenced and forgot to take care of its basic needs. The Ministry formally classifies using the Silencing Charm on a baby as a form of child abuse, but this rule is almost never enforced, and very few parents are able to resist the temptation forever.</p>""",
},
{
        
  "content_warning":""""gore""",
  "force_id":"4e9ac96309df226c1177992a4714d954",
  "force_date":datetime.date(2012, 5, 7),

  "transcript":"""James holds up the parchment Lily handed zem. At the top are a bunch of symbols. Below them is Lily's translation.<br/>
PARCHMENT: Trans&ndash; (Evans) "sacrificial protection" being a spell to capture the life of the parent as a shield on the child. While the child remains in the houses of his fathers, the intruder's curse will be returned a thousandfold { then, in messier writing } (worth it as last resort?)<br/>
JAMES: This is insane! We'd be better off if you'd never started looking&ndash;<br/>
LILY: Think of all the people who will die after us if we do nothing!<br/>
JAMES: <em>Lily!</em> Neither of us is going to die!<br/>
VOLDEMORT: Ha. Ha.<br/>
Visually, all the details of the house disappear, and the ground becomes a wash of Voldemort's color. The sharp shadows of Voldemort and zir cat and snake loom towards Lily and James. James panics; Lily has an expression of grim determination.<br/>
JAMES: Wh&ndash; Stupefy! { "Stupefy" is the incantation of the Stunning Spell, which is supposed to render the target unconscious. }
The glare of the stunning spell illuminates Voldemort in a harsh light, but ze is entirely unaffected by it.<br/>
LILY: James, no! Get back!<br/>
VOLDEMORT: Boring.<br/>
Voldemort looks different now. Zir robe has no arms; Voldemort's right arm, which clutches zir wand, is a muscular human arm, but zir left arm is translucent and silvery. As before, zir face is hidden and ze is wearing a Time-Twister around zir neck.<br/>
Voldemort grabs James's hand in zir silvery hand and raises it above their heads. Then ze crushes the hand, with the wand inside it. Severed fingers and blood spill everywhere.<br/>
JAMES: AAAAAAAAAAAA<br/>
VOLDEMORT: I feel I've been here before... in my past... your future... I know what happens here.<br/>
James's wand lies in two pieces on the floor. One piece is stained with blood.""",
  "annotation":"""<p>A few years before this, when Lily was at Hogwarts, other students made fun of zem for focusing on the study of Ancient Runes instead of something more useful for self-defense, like Charms or Transfiguration.</p>

<p>The Ministry prohibits the possession of books of "dark magic", such as the one Lily got that spell from, without special authorization; the Hogwarts library has this authorization, but Lily does not. However, at the height of Voldemort's power, the Department of Magical Law Enforcement has more important things to do than bust people for having banned books. The law mainly functions as an excuse to make arrests if Ministry officials suspect someone of being a Death Eater and raid zir home, but don't find real evidence. Many people have such books out of curiosity, or for self-defense, or because "dark" spells were included in a book they had for unrelated reasons, but once it's gotten to that point, <abbr title="Department of Magical Law Enforcement">DMLE</abbr> agents don't stop to wonder if the accused might be innocent.</p>""",
},
{
        
  "content_warning":""""gore""",
  "force_id":"3751eddceaa7711b6f14a5c199e05c76",
  "force_date":datetime.date(2012, 5, 8),

  "transcript":"""VOLDEMORT: I ask myself... What will happen here, in the house of those who have thrice defied me? And I answer myself...<br/>
Voldemort's Time-Twister is glowing, and the entire page is dominated by a spiral of light reminiscent of the Time-Twister. The action of the page takes place between the glowing bands. Everywhere Voldemort appears on this page, tendrils of light connect the Time-Twister ze's wearing to the page background.<br/>
VOLDEMORT: First, I will punish James. He killed my cat, and this cat Inferius bores me. { An Inferius is a dead body reanimated and controlled by magic. It has no will of its own. }<br/>
Voldemort holds up one hand, carrying zir cat, and the cat leaps from that hand. Earlier, the cat had glowing eyes, but now, it is entirely black.<br/>
VOLDEMORT: But I will be too careless to make him suffer long.<br/>
The cat lands atop James, who is lying on the ground with zir bleeding hand. The cat raises a claw... and the next image is one of James's head, with both eyes ripped out, lying in a pool of zir own blood.<br/>
VOLDEMORT: I have little patience for human frailty.<br/>
The cat walks away.<br/>
VOLDEMORT: As he bleeds out, Lily will transfer his life energy to the child. I will think it is a romantic but useless gesture.<br/>
We see this happen. Lily stands between flat, iconic images of James and Harry. Creepy-looking tendrils of light emerge from James's face, and Lily directs them towards Harry.<br/>
VOLDEMORT: Lily killed my snake. A dead snake is alright. I will spare her and keep her out of the way.<br/>
Voldemort's snake, which is now pale and has black eyes instead of glowing ones, leaps at Lily and grabs zir wand from zir hand, then coils around zir head and arms, trapping zem.<br/>
VOLDEMORT: I will pause to muse that I have never exploded a baby before... and then...<br/>
Voldemort stands in front of the Time-Twister's bands. Lily, right behind zem, is wrapped three times around by the snake and can't reach zir wand, which is still in the snake's mouth. Voldemort reaches down and points zir wand at Harry's forehead. Lily has a very tense expression on zir face; Voldemort is as impassive as usual.<br/>
VOLDEMORT: <strong>Confringo.</strong> { The incantation of the Blasting Curse. }""",
  "annotation":"""<p>Writing and drawing this page took me nine hours...</p>

<p>In the original series, Voldemort is a fairly generic fantasy villain &ndash; a plot device, an easy source of conflict ("How will the heroes defeat the villain this time?! Find out next chapter!") and a caricature. Dumbledore describes zem as "without love", as if that explains why ze wants to torture people and conquer the world.</p>

<p>What other roles can a powerful villain serve in a story? What could cause a person behave as Voldemort does?</p>""",
},
{
  "force_id":"de3f982885ac20277bb220920270d5ed",
  "force_date":datetime.date(2012, 5, 9),

  "transcript":"""VOLDEMORT: Confringo.<br/>
Everything explodes, especially the Time-Twister.<br/>
The narrative frame of past Harry describing zir memory closes. We are back in Snape's office.<br/>
PAST HARRY: The memory ends there. But I know what happened. The explosion destroyed Voldemort's body. Lily died. I lived. The Aurors hunted down the bits of his soul and destroyed them... leaving me here with the Dursleys... the Malfoys... He may be gone from this life, but Voldemort is my past, present, and future... So you want to know how I can hate James Potter. He did nothing to protect me. He&ndash;<br/>
Harry becomes visibly upset, crying.<br/>
PAST HARRY: I'm not like him, I don't want him to be part of me... ...that spell... "in the houses of his fathers"... is that why Dumbledore&ndash;<br/>
SNAPE: <em>Professor</em> Dumbledore, Harry&ndash;<br/>
Crying, Harry runs out of the room and down the corridors of Hogwarts, to Luna, who is standing on a table. Harry collapses in front of the table.<br/>
PAST HARRY: Luna, help me, please, I need something to change. Anything.<br/>
LUNA: Of course I'll help you! But if you want to change things, you've got to understand the seats of influence.""",
  "annotation":"""<p>How would this have gone differently if Snape had given Harry a hug instead?</p>

<p>I briefly considered doing that (but still having Harry, after the "<em>Professor</em>" line, reject Snape's affection and run away). But, no, Harry's world is a world of very little affection. There's an interesting compromise going on here, between the <em>atmosphere</em> of the world and the <em>action</em> of each page: Setting the atmosphere is very important, but when characters being emotionally distant happens so often, it doesn't have any special impact when it does happen.</p>

<p>On another note, Voldemort has some very cool lines in the <i>Harry Potter</i> series. "Voldemort is my past, present and future" is something that ze (as the memory of Tom Riddle) says in the second book. One of the coolest things about "alternate universe" fanfiction in general is when you can take an event from the original story, but show it in a different context and with different reasons behind it.</p>""",
},
{
  "force_id":"810016b3a8050b13cd8924955746b6c2",
  "force_date":datetime.date(2012, 5, 10),

  "transcript":"""LUNA: Well, there's a lot of different seats in our world.<br/>
A large metaphorical illustration appears. There are three chairs, labeled "Headmaster of Hogwarts", "Minister of Magic", and "Chief Warlock of the Wizengamot". There are many colors of double-headed arrows pointing between adjacent chairs. From the left, four arrows labeled "Parents" point from off-page towards the Headmaster chair. From above, four arrows labeled "Voters" point from off-page towards the Minister chair. From the right, four arrows labeled "Precedent" point from off-page towards the Chief Warlock chair. From below on the page, giant arrows in Voldemort's colors rear up and point at everything.<br/>
LUNA: But my dad says they all have the same weakness. They make you sit still! If you move too much towards something different, you just fall out. Think about it! If Dumbledore tries something unpopular like respecting us, he'll be gone in no time.<br/>
PAST HARRY: Then everyone is evil and we should just give up.<br/>
LUNA: Aww, you're a pessimist, like my dad! But I realized there's one role that's not influenced by the seats. Where you can change everything and no one stops you. It's called being a Dark Lord!<br/>
Luna appears as a Dark Lord. Ze's carrying two wands, which are the source of the "Voldemort" arrows in the picture above. Zir face is obscured, but unlike Voldemort, ze's smiling, which is probably rather disconcerting.<br/>
LUNA: Will you be Dark Lords with me, Harry?""",
  "annotation":"""<p>Are these the opinions of the author? Does it matter? One might say an idea should be judged on its own merits, not on the existence, or lack thereof, of the person suggesting it.</p>

<p>Luna is being pretty blunt here. Do you think ze's oversimplifying how society works? Or do you think ze's using just the right amount of simplification?</p>

<p>Would <em>you</em> like to be Dark Lords with Luna?</p>

<p>On another note, I've got a question for y'all about the transcript. So far, I've mostly avoided referring to specific colors (green, blue, etc); I think that's a bad idea, and I'd like to have the transcript say what the colors on the page are. But <em>describing</em> the colors is a bit of a problem. For instance, I could describe the color of Voldemort's cat's eyes (when it was alive) as "orange", but there's a lot of different shades of orange; just saying "orange" doesn't specify that the eyes are exactly the same color as the Cruciatus Curse, which is symbolically semi-important. So I want a way to specify that, but how do I do it? I could refer to that color by the same phrase everywhere (e.g. "The orange of Voldemort's cat's eyes"), but that's very awkward and unnecessarily gives more weight to one specific use of the color. I could give its HTML code ("#ffc800"), which is exact, but that's obviously a bad idea. Any suggestions?</p>""",
},
{
        
  "content_warning":""""violence""",
  "force_id":"cd5430abf56bfbfc370d376919c9e550",
  "force_date":datetime.date(2012, 5, 12),

  "transcript":"""Past Harry has leapt up onto the table where Luna is standing.<br/>
PAST HARRY: You're mad! The Dark Lord killed my parents! I'll never be a Dark Lord, never!<br/>
Harry shoves Luna with one hand. One leg of the table cracks under them. Harry's other hand is swung back, as if ze's about to punch Luna.<br/>
PRESENT HARRY: I was a fool... now I rue every day I delayed the moment when we would be joined together as equals.<br/>
Harry, Luna, and a silhouetted figure stand in a circle, raising their wands to conjure a three-way yin-yang shape. Their faces are blank.<br/>
PRESENT HARRY: I know you have not caught her. You never will. She has powers even I don't know about. She will rescue me, Granger. She is coming, even as we speak, and there's nothing you can do to stop her!<br/>
The narrative frame of present Harry describing the past closes. In the interrogation room, a green fire springs up in a nearby fireplace, and a silhouetted shape appears in the fireplace. Green smoke floats into the room. Granger and Tonks face the fireplace, wands drawn.<br/>
TONKS: What the&ndash;<br/>
GRANGER: Protego! { The incantation of the Shield Charm. }<br/>
A hemispherical shield appears between Granger and the fireplace.""",
  "annotation":"""<p>Thus ends Chapter Three, "Seats of Influence".</p>""",
},
{
  "force_id":"2ac6629f7a8dfa8c13660be159335bea",
  "force_date":datetime.date(2012, 5, 13),

  "transcript":"""CHAPTER FOUR<br/>
<br/>
An image of Granger sitting at a desk, doing paperwork. There's a parchment right in front of zem, and ze's about to write on it with a quill pen; to one side is a huge stack of pages, which is constantly being piled on by more that fall from the darkness above. Voldemort is standing behind Granger; Granger isn't looking at Voldemort, but with zir other hand, Granger is pointing zir wand over zir shoulder to conjure a bright magic shield to keep Voldemort away. The floor of the entire scene is covered in shallow water (so Granger's feet and the table and chair feet are in the water), and papers Granger is done with are falling off the side the table and into the water.<br/>
At the bottom is the chapter title:<br/>
The Daily Struggle for Dignity""",
  "annotation":"""<p>A slight change of pace.</p>

<p>It always takes me a while to come up with these visual metaphors, but I really like them once I finish them.</p>
""",
},
{
  "force_id":"ca22fb2303c220c564f9b9f60f5ef021",
  "force_date":datetime.date(2012, 5, 13),

  "transcript":"""Tonks and Granger face the fireplace, where someone's head is surrounded by green fire; this is the normal way people communicate using the Floo Network. Granger's shield floats between them.<br/>
GRANGER: Identify yourself.<br/>
FIREPLACE HEAD: No need to shield! Percy Ignatius Weasley, secretary to the Minister. You asked to be reminded that the DMLE senior staff meeting begins in a half-hour. The Minister will attend.<br/>
Percy is smiling, but Tonks looks annoyed.<br/>
GRANGER: Thank you, Percy. However, this room should not be connected to the Floo Network, as it poses a security risk.<br/>
PERCY: I'll notify the relevant authorities immediately.<br/>
Granger and Tonks head back up the stairs.<br/>
GRANGER: "No need to shield"? Fudge's office doesn't know ours. An Auror shields first and acts surprised later.<br/>
TONKS: ...Unless she's an infiltrator and needs her reactions not to give her away. { Tonks is referring to zemself. }<br/>
GRANGER: Of course, Tonks.<br/>
They reach the top of the stairs. A trail of magical energy indicates that Granger has flown up by magic, the same way ze descended. Tonks has walked.<br/>
TONKS: Do you have a lot to do before your meeting?<br/>
GRANGER: Just one thing...<br/>
Granger starts to pull a Time-Twister from under zir coat; presumably, ze has been wearing it this whole time.<br/>
GRANGER: I wouldn't want to disrupt anyone's schedule by wearing this.<br/>
TONKS: You still <em>have</em> that thing?""",
  "annotation":"""<p>A cliffhanger that turns out to be something completely banal? Percy Weasley unintentionally makes life annoying for everyone, including the reader!</p>

<p>Did Granger and Tonks just leave Harry restrained in a cell? Yes, but the Department of Magical Law Enforcement (DMLE) operates on a strict schedule, and there will be other people along shortly to take care of Harry's physical needs.</p>

<p>Also, with this page &ndash; if we assume that the characters are all actually the genders people assume about them &ndash; <i>Voldemort's Children</i> finally passes the Bechdel test. (The Bechdel Test is "(1) it has two female characters in it who (2) talk to each other about (3) something other than a man". Granger and Tonks talked to each other on the first two pages, but it was about Harry.) It took this long because almost all conversations so far have included Harry; by comparison, if Harry was female, we wouldn't have passed the reverse test yet (unless you count James and Sirius when they were bullying Snape), and wouldn't pass it until chapter seven, when there will be a flashback where Dumbledore talks to the young Tom Riddle.</p>""",
},
{
  "force_id":"b71531d0ccad6bbffed887bc25ff7bc3",
  "force_date":datetime.date(2012, 5, 14),

  "transcript":"""GRANGER { talking about the Time-Twister }: There is no safe place to store an object that can do this much damage. Even Gringotts can be robbed. I barely trust this magically locked desk, even for a few hours. I'm certainly not going to return it and let them issue it to someone else&ndash; the regulations are insufficent to what the research demands.<br/>
Granger uses a key to unlock a drawer in a desk, and puts the Time-Twister inside.<br/>
TONKS: It's blue-shifted, I hope you haven't been <em>using</em> it&ndash;<br/>
GRANGER: Not myself, no. Each extant Time-Twister resonates with the others. Somewhere, someone is overusing one. If the damage will be done either way, I might as well use that to my advantage. Join me in the lounge while I stabilize?<br/>
They go to the lounge and sit in comfy chairs. Tonks is slightly restless in zir chair; Granger takes a more relaxed but slightly formal posture.<br/>
TONKS: About Potter... Not that I'd question your judgment, but why'd you promise not to give him the truth potion?<br/>
GRANGER: The truth potion? It makes the subject answer the questions you ask, and no more. I am not such a fool as to believe that I know all the right questions.""",
  "annotation":"""<p>Does Granger make zir choices for moral reasons or for practical ones? When do those overlap, and when do they differ?</p>

<p>Time-Twisters are normally yellow, the color of the band from <a href="/main/posts/166-voldemort's-children-page-7">this page where Voldemort activates one</a>. They're only blue when they're active, which they have been every time we've seen one.</p>

<p>The desk works like Moody's trunk from the books: If you open it with Granger's key, you'll find the drawer with the Time-Twister in it, but if you open it with a different key, you'll find something different. If you open it with the kind of lockpicks you can get from Weasleys' Wizard Wheezes, you'll find a high-tech burglar alarm system. Tonks personally disguised zemself as a Hogwarts student (Fred and George don't usually sell to <abbr title="Department of Magical Law Enforcement">DMLE</abbr> agents) and bought a set in order to make sure DMLE security is safe against the current tools available.</p>""",
},
{
  "force_id":"6c9f09af7218c634ca266ecb3d24c7fa",
  "force_date":datetime.date(2012, 5, 16),

  "transcript":"""TONKS: What are these meetings like, anyway? You don't talk about them much.<br/>
GRANGER: It is not professional to complain about one's duties.<br/>
TONKS: That bad, huh?<br/>
GRANGER: Well...<br/>
We enter a narrative frame in which Granger describes a recent DMLE senior staff meeting. Granger and five other people, including Bartemius Crouch senior, stand around a long table.<br/>
PAST GRANGER: I have every faith in my trackers, but Potter seems untraceable. Therefore, I propose a strategy that will force Potter to come to us. He has often targetted those accused of using the Torture Curse on Muggles or other wizards, as he believes he knows who has truly used the Torture Curse and who has n&ndash;<br/>
Barty Crouch interrupts. Ze is frowning sharply and zir speech is drawn in a harsh, rigid style.
CROUCH: In my time as an Auror, we called the Cruciatus Curse by its <em>proper</em> name.<br/>
PAST GRANGER: Excuse me, Mr Crouch, but the policy of the Auror Office is now&ndash;<br/>
CROUCH: I understand this to be a policy of <em>Hermione Granger</em>. Another ill-informed, soft&ndash;<br/>
PAST GRANGER: Mr Crouch, if we use that name in the field, it is so similar to the incantation that it can cause false alarms or serve as a potent reminder of the trauma that civilians or other Aurors may have experienced. Surely you can understand the tactical significance.<br/>
PRESENT GRANGER: In private, we can say that it is a common trigger for posttraumatic stress disorder. Muggle science far outstrips our own in understanding the human mind. However, one would hardly appeal to the authority of a Muggle before Bartemius Crouch.<br/>
PAST GRANGER: As I was saying, it should be possible to set a trap for Potter.<br/>
Kingsley Shacklebolt replies. Ze has a friendly demeanor and zir speech is drawn in a somewhat curvy style.<br/>
SHACKLEBOLT: Very logical, but who in their right minds would play the bait?<br/>
PAST GRANGER: As a matter of fact...""",
  "annotation":"""<p>The Aurors under Granger, as a matter of policy and habit, don't say any word that contains the syllable "cru-". "crew" becomes "team", "crucial" becomes "essential", and so on. "Cruciatus Curse", of course, becomes "Torture Curse". They also refer to the Imperius Curse as the "Control Curse"; the PTSD issue is much less for that one, but the "false alarm" issue is especially relevant, since an indoors, apparently-friendly situation is the one in which you need to be the most vigilant against people <em>actually</em> casting the Imperius Curse.</p>

<p>From left to right: Arthur Weasley (Head of Misuse of Muggle Artefacts Office), Pius Thicknesse, Bartemius Crouch, Amelia Bones (Head of <abbr title="Department of Magical Law Enforcement">DMLE</abbr> as a whole), Hermione Granger (Head of Auror Office), Kingsley Shacklebolt. In the books, it's not specified exactly what career path Crouch took to becoming the head of DMLE (while Voldemort was in power &ndash; ze was later demoted), but I decided it was natural that ze had been an Auror at some point along the way.</p>

<p>Arthur Weasley will wake up when they start talking about misuse of Muggle artefacts, which will probably be never.</p>

<p>Tonks, of course, is one of the trackers Granger refers to. Ze's very good, but people who haven't worked with zem sometimes have trouble believing in zir skills because of the informal, casual way ze approaches everything.</p>""",
},
{
  "force_id":"61989a1205a975589721a63747b7f121",
  "force_date":datetime.date(2012, 5, 17),

  "transcript":"""Still in Granger's description of the earlier DMLE senior staff meeting.<br/>
PAST GRANGER: ...I have already been contacted by a person seeking our protection, who seems like the ideal candidate. You may have heard of Alecto Carrow.<br/>
Pius Thicknesse smirks.<br/>
THICKNESSE: Oh, I think we <em>all</em> know Alecto Carrow.<br/>
PAST GRANGER: Excuse me?<br/>
CROUCH: Is Granger unaware of the number of reports we receive from that woman?<br/>
Inside a short narrative frame, we see Crouch's opinion of what Alecto Carrow does. One of Alecto's eyes is wide open, and the other is squinted; in general, ze's a caricature of a crazy person. Ze's writing messily on a parchment, and an owl is perched nearby, as if ze's writing a note that will be sent by owl to DMLE.<br/>
ALECTO: The bushes are rustling again! It must be a murderer!!<br/>
That narrative frame closes.<br/>
CROUCH: We simply do not have time to waste on&ndash;<br/>
PAST GRANGER: I'm sure no one here would mean to imply that the fears of a witch whose brother was recently murdered under similar circumstances are illegitimate. As you know, before his death at Potter's hand, Amycus Carrow was involved in a charity alleged in the <i>Prophet</i> to be a cover for procuring Muggles for torture. Our own investigation seems to clear Alecto of involvement, but the <i>Prophet</i> is now sitting on an article that implicates her as well. I intend to let them publish it, and secretly place Alecto under constant guard.<br/>
The narrative frame of Granger describing the DMLE meeting closes.<br/>
TONKS: There's one thing that's been bothering me...<br/>
GRANGER: Do tell.""",
  "annotation":"""<p>You've actually seen Amycus Carrow before. <a href="/main/posts/167-voldemort's-children-page-8">Ze was the one killed in front of the white steps on this page</a>.</p>

<p>Granger saying "I intend to let them publish it" implies that Granger has the power to stop the <i>Daily Prophet</i> from publishing a story. This is, in fact, true; a high-ranking Ministry official such as Granger can effectively block any story the <i>Prophet</i> wants to print. If Granger's other implication is correct, and Potter is willing to pursue and kill a person based on accusations in the <i>Prophet</i>, then what do you think of the ethics of this? Is it acceptable to publish a story when you know a person is likely to kill based on what it says? Is it acceptable for another person to stop you from publishing it?</p>""",
},
{
  "force_id":"6f7203fd9b69e1b36e401466051e2e5e",
  "force_date":datetime.date(2012, 5, 19),

  "transcript":"""Harsh lighting. Tonks leans forward in zir chair as if looking at something in the distance.<br/>
TONKS: What if he's right? We know he's a powerful Legilimens&ndash; if he really knows who's guilty, what does that make us? Are we just protecting torturers?<br/>
GRANGER: Ah. <em>That</em> question. {pause} I could list for you the people whom Potter has killed without giving any reasons: the Slytherin students; Gilderoy Lockhart; Sirius Black; Arnold Peasegood&ndash;<br/>
TONKS: Who?<br/>
GRANGER: &ndash;He worked for the Accidental Magic Reversal Squad as an Obliviator... Does that answer satisfy you?<br/>
TONKS: I guess it does...<br/>
Granger stands over Tonks in a slightly intimidating way.<br/>
GRANGER: It <em>shouldn't</em>. You knew most of that already, and you still had a question. You should trust yourself that the question is worth asking, because when you find your answer, you'll be a better Auror and a stronger person, but if you always let the complications make you delay answering, you won't.<br/>
Granger pulls back a sleeve to reveal a wristwatch.<br/>
GRANGER: Ah, excuse me. The time.<br/>
Granger starts to leave for the DMLE meeting.<br/>
TONKS: Maybe they'll show more respect now that your plan <em>caught</em> Harry Potter.<br/>
GRANGER: I suppose that is possible.""",
  "annotation":"""<p>Did Granger just dodge a question? What exactly is ze doing here?</p>

<p>Granger has a magical wristwatch that shows both zir own personal time and Ministry Common Time. The latter is unreliable while ze's using the Time-Twister, but it syncs up after a few minutes outside its effects.</p>""",
},
{
        
  "content_warning":""""violence, blood""",
  "force_id":"f4743f2324f586f0f88766251ac404f0",
  "force_date":datetime.date(2012, 5, 20),

  "transcript":"""In the present DMLE senior staff meeting.<br/>
BONES: We will begin today's meeting with the Auror Office report. Granger?<br/>
GRANGER: Thank you, Madam Bones. I received John Dawlish's distress call at 21:40 {9:40 PM} on Monday, his shift guarding Carrow. Naturally, I gathered the Aurors on call and Apparated to an adjoining room at once.<br/>
We enter a narrative frame in which Granger describes past events.<br/>
Granger, Shacklebolt, and Tonks are standing in the Auror Office lounge. They Apparate from there to a different room, where there is a doorway. Voices are heard from the next room.<br/>
ALECTO {not yet visible}: Please don't hurt him, I don't want more trouble&ndash;<br/>
HARRY {not yet visible}: This isn't about you, Carrow, it's about the people he'll&ndash;<br/>
Harry, Alecto, and three others come into view through the door.<br/>
GRANGER: Stun, then shield. Aim high.<br/>
The next room is furnished with a candelabra and a writing desk. The desk has a parchment and quill pen on it, but the inkwell has been knocked over and spilled across the page. Near the desk, Harry is standing over John Dawlish, who is wearing a trench coat identical to the one Granger wears, and bleeding from the shoulder. Harry is pointing zir wand at Dawlish, who is desperately trying to defend zemself.<br/>
HARRY: Sectumse&ndash; { The beginning of "sectumsempra", the incantation for a curse that causes severe cuts on the victim's body. }<br/>
DAWLISH: Prote&ndash; { The beginning of "protego", the incantation for the Shield Charm. }<br/>
Luna and a silhouetted figure stand nearby, wands out. Near Dawlish, Alecto Carrow is sitting on the floor, with one wrist chained to a leg of the desk behind zem. Ze has zir eyes closed tight.<br/>
ALECTO: Please, no! No, no, no&ndash;<br/>
SHACKLEBOLT, GRANGER, AND TONKS: Stupefy! { The incantation of the Stunning Spell. }<br/>
Jets of red light shoot everywhere. The candelabra breaks and falls. Harry gets hit in the back of the head and crumples to the floor. Luna appears to get hit in the face, but be unaffected.<br/>
SHACKLEBOLT AND TONKS: Protego!<br/>
GRANGER: Aegidivitrea! { A non-canon spell; loosely, Latin for "glass shield". }<br/>
Following the stunners, the three Aurors approach, surrounded by a huge, round shield made of blue-green glass, plus the regular "Protego" shields.<br/>
LUNA: Oh, hello, Hermione!""",
  "annotation":"""<p>I've waited a long time for Granger to get into a situation where ze wants to use that spell!</p>

<p>In the books, they say that the Killing Curse is unblockable. Presumably, what that means is that the Killing Curse is too powerful to be blocked by <em>magical shields</em>, since, literally speaking, it gets blocked by various things, including a phoenix, an animated stone statue, and the power of love. Granger doesn't like relying on lucky circumstances, so ze decided to develop a spell that could block the Killing Curse reliably. In <i>Voldemort's Children</i>, love can't block curses, so ze had to stick to using a physical object.</p>

<p>So, Granger invented "Aegidivitrea", the Glass Shield Charm (ze's very practical about naming things). It conjures a thick shield of glass around the caster and anyone else the caster wishes to protect, and continuously keeps the glass hovering in the air. Since it's a solid object, almost all curses will bounce off of it. The easiest way to attack the shield is with a spell like the Blasting Curse ("Confringo"), but those spells can be blocked normally, so when coupled with the regular Shield Charm, as the three Aurors are doing here, it's very hard to attack.</p>

<p>The main catch is that conjuration is permanent in this universe. It's easy to make the glass disappear again, but if you become incapacitated somehow and can't do that, there's a ton of unsupported glass ready to fall down on top of you. So the Aurors only use the spell when they are travelling in groups of two or more, so that they can cover for each other. And fighting in groups is the ideal way for Aurors to operate in any case.</p>

<p>(You might think there's another weakness in that the shield blocks spells you cast from the inside just as much as it blocks spells your opponents cast from the outside, but it's easy to create little holes in the shield to cast spells from, while your opponents will have a very hard time hitting those holes accurately.)</p>""",
},
{
        
  "content_warning":""""blood, wrist damage""",
  "force_id":"ffc08f1eec255a8cced7f8b066fdb02b",
  "force_date":datetime.date(2012, 5, 22),

  "transcript":"""The three Aurors point their wands at Luna. Luna smiles innocently and shrugs.<br/>
LUNA: I'd stay to chat, but I'd rather not get arrested. Bye!<br/>
Luna raises zir wand and conjures a zigzag of light, which engulfs zem and apparently transports zem out of the room.<br/>
TONKS: Is she gone?<br/>
GRANGER: Homenum revelio. { The incantation of a spell that reveals nearby people, including if they're invisible. } She's gone. Tonks, trace that spell. Kingsley, you make sure the attackers are stunned and restrained, then help Dawlish. I will see to Alecto.<br/>
Tonks waves zir wand in a circle.<br/>
TONKS: There's nothing I can trace! It's like she wasn't even here!<br/>
Shacklebolt looks over the fallen bodies. Harry is sprawled over Dawlish's lap; Dawlish is now trying to sit up, and looks down at Harry without much emotion. Shacklebolt is looking at the other stunned person, who is still hidden as a silhouette.<br/>
SHACKLEBOLT: We've got Potter and... who's this? It can't be!<br/>
Granger kneels near Alecto and takes zir chained wrist in one hand. Alecto looks away and cries from one eye. Granger taps the chain with zir wand, causing it to disintegrate, then holds Alecto's limp hand in zir hand. There is a laceration across Alecto's wrist. Blood drips from it.<br/>
GRANGER: Hmm.""",
  "annotation":"""<p>Wizard chains don't have keys. Wizards just conjure them in place and then remove them by magic when they're finished.</p>""",
},
{
  "force_id":"9fca0d04ffe17f4f08a93947e4a11653",
  "force_date":datetime.date(2012, 5, 24),

  "transcript":"""Past Granger kneels near Alecto. Alecto is now holding zir wrist close to zir chest.<br/>
PAST GRANGER: Dawlish, how did Carrow come to be chained like this?<br/>
Dawlish is crawling out from under Harry. Ze looks irritated.<br/>
DAWLISH: Before Potter attacked, she was acting mental. She tr&ndash;<br/>
PAST GRANGER: And you chained her here?<br/>
DAWLISH: Yes, she&ndash;<br/>
PAST GRANGER: You are aware of the protocol for short-term restraint?<br/>
DAWLISH: Yes, but&ndash;<br/>
PAST GRANGER: Thank you, Dawlish.<br/>
DAWLISH: She tried to stab me with a muggle pen!<br/>
The narrative frame of Granger describing the events of Harry's capture closes. We are back in the present DMLE meeting. In addition to the people we've seen before, Cornelius Fudge is present; ze sits at the opposite end of the table from Amelia Bones.<br/>
GRANGER: I saw no Muggle pen in the residence, but perhaps he mistook something else for a pen; his ignorance of Muggle culture is quite plain. What is <em>not</em> uncertain is the extent of the injury to Carrow's wrist; the evidence I have gathered suggests that she was left in that position for nearly two hours while Dawlish stood guard. The threat of Luna Lovegood is the primary subject I will bring before this meeting, but we must reserve some time to discuss the conduct of John Dawli&ndash;<br/>
CROUCH: "Conduct"? He was injured in battle with Harry Potter! He deserves the Order of Merlin, First Class, no question!<br/>
GRANGER: And before that happened, he broke protocol to injure an innocent person.<br/>
THICKNESSE: You're worried about a little <em>protocol</em> from someone who just <em>caught Harry Potter</em>?<br/>
GRANGER: There is no higher duty of this office than to ensure the safety of those we serve!<br/>
CROUCH: You have no right to lecture us about duty!<br/>
BONES: I do not see eye to eye with Granger on this matter, but I am curious, Mr Crouch, why the Head of the Auror Office would not have the authority to speak on Auror Office principles!<br/>
FUDGE: I hardly think Barty Crouch is the one in the wrong here! Granger is&ndash; she's only&ndash;<br/>
THICKNESSE: Ah, Minister, careful&ndash;<br/>
The argument rages on, but no more of the dialogue is legible to the reader; instead, strings of non-word symbols, colored like the characters' normal dialogue, spiral around the table. At the center of the spiral, Shacklebolt says "If we could all calm down for a&ndash;", but it seems that everyone ignores zem. The next thing the reader sees is Granger coming out a door, where ze is greeted by Tonks.<br/>
TONKS: Wotcher, Granger, the Aurors are waitin&ndash; wow, you look mad knackered!<br/>
Indeed, Granger looks very tired.<br/>
GRANGER: I always look like this after department meetings.<br/>
TONKS: Well, we're all waiting in the Strategy Room for you to speak. I think some of us are impatient&ndash; you said you'd be quick.""",
  "annotation":"""<p>This page was an exercise in deciding which information was the most important. There's a huge amount of backstory &ndash; I know the details of the injury, I know the attitudes of all people in the room, I know the defenses Granger would make to a variety of counterarguments, I even know exactly what happened between Alecto and Dawlish (though Granger doesn't) &ndash; but my sense of the narrative flow says I shouldn't spend too much time in this argument, so I have to cut a lot of that out.</p>

<p>Feel free to ask about anything in the comments, though!</p>""",
},
{
  "force_id":"592d88ee94e6529e799cca92e9569706",
  "force_date":datetime.date(2012, 5, 25),

  "transcript":"""Granger and Tonks walk in through the double doors of the Strategy Room, where the other Aurors are already standing in rows. Shacklebolt, Dawlish, and Alastor Moody are in the front row. Moody stands out with zir scars, wooden leg, and bright magical eye. Tonks heads for a back row; Granger strides out in front of the others and makes a speech.<br/>
GRANGER: Thank you for your patience. I will attempt to be brief. { pause } We have suspected for months that Potter has two primary accomplices, and that one of them is Luna Lovegood. This is now confirmed. Potter and the other are now in our custody, but Lovegood is still free. Four of us have seen her take a direct Stunning Spell and be unaffected, then escape by a means similar to Apparition, but untraceable. We don't know what her powers are or where they come from. I will meet with you again this evening to discuss our strategy against Lovegood; before then, I have a grim errand to complete. { pause } This puts us in an uncertain position. In these circumstances, I understand there may be some temptation to... well, to jinx first and ask questions later, especially when we have spells such as the Disarming Charm that are designed to neutralize an opponent without doing too much harm. However, there have been recorded instances in which even the Disarming Charm has hurled a person clear across a room, resulting in injury or death. { pause } No Auror has killed a person by accident since before Voldemort's defeat. I do not intend for any of you to be the first. Thus, if I discover that one of my Aurors has cast <em>any</em> offensive spell without reasonable justification to use force, I will personally make sure that that person no longer works for this office. Understood?<br/>
A pause. Then:<br/>
DAWLISH: Are you r&ndash;<br/>
Dawlish is cut off by Moody. Moody's speech is drawn in a heavy, rough, dark gray style.<br/>
MOODY: Understood.<br/>
DAWLISH { in a much smaller voice }: I still have no idea how she got <em>Moody</em> on her side.""",
  "annotation":"""<p>This page was informed by my thoughts about Tasers.</p>

<p>Who is Dawlish talking to? Ze could be muttering to zemself, or ze could be talking to Gawain Robards, the one further to the right. Robards might have some reason to resent Granger as well; in the books, ze became the Head of Office after Scrimgeour left, but here, ze was upstaged by the much younger Granger.</p>

<p>I think there are about twenty Aurors in total. The four in the front are the senior Aurors (whom you can also recognize by their darker coats/robes). To gain seniority, an Auror has to both be exceptionally skilled and be around for a long time. Tonks is skilled enough to be one, but ze's relatively new. Dawlish probably isn't skilled enough to qualify; ze was granted seniority under the somewhat corrupt leadership of Rufus Scrimgeour. (Granger became an Auror at about the same time as Tonks, but ze counts as a senior Auror because ze's the Head of Office.)</p>

<p>I decided not to have Moody retire &ndash; there's no particular reason for that, but I wanted to have zem as a character to play with, and making zem be a current Auror was an easy way to make zem relevant to the plot. I'm already rearranging the timeline of the backstory for other reasons, so perhaps this is simply a younger Moody than the one we meet in the books.</p>""",
},
{
  "force_id":"9fb0d64b0da73fb10769ef5176ec4616",
  "force_date":datetime.date(2012, 5, 25),

  "transcript":"""GRANGER: I will leave on my errand in, perhaps, a few hours. Meanwhile, let us make the most of the time when Potter is in our custody, rather than the courts'.<br/>
TONKS: So, what's your errand?<br/>
GRANGER: Whether it succeeds or fails, you will learn this evening.<br/>
TONKS: Okay... { pause } You're still worrying about the business with Dawlish, aren't you.<br/>
Granger and Tonks are descending the huge spiral stairs to where Harry is kept; as usual, Tonks walks and Granger flies. They are dwarfed by the staircase. It takes Granger a while to respond.<br/>
GRANGER: ...Yes. I have warned him before. That only means that I could have anticipated this. The wrist will heal with the right magic, and I will maneuver Dawlish off the force; all will be repaired, and yet... I cannot escape responsibility for what was done to Alecto, because it was I who gave the order for him to guard her. Perhaps she would have died if I had not. Does that make it right?<br/>
Granger approaches a door at the bottom of the stairs and reaches for the handle.<br/>
GRANGER: My mind turns to the story of Lily Evans, and how a person may do a thing not because it is right, but because she has to.""",
  "annotation":"""<p>Thus ends Chapter Four, "The Daily Struggle for Dignity".</p>

<p>Tonks has known Granger since Auror training, so ze has a good intuition for what Granger is thinking.</p>

<p>Granger will probably convince Dawlish to accept a cushy retirement as a hero. Granger has the ability to fire Dawlish, but Dawlish is respected by a lot of people, so that would create a spectacle that would be very costly (in time, effort, and reputation) for Granger. This would not be entirely bad, because it would show the world that Granger intends to follow zir principles even when it is not convenient for zem, but I doubt it would be the best use of Granger's resources at this time.</p>""",
},
{
  "force_id":"5f63013ab12e69a278930e0782bd17a5",
  "force_date":datetime.date(2012, 5, 27),

  "transcript":"""CHAPTER FIVE<br/>
<br/>
A metaphorical image: Voldemort's two hands, at a huge scale, loom into the page from the left and right. Harry Potter and Draco Malfoy, at a much smaller scale (their entire bodies are barely bigger than Voldemort's hands) dangle from them; Voldemort is lifting them by the backs of the necks of their robes, strangling them. Their faces are reddened. Harry is in zir usual student robes, but Draco is in a white robe. As usual, Harry's body is significantly bulkier and rougher-looking than Draco's. Both of them have all body parts except their heads concealed in the robes, making them look a bit like cocoons. Both of them are staring into space; they have fairly neutral expressions, and aren't looking at each other or away from each other, as if each is alone in space. Harry doesn't have zir glasses on.<br/>
At the bottom is the chapter title:<br/>
In The Houses Of His Fathers""",
  "annotation":"""<p>Who is the main character of <i>Voldemort's Children</i>? Is it Granger, who is our eyes and ears in this world? Is it Harry, whose struggle is at the center of the narrative? Or is it the inscrutable Lord Voldemort, whose influence seems to reach into every corner?</p>""",
},
{
  "force_id":"6d40b8b2ea4869556fdca157ee85b53f",
  "force_date":datetime.date(2012, 5, 28),

  "transcript":"""Granger is speaking to Harry in the interrogation cell.<br/>
GRANGER: This morning, you were telling us about your third year. You must have met Sirius Black that year, after he was released.<br/>
The word "released" opens into a narrative frame with one image in it, of Sirius being released from Azkaban. In front of Sirius, a junior Auror is carrying two broomsticks, and offering one to Sirius. Behind zem, two Dementors are standing near a barred gateway. The Dementors wear dark cloaks, but glow with pale light, and only blackness can be seen under their hoods. The glow also covers part of Sirius. Sirius's face shows no emotion.<br/>
GRANGER: We had hoped he could take care of you.<br/>
HARRY: It was not Sirius who would take care of anyone that year. But I did meet him.<br/>
We enter a narrative frame in which Harry describes past events. In the narrative frame, Harry is being escorted by the same junior Auror; they are on the driveway leading up to the door of a house. There are two windows alongside the door, but they are dark; there is nothing to indicate that the house is inhabited.<br/>
PRESENT HARRY: One of your people took me to the house where he was being kept.<br/>
Harry is silhouetted in the door for a moment as ze enters the house. Then ze's inside, looking uncertainly into the darkness.""",
  "annotation":"""<p>The Auror escort is because the location of that house is secret; only a few people are allowed to visit without Sirius explicitly asking for them. This isn't standard practice, but lots of people on both sides might still be interested in getting revenge on Sirius, based on what they believe ze did or didn't do.</p>

<p>The Aurors weren't literally "your [Granger's] people" at the time, but the phrase still works. It's also possible that Harry is using "your people" to mean people in authority in general, as Granger has been on that track almost since the day ze arrived in the magical world.</p>
""",
},
{
  "force_id":"5e77416cb19a1d9afae4661204e2b20e",
  "force_date":datetime.date(2012, 5, 29),

  "transcript":"""Inside the house, Harry approaches Sirius. Sirius is lying in a bed, staring into space.<br/>
Harry walks up next to Sirius and looks at zem. Ze doesn't look back. Harry squints at Sirius, then waves zir hand in front of Sirius's face. Sirius just keeps staring.<br/>
PAST HARRY: Sirius Black!<br/>
Sirius looks up, surprised.<br/>
SIRIUS: L-Lily...?""",
  "annotation":"""<p>The Dementors no longer guard Azkaban, but they did for the entire thirteen years Sirius was imprisoned there.</p>""",
},
{
        
  "content_warning":""""negative self-talk""",
  "force_id":"20109e61adc31d9d75190f8e268e7679",
  "force_date":datetime.date(2012, 5, 29),

  "transcript":"""PAST HARRY: I'm not Lily!<br/>
SIRIUS: She always used to do that... walk in on me, say my name...<br/>
Sirius continues talking over Harry. Zir voice has become less neat, more ragged-looking.<br/>
SIRIUS { imitating what Lily might say }: Sirius Black! When will you show some respect! You're disgusting... pathetic... Sirius Black! You've failed us... So you thought you were clever enough to fool Lord Voldemort all by yourself... We had all of Dumbledore's protection, and you ruined it, Sirius Bla&ndash;<br/>
PAST HARRY: Lily never said that! You're off your gourd! { "off your gourd" is slang for "insane" }<br/>
Sirius leans over in the bed and reaches towards Harry.<br/>
SIRIUS: W-who are you? Are you J&ndash;<br/>
HARRY: I'm Harry, their&ndash;<br/>
SIRIUS: You look like Lily... But you have James's eyes...<br/>
Sirius touches Harry's face. Harry looks surprised for a moment. Then Harry pulls away in disgust. The next thing we see is Harry standing outside the house with the Auror who brought zem.""",
  "annotation":"""<p>How would this feel different if I had put the "Sirius Black! When will you..." line inside a narrative frame, with an imaginary abusive version of Lily saying it, instead of Sirius saying it directly?</p>""",
},
{
  "force_id":"65d5315f0bf38989d4364da6f109fbd8",
  "force_date":datetime.date(2012, 5, 31),

  "transcript":"""PRESENT HARRY: Sirius could not help me... But I had this note someone at Hogwarts had slipped to me.<br/>
Close-up of past Harry clutching a scrap of parchment in zir hand. The parchment says "Midnight. Astronomy tower." Harry is looking upwards at the Astronomy Tower, a crenellated tower surrounded by stars. Inside the tower, a spiral staircase ascends to an enclosed room on the roof of the tower; this room has a door in the side, which is the way the roof is accessed.<br/>
Past Harry climbs the stairs and opens the door. Through the door, we can see another person standing between two crenellations. That person is silhouetted against the starry night sky.""",
  "annotation":"""<p>The next few pages will have no annotations...</p>""",
},
{
        
  "content_warning":""""violence""",
  "force_id":"3248fbdfa470a7daa91dc4166d1e65dd",
  "force_date":datetime.date(2012, 6, 1),

  "transcript":"""The silhouetted figure turns, revealing itself to be Draco Malfoy. Draco has the same dark marks under zir eyes that Harry usually does; otherwise, zir expression is ambiguous. Draco approaches Harry with arms raised. Harry pulls a wand and blasts Draco with a spell; Draco is slammed backwards against one of the crenellations. Draco collapses at Harry's feet and begins to say something.<br/>
We see no words of what Draco says; a narrative frame opens instead. In the frame, Draco and Goyle are standing together, and behind them, someone is pointing a wand towards them.<br/>
PERSON WITH WAND: I've heard something <em>very</em> interesting, Malfoy...""",
  "annotation":"""<p>...</p>""",
},
{
        
  "content_warning":""""child abuse, blood""",
  "force_id":"48283fb23344f00ae2112378ebd47516",
  "force_date":datetime.date(2012, 6, 2),

  "transcript":"""In Draco's narration, the person pointing the wand turns out to be Blaise Zabini. Zabini is still holding the wand. Draco and Zabini look at each other angrily.<br/>
ZABINI: They say that you've been avoiding the Potter brat... that you're <em>scared</em>...<br/>
Zabini starts to cast a curse at Draco. Instead of helping Draco, Goyle grabs Draco's arms so ze can't defend zemself.<br/><br/>
The narrative frame closes. On the Astronomy Tower, Harry interrupts Draco's narration with zir own. We see a bunch of scenes from Draco's life, at least as Harry imagines it: Draco's parents, Lucius and Narcissa Malfoy, holding a baby Draco and smiling down at zem; Lucius tucking Draco into bed, both of them smiling; Lucius buying an eager Draco a Nimbus 2000 broomstick; Draco playing Quidditch, breezing past the Gryffindor seeker (who is Granger, although it's probably drawn too small to tell, and has a broom that is <em>not</em> a Nimbus 2000) to grab the Snitch; Lucius introducing Draco to Crabbe and Goyle, who bow deferentially.<br/><br/>
On the Astronomy Tower, Harry stands over Draco and kicks Draco in the face; blood sprays. Harry is still pointing zir wand down at Draco.<br/><br/>
Meanwhile, Harry continues narrating, now telling about zir own life: the baby Harry amid the wreckage of zir cradle, with fragments of Lily's body lying around, as well as the dead James and bits of Voldemort's snake; Vernon shoving a resistant Harry into the cupboard under the stairs; Harry lying on the hard floor of the cupboard under the stairs, sleeping or trying to sleep, with zir hands over zir face.""",
  "annotation":"""<p>...</p>""",
},
{
        
  "content_warning":""""violence, blood""",
  "force_id":"3c98841300d774219796f2385600e85f",
  "force_date":datetime.date(2012, 6, 3),

  "transcript":"""Harry narrates through images: a much younger Harry reaches into a refrigirator, glancing over zir shoulder at Aunt Petunia, who is facing the other direction, but looking suspiciously back in Harry's general direction.<br/>
Harry narrates through images: Draco, as a smiling child, sits at a table, with food in front of zem. Lucius sits nearby, smiling at Draco.<br/>
Harry narrates through images: Draco, as a child, frowns and shows Lucius that Draco's hand has a cut/scrape on it. Lucius uses magic to heal the cut. Draco smiles.<br/>
On the Astronomy Tower, we see a single large image of Harry and Draco, from a low angle, against a wide, star-filled sky. Harry has lifted Draco and pinned zem against one of the crenellations. Draco is bleeding from the mouth. Harry's face is pressed very close to Draco's; Harry is looking in Draco's eyes, using Legilimency. A narrative frame opens to represent the memory of Draco's that Harry is reading.<br/>
In Draco's memory, Draco, as a child, is standing near the top of an elegant spiral stairway. Below is the dinner table we saw earlier. Lucius and Narcissa Malfoy are sitting at the table; Narcissa is leaning forward, angry, looking at someone who is on the other side of the table, unseen. Lucius has zir hand on Narcissa's arm, as if holding zem back. Draco watches this, confused.""",
  "annotation":"""<p>...</p>""",
},
{
        
  "content_warning":""""child abuse""",
  "force_id":"c90a5fc8e1a60879977e9d80f5e9e5fa",
  "force_date":datetime.date(2012, 6, 4),

  "transcript":"""In Draco's memory, Draco walks down the stairs. At the table are Lucius, Narcissa, and Voldemort. Lucius and Narcissa speak in the curvy style characteristic of Slytherin.<br/>
LUCIUS: We mustn't anger him, Narcissa.<br/>
NARCISSA: This is the one request we cannot allow!<br/>
LUCIUS: Would you have us defy our lord? It will be all right in the end. Trust me.<br/>
Voldemort is ignoring them and looking towards Draco on the stairs.<br/>
VOLDEMORT: Ah. Draco. I have longed to meet you.<br/>
LUCIUS: Go with the Dark Lord, Draco. Do as he says... be good...<br/>
Draco and Voldemort walk back up the stairs, to a corridor with several doors. One of the doors goes to Draco's room; it is labeled "Draco" in gold lettering in the Slytherin style.<br/>
Draco and Voldemort enter Draco's room. The room contains a desk, the bed we've seen in Harry's narration, and two windows. The windows have curtains; there is bright sunlight outside, but Voldemort is casting a spell to close the curtains.""",
  "annotation":"""<p>...</p>""",
},
{
        
  "content_warning":""""child abuse""",
  "force_id":"8504bd76317cb7bc2216706f2cbc500b",
  "force_date":datetime.date(2012, 6, 4),

  "transcript":"""The curtains are closed. Voldemort sits on Draco's bed.<br/>
VOLDEMORT: Come sit, Draco.<br/>
Draco doesn't.<br/>
VOLDEMORT: You won't sit for me? You would not want to anger me. <em>Accio child</em>. { "Accio" is the incantation for the Summoning Charm, which causes the named object to fly to the caster's location. }<br/>
Voldemort's spell pulls Draco to the bed; Voldemort puts zir arm - specifically, the translucent silver arm - around Draco. Draco doesn't seem to like this.<br/>
VOLDEMORT: Talk to me, Draco. Why do other people have things I can't have?<br/>
There is an uncomfortable silence. Voldemort pulls Draco closer in an intimidating way.<br/>
VOLDEMORT: So silent. Perhaps you think Lord Voldemort will endure your stubbornness and forgive?""",
  "annotation":"""<p>...</p>""",
},
{
        
  "content_warning":""""child abuse""",
  "force_id":"948e70310489760dfb43430cf5ea05fa",
  "force_date":datetime.date(2012, 6, 6),

  "transcript":"""VOLDEMORT: I think not. Silencio. { The incantation of the Sliencing Charm. }<br/>
Draco is silenced.<br/>
Half the page is dominated by an image of Voldemort, still sitting on the bed, holding up Draco by Draco's hair using zir silver hand, and pointing zir wand at Draco's chest with the other.<br/>
VOLDEMORT: Crucio. { The incantation of the torture curse. }<br/>
Voldemort shows no special feeling as ze does this; as ever, ze is completely impassive. Draco's face twists in pain (but makes no sound because of the Silencing Charm), and the color of the torture curse floods the other half of the page.<br/>
VOLDEMORT: Ha. Ha.<br/>
At the bottom is a tiny image of Draco lying curled up on the floor with zir hands over zir head. The rest of the room is barely visible in the darkness.""",
  "annotation":"""<p>...</p>""",
},
{
        
  "content_warning":""""child abuse, blood""",
  "force_id":"e92320a3c87aa53eb4df89694bec3d82",
  "force_date":datetime.date(2012, 6, 7),

  "transcript":"""We see a bunch of Draco's memories, in no clear order. In all of these, Lucius looks concerned instead of happy.<br/>
<br/>
Draco curls up with zir blankets on the floor next to zir bed. Lucius Malfoy is on the other side of the bed, beckoning Draco, but Draco is looking away angrily.<br/>
<br/>
Draco and Lucius sit at the dinner table from <a href="http://www.elidupree.com/main/posts/256-voldemort's-children-page-67">[TW: violence, blood] page 67</a>; Draco pushes zir plate away.<br/>
<br/>
Lucius and Narcissa lie in bed together. Narcissa is facing away from Lucius.<br/>
NARCISSA: What have we done to him?<br/>
LUCIUS: He'll pull through... please believe me...<br/>
<br/>
Draco waking up in bed, zir face twisted with terror. All the lines of the drawing glow like the curse on the previous page. This looks very similar to Harry waking up on <a href="http://www.elidupree.com/main/posts/175-voldemort's-children-page-16">page 16</a>.<br/>
<br/>
Lucius buys the Nimbus 2000 for Draco, like on <a href="http://www.elidupree.com/main/posts/255-voldemort's-children-page-66">[TW: child abuse, blood] page 66</a>. Draco takes it, but is annoyed or impatient rather than happy about it.<br/>
<br/>
Draco flies above a row of other students, using one of the school broomsticks. Draco is smirking and holding up a red sphere; it's Neville's Remembrall, as in the first book of the <i>Harry Potter</i> series. The other students' brooms are lying on the ground; Granger and Harry are looking up at Draco with irritation, but neither has moved to challenge Draco.<br/>
<br/>
Draco points a finger, commanding Crabbe and Goyle. Crabbe and Goyle drag Harry, in a position very similar to the other children dragging Harry on <a href="http://www.elidupree.com/main/posts/194-voldemort's-children-page-31">[TW: child abuse, blood] page 31</a>. Draco has zir face concealed like Voldemort.<br/>
DRACO: Ha. Ha.<br/>
<br/>
The narrative frame closes; we're back on the Astronomy Tower. Harry stops using Legilimency on Draco and looks at Draco in shock. Draco's cheeks turn red, and ze turns away from Harry and looks down. Draco is still bleeding from the mouth.""",
  "annotation":"""<p>...</p>""",
},
{
  "force_id":"29e554745f96871c27889385551e31fc",
  "force_date":datetime.date(2012, 6, 8),

  "transcript":"""PRESENT HARRY: And slowly the pieces begain to fall into place... What Dumbledore had meant when he said "The Dark Lord tore families apart"...<br/>
DRACO: I was five... we kept hearing the stories about the Dark Lord being killed, his Time-Twister destroyed... But for us, he was all too alive...<br/>
PRESENT HARRY: I had thought of Malfoy so long as an enemy, but now suddenly he was just a child like me... Alone and friendless... Abandoned by his followers... Suddenly he was someone I felt <em>I</em> had to protect. And I began to think in new ways.<br/>
Harry and Draco sit on opposite side of the page, facing away from each other. The drawing is very simple and stark; the background is black, without the vista of stars that recent pages have had. Past Harry's speech is now pale red. (Present Harry's speech is bright red, and past Harry's speech has been, until this point, grey.)<br/>
PAST HARRY: I'm sorry for kicking you.<br/>
DRACO: I'm sorry for... you know... everything...<br/>
PAST HARRY: Sometimes when I sleep, I am there again... in that cupboard...<br/>
DRACO: On that bed...<br/>
PAST HARRY: He has his hand in everything that happens to us...<br/>
DRACO: In everything we do...<br/>
PAST HARRY: We are truly Voldemort's children.""",
  "annotation":"""<p>Thus ends Chapter Five, "In The Houses Of His Fathers".</p>

<p>I didn't write annotations on the last few pages because I thought too many words would spoil their emotional impact. (It's the same reason I didn't use many words on the pages themselves.) The annotations are back now (although I might do the same thing occasionally in the future).</p>

<p>If I had more time to dwell on the details, I would have shown Draco's reluctance to talk. In Draco's world, the most important thing is to be strong; if you show weakness, you're supposed to be punished for it rather than to receive sympathy. So it would be a very awkward scene where Harry tries to communicate to Draco that ze feels sympathetic, while Draco tries to appear strong to compensate for the fact that Harry has just seen zir weakness (since ze assumes Harry will think less of zem for it).</p>

<p>Harry probably wouldn't feel the same way if Draco had just <em>told</em> zem about what we've just seen, but there's a certain unavoidability about directly experiencing another person's memories.</p>""",
},
{
  "force_id":"9a05454b878c9a6c4b7e2fb8df34caf3",
  "force_date":datetime.date(2012, 6, 9),

  "transcript":"""PRESENT HARRY: And now that you know how I met my allies, I can tell you about...<br/>
<br/>
Chapter title image: Hogwarts towers loom dimly in the background. An extremely bright blaze of fire enters the page from the left side and stops in the middle. In the head of the blaze are the slihouettes of Harry, Luna, and Draco, with their wands out. Draco crouches at the front; Luna, with zir wand raised above zir head, is in the middle; Harry is in the back, and Harry's forehead scar shows through the silhouette.<br/>
<br/>
At the bottom of the page is the title:<br/>
CHAPTER SIX<br/>
The Purge of Hogwarts""",
  "annotation":"""<p>How much has Harry really told us about how zir group came together? Only time will tell.</p>

<p>I've been having an annoying physical health issue for most of this week. I've kept up until now, but I've run out of my page buffer again, and since the next chapter isn't fully planned yet, I'm going to leave off writing more pages until I've recovered. I wouldn't want to make a lower-quality product with this thing disrupting my ability to concentrate and remember things.</p>""",
},
{
  "force_id":"c4089e26d6e8b8c282816e61ffb7a30a",
  "force_date":datetime.date(2012, 6, 14),

  "transcript":"""A tent, amid some trees. Past Harry, Draco, and Luna are inside. Luna and Harry are now wearing red robes like the ones Lily was wearing when Voldemort attacked, and this version of Harry speaks in the pure red of present Harry. Draco is still wearing grey student robes, but zir collar is now red instead of green. Draco's face has two new scars on it that we haven't seen before; one is at the left corner of zir mouth where Harry kicked zem (the same place as Harry's mouth scar, but a different shape), and the other is next to zir right eye.<br/>
PAST HARRY: &ndash;and after we kill <em>them</em>, we can break into the kitchens and let the elves escape with us.<br/>
LUNA: We can't free the slaves, Harry...<br/>
PAST HARRY: Of course we can, th&ndash;<br/>
DRACO: They won't come.<br/>
LUNA: No, Draco, let me be the one to tell him about the elves!<br/>
A narrative frame opens in which Luna describes the founding of Hogwarts.<br/>
LUNA: The history books make a big deal about the conflict over admitting muggle-borns...<br/>
The four founders (Godric Gryffindor, Rowena Ravenclaw, Salazar Slytherin, and Helga Hufflepuff) stand at the corners of a metaphorical four-sided shape. Gryffindor is bearded, wears pants and boots, and has a sword. Ravenclaw has long purple hair and a smooth appearance, with zir hair and robes trailing as if they're in the wind, but in opposite directions. Slytherin has zir arms folded, wears dark robes, and has grey hair and a thin grey beard. Hufflepuff is short and plump, and wears earthy colors. Where they're standing, Gryffindor and Hufflepuff are close to each other, as are Ravenclaw and Slytherin, but the pairs (Gryffindor-Hufflepuff and Ravenclaw-Slytherin) are farther apart from each other.<br/>
SLYTHERIN: Muggles are an inferior race!<br/>
GRYFFINDOR: Yeah, but Muggle-borns are still wizards!<br/>
RAVENCLAW: They simply are not equipped to study here.<br/>
HUFFLEPUFF: What? They'll work as hard as anyone else.<br/>
LUNA: But they { the history books } only make a footnote of Helga Hufflepuff's belief that students, not enslaved elves, should do the daily work of the castle.<br/>
The four founders are now arranged with Hufflepuff far away from the others, who are all close together. The other three are facing away from Hufflepuff.<br/>
HUFFLEPUFF: It will teach them humility and citizenship.<br/>
GRYFFINDOR, RAVENCLAW, AND SLYTHERIN: There's no excuse to waste the time of witches and wizards!<br/>
Luna's narrative frame closes; we are back in the tent.<br/>
LUNA: Today, the house-elves do not serve the Hufflepuff dormitory. The laundry is done by students... the beds are made by s&ndash;<br/>
PAST HARRY: Then Hufflepuff is the only house worth being Sorted into!<br/>
A pause.<br/>
DRACO: Um... Are either of you&ndash;<br/>
Harry and Luna look down. { Harry is in Gryffindor, Luna is in Ravenclaw, and Draco is in Slytherin. }""",
  "annotation":"""<p>Harry is essentially saying that if a group passively supports a horrific institution like slavery, then you should completely reject that group, regardless of any other virtues it may have. Do you agree?</p>

<p>The Hufflepuff students, by the way, still do eat elf-cooked food in the Great Hall with the others.</p>

<p>The tent where Harry, Draco, and Luna are meeting is in a hidden location, much like in the seventh book when the trio are on the run from Voldemort. This is also the same location where they listen to the radio all the way back on <a href="/main/posts/163-voldemort's-children-page-4">page 4</a>; maybe I'll retcon a tent onto that page eventually, to make it more clear.</p>

<p>On a more technical note... Until (and including) this page, I've hand-lettered all the dialogue in <i>Voldemort's Children</i>. That's been okay so far, even in chapter four (I was taking 1-2 hours for each page just drawing Granger's dialogue, but that was reasonable because Granger was talking a lot). The trouble is, Luna's speech takes a <em>long time</em> to draw &ndash; I spent an entire two hours just drawing zir dialogue on this page, out of six hours total to draw the page. That's not really worth it. So I've created a TrueType font for Luna, and I'm going to start using that on tomorrow's page. It won't look quite as nice, because it won't have all the friendly irregularities of the hand-drawn dialogue, but it's still generally the same.</p>

<p>If I decide I like the choice, I'll probably do the same thing for Granger next time ze talks a lot, because Granger is very verbose and zir speech is already pretty standardized.</p>""",
},
{
  "force_id":"aa8e13637c8305b38c0e37068d7eb9f2",
  "force_date":datetime.date(2012, 6, 15),

  "transcript":"""LUNA: But for the other three founders, the only question was how to minimize the risk of a rebellion that could affect their students... which led them to demand that their elves be raised carefully from birth to believe that the only meaning of their lives was to serve wizards... Their agents used a combination of punishment and mind altering magic&ndash;<br/>
An image illustrates four house-elves &ndash; short beings with tiny limbs, large heads, and pointy ears &ndash; moving in perfect synchrony. A bored wizard is holding a wand with rays that touch the elves' heads. Godric Gryffindor watches this, and is pleased.<br/>
Harry interrupts Luna.<br/>
PAST HARRY: So people are okay with this, we should kill them all, every last person who knows and does nothing&ndash;<br/>
LUNA: No, Harry! Remember what we planned! We're only&ndash;<br/>
PAST HARRY: only killing the worst of the worst, I know... the ones who... who...<br/>
Harry's face becomes pained.<br/>
DRACO: After all this time, you still can't say it out loud.<br/>
PAST HARRY: It doesn't matter if I can&ndash;<br/>
DRACO: Excuse me if I want to know you're not just so fucked in the head that you're going to lead us on some kind of suicidal revenge spr&ndash;<br/>
Harry gets angry leans towards Draco aggressively. Draco looks back calmly.<br/>
DRACO: &ndash;Please don't hurt me.<br/>
Luna grabs Harry's arm. Luna is still smiling calmly; it seems ze always is, no matter how tense the situation is or how dark the topic of conversation is.<br/>
LUNA: You can hurt me instead, I'm okay with it! I don't feel pain, remember?<br/>
PAST HARRY: You're both barking.<br/>
Harry turns away from the other two.<br/>
PAST HARRY: ...I'll tell you a story. Then you can decide if you think I'm crazy for revenge.""",
  "annotation":"""<p>The house-elves will not appear again. I just wanted to remind you that the entire society of the <i>Harry Potter</i> universe is based on slavery.</p>

<p>In the bubble at the top, I knew I wanted the elves' training to be overseen by one of the three founders (other than Hufflepuff), but it took me a while to decide who it should be. I sketched in Slytherin at first, but ze seemed too obvious &ndash; and I'd expect the actual Salazar Slytherin to be more of a "hands-off" person who wants to profit from this dirty business but not actually be involved in it. Between Ravenclaw and Gryffindor, I settled on Gryffindor for two reasons:</p>

<ol><li>I wanted to play up the "Gryffindor may seem like a good guy, but ze's not" statement from the previous page.</li><li>With the sword and the boots, I'm going for a fighter/conquerer image, and that fits perfectly with the subjugation of another race.</li></ol>

<p>That said, there was also a point in Ravenclaw's favor: It would enhance the "They thought about the elves' lives purely as a logistical problem" angle.<p>

<p>As a side note, I've recently learned that in J.K. Rowling's vision, Helga Hufflepuff <em>brought</em> the elves to Hogwarts. In that version, ze did it because no one would be cruel to them in the Hogwarts kitchens, which was the best ze could achieve in an era of history when nobody would accept actually freeing them. I think there's some merit to that version of the story, but it fits much too easily into the books' narrative of Harry's and Hermione's interactions with the elves (especially Kreacher), where the moral of the story seems to be "It's okay to have slaves, but you should treat your slaves nicely".</p>""",
},
{
        
  "content_warning":""""car crash""",
  "force_id":"96f8763636741b9478f71120108ad614",
  "force_date":datetime.date(2012, 6, 16),

  "transcript":"""PAST HARRY: I got revenge once...<br/>
We enter a narrative frame in which Past Harry describes further-in-the-past events. In the frame, the Dursleys and Harry are exiting a hospital on a bright sunny day; Harry has bandages on zir face where the mouth scar is, and Dudley is snickering behind Harry's back.<br/>
PAST HARRY: The doctors had just fixed me up. But I was scarred. And Dudley was still...<br/>
We see close-up images of Harry's eyes as Harry's face twists with anger. Harry's eyes glow. Lightning flashes, stormclouds move in, and a heavy rain begins. As Vernon and Dudley are crossing at a sidewalk, a car slips on the wet road and hits Dudley. Harry grins as Vernon and Petunia rush to where Dudley lies on the ground. The driver of the car has also stopped and gotten out, and is shocked. The next thing we see is Vernon, Petunia, and Dudley exiting the hospital again, with Dudley in a wheelchair.""",
  "annotation":"""<p>Now you know why Dudley was in a wheelchair on <a href="/main/posts/175-voldemort's-children-page-16">page 16</a>. (And for reference, Harry is recovering from the injury we saw on <a href="/main/posts/194-voldemort's-children-page-31">[TW: child abuse, blood] page 31</a>.)</p>

<p>During this flashback, Harry still believes the Dursleys' lie that zir parents died in a car crash. I wonder what <em>that</em> implies...</p>

<p>By the way, I consider the Luna font a success, and I'm making Slytherin, Gryffindor, and Granger fonts now. (For the moment, that'll only affect Draco, but a bunch of other minor characters speak in the Gryffindor and Slytherin fonts.)</p>""",
},
{
  "force_id":"7d78bee4d30999aec74731895f5e2ee0",
  "force_date":datetime.date(2012, 6, 17),

  "transcript":"""PAST HARRY: I didn't know about underage magic then, so I thought it as just an accident. But I did know that Dudley was suffering, and that made me happy... Until...<br/>
Dudley, in zir wheelchair, approahces Harry.<br/>
DUDLEY: Harry? I realized something...<br/>
Harry stands outside the cupboard under the stairs, with zir arms crossed.<br/>
DUDLEY: Mum and dad... they talk about me now like I'm not even in the room... like I'm just a piece of charity they're doing... that's the way they've been talking about you all these years, isn't it...? Harry? I've been a bad cousin...<br/>
PAST HARRY: I'd had my revenge, but I only felt sick inside. I don't like hurting people, Malfoy. But you know why we have to do this. I need to see your list of the people who &ndash; who we have to kill. You're the only one of us who knows who they all are, and... I trust you.<br/>
The narrative frame closes; we are back in the tent. Draco looks defeated. Ze goes in a corner and writes a list on a scrap of parchment, then hands it to Harry. While handing it, Harry faces away and Draco has zir eyes closed and head bent, very reminiscent of Lily handing James the spell on <a href="/main/posts/209-voldemort's-children-page-43">page 43</a>.<br/>
Harry looks at the list.<br/>
PAST HARRY: You wrote Crabbe and not Goyle...<br/>
DRACO: Hah... Goyle is too stupid to learn the spells.<br/>
In the background, we see an angular view of the list of names from Fudge's speech on <a href="/main/posts/164-voldemort's-children-page-5">page 5</a>, except that Draco's name isn't in the list.<br/>
PAST HARRY: So many names...
""",
  "annotation":"""<p>The Dursleys blamed Harry for the 'accident' anyway, of course. They locked zem in the cupboard without food until two days later when Dumbledore visited to intimidate them. Dumbledore draws the line at things that could endanger Harry's life.</p>

<p>This page also gives an (equally cryptic) answer to my cryptic clue from the annotation of <a href="/main/posts/164-voldemort's-children-page-5">page 5</a>; in the books, being nasty helps you cast nasty spells, but in <i>Voldemort's Children</i>, all spells require skill and intelligence. I decided that Crabbe is somewhat smarter than Goyle because ze's the one who casts the Fiendfyre spell in the books (and they explicitly say that that spell is very difficult).</p>""",
},
{
  "force_id":"6f694ad984a8190c1649645132bfdd45",
  "force_date":datetime.date(2012, 6, 18),

  "transcript":"""PRESENT HARRY: Malfoy was still reluctant at first...<br/>
An image of Draco looking pained.<br/>
DRACO: They were my friends... I'm not sure I can do this...<br/>
PRESENT HARRY: But he was still living with them at Hogwarts... And in the coming weeks, as the idea sank in...<br/>
An image of Draco in a rage.<br/>
DRACO: I hate the way they talk, I hate the way they move, I want to <strong>kill them all</strong> with my <strong>bare hands</strong>&ndash;<br/>
PRESENT HARRY: And finally...<br/>
An image of Draco looking resolute.<br/>
DRACO: I'm ready.<br/>
In the tent, Harry, Draco, and Luna sit around a map of Hogwarts.<br/>
DRACO: This is the plan: I invite them each, in secret, to a dungeon room with only one exit. They will come; I can ensure this. No one else will know until morning... No one else will have to die...<br/>
LUNA: What about Dumbledore? He knows everything that happens in the castle. And he never sleeps!<br/>
PAST HARRY: I know his mind. I will send him an owl, in my own name. He will meet me in his office, assuming I am seeking redemption... He will not contact the Ministry, or suspect that it is a distraction, a trap, until it is too late.<br/>
LUNA: Isn't that a bit unreliabl&ndash;<br/>
PAST HARRY: It is what I will do.""",
  "annotation":"""<p>Harry and Luna have left Hogwarts to go on their mission; Draco is helping them while living a double life as an innocent student.</p>""",
},
{
  "force_id":"a36853749e4c1b618a2cd574fd419121",
  "force_date":datetime.date(2012, 6, 19),

  "transcript":"""PRESENT HARRY: With our plans in order, we waited... and finally the night we'd chosen arrived...<br/>
Past Harry, Draco, and Luna stand in the moonlight. The gibbous moon is glowing brightly behind the word "order" of present Harry's line. Luna casts zir zigzag transportation spell, and a bright zigzag fills the page.<br/>
PRESENT HARRY: Luna took me to the door of Dumbledore's office, and there we parted ways... They to the room where the slaughter would take place... and I to keep an oath I had once sworn to myself...<br/>
The edge of the narrative frame we're in starts to split the right side of the page from the left side. On the right side of the page, Harry arrives in front of Dumbledore's door. On the left side of the page, Draco and Luna arrive in front of a grey door. In between, there's a sliver of a view of present Harry in the interrogation cell.""",
  "annotation":"""<p>The Slytherin font is finished &ndash; just in time for this page, which, ironically, is the only remaining page of this chapter that won't use it.</p>""",
},
{
        
  "content_warning":""""magical massacre""",
  "force_id":"4a81763cd26c109838b06c66a651a9b",
  "force_date":datetime.date(2012, 6, 20),

  "transcript":"""The page is still a split frame.<br/>
<br/>
On the left side:<br/>
The seven students to be killed are standing around in a large dungeon room, talking amongst each other, when Draco and Luna peek in the door with wands out. Some of the students notice them, others don't. The room has a tiled stone floor and dark walls with hexagonal pillars built into them.<br/>
Draco and Luna step into the room.
DRACO AND LUNA: Avada kedavra!<br/>
Pansy Parkinson and Graham Montague die before they can react.<br/>
Draco and Luna continue advancing and casting Killing Curses. Crabbe tries to pull out zir wand, but is too slow. Daphne Greengrass casts a shield spell, but Luna's curse blasts right through the shield.<br/>
<br/>
On the right side of the page:<br/>
Harry steps into Dumbledore's office, with zir wand clenched in zir fist.<br/>
PRESENT HARRY: It had been four years since the day I promised myself to kill him...<br/>
Dumbledore starts to step from behind zir desk.<br/>
DUMBLEDORE: Ah, Harry, I confess th&ndash;<br/>
PAST HARRY: Stupefy!<br/>
PRESENT HARRY: I had been so young, I felt... And yet...<br/>
Dumbledore is blasted backwards by the spell, and for the first time, we see zir whole face, which is heavily lined and surrounded by a thick mane of white or grey hair. Dumbledore collapses on the floor in front of zir desk and Harry, now drawn as a silhouette, stands over zem. Harry is pointing zir wand down at Dumbledore.<br/>
PRESENT HARRY: I would not break the trust of myself...<br/>
DUMBLEDORE: Harry...""",
  "annotation":"""<p>The Stunning Spell is supposed to knock the target unconscious. It didn't work completely, not because Dumbledore has any special immunity the way Luna does, but because Harry isn't very good at magic.</p>

<p>In the room on the top left, from left to right, those are Zabini, Crabbe, Millicent Bulstrode, Charles Warrington, Daphne Greengrass, Pansy Parkinson, and Graham Montague. We've seen Daphne Greengrass and Graham Montague before - they were the two students bullying Harry in McGonagall's class on <a href="http://www.elidupree.com/main/posts/167-voldemort's-children-page-8">page 8</a>. And of course we've seen Zabini and Crabbe before.</p>""",
},
{
        
  "content_warning":""""verbal abuse""",
  "force_id":"86c837b17dc1061ed15e82bb78dbb627",
  "force_date":datetime.date(2012, 6, 21),

  "transcript":"""The page is still a split frame.<br/>
<br/>
On the left side:<br/>
Luna and Draco kill Millicent Bulstrode and Charles Warrington, leaving only Blaise Zabini alive. Zabini raises zir wand.<br/>
ZABINI: Fiendfyre! { Spoken as a spell incantation, in huge, jagged letters. }<br/>
A bright flame with blackness at its core appears at the tip of Zabini's wand.<br/>
LUNA: Hello, Blaise! Nice fire!<br/>
ZABINI: You like it, freak? I'm the only one here who can control it. So you're not going to kill me... Not unless Malfoy wants you to kill his whole House... we're not far from the dormitories... They'll be asleep... So I've got all the time I want here with you... I suppose Malfoy told you all about us. Well, let me tell you... You lot deserved everything we gave you. Weaklings... Mudbloods... Blood traitors... Freaks...<br/>
DRACO: Zabini, don't you dare! I'll&ndash; I'll&ndash;<br/>
Zabini smiles.<br/>
ZABINI: Is that a threat I hear? From Malfoy the deserter? You screamed like a little Muggle when we came for you...<br/>
Draco is pointing zir wand at Zabini angrily, and crying.<br/>
ZABINI: And... you! I'm not even going to dirty my lips with your name&ndash;<br/>
LUNA: I'm okay with whatever you want to say about me!<br/>
ZABINI: Well, you&ndash; You're&ndash;<br/>
Zabini swings zir wand towards Luna; the fire streaks brightly, and it becomes clear that dark creature-like shapes are forming in it.<br/>
<br/>
On the right side of the page:<br/>
The portraits of former Headmasters and Headmistresses start yelling at Harry.<br/>
PORTRAIT 1: How dare you!<br/>
PORTRAIT 2: Attacking the Headmaster! It's a &ndash;<br/>
PAST HARRY: Shut up!<br/>
DUMBLEDORE: Harry, I'm&ndash;<br/>
PORTRAIT 3: You should be ashamed!<br/>
PORTRAIT 4: No student of mine ever&ndash;<br/>
PAST HARRY: Shut up or I'll burn you all!<br/>
PORTRAIT 3: Ungrateful child!<br/>
PORTRAIT 2: Have you forgotten all the good Dumbledore has done you?<br/>
PAST HARRY: Incendio! Incendio! Incendio! { The incantation for the Fire-Making Spell. }<br/>
The office is engulfed in bright flames. The portraits burn. The devices on the side table fall and go to pieces. Amid the flames, Harry turns zir wand back towards Dumbledore.""",
  "annotation":"""<p><a href="/main/posts/175-voldemort's-children-page-16">I've mentioned Zabini's gender before.</a> By the way, Zabini is <a href="http://en.wikipedia.org/wiki/Gender_binary">binary</a> and <a href="http://en.wikipedia.org/wiki/Cisgender">cis</a>, and all of the other characters recognize zem unambiguously as zir actual gender.</p>""",
},
{
  "force_id":"2723b6050b28d844e9e407800db87c4e",
  "force_date":datetime.date(2012, 6, 22),

  "transcript":"""The page is still a split frame. This time, the split curves from left to right, so the right side is mostly at the top of the page and the left side is mostly at the bottom of the page.<br/>
<br/>
On the right side:<br/>
PRESENT HARRY: And now the moment had come... The moment to bring and end to this all...<br/>
The room is a fiery haze. Harry and Dumbledore are silhouettes.<br/>
DUMBLEDORE: Harry... I'm... sorry...<br/>
HARRY: Avada Ke&ndash; Avada&ndash;<br/>
The first few letters of the incantation glow like casting a spell, but then the glow disappears. Harry looks down at Dumbledore, anguished.<br/>
<br/>
On the left side of the page:<br/>
LUNA: You can't put out that fire you've started, can you.<br/>
ZABINI: Did I say I would?<br/>
Luna pulls Draco back as Zabini throws the Fiendfyre on the ground. It erupts into a giant mass of eyeless, fire-wreathed monsters between Zabini and the others. Zabini grins maniacally.<br/>
ZABINI: Run while you can. I'm not going to give you the satisfaction of seeing me die.""",
  "annotation":"""<p>There's also a metaphorical reason why you will not see Zabini die: Much like with Voldemort, the forces that Zabini <em>represents</em> do not die with zem. (And, like with Voldemort, Zabini really does die; this isn't one of those things where five episodes later it turns out that they had a secret escape route all along.)</p>""",
},
{
  "force_id":"832ebfbb5ed9fb5e047c3811b6f5a582",
  "force_date":datetime.date(2012, 6, 23),

  "transcript":"""The first half of the page is still a split frame.<br/>
<br/>
On the left side:<br/>
Draco and Luna have left the dungeon room; Draco closes the door behind zemself, but the flames are already intruding around the edge of the door.<br/>
LUNA: The door won't stop it for long!<br/>
DRACO: Sonorus! { The incantation for a spell that makes the caster's voice very loud. }<br/>
Draco shouts into the air:
DRACO: <strong>Everybody wake up! There's Fiendfyre in the dungeons! Get moving if you want to live!</strong><br/>
DRACO: Quietus. { The counterspell to Sonorus. }<br/>
Draco and Luna start running.
DRACO: That'll wake Snape. He'll know what to do. Now let's get Harry and <strong>go</strong>!<br/>
<br/>
On the right side of the page:<br/>
Harry drags the unconscious or barely-conscious Dumbledore out of the burning office, and shuts the door behind zem. Dumbledore lies on the ground; zir right hand is burnt and the sleeve is still on fire.<br/>
PRESENT HARRY: For all the people I'd killed... I couldn't bring myself to kill the one who had hurt me the most.<br/>
The two side of the page join again with Luna's zigzag transportation spell. Luna grabs Harry and they land ignominiously back at the tent. Luna and Harry have fallen over and Draco is on zir knees. The moon still shines brightly above.<br/>
LUNA: Oof! Sorry about the landing!<br/>
Draco looks at zir own hands.""",
  "annotation":"""<p>In the books, the Headmaster's office can seal itself against powerful wizards who try to intrude, so it would be strange if ordinary fire could get through the door.</p>

<p>I think the door in the <em>dungeons</em> is an ordinary door made of stone. If the Fiendfyre can burn through the door, does that mean it also burns all the walls? That could cause major structual damage to the castle! I can see a few different ways it could work:</p>
<ul><li>It's like gas pressure and looks for the easiest way to expand &ndash; it'll only burn rock until it breaks through into another open space.</li><li>It can't burn the door, but it can push through the cracks around the door until there's enough on the other side.</li><li>It doesn't have the power to burn very much rock, but it's intelligent or semi-intelligent and likes killing people and/or destroying valuable objects, so it attacks the door on purpose in order to get to them.</li></ul>

<p>Also, what can actually stop Fiendfyre from expanding? In the books, they escape by exiting a magical room that's different every time you enter it; what if you cast Fiendfyre outdoors? Here are a few of the many possibilities:</p>
<ul><li>It would actually burn the whole world, but only a few people have the skill and interest to learn to cast it, and none of those people have ever been stupid/omnicidal enough to try it.</li>
<li>It would burn the whole world, except that a lot of people know how to put it out by magic, and it doesn't become much harder to stop just because it expands wildly.</li>
<li>It doesn't actually gain power from expanding or burning things, and only expands until it runs out of the energy given to it by the person who cast it.</li></ul>

<p>I think my favorite interpretation is that it's intelligent and can only expand by consuming magic, which it can get by burning magical objects or killing magical people. On the other hand, it can keep burning for a long time by just sitting in the same place, so if you seal it in, it's only safe until the seal is broken again.</p>

<p>In this particular situation, how they deal with it afterwards isn't important enough to make it onto a page, but it's easy to explain here. Snape knows about Fiendfyre because ze's studied the "Dark Arts" extensively. Snape is also sensible/cowardly enough (take your pick) that ze doesn't try to go extinguish it zemself, but blocks it, evacuates the students, and alerts the Ministry. At that point, Granger (who knows about Fiendfyre because ze's studied <em>everything</em> extensively) arrives and extinguishes it, possibly with some help from Snape or the other professors. Normally, Dumbledore would be able to do that, but Dumbledore isn't exactly in a position to do so right now.</p>

<p>Also, I decided that there's an old wizarding law that says a person who casts Fiendfyre and lets it run wild must pay a penalty of fifty Galleons to the person who extinguishes it. So, in the present, Granger now knows that Zabini's family owes zem fifty Galleons. Ze hardly plans to collect.</p>""",
},
{
  "force_id":"ff4f8710c888f5e52fe087a994305a9c",
  "force_date":datetime.date(2012, 6, 24),

  "transcript":"""DRACO: Th... they're dead... they're really all dead...<br/>
Draco starts crying. Harry hugs Draco, who continues crying in zir arms.<br/>
DRACO: And I can't go back... they'll know it was me...<br/>
LUNA: Um, probably, they'll think you're dead with the others. But yeah, no going back.<br/>
At some later time, Draco sends a message by owl to Lucius Malfoy, saying "I am alive. Tell no one."<br/>
The narrative frame of present Harry describing the past closes. Percy Weasley pokes zir head in the door.<br/>
PERCY {quietly}: Phew! What a lot of stairs!<br/>
PERCY: Granger, the responses are as you expected.<br/>
GRANGER: Then it appears that, for now, our time here is at an end.
""",
  "annotation":"""<p>Thus ends Chapter Six, "The Purge of Hogwarts."</p>

<p>Those are the actual Granger and Gryffindor fonts at the end; I finished them earlier today. Since I started making the fonts, this is the first page without <em>any</em> hand-drawn letters.</p>

<p>How have the trio been sending owls to people when they're on the run from the law? There's a bunch of possibilities; I like these two the best:</p>
<ul><li>They go in disguise and rent owls from owl-rental places.</li><li>They have sympathizers who know where they are and send them messages by owl sometimes; they use those owls to send messages later.</li></ul>""",
},
{
  "force_id":"5358acfdb19b93763b123ad1e6fbb184",
  "force_date":datetime.date(2012, 6, 25),

  "transcript":"""CHAPTER SEVEN<br/>
<br/>
A metaphorical image: Across the top are Granger, Voldemort, and Dumbledore; Voldemort looks straight ahead, while Granger and Dumbledore face away, towards the side of the page, looking concerned, pointing their fingers as if to illustrate a point in an argument. Dumbledore's right hand is black and shriveled. In the middle of the page is a child, the young Tom Riddle: Ze looks very much like Voldemort except that ze's smiling instead of having a flat expression, zir face is hidden by a baseball cap instead of by darkness, and ze's wearing a colorful shirt and pants instead of a dark robe. To the right of Riddle is a younger version of Dumbledore, who has a less-wrinkled face and brown hair and beard instead of grey, but still wears the purple robes and glasses of zir present self; to the left is a two-story brick building with gables and windows, some of which are lit.<br/>
At the bottom is the chapter title:<br/>
The Riddle of the Past""",
  "annotation":"""<p>This chapter's title is one of the few puns I have allowed myself.</p>

<p>(Since I'm designing <i>Voldemort's Children</i> to be a serious story with a grand sense of drama, I can't use most of the hilarious things that I think of while I'm writing it. This one was acceptable because the double-meaning of the name "Riddle" feeds into my themes, rather than being a distraction.)</p>""",
},
{
  "force_id":"c6d42940e513bbe78b5a1ed97f659f03",
  "force_date":datetime.date(2012, 6, 26),

  "transcript":"""Granger and Tonks are standing at the bottom of the stairs, just outside Harry's cell.<br/>
GRANGER: I may have to move quickly before a certain person becomes too settled in his opinions. Don't be alarmed; I will Disapparate as soon as I escape the range of the cells' Anti-Disapparation Jinx.<br/>
Granger flies up the staircase and Disapparates in midair, then reappears high above Hogwarts Castle. Then ze flies down to the wall of Dumbledore's office, causes the stone blocks to move aside by magic, and steps in. Dumbledore has new furniture, which is dark grey, and zir right hand is blackened. A piece of parchment and the Pensieve sit on Dumbledore's desk. Granger is nonchalantly putting the blocks back in place when Dumbledore speaks.<br/>
DUMBLEDORE: Ah, Hermione. But how...?<br/>
GRANGER: Please call me Granger; I am here on business. The castle defenses have a height limit and this office is not enchanted against intrusion through stone walls by air, but I'm not here to talk about clever magic. I'm here to discuss <em>this</em>.<br/>
Granger points at the parchment on Dumbledore's desk.<br/>
DUMBLEDORE: I was afraid you would say that.
""",
  "annotation":"""<p>Dumbledore had to replace zir furniture after the fire. The Pensieve survived, though. (It's made of stone, and probably enchanted to be harder to break as well.)</p>

<p>Granger could have taken the Floo Network instead of using such a showy method of travel, but many people can access the Floo Network Authority records, and zir enemies would find it very valuable to be able to track zir location.</p>

<p>In the books, there are some sort of unspecified defenses that make it harder to fly towards Hogwarts by broomstick (and possibly by other means), in addition to the Anti-Apparition Charm and Anti-Disapparition Jinx that cover the castle. That might prevent Granger from using zir flight magic to enter the castle airspace. However, unless there's a hard barrier that blocks physical objects, there's nothing to stop Granger from <em>falling</em> to the interior of the shield and then flying the rest of the way as normal.</p>
""",
},
{
  "force_id":"7054c61e1793ca03a54e339eda23aea2",
  "force_date":datetime.date(2012, 6, 27),

  "transcript":"""GRANGER: The Minister and the rest of the Wizengamot have already signed. We are only waiting on your signature.<br/>
DUMBLEDORE: Already? Since this morning?<br/>
GRANGER: They see the urgency of the situation.<br/>
DUMBLEDORE: But with Harry captured, surely&ndash;<br/>
GRANGER: Lovegood is the power behind his faction. I suspect that Potter was a mere figurehead; we cannot verify that he even has the ability to cast the Killing Curse.<br/>
DUMBLEDORE: Even so, to do this...<br/>
GRANGER: It is the only way we can rely upon.<br/>
DUMBLEDORE: Is Azkaban not secure enough? Now that it uses real guards instead of Dementors, I thought...<br/>
GRANGER: Capture is preferable, of course, but Lovegood has made herself difficult to capture.<br/>
DUMBLEDORE: I cannot argue with your logic, but still...<br/>
Dumbledore is holding the parchment. We can now see some of the text on it: "Ministry of Magic" at the top, then "AUTHORIZATION FOR DEADLY FORCE", and somewhere in the body of the (still mostly illegible) text, "Luna Lovegood".<br/>
DUMBLEDORE: I've never signed away a life.<br/>
GRANGER: And what of the dozens you may sign away by denying us the powers we need to end this killing spree? You yourself lived through Voldemort's reign of terror; would you hold one life in balance with everything he did? Would you spare even Tom Riddle, knowing what he would go on to do?<br/>
DUMBLEDORE: Ah, Tom Riddle... A matter that touches close to my heart... I was the first one to tell him he was a wizard, you know.<br/>
We enter a narrative frame in which Dumbledore describes past events. In the frame, a younger Dumbledore is standing at the intersection of two Muggle roads, holding a map. The map has labels for "Main St" and "Church St", and a mark suggesting a destination.<br/>
PRESENT DUMBLEDORE: I found him in a Muggle orphanage...""",
  "annotation":"""<p>The Minister and the Wizengamot members agreed fairly easily to having Luna killed. The authorities in the patriarchal world of real-life Britain probably wouldn't agree so easily to killing a young, white, female person like Luna Lovegood, regardless of the circumstances. But in the relatively gender-egalitarian world of <i>Voldemort's Children</i>, they don't think about it any differently than if ze was a male serial killer.</p>

<p>Also, I'm sure glad I have a font for Granger now! (I still have to draw Dumbledore's voice, but it's actually quicker to draw than Granger's was, and it would be much harder to make a font for.)</p>""",
},
{
  "force_id":"7af9b6ca5c5c6109f8c4860fd0eec42d",
  "force_date":datetime.date(2012, 6, 28),

  "transcript":"""PRESENT DUMBLEDORE: ...An orphanage called Sunshine Meadows.<br/>
The entire page is a brightly-colored landscape of the orphanage (the same brick building we saw on the chapter title page) with lush meadows in the background and a sunny sky above. Unlike most scenes, this one does not fade into shadow at the edges. The young Dumbledore is looking from the bottom right corner, zir back to the viewer; in the distance, two children are running in the grasses. A road runs from the front of the page to the horizon.)""",
  "annotation":"""<p>...</p>""",
},
{
  "force_id":"c0b1e4fc28e15dd8c2731c362d97b13e",
  "force_date":datetime.date(2012, 6, 29),

  "transcript":"""PRESENT DUMBLEDORE: The matron, Mrs Cole, was very pleasant.<br/>
Past Dumbledore and Mrs Cole are sitting at a table together.<br/>
COLE: Ah, you must be the one from Hogwarts, the school of &ndash; what was it again? You'll want to talk to Tom Riddle, I suppose.<br/>
Past Dumbledore's speech is slightly paler than present Dumbledore's.<br/>
PAST DUMBLEDORE: How is he getting along?<br/>
COLE: The other children positively idolize him. I tell him he should meet more people, but he just seems so happy with the friends he has now, I haven't the heart to push him. Well, good luck finding him&ndash; I'm sure he's somewhere on the grounds, but he can be hard to track down, especially for strangers.<br/>
Dumbledore leaves the building and walks down the road through the sunlit grass. Like on the previous page, the light fills a wide area and doesn't fade into shadow at the edges.<br/>
PRESENT DUMBLEDORE: I did not find Tom first, but another child, crying at the side of the road.<br/>
Dumbledore kneels next to a child who is clearly upset, kneeling next to a little garden plot with dead plants in it.<br/>
PAST DUMBLEDORE: What's the matter, little friend?<br/>
CHILD: My plants! I was at my aunt's and couldn't water them and it was supposed to finally rain, but Tom just kept making it sunny! He <em>always</em> makes it sunny!""",
  "annotation":"""<p>In the books, Dumbledore uses mind-affecting magic to make Mrs Cole stop asking questions about Hogwarts. I didn't want to do that here, because my Dumbledore is someone who's "well-intentioned" and genuinely cares about other people, even though ze does things that are harmful. Ze isn't supposed to disregard the lives of others for zir own convenience. (Isn't that ironic &ndash; I have to make Dumbledore <em>nicer</em> for this story.)</p>

<p>To justify the change, one could argue that it's not the most practical way to hide the existence of magic. I could imagine something like this happening: After Dumbledore leaves, some of Mrs Cole's friends ask zem about Riddle, and ze says that Tom is going to a school called Hogwarts. They try to look up Hogwarts, and it doesn't exist, so they tell Mrs Cole it must be a hoax perpetrated by someone trying to steal children. Mrs Cole gets upset and goes to the local newspaper, who (since wizards can't infiltrate <em>every</em> newspaper in Britain) prints a story about it. By the time the magical world hears about it, there's an entire municipality full of people who will mistrust anything by the name "Hogwarts". That would be inconvenient.</p>

<p>So, instead, I think it works like this: non-magical people are encouraged to know that "Hogwarts" exists and is a very exclusive boarding school, and in circumstances like Tom's, Hogwarts representatives contact the children's guardians years earlier (under various pretenses) so that it isn't a surprise when one of them comes to take the child away to school.</p>""",
},
{
  "force_id":"b87efc7dbdeb494fddee24a144e29d0",
  "force_date":datetime.date(2012, 6, 30),

  "transcript":"""Dumbledore wanders through the grass under the sunny sky. The grasses are as tall as Dumbledore is here. A cloud hovering over Dumbledore looks a bit like a hand.<br/>
PRESENT DUMBLEDORE: As I moved on, I quickly became lost in the tall grasses.<br/>
PAST DUMBLEDORE: Point me. { The incantation of a spell that makes the caster's wand point North. }<br/>
PRESENT DUMBLEDORE: With a little surreptitious magic, I soon found Tom playing some Muggle version of Quidditch.<br/>
Dumbledore pushes through the grass and sees Tom and another child playing basketball on a nearly overgrown half-court.<br/>
PRESENT GRANGER: Basketball.<br/>
PRESENT DUMBLEDORE: Hmm?<br/>
PRESENT GRANGER: He was playing basketball. I <em>am</em> a Muggle-born, you know.<br/>
PRESENT DUMBLEDORE: I took Tom aside. He was very curious, a quality I value in a student.<br/>
Tom's voice is much more rounded than the adult Voldemort's, and it is pink instead of green.<br/>
TOM: Who are you? How did you get here so quickly?
""",
  "annotation":"""<p>Dumbledore romanticizes the non-magical people of Britain, and probably knows more about them than the average magical person, but ze hasn't spent very much time actually living with them, so ze's unfamiliar with many parts of their culture.</p>""",
},
{
  "force_id":"d17079e65e6384ab2e774238890e6b9",
  "force_date":datetime.date(2012, 6, 30),

  "transcript":"""PRESENT DUMBLEDORE: Once we were out of earshot of the others, I told him.<br/>
Past Dumbledore and Tom Riddle are talking in another brightly sunlit field of grass.<br/>
TOM: A wizard?! So there are other people who can do things like I can? If you're a professor, can you teach me more about magic? When can I start? I can't wait to tell everyone!<br/>
PRESENT DUMBLEDORE: I politely insisted that, by our International Statute of Secrecy, he must <em>not</em> tell anyone. Then I took him back to have a conversation with Mrs Cole and myself about the details of boarding-school life.<br/>
Tom, Mrs Cole, and Dumbledore are sitting at the table in the orphanage building. Tom frowns.<br/>
TOM: You mean I'm going to have to leave my friends.<br/>
DUMBLEDORE: And at that moment, the storm began...<br/>
Lightning strikes outside the window and rain pours down; the three inside are lit sharply.""",
  "annotation":"""<p>The first step of an abusive relationship: Take away their support network...</p>

<p>In the books, the International Statute of Wizarding Secrecy presumably has an exception for the immediate families of Muggle-born wizards; the families of Muggle-borns we meet in the books (Hermione, Lily) are routinely aware of the existence of magic. But outside of that, there's nothing, and it's not common practice to tell Muggle-borns about their abilities before the year they enter Hogwarts. (And not from lack of ability to identify them earlier; all magical children are detected at birth.)</p>

<p>I'd be very surprised if there isn't a large achievement gap between Muggle-born and wizard-born students at Hogwarts and its peer institutions; Muggle-borns are, at age 11, shoved into a new world they know nothing about, and to make it worse, they're not allowed to talk about it even with their closest friends.</p>

<p>Thus, even though the Statute doesn't have an explicit blood-purist ideology written into it, it's still designed from such a magical-world-centric point of view that it hurts the very people who are already hurt the most by prejudice and discrimination.</p>

<p>Does this remind you of anything from real life? Please answer in the comments!</p>

<p>(In the books, all the major characters who were raised by Muggles &ndash; Harry, Hermione, Lily, Tom Riddle &ndash; are quite successful at Hogwarts. This is consistent with the books' general pattern of ignoring the more insidious aspects of societal privilege for those who do not have it.)</p>""",
},
{
  "force_id":"d27563cda36c2735dbbc6c861bafc9ce",
  "force_date":datetime.date(2012, 7, 1),

  "transcript":"""The page is, once again, predominantly dark.<br/>
PRESENT DUMBLEDORE: As the other children rushed in from the storm, Tom went to them and hugged them one by one.<br/>
We see this happen: A thunderstorm with visible lightning rolls in from the right, chasing three children. Tom hugs each of them, and starts crying in the middle of doing it. Zir face is still hidden by the baseball cap; we only see tears rolling out from under it.<br/>
PRESENT DUMBLEDORE: A last moment of painful happiness...<br/>
PRESENT DUMBLEDORE: And finally, he turned to me and said, now in the flat, emotionless voice I would come to fear...<br/>
Tom stands alone, with a flat expression, and tear trails still visible on the parts of zir face that we can see. Ze speaks in the adult Voldemort's pale green voice, with its rigid straight lines.<br/>
TOM: I'm ready.<br/>
PRESENT DUMBLEDORE: We took the next train for London; there would be paperwork for the Muggle bureaucracy, but I had asked Minerva to check in with Mrs Cole later to put everything in order.<br/>
We see a train, which is quite unlike the Hogwarts Express; it is blocky and (relatively) modern. An owl is flying to catch up to it, carrying a piece of parchment.<br/>
PRESENT DUMBLEDORE: But as we rode through the countryside, I received an owl from Minerva, indicating that things were not at all in order.""",
  "annotation":"""<p>It's tricky to give Tom facial expressions, or expressiveness in general, when most of zir face is covered. I hope it's clear that ze's crying on this page. (Of course, you also have Dumbledore's narration to give you a sense of what's going on, but Dumbledore is not necessarily a reliable source.)</p>

<p>I was once in a play where the actors wore masks, and the director gave us lots of good tips about how to be expressive without using a face. I think that experience has helped me in writing <i>Voldemort's Children</i>.</p>""",
},
{
  "force_id":"87f7ae1ba33e77ec2bf9593053492d5",
  "force_date":datetime.date(2012, 7, 2),

  "transcript":"""Past Dumbledore and Tom Riddle are sitting side by side on a simple train seat.<br/>
PRESENT DUMBLEDORE: The lightning had sparked a sudden grass fire, which swept through in minutes...<br/>
A short narrative frame coming from the parchment Dumbledore has received shows a bright fire overwhelming the orphanage building and everything around it. The rain and lightning continue in the background.<br/>
PRESENT DUMBLEDORE: The entire orphanage was destroyed...<br/>
The narrative frame of the orphanage burning closes.<br/>
PRESENT DUMBLEDORE: How would I break the news to Tom? How long could I delay telling him the awful truth? But he interrupted my wondering...<br/>
Tom still has a flat expression and is speaking in the Voldemort style.<br/>
TOM: Don't worry about that. I already know.<br/>
Tom reaches up to pull off zir hat.<br/>
TOM: And, Professor, if I'm going to be a wizard, I won't be wearing this anymore... Will I.<br/>
Tom pulls off the hat, and we see zir whole face for the first time. Ze has the same black hair as Harry, as well as the same skin color; zir eyes are green, but a much more bluish green than Harry's. Ze is staring directly forwards with eyes wide, but still has a completely flat expression.<br/>
The hat lies alone on the seat where Tom leaves it.""",
  "annotation":"""<p>If <em>I</em> learned that the adult next to me was planning to hide major information about my life from me like that, I'd be pretty angry about it. The Tom Riddle from the books would be, too...</p>""",
},
{
  "force_id":"86e597b9260faae5650f676b8e3c5a9e",
  "force_date":datetime.date(2012, 7, 4),

  "transcript":"""PRESENT DUMBLEDORE: He was Sorted into Ravenclaw immediately, of course.<br/>
Tom wears the Sorting hat.<br/>
SORTING HAT: Ravenclaw!<br/>
A table of Ravenclaw students cheers.<br/>
PRESENT DUMBLEDORE: Once he settled in at Hogwarts, he seemed happy again, and dived into his studies with a fervor that we rarely see. In his third year, he was issued a Time-Twister to help him take more classes, a decision we now sorely regret...<br/>
PRESENT GRANGER: So that's why Professor McGonagall was so apprehensive when I received mine!<br/>
PRESENT DUMBLEDORE: Indeed.<br/>
PRESENT DUMBLEDORE: Riddle was very popular with children and adults alike, as he had been at the orphanage, but he was aloof. I think perhaps there was no one he was truly close to.<br/>
Professor McGonagall sits at a chair and smiles contentedly as ze writes "Perfect!" on one of Tom's essays. Meanwhile, Tom, who is now wearing the Time-Twister, excitedly reads a book and tries out some magic while pushing away other students who are offering zem a bag of gold and a symbolic heart.<br/>
PRESENT DUMBLEDORE: But we professors overlooked that, mesmerized as we were by his amazing talents. He excelled at every subject he tried &ndash; again, so much like yourself. He especially loved animals, and spent long evenings having Hagrid teach him the languages of cats and snakes.<br/>
Hagrid watches as Tom happily chats with a snake in an unreadable language. Tom is speaking in the voice from earlier, not the Voldemort voice.""",
  "annotation":"""<p>Tom Riddle is born much later in <i>Voldemort's Children</i> than in the books, in order to make my timeline work out. Thus, Hagrid attended Hogwarts already, and graduated as normal before going on to become the Hogwarts gamekeeper.</p>

<p>In book 7, Ron is able to open the Chamber of Secrets just by remembering the hissing sounds Harry made. Thus, it's probably possible to learn that language like any other, even if some people have the ability innately for some reason &ndash; and Hagrid would certainly have every motivation to learn animal languages if ze can. Also, considering that Riddle is a Ravenclaw here, ze probably isn't the Heir of Slytherin, and probably isn't innately a Parselmouth.</p>""",
},
{
  "force_id":"9591e96cfc89390f44ea405e929e184c",
  "force_date":datetime.date(2012, 7, 5),

  "transcript":"""PRESENT DUMBLEDORE: As he rose through the years, he was especially helpful to the younger students. There were a few with whom he spent time often. They began to do very well, and be very focused on their classes... I almost thought of them as Riddle's children within the school. In hindsight, maybe he was already recruiting, but not all of them followed his ideals after he became Lord Voldemort. Lucius Malfoy was one; so was Severus Snape...<br/>
Tom and a young Snape sit in a room with bookshelves, similar to the one from the end of <a href="/main/posts/177-voldemort's-children-page-18">page 18</a>. Tom, grinning, shows Snape how to levitate a rock. Snape is also levitating a rock, but has more trouble.<br/>
PRESENT GRANGER: Hmm. Lucius Malfoy? When I was interrogating Harry, he said that Draco&ndash;<br/>
PRESENT DUMBLEDORE: Yes?<br/>
PRESENT GRANGER: My apologies; I suspect that this is something you would prefer not to know.<br/>
PRESENT DUMBLEDORE: Ah, then I suppose you will not tell me.<br/>
PRESENT DUMBLEDORE: When Riddle started slipping away from us in his sixth year, we were concerned for him. He stopped showing emotion, and he shunned everyone outside his inner circle. Only in hindsight have I come to the realization that he as not putting on a mask &ndash; he was removing one.<br/>
Tom stands with a flat expression, staring blankly into space. Ze is carrying a happy mask and an upset mask, like the Comedy/Tragedy masks, which are the same color as zir skin. In the place of the Time-Twister is the black sphere from <a href="/main/posts/166-voldemort's-children-page-7">page 7</a>; it has three soul fragments in it, and the other four fragments are scattered around the edges of the page.<br/>
PRESENT DUMBLEDORE: I believe that was the year he learned the power to split his soul, and once he was unkillable, he no longer needed our approval to take what he wanted. He no longer had to hide his true self.""",
  "annotation":"""<p>Dumbledore is more perceptive in the bottom half of this page than I wanted zem to be. If I had more time to spend on this story, I would structure it so that you <em>see</em> what Dumbledore is describing, Dumbledore makes different assumptions, and you already have specific information from Harry that would make you realize that Dumbledore's assumptions are incorrect.</p>

<p>The trouble is, if I did it the way I want to, it would be about three times as long. I'd love to make every chapter three times as long, but I have real-life plans (e.g. <a href="/main/posts/205-a-look-at-lasercake-one-of-my-upcoming-projects">Lasercake</a>) that require me to finish <i>Voldemort's Children</i> more quickly than that.</p>""",
},
{
  "force_id":"9d47551d7d5ca9e15bae65c7249e4c83",
  "force_date":datetime.date(2012, 7, 6),

  "transcript":"""PRESENT DUMBLEDORE: And in his seventh year... the petrifications, the death of poor Myrtle... The ominous message on the wall...<br/>
Two grey-faced, immobile students flank a place where a message is written messily in bright, runny paint. It says "The Chamber of Secrets has been opened. Dumbledore, your world will crumble around you."<br/>
PRESENT DUMBLEDORE: Hagrid's roosters had been killed beforehand, so we professors deduced that someone was setting a Basilisk on the school. We quickly devised a solution.<br/>
Past Dumbledore is carrying a rooster and pointing zir wand at it.<br/>
PAST DUMBLEDORE: The rooster's crow is fatal to it... Therefore... Sonorus. { The incantation for a spell that makes someone's voice very loud. }<br/>
ROOSTER {in gigantic, glowing letters}: Cock-a-doodle-doo!<br/>
PRESENT DUMBLEDORE: We searched the castle and found first the expired Basilisk and then the Chamber entrance. Riddle had left it open for us.<br/>
Past Dumbledore and Minerva McGonagall approach the tunnel to the Chamber, next to a sink. They step carefully past the giant Basilisk, which is upside-down and dead. Off to the side, the ghost of Myrtle floats, with zir arms crossed.<br/>
MYRTLE {quietly}: Bah! I <em>die</em>, and still everyone ignores me.<br/>
PRESENT DUMBLEDORE: When we found him inside, he made no move to defend himself. He just stood there and laughed...<br/>
Tom Riddle stands on a low platform under the giant statue of the head of Salazar Slytherin. Dumbledore and McGonagall are pointing their wands at zem. Ze isn't wearing the Time-Twister.<br/>
TOM {in the Voldemort voice}: Ha. Ha.<br/>
PRESENT DUMBLEDORE: We apprehended him and turned him over to the courts, thinking that would be the end of this tragic story.""",
  "annotation":"""<p>"The crow of the rooster is fatal to it" is a rather silly rule; I wouldn't have used it if the Basilisk was a major character. Here, it provides a anticlimactic solution to one of the books' major conflicts, much like the way Voldemort was eliminated after zir attack on Harry's family.</p>

<p>One of my principles for <i>Voldemort's Children</i> as I was developing the story was that the characters should be forced to make decisions without having a convenient Dark Lord to oppose or seemingly wise adult authority figure to look to for guidance. By comparison to the other choices the characters make, the choice of how to dispose of the Basilisk is an <em>easy</em> choice, and therefore it can be covered in a quick and even silly way.</p>

<p>As a side note, the statue in the Chamber of Secrets is supposed to be a full-body statue and not just the head, but this is more recognizable from the films and fits more easily on the page (and this is a small enough detail of the story that it doesn't deserve the drama of taking up more page space or having a cooler view angle).</p>""",
},
{
  "force_id":"e080a857880f632e6916fed1076e40f5",
  "force_date":datetime.date(2012, 7, 7),

  "transcript":"""PRESENT DUMBLEDORE: You know the rest... how Riddle refused to show remorse and was sent to Azkaban for life... how he walked out, unaffected by the Dementors, and began his reign of terror as Lord Voldemort... How the old blood-purist faction flocked to him, even though he seemd to hurt his allies more often than he hurt his enemies...<br/>
Tom Riddle, now Voldemort, stands with two Dementors behind zem. The dementors are looking away. In front of zem, three people kneel &ndash; Narcissa Malfoy, Lucius Malfoy, and Bellatrix Lestrange. Voldemort is idly pointing zir wand down, conjuring magic the color of the Cruciatus Curse to flood over everyone. Voldemort isn't looking at them, though; ze is staring into space with the same blank expression as usual. Zir Time-Twister is glowing.<br/>
PRESENT DUMBLEDORE: But of this entire story, there is not one piece that I can truly understand. Was Riddle manipulating me from the beginning? Was it all just a trauma response? The only thing I know for sure is that my judgement has been clouded every step of the way...<br/>
The narrative frame of Dumbledore describing past events closes. In Dumbledore's office, ze dips a quill pen in an inkwell, using zir burned hand.<br/>
DUMBLEDORE: Just as it has been clouded in all matters that touch Harry Potter... {pause} I suppose... {in a very small voice} I suppose I must defer to yours.<br/>
We see a huge view of the Authorization for Deadly Force, the tip of Dumbledore's pen, and Dumbledore's burned hand as ze signs it.""",
  "annotation":"""<p>One thing I considered including on this page, but didn't, was an origin for the name "Death Eaters". The idea was that they were those who would eat anything from Voldemort's hand, even death, if ze chose to give it to them. I liked the idea, but the wording is convoluted enough that it seems contrived.</p>

<p>Still, Voldemort kills a lot of people <em>personally</em>, and even in the books, being a Death Eater is a significant risk factor for being killed by Voldemort. Voldemort kills about twenty named characters, and at least two of them (Peter Pettigrew and Severus Snape) were Death Eaters. The vast majority of characters aren't Death Eaters. So depending how you count, you can reach the conclusion that Death Eaters are <em>more likely</em> to be killed by Voldemort than the general population. Voldemort is willing to kill anyone who is not useful to zem, so even being in zir presence, no matter which side you're on, can be deadly. In <i>Voldemort's Children</i>, I don't think <em>anyone</em> is useful to Voldemort.</p>

<p>Voldemort's tendency to kill people is the main reason I didn't have Lily call Voldemort "Wizard Hitler" on <a href="/main/posts/209-voldemort's-children-page-43">page 43</a>; as far as history knows, Adolf Hitler didn't kill people personally (and ze certainly didn't have incredible powers). I <em>did</em> want to have Lily make a Muggle reference, though. (<a href="http://www.elidupree.com/main/posts/38-recommended-website-harry-potter-and-the-methods-of-rationality"><i>Harry Potter and the Methods of Rationality</i></a> has Harry say "Wizard Hitler", but it's a flippant comparison, while Lily's comparison is serious.)</p>""",
},
{
  "force_id":"b42bedeaa238a908027fd3a30053fdf9",
  "force_date":datetime.date(2012, 7, 8),

  "transcript":"""DUMBLEDORE: Perhaps you can stay&ndash;<br/>
Granger flies out through the wall the way ze entered and Disapparates after saying:<br/>
GRANGER: I do owe you a personal visit, but I am afraid it must wait until my duties of the day are completed.<br/>
Dumbledore is distraught.<br/>
The next thing we see is Granger in the Strategy Room at the Auror Offices, addressing the Aurors. Ze is carrying the parchment Dumbledore signed, and others, in zir left hand; in zir right, ze is pointing zir wand to levitate a Muggle water dispenser.<br/>
GRANGER: Aurors! I have brought you here for the second time today to discuss our new situation in relation to Luna Lovegood. I have, in my hand, the signatures of the Minister and entire Wizengamot to the effect that she is to be killed on sight. You may ask yourselves if this is the right thing; perhaps it is not, but as in any situation, by the time our Office becomes involved, the moment is long past when whatever happens will be the right thing. All that we can do is minimise the damage that occurs afterwards. You must prepare yourselves to be able to kill without hesitation. {pause} However... {pause} It would not do for a member of our Office to execute a mere prankster or hostage who has been disguised as Lovegood. To address this, the goblins of Gringotts have generously supplied me with a small amount of water from the Thief's Downfall, which cancels any magical concealment or enchantment. You will each be given enough to spray a person a few times. {pause} You must only use this water on a person you believe might be Lovegood, for three reasons: One, our supply is limited; two, it can be fatal to people who rely upon life-sustaining enchantments; three, I have promised the goblins that you will not, and cooperative wizard-goblin relations are more important than our lives. {pause} Shacklebolt, I believe you are familiar with this Muggle convenience; I didn't trust a magical keg to seal well after being disenchanted. I leave you in charge of its efficient usage. {pause} Tonks, if I may impose on your time for a final time today...""",
  "annotation":"""<p>Thus ends Chapter Seven, "The Riddle of the Past".</p>

<p>Why did the goblins do anything to help Granger? I think the most likely explanation is this: Granger has proven zemself an ally to the goblins, <em>and</em> ze paid them well for the Thief's Downfall water. Granger understands that for the goblins to sell the water at all, even for a high price, is a generous act rather than a stingy one. The goblins don't like participating in conflicts between one wizard and another. (Hence, also, why they demanded the promise that it would only be used for this specific purpose &ndash; a purpose which is not intrigue-filled and is potentially life-saving.)</p>""",
},
{
  "force_id":"23f577139d9cc36caf05806a6dbe78cd",
  "force_date":datetime.date(2012, 7, 9),

  "transcript":"""CHAPTER EIGHT<br/>
<br/>
An image of a set of scales. On the right side, there is a small version of Granger standing, being weighed. The left side of the scales is filled with small versions of other characters: Voldemort, Dumbledore, McGonagall, the Dursleys, Zabini, Crabbe, and Goyle. A hand reaches from above and pushes down Granger's side, so it appears that Granger is weighed heavier than all the others put together.<br/>
At the bottom is the chapter title:<br/>
The Harshest Judge""",
  "annotation":"""
<p>This will be a chapter about Granger!</p>

<p>The illustration was inspired by the Ancient Egyptian myth that, in the afterlife, your heart/soul is weighed against a feather. If it's heavier (meaning more evil) than the feather, then it will be devoured by a monster.</p>

<p>Incidentally, I've known what this image will be for a long time. For the earlier chapters, I've invented most of the title-page visual metaphors on the same days I drew them, but for this one and the next one, I've known since before I drew the first page.</p>""",
},
{
  "force_id":"bfd40bc801a1e82ddbda7fdf4463ab95",
  "force_date":datetime.date(2012, 7, 10),

  "transcript":"""GRANGER: Good evening, Harry. I have given much thought to your story since I was last here. One thing puzzles me: What changed your mind? When did you turn, from the child who would attack his closest friend for even suggesting a Dark path, to&ndash;<br/>
Granger and Tonks are standing in front of the window to Harry's cell, once again questioning zem. In the cell, Harry has an image of Voldemort (still with zir face visible) standing over zem. Voldemort is covering Harry's mouth. They speak in unison as they did on <a href="/main/posts/168-voldemort's-children-page-9">[TW: physical bullying] page 9</a>.<br/>
HARRY AND VOLDEMORT: No. Enough. I've told you far too much already.<br/>
GRANGER: You are not worried that no one will know your story?<br/>
HARRY AND VOLDEMORT: It's better if they don't. There's no reason for me to afflict even one more person with what I know.<br/>
GRANGER: Then perhaps I will, instead, tell you <em>my</em> story.<br/>
TONKS {whispering to Granger}: Granger, what are you doing?<br/>
GRANGER {whispering back}: Harry is strongly affected by even the simplest shows of respect. If I open up to him, he will feel obligated to open up to me. Seal the room so that we can't be overheard; I trust you, but not everyone should know what I will say now.""",
  "annotation":"""<p>Granger could also lie, I suppose, and give a mostly fictional account of zir past. That would be less nice for the reader, though. And, although Granger has practiced a wide variety of skills, I don't think "telling elaborate lies" is among them.</p>""",
},
{
  "force_id":"b6372b0964bb473775db5499d80affe6",
  "force_date":datetime.date(2012, 7, 11),

  "transcript":"""GRANGER: For me, it all begins with a troll. Months before, I had been an unnoted Muggle child; we have traced my ancestry back four generations, but there are no traces of magic in them.<br/>
We enter a narrative frame in which Granger describes past events. Things drawn in Granger's narration don't fade off into darkness at the edges; they are drawn in rectangular panels with black outside, but light everywhere inside.<br/>
We see an abstract family tree, with all of Granger's ancestors up to zir great-grandparents. Granger's parents are both wearing lab coats, as is one of zir grandparents. Another grandparent carries a pitchfork. Most of the people in the tree are light-skinned, like Granger, but one great-grandparent is quite dark-skinned, and ze's paired with a person dressed in a uniform like that of a military officer. Beyond the great-grandparents, there are only question marks.<br/>
PRESENT GRANGER: I had had many advantages: Good health... this intelligence that I have been told is extraordinary... My parents are medical professionals, and they gave me the best education up to age eleven that the Muggle world has to offer. But the moment that I feel sets me apart is the moment of my first Halloween at Hogwarts.<br/>
We see a troll &ndash; a large, blocky green humanoid &ndash; dragging a club and punching through a door. Next to the door is a sign indicating that this is a bathroom intended for female people.<br/>
PRESENT GRANGER: Later, I learned that Professor Quirrel had starved the troll to the point of desperation &ndash; Trolls are not naturally violent towards humans &ndash; and set it on the castle as a distraction while he attempted to steal the Philosopher's Stone. At the end of the year, Quirrel was caught and dismissed from professorship, and I received a Special Award for Services to the School, when I rescued him from the Devil's Snare during another botched theft attempt. {pause} But for the moment, knowing none of this, I was just a lone child facing against a creature much, much larger than myself...""",
  "annotation":"""<p>Sexist tropes used in the <i>Harry Potter</i> books: "The main female character will be <em>attacked by a monster</em>, while ze's <em>in a bathroom</em>, and ze will <em>need the male main characters to save zem</em> (despite the fact that ze's generally much more competent than they are)."</p>

<p>Before I started writing <i>Voldemort's Children</i>, I didn't think of the <i>Harry Potter</i> series as being particularly sexist. But now that I've started scrutinizing it more deeply (as I have to, in order to write a good fanfic), I've started seeing the sexism everywhere.</p>

<p>On a mostly-unrelated note, in real life, there basically aren't any creatures that intentionally walk around attacking other creatures, except for predators attacking prey. Wild animals often attack humans or other animals that intrude on their territory or come near their offspring, but alone in an unfamiliar place, it's rather strange that this troll would attack humans on sight. An animal that is large, slow, and stupid would not make a good predator; I'm guessing that trolls are omnivorous, something like bears.</p>

<p>The other possibility, I suppose, is that trolls were originally created by magic, and were specifically designed to be violent. I think the "trolls aren't monsters, just wild animals" interpretation is nicer, though.</p>""",
},
{
        
  "content_warning":""""violence""",
  "force_id":"9c12248c9272d3eda36bb5633a63347f",
  "force_date":datetime.date(2012, 7, 12),

  "transcript":"""PRESENT GRANGER: I had been in the bathroom, crying because of an insult that now seems insignificant&ndash;<br/>
PRESENT TONKS: Really? <em>You?</em><br/>
PRESENT GRANGER: Hard to believe, I know. For what it's worth, I was only eleven. In the moments before the troll struck me, I recall screaming, irrationally hoping that someone would come through the door and save me.<br/>
This page consists of six panels.<br/>
Panel 1: The eleven-year-old Granger is in the bathroom, facing away from the door, with zir hands over zir face, as the troll walks in through the destroyed door. There is a sink between them.<br/>
Panel 2: The troll stands over Granger; Granger looks up at it with a horrified expression. The sink has been torn out of the wall, and the exposed pipes are spilling water out onto the floor.<br/>
Panel 3:<br/>
PRESENT GRANGER: As its hand crushed my arm, I finally understood that this was real, that no one would fight for me, and that if I did not fight for myself, I would die.<br/>
A close-up, X-ray view of the troll's hand on Granger's upper arm shows that the arm bone (specifically, the humerus) is broken. The troll's hand has only three fingers, which have fewer joints than a human hand. (However, humans have often been drawn with three fingers, too, just because of the simplified style.)<br/>
Panel 4:<br/>
An angular view of the troll from Granger's perspective, looming above zem. Granger desperately casts a Stunning Spell into the troll's eye.<br/>
PAST GRANGER: Stupefy! { The incantation of the Stunning Spell. }<br/>
Panel 5:<br/>
PRESENT GRANGER: I had made the wrong move, and I realized my mistake faster than you could say "crush asphyxia". But I had just enough breath for one more spell...<br/>
The troll is lying on top of Granger. The floor has been cracked where the troll fell. Granger points zir wand at the troll.<br/>
PAST GRANGER: Wingardium Leviosa. { The incantation of the Hover Charm, which levitates objects into the air. }<br/>
Panel 6: The troll is floating near the ceiling. Granger is trying to crawl away. Zir left arm, the broken one, is folding up under zem, and zir left hand is purplish.""",
  "annotation":"""<p>Eleven-year-old Granger was familiar with the term "crush asphyxia" because the <a href="http://en.wikipedia.org/wiki/Hillsborough_disaster">Hillsborough disaster</a> had been in the news a lot in the past year.</p>""",
},
{
  "force_id":"dbd1b43b075b06f3dd020e4ad08feb2a",
  "force_date":datetime.date(2012, 7, 13),

  "transcript":"""PRESENT GRANGER: The professors were shocked that anyone below their third year had been able to stop a mountain troll. I had been lucky to hit it in the eye, they said; its hide can absorb even the best Stunning Spell. Professor McGonagall tried to scold me for putting myself in danger, but she could not hide her pride in my abilities...<br/>
A panel shows the young Granger lying on a white bed, with some kind of magical object like a cast for zir broken arm. McGonagall kneels next to the bed, smiling at Granger.<br/>
PRESENT GRANGER: I decided I was glad that it had been me. I had escaped with injuries no worse than Madam Pomfrey could heal overnight; what if another student had been there in my place? Better, I thought, for the danger to fall on the one best equipped to defend herself... {pause} But I had made a mistake, and that mistake had nearly gotten me killed. If I wanted to protect myself, or to protect others, I would have to be better-prepared the next time. And if my knowledge of magic was the only weapon I had... {pause} At the end of my second year, I signed up for every subject Hogwarts had to offer. I was issued a Time-Twister, becoming the first student since Tom Riddle for whom such an issue had been approved.<br/>
A panel shows a smiling Dumbledore putting a Time-Twister around the neck of a smiling Granger. McGonagall looks on; ze might be smiling, but zir expression is more ambiguous.<br/>
PRESENT GRANGER: So again I walked into a situation without knowing the dangers. The Ministry had not yet completed its research on the effects of Time-Twister use, which would show how much damage they can do even during routine application...""",
  "annotation":"""<p>What's so bad about destroying the fabric of time, anyway? It'll make life different, certainly, but will it actually be worse?</p>

<p>It reminds me of how some people in real life said "What's so bad about the Earth warming up by a few degrees?", and then it turned out that it causes massive ecological disasters. So it's probably something like that.</p>""",
},
{
  "force_id":"a4bbfcb8060d42ce545c977c3fd0cb3",
  "force_date":datetime.date(2012, 7, 14),

  "transcript":"""PRESENT GRANGER: Before my third year, a part-Kneazle cat named Crookshanks took a liking to me. Kneazles can sense magical deception, so when Crookshanks behaved aggressively towards Ron Weasley's rat, I was immediately suspicious.<br/>
This page consists of six panels.<br/>
Panel 1: Granger stands, holding up Crookshanks &ndash; a smiling, orange cat with a wide face. A sign nearby says "Thank you for shopping at the Magical Menagerie!", and on a nearby table, there is a bright green, glowing frog in a cage.<br/>
Panel 2: The rat, Scabbers (who's actually Peter Pettigrew in disguise) is hiding between a desk and a wall; Crookshanks, who doesn't fit between, is clawing at the rat, trying to reach it.<br/>
Panel 3: Granger confronts Ron Weasley.<br/>
RON: Come on, he's just a rat!<br/>
PAST GRANGER: Then you won't mind if I cast... Homenum Revelio! { The incantation of a spell that reveals nearby people, including if they're transfigured into animals. }<br/>
Panel 4: A large view of Granger's face facing the rat, casting the spell. Granger smiles triumphantly.<br/>
Panel 5: Pettigrew transforms back into a human and faces off with Granger angrily while Ron backs away in astonishment.<br/>
Panel 6: Granger shoots spells back in Pettigrew's direction.<br/>
PAST GRANGER: Impedimenta; Petrificus Totalus. { "Impedimenta", the Impediment Jinx, slows or stops a person or other creature in their tracks. "Petrificus Totalus", the Full Body-Bind Curse, magically holds a person completely still. }<br/>
PRESENT GRANGER: Preparation worked. I seemed to have a knack for running into Dark Wizards. Maybe, I thought to myself, I should become an Auror. I had not yet considered the... complications...""",
  "annotation":"""<p>In the magical world, not knowing that Kneazles can detect magical deception is like not knowing that cats purr. People tend to laugh at you if you don't know it. In this particular case, that means that people tend to laugh <em>at Muggle-borns</em>.</p>

<p>Laughing at people who lack cultural knowledge is one of the tools of exclusion in real life, too. Try not to do it.</p>

<p>Granger mentioned that fact because ze thought Harry might not know it, given Harry's history. But what if Harry <em>does</em> know, and feels insulted by the implication that ze wouldn't? But if Granger didn't say it, what if Harry <em>doesn't</em> know, and gets confused by the story?</p>

<p>How do <em>you</em> decide how much of the cultural context to explain when you say things to people?</p>""",
},
{
  "force_id":"bfab805808a6828501de9d38d91ced76",
  "force_date":datetime.date(2012, 7, 15),

  "transcript":"""PRESENT GRANGER: I had done a great deed, or so people told me. The names were not new to me, but I had viewed the tale of Pettigrew, and Black, and your parents, as mere history. {pause} Now I was part of that history, and according to the judgment of the world, I was the hero; Pettigrew had confessed everything, and now I was the one who had revealed the truth, set free the innocent, and delivered the guilty to their proper fate...<br/>
We see a view of Granger sitting in the Gryffindor common room, reading the Daily Prophet newspaper. The headline is "Hogwarts student uncovers Pettigrew", and it has a picture of Granger on the front cover.<br/>
DAILY PROPHET: Granger takes it all with perfect modesty. "All it took was one person to be suspicious of their neighbor's rat", she said in an interview. "And really, I wouldn't have noticed anything if it wasn't for Crookshanks. She deserves as much credit as I do." {paragraph break} Student response to the news that a Dark Wizard was living among them is mixed. "I know I'm going to take Defense Against the Dark Arts more seriously after this," Ron Weasley said, speaking for the majority. But not all students are surprised. "Everyone knows twenty percent of Hogwarts pets are unregistered Animagi," said Luna Lovegood, a second year Ravenclaw. "Mostly stalkers and overprotective parents, so a fugitive is nice for variety!"<br/>
PRESENT GRANGER: But when I return from it all &ndash; when the professors are done praising my skill &ndash; when the Aurors have thanked me for the last time for my cooperation &ndash; when Dumbledore has finally run out of breath with which to call me brave &ndash; when I am alone &ndash; I come before the harshest judge, who is myself.<br/>
Granger sits alone on a bed, looking fatigued. Two windows let in bright sunlight next to zem, but ze is looking away and the colors in the room are all dull despite the light. Unlike most of Granger's narration, this image fades into shadow at the edges.""",
  "annotation":"""<p>In the books, the characters call Crookshanks "he". In the fantasy novels I've read, if a female character has an animal companion, it's almost always male; I haven't been able to come up with any examples of a female character with a female animal companion. I'm sick of this "male and female are complementary opposites" bullshit, so I've decided to go against the trend here.</p>

<p>I haven't specified exactly <em>what</em> the difference from the books is, though; perhaps Crookshanks is a transgender female cat, and the only difference from the books is that Granger is perceptive enough to notice and respect that.</p>""",
},
{
  "force_id":"7b898a3cb6a3f8d88987789025faf96e",
  "force_date":datetime.date(2012, 7, 16),

  "transcript":"""PRESENT GRANGER: They allowed me to visit Sirius Black once. I didn't stay long; as soon as I entered the house, I felt nervous from all the anti-suicide jinxes working on my mind... They used to say that releasing someone from Azkaban was a death sentence... {pause} And what of the other person, Pettigrew, the one I'd put in Azkaban? Every new thing I learned about the place made me feel sicker about what I'd done. As a rat, he had been free, harming no one. Now he was having every happy thought sucked out of him... I had thought I was doing the right thing by turning him over to the law. But if those who enforce the law would not provide justice, who would? {pause} My father used to say, "if you want a thing done right, do it yourself." {pause} So my impulse to enter Auror training became a plan, with an uncertain path but a clear destination. With the Time-Twister, I told myself, I would not need to delay long before I could begin... What would have been my third and fourth years became the rest of my stay at Hogwarts.<br/>

A single large image: Granger, surrounded by the spiral arms of the glowing Time-Twister, much like on <a href="/main/posts/211-voldemort's-children-page-45">[TW: gore] page 45</a>. Granger is performing many tasks at once &ndash; ze is reading a book, writing on a parchment with one hand, holding zir wand in the other hand and using it to levitate the book and parchment, conjuring a fire to boil a potion that is overseen by Professor Snape, and transfiguring a pincushion into a hedgehog for Professor McGonagall.<br/>

PRESENT GRANGER: How much damage did I do, I wonder? Ever since the research came out, I have been plagued with thoughts of all the hours I took... Hours to study, when I could have worked harder in the time I had... Hours to rest &ndash; did I really need that rest more than the fabric of time needed to be whole? I was haunted by the story of the investigator who had picked up a shard of Voldemort's destroyed Time-Twister, and reappeared four years later... minus a few limbs, which waited six years instead...""",
  "annotation":"""<p>One thing that never made it onto a page is the reason for the Time-Twister's clockwise spiral.</p>

<p>You activate the Time-Twister by twisting the tiny hourglass in the middle of the spiral (which has occasionally been visible, but is usually too small to see in the pictures), in a counterclockwise direction. So the line is, "Whenever you try to turn back time, you only wind it tighter".</p>""",
},
{
  "force_id":"acceb9ee91654e7689b9ed55c74f42b4",
  "force_date":datetime.date(2012, 7, 17),

  "transcript":"""PRESENT GRANGER: Auror training was austere. We slept in bunks in the shared Auror quarters; we ate together and practiced together. Tonks was in training when I arrived. It was the first time I had a real friend in the wizarding world...<br/>
PRESENT TONKS: Aww, come off it!<br/>
PRESENT GRANGER: It's true! You treat me like an equal! At Hogwarts, everyone who didn't look down on me as a Mudblood was worshipping me as a genius...<br/>
A large panel shows a view of the Auror quarters. There are two pairs of bunked beds, which are rather drab-colored, and a drab door. A comfy chair sits in one corner. Past Granger and Tonks are crouched on the floor, around a chessboard, lit by a candle nearby. Granger, playing Black, has a king and a rook left; Tonks has a king and a knight. Granger is holding up the black king. The black king speaks in a pompous way.<br/>
BLACK KING: Well, I'm the King, and I say &ndash; I can move two spaces!<br/>
PAST GRANGER: But&ndash; but that's now how the <strong>rules</strong> work!<br/>
PAST TONKS: Heh, don't let a little chess set get to you, Granger.<br/>
PRESENT GRANGER: Sometimes one or two trainees would be taken on a mission with the full Aurors. We were supposed to be on the safer missions, but "safer" is a weak qualifier for any mission involving Aurors. {pause} Tonks, do you mind if I tell about when we raided the Malfoy home, after Lucius was brought in on corrpution charges? I don't need to if you'd rather I not&ndash;<br/>
PRESENT TONKS: Ha ha, are you worried Harry'll think less of me for it? Tell whatever you like.""",
  "annotation":"""<p>Silly King, Granger can win that rook vs. knight endgame without resorting to cheating. Cheating would certainly help, but I doubt ze would agree to it.</p>

<p>If Granger had a top bunk, ze wouldn't need that ladder to get down, and might even remove the ladder to force zemself to practice descending by magic. However, Granger has a bottom bunk.</p>

<p>Lucius was acquitted of corruption, of course, which, I assure you, has nothing whatsoever to do with the fact that ze recently offered generous gifts to certain Wizengamot members. The Wizengamot probably issues a warrant against Lucius whenever they're short on cash. All such actions against Lucius are, strictly speaking, legitimate, because ze actually committed the crimes they accuse zem of. How do you think Granger feels about participating in this scheme?</p>""",
},
{
        
  "content_warning":""""verbal abuse""",
  "force_id":"9e0fb34bcec57974051d114e19f6aac7",
  "force_date":datetime.date(2012, 7, 18),

  "transcript":"""PRESENT GRANGER: It happened only weeks before I would complete the training...<br/>
This page consists of eight panels.<br/>
Panel 1: A fancy iron gate in a brick wall. Beyond the gate are marble steps leading up to a door.<br/>
VOICE FROM INSIDE: Yes, thank you for your cooperation, Narcissa.<br/>
Panel 2: It turns out that the voice was John Dawlish. Ze is speaking to Narcissa Malfoy, in the same room with the stairs that we saw in chapter 5. Granger and Tonks stand by. Both of them are wearing the coats of junior Aurors.<br/>
DAWLISH: Tonks, Granger, check the rooms we passed on the way in. Wouldn't want anything to slip past.<br/>
Panel 3: Granger and Tonks are in a corridor. Granger is in the foreground; Tonks, in the background, is poking zir head in a door that branches off of the hallway.<br/>
PAST TONKS: Auror Office! Anyone in here?<br/>
Panel 4: Tonks walks into the room. There are a couple of comfy chairs, but it's too dark to see much.<br/>
PAST TONKS: No? Alright, then! Homenum Revelio... { The incantation of a spell that reveals nearby people. } Wait, there's someone hidi&ndash;<br/>
Panel 5: A hand points a wand at Tonks.<br/>
VOICE FROM OFF-PANEL: <strong>Crucio!</strong> { The incantation of the torture curse. }<br/>
Tonks is thrown backwards by the curse.<br/>
Panel 6: The caster of the curse, Bellatrix Lestrange, steps out from hiding. Tonks writhes in pain on the ground. Bellatrix has long, sleek black hair with bright white streaks in it, and has black marks under zir eyes that make zem look cool.<br/>
BELLATRIX: <em>Aurors.</em> They dare? Oh, that I must see my sister's home troubled with such filth...<br/>
Panel 7: Bellatrix continues torturing Tonks. We see zem from a low angle, almost from Tonks's perspective (though not exactly; Tonks is now face-down, covering zir face with zir hands).<br/>
BELLATRIX: And to send <em>you</em>... The final insult! Intruding on the very house you've defiled&ndash; { Tonks is the child of Bellatrix's other sibling by a Muggle. Since Bellatrix is an extreme blood-purist, ze has a personal grudge against Tonks. }<br/>
Panel 8: Granger steps to the door of the room and stares angrily inside.""",
  "annotation":"""<p>I've only seen bits and pieces of the films, and what I've seen seems mostly true to the books. The one character who's <em>nothing like</em> how I imagined zem in the books is Bellatrix Lestrange.</p>

<p>The thing that stands out to me about Bellatrix in the books is zir extreme pride, with the power to back it up. Ze is always in control of the situation (with the small exception of when ze's around Voldemort or Snape, who are better at controlling situations than ze is). Ze lectures Harry on how to use the Cruciatus Curse <em>in the middle of a battle</em>, ze declares zir loyalty to Voldemort <em>while being sentenced to life in Azkaban</em>, ze's second only to Voldemort in the number of named characters ze kills by sheer magical skill, and ze never passes up an opportunity to impose zir unforgiving, blood-purist ideology on other people.</p>

<p>In the films, ze's nothing like that; instead, ze's an "out of control woman" stereotype. The actor who plays zem describes zem as "really naughty" and "incredibly infantile". Ze just does whatever ze feels like, and ze always feels like causing havoc and destruction. There are a few elements of that in the books, but the films add a lot more that wasn't in the books at all, and reduce the other aspects of zir character.</p>

<p>There's an interesting question here about the concept of <strong>agency</strong>: The actor describes Bellatrix-in-the-films as "liberated", but to me, it feels like ze lacks agency, because, unlike in the books, ze's never steering the course of the narrative &ndash; instead, ze's going along with the narrative created by the other characters.</p>

<p>In my process of writing <i>Voldemort's Children</i>, the important thing about each character is not the personality quirks ze happens to have, but the ideology ze attempts to impose on the world.</p>""",
},
{
  "force_id":"d2a690d4bffac50cb4757df08b479811",
  "force_date":datetime.date(2012, 7, 19),

  "transcript":"""The top half of the page is divided into six panels.<br/>
Panel 1: Past Granger, standing in the doorway, shoots blue magic beams at Bellatrix.<br/>
Panel 2: Bellatrix deflects the beams and blasts back at Granger with orange magic. Granger blocks it with a shield.<br/>
Panel 3: Bellatrix continues blasting and jams zir wand close to Granger's shield, but fails to break through it.<br/>
Panel 4: Tonks crawls up from the floor and shoots red beams at Bellatrix. Granger hits Bellatrix with a blue-green spell.<br/>
BELLATRIX: Ack&ndash;<br/>
Panel 5: Bellatrix starts to Disapparate.<br/>
BELLATRIX: You've been lucky this time, Auror. But I know your face. It won't go well for you next time we meet.<br/>
Panel 6: Granger alone.<br/>
PAST GRANGER: Damn. Disapparated...<br/>
PRESENT GRANGER: Lestrange and I did not meet again, however.  She died at your hand before we could track her down.<br/>
PRESENT HARRY: Sounds like I've done you both a favor.<br/>
PRESENT GRANGER: Perhaps you have.<br/>
PRESENT TONKS: You're just going to let him say that?! <em>Murder</em> is a favor now?<br/>
PRESENT GRANGER: You disagree with him, I assume?<br/>
PRESENT TONKS: Of course&ndash;<br/>
PRESENT GRANGER: Then there is no one here to whom I must prove myself. At the time, nothing could have been further from my  mind...<br/>
The bottom half of the page is divided into four panels with angular borders.<br/>
Panel 1: Past Granger looks at past Tonks with concern.<br/>
PAST GRANGER: Are you alright?<br/>
PAST TONKS: Yeah, just a little shaken is all.<br/>
PAST GRANGER: Cast a Shield Charm.<br/>
PAST TONKS: Eh?<br/>
PAST GRANGER: Just cast it.<br/>
Panel 2: Tonks strains to cast the Shield Charm.<br/>
PAST TONKS: Protego!<br/>
Only fragments of a shield appear.<br/>
PAST GRANGER: ...you're not alright.<br/>
Panel 3: A distant top view of the room.<br/>
PAST GRANGER: Please rest. The couch is not cursed.<br/>
Tonks sits on a couch that was in the room.<br/>
PAST GRANGER: I will inform Dawlish. Expecto Patronum. { The incantation of the Patronus Charm, which creates temporarily creates a silvery animal which, if the caster is skilled enough, can be used to deliver messages. }<br/>
A silvery dragonfly appears and Granger sends it out through the door.<br/>
Panel 4: Tonks smiles weakly and looks up from the couch.<br/>
PAST TONKS: d'y'know {do you know} how scary you are sometimes?""",
  "annotation":"""<p>The original design for this page involved Granger fighting some random Dark Wizard, and easily defeating and capturing zem. When the Dark Wizard in question turned out to be Bellatrix friggin' Lestrange, I had to revise that series of events a bit. I think Granger can defeat any single other character, but not necessarily without a fight.</p>

<p>If I had more time to spend on this scene, I'd make Bellatrix use the same blue shield that Granger uses, to emphasize how they're both powerful wizards who fight on the same terms. The duel would also have more tension, while they both tried to break through the other's shield, and be less showy, with fewer beams flying around. (Incidentally, I think Granger's opening volley on this page is mainly to distract Bellatrix from Tonks rather than to be an effective attack.) But in a half page, it was simpler and easier to do the "orange vs. blue" thing.</p>""",
},
{
  "force_id":"59570d6845026958fbc3a1da843980cc",
  "force_date":datetime.date(2012, 7, 20),

  "transcript":"""PRESENT GRANGER: We finished the job without incident, and Tonks insisted that there was no need to worry on her behalf. But I barely slept that night, hearing her toss and turn on the bed above mine. Intellectually, I was familiar with the psychological aftermath of the Torture Curse; Tonks was not the first of my new companions who had experienced it, and she would not be the last. I had studied both the Muggle and the magical interpretations of trauma. But I fell to wondering:<br/>
The page is dominated by a large panel of Granger lying in bed, looking up at the wooden boards that hold up Tonks's bed above zem.<br/>
PRESENT GRANGER: Must I be the only one with the power
to hold the world at a distance? {pause} Will I always remain safe, while those around me suffer? {pause} So the next morning...<br/>
Past Granger hurries down a corridor after Alastor Moody.<br/>
PAST GRANGER: Moody? I need to ask something of you. Something no one else will help me with.""",
  "annotation":"""<p>What do you choose to do when you realize how full of horror the world is?</p>""",
},
{
  "force_id":"c4e0ee8999380a3d2c46b9291e0737d2",
  "force_date":datetime.date(2012, 7, 21),

  "transcript":"""PAST GRANGER: Let's go somewhere where we can't be overheard.<br/>
Granger takes Moody's arm and Apparates to a sunlit location with a lake, some tall grass, and trees.<br/>
Moody's speech is drawn in a very rough style, and is much darker than Granger's.<br/>
MOODY: Where are we?<br/>
PAST GRANGER: The first thing I did after I learned to Apparate was to find and memorize eighteen remote locations to use as escape routes. Now that you've seen this one, I have seventeen left. I picked them using dice and a map of Britain, so there's no way for anyone else to guess where I would have picked.<br/>
MOODY: Useful. But what will you do if your enemy grabs you before you can Disapparate?<br/>
PAST GRANGER: I've equipped two locations with traps for anyone who follows me.<br/>
MOODY: So you could have taken me into a trap. Good. Right then. You had a favor to ask. One that requires a moderate level of security.<br/>
PAST GRANGER: I want you to use the Cruciatus Curse on me. If I'm going to face it, and my fellow Aurors are going to face it, I need to know what it's like to be hit by it.<br/>
PRESENT GRANGER: Or so I rationalized it to myself. What did I expect to accomplish? Would putting myself through this somehow change what had happened? Or was it simply the most convenient way to assuage a sense of suvivor's guilt? Do I know myself well enough to be sure?""",
  "annotation":"""<p>Granger may be second-guessing zemself here, but to Moody, that explanation seemed perfectly sensible and logical!</p>

<p>This was obviously before Granger <a href="http://www.elidupree.com/main/posts/224-voldemort's-children-page-52">instituted the policy about saying "Torture Curse" instead of "Cruciatus Curse."</a></p>

<p>Granger also has escape locations outside of Britain, but there's a limit to how far you can Apparate, so those locations are only relevant while Granger is travelling to other countries.</p>

<p>One thing that I left out of this page was to have Granger and Moody confirm each other's identities before leaving the Ministry. It would have added to the "Moody is totally serious about security, and so is Granger" thing, but I couldn't come up with a good way to do it. They could have security questions, but it's hard to come up with shared information that can't also be guessed by someone who's been planning to impersonate you, and the bigger threat is if the person is under the Imperius Curse (Can the curse force someone to give the proper answer to a question? I'd guess that it can). The real Granger can resist the Imperius Curse, but it wouldn't be Moody's style to trust in that.</p><p>The only clever solution I came up with was for the two parties to make an Unbreakable Vow that they would truthfully reveal their identity and whether they're acting of their own free will. However, if that style of thing worked, people could use Unbreakable Vows for all kinds of things, which would change a lot of stuff about society in unexpected ways. So I figure there must be some major additional restrictions on the Vow that make it undesirable for general use. (Also, it requires a third person.)</p>""",
},
{
  "force_id":"829e44ef515bc2933e02bc6e5633e59f",
  "force_date":datetime.date(2012, 7, 24),

  "transcript":"""This page is divided into eight panels.<br/>
Panel 1: The trees and lake are still visible. Moody, facing away from Granger, looks back over zir shoulder.<br/>
MOODY: I'll do it. Are you ready?<br/>
Panel 2: Granger, looking determined, is set against an empty background.<br/>
PAST GRANGER: I am ready.<br/>
The next three panels are very angular and slant upwards across the page.<br/>
Panel 3: Moody casts the torture curse at Granger; the whole panel is filled with its orange light. Granger is still standing, head bowed, wand held at zir side.<br/>
MOODY: Crucio.<br/>
Panel 4: Granger falls to zir knees in pain from the curse.<br/>
Panel 5: Granger pulls up zir wand, blocking the curse with a shield.<br/>
Panel 6: The shield hovers between Granger and Moody.<br/>
PAST GRANGER: Is the spell supposed to leave me enough concentration to cast a shield&ndash;<br/>
Panel 7: Close-up of Granger's face, looking somewhat angry.<br/>
PAST GRANGER: &ndash;or did you hold back on me?<br/>
Panel 8: Close-up of Moody's face. Ze looks astonished.""",
  "annotation":"""<p>Is Moody shocked that Granger caught zem being a softie, or is ze shocked that Granger is badass enough to cast spells while being tortured at full power? Or something else entirely?</p>

<p>This is the second <a href="http://en.wikipedia.org/wiki/False_dichotomy">false dichotomy</a> Granger has made in two pages. Does that mean that Granger cares more about rhetorical effectiveness than about logic?</p>""",
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
