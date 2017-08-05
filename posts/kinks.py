#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import json

def simple_item(name, min_unpleasantness, max_unpleasantness, min_pleasantness, max_pleasantness, min_time_commitment, description, extra = {}):
  result = extra.copy()
  result.update ({
    "name": name,
    "min_unpleasantness": min_unpleasantness,
    "max_unpleasantness": max_unpleasantness,
    "min_pleasantness": min_pleasantness,
    "max_pleasantness": max_pleasantness,
    "min_time_commitment": min_time_commitment,
    "description": description,
  })
  return result

immediate = 1
small = 3
medium = 5
long = 8

stimulation_list = [
  simple_item ("push me around", 0, 1, 0, 2, immediate, "TODO description", {"no_self": True}),
  simple_item ("pin me down", 0, 1, 0, 3, immediate, "TODO description", {"no_self": True}),
  simple_item ("grab me by the hair", 1, 4, 0, 2, immediate, "A great combination of the slight pain of pulling my hair with physical control over the position of my head. Just be careful not to bend my neck in a weird direction."),
  simple_item ("slap me in the face", 1, 4, 0, 0, immediate, "TODO description"),
  simple_item ("tickle me", 2, 4, 0, 3, immediate, "TODO description", {"no_self": True}),
  simple_item ("squeeze my breasts", 0, 2, 1, 4, immediate, "TODO description"),
  simple_item ("pinch/twist my nipples", 1, 6, 0, 3, immediate, "TODO description"),
  simple_item ("stroke/lick/suck my neck, nipples, undersides of arms, sides, face, inner thighs", 0, 2, 1, 6, immediate, "TODO description", {"variants":[
    simple_item (verb+" "+noun, 0, 2, 1, 6, immediate, "", {"weight":weight, "no_self": verb != "stroke"})
      for (verb, weight) in [("stroke", 2), ("lick", 1), ("suck", 1)]
      for noun in ["my neck","my nipples","the undersides of my arms","my sides","my face","my inner thighs"]
      if (verb != "suck") or (noun not in ["my sides","my face","my inner thighs"])
  ]}),
  simple_item ("slap/whip me in the chest, nipples, stomach, inner thighs", 1, 7, 0, 2, immediate, "The best thing is to slap/whip me on all different parts of my body. If you whip the same spot repeatedly, the pain gets more intense, but stops being sexy.", {"variants":[
    simple_item (verb+" me in the "+noun, 1 + intensity, 5 + intensity, 0, 2, time, "")
    for (verb, time, intensity) in [("slap", immediate, 0), ("whip", immediate + 1, 2)] for noun in ["chest","nipples","chest and stomach","inner thighs"]
  ]}),
  simple_item ("spray me with water", 0, 3, 1, 5, medium, "TODO description"),
  simple_item ("hit me in the balls", 2, 7, 1, 3, immediate, '''Some people worry that the sudden pain of ball-kicking can risk causing a heart attack. I normally avoid risk, but in this case, I think that I get a lot less pain than most people with testicles do. Maybe mine are desensitized because I've hit them for fun so many times, or maybe they've just always been less sensitive. When I was a little kid, I got hit there once during a soccer game, and my reaction was like "This pain is kind of weird, but why is everyone acting so empathetic? It's not THAT bad."<br> The real caveat is that if my balls get hit a lot of times, they'll be achy for the next few days, which is inconvenient. Hitting them <em>hard</em> is good if you do it once or a few times, but hitting them <em>repeatedly</em> is a bigger commitment.''', {"caveat": True}),
  simple_item ("scratch me", 2, 5, 2, 3, immediate, "I didn't think of this myself. A play partner asked to try scratching me, and I didn't expect much from it, but it turned out to be a much bigger sensation than I expected. Kind of like tickling, but more aggressive. Scratching me repeatedly gets annoying, but an occasional long scratch really emphasizes that you have the power to inflict sensations on me, which is exciting."),
  simple_item ("scratch the soles of my feet", 4, 7, 0, 1, immediate+1, "TODO description"),
  simple_item ("force me to orgasm", 0, 2, 3, 7, medium, '''Being forced to orgasm is a huge fantasy for me. The trouble is that generally, after I <em>actually</em> orgasm, I completely lose interest in sexual things. I don't even get the "post-orgasm glow" or satisfied feeling that a lot of people say they get. I <em>sometimes</em> stay interested, but I don't know exactly what determines it. With the right play partner, I might be interested in experimenting with this. Currently, I generally avoid orgasming when actually playing with people.''', {"caveat": True}),
  simple_item ("dunk me in water", 1, 2, 1, 4, medium, "TODO description"),
  simple_item ("put your hand threateningly on my throat, balls", 0, 1, 2, 4, immediate, "I don't do actual choking because of the risks, but the threat is exciting.", {"no_self": True, "variants": [
    simple_item ("put your hand threateningly on my "+noun, 0, 1, 2, 4, immediate, "", {"no_self": True})
    for noun in ["throat","balls"]
  ]}),
  simple_item ("talk to me intimidatingly", 0, 2, 0, 4, immediate, "I feel like most of the time I'd just laugh at it, but if you said exactly the right thing and I was in exactly the right mood, it could be exciting.", {"no_self": True, "unsure": True}),
  simple_item ("electrostim", 1, 7, 0, 1, immediate, "The idea of being tortured with electricity turns me on a lot. In practice, I'd have to find someone who was enough of an expert to make sure it was safe. It's not my biggest desire, so I haven't gone out looking, but if I run into someone with the knowledge, I'm eager to try it.", {"unsure": True, "no_generate": True}),
]

participation_list = [
  simple_item ("strip naked", 0, 1, 0, 3, small, "TODO description"),
  simple_item ("allow you to strip me yourself", 0, 2, 1, 4, small, "It would be nice if this could go in the stimulation list, but in practice, it's pretty hard to pull off someone's clothes if they're just sitting there rather than actively helping out."),
  simple_item ("do exercises (e.g. squats, situps, jumping jacks)", 1, 5, 0, 2, small, "TODO description"),
  simple_item ("get in a cold shower", 3, 5, 0, 0, medium, "TODO description"),
  simple_item ("get in a shower with my clothes still on", 1, 2, 0, 2, medium, "TODO description"),
  simple_item ("sleep naked overnight", 0, 0, 0, 2, long, "TODO description"),
  simple_item ("sleep naked and exposed, with no blankets", 1, 2, 0, 2, long, "TODO description"),
  simple_item ("do [anything from the stimulation list] to myself", 0, 7, 0, 7, immediate, "TODO description", {"no_generate": True}),
  simple_item ("put myself in [anything from the conditions list]", 0, 7, 0, 7, immediate, "TODO description", {"no_generate": True}),
]

conditions_list = [
  simple_item ("I'm tied up", 0, 3, 0, 3, medium, "TODO description", {"inflict": "tie me up", "enhance": True}),
  simple_item ("I'm blindfolded", 0, 2, 0, 1, immediate, "TODO description", {"inflict": "blindfold me", "enhance": True}),
  simple_item ("I'm gagged", 0, 2, 0, 2, medium, "TODO description", {"inflict": "gag me"}),
  simple_item ("I'm kneeling", 0, 2, 0, 0, immediate, "TODO description", {"assume": "kneel", "enhance": True}),
  simple_item ("I'm forced to remain naked/partially naked", 0, 1, 0, 3, small, "TODO description", {}),
  simple_item ("I'm forced to remain naked when it's cold", 1, 3, 0, 3, small, "TODO description", {}),
  simple_item ("I have clothespins on my nipples", 1, 5, 0, 3, immediate + 1, "TODO description", {"inflict": "put clothespins on my nipples"}),
  simple_item ("I'm wearing a collar", 0, 1, 0, 2, small, "Collars aren't as exciting for me as they are for people who do power dynamics, but the slight pressure on my neck makes me feel nice and vulnerable.", {"inflict": "put a collar on me"}),
  simple_item ("I'm forced to stand in a stress position, like with my legs bent and/or my arms over my head", 2, 5, 0, 4, immediate + 1, "Having my muscles straining makes all pleasure sensations much more intense.", {"maintain": "stand in a stress position", "enhance": True}),
  simple_item ("I'm in a predicament bondage position", 4, 7, 0, 4, medium, "TODO description", {"inflict": "put me in predicament bondage", "enhance": True}),
  simple_item ("I'm forced to stay perfectly still", 0, 1, 0, 1, immediate, "TODO description", {"maintain": "stay perfectly still", "enhance": True}),
  simple_item ("I'm forced to keep my eyes closed", 2, 3, 0, 3, immediate, '''I don't normally trust people enough to close my eyes in front of them. If someone says "close your eyes", I just don't do it. In a BDSM context, it can make me nervous in a good way. It's like being blindfolded, but with the extra bonus that I feel threatened by the idea that I could be making a mistake by trusting the other person. (Literally speaking, I'm trusting them just as much if I let them blindfold me, but it feels different. It feels more like I have the option to open my eyes at any time, so the "mistake" is prolonged.)''', {"maintain": "keep my eyes closed", "enhance": True}),
  simple_item ("I'm forced to look you in the eye", 0, 3, 0, 2, immediate, "Eye contact can be slightly uncomfortable for me, as it is for many autistic people. In the right context, that discomfort can be used for fun. Also, it stops me from looking at what you're doing, which is exciting for the same reason as a blindfold.", {"maintain": "look you in the eye", "caveat": True, "enhance": True}),
  simple_item ("one or more other people are watching/participating", 0, 0, 0, 2, medium, "Naturally, I would have to trust everyone involved. But I'd love to have people ganging up on me.", {"caveat": True, "no_generate": True}),
]

lists = [
  {"name": "Stimulation list", "description": "Things you can do to me even if I don't actively cooperate", "list": stimulation_list},
  {"name": "Participation list", "description": "Things you can force me to do, that require my cooperation", "list": participation_list},
  {"name": "Conditions list", "description": "Things that can be ongoing while you do other stuff to me", "list": conditions_list},
]

def render_item(simple, item, list):
  name = item["name"] + ("*" if "caveat" in item else "") + ("?" if "unsure" in item else "")
  if simple:
    return "<li>" + name + "</li>"
  return ("<tr>" + 
    "<td>" + name + "</td>" +
    "<td>" + str (item ["min_unpleasantness"]) + "-" + str (item ["max_unpleasantness"])  + "</td>" +
    "<td>" + str (item ["min_pleasantness"]) + "-" + str (item ["max_pleasantness"])  + "</td>" +
    "<td>" + str (item ["min_time_commitment"]) + "</td>" +
    "<td>" + item ["description"] + "</td>" +
  "</tr>")
  

def render_list(simple, list):
  header = "<h3>" + list ["name"] + '</h3> <p class="subtitle">' + list["description"] + "</p>"
  items ="".join([render_item (simple, item, list) for item in list["list"]])
  if simple:
    return header + "<ul>" + items + "</ul>"
  return header + "<table><tr><th></th><th> Unpl. </th><th> Plea. </th><th> Time </th><th> Notes </th></tr>" + items + "</table>"

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

I've also listed "pleasantness" for sensations that can become intense, but are still fine when I'm tired. It uses the same scale. "Time" is on a more arbitrary 1-10 scale. The time listed for each thing is the <em>minimum</em> time commitment. (Most of them can go on for longer just by repeating the thing.)

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
td { padding-top: 0.5em }
ul { margin-top: 0.6em; margin-bottom: 0.9em; }
h3 { padding-top: 0.5em }
.subtitle {margin:0.3em 0;}
textarea {display: block; width: 100%; height: 10em;}
  </style>
  ''',
  "after_body": """<script type="text/javascript">

var stimulation = 0;
var participation = 1;
var conditions = 2;
var preprocessed_lists = JSON.parse (`"""+json.dumps(lists)+r"""`)

function rename (item, name) {
  var changed = Object.assign({}, item);
  changed.name = name;
  return changed;
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
      preprocessed_lists[stimulation].list.push (rename (item, item.inflict));
    }
    if (item.assume) {
      preprocessed_lists[participation].list.push (rename (item, item.assume));
    }
  });
});
Array.prototype.push.apply (preprocessed_lists[participation].list, preprocessed_lists[stimulation].list.filter (item => !item.no_self).map (item => {
  var changed = Object.assign({}, item);
  changed.name = item.name.replace (/\bme\b/, "myself").replace (/\bmy\b/, "my own").replace (/\byour\b/, "my");
  return changed;
}));



/* Things to generate notes
punishment for losing one round of a game
punishment for losing big game
scene for an afternoon together
something to do remotely
something to do while I'm tied up
*/

function random_range (min, max) {
  return min + Math.floor (Math.random()*(max - min));
}
function random_choice (sequence) {
  return sequence [random_range (0, sequence.length)];
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
function maintain_condition (lists) {
  return choose (lists[conditions].filter (item => item.maintain).map (item => rename (item, item.maintain)));
}
/*function while_enhanced (lists) {
  var item = random_choice (lists[conditions].filter (item => item.enhance && !item.maintain));
  if (item.inflict)
    return "agree to " + participate (lists);
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
  var generators = [
    function(lists) {
      return inflict (lists);
    },
    function(lists) {
      return "make me " + participate (lists);
    },
    function(lists) {
      return "make me " + maintain_condition(lists) + " while you " + choose (lists [stimulation].filter (item => item.max_sensation >= 4));
    },
    function(lists) {
      return choose (lists [stimulation].filter (item => item.max_unpleasantness >= 6).concat ([{name: "squeeze my balls"}])) + " until I " + surrender(lists);
    },
    function(lists) {
      return "threaten to "+choose (lists [stimulation].filter (item => item.max_unpleasantness >= 6).concat ([{name: "squeeze my balls"},{name: "beat me up"},{name: "cut me with a (not actually sharp) knife"}])) + " unless I " + surrender(lists);
    },
    function (lists) {
      return "while " + choose (lists[conditions].filter (item => item.enhance && !item.maintain)) + ", " + inflict(lists);
    },
  ];
  var recursive_generators = [
    function (lists, generate) {
      return "while " + condition(lists) + ", " + generate();
    },
  ];
  
function global_generate (parameters, recursion_levels) {
  var filter = function (item) {
    return (
      item.min_unpleasantness <= parameters.max_unpleasantness &&
      item.min_time_commitment <= parameters.max_time &&
      (parameters.caveat_allowed || !item.caveat) &&
      (parameters.unsure_allowed || !item.unsure)
    )
  }
  var filtered_lists = preprocessed_lists.map (function (list) {return list.list.filter (filter);});

  //[].concat(
  //  stimulation_list.filter (filter),
  //);
  
  return random_choice (generators)(filtered_lists);
}
function UI_generate() {
  return global_generate({max_unpleasantness: $("#max_unpleasantness").val(), max_time: $("#max_time").val(), caveat_allowed: true});
}

display = $("<textarea>");
$("#kink_generator").append (
  
  $("<button>").text ("Generate").click (function() {
    var result = UI_generate();
    for (var index = 1; index < $("#number").val();++index) {
      result += "\n"+UI_generate();
    }
    display.text(result);
  }),
  $("<input>", {id: "number", type:"number", min: 1, max: 100, value: 7,}),
  "activities with no more than",
  $("<input>", {id: "max_unpleasantness", type:"number", min: 0, max: 10, value: 10,}),
  "unpleasantness, which take no longer than",
  $("<input>", {id: "max_time", type:"number", min: 0, max: 10, value: 10,}),
  "time",
  display
);

</script>"""
},
]

