#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import json

def simple_item(name, min_unpleasantness, max_unpleasantness, min_pleasantness, max_pleasantness, min_time, max_time, description, extra = {}):
  result = extra.copy()
  result.update ({
    "name": name,
    "min_unpleasantness": min_unpleasantness,
    "max_unpleasantness": max_unpleasantness,
    "min_pleasantness": min_pleasantness,
    "max_pleasantness": max_pleasantness,
    "min_time": min_time,
    "max_time": max_time,
    "description": description,
  })
  return result

def brief_item(name, min_time, max_time, description, extra = {}):
  result = extra.copy()
  result.update ({
    "name": name,
    "min_time": min_time,
    "max_time": max_time,
    "description": description,
  })
  return result

immediate = 1
several_minutes = 3
half_hour = 4
hours = 5
all_afternoon = 6
multiple_days = 7
indefinitely = 7

stimulation_list = [
  simple_item ("push me around", 0, 1, 0, 2, immediate, half_hour, "TODO description", {"no_self": True}),
  simple_item ("pin me down", 0, 1, 0, 3, immediate, half_hour, "TODO description", {"no_self": True}),
  simple_item ("grab me by the hair", 1, 3, 0, 2, immediate, several_minutes, "A great combination of the slight pain of pulling my hair with physical control over the position of my head. Just be careful not to bend my neck in a weird direction."),
  simple_item ("slap me in the face", 1, 4, 0, 0, immediate, several_minutes, "TODO description"),
  simple_item ("put your hand threateningly on my throat and/or balls", 0, 1, 2, 4, immediate, immediate + 1, "I don't do actual choking because of the risks, but the threat is exciting.", {"no_self": True, "variants": [
    simple_item ("put your hand threateningly on my "+noun, 0, 1, 2, 4, immediate, immediate + 1, "", {"no_self": True})
    for noun in ["throat","balls"]
  ]}),
  simple_item ("pull off my clothes", 0, 2, 1, 4, several_minutes, several_minutes, "This kind of requires my participation, but only a little.", {"weight":3, "no_self": True}), # no_self because there's already a participation version
  simple_item ("tickle me", 2, 5, 0, 3, immediate, hours, "TODO description", {"weight":2, "no_self": True}),
  simple_item ("stroke/lick/suck my neck, nipples, undersides of arms, sides, face, inner thighs", 0, 2, 1, 6, immediate, hours, "TODO description", {"variants":[
    simple_item (verb+" "+noun, 0, 2, 1, 6, immediate, hours, "", {"weight":weight, "no_self": verb != "stroke"})
      for (verb, weight) in [("stroke", 2), ("lick", 1), ("suck", 1)]
      for noun in ["my neck","my nipples","the undersides of my arms","my sides","my face","my inner thighs"]
      if (verb != "suck") or (noun not in ["my sides","my face","my inner thighs"])
  ]}),
  simple_item ("squeeze my breasts", 0, 2, 1, 4, immediate, half_hour, "TODO description"),
  simple_item ("pinch/twist my nipples", 1, 6, 0, 3, immediate, half_hour, "TODO description", {"weight":2}),
  simple_item ("slap/whip me in the chest, nipples, stomach, inner thighs", 1, 7, 0, 2, immediate, half_hour, "The best thing is to slap/whip me on all different parts of my body. If you whip the same spot repeatedly, the pain gets more intense, but stops being sexy.", {"variants":[
    simple_item (verb+" me in the "+noun, 1 + intensity, 5 + intensity, 0, 2, time, half_hour, "")
    for (verb, time, intensity) in [("slap", immediate, 0), ("whip", immediate + 1, 2)] for noun in ["chest","nipples","chest and stomach","inner thighs"]
  ]}),
  simple_item ("spray me with water", 0, 3, 1, 5, hours, hours, "TODO description"),
  simple_item ("dunk me in water", 1, 2, 1, 4, hours, half_hour, "TODO description"),
  simple_item ("hit me in the balls", 2, 7, 1, 3, immediate, immediate + 1, '''Some people worry that the sudden pain of ball-kicking can risk causing a heart attack. I normally avoid risk, but in this case, I think that I get a lot less pain than most people with testicles do. Maybe mine are desensitized because I've hit them for fun so many times, or maybe they've just always been less sensitive. When I was a little kid, I got hit there once during a soccer game, and my reaction was like "This pain is kind of weird, but why is everyone acting so empathetic? It's not THAT bad."<br><br>The real caveat is that if my balls get hit a lot of times, they'll be achy for the next few days, which is inconvenient. Hitting them <em>hard</em> is good if you do it once or a few times, but hitting them <em>repeatedly</em> is a bigger commitment.<br><br>Since I've done this to myself a lot of times, I've noticed some interesting things about its effects. One is that getting hit in the balls makes me slightly more aroused for a while, on a mostly physical level – it's separate from the mental arousal I get from feeling vulnerable. Another thing is that hitting myself in the balls can help clear gas pressure from my digestive system. My reaction must make me tense some combination of muscles that I don't have conscious control over.''', {"variants":[
    simple_item (verb+" me in the balls", 2, 7, 1, 3, immediate, immediate + 1, "", {"weight":0.6})
    for verb in ["punch","punch","kick"]
  ]}),
  simple_item ("scratch me", 2, 5, 2, 3, immediate, several_minutes, "I didn't think of this myself. A play partner asked to try scratching me, and I didn't expect much from it, but it turned out to be a much bigger sensation than I expected. Kind of like tickling, but more aggressive. Scratching me repeatedly gets annoying, but an occasional long scratch really emphasizes that you have the power to inflict sensations on me, which is exciting.", {"weight":0.5}),
  simple_item ("scratch the soles of my feet", 4, 7, 0, 1, several_minutes, several_minutes, "Like tickling, this doesn't cause <em>pain</em> per se. It does cause an overwhelming sensation that my mind has trouble dealing with.", {"weight":0.5}),
  simple_item ("force me to orgasm", 0, 2, 3, 7, hours, several_minutes, '''Being forced to orgasm is a huge fantasy for me. The trouble is that generally, after I <em>actually</em> orgasm, I completely lose interest in sexual things. I don't even get the "post-orgasm glow" or satisfied feeling that a lot of people say they get. I <em>sometimes</em> stay interested, but I don't know exactly what determines it. With the right play partner, I might be interested in experimenting with this. Currently, I generally avoid orgasming when actually playing with people.''', {"caveat": True}),
  simple_item ("talk to me intimidatingly", 0, 2, 0, 4, immediate, several_minutes, "I feel like most of the time I'd just laugh at it, but if you said exactly the right thing and I was in exactly the right mood, it could be exciting.", {"no_self": True, "unsure": True}),
  simple_item ("electrostim", 1, 7, 0, 1, immediate + 1, half_hour, "The idea of being tortured with electricity turns me on a lot. In practice, I'd have to find someone who was enough of an expert to make sure it was safe. It's not my biggest desire, so I haven't gone out looking, but if I run into someone with the knowledge, I'd be eager to try it.", {"unsure": True, "no_generate": True}),
]

participation_list = [
  simple_item ("strip naked", 0, 1, 0, 3, several_minutes, several_minutes, "TODO description", {"weight":2}),
  simple_item ("do exercises (e.g. squats, situps, jumping jacks)", 1, 5, 0, 2, several_minutes, hours, "TODO description"),
  simple_item ("get in a cold shower", 3, 5, 0, 0, hours, half_hour, "TODO description"),
  simple_item ("get in a shower with my clothes still on", 1, 2, 0, 2, hours, half_hour, "TODO description"),
  simple_item ("sleep naked overnight", 0, 0, 0, 2, multiple_days, multiple_days, "TODO description"),
  simple_item ("sleep naked and exposed, with no blankets", 1, 2, 0, 2, multiple_days, multiple_days, "TODO description"),
  simple_item ("do [anything from the stimulation list] to myself", 0, 7, 0, 7, immediate, indefinitely, "TODO description", {"no_generate": True}),
  simple_item ("put myself in [anything from the conditions list]", 0, 7, 0, 7, immediate, indefinitely, "TODO description", {"no_generate": True}),
]

conditions_list = [
  simple_item ("I'm tied up", 0, 3, 0, 3, half_hour, all_afternoon, "When I was a little kid, I liked to tie myself up naked or nearly naked. At the time, I didn't understand that it was a sexual thing, but now I do. I would sometimes imagine that I been tied up naked and left on a pirate ship. (I didn't really care about pirates, it was just the excuse for why people would tie me up.)<br><br>It's a little disappointing that I never got to play tie-up games with other children. At the time, I was never willing to show vulnerability to other kids – perhaps as a reaction to the coercive environment I was always in at school. But now that I'm out of that environment, I've been able to start experimenting with showing vulnerability.<br><br>Being tied up is one of my biggest turn-ons. It lets me feel vulnerable and helpless, and it also lets me exert my muscles by struggling against the bonds. When I twist and struggle, but still can't stop what's happening, that's an amazing feeling.", {"inflict": "tie me up", "enhance": True}),
  simple_item ("I'm blindfolded", 0, 2, 0, 1, immediate + 1, hours, "Being blindfolded heightens my other sensations, and lets me be pleasantly nervous about not knowing where you're going to touch me next.", {"inflict": "blindfold me", "enhance": True}),
  simple_item ("I'm gagged", 0, 2, 0, 2, half_hour, half_hour, "Honestly, gags aren't very believable. They can't actually stop you from yelling – or even talking understandably – unless they dangerously block your airways. But it's still exciting to have one pushed into my mouth, because it's an intimate space that I wouldn't normally let such things into.", {"inflict": "gag me"}),
  simple_item ("I'm kneeling", 0, 2, 0, 0, immediate, hours, "Aside from the symbolic meaning of kneeling, I'm also a fairly tall person. Kneeling forces me to me look up at my partners instead of down, which makes them feel bigger and more dangerous.", {"assume": "kneel", "enhance": True}),
  simple_item ("I'm forced to remain naked/partially naked", 0, 1, 0, 3, half_hour, multiple_days, """In reality, I don't have any discomfort about being naked around other people. But if I <em>pretend</em> that I do, then have nudity "forced" on me, it can become a great vulnerability thing. It's not the fact of <em>being</em> naked that's exciting, it's the idea that you can keep me that way whether I want you to or not.<br><br>Interestingly, wearing just my underpants doesn't feel the most vulnerable. I think it has to do with the point of reference. If I'm topless, it feels like "I have clothes on <em>except that my chest and underarms are exposed</em>." If I'm wearing underpants and a <em>shirt</em>, it feels like "I have clothes on <em>except that my thighs are exposed</em>." But with just underpants, it feels like "I'm naked <em>except that my crotch is covered</em>." """, {"variants": [
    simple_item ("I'm forced to remain "+state, 0, 1, 0, 3, half_hour, multiple_days, "", {"maintain": "remain "+state, "long_term": True})
    for state in ["naked", "topless", "wearing only a shirt", "wearing only a shirt and underpants"]
  ]}),
  simple_item ("I'm forced to remain naked when it's cold", 1, 3, 0, 3, half_hour, hours, "TODO description", {}),
  simple_item ("I have clothespins on my nipples", 0, 5, 0, 3, immediate + 1, half_hour, """Interestingly, depending on the exact angle, clothespins can cause anything from "no pain at all" to "lots of pain". If you want, you can order me to adjust them to whatever level of pain you specify.""", {"inflict": "put clothespins on my nipples"}),
  simple_item ("I'm wearing a collar", 0, 1, 0, 2, several_minutes, hours, "Collars aren't as exciting for me as they are for people who do power dynamics, but the slight pressure on my neck still makes me feel nice and vulnerable.", {"inflict": "put a collar on me"}),
  simple_item ("I'm forced to stand in a stress position, like with my legs bent and/or my arms over my head", 2, 5, 0, 4, immediate + 1, half_hour, "Having my muscles straining makes all pleasure sensations much more intense. It's one of the same reasons that I enjoy struggling in bondage.", {"maintain": "stand in a stress position", "enhance": True}),
  simple_item ("I'm in a predicament bondage position", 4, 7, 0, 4, half_hour, half_hour, "TODO description", {"inflict": "put me in predicament bondage", "enhance": True}),
  simple_item ("I'm forced to stay perfectly still", 0, 1, 0, 1, immediate, half_hour, """I'm really good at suppressing my own reactions, but it does take a mental effort. There's a lot of facets to this kind of restraint. First, I can't protect myself against your touch because of my own suppression. Second, when you do touch me, it not only forces the sensation on me, but also forces the internal mental effort. And finally, there's the fear of however you might "punish" me if I mess up and move.""", {"maintain": "stay perfectly still", "enhance": True, "possible_tied": True}),
  simple_item ("I'm forced to keep my eyes closed", 2, 3, 0, 3, immediate, half_hour, '''I don't normally trust people enough to close my eyes in front of them. If someone says "close your eyes", I just don't do it. In a BDSM context, it can make me nervous in a good way. It's like being blindfolded, but with the extra bonus that I feel threatened by the idea that I could be making a mistake by trusting the other person. (Literally speaking, I'm trusting them just as much if I let them blindfold me, but it feels different. It feels more like I have the option to open my eyes at any time, so the "mistake" is prolonged.)''', {"maintain": "keep my eyes closed", "enhance": True, "possible_tied": True}),
  simple_item ("I'm forced to look you in the eye", 0, 3, 0, 2, immediate, half_hour, "Eye contact can be slightly uncomfortable for me, as it is for many autistic people. In the right context, that discomfort can be used for fun. Also, it stops me from looking at what you're doing, which is exciting for the same reason as a blindfold.", {"maintain": "look you in the eye", "enhance": True, "possible_tied": True}),
  simple_item ("one or more other people are watching/participating", 0, 0, 0, 2, several_minutes, indefinitely, "Naturally, I would have to trust everyone involved. But I'd love to have people ganging up on me.", {"caveat": True, "no_generate": True}),
]

scene_list = [
  brief_item ("we play a game and the winner tops the loser", hours, multiple_days, "Losing at games is one of my biggest turn-ons. If there's a set punishment for losing, then every time it starts to look like I'm losing the game, I get to feel a rush of vulnerability as I anticipate the punishment. And then another rush after the final move when I've actually lost.", {}),
  brief_item ('we play a strip game, except with BDSM "punishments" instead of just stripping', hours, all_afternoon, "Perhaps using the random generator at the bottom of this post to pick the punishment after each round!", {}),
  brief_item ("we wrestle and the winner tops the loser", several_minutes, hours, 'Another thing I sometimes did as a kid was to "wrestle" with a heavy blanket and imagine that it had pinned me down on the bed.', {}),
  brief_item ("you violently overpower me, then use that to force other stimulation on me", several_minutes, hours, "TODO description", {}),
  brief_item ('you start pleasuring me, then when I relax into it, you "take advantage" by doing other things to me', several_minutes, hours, "TODO description", {}),
  brief_item ("you order me to do various things to myself while you sit back and enjoy the show", immediate, hours, "This is something we could even do remotely, like over video chat.", {}),
  brief_item ("while we're hanging out for a while, you casually keep me in a state of [anything from the conditions list] and/or casually do things to me from time to time", half_hour, multiple_days, "This could be especially nice if I had a play partner I lived with. It would keep me in an ongoing state of slight vulnerability, even if we were both busy with other things and didn't want to do a full scene.", {}),
  brief_item ("you dare me to do a difficult challenge, then top me if I refuse or fail at it", several_minutes, all_afternoon, '''When people dared me to do things as a kid, I rarely did them, since I felt like "why would I do that just because you dared me to?" The idea of letting someone give me dares that I might <em>not</em> be able to refuse is an exciting kind of vulnerability. (Of course, in reality, I'd be able to refuse the dares if I wanted. But I can pretend, just like for all the other things.)''', {}),
  brief_item ('''you force me to exercise until I'm exhausted, then use that to "take advantage" of me''', all_afternoon, multiple_days, "I love the helplessness of being too tired to fight back. However, there might be some safety concerns about overdoing the exercise.", {"caveat": True}),
]

bondage_list = [
  brief_item ("tied spreadeagled on the bed", half_hour, hours, "", {}),
  brief_item ("tied to a chair, with my legs apart", half_hour, hours, '''Sometimes I tie my legs to my computer chair and imagine someone's forcing me to play computer games, with additional "punishments" when I lose at them.''', {}),
  brief_item ("hands tied behind my back", half_hour, half_hour, "", {}),
  brief_item ("hands tied together above my head", half_hour, half_hour, "This one's nice because it also makes my underarms very exposed.", {}),
  brief_item ("legs tied together at both the ankles and the knees", half_hour, hours, "Whenever I'm tied up, I get an extra surge of vulnerability whenever one of my automatic movements is blocked. Tying my legs at the knees blocks a <em>lot</em> of automatic movements that I don't even think about normally.", {}),
  brief_item ("big toes tied together", half_hour, hours, "Like with the knees, tying my toes blocks a lot of movements that I don't <em>expect</em> to be blocked.", {}),
  brief_item ("ankles and toes tied to a bed frame above, with my body face-down", half_hour, hours, "Having my feet exposed and tortured isn't my <em>main</em> kink, but this position is great for it. It makes me feel so helpless. Not only am I unable to stop you, but it's hard for me to even see what you're doing.", {}),
  brief_item ("hands and/or ankles tied together loosely, so I can still walk but it's awkward", half_hour, all_afternoon, "This one is good if you want to keep me tied up for a while without getting uncomfortable, or if you want to force me to move around while partially tied up.", {"long_term": True}),
  brief_item ("ankles each tied to the same thigh", half_hour, hours, "Note: We can't do the same thing with my arms, because I need to be careful about ulnar nerve problems from folding up the elbows.", {}),
  brief_item ("tied thoroughly to a rigid object (bed frame? pole?) so that I'm as immobile as possible", half_hour, half_hour, "", {}),
  brief_item ("ankles tied to my waist so that I can't stand up all the way", half_hour, all_afternoon, "This could be part of a stress position. Or you could force me to walk around while I'm tied like this.", {"long_term": True}),
  brief_item ("nipple-clothespins tied to an overhead hook, so I have to stand on my tiptoes", half_hour, half_hour, "", {}),
  brief_item ("nipple-clothespins tied to an overhead hook to wrists/thumbs/ankles/toes, so I have to keep holding up my arms/legs", half_hour, half_hour, "", {}),
]

circumstances_list = [
'''you jump me in retaliation for saying something smug
you ambush me by surprise?
you ambush me while I'm still asleep? (is it possible to tie me to the bed without waking me up?)
I stake "you can top me as much as you want for the next X days" on one of the above
foreshadow topping

online

while I'm doing a game/challenge, you keep teasing me/feeling me up/reminding me of what you'll do to me once I lose
being unfair

find list for squeeze balls/beat up/knife'''
]

lists = [
  {"name": "Stimulation list", "id": "stimulation", "description": "Things you can do to me even if I don't actively cooperate", "list": stimulation_list},
  {"name": "Participation list", "id": "participation", "description": "Things you can force me to do, that require my cooperation", "list": participation_list},
  {"name": "Conditions list", "id": "conditions", "description": "Things that can be ongoing while you do other stuff to me", "list": conditions_list},
  {"name": "Scene list", "id": "scene", "description": "Overall progressions of things we can do together", "list": scene_list},
  {"name": "Bondage list", "id": "bondage", "description": "A few of the infinite ways I like to be tied up", "list": bondage_list},
]

def render_item(simple, item, list):
  name = item["name"] + ("*" if "caveat" in item else "") + ("?" if "unsure" in item else "")
  if simple:
    return "<li>" + name + "</li>"
  return ("<tr>" + 
    "<td>" + name + "</td>" +
    ("<td>" + str (item ["min_unpleasantness"]) + "-" + str (item ["max_unpleasantness"])  + "</td>" +
    "<td>" + str (item ["min_pleasantness"]) + "-" + str (item ["max_pleasantness"])  + "</td>" +
    "<td>" if "min_unpleasantness" in item else '<td>') +
    str (item ["min_time"]) + "-"+ str (item ["max_time"]) + "</td>" +
    "<td>" + item ["description"] + "</td>" +
  "</tr>")
  

def render_list(simple, list):
  header = "<h3>" + list ["name"] + '</h3> <p class="subtitle">' + list["description"] + "</p>"
  items ="".join([render_item (simple, item, list) for item in list["list"]])
  if simple:
    return header + "<ul>" + items + "</ul>"
  return header + "<table><tr><th></th>"+ ("<th> Unpl. </th><th> Plea. </th>" if "min_unpleasantness" in list ["list"] [0] else "")+"<th> Time </th><th> Notes </th></tr>" + items + "</table>"

def render(simple):
  return "".join([render_list (simple, list) for list in lists])


contents = '''

<p>(Content: Details of sexual stuff, including BDSM things that would normally be violent.)</p>

This post describes the things I enjoy doing sexually. I have a lot of different purposes in writing it:
<ul class="big_list">
<li>For me and my play partners to use as a reference, to find ideas for things to do together.</li>
<li>To help normalize these desires. Now, I am hardly a normal person, so just listing them doesn't prove they're "normal". But trust me, none of them are especially rare. I also want to make sure everyone knows it's possible to do these things in a consensual environment. If you also want these things, but you're only getting them from a coercive relationship, trust me: better things are possible.</li>
<li>For people to enjoy reading, either because it sexually excites them or because it just satisfies their curiosity.</li>
</ul>

You may share this. I'm not keeping it secret from anyone.

<h2><em>Who</em> I would do these things with</h2>

Anyone who wants to do them with me, as long as I know them and trust that they wouldn't harm me or <em>be</em> harmed.

A note about "be harmed": Many people form emotional attachments when they do sexual things. My brain works differently. It doesn't form emotional attachments to people, in any situation. Not everyone likes being attached to someone who isn't attached back. Asymmetric attachments aren't always bad, but it they have some risks, which I need to consider before I do stuff.

<h2>Terminology</h2>

Most of the things I like involve having something "forced" on me by another person. In real life, I and another person would mutually agree to play out the "forcing". In that context, the one <em>doing</em> the thing is called the <strong>top</strong>, and the one <em>having the thing done to them</em> is called the <strong>bottom</strong>. "<strong>Topping</strong>" is also the verb for doing this.

You may have seen the similar terms "dom" and "sub". These are subtly different – they refer to some sort of human authority structures. For me, on a gut level, human authority structures are just meaningless. So I use different terms.

This is mostly a list of ways I like other people topping me. I also enjoy topping other people. However, I'm not listing those for a couple reasons. First, when I top someone, what I enjoy is much more dependent on what the other person likes. (I think I get a lot of my enjoyment out of internally mirroring their reactions.) Second, if I did have to pick my own preferences, it would basically be the same list, just in reverse.

Lastly, instead of saying "the top" or "the person I'm playing with" in this list, I'm going to say "you", because it's easier to read and doesn't sound as dry and formal. 


<h2>The list</h2>

'''+ render (True) +'''

<h2>Detailed descriptions</h2>

I've rated the "unpleasantness" of each thing using <a href="/blog/my-0-10-pain-scale">my 0-10 pain scale</a>. I say "unpleasantness" instead of "pain", because the important thing is that I get overwhelmed with sensation, not exactly what kind of sensation it is. For instance, tickling can be overwhelming, but isn't literal pain. Higher unpleasantness can be either good or bad, depending on my mood at the time. Generally, the more tired I am, the more I want to avoid unpleasantness. The more energetic I am, the more I seek out unpleasantness on purpose.

I've also listed "pleasantness" for sensations that can become intense, but are still fine when I'm tired. It uses the same scale. "Time" is on a more arbitrary 1-7 scale. The minimum time listed for each thing is the minimum time <em>commitment</em> – for instance, including any setup or cleanup time. The maximum is the longest I could generally continue to enjoy doing it. That's why the minimum is greater than the maximum for some of them.

'''+ render (False) +'''

<h2>Activity generator</h2>
<p class="noscript">(There would also be a button here to randomly choose an activity from the lists, but it requires JavaScript.)</p>

<div id="kink_generator"></div>

'''

for list in lists:
  for item in list ["list"]:
    del item ["description"]

posts = [
{
  "title":"My kinks",
  "don't deploy": True,
  "auto_paragraphs": True,
  "contents": contents,
  "head": '''
  <style type="text/css">
th,td { padding: 0.3em 0; }
td { border-top: 1px solid black; }
ul,table { margin-top: 0.6em; margin-bottom: 0.9em; }
h3 { padding-top: 0.5em }
.subtitle {margin:0.3em 0;}
textarea {display: block; width: 100%; height: 10em;}
  </style>
  ''',
  "after_body": """<script type="text/javascript">

var stimulation = 0;
var participation = 1;
var conditions = 2;
var preprocessed_lists = """+json.dumps(lists)+r"""


function adjust (item, attrs) {
  return changed = Object.assign({}, item, attrs);
}
function rename (item, name) {
  return adjust (item, {name});
}

preprocessed_lists.forEach(function(list) {
  var varying = [];
  list.list = list.list.filter(function(item) {
    if (item.variants) {
      Array.prototype.push.apply (varying, item.variants);
      return false;
    }
    if (item.no_generate) {
      return false;
    }
    return true;
  });
  
  Array.prototype.push.apply (list.list, varying);
});
preprocessed_lists.forEach(function(list) {
  list.list.forEach(function(item) {
    item.max_sensation = Math.max (item.max_unpleasantness, item.max_pleasantness);
    if (item.inflict) {
      preprocessed_lists[stimulation].list.push (adjust (item, {name: item.inflict, original_list: list.name}));
    }
    if (item.assume) {
      preprocessed_lists[participation].list.push (adjust (item, {name: item.assume, original_list: list.name}));
    }
  });
});
Array.prototype.push.apply (preprocessed_lists[participation].list, preprocessed_lists[stimulation].list.filter (item => !item.no_self).map (item => {
  return adjust (item, {
    name: item.name.replace (/\bme\b/, "myself").replace (/\bmy\b/, "my own").replace (/\byour\b/, "my"),
    weight: (item.weight || 1) / (item.max_unpleasantness > 3 ? 3 : 1000),
  });
}));



function random_range (min, max) {
  return min + Math.floor (Math.random()*(max - min));
}
function random_choice (list) {
  var total = list.reduce (function (total, item) {return total + (item.weight || 1);}, 0);
  var choice = Math.random ()*total;
  return list.find (function (item) {choice -= (item.weight || 1); return choice < 0.00000001});
  //return list [random_range (0, list.length)];
}
function choose (list) {
  var item = random_choice (list);
  return item && item.name
}


function inflict (lists) {
  return choose (lists[stimulation]);
}
function participate (lists) {
  return choose (lists[participation]);
}
function condition (lists) {
  return choose (lists[conditions]);
}
function maintain_condition (lists, need_enhance) {
  return choose (lists[conditions].filter (item => item.maintain && (item.enhance || !need_enhance)).map (item => rename (item, item.maintain)));
}
/*function while_enhanced (lists) {
  var item = random_choice (lists[conditions].filter (item => item.enhance && !item.maintain));
  if (item.inflict)
    return "agree to " + choose (lists [participation].filter (item => item.max_unpleasantness < 6));
  }
  return "let you " + choose (lists [stimulation].filter (item => item.max_unpleasantness < 6));
}*/
function surrender (lists) {
  if (Math.random() <0.5) {
    return "agree to " + participate (lists);
  }
  return "let you " + choose (lists [stimulation].filter (item => item.max_unpleasantness < 6));
}

function act (lists) {
  
}

function I_must_strip(lists) {
      return "I must remove a piece of clothing";
    }
function I_must_participate(lists) {
      return "I must " + participate (lists);
    }
function make_me_participate(lists) {
      return "make me " + participate (lists);
    }
    function maintain_while_inflict (lists) {
      return "make me " + maintain_condition(lists, true) + " while you " + choose (lists [stimulation].filter (item => item.max_sensation >= 4));
    }
    function inflict_until_surrender (lists) {
      return choose (lists [stimulation].filter (item => item.max_unpleasantness >= 6).concat ([{name: "squeeze my balls"}])) + " until I " + surrender(lists);
    }
    function threaten_unless_surrender (lists) {
      // since the threat needn't be carried out, we choose it from the unfiltered list
      return "threaten to "+choose (preprocessed_lists [stimulation].list.filter (item => item.max_unpleasantness >= 6).concat ([{name: "squeeze my balls"},{name: "(not actually) beat me up"},{name: "cut me with a (not actually sharp) knife"}])) + " unless I " + surrender(lists);
    }
    function while_condition_inflict (lists) {
      return "while " + choose (lists[conditions].filter (item => item.enhance && !item.maintain)) + ", " + inflict(lists);
    }
    function challenge_to_maintain (lists) {
      var inflict_first = choose (lists [stimulation].filter (item => item.max_unpleasantness >= 5 && !item.original_list));
      return "challenge me to " + maintain_condition(lists, true) + " while you " + inflict_first + ". If I can't keep it up, " + choose (lists [stimulation].filter (item => item.max_sensation >= 7 && item.name !== inflict_first));
    }
  
function global_generate (parameters, generators) {
  var filter = function (item) {
    return (
      item.min_unpleasantness <= parameters.max_unpleasantness &&
      item.min_time <= parameters.max_time &&
      (parameters.caveat_allowed || !item.caveat) &&
      (parameters.unsure_allowed || !item.unsure)
    )
  }
  var filtered_lists = preprocessed_lists.map (function (list) {return list.list.filter (function(item) {
    return filter(item) && (!parameters.filter || parameters.filter(item, list))
  });});

  //[].concat(
  //  stimulation_list.filter (filter),
  //);
  
  var result = "undefined";
  var attempts = 0;
  while (result.includes ("undefined")) {
    result = ""+random_choice (generators)(filtered_lists);
    if (++attempts > 1000) {return "Oops! Couldn't find any activities that meet your restrictions";}
  }
  return result;
}
function UI_generate(generators, parameters) {
  parameters = Object.assign({}, parameters);
  var max_time = Math.min($("#max_time").val(), parameters.max_time || 7);
  delete parameters.max_time;
  return global_generate(Object.assign({max_unpleasantness: $("#max_unpleasantness").val(), max_time, caveat_allowed: true}, parameters), generators);
}

/* Things to generate notes
punishment for losing one round of a game
punishment for losing big game
scene for an afternoon together
something to do remotely
something to do while I'm tied up
a way to tie me up
*/

function button (text, generators, parameters) {
  return $("<button>").css("display", "block").text ("Pick "+text).click (function() {
    var result = UI_generate(generators, parameters);
    for (var index = 1; index < $("#number").val();++index) {
      result += "\n"+UI_generate(generators, parameters);
    }
    display.text(result);
  });
}

display = $("<textarea>");
$("#kink_generator").append (
  
  
  "Generate ",
  $("<input>", {id: "number", type:"number", min: 1, max: 100, value: 7,}),
  "activities, with no more than",
  $("<input>", {id: "max_unpleasantness", type:"number", min: 0, max: 10, value: 10,}),
  "unpleasantness, which take no longer than",
  $("<input>", {id: "max_time", type:"number", min: 1, max: 7, value: 7,}),
  "time",
  
  button("something to do to me while I'm tied up", 
    [inflict, inflict, inflict, inflict, inflict, inflict, maintain_while_inflict, inflict_until_surrender, threaten_unless_surrender, challenge_to_maintain],
    {filter: function (item, list) {
      return list.id === "stimulation" || item.possible_tied
    }}
  ),
  button("a punishment for losing one round of a game", 
    [I_must_strip, inflict, inflict, I_must_participate, I_must_participate, maintain_while_inflict ],
    { max_time: 3, }
  ),
  
  display
);

</script>"""
},
]

