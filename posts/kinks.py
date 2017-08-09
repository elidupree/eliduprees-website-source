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
  
def simplest_item(name, description, extra = {}):
  result = extra.copy()
  result.update ({
    "name": name,
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
  simple_item ("push me around", 0, 1, 0, 2, immediate, half_hour, "", {"no_self": True, "not_when_tied": True}),
  simple_item ("pin me down with your body", 0, 1, 0, 3, immediate, half_hour, "", {"no_self": True}),
  simple_item ("grab me by the hair", 1, 3, 0, 2, immediate, several_minutes, "A great combination of the slight pain of pulling my hair with physical control over the position of my head. Just be careful not to bend my neck in a weird direction."),
  simple_item ("slap me in the face", 1, 4, 0, 0, immediate, several_minutes, ""),
  simple_item ("put your hand threateningly on my throat and/or balls", 0, 1, 2, 3, immediate, immediate + 1, "I don't do actual choking because of the risks, but the threat is exciting.", {"no_self": True, "variants": [
    simple_item ("put your hand threateningly on my "+noun, 0, 1, 2, 4, immediate, immediate + 1, "", {"no_self": True, "weight":0.5})
    for noun in ["throat","balls"]
  ]}),
  simple_item ("pull off my clothes", 0, 2, 1, 4, several_minutes, several_minutes, "This kind of requires my participation, but only a little.", {"weight":3, "no_self": True}), # no_self because there's already a participation version
  simple_item ("tickle me", 2, 5, 0, 3, immediate, hours, "My ticklishness depends a lot on my mental state. Sometimes, I can laugh and thrash around for a long time. Other times, I don't react and it doesn't feel like much sensation at all. I have a lot of control over it – I can usually suppress my reactions and stop feeling the tickling. On the other hand, it's much harder to <em>become</em> ticklish when I didn't start that way. In practice, since I enjoy tickling, I have to use a bit of mental control to <em>maintain</em> my ticklishness while I'm being tickled. I sometimes deliberately squirm around even if the tickling didn't force me to, because squirming helps me stay ticklish.", {"weight":2, "no_self": True}),
  simple_item ("stroke/lick/suck my neck, nipples, undersides of arms, sides, face, inner thighs", 0, 2, 1, 6, immediate, hours, "Those are the body parts when I'm generally sensitive in a sexy way.<br><br>Interestingly, I don't find <em>butts</em> or <em>backs</em> sexy at all (either mine or others'). I think it's because my main turn-on is vulnerability, and if you curl up in a ball to protect yourself, your butt and back are exactly the things that <em>are</em> exposed. On the other hand, the throat, underarms, and inner thighs are normally well-protected.", {"variants":[
    simple_item (verb+" "+noun, 0, 2, 1, 6, immediate, hours, "", {"weight":weight, "no_self": verb != "stroke"})
      for (verb, weight) in [("stroke", 2), ("lick", 1), ("suck", 1)]
      for noun in ["my neck","my nipples","the undersides of my arms","my sides","my face","my inner thighs"]
      if (verb != "suck") or (noun not in ["my sides","my face","my inner thighs"])
  ]}),
  simple_item ("squeeze my breasts", 0, 2, 1, 4, immediate, half_hour, '''My chest is typical of a "male" person, so my breasts are small and you need to grip at the right angle to be able to squeeze them. But having my breasts groped is both a pleasant sensation and a nice vulnerability thing.<br><br>Since I'm agender, I generally avoid gender-coded language to refer to my own body parts. "Breasts" and "chest" are both technically gender-neutral, but usually have gender implications. I'm stuck with them, though, so I'll use whichever one seems more fitting in each situation. Here, the area between my breasts is specifically irrelevant to what turns me on, so "breasts" fits best.'''),
  simple_item ("pinch/twist my nipples", 1, 6, 0, 3, immediate, half_hour, "", {"weight":2}),
  simple_item ("slap/whip me in the chest, nipples, stomach, inner thighs", 1, 7, 0, 2, immediate, half_hour, "The best thing is to slap/whip me on all different parts of my body. If you whip the same spot repeatedly, the pain gets more intense, but stops being sexy.", {"variants":[
    simple_item (verb+" me in the "+noun, 1 + intensity, 5 + intensity, 0, 2, time, half_hour, "")
    for (verb, time, intensity) in [("slap", immediate, 0), ("whip", immediate + 1, 2)] for noun in ["chest","nipples","chest and stomach","inner thighs"]
  ]}),
  simple_item ("hit me in the balls", 2, 7, 1, 3, immediate, immediate + 1, '''A good hit in the balls can give me a lingering ache that leaves me feeling aroused and vulnerable.<br><br>Some people worry that the sudden pain of ball-kicking can risk causing a heart attack. I normally avoid risk, but in this case, I think that I get a lot less pain than most people with testicles do. Maybe mine are desensitized because I've hit them for fun so many times, or maybe they've just always been less sensitive. When I was a little kid, I got hit there once during a soccer game, and my reaction was like "This pain is kind of weird, but why is everyone acting so empathetic? It's not THAT bad."<br><br>The real caveat is that if my balls get hit a lot of times, they'll be achy for the next few days, which is inconvenient. Hitting them <em>hard</em> is good if you do it once or a few times, but hitting them <em>repeatedly</em> is a bigger commitment.<br><br>Since I've done this to myself a lot of times, I've noticed some interesting things about its effects. One is that getting hit in the balls makes me slightly more aroused for a while, on a mostly physical level – it's separate from the mental arousal I get from feeling vulnerable. Another thing is that hitting myself in the balls can help clear gas pressure from my digestive system. My reaction must make me tense some combination of muscles that I don't have conscious control over.''', {"variants":[
    simple_item (verb+" me in the balls", 2, 7, 1, 3, immediate, immediate + 1, "", {"weight":0.6})
    for verb in ["punch","punch","kick"]
  ]}),
  simple_item ("spray me with water", 0, 3, 1, 5, hours, hours, '''When I was growing up (see the notes on "I'm tied up" below), I always <em>wanted</em> squirt-gun fights to be exciting, but I just couldn't feel like "oh no, I've been hit!" from such a small amount of water. Maybe if you made me run laps while you threw water balloons at me… although that might be impractical because of my sun sensitivity. More practically, you can spray me indoors over a bathtub.''', {"not_when_tied": True}),
  simple_item ("dunk me in water", 1, 2, 1, 4, hours, half_hour, '''Water is kind of interesting for me. If most of my body is submerged in water, the pressure from the water is kind of arousing. And dunking my head underwater makes me feel nice and vulnerable. On the other hand, water makes my skin slippery, which makes it less sensitive to touch. One of my favorite variations is for you to dunk just my <em>head</em> in water, like over the side of a bathtub, while leaving the rest of me dry and exposed.''', {"not_when_tied": True}),
  simple_item ("scratch me", 2, 5, 2, 3, immediate, several_minutes, "I didn't think of this myself. A play partner asked to try scratching me, and I didn't expect much from it, but it turned out to be a much bigger sensation than I expected. Kind of like tickling, but more aggressive. Scratching me repeatedly gets annoying, but an occasional long scratch really emphasizes that you have the power to inflict sensations on me, which is exciting.", {"weight":0.5}),
  simple_item ("scratch the soles of my feet", 4, 7, 0, 1, several_minutes, several_minutes, "Like tickling, this doesn't cause <em>pain</em> per se. It does cause an overwhelming sensation that my mind has trouble adapting to.", {"weight":0.5}),
  simple_item ("push me down naked in the snow", 3, 4, 2, 4, hours, several_minutes, "", {"no_generate": True}),
  simple_item ("force me to orgasm", 0, 2, 3, 7, hours, several_minutes, '''Being forced to orgasm is a huge fantasy for me. The trouble is that generally, after I <em>actually</em> orgasm, I completely lose interest in sexual things. I don't even get the "post-orgasm glow" or satisfied feeling that a lot of people say they get. I <em>sometimes</em> stay interested, but I don't know exactly what determines it. With the right play partner, I might be interested in experimenting with this. Currently, I generally avoid orgasming when actually playing with people.''', {"caveat": True}),
  simple_item ("talk to me intimidatingly", 0, 2, 0, 4, immediate, several_minutes, "I feel like most of the time I'd just laugh at it, but if you said exactly the right thing and I was in exactly the right mood, it could be exciting.", {"no_self": True, "unsure": True}),
  simple_item ("electrostim", 1, 7, 0, 1, immediate + 1, half_hour, "The idea of being tortured with electricity turns me on a lot. In practice, I'd have to find someone who was enough of an expert to make sure it was safe. It's not my biggest desire, so I haven't gone out looking, but if I run into someone with the knowledge, I'd be eager to try it.", {"unsure": True, "no_generate": True}),
]

participation_list = [
  simple_item ("strip naked", 0, 1, 0, 3, several_minutes, several_minutes, "", {"weight":2}),
  simple_item ("do exercises (e.g. squats, sit-ups, jumping jacks)", 1, 5, 0, 2, several_minutes, hours, "I wish I could include push-ups in this list, but my hand problems currently rule them out.", {"variants":[
    simple_item ("do "+str(number)+" "+exercises, intensity, intensity, 0, 2, time, time, "", {"weight": 0.1})
    for (exercises, multiplier) in [("squats", 1), ("sit-ups", 1), ("jumping jacks", 2)]
    for (number, intensity, time) in [(20*multiplier, 2, 2), (30*multiplier, 3, 2), (40*multiplier, 4, 1+multiplier), (60*multiplier, 5, 1+multiplier)]
  ] #TODO: walking? Running? Bicycling?
  }),
  simple_item ("get in a cold shower", 3, 5, 0, 0, hours, half_hour, "The shock of the cold water puts my body into a more energetic state. After I get out of the cold shower, I generally feel energized, and my skin is more sensitive in a good way."),
  simple_item ("get in a shower with my clothes still on", 1, 2, 0, 2, hours, half_hour, "It can be fun to have someone force me to do things I'm reluctant to do. Of course, usually when I'm reluctant to do something, it's because it's actually a bad idea to do it. So I need to find things like this, where it's actually harmless, but pushing past the reluctance is still an exciting feeling."),
  simple_item ("sleep naked overnight", 0, 0, 0, 2, multiple_days, multiple_days, ""),
  simple_item ("sleep naked and exposed, with no blankets", 1, 2, 0, 2, multiple_days, multiple_days, ""),
  simple_item ("do [anything from the stimulation list] to myself", 0, 7, 0, 7, immediate, indefinitely, "", {"no_generate": True}),
  simple_item ("put myself in [any of the conditions from the conditions list]", 0, 7, 0, 7, immediate, indefinitely, "", {"no_generate": True}),
]

conditions_list = [
  simple_item ("I'm tied up", 0, 3, 0, 3, half_hour, all_afternoon, "When I was a little kid, I liked to tie myself up naked or nearly naked. At the time, I didn't understand that it was a sexual thing, but now I do. I would sometimes imagine that I'd been tied up naked and left on a pirate ship. (I didn't really care about pirates, it was just the excuse for why people would tie me up.)<br><br>It's a little disappointing that I never got to play tie-up games with other children. There are some ways it was <em>more</em> fun to enjoy being tied up the way I did as a child, without the <em>additional</em> sexual feelings I got as I grew older. But at the time, I was never willing to show vulnerability to other kids – perhaps as a reaction to the coercive environment I was always in at school. Now that I'm out of that environment, I've been able to start experimenting with showing vulnerability.<br><br>Being tied up is one of my biggest turn-ons. It lets me feel vulnerable and helpless, and it also lets me exert my muscles by struggling against the bonds. When I twist and struggle, but still can't stop what's happening, that's an amazing feeling.", {"inflict": "tie me up", "enhance": True}),
  simple_item ("I'm blindfolded", 0, 2, 0, 1, immediate + 1, hours, "Being blindfolded heightens my other sensations, and lets me be pleasantly nervous about not knowing where you're going to touch me next.", {"inflict": "blindfold me", "enhance": True, "possible_tied": True}),
  simple_item ("I'm gagged", 0, 2, 0, 2, half_hour, half_hour, "Honestly, gags aren't very believable. They can't actually stop you from yelling – or even talking understandably – unless they dangerously block your airways. But it's still exciting to have one pushed into my mouth, because it's an intimate space that I wouldn't normally let such things into.", {"inflict": "gag me", "possible_tied": True}),
  simple_item ("I'm kneeling", 0, 2, 0, 0, immediate, hours, "Aside from the symbolic meaning of kneeling, I'm also a fairly tall person. Kneeling forces me to me look up at my partners instead of down, which makes them feel bigger and more dangerous.", {"assume": "kneel", "enhance": True}),
  simple_item ("I'm forced to remain naked/partially naked", 0, 1, 0, 3, half_hour, multiple_days, """In reality, I don't have any discomfort about being naked around other people. But if I <em>pretend</em> that I do, then have nudity "forced" on me, it can become a great vulnerability thing. It's not the fact of <em>being</em> naked that's exciting, it's the idea that you are purposefully keeping me that way whether I want you to or not.<br><br>Interestingly, wearing just my underpants doesn't feel especially vulnerable. I think it has to do with the point of reference. If I'm topless, it feels like "I have clothes on <em>except that my chest and underarms are exposed</em>." If I'm wearing a shirt and underpants, it feels like "I have clothes on <em>except that my thighs are exposed</em>." But with just underpants, it feels like "I'm naked <em>except that my crotch is covered</em>."<br><br>There are other ways to play with clothing, too. <ul> <li>If you grope me while I'm still <em>wearing</em> clothes, it's exciting because "the clothing didn't protect me".</li> <li>If I'm wearing a crotch-guard or other protective gear, it's exciting because of the idea that I might <em>need</em> the protection.</li> <li>If you're the one who's (semi-)naked while <em>you're</em> topping <em>me</em>, then instead of being a "vulnerability" thing, it can become a "sexual aggressiveness" thing.</li></ul> """, {"variants": [
    simple_item ("I'm forced to remain "+state, 0, 1, 0, 3, half_hour, multiple_days, "", {"maintain": "remain "+state, "non_interfering": True})
    for state in ["naked", "topless", "wearing only a shirt", "wearing only a shirt and underpants"]
  ]}),
  simple_item ("I'm forced to remain naked when it's cold", 1, 3, 0, 3, half_hour, hours, "", {}),
  simple_item ("I have clothespins on my nipples", 0, 5, 0, 3, immediate + 1, half_hour, """Interestingly, depending on the exact angle, clothespins can cause anything from "no pain at all" to "lots of pain". If you want, you can order me to adjust them to whatever level of pain you specify.""", {"inflict": "put clothespins on my nipples", "non_interfering": True, "possible_tied": True}),
  simple_item ("I'm wearing a collar", 0, 1, 0, 2, several_minutes, hours, "Collars aren't as exciting for me as they are for people who do power dynamics, but the slight pressure on my neck still makes me feel nice and vulnerable.", {"inflict": "put a collar on me", "maintain": "wear a collar", "non_interfering": True, "possible_tied": True}),
  simple_item ("I'm forced to stand in a stress position, like with my legs bent and/or my arms over my head", 2, 5, 0, 4, immediate + 1, half_hour, "Having my muscles straining makes all pleasure sensations much more intense. It's one of the same reasons that I enjoy struggling in bondage.", {"maintain": "stand in a stress position", "enhance": True}),
  simple_item ("I'm in a predicament bondage position", 4, 7, 0, 4, half_hour, half_hour, '''Predicament bondage is when you're tied in a position where you have to choose between multiple uncomfortable options. For instance, you could put clothespins on my nipples and tie them to an overhead hook, so I have to either strain to stand on my tiptoes, or have my nipples pulled hard.<br><br>Predicament bondage combines a lot of different things I like. And while a <em>single</em> painful sensation tends to become too much and stop being sexy, predicament bondage naturally keeps each sensation at the "very intense, but not excessively intense" level.''', {"inflict": "put me in predicament bondage", "enhance": True}),
  simple_item ("I'm forced to stay perfectly still", 0, 1, 0, 1, immediate, half_hour, """I'm really good at suppressing my own reactions, but it does take a mental effort. There's a lot of different sides to this kind of restraint. First, I can't protect myself against your touch because of my own suppression. Second, when you do touch me, it not only forces the sensation on me, but also forces the internal mental effort. And finally, there's the fear of however you might "punish" me if I mess up and move.""", {"maintain": "stay perfectly still", "enhance": True, "possible_tied": True}),
  simple_item ("I'm forced to keep my eyes closed", 2, 3, 0, 3, immediate, half_hour, '''I don't normally trust people enough to close my eyes in front of them. If someone says "close your eyes", I just don't do it. In a BDSM context, it can make me nervous in a good way. It's like being blindfolded, but with the extra bonus that I feel threatened by the idea that I could be making a mistake by trusting the other person. (Literally speaking, I'm trusting them just as much if I let them blindfold me, but it feels different. It feels more like I have the option to open my eyes at any time, so the "mistake" is prolonged.)''', {"maintain": "keep my eyes closed", "enhance": True, "possible_tied": True}),
  simple_item ("I'm forced to look you in the eye", 0, 3, 0, 2, immediate, half_hour, "Eye contact can be slightly uncomfortable for me, as it is for many autistic people. In the right context, that discomfort can be used for fun. Also, it stops me from looking at what you're doing, which is exciting for the same reason as a blindfold.", {"maintain": "look you in the eye", "enhance": True, "possible_tied": True}),
  simple_item ("one or more other people are watching/participating", 0, 0, 0, 2, several_minutes, indefinitely, "Naturally, I would have to trust everyone involved. But I'd love to have people ganging up on me.", {"caveat": True, "no_generate": True}),
]

scene_list = [
  brief_item ("we play a game and the winner tops the loser", half_hour, multiple_days, "Losing at games is one of my biggest turn-ons. If there's a set punishment for losing, then every time it starts to look like I'm losing the game, I get to feel a rush of helplessness as I anticipate the punishment. And then another rush after the final move when I've actually lost.", {"possible_remotely": True}),
  brief_item ('we play a strip game, except with BDSM "punishments" instead of just stripping', half_hour, all_afternoon, "Perhaps using the random generator at the bottom of this post to pick the punishment after each round!", {"possible_remotely": True}),
  brief_item ('''we play <a href="/hexy">Hexy Bondage</a>''', hours, all_afternoon, "", {}),
  brief_item ("we wrestle and the winner tops the loser", several_minutes, hours, 'Another thing I sometimes did as a kid was to "wrestle" with a heavy blanket and imagine that it had pinned me down on the bed.', {}),
  brief_item ("you violently overpower me, then use that to force other stimulation on me", several_minutes, hours, '''All sensations become much more exciting when the idea is that they're being forced on me by violence.''', {}),
  brief_item ('you start pleasuring me, then when I relax into it, you "take advantage" by doing other things to me', several_minutes, hours, '''This is the kind of strange one for me, because there's no feeling of a threat that it would work on me in real life. (Unlike violence, which would obviously still hurt me.) Because of the way my mind works, I either trust someone or I don't – pleasure doesn't make me relax my boundaries at all. It's pretty interesting that I can still be aroused by doing a scene where I <em>pretend</em> that my mind works in a different way than it does.''', {}),
  brief_item ("you order me to do various things to myself while you sit back and enjoy the show", immediate, hours, "This is something we could even do remotely, like over video chat.", {"possible_remotely": True}),
  brief_item ("while we're hanging out for a while, you casually keep me in a state of [anything from the conditions list] and/or casually do things to me from time to time", half_hour, multiple_days, "This could be especially nice if I had a play partner I lived with. It would keep me in an ongoing state of slight vulnerability, even if we were both busy with other things and didn't want to do a full scene.", {"no_generate": True}),
  brief_item ("you dare me to do something difficult, then top me if I refuse or fail at it", several_minutes, all_afternoon, '''When people dared me to do things as a kid, I rarely did them, since I felt like "why would I do that just because you dared me to?" The idea of letting someone give me dares that I might <em>not</em> be able to refuse is an exciting kind of vulnerability. (Of course, in reality, I'd be able to refuse the dares if I wanted. But I can pretend, just like for all the other things.)''', {"possible_remotely": True}),
  brief_item ("we have a snowball fight", hours, hours, "", {"no_generate": True}),
  brief_item ('''you force me to exercise until I'm exhausted, then use that to "take advantage" of me''', all_afternoon, multiple_days, "I love the helplessness of being too tired to fight back. However, there might be some safety concerns about overdoing the exercise.", {"caveat": True}),
]

bondage_list = [
  brief_item ("tied spreadeagled on the bed", half_hour, hours, "", {}),
  brief_item ("tied to a chair, with my legs apart", half_hour, hours, '''Sometimes I tie my legs to my computer chair and imagine someone's forcing me to play computer games, with additional "punishments" when I lose at them.''', {}),
  brief_item ("hands tied behind my back", half_hour, half_hour, "", {}),
  brief_item ("hands tied together above my head", half_hour, half_hour, "This one's nice because it also makes my underarms very exposed.", {}),
  brief_item ("legs tied together at both the ankles and the knees", half_hour, hours, "Whenever I'm tied up, I get an extra surge of helplessness whenever one of my automatic movements is blocked. Tying my legs at the knees blocks a lot of automatic movements that I don't even think about normally.", {}),
  brief_item ("big toes tied together", half_hour, hours, "Like with the knees, tying my toes blocks a lot of movements that I don't <em>expect</em> to be blocked.", {}),
  brief_item ("ankles and toes tied to a bed frame above me, with my body face-down", half_hour, hours, "Having my feet exposed and tortured isn't my <em>main</em> kink, but this position is great for it. It makes me feel so helpless. Not only am I unable to stop you, but it's hard for me to even see what you're doing.", {}),
  brief_item ("hands and/or ankles tied together loosely, so I can still walk but it's awkward", half_hour, all_afternoon, "This one is good if you want to keep me tied up for a while without getting uncomfortable, or if you want to force me to move around while partially tied up.", {"non_interfering": True}),
  brief_item ("ankles each tied to the same thigh", half_hour, hours, "Note: We can't do the same thing with my arms, because I need to be careful about ulnar nerve problems from folding up the elbows.", {}),
  brief_item ("tied thoroughly to a rigid object (bed frame? pole?) so that I'm as immobile as possible", half_hour, half_hour, "", {}),
  brief_item ("ankles tied to my waist so that I can't stand up all the way", half_hour, all_afternoon, "This could be part of a stress position. Or you could force me to walk around while I'm tied like this.", {"non_interfering": True}),
  brief_item ("clothespins on my nipples tied to an overhead hook, so I have to stand on my tiptoes", half_hour, half_hour, "", {}),
  brief_item ("clothespins on my nipples tied over an overhead hook to my wrists/thumbs/ankles/toes, so I have to keep holding up my arms/legs", half_hour, half_hour, "", {"variants": [
    brief_item ("clothespins on my nipples tied over an overhead hook to my "+extremities+", so I have to keep holding up my "+limbs, half_hour, half_hour, "", {"weight":0.4})
    for (extremities, limbs) in [("wrists", "arms"), ("thumbs", "arms"), ("ankles", "legs"), ("toes", "legs")]
  ]}),
  brief_item ("buried in the snow", hours, half_hour, "", {"no_generate": True}),
]

impractical_list = [
  simplest_item ("being threatened with a knife", "I don't want to take the risk of using an <em>actual</em> knife, but threatening me with a butter knife and <em>pretending</em> it's sharp can be fun.", {"control": "threaten me with a (not actually sharp) knife to make me", "possible_tied": True}),
  simplest_item ("being beaten up for real", "", {"control": "(play-)threaten to beat me up unless I", "possible_tied": True}),
  simplest_item ("no-holds-barred fighting", "It turns me on SO much to imagine getting beaten in a no-holds-barred fight. I like to feel helpless, but usually, the helplessness is partly sabotaged by my knowledge that I'm not <em>actually</em> resisting as hard as I could be. But if I could somehow fight back with my full abilities and still get crushed…<br><br>Even if I don't lose, there's also the <em>body exhilaration</em> of fighting as hard as I can and disengaging my normal reluctance to injure others.<br><br>Anyway, I don't want anyone to die or get injured, so I can't actually do this. But it's still a persistent fantasy of mine.", {}),
  simplest_item ("penetrative sex, or other things with STI risk", "I don't want to do anything that risks transmitting STIs. Condoms can <em>reduce</em> the risk, but not remove it. Since this isn't a major part of my sexual interests, it's a logical decision for me not to take the risk. I don't even want much mouth-to-mouth contact – a forced kiss would turn me on, but I'm happy to sacrifice ever doing that in order to slightly reduce my risk of some diseases.", {}),
  simplest_item ("playing in the woods when it's warm", "We have a lot of mosquitoes. Also, in my area, tickborne diseases are a serious concern. It's not such a big risk that people should avoid the woods in <em>general</em>, but I'm a person who doesn't like the outdoors that much anyway.", {}),
  simplest_item ("getting topped by programmed robots", '''Like in my story, <a href="/stories/will-you-try-to-escape">Will You Try to Escape?</a>. Maybe if robots are much cheaper and easier to program in the future… Nah, it would probably still have too many safety concerns and not actually be worth the effort.''', {}),
  simplest_item ("literal magic", "There are so many sexy things you could do with magic. Shapeshifting… Mind control… Telekinesis… There are way too many for me to list them all.", {"control": "pretend to use magical mind control to make me", "possible_tied": True, "possible_remotely": True}),
]

miscellaneous_list = [
  simplest_item ("we agree that you can start topping me whenever you feel like it, without asking first", "I get a rush out of looking at someone and knowing that they <em>could</em> just jump me whenever they wanted.", {}),
  simplest_item ("you jump me in retaliation for saying something smug", '''I say a lot of smug things. I sometimes even make it into a game – how to say the thing that's <em>as smug as possible</em>. Then we can have a playful back-and-forth, either with more smug things or physical attacks. In a way, retaliating can actually be a form of appreciation, even if it's "violent". It's like the affectionately incredulous "I can't <em>believe</em> you actually said that".''', {}),
  simplest_item ("you interpret game rules unfairly against me", '''In my normal life, I like playing games, but I have a lot of boundaries about them. <ul> <li>I don't like playing games with ambiguous rules. This includes most physical games, because someone has to call what's "close enough".</li> <li>I always refuse to play games where the rules refer to things from real life, like the ages of the players.</li> <li>I don't even like playing games with real-life rewards, although I'm usually fine if I just pretend there's no reward.</li></ul> I feel like these things <em>violate the boundaries of a game</em>. They drag human social problems into my fun. The discomfort I get from them usually makes the game not worth playing. <br><br>In a BDSM context, playing with that discomfort on purpose can be fun. I can deliberately let myself get attached to the outcome, and then let myself feel unstable when I start to lose or when you change the rules out from under me. And I don't feel like my <em>real</em> boundaries have been violated, because the real boundary is drawn around the BDSM context as a whole.''', {}),
  simplest_item ("while I'm doing a game/challenge, you keep teasing me/feeling me up/reminding me of what you'll do to me once I lose", "", {}),
  simplest_item ("I [make a bet/play a game] where the punishment for losing is that you can top me as much as you want for the next X days", "", {}),
  simplest_item ("you order me to do things to myself even when we're not physically together", "Most of what I enjoy is on a mental level. My excitement comes from the <em>idea</em> of being vulnerable or helpless. So there's really no reason we actually have to be in the same place to do it.<br><br>This can be anything from just emailing me orders to challenging me to play a game with punishments over video chat.", {}),
  simplest_item ("you corner me in the bathroom", '''Because the bathroom is normally a private space, entering it is one of those things that's "exciting because I wouldn't normally allow it, but actually not harmful in any way, so it's fun to use for BDSM". Also, bathrooms usually have only one exit, so I'm cornered. You could even come in when I'm showering and take my clothes hostage.''', {}),
  simplest_item ("you ambush me by surprise", '''Normally, I don't like surprises. It's not that I <em>hate</em> been surprised – it's more like my reaction is just "well this new information is somewhat disruptive, please wait a moment so I can have a chance to process it". So I'm not entirely sure whether a surprise BDSM ambush would be fun. But I'm curious to try it.''', {"unsure": True}),
  simplest_item ("you ambush me while I'm still asleep", "I wonder if it's possible to tie me to the bed without waking me up...", {"unsure": True}),
]

circumstances_list = [
'''


fix hexy link
css generator

'''
]

lists = [
  {"name": "Stimulation list", "id": "stimulation", "description": "Things you can do to me even if I don't actively cooperate.", "list": stimulation_list},
  {"name": "Participation list", "id": "participation", "description": "Things you can force me to do, that require my cooperation.", "list": participation_list},
  {"name": "Conditions list", "id": "conditions", "description": "Things that can be ongoing while you do other stuff to me", "list": conditions_list},
  {"name": "Scene list", "id": "scene", "description": "Overall progressions of things we can do together.", "list": scene_list},
  {"name": "Bondage list", "id": "bondage", "description": "A few of the infinite ways I like to be tied up.", "list": bondage_list},
  {"name": "Miscellaneous list", "id": "miscellaneous", "description": '''Things that didn't fit into one of the other lists. Some of these things are hard to get permission for in-the-moment, so we'd have to <a href="/blog/consenting-in-advance">negotiate about them ahead of time</a>.''', "list": miscellaneous_list},
  {"name": "Impractical list", "id": "impractical", "description": "Things that I sometimes fantasize about, but don't do in real life because they're risky or impossible. Although we can still pretend or play-threaten to do them.", "list": impractical_list},
]

def render_item(simple, item, list):
  name = item["name"] + ("*" if "caveat" in item else "") + ("?" if "unsure" in item else "")
  if simple:
    return "<li>" + name + "</li>"
  return ("<tr>" + 
    "<td>" + name + "</td>" +
    ("<td>" + str (item ["min_unpleasantness"]) + "-" + str (item ["max_unpleasantness"])  + "</td>" +
    "<td>" + str (item ["min_pleasantness"]) + "-" + str (item ["max_pleasantness"])  + "</td>"
     if "min_unpleasantness" in item else '') +
    ("<td>" +str (item ["min_time"]) + "-"+ str (item ["max_time"]) + "</td>"
     if "min_time" in item else '') +
    "<td>" + item ["description"] + "</td>" +
  "</tr>")
  

def render_list(simple, list):
  header = "<h3>" + list ["name"] + '</h3> <p class="subtitle">' + list["description"] + "</p>"
  items ="".join([render_item (simple, item, list) for item in list["list"]])
  if simple:
    return header + "<ul>" + items + "</ul>"
  return header + "<table><tr><th></th>"+ ("<th> Unpl. </th><th> Plea. </th>" if "min_unpleasantness" in list ["list"] [0] else "")+("<th> Time </th>" if "min_time" in list ["list"] [0] else "")+"<th> Notes </th></tr>" + items + "</table>"

def render(simple):
  return "".join([render_list (simple, list) for list in lists])


contents = '''

<p>(Content: Details of sexual stuff, including BDSM things that would normally be violent.)</p>

This post describes the things I enjoy doing sexually. I have a lot of different purposes in writing it. Here are a few of them:
<ul class="big_list">
<li>For me and my play partners to use as a reference, to find ideas for things to do together.</li>
<li>To help normalize these desires. Now, I am hardly a normal person, so just listing them doesn't prove they're "normal". But trust me, none of them are especially rare. I also want to make sure everyone knows it's possible to do these things in a consensual environment. If you also want these things, but you're only getting them from a coercive relationship, trust me: better things are possible.</li>
<li>For people to enjoy reading, either because it sexually excites them or because it just satisfies their curiosity.</li>
</ul>

You may share this. I'm not keeping it secret from anyone.

<h2><em>Who</em> I would do these things with</h2>

Anyone who wants to do them with me, as long as I know them and trust that they wouldn't harm me or <em>be</em> harmed.

This theoretically has no boundaries of gender, although it's generally a bit harder for me to trust male people, in both ways.

A note about "be harmed": Many people form emotional attachments when they do sexual things. My brain works differently. It doesn't form emotional attachments to people, in any situation. Not everyone likes being attached to someone who isn't attached back. Asymmetric attachments aren't always bad, but they do have some risks, which I need to consider before I do stuff.

It's okay to try to befriend me specifically because you're looking for a play partner. If you do, I'd prefer that you be upfront about it, but I'm also fine if you don't. I'll understand if you aren't ready to trust <em>me</em> right away either. Also, you can always ask me for my honest assessment of how much I trust you at the moment and how much I expect I might trust you in the future.

<h2>Terminology</h2>

Most of the things I like involve having something "forced" on me by another person. In real life, I and another person would mutually agree to play out the "forcing". In that context, the one <em>doing</em> the thing is called the <strong>top</strong>, and the one <em>having the thing done to them</em> is called the <strong>bottom</strong>. "<strong>Topping</strong>" is also the verb for doing this.

You might have seen the similar terms "dom" and "sub". These are subtly different – they refer to some sort of human authority structures. For me, on a gut level, human authority structures are just meaningless. So I use different terms.

This is mostly a list of ways I like other people topping me. I also enjoy topping other people. However, this list doesn't cover that, for a couple reasons. First, when I top someone, what I enjoy is much more dependent on what the other person likes. (I think I get a lot of my enjoyment out of mentally mirroring their reactions.) Second, if I did have to pick my own preferences, it would basically be the same list, just in reverse.

Lastly, instead of saying "the top" or "the person I'm playing with" in this list, I'm going to say "you", because it's easier to read and doesn't sound as dry and formal.


<h2>The list</h2>

<p>(* = Only with specific caveats. ? = I haven't done this before, and I think I'd like it, but I'm not sure.)</p>

'''+ render (True) +'''

<h2>Detailed descriptions</h2>

I can identify four main ways things turn me on:

<ul>
<li><strong>Vulnerability</strong>, the feeling of my real-life boundaries being crossed</li>
<li><strong>Helplessness</strong>, the feeling of trying to resist but failing</li>
<li><strong>Sensation</strong>, either pain or sensual touch</li>
<li><strong>Exertion</strong>, using my muscles heavily</li>
</ul>

Naturally, many activities involve more than one of these things. There's also an element of <strong>choice</strong> – I almost always have to choose to interpret something in an arousing way, it doesn't just happen automatically.

I've rated the "unpleasantness" of each thing using <a href="/blog/my-0-10-pain-scale">my 0-10 pain scale</a>. I say "unpleasantness" instead of "pain", because the important thing is that I get overwhelmed with sensation, not exactly what kind of sensation it is. For instance, tickling can be overwhelming, but isn't literal pain. Higher unpleasantness can be either good or bad, depending on my mood at the time. Generally, the more tired I am, the more I want to avoid unpleasantness. The more energetic I am, the more I seek out unpleasantness on purpose.

I've also listed "pleasantness" for sensations that can become intense, but are still fine when I'm tired. It uses the same scale. "Time" is on a more arbitrary 1-7 scale. The minimum time listed for each thing is the minimum time <em>commitment</em> – for instance, including any setup or cleanup time. The maximum is the longest I could generally continue to enjoy doing it. That's why the minimum is greater than the maximum for some of them.

'''+ render (False) +'''

<h2>Activity generator</h2>

<div id="kink_generator"><p class="noscript">(There would also be a button here to randomly choose an activity from the lists, but it requires JavaScript.)</p></div>

<h2>Source code</h2>

<p><a href="https://github.com/elidupree/eliduprees-website-source/blob/master/posts/kinks.py">The source code of this whole page is available here on GitHub.</a></p>

'''

for list in lists:
  for item in list ["list"]:
    del item ["description"]

posts = [
{
  "title":"My kinks",
  "title_url_override": "kinks",
  "don't deploy": True,
  "auto_paragraphs": True,
  "contents": contents,
  "head": '''
  <style type="text/css">
th { padding: 0.3em 0em; }
td { padding: 0.3em 0.2em; }
td { border-top: 1px solid black; }
ul,table { margin-top: 0.6em; margin-bottom: 0.9em; }
h3 { padding-top: 0.5em }
.subtitle {margin:0.3em 0;}
/*textarea {display: block; width: 100%; height: 10em;}*/
#kink_generator {background-color: #ddd; border-radius: 2em; padding: 0.8em; }
#display {background-color: white; border-radius: 1.5em; padding: 0.8em; }
  </style>
  ''',
  "after_body": """<script type="text/javascript">

var stimulation = 0;
var participation = 1;
var conditions = 2;
var preprocessed_lists = """+json.dumps(lists)+r"""
var bondage;
var impractical;
var scene;


function adjust (item, attrs) {
  return changed = Object.assign({}, item, attrs);
}
function rename (item, name) {
  return adjust (item, {name});
}

preprocessed_lists.forEach(function(list) {
  var varying = [];
  list.list = list.list.filter(function(item) {
    item.original_list = list.id;
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
preprocessed_lists.forEach(function(list, index) {
  if (list.id === "bondage") {
    bondage = index;
  }
  if (list.id === "impractical") {
    impractical = index;
  }
  if (list.id === "scene") {
    scene = index;
  }
  list.list.forEach(function(item) {
    item.max_sensation = Math.max (item.max_unpleasantness, item.max_pleasantness);
    if (item.inflict) {
      preprocessed_lists[stimulation].list.push (adjust (item, {name: item.inflict, from_different_list: true, possible_tied: false}));
    }
    /*if (item.assume) {
      preprocessed_lists[participation].list.push (adjust (item, {name: item.assume, from_different_list: true}));
    }*/
  });
});
Array.prototype.push.apply (preprocessed_lists[participation].list, preprocessed_lists[stimulation].list.filter (item => !item.no_self).map (item => {
  return adjust (item, {
    name: item.name.replace (/\bme\b/, "myself").replace (/\bmy\b/, "my own").replace (/\byour\b/, "my"),
    weight: (item.weight || 1) * item.max_unpleasantness * item.max_unpleasantness / 100,
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
  return item && item.name;
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
    function inflict_until_surrender (lists, extras) {
      var unfiltered_list = [].concat (
        preprocessed_lists [stimulation].list.filter (item => item.max_unpleasantness >= 6),
        [{name: "squeeze my balls"}],
      );
      return choose (unfiltered_list.filter (extras.filter)) + " until I " + surrender(lists);
    }
    function threaten_unless_surrender (lists, extras) {
      // since the threat needn't be carried out, we choose it from the unfiltered list
      var unfiltered_list = [].concat (
        preprocessed_lists [stimulation].list.filter (item => item.max_unpleasantness >= 6).map (item => rename (item, "threaten to "+item.name + " unless I")),
        [{name: "threaten to squeeze my balls unless I"}],
        preprocessed_lists [impractical].list.filter (item => item.control).map (item => rename (item, item.control)),
      );
      return choose (unfiltered_list.filter(parameter_filter (adjust (extras.parameters,{max_unpleasantness: 10})))) + " " + surrender(lists);
    }
    function while_condition_inflict (lists) {
      return "while " + choose (lists[conditions].filter (item => item.enhance && !item.maintain)) + ", " + inflict(lists);
    }
    function challenge_to_maintain (lists) {
      var inflict_first = choose (lists [stimulation].filter (item => item.max_unpleasantness >= 5 && !item.from_different_list));
      return "challenge me to " + maintain_condition(lists, true) + " while you " + inflict_first + ". If I can't keep it up, " + choose (lists [stimulation].filter (item => item.max_sensation >= 7 && item.name !== inflict_first));
    }
function casually_force_condition (lists) {
      var item = random_choice (lists [conditions].filter (item => item.maintain && item.non_interfering))
      return item && ("casually force me to " + item.maintain + " for a while");
    }
function casually_inflict (lists) {
      return "from time to time, casually " + choose (lists [stimulation].filter (item => item.min_time <= 2 && item.max_sensation < 7));
    }
function tie_me_up (lists) {
  var item = random_choice (lists [bondage]);
  if (!item) return undefined;
  if (item.name.startsWith ("clothespins")) {
      return "put clothespins on my nipples and tie them " + item.name.replace ("clothespins on my nipples tied ", "");
    }
  if (item.name.startsWith ("tied")) {
    return "tie me " + item.name.replace ("tied ", "");
  }
  return "tie my " + item.name.replace ("tied ", "");
}
function random_scene(lists) {
  return choose (lists[scene].map (item => rename (item, item.name.replace ("you ", "").replace (", you", ","))));
}

function parameter_filter (parameters) {
  return function (item, list) {
    return (
      (item.min_unpleasantness === undefined || item.min_unpleasantness <= parameters.max_unpleasantness) &&
      (item.min_time === undefined || item.min_time <= parameters.max_time) &&
      (parameters.caveat_allowed || !item.caveat) &&
      (parameters.unsure_allowed || !item.unsure) &&
      (!parameters.remote_only || list.id === "participation" || (item.maintain && list.id !== "stimulation") || item.possible_remotely)
    );
  };
}
 
function global_generate (parameters, generators) {
  var filter = parameter_filter (parameters);
  var filtered_lists = preprocessed_lists.map (function (list) {return list.list.filter (function(item) {
    return filter(item, list) && (!parameters.filter || parameters.filter(item, list))
  });});

  //[].concat(
  //  stimulation_list.filter (filter),
  //);
  
  var result = "undefined";
  var attempts = 0;
  while (result.includes ("undefined")) {
    result = ""+random_choice (generators)(filtered_lists, {parameters, filter});
    if (++attempts > 1000) {return "Oops! Couldn't find any activities that meet your restrictions";}
  }
  return result;
}
function UI_generate(generators, parameters) {
  parameters = Object.assign({}, parameters);
  var max_time = Math.min($("#max_time").val(), parameters.max_time || 7);
  if ($("#remote").prop ("checked")) {
    parameters.remote_only = true;
    generators = generators.map (generator => (
      generator === inflict || generator === maintain_while_inflict || generator === inflict_until_surrender || generator === challenge_to_maintain || generator === casually_inflict || generator === tie_me_up
    ) ? I_must_participate : generator);
  }
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
    var number = $("#number").val();
    for (var index = 1; index < number;++index) {
      result += "<br>\n"+UI_generate(generators, parameters);
    }
    display.html(result);//.css("height", ""+(2+number*10/7)+"em");
  });
}

display = $("<div>", {id: "display"});
$("#kink_generator").append (
  
  
  "Generate ",
  $("<input>", {id: "number", type:"number", min: 1, max: 100, value: 7,}),
  " activities, with no more than ",
  $("<input>", {id: "max_unpleasantness", type:"number", min: 0, max: 10, value: 10,}),
  " unpleasantness, which take no longer than ",
  $("<input>", {id: "max_time", type:"number", min: 1, max: 7, value: 7,}),
  " time",
  $("<br>"),
  $("<input>", {id: "remote", type:"checkbox",}),
  $("<label>", {for:"remote", text:"only list things that we can do remotely (e.g. by email or video chat)"}),
  
  button("any random thing for us to do", 
    [inflict, inflict, inflict, I_must_participate, I_must_participate, I_must_participate, maintain_while_inflict, inflict_until_surrender, threaten_unless_surrender, challenge_to_maintain, casually_force_condition, casually_inflict, tie_me_up, random_scene, random_scene, random_scene, random_scene],
    {}
  ),
  button("a scene structure", 
    [random_scene],
    {}
  ),
  button("a way to tie me up", 
    [tie_me_up],
    {}
  ),
  button("something to do to me while I'm tied up", 
    [inflict, inflict, inflict, inflict, inflict, inflict, maintain_while_inflict, inflict_until_surrender, threaten_unless_surrender, challenge_to_maintain],
    {filter: function (item, list) {
      return ((list.id === "stimulation" && item.original_list === "stimulation") || item.possible_tied) && !item.not_when_tied;
    }}
  ),
  button("a punishment for losing one round of a game", 
    [I_must_strip, inflict, inflict, inflict, I_must_participate, I_must_participate, maintain_while_inflict ],
    {
      max_time: 3,
      filter: function (item, list) {
        return (item.original_list !== "stimulation" || item.max_sensation >= 4) &&
               (item.original_list !== "conditions" || item.non_interfering) &&
               (item.name !== "strip naked");

      }
    }
  ),
  
  display
);

</script>"""
},
]

