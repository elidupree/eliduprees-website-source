#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division



import utils
import re

def add_redirect(page_dict, from_path, to_path):
  utils.checked_insert(page_dict, from_path + '.301', to_path)
  return

old_website_conversions = {
  "main": "",
  "main/blog": "blog",
  "main/latest_comic_and_blog": "blog",
  "main/index": "",
  "main/atom.xml": "atom.xml",
  "main/tags/stories": "stories",
  "main/tags/games": "games",
  "main/tags/comic-pages": "comics",
  "main/tags/major-announcements-about-eli's-life": "blog/tags/announcements",
  "main/tags/posts-about-gender": "blog/tags/gender",
  "main/tags/posts-about-neurodiversity": "blog/tags/neurodiversity",
  "main/tags/posts-about-age-and-ageism": "blog/tags/ageism",
  "main/tags/posts-about-sex-and-sexuality": "blog/tags/sex",
  "main/tags/posts-about-writing": "blog/tags/writing",
  "main/tags/posts-about-other-philosophical-stuff": "blog/tags/philosophical",
  "main/tags/posts-about-visual-art": "blog/tags/visual-art",
  "main/tags/posts-about-mathematics": "blog/tags/math",
  "main/tags/posts-about-computer-programming": "blog/tags/programming",
  "main/tags/posts-about-crass-physical-reality": "blog/tags/crass-physical-reality",
  "main/tags/posts-about-lasercake": "blog/tags/lasercake",
  "main/tags/recommendations-of-other-websites": "blog/tags/other-websites",
  "main/tags/posts-about-the-website-itself": "blog/tags/this-website",
  "main/tags/posts-about-the-graphics-editing-project": "blog/tags/the-graphics-editing-project",
  "main/tags/pages-of-a-couple-of-badass-superheroes": "a-couple-of-badass-superheroes/archive",
  "main/tags/pages-of-voldemort's-children": "voldemorts-children/archive",
  "main/stories/121-not-what-i-am": "stories/not-what-i-am",
  "green_caves_game.html": "games/green-caves",
  "as-yet-untitled-story.html": "stories/will-you-try-to-escape",
  "will-you-try-to-escape.html": "stories/will-you-try-to-escape",
  "hexy-thank-you": "hexy",
  "temporary_hexy_bondage_distribution.html": "hexy",
  "pac-asteroids.html": "games/pac-asteroids",
  "pac-asteroids-first.html": "games/pac-asteroids",
  "hpmor_ending": "TODO",
  "colby_stuff/how_I_experienced_the_four_o_clock_discourse.png": "TODO",
  "colby_stuff/2011_11_06.png": "TODO",
  "colby_stuff/2011_11_07.png": "TODO",
  "main/posts/latest/voldemort's-children": "TODO",
  "main/posts/latest/a-couple-of-badass-superheroes": "TODO",
  "main/archives/a-couple-of-badass-superheroes": "a-couple-of-badass-superheroes/archive",
  "main/archives/voldemort's-children": "voldemorts-children/archive",
  
  
  
  "main/posts/1-the-epic-first-post": "blog/the-epic-first-post",
  "main/posts/6-user-comment": "blog/the-epic-first-post",
  "main/posts/7-user-comment": "blog/the-epic-first-post",
  "main/posts/8-user-comment": "blog/the-epic-first-post",
  "main/posts/9-scrutinized-words-she-he": "blog/scrutinized-words-she-he",
  "main/posts/10-user-comment": "blog/the-epic-first-post",
  "main/posts/11-user-comment": "blog/scrutinized-words-she-he",
  "main/posts/12-introducing-the-graphics-editing-project": "blog/introducing-the-graphics-editing-project",
  "main/posts/13-i-ordered-a-tablet-now-what": "blog/i-ordered-a-tablet-now-what",
  "main/posts/14-user-comment": "blog/i-ordered-a-tablet-now-what",
  "main/posts/15-author's-comment": "blog/i-ordered-a-tablet-now-what",
  "main/posts/16-first-progress": "blog/first-progress",
  "main/posts/17-user-comment": "blog/first-progress",
  "main/posts/18-user-comment": "blog/first-progress",
  "main/posts/19-user-comment": "blog/first-progress",
  "main/posts/20-scrutinized-words-man-woman-boy-girl": "blog/scrutinized-words-man-woman-boy-girl",
  "main/posts/21-an-unnamed-blog-post": "blog/minor-progress-on-the-haskell-exercise-and-stuff",
  "main/posts/22-user-comment": "blog/minor-progress-on-the-haskell-exercise-and-stuff",
  "main/posts/23-user-comment": "blog/first-progress",
  "main/posts/24-this-is-a-child-friendly-website": "blog/this-is-a-child-friendly-website",
  "main/posts/25-c-vs-haskell-round-one-what's-a-programming-language-anyway": "blog/c-vs-haskell-round-one-whats-a-programming-language-anyway",
  "main/posts/26-user-comment": "blog/scrutinized-words-man-woman-boy-girl",
  "main/posts/27-author's-comment": "blog/scrutinized-words-man-woman-boy-girl",
  "main/posts/28-nudity": "blog/nudity",
  "main/posts/29-release-early-release-often": "blog/release-early-release-often",
  "main/posts/30-user-comment": "blog/release-early-release-often",
  "main/posts/31-title-c-vs-haskell-round-two-but-i-want-it-to-be-fast": "blog/title-c-vs-haskell-round-two-but-i-want-it-to-be-fast",
  "main/posts/32-tablet-received": "blog/tablet-received",
  "main/posts/33-user-comment": "blog/title-c-vs-haskell-round-two-but-i-want-it-to-be-fast",
  "main/posts/34-user-comment": "blog/title-c-vs-haskell-round-two-but-i-want-it-to-be-fast",
  "main/posts/35-user-comment": "blog/title-c-vs-haskell-round-two-but-i-want-it-to-be-fast",
  "main/posts/36-two-days-later-everything-is-a-piece-of-shit": "blog/two-days-later-everything-is-a-piece-of-shit",
  "main/posts/37-user-comment": "blog/two-days-later-everything-is-a-piece-of-shit",
  "main/posts/38-recommended-website-harry-potter-and-the-methods-of-rationality": "blog/recommended-website-harry-potter-and-the-methods-of-rationality",
  "main/posts/39-a-few-concepts-i-need": "blog/a-few-concepts-i-need",
  "main/posts/40-user-comment": "blog/a-few-concepts-i-need",
  "main/posts/41-user-comment": "blog/recommended-website-harry-potter-and-the-methods-of-rationality",
  "main/posts/42-user-comment": "blog/recommended-website-harry-potter-and-the-methods-of-rationality",
  "main/posts/43-author's-comment": "blog/a-few-concepts-i-need",
  "main/posts/44-user-comment": "blog/scrutinized-words-man-woman-boy-girl",
  "main/posts/45-author's-comment": "blog/scrutinized-words-man-woman-boy-girl",
  "main/posts/46-happy-tau-day": "blog/happy-tau-day",
  "main/posts/47-sex": "blog/sex",
  "main/posts/48-user-comment": "blog/happy-tau-day",
  "main/posts/49-user-comment": "blog/sex",
  "main/posts/50-author's-comment": "blog/sex",
  "main/posts/51-recommended-website-fugitivus": "blog/recommended-website-fugitivus",
  "main/posts/52-neurodiversity": "blog/neurodiversity",
  "main/posts/53-user-comment": "blog/scrutinized-words-she-he",
  "main/posts/54-a-story-idea": "blog/story-idea-the-shell",
  "main/posts/55-user-comment": "blog/story-idea-the-shell",
  "main/posts/56-tired-of-coding": "blog/tired-of-coding",
  "main/posts/57-pornography": "blog/pornography",
  "main/posts/58-imagining-pain": "blog/imagining-pain",
  "main/posts/59-user-comment": "blog/imagining-pain",
  "main/posts/60-user-comment": "blog/imagining-pain",
  "main/posts/61-author's-comment": "blog/imagining-pain",
  "main/posts/62-user-comment": "blog/imagining-pain",
  "main/posts/63-user-comment": "blog/sex",
  "main/posts/64-author's-comment": "blog/sex",
  "main/posts/65-user-comment": "blog/sex",
  "main/posts/66-user-comment": "blog/story-idea-the-shell",
  "main/posts/67-user-comment": "blog/imagining-pain",
  "main/posts/68-user-comment": "blog/imagining-pain",
  "main/posts/69-user-comment": "blog/story-idea-the-shell",
  "main/posts/70-user-comment": "blog/sex",
  "main/posts/71-user-comment": "blog/imagining-pain",
  "main/posts/72-some-thoughts-about-expressiveness-socializing-and-honesty": "blog/some-thoughts-about-expressiveness-socializing-and-honesty",
  "main/posts/73-user-comment": "blog/some-thoughts-about-expressiveness-socializing-and-honesty",
  "main/posts/74-user-comment": "blog/neurodiversity",
  "main/posts/75-user-comment": "blog/some-thoughts-about-expressiveness-socializing-and-honesty",
  "main/posts/76-a-little-update": "blog/a-little-update",
  "main/posts/77-user-comment": "blog/scrutinized-words-man-woman-boy-girl",
  "main/posts/78-user-comment": "blog/this-is-a-child-friendly-website",
  "main/posts/79-author's-comment": "blog/scrutinized-words-man-woman-boy-girl",
  "main/posts/80-author's-comment": "blog/this-is-a-child-friendly-website",
  "main/posts/81-recommended-website-riot-nrrd": "blog/recommended-website-riot-nrrd",
  "main/posts/82-arrival": "blog/arrival",
  "main/posts/83-prose-vs-graphic-narration": "blog/prose-vs-graphic-narration",
  "main/posts/84-user-comment": "blog/imagining-pain",
  "main/posts/85-author's-comment": "blog/imagining-pain",
  "main/posts/86-user-comment": "blog/prose-vs-graphic-narration",
  "main/posts/87-author's-comment": "blog/prose-vs-graphic-narration",
  "main/posts/88-user-comment": "blog/sex",
  "main/posts/89-author's-comment": "blog/sex",
  "main/posts/90-user-comment": "blog/sex",
  "main/posts/91-user-comment": "blog/sex",
  "main/posts/92-user-comment": "blog/sex",
  "main/posts/93-user-comment": "blog/sex",
  "main/posts/94-user-comment": "blog/sex",
  "main/posts/95-user-comment": "blog/sex",
  "main/posts/96-user-comment": "blog/sex",
  "main/posts/97-in-which-i-rant-about-the-study-of-english": "blog/in-which-i-rant-about-the-study-of-english",
  "main/posts/98-user-comment": "blog/in-which-i-rant-about-the-study-of-english",
  "main/posts/99-user-comment": "blog/in-which-i-rant-about-the-study-of-english",
  "main/posts/100-user-comment": "blog/in-which-i-rant-about-the-study-of-english",
  "main/posts/101-author's-comment": "blog/in-which-i-rant-about-the-study-of-english",
  "main/posts/104-user-comment": "blog/in-which-i-rant-about-the-study-of-english",
  "main/posts/105-user-comment": "blog/in-which-i-rant-about-the-study-of-english",
  "main/posts/106-author's-comment": "blog/in-which-i-rant-about-the-study-of-english",
  "main/posts/107-user-comment": "blog/in-which-i-rant-about-the-study-of-english",
  "main/posts/108-an-unnamed-blog-post": "blog/minor-progress",
  "main/posts/109-a-couple-of-badass-superheroes-page-1": "a-couple-of-badass-superheroes/1",
  "main/posts/110-how-i-don't-get-frustrated-at-anything": "blog/how-i-dont-get-frustrated-at-anything",
  "main/posts/111-a-couple-of-badass-superheroes-page-2": "a-couple-of-badass-superheroes/2",
  "main/posts/112-user-comment": "a-couple-of-badass-superheroes/3",
  "main/posts/113-new-index-page": "blog/new-index-page",
  "main/posts/114-user-comment": "blog/new-index-page",
  "main/posts/115-author's-comment": "blog/new-index-page",
  "main/posts/116-user-comment": "blog/new-index-page",
  "main/posts/117-a-couple-of-badass-superheroes-page-3": "a-couple-of-badass-superheroes/4",
  "main/posts/118-some-things": "blog/some-things",
  "main/posts/119-a-couple-of-badass-superheroes-page-4": "a-couple-of-badass-superheroes/5",
  "main/posts/120-user-comment": "a-couple-of-badass-superheroes/6",
  "main/posts/121-finally-the-novella": "stories/not-what-i-am",
  "main/posts/122-user-comment": "stories/not-what-i-am/discussion",
  "main/posts/123-author's-comment": "stories/not-what-i-am/discussion",
  "main/posts/124-user-comment": "stories/not-what-i-am/discussion",
  "main/posts/125-author's-comment": "stories/not-what-i-am/discussion",
  "main/posts/126-user-comment": "stories/not-what-i-am/discussion",
  "main/posts/127-user-comment": "stories/not-what-i-am/discussion",
  "main/posts/128-a-couple-of-badass-superheroes-page-5": "a-couple-of-badass-superheroes/7",
  "main/posts/129-self-study": "blog/self-study",
  "main/posts/130-user-comment": "blog/self-study",
  "main/posts/131-user-comment": "a-couple-of-badass-superheroes/8",
  "main/posts/132-a-couple-of-badass-superheroes-page-6": "a-couple-of-badass-superheroes/9",
  "main/posts/133-author's-comment": "a-couple-of-badass-superheroes/10",
  "main/posts/134-no-comic-today": "blog/no-comic-today",
  "main/posts/135-a-couple-of-badass-superheroes-page-7": "a-couple-of-badass-superheroes/11",
  "main/posts/136-a-couple-of-badass-superheroes-page-8": "a-couple-of-badass-superheroes/12",
  "main/posts/137-recommended-website-the-usual-error": "blog/recommended-website-the-usual-error",
  "main/posts/138-let's-talk-about-affirmative-consent": "blog/lets-talk-about-affirmative-consent",
  "main/posts/139-user-comment": "blog/lets-talk-about-affirmative-consent",
  "main/posts/140-now-selling-posters": "blog/now-selling-posters",
  "main/posts/141-a-couple-of-badass-superheroes-page-9": "a-couple-of-badass-superheroes/13",
  "main/posts/142-user-comment": "a-couple-of-badass-superheroes/14",
  "main/posts/143-a-couple-of-badass-superheroes-page-10": "a-couple-of-badass-superheroes/15",
  "main/posts/144-user-comment": "a-couple-of-badass-superheroes/16",
  "main/posts/145-website-upgrades": "blog/website-upgrades",
  "main/posts/146-a-couple-of-badass-superheroes-page-11": "a-couple-of-badass-superheroes/17",
  "main/posts/147-a-couple-of-badass-superheroes-page-12": "a-couple-of-badass-superheroes/18",
  "main/posts/148-introducing-the-colby-sex-club": "blog/introducing-the-colby-sex-club",
  "main/posts/149-user-comment": "blog/introducing-the-colby-sex-club",
  "main/posts/150-author's-comment": "blog/introducing-the-colby-sex-club",
  "main/posts/151-a-couple-of-badass-superheroes-page-13": "a-couple-of-badass-superheroes/19",
  "main/posts/152-user-comment": "a-couple-of-badass-superheroes/20",
  "main/posts/153-a-couple-of-badass-superheroes-epilogue": "a-couple-of-badass-superheroes/21",
  "main/posts/154-more-website-upgrades": "blog/more-website-upgrades",
  "main/posts/155-user-comment": "blog/more-website-upgrades",
  "main/posts/156-author's-comment": "blog/more-website-upgrades",
  "main/posts/157-user-comment": "blog/introducing-the-colby-sex-club",
  "main/posts/158-author's-comment": "blog/introducing-the-colby-sex-club",
  "main/posts/159-voldemort's-children-cover-page": "voldemorts-children",
  "main/posts/160-voldemort's-children-page-1": "voldemorts-children/1",
  "main/posts/161-voldemort's-children-page-2": "voldemorts-children/2",
  "main/posts/162-voldemort's-children-chapter-1-title-page": "voldemorts-children/3",
  "main/posts/163-voldemort's-children-page-4": "voldemorts-children/4",
  "main/posts/164-voldemort's-children-page-5": "voldemorts-children/5",
  "main/posts/165-voldemort's-children-page-6": "voldemorts-children/6",
  "main/posts/166-voldemort's-children-page-7": "voldemorts-children/7",
  "main/posts/167-voldemort's-children-page-8": "voldemorts-children/8",
  "main/posts/168-voldemort's-children-page-9": "voldemorts-children/9",
  "main/posts/169-voldemort's-children-chapter-2-title-page": "voldemorts-children/10",
  "main/posts/170-voldemort's-children-page-11": "voldemorts-children/11",
  "main/posts/171-voldemort's-children-page-12": "voldemorts-children/12",
  "main/posts/172-voldemort's-children-page-13": "voldemorts-children/13",
  "main/posts/173-voldemort's-children-page-14": "voldemorts-children/14",
  "main/posts/174-voldemort's-children-page-15": "voldemorts-children/15",
  "main/posts/175-voldemort's-children-page-16": "voldemorts-children/16",
  "main/posts/176-voldemort's-children-page-17": "voldemorts-children/17",
  "main/posts/177-voldemort's-children-page-18": "voldemorts-children/18",
  "main/posts/178-voldemort's-children-page-19": "voldemorts-children/19",
  "main/posts/179-voldemort's-children-page-20": "voldemorts-children/20",
  "main/posts/180-voldemort's-children-page-21": "voldemorts-children/21",
  "main/posts/181-voldemort's-children-page-22": "voldemorts-children/22",
  "main/posts/182-voldemort's-children-page-23": "voldemorts-children/23",
  "main/posts/183-voldemort's-children-chapter-3-title-page": "voldemorts-children/24",
  "main/posts/184-voldemort's-children-page-25": "voldemorts-children/25",
  "main/posts/185-voldemort's-children-page-26": "voldemorts-children/26",
  "main/posts/186-voldemort's-children-page-27": "voldemorts-children/27",
  "main/posts/187-user-comment": "voldemorts-children/27",
  "main/posts/188-author's-comment": "voldemorts-children/27",
  "main/posts/189-voldemort's-children-page-28": "voldemorts-children/28",
  "main/posts/190-voldemort's-children-page-29": "voldemorts-children/29",
  "main/posts/191-user-comment": "voldemorts-children/29",
  "main/posts/192-author's-comment": "voldemorts-children/29",
  "main/posts/193-voldemort's-children-page-30": "voldemorts-children/30",
  "main/posts/194-voldemort's-children-page-31": "voldemorts-children/31",
  "main/posts/195-voldemort's-children-page-32": "voldemorts-children/32",
  "main/posts/196-voldemort's-children-page-33": "voldemorts-children/33",
  "main/posts/197-voldemort's-children-page-34": "voldemorts-children/34",
  "main/posts/198-voldemort's-children-page-35": "voldemorts-children/35",
  "main/posts/199-voldemort's-children-page-36": "voldemorts-children/36",
  "main/posts/200-voldemort's-children-page-37": "voldemorts-children/37",
  "main/posts/201-voldemort's-children-page-38": "voldemorts-children/38",
  "main/posts/202-voldemort's-children-page-39": "voldemorts-children/39",
  "main/posts/203-voldemort's-children-page-40": "voldemorts-children/40",
  "main/posts/204-voldemort's-children-page-41": "voldemorts-children/41",
  "main/posts/205-a-look-at-lasercake-one-of-my-upcoming-projects": "blog/a-look-at-lasercake-one-of-my-upcoming-projects",
  "main/posts/206-user-comment": "blog/a-look-at-lasercake-one-of-my-upcoming-projects",
  "main/posts/207-voldemort's-children-page-42": "voldemorts-children/42",
  "main/posts/208-user-comment": "voldemorts-children/42",
  "main/posts/209-voldemort's-children-page-43": "voldemorts-children/43",
  "main/posts/210-voldemort's-children-page-44": "voldemorts-children/44",
  "main/posts/211-voldemort's-children-page-45": "voldemorts-children/45",
  "main/posts/212-voldemort's-children-page-46": "voldemorts-children/46",
  "main/posts/213-voldemort's-children-page-47": "voldemorts-children/47",
  "main/posts/214-user-comment": "voldemorts-children/47",
  "main/posts/215-voldemort's-children-page-48": "voldemorts-children/48",
  "main/posts/216-author's-comment": "voldemorts-children/48",
  "main/posts/217-user-comment": "voldemorts-children/48",
  "main/posts/218-voldemort's-children-chapter-4-title-page": "voldemorts-children/49",
  "main/posts/219-user-comment": "voldemorts-children/49",
  "main/posts/220-author's-comment": "voldemorts-children/49",
  "main/posts/221-user-comment": "voldemorts-children/49",
  "main/posts/222-voldemort's-children-page-50": "voldemorts-children/50",
  "main/posts/223-voldemort's-children-page-51": "voldemorts-children/51",
  "main/posts/224-voldemort's-children-page-52": "voldemorts-children/52",
  "main/posts/225-voldemort's-children-page-53": "voldemorts-children/53",
  "main/posts/226-voldemort's-children-page-54": "voldemorts-children/54",
  "main/posts/227-voldemort's-children-page-55": "voldemorts-children/55",
  "main/posts/228-user-comment": "voldemorts-children/55",
  "main/posts/229-user-comment": "voldemorts-children/55",
  "main/posts/230-author's-comment": "voldemorts-children/55",
  "main/posts/231-voldemort's-children-page-56": "voldemorts-children/56",
  "main/posts/232-voldemort's-children-page-57": "voldemorts-children/57",
  "main/posts/233-user-comment": "voldemorts-children/57",
  "main/posts/234-voldemort's-children-page-58": "voldemorts-children/58",
  "main/posts/235-user-comment": "voldemorts-children/58",
  "main/posts/236-voldemort's-children-page-59": "voldemorts-children/59",
  "main/posts/237-voldemort's-children-chapter-5-title-page": "voldemorts-children/60",
  "main/posts/238-author's-comment": "voldemorts-children/60",
  "main/posts/239-user-comment": "voldemorts-children/60",
  "main/posts/240-author's-comment": "voldemorts-children/60",
  "main/posts/241-user-comment": "voldemorts-children/60",
  "main/posts/242-user-comment": "voldemorts-children/60",
  "main/posts/243-voldemort's-children-page-61": "voldemorts-children/61",
  "main/posts/244-voldemort's-children-page-62": "voldemorts-children/62",
  "main/posts/245-user-comment": "voldemorts-children/62",
  "main/posts/246-author's-comment": "voldemorts-children/62",
  "main/posts/247-social-standards-of-dress": "blog/social-standards-of-dress",
  "main/posts/248-user-comment": "blog/social-standards-of-dress",
  "main/posts/249-author's-comment": "blog/social-standards-of-dress",
  "main/posts/250-user-comment": "blog/social-standards-of-dress",
  "main/posts/251-voldemort's-children-page-63": "voldemorts-children/63",
  "main/posts/252-user-comment": "voldemorts-children/63",
  "main/posts/253-voldemort's-children-page-64": "voldemorts-children/64",
  "main/posts/254-voldemort's-children-page-65": "voldemorts-children/65",
  "main/posts/255-voldemort's-children-page-66": "voldemorts-children/66",
  "main/posts/256-voldemort's-children-page-67": "voldemorts-children/67",
  "main/posts/257-voldemort's-children-page-68": "voldemorts-children/68",
  "main/posts/258-voldemort's-children-page-69": "voldemorts-children/69",
  "main/posts/259-voldemort's-children-page-70": "voldemorts-children/70",
  "main/posts/260-voldemort's-children-page-71": "voldemorts-children/71",
  "main/posts/261-voldemort's-children-page-72": "voldemorts-children/72",
  "main/posts/262-voldemort's-children-chapter-6-title-page": "voldemorts-children/73",
  "main/posts/263-voldemort's-children-page-74": "voldemorts-children/74",
  "main/posts/264-voldemort's-children-page-75": "voldemorts-children/75",
  "main/posts/265-voldemort's-children-page-76": "voldemorts-children/76",
  "main/posts/266-voldemort's-children-page-77": "voldemorts-children/77",
  "main/posts/267-voldemort's-children-page-78": "voldemorts-children/78",
  "main/posts/268-user-comment": "voldemorts-children/78",
  "main/posts/269-author's-comment": "voldemorts-children/78",
  "main/posts/270-user-comment": "voldemorts-children/78",
  "main/posts/271-voldemort's-children-page-79": "voldemorts-children/79",
  "main/posts/272-voldemort's-children-page-80": "voldemorts-children/80",
  "main/posts/273-voldemort's-children-page-81": "voldemorts-children/81",
  "main/posts/274-voldemort's-children-page-82": "voldemorts-children/82",
  "main/posts/275-voldemort's-children-page-83": "voldemorts-children/83",
  "main/posts/276-voldemort's-children-page-84": "voldemorts-children/84",
  "main/posts/277-user-comment": "voldemorts-children/84",
  "main/posts/278-voldemort's-children-chapter-7-title-page": "voldemorts-children/85",
  "main/posts/279-voldemort's-children-page-86": "voldemorts-children/86",
  "main/posts/280-voldemort's-children-page-87": "voldemorts-children/87",
  "main/posts/281-voldemort's-children-page-88": "voldemorts-children/88",
  "main/posts/282-voldemort's-children-page-89": "voldemorts-children/89",
  "main/posts/283-voldemort's-children-page-90": "voldemorts-children/90",
  "main/posts/284-voldemort's-children-page-91": "voldemorts-children/91",
  "main/posts/285-voldemort's-children-page-92": "voldemorts-children/92",
  "main/posts/286-voldemort's-children-page-93": "voldemorts-children/93",
  "main/posts/287-voldemort's-children-page-94": "voldemorts-children/94",
  "main/posts/288-voldemort's-children-page-95": "voldemorts-children/95",
  "main/posts/289-voldemort's-children-page-96": "voldemorts-children/96",
  "main/posts/290-voldemort's-children-page-97": "voldemorts-children/97",
  "main/posts/291-voldemort's-children-page-98": "voldemorts-children/98",
  "main/posts/292-user-comment": "blog/social-standards-of-dress",
  "main/posts/293-user-comment": "blog/in-which-i-rant-about-the-study-of-english",
  "main/posts/294-user-comment": "blog/sex",
  "main/posts/295-user-comment": "blog/sex",
  "main/posts/296-author's-comment": "blog/sex",
  "main/posts/297-author's-comment": "blog/in-which-i-rant-about-the-study-of-english",
  "main/posts/298-voldemort's-children-page-99": "voldemorts-children/99",
  "main/posts/299-voldemort's-children-page-100": "voldemorts-children/100",
  "main/posts/300-voldemort's-children-page-101": "voldemorts-children/101",
  "main/posts/301-user-comment": "blog/in-which-i-rant-about-the-study-of-english",
  "main/posts/302-user-comment": "blog/in-which-i-rant-about-the-study-of-english",
  "main/posts/303-user-comment": "blog/in-which-i-rant-about-the-study-of-english",
  "main/posts/304-author's-comment": "blog/in-which-i-rant-about-the-study-of-english",
  "main/posts/305-author's-comment": "blog/in-which-i-rant-about-the-study-of-english",
  "main/posts/306-voldemort's-children-page-102": "voldemorts-children/102",
  "main/posts/307-user-comment": "voldemorts-children/102",
  "main/posts/308-voldemort's-children-page-103": "voldemorts-children/103",
  "main/posts/309-voldemort's-children-page-104": "voldemorts-children/104",
  "main/posts/310-user-comment": "voldemorts-children/104",
  "main/posts/311-user-comment": "voldemorts-children/104",
  "main/posts/312-voldemort's-children-page-105": "voldemorts-children/105",
  "main/posts/313-voldemort's-children-page-106": "voldemorts-children/106",
  "main/posts/314-voldemort's-children-page-107": "voldemorts-children/107",
  "main/posts/315-user-comment": "voldemorts-children/107",
  "main/posts/316-voldemort's-children-page-108": "voldemorts-children/108",
  "main/posts/317-voldemort's-children-page-109": "voldemorts-children/109",
  "main/posts/318-voldemort's-children-page-110": "voldemorts-children/110",
  "main/posts/319-user-comment": "voldemorts-children/110",
  "main/posts/320-voldemort's-children-page-111": "voldemorts-children/111",
  "main/posts/321-user-comment": "voldemorts-children/111",
  "main/posts/322-author's-comment": "voldemorts-children/111",
  "main/posts/323-user-comment": "voldemorts-children/111",
  "main/posts/324-author's-comment": "voldemorts-children/111",
  "main/posts/325-user-comment": "voldemorts-children/111",
  "main/posts/326-voldemort's-children-page-112": "voldemorts-children/112",
  "main/posts/327-user-comment": "voldemorts-children/112",
  "main/posts/328-user-comment": "voldemorts-children/112",
  "main/posts/329-user-comment": "voldemorts-children/112",
  "main/posts/330-user-comment": "voldemorts-children/112",
  "main/posts/331-author's-comment": "voldemorts-children/112",
  "main/posts/332-user-comment": "voldemorts-children/112",
  "main/posts/333-author's-comment": "voldemorts-children/112",
  "main/posts/334-user-comment": "voldemorts-children/112",
  "main/posts/335-user-comment": "voldemorts-children/112",
  "main/posts/336-author's-comment": "voldemorts-children/112",
  "main/posts/337-user-comment": "voldemorts-children/112",
  "main/posts/338-user-comment": "voldemorts-children/112",
  "main/posts/339-author's-comment": "voldemorts-children/112",
  "main/posts/340-user-comment": "voldemorts-children/112",
  "main/posts/341-author's-comment": "voldemorts-children/112",
  "main/posts/342-user-comment": "voldemorts-children/112",
  "main/posts/343-i'm-back": "blog/im-back",
  "main/posts/344-user-comment": "blog/im-back",
  "main/posts/345-user-comment": "blog/im-back",
  "main/posts/346-the-food-experiments": "blog/the-food-experiments",
  "main/posts/347-user-comment": "blog/the-food-experiments",
  "main/posts/348-i-made-biscuits": "blog/i-made-biscuits",
  "main/posts/349-user-comment": "blog/i-made-biscuits",
  "main/posts/350-the-carrying-contraption": "blog/the-carrying-contraption",
  "main/posts/351-user-comment": "blog/the-carrying-contraption",
  "main/posts/352-user-comment": "blog/how-i-dont-get-frustrated-at-anything",
  "main/posts/353-i-was-overheated-and-unproductive-but-now-i'm-not": "blog/i-was-overheated-and-unproductive-but-now-im-not",
  "main/posts/354-an-illustrated-guide-to-the-biscuits": "blog/an-illustrated-guide-to-the-biscuits",
  "main/posts/355-the-green-caves-game-returns": "blog/the-green-caves-game-returns",
  "main/posts/356-a-sexual-board-game": "blog/a-sexual-board-game",
  "main/posts/357-alignments": "blog/alignments",
  "main/posts/358-capitalism-sat": "stories/capitalism-sat",
  "main/posts/359-game-theory-contracts-altruism": "blog/game-theory-contracts-altruism",
  "main/posts/360-user-comment": "blog/game-theory-contracts-altruism",
  "main/posts/361-user-comment": "blog/neurodiversity",
  "main/posts/362-user-comment": "blog/some-thoughts-about-expressiveness-socializing-and-honesty",
  "main/posts/363-user-comment": "voldemorts-children/112",
  "main/posts/364-user-comment": "voldemorts-children/112",
  "main/posts/365-user-comment": "voldemorts-children/112",
  "main/posts/366-user-comment": "blog/alignments",
  "main/posts/367-user-comment": "blog/game-theory-contracts-altruism",
  "main/posts/368-author's-comment": "blog/game-theory-contracts-altruism",
  "main/posts/369-user-comment": "blog/alignments",
}
conveniences = {
  "hexybondage": "/hexy",
  "hexy-bondage": "/hexy",
  "hexy_bondage": "/hexy",
  "eohs": "https://www.patreon.com/EoHS",
  "Eohs": "https://www.patreon.com/EoHS",
  "EoHS": "https://www.patreon.com/EoHS",
  "EohS": "https://www.patreon.com/EoHS",
  "EOHS": "https://www.patreon.com/EoHS",
  "vc": "/voldemorts-children",
  "VC": "/voldemorts-children",
}

def add_redirects(page_dict):
  for from_path, to_path in old_website_conversions.items():
    add_redirect(page_dict, '/'+from_path, '/'+to_path)
    e = re.sub("'", "%27", from_path)
    if e != from_path:
      add_redirect(page_dict, '/'+e, '/'+to_path)
  for from_path, to_path in conveniences.items():
    add_redirect(page_dict, '/'+from_path, to_path)



