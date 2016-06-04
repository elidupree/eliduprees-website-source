#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime



posts = [
{
  "title":"""A look at Lasercake, one of my upcoming projects!""",
  "force_id":"eccf2348a0bdbee93be643a8c728fae2",
  "force_date":datetime.date(2012, 4, 14),
  "tags":["announcements","Lasercake"],
  "contents":'''

<p>[Update: This project now has its own website at <a href="http://www.lasercake.net/">lasercake.net</a>]</p>

<p>I wrote the following (slightly edited for the web) as part of an application for the "Senior Scholars" program here at Colby College, which will allow me to earn academic credit for doing this project.</p>

<h2>Overview</h2>

<p>Lasercake is an educational computer game project.</p>

<p>As a game, Lasercake will be a open "sandbox" game – one where the player is presented with a world to experiment in, rather than given a specific goal to accomplish as effectively as possible. As an educational project, the <cut>game environment will give the player numerous opportunities to encounter real-world science within the context of an industrial empire that the player is allowed to create.</p>

<p>It has become very clear how much potential there is for learning in computer games like this. One of the inspirations of this project is the SimCity series of games, in which the player takes on the role of a city planner, and develops a city by assigning zoning and building roads, power plants, and other city infrastructure. Research on SimCity has shown that it significantly alters how players understand city infrastructure and management (Tanesa and Cemalcilar, 2010) and is consistently useful, despite certain limitations, as an educational tool (Gaber, 2007). I recall playing SimCity 2000 while growing up, and it was a valuable contributor to the perspective that I have now. Active participation in a virtual world allows people to develop knowledge in a way that passively receiving information cannot (Annetta, 2010). So there is a great, unseen need for games that can present understandings of other systems within our world – especially when the commercial game industry seems uninterested in creating such games, and consistently presents unrealistic or imaginary science. (I happen to believe that there are many ways in which even commercial games help kids' intellectual development, it's just that presenting accurate science isn't one of them.) Lasercake, by contrast, will attempt to use accurate science as a way to promote an understanding of energy and ecological issues.</p>

<p>For example:</p>

<ul><li>All the player's power generators, robots, lasers, factories, and so forth use real-world energy quantities, with joules as the basic unit. Time, distance, and other quantities are also measured in SI units, and are consistent throughout (for example, a hydroelectric power generator extracts the actual amount of potential energy that you can compute would be stored in the volume of water that passes through it, and the game tutorials will emphasize this aspect while they explain how you build the generators).</li>
<li>Most games that offer the player a way to dig in the ground simply have the rock disappear in front of the player's digging equipment. In Lasercake, by contrast, the mine waste has to be hauled out of the mountain and left somewhere, where it will pollute the surrounding land and water and disrupt the local ecosystem. There will be multiple systems (water cycle, temperature, flora, fauna...) – each implemented in a relatively simple way in its own right, so that it can simulate very quickly and the player can come to understand it without excessive explanation (and, as it might bear acknowledging, so that I can implement all of them within the relatively short timetable of one year).</li></ul>

<p>Again, this is all in the context of an expansive world where the player can build at their own pace. Since it doesn’t have a specific goal where you win or lose, it can appeal to a wide range of players – newcomers won’t have to worry about their ability to be successful, power gamers will find the range of options in the game wide enough to build incredibly awesome things, and almost everyone can appreciate the fun of being able to build their own high-tech establishment full of robots and lasers. These are many of the attributes that made the SimCity series such a success as well.</p>

<p>There will be a series of in-game tutorials (or more accurately, a web of them) that introduce the game concepts, and the science behind them, in an intuitive way.</p>

<h2>Background</h2>

<p>I have already begun work on the technical side of Lasercake, in conjunction with <a href="http://www.idupree.com/">my sibling, Isaac</a>. We worked together for three weeks during last winter break and part of January to implement the most complicated parts of the physics; we have a working demo that I've showed to the professors who will be involved in the project. Isaac and I work very effectively together, and we will continue to collaborate on this project throughout the upcoming year. We have made extensive plans for how to accomplish all of the things written above.</p>

<p>Lasercake is multi-platform; it is written in the programming language C++ and uses OpenGL for graphics, which both work on all major operating systems. Some of the new web technologies currently being popularized will also enable us to run the game simulation on a server and allow anyone to play through a web browser.</p>

<p>Isaac and I both literally grew up doing computer programming, including experimenting with how different systems behave depending on the rules one sets for them. We have extensive knowledge of the things included in the technical side of this project. Both of us have contributed to many open-source software communities; Isaac has also studied software development at Marlboro College, participated in Google Summer of Code, and interned at Fog Creek Software.</p>

<p>From the environmental-science side of things, although I haven't made that part of my academic study at Colby College, I do my best to follow environmental activism and stay informed through a variety of channels – not least of which is my family, all of whom take a great interest in the sciences. My high school education gave me a very good background for this area, with an AP Biology teacher who made zir course very in-depth and aware, as well as the most advanced classes available in physics and chemistry. Isaac also brings valuable knowledge; ze has studied environmental science academically at Marlboro College, ze helped me develop the ideas explained above, and ze has chaired Marlboro's Environmental Quality Committee.</p>

<p>The course I took this January, "Creating Media for Social Change", has had a significant influence on this project; if there were more courses on that subject, I would certainly have taken them. Theater design classes both here and in high school have helped me develop a way of thinking about how to present ideas through visual images. Anyone who knows me more than as a passing acquaintance knows my interest in how to construct a wide variety of media in order to promote new understanding.</p>

<p>Since this is a very multi-disciplinary, ambitious project, the Senior Scholars program seemed like a natural avenue in which to pursue it.</p>

<h2>Timeline</h2>

<p>The timeline I anticipate is as follows:</p>

<p>Isaac and I will work on Lasercake throughout the summer. By the time I return to Colby in the fall, it should be in a state where most or all of the game systems exist at least in a rudimentary way, so that, once at Colby, I can concentrate on what I consider the true meat of this project: developing the ways in which the user can interact with the game, and refining the game in order to best communicate the understanding that I intend to communicate. This refinement involves both the game mechanics (i.e. what happens in the game and what the user is able to do) and the tutorials through which the game presents those mechanics.</p>

<p>I'm at a bit of a loss to provide a monthly timetable, because of the essential way that this project involves figuring out what will have the desired effect as much as it involves creating something that I already understand. It will be steered by the feedback I get – and I will present it both to other students here at Colby, and to students at in the 4-6th grades in two local school districts. The project isn't locked into one course, because it will – must – be able to adapt to accommodate (or abandon) to the points at which it fails to communicate, and to fully pursue any way in which it's particularly effective.</p>

<p>Lasercake will also operate on the mantra of the dominant Free-and-Open-Source-Software development model: "Release early, release often." We already have <a href="https://github.com/elidupree/Lasercake">a repository on GitHub</a> (a website used for collaborative work on open-source projects), and our code is licensed under the GNU GPL, a Free Software license that allows people to view the source code and create their own versions, but prohibits them from taking advantage of the "share-alike" system by imposing additional restrictions on their versions or hiding their code modifications. In this way, Lasercake is part of the larger Free Software community, which is usually a very supportive community where people are eager to collaborate and offer their different skills to any project that seems worth contributing to. By having a transparent development process and frequent release schedule, we can let people outside the project follow what we're doing and offer feedback or even contributions.</p>

<p>By the end of the year, I hope to have developed Lasercake to the point where I am ready to reach out to schools and educators to offer Lasercake as a way for students to engage in science and scientific thinking.</p>

<h2>References</h2>

<p>Annetta, L.A. "The “I's” have it: A framework for serious educational game design." Review of General Psychology, 2010, Vol. 14, No. 2, 105–112. <a href="http://psycnet.apa.org/journals/gpr/14/2/105/">http://psycnet.apa.org/journals/gpr/14/2/105/</a></p>

<p>Gaber, J. "Simulating Planning: SimCity as a Pedagogical Tool". Journal of Planning Education and Research 2007 27: 113 <a href="http://jpe.sagepub.com/content/27/2/113.refs">http://jpe.sagepub.com/content/27/2/113.refs</a></p>

<p>Tanesa Z, Cemalcilar Z. "Learning from SimCity: An empirical study of Turkish adolescents". Journal of Adolescence, Volume 33, Issue 5, October 2010, Pages 731–739. <a href="http://www.sciencedirect.com/science/article/pii/S0140197109001304">http://www.sciencedirect.com/science/article/pii/S0140197109001304</a></p>''',
},
{
  "title":"""Social standards of dress""",
  "force_id":"a90fa6a646f897c25aec387ef32b09ab",
  "force_date":datetime.date(2012, 5, 29),
  "tags":["gender"],
  "contents":'''

<p>I wrote this for a discussion on an Internet forum, in response to a person saying that it was "disrespectful" to violate social standards about what clothing to wear in specific situations.</p>

<p>It's easy for you to say that if you have the <em>ability</em> to conform to those social standards of dress (either at all, or without going to prohibitively large amounts of effort).</p>

<p>For instance, "dressing up" is a (not entirely anymore, but still mostly) gender-segregated thing: There isn't a way "to dress up", there's a way "to dress up male" and a way "to dress up female". This causes me two problems:</p>
<ol><li>Since I'm agendered, there is no possible way for me to dress up.</li>
<li>Even if I could, I wouldn't, because I hate gendered conventions with a fiery passion.</li></ol>
I personally deal with this by never going to a venue that requires me to dress up, but not everybody has the luxury of being able to avoid such venues.

<p>And to some people, "dress up" means "buy an extra garment you can ill afford".</p>
<p>Or "Battle your depression into letting you spend lots of effort dealing with clothes and body stuff, using energy you would rather have spent on the actual task".</p>
<p>Or "Spend all day trying to overcome social anxiety to go ask some social person to help you choose clothing because you cannot seem to understand what the conventions are".</p>
<p>Or many other things.</p>

<p>My moral system says it's intolerable to pressure someone into doing the above things merely to make them look "nicer", so I cannot agree with a set of conventions that does that. So maybe there are two options left:</p>
<ol style="list-style-type: upper-alpha"><li>Pressure people to do that if it's easy for them, but don't pressure people if it's too hard for them;</li>
<li>View clothing conventions as optional and don't pressure anybody to do them.</li></ol>
<p>Option A is completely impossible, since you cannot actually know how hard it is for people (unless you're going to go around asking them all the time, which would be a total waste of effort and probably a form of pressure in itself). So, lacking any other choice that isn't repugnant to me, I take option B.</p>''',
},
{
  "title":"""I'm back!""",
  "force_id":"892485471d1663a3e61417f14af6ae52",
  "force_date":datetime.date(2013, 6, 7),
  "tags":["announcements"],
  "contents":'''

<p>I haven't blogged in more than a year, but that will now change!</p>

<p>A little after my last blog post, I strained my wrist by programming for eight hours and drawing comics for five hours every day for a week. For a few months, I could barely type &ndash; so I stopped blogging, and when I got better, I was busy with other things. Like college. I graduated from Colby College this year, and despite its many structural problems, I think I managed to squeeze a good education from it.</p>

<p>Let me tell you about some of the things I've done in the last year. Leave a comment to tell me which ones you want to hear more about!</p>

<h2>Before this summer</h2>

<p>Watched a lot of anime. Solved all the levels of <a href="http://fillets.sourceforge.net/">Fish Fillets</a>. Got paid to tutor some people in math. Did a lighting design for a short dance piece. Worked on <a href="http://www.lasercake.net">Lasercake</a> a lot and released a prototype. Did BDSM with a partner for the first time. Ran a tabletop RPG for the first time. Played a tabletop RPG for the first time. Learned (and invented!) some useful knots. Wrote a 10-minute play and had it produced by the Colby theater department. Participated in some student activism. Built an exellent new device to carry my stuff around in. Initiated five other people into Eli Dupree's Cult of DOOM. Designed a sexual board game, and learned a lot about <a href="http://inkscape.org/">Inkscape</a> to do it.</p>

<h2>Since the beginning of this summer (May 18)</h2>

<p>I'm at home now, with nothing but free time to do awesome projects all the time!</p>

<p>Reorganized my room. Reorganized my computer stuff. Started improving my diet, inspired by <a href="http://soylent.me/">Rob Rhinehart's "Soylent" project</a>. Learned to use a sewing machine. Got back to working on my comic. Started using an EMG biofeedback device to help me draw without clenching my hand. Set up an exercise bicycle we have and improved my bicycle endurance a lot. Continued work on Lasercake and the board game. Updated a <a href="http://www.wesnoth.org/">Battle for Wesnoth</a> add-on (<q>Era of High Sorcery</q>) that I wrote years ago. Bought a used monitor, built a wooden shelf, and rearranged my workstation <a href="/media/workstation_2013_06_04.jpg?rr">[picture]</a>.</p>

<h2>Some things I'm going to do soon</h2>

<p>I'm going to finish <i>Voldemort's Children</i>, finally. It will probably take me at least a month, and I'm going to do all the remaining pages as a batch (so I won't be able to post any until it is all finished). But it is coming!</p>

<p>I'll redesign this website a bunch. Writing it from scratch two summers ago was a great experience, but now that I've used it for a while, I've seen a bunch of flaws in its current design.</p>

<p>I'll leave it at that for now. I don't know what else I'll do next, because there are so <em>many</em> different things I want to do next! But you will hear from me soon. I will blog more, I promise! I'm going to try to post at least one awesome thing each week, possibly more.</p>''',
},
{
  "title":"""The Food Experiments""",
  "force_id":"e1e2e7d11d0c4813c38f721358563a4a",
  "force_date":datetime.date(2013, 6, 11),
  "tags":["crass physical reality"],
  "contents":'''

<p>Inspired by <a href="http://soylent.me/">Rob Rhinehart's "Soylent" project</a>, I've been changing my diet. I'm trying to improve three aspects: Nutrition, portability, and price.</p>

<p>I've always had problems with eating. I don't <em>like</em> eating food, so I often don't eat enough of it. And I'm extremely sensitive to taste, so most foods are overwhelmingly strong and I can't eat them. Between those two things, I don't try new foods very often.</p>

<p>Previously, the main parts of my diet were rice, cheese, apple juice, and a multivitamin. For such a limited diet, that's not bad. But it's not great either. I think I was <cut>deficient a bunch of nutrients, including potassium. And the other downsides of cheese are that it needs to be refrigerated and that it's relatively expensive. The cheese I ate was costing more than $2 per day by itself, and all my food together cost about $4.18 per day. (All prices here are listed in US dollars and cents because that's the local currency.)</p>

<p>Replacing cheese wasn't easy, though. As far as I can tell, it was:</p><ul><li>my only source of protein</li><li>my only source of fat</li><li>my only source of sodium</li><li>my only source of calcium</li></ul>

<p>So what did I do?</p>

<h2>Building a new diet</h2>

<p>Well, I needed information. I got a lot of that from <a href="http://nutritiondata.self.com">this website that lists food content</a> and <a href="http://fnic.nal.usda.gov/fnic/interactiveDRI/">this tool to estimate my nutrient needs</a>, both of which are based on USDA data. (It could be better, but it's a lot more reliable than most nutrition information on the Internet.) Bear in mind that the nutrient needs are an approximate, and vary between people and environments. For instance, it recommends 2700 calories per day for someone of my height, weight, sex, and activity level, but when I'm eating the amount that feels right to me, I usually eat around 2300 calories (estimated).</p>

<p>Then I looked at the foods that are available cheaply at the local grocery store.</p>

<p>The ruler of calories-per-dollar is vegetable oil - it costs about 56 cents to get me 2300 calories. The downside of vegetable oil is that it has nothing <em>but</em> calories in it.</p>

<p>Next up are the grains - wheat flour, corn meal, rice, beans. They range from $1 to $2 for 2300 calories. They provide a lot of calories from carbohydrates, mostly complex carbs. The beans also provide a lot of protein, potassium, fiber, and a lot of the micronutrients as well.</p>

<p>I started eating black beans, which are very nutrient-dense and have a very bland taste.</p>

<p>As soon as I started eating black beans, my nose cleared up. My nose has always been stuffy &ndash; I've never been able to comfortably breathe through my nose, at least not if I want to get enough air. Now I can breathe through my nose easily &ndash; in fact, I was doing it without even noticing while I wrote this paragraph. I figure the stuffiness must have been a symptom of some nutrient deficiency.</p>

<p>So my new diet is based on black beans and canola oil. I also got a new multivitamin/multimineral pill that's more comprehensive than the one I was taking.</p>

<p>Black beans are about 25% protein by calorie. They aren't a "complete protein" in the strictest sense of the term, but I looked at their actual amino-acid content and the intake recommendations, and since I'm eating so much of them, I should meet all the recommended amounts. The main things still missing are sodium and calcium &ndash; the body needs too much of them to fit in a pill. Sodium is easy &ndash; I just add table salt. For some reason, I have no problem eating things that are very salty.</p>

<p>Most calcium-rich foods are much more expensive than the oil and beans. Some people take supplements in the form of purified calcium carbonate or calcium citrate, which are much cheaper (per calcium) than the foods. I was planning on doing that. But then I learned that eggshells, which are mostly calcium carbonate, are an effective source of calcium too. (But be careful - uncooked eggshells, like uncooked eggs, can carry salmonella, so make sure to cook them first.) One of my family members eats eggs frequently, so I'm having zem save zir eggshells to add to my meal.</p>

<p>In theory, if I eat nothing else, these ingredients will cost somewhere between $1.30 and $1.50 per day, and provide <em>all</em> the nutrition I need.</p>

<p>Problem: Black beans mixed with canola oil and eggshells were disgusting to eat. And cooked beans still require refrigeration. I had to do something about that.</p>

<h2>Preparing the new food</h2>

<p>I rarely leave my house. Part of the reason for that is that everything I need is here; the other part is that traveling is inconvenient. I want to eventually start going out more, so I'm working on making travel more convient. One thing I'm doing is training my bicycle endurance. Another is making a food that I can easily carry for a day without refrigeration.</p>

<p>To do that, I dehydrated the beans. Right now, I'm doing it by cooking them in an oven for about two hours at 250&deg;F (121&deg;C), opening the door sometimes to let out the steam. But I'm hoping to build a solar dehydrator to reduce the amount of heat it lets into the house (and also to save electricity).</p>

<p>Dried beans are very hard, which makes them difficult to eat. So I grind them into powder. I was lucky that we already have a hand-powered food grinder in the house. (We also have an ancient blender, but it's very loud, incovenient to clean, and makes an inconsistent product). I also throw the eggshells into the grinder with the beans, and get a bean powder / eggshell powder mix.</p>

<p>Both canola oil and dry bean powder can keep for a very long time without refrigeration.</p>

<p>When I want to eat it, I pour out some powder, add oil until it's not too dry to eat, and add salt. I get this:</p>

<img src="/media/new_food_2013_06_11.jpg?rr" alt="a bowl full of dark, clumpy stuff, with a spoon in it" />

<p>It's pretty tasteless except for the salt. It sticks to itself a bit, so it's hard to spill, which makes it a good thing to snack on while I work. Although it would be even better if I could make it into crackers so that I don't need the bowl and spoon.</p>

<p>That amount is about half a meal. It's very high in calories-per-size (which makes it even better for travel) because it has essentially no water or air in it, and has a lot of fat in it. A full bowl of it would be more than a day's food.</p>

<p>I haven't switched over to eating this exclusively (and probably won't), but I'd like to try going for a few days on just this stuff to see how it works out.</p>

<p>Lastly, people say that you fart more if you eat lots of beans, but I haven't noticed myself farting much more than usual.</p>

''',
},
{
  "title":"""I made biscuits!""",
  "force_id":"c840af63853c95cf2bc19ccf27557cbb",
  "force_date":datetime.date(2013, 6, 16),
  "tags":["crass physical reality"],
  "contents":'''

<p>Following <a href="/blog/the-food-experiments">my last experiments</a>, I've been trying to put my bean/oil/eggshell mush into a more convenient form. I'm now eating this stuff for all my meals except breakfast each day.</p>

<p>At first, I tried baking using just the bean powder. The results were too crumbly to be practical, so I added wheat flour.  A family member suggested that, instead of dehydrating the cooked beans and then re-baking them, I could just mash the cooked beans in with the other ingredients before baking them. That also saves the trouble of grinding them. I tried it and got this:</p>

<img src="/media/biscuits_2013_06_16.jpg?rr" alt="A cooling rack with about 16 lumpy biscuits on it" />

<p>(The colors are a bit off in that photo; the one on the far right is the closest to their actual color.)</p>

<p>These were pretty good - they're crunchy and a bit hard to chew, but <cut>I currently like that. I can still improve upon them, but the basic idea works great.</p>

<p>My recipe for this batch was:</p>

<ul>
<li>3 cups cooked beans</li>
<li>1 cup whole wheat flour</li>
<li>1/2 cup canola oil</li>
<li>1/2 tsp salt</li>
<li>eggshells (see below)</li>
</ul>

<p>Mix together the ingredients in a bowl and mash them up (I used a tough <a href="http://en.wikipedia.org/wiki/Pastry_cutter">pastry cutter</a> for that). Knead thoroughly, roll and fold in thirds repeatedly, fold in half and roll into about 1/2 inch sheet, cut into biscuits and bake at 250&deg;F for 2 hours. (Biscuits are usually cooked at a higher temperature, but we think the higher temperature might destroy some of the nutrients, and there's no particular reason to do it.)</p>

<p>I used about one eggshell for this. Later that day, I received a milligram scale that I'd ordered, and massed an eggshell. It was about 6.1 grams, which should be about 2.2 grams of calcium<footnote((Eggshells are at least 90% calcium carbonate, and calcium carbonate is 40% calcium by mass. 6.1g eggshell * 0.9g CaCO<sub>3</sub>/g eggshell * 0.4g Ca/g CaCO<sub>3</sub> ~= 2.2g Ca.))>. This batch was about a day's food; the recommendation is one gram of calcium per day, and not more than 2.5 grams. Getting 2.2 from the eggshells is pushing it. Before I measured it, I had mistakenly thought the eggs had about half that much calcium. Well, good news: I can now use half as many eggshells, which is a closer match for how many eggs my family eats anyway!</p>

<p>The beans would otherwise become 1 cup of dried bean powder, so this recipe is essentially using a 1:1 ratio of bean to wheat, by volume. The beans are more calorie-dense and nutrient-dense per volume, though. Earlier, I tried using less wheat, but the biscuits were still too crumbly. However, in those tests, I was also still using the gritty bean powder instead of whole moist beans, which might make a difference. More tests are in order.</p>

<p>The salt is a bit less than my formula calls for; I haven't been getting the recommended 1.5g/day of sodium, and my body hasn't been craving more. Maybe that's appropriate because I sweat less than the average person, both physically (I overheat fast because I don't sweat much in the heat) and behaviorally (I'm fairly inactive and I avoid heat as much as I can). I've heard that the body is fairly good at regulating its salt intake, so I might start craving salt if I actually need it. I'll pay attention to whether that happens as time goes forward.</p>

''',
},
]
