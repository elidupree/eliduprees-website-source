#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

import re

import utils

# You usually need to use re.DOTALL with this.
def grouped_string_regex(groupname):
  return r'[(](?P<delim_'+groupname+'>[^(]*)[(](?P<'+groupname+'>.*?)[)](?P=delim_'+groupname+')[)]'

scrutinized_words = [
  {
    "words":["she","her","hers","herself","he","him","his","himself"],
    "rationale_post":"/blog/scrutinized-words-she-he",
  },
  {
    # Note: "womyn" form for completeness, because I've seen it used a bunch, not to scrutinize it in particular.
    # Note: "guy" omitted because it's also a name, but I want to include it.
    "words":["man","men","woman","women","womyn","wymyn","boy","boys","girl","girls"],
    "rationale_post":"/blog/scrutinized-words-man-woman-boy-girl",
  },
]

any_scrutinized_word_regex = r"\b(?:"+("|".join(["|".join(info["words"]) for info in scrutinized_words]))+r")\b"

def scrutinized_word_info(word):
  for info in scrutinized_words:
    if word.lower() in info["words"]:
      return info
  return None

def scrutinize_word(word):
  info = scrutinized_word_info(word)
  if info is None:
    return word
  else:
    return '<a class="scrutiny" href="'+info["rationale_post"]+'">'+word+'</a>'

# returns a string with the words replaced.
# Note that this requires the post to have been cleaned up already (or it may choke on invalid quote structures).
def scrutinize_non_quoted_words(post_string):
  quote_levels = 0
  pieces = []
  amount_of_original_string_used = 0
  for match in re.finditer(r"<.*?>|(?:"+any_scrutinized_word_regex+r")", post_string, re.IGNORECASE):
    if match.group(0).lower() == "<q>" or match.group(0).lower() == "<blockquote>":
      quote_levels += 1
    elif match.group(0).lower() == "</q>" or match.group(0).lower() == "</blockquote>":
      quote_levels -= 1
    elif quote_levels == 0:
      for info in scrutinized_words:
        if match.group(0).lower() in info["words"]:
          pieces.append(post_string[amount_of_original_string_used:match.start(0)])
          pieces.append(scrutinize_word(match.group(0)))
          amount_of_original_string_used = match.end(0)
  return ("".join(pieces+[post_string[amount_of_original_string_used:]]), len(pieces))

def neurodiversity_link(post_string):
  quote_levels = 0
  pieces = []
  amount_of_original_string_used = 0
  for match in re.finditer(r"<.*?>|neurodiversity|neurelitist|neurelitism|neurovariant|neurodivergent", post_string, re.IGNORECASE):
    if match.group(0).lower() == "<q>" or match.group(0).lower() == "<blockquote>":
      quote_levels += 1
    elif match.group(0).lower() == "</q>" or match.group(0).lower() == "</blockquote>":
      quote_levels -= 1
    elif quote_levels == 0:
      if match.group(0) [0] != "<":
        pieces.append(post_string[amount_of_original_string_used:match.start(0)])
        pieces.append('<a href="/blog/neurodiversity">'+match.group(0)+'</a>')
        amount_of_original_string_used = match.end(0)
        break
  return "".join(pieces+[post_string[amount_of_original_string_used:]])

def postprocess_post_string(initial_string, unique_id, title, mark_broken_tags, scrutinize = True):
  result_string = initial_string
  marked_broken_tags = False

  # HACK: This currently has to be the FIRST operation done on the post string because it compares directly to the post_string
  if mark_broken_tags:
    result_string = re.sub(chars_to_html_escapements["<"]+"/?[a-z]+/?"+chars_to_html_escapements[">"], lambda pattern: '<span class="skepticism">'+pattern.group(0)+'</span>', initial_string)
    if result_string != initial_string:
      marked_broken_tags = True

  # Replace most normal quotations with <q></q>. This is very imperfect, but covers most normal situations.
  result_string = re.sub(r'(?:\A|(?<=[>\-\s]))"(?! )([^"]*?)(?<! )"', lambda match: "<q>"+match.group(1)+"</q>", result_string)

  next_footnote_number = 1
  footnotes = []
  while True:
    footnote_generator = re.search(r"<footnote"+grouped_string_regex("footnote_text")+">", result_string, re.DOTALL)
    if footnote_generator is None:
      break
    footnote_identifier_string = str(next_footnote_number)+'_'+unique_id
    result_string = result_string[0:footnote_generator.start(0)]+'<sup><a class="footnote_link" id="footnote_link_'+footnote_identifier_string+'" href="#footnote_body_'+footnote_identifier_string+'">'+str(next_footnote_number)+'</a></sup>'+result_string[footnote_generator.end(0):]
    footnotes.append('<li id="footnote_body_'+footnote_identifier_string+'">'+footnote_generator.group("footnote_text")+' <sup><a class="footnote_link" href="#footnote_link_'+footnote_identifier_string+'">back</a></sup></li>')
    next_footnote_number = next_footnote_number + 1
  if len(footnotes) > 0:
    result_string = result_string+'<div class="footnotes">Footnotes:<br/><ol>'+''.join(footnotes)+'</ol></div>'

  words_replaced = 0
  if scrutinize:
    (result_string, words_replaced) = scrutinize_non_quoted_words(result_string)
  result_string = re.sub(r"<blockquote>", '<div><span class="big_quote_mark_outer"><span class="big_quote_mark_inner">&#8220;</span></span><blockquote>', result_string)
  result_string = re.sub(r"</blockquote>", '</blockquote></div>', result_string)
  if title != "Neurodiversity":
    # Sub in the first use of the string "neurodiversity" with a link to my awesome post. Note that this is done AFTER the footnotes are replaced, in order to prefer subbing the first occurence of the word in the body text rather than the first in the flow of reading all footnotes immediately.
    result_string = neurodiversity_link(result_string)
  
  #hack: q tags automatically display quote marks, but they can't be copied,
  #so that's bad. So replace them.
  result_string = re.sub(r"<q>", '<span class="inline_quote">“', result_string)
  result_string = re.sub(r"</q>", '”</span>', result_string)
  return (result_string, words_replaced, marked_broken_tags)
