#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import html_pages
import bars
	  
def add_game(page_dict):
  utils.make_page (page_dict,
    '/hexy.html',
      "Hexy Bondage ⊂ Eli Dupree's website",
      r'''
<style>
body.hexy .bars_outer_box {
  background-color: #878787;
  background-image: url("/media/hexy_bondage_page_background.jpg?rr"); }

div.hexy_content h1{ font-size: 200%; font-weight: bold; padding-top: 0.20em; }
div.hexy_content h2{ font-size: 150%; font-weight: bold; padding-top: 0.30em; }
div.hexy_content p,div.hexy_content div.fake_p { margin: 0; padding: 0.5em 0; }
div.hexy_content a:link { color:blue }
div.hexy_content a:visited { color:purple }

div.hexy_content div.subtitle { font-weight: bold; font-size: 90%; padding-bottom: 0.5em;}
div.hexy_content {
  text-align: center;
  font-family: Arial, Helvetica, sans-serif;
  max-width: 50em;
  margin: 0 auto; }
div.hexy_content form,div.hexy_content table {
  display: inline; }
div.hexy_content .paynowbutton {
  vertical-align: middle; }
div.hexy_content div.bigbox_outer {
  padding: 0.2em 0.4em; }
div.hexy_content div.bigbox {
  border-radius: 1.4em;
  padding: 0.3em;
  background-color: #ffffff;
  background-color: rgba(255,255,255,0.95); }
div.hexy_content div.bigbox.thankyou {
  padding: 1.0em 0.3em;
  background-color: #ffff00;
  background-color: rgba(255,255,0,0.90); }
div.hexy_content div.bigbox_outer.narrower { display:inline-block; }
div.hexy_content div.bigbox_outer.last { padding-bottom: 0.4em; }
div.hexy_content div.bigbox_outer:first-child { padding-top: 0.4em; }

div.hexy_content div.bigbox_outer.comments {
  font-size: 80%;
  font-family: Times New Roman, Times, serif; }
div.hexy_content div.bigbox.comments {
  padding-bottom: 1.0em; }

@media (min-width: 30em) {
  div.hexy_content div.bigbox_outer {
    padding: 0.6em 1.8em; }
  div.hexy_content div.bigbox {
    border-radius: 2.2em;
    padding: 0.7em 1em;
  }
  div.hexy_content div.bigbox.thankyou {
    padding: 1.8em 1em; }
  div.hexy_content div.bigbox_outer.last { padding-bottom: 1.2em; }
  div.hexy_content div.bigbox_outer:first-child { padding-top: 1.2em; }
  div.hexy_content {
    font-size: 1.2em; 
  }
  div.hexy_content div.bigbox_outer.comments {
    font-size: 70%; }
  div.hexy_content form.paypal_stuff {
    white-space: nowrap;
  }
}
@media (min-width: 13em) {
  div.hexy_content a.lesswrap {
    white-space: nowrap;
  }
}
</style>
''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''<main>
  <div id="content" class="hexy_content">
<div class="bigbox_outer">
<div class="bigbox">
  <h1>Hexy Bondage</h1>
  <div class="subtitle">A sexual board game for two or more players</div>
  <p>
Hexy Bondage is a game where in-game actions cause you to be tied up in real life.
  </p>
  <p>
Players take turns placing tiles. Each tile has an icon (hand, foot, torso, crotch, furniture...)
and some paths. The paths can be used to connect icons together. Connections cause
things to happen in real life, like tying your body parts together. A player wins
when their “opponent” is too tied up to reach the board.
  </p>
  <p><a class="lesswrap" href="/hexy/hexy-bondage-rules.pdf">Read the full rules (pdf)</a></p>
</div>
</div>
<div class="bigbox_outer">
<div class="bigbox">
  <div class="fake_p">Tiles (print them, cut them out): <a class="lesswrap" href="/hexy/hexy-bondage-tiles.pdf">Download tiles</a> and/or 
  
<!-- Notes: The PayPal button code modified as follows:
  Remove the table structure and the visible ":"
  add class="paypal_stuff" to the form element
  add class="paynowbutton" to the select and input-image elements
  add selected to the second option
  change button image alt to "Pay Now"
  remove the (probably for tracking and nothing else) pixel gif
-->
<form class="paypal_stuff" action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_s-xclick">
<input type="hidden" name="hosted_button_id" value="VR5BUZK88GMCL">
<input type="hidden" name="on0" value=":">
<select class="paynowbutton" name="os0">
        <option value="Be cool...">Be cool... $10.00 USD</option>
        <option selected value="Be awesome...">Be awesome... $20.00 USD</option>
        <option value="Be extravagant...">Be extravagant... $50.00 USD</option>
</select>
<input type="hidden" name="currency_code" value="USD">
<input class="paynowbutton" type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_paynow_SM.gif" border="0" name="submit" alt="Pay Now">
</form>


</div>
<p>(Paying supports my work, so I can keep making things available to those who can't pay.)</p>
</div>
</div>
<div class="bigbox_outer">
<div class="bigbox">
  <h2>Extras:</h2>
  <p>Tile sheets for extra players:
    <a class="lesswrap" href="/hexy/hexy-bondage-extra-tiles-green.pdf">green checkers</a>,
    <a class="lesswrap" href="/hexy/hexy-bondage-extra-tiles-pink.pdf">pink polka dots</a>,
    <a class="lesswrap" href="/hexy/hexy-bondage-extra-tiles-blue.pdf">blue waves</a>,
    <a class="lesswrap" href="/hexy/hexy-bondage-extra-tiles-purple.pdf">purple stripes</a></p>
  <p>Black-and-white versions of tiles for extra players:
    <a href="/hexy/hexy-bondage-extra-tiles-checkers.pdf">checkers</a>,
    <a href="/hexy/hexy-bondage-extra-tiles-polkadots.pdf">polka dots</a>,
    <a href="/hexy/hexy-bondage-extra-tiles-waves.pdf">waves</a>,
    <a href="/hexy/hexy-bondage-extra-tiles-stripes.pdf">stripes</a></p>
  <p><a href="/hexy/hexy-bondage-blank-tiles.pdf">Sheet of blank tiles</a></p>
</div>
</div>
<div class="bigbox_outer narrower">
<div class="bigbox narrower">
  <p>Hexy Bondage is a creation of <a class="lesswrap" href="/" xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName" rel="cc:attributionURL">Eli Dupree.</a><br />Contact Eli to report any issues, no matter how minor:<br />'''+exmxaxixl.a(exmxaxixl.axdxrxexsxs)+'''</p>
  <p><a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Hexy Bondage</span> is licensed under a<br /><a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.
  </p>
</div>
</div>
<div class="bigbox_outer narrower comments last">
<div class="bigbox narrower comments last">
  '''+blog.comments_section("hexy")+'''
</div>
</div>
  </div>
</main>'''), {"body_class":"hexy"}
  )
