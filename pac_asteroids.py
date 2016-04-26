#!/usr/bin/python
# -*- coding: utf-8 -*-

import utils
import html_pages
import bars
	  
def add_game(page_dict):
  utils.checked_insert(page_dict,
    '/games/pac-asteroids.html',
    html_pages.make_page(
      "Pac-Asteroids ⊂ Eli Dupree's website",
      r'''
    <script type="text/javascript" src="/media/jquery-1.6.2.min.js?rr"></script>
    <script type="text/javascript">
Math.TAU = Math.PI*2;
$(function(){
  var TILE_SIZE = 20;
  var ARENA_WIDTH = 32;
  var ARENA_HEIGHT = 24;
  var DOT_RADIUS = TILE_SIZE/12;
  var MIN_ASTEROID_RADIUS = DOT_RADIUS * 4;
  var BULLET_SPEED = 6;
  var BULLET_DURATION = (TILE_SIZE * 12 / BULLET_SPEED);
  var PACMAN_RADIUS = TILE_SIZE / 2;

  var game_canvas_context = document.getElementById("game_canvas").getContext("2d");
  var tick_finished = true;
  var ticks = 0, tick_skips = 0;
  var mousedown = false; 
  var you_base_loc = { x: Math.floor(ARENA_WIDTH / 2), y: Math.floor(ARENA_HEIGHT / 2) };
  var mouse_x = 0, mouse_y = 0;
  var wanted_movement = { x: 0, y: 0 };
  var current_movement = { x: 0, y: 0 }, progress = 0;
  var dots = [];
  var asteroids = [];
  var bullets = [];
  var you_have_lost = false;

  var i, j, x, y;

  var draw_all_four = function(real_x, real_y, draw_func){
    var draw_x, draw_y, which_x, which_y;
    for (which_x = 0; which_x < 2; ++which_x) {
      for (which_y = 0; which_y < 2; ++which_y) {
        draw_x = real_x;
        draw_y = real_y;

        if (which_x === 1) {
          if (draw_x > ARENA_WIDTH * TILE_SIZE / 2) { draw_x -= ARENA_WIDTH * TILE_SIZE; }
          else { draw_x += ARENA_WIDTH * TILE_SIZE; }
        }
        if (which_y === 1) {
          if (draw_y > ARENA_HEIGHT * TILE_SIZE / 2) { draw_y -= ARENA_HEIGHT * TILE_SIZE; }
          else { draw_y += ARENA_HEIGHT * TILE_SIZE; }
        }

        draw_func(draw_x, draw_y);
      }
    }
  };

  var tick = function(){
    var you_movement_angle = 0;
    var mouth_open_angle = 0;
    var you_actual_loc;
    var dx, dy, mag;
    var i, j, x, y;
    game_canvas_context.fillStyle = "black";
    game_canvas_context.fillRect(0,0,640,480);
    if (!you_have_lost) {
      progress += (1/8);
      if (progress >= 1 || (current_movement.x === 0 && current_movement.y === 0)) {
        progress = 0;
        you_base_loc.x += current_movement.x;
        you_base_loc.y += current_movement.y;
        if (you_base_loc.x < 0) you_base_loc.x += ARENA_WIDTH;
        if (you_base_loc.y < 0) you_base_loc.y += ARENA_HEIGHT;
        if (you_base_loc.x >= ARENA_WIDTH) you_base_loc.x -= ARENA_WIDTH;
        if (you_base_loc.y >= ARENA_HEIGHT) you_base_loc.y -= ARENA_HEIGHT;
        current_movement.x = wanted_movement.x;
        current_movement.y = wanted_movement.y;
        if (dots[you_base_loc.x][you_base_loc.y]) {
          dots[you_base_loc.x][you_base_loc.y] = false;
          dx = mouse_x - you_base_loc.x*TILE_SIZE;
          dy = mouse_y - you_base_loc.y*TILE_SIZE;
          mag = Math.sqrt(dx*dx + dy*dy);
          if (mag === 0) { dx = 1; dy = 0; mag = 1; }
          bullets.push({ x: you_base_loc.x*TILE_SIZE, y: you_base_loc.y*TILE_SIZE, vx: dx*BULLET_SPEED/mag, vy: dy*BULLET_SPEED/mag, duration: BULLET_DURATION });
        }
      }
    }
    you_actual_loc = { x: TILE_SIZE*(you_base_loc.x + (current_movement.x * progress)),
                       y: TILE_SIZE*(you_base_loc.y + (current_movement.y * progress)) };

    var move_and_wrap = function(thing){
      thing.x += thing.vx;
      thing.y += thing.vy;
      if (thing.x < 0) thing.x += ARENA_WIDTH*TILE_SIZE;
      if (thing.y < 0) thing.y += ARENA_HEIGHT*TILE_SIZE;
      if (thing.x >= ARENA_WIDTH*TILE_SIZE) thing.x -= ARENA_WIDTH*TILE_SIZE;
      if (thing.y >= ARENA_HEIGHT*TILE_SIZE) thing.y -= ARENA_HEIGHT*TILE_SIZE;
    }
    var intersects = function(loc1, rad1, loc2, rad2) {
      var dx, dy;
      dx = Math.abs(loc1.x - loc2.x);
      if (dx > ARENA_WIDTH*TILE_SIZE/2) { dx = ARENA_WIDTH*TILE_SIZE - dx; }
      dy = Math.abs(loc1.y - loc2.y);
      if (dy > ARENA_HEIGHT*TILE_SIZE/2) { dy = ARENA_HEIGHT*TILE_SIZE - dy; }
      return (dx * dx + dy * dy <= (rad1 + rad2) * (rad1 + rad2));
    }
    for (i = 0; i < asteroids.length; i++) {
      move_and_wrap(asteroids[i]);
    }
    for (i = 0; i < bullets.length; i++) {
      bullets[i].duration--;
      if (bullets[i].duration <= 0) {
        bullets.splice(i, 1);
        i--; // so we don't skip the next bullet 
      }
      else {
        move_and_wrap(bullets[i]);
      }
    }
    for (i = 0; i < bullets.length; i++) {
      for (j = 0; j < asteroids.length; j++) {
        if (intersects(bullets[i], DOT_RADIUS, asteroids[j], asteroids[j].radius)) {
          // blargh... this "function" is just to give me a new scope
          (function(){
            var first_vel_dir;
            var vel_mag;
            if (asteroids[j].radius >= MIN_ASTEROID_RADIUS * 2) {
              first_vel_dir = Math.random() * Math.TAU;
              vel_mag = 1 + Math.random()*2;
              asteroids.push({
                radius: asteroids[j].radius / 2,
                x: asteroids[j].x,
                y: asteroids[j].y,
                vx: asteroids[j].vx + Math.cos(first_vel_dir)*vel_mag,
                vy: asteroids[j].vy + Math.sin(first_vel_dir)*vel_mag,
                });
              asteroids.push({
                radius: asteroids[j].radius / 2,
                x: asteroids[j].x,
                y: asteroids[j].y,
                vx: asteroids[j].vx - Math.cos(first_vel_dir)*vel_mag,
                vy: asteroids[j].vy - Math.sin(first_vel_dir)*vel_mag,
                });
            }
          }());
          asteroids.splice(j, 1);
          bullets.splice(i, 1);
          i--; // so we don't skip the next bullet
          break;
        }
      }
    }
    for (i = 0; i < asteroids.length; i++) {
      if (intersects(you_actual_loc, PACMAN_RADIUS, asteroids[i], asteroids[i].radius)) {
        you_have_lost = true;
      }
    }

    game_canvas_context.fillStyle = "yellow";

    if (current_movement.x > 0) you_movement_angle = 0;
    if (current_movement.y > 0) you_movement_angle = Math.TAU / 4;
    if (current_movement.x < 0) you_movement_angle = Math.TAU / 2;
    if (current_movement.y < 0) you_movement_angle = Math.TAU * 3 / 4;
    mouth_open_angle = 0.5 - Math.abs(progress - 0.5);

    draw_all_four(you_actual_loc.x, you_actual_loc.y, function(draw_x, draw_y){
      var EYE_LENGTH = PACMAN_RADIUS / 4;
      var EYE_DISTANCE = PACMAN_RADIUS / 2.8;
      if (you_have_lost) {
        game_canvas_context.beginPath();
        game_canvas_context.arc(draw_x,draw_y,PACMAN_RADIUS,0,Math.TAU,true);
        game_canvas_context.closePath();
        game_canvas_context.fill();

        game_canvas_context.lineWidth = 1.5;
        game_canvas_context.beginPath();
        game_canvas_context.moveTo(draw_x - EYE_DISTANCE - EYE_LENGTH, draw_y - EYE_DISTANCE - EYE_LENGTH);
        game_canvas_context.lineTo(draw_x - EYE_DISTANCE + EYE_LENGTH, draw_y - EYE_DISTANCE + EYE_LENGTH);
        game_canvas_context.moveTo(draw_x - EYE_DISTANCE - EYE_LENGTH, draw_y - EYE_DISTANCE + EYE_LENGTH);
        game_canvas_context.lineTo(draw_x - EYE_DISTANCE + EYE_LENGTH, draw_y - EYE_DISTANCE - EYE_LENGTH);
        game_canvas_context.moveTo(draw_x + EYE_DISTANCE - EYE_LENGTH, draw_y - EYE_DISTANCE - EYE_LENGTH);
        game_canvas_context.lineTo(draw_x + EYE_DISTANCE + EYE_LENGTH, draw_y - EYE_DISTANCE + EYE_LENGTH);
        game_canvas_context.moveTo(draw_x + EYE_DISTANCE - EYE_LENGTH, draw_y - EYE_DISTANCE + EYE_LENGTH);
        game_canvas_context.lineTo(draw_x + EYE_DISTANCE + EYE_LENGTH, draw_y - EYE_DISTANCE - EYE_LENGTH);
        game_canvas_context.stroke();
      }
      else {
        game_canvas_context.beginPath();
        game_canvas_context.arc(draw_x,draw_y,PACMAN_RADIUS,you_movement_angle + mouth_open_angle,you_movement_angle + Math.TAU - mouth_open_angle,false);
        game_canvas_context.lineTo(draw_x,draw_y);
        game_canvas_context.closePath();
        game_canvas_context.fill();
      }
    });
    for (x = 0; x < ARENA_WIDTH; x++) {
      for (y = 0; y < ARENA_WIDTH; y++) {
        if (dots[x][y]) {
          draw_all_four(x*TILE_SIZE, y*TILE_SIZE, function(draw_x, draw_y){
            game_canvas_context.beginPath();
            game_canvas_context.arc(draw_x,draw_y,DOT_RADIUS,0,Math.TAU,true);
            game_canvas_context.closePath();
            game_canvas_context.fill();
          });
        }
      }
    }
    for (i = 0; i < bullets.length; i++) {
      draw_all_four(bullets[i].x, bullets[i].y, function(draw_x, draw_y){
        game_canvas_context.beginPath();
        game_canvas_context.arc(draw_x, draw_y, DOT_RADIUS, 0, Math.TAU, true);
        game_canvas_context.closePath();
        game_canvas_context.fill();
      });
    }
    game_canvas_context.fillStyle = "gray";
    for (i = 0; i < asteroids.length; i++) {
      draw_all_four(asteroids[i].x, asteroids[i].y, function(draw_x, draw_y){
        game_canvas_context.beginPath();
        game_canvas_context.arc(draw_x, draw_y, asteroids[i].radius, 0, Math.TAU, true);
        game_canvas_context.closePath();
        game_canvas_context.fill();
      });
    }

    if (mousedown) {  
      game_canvas_context.beginPath();
      game_canvas_context.arc(mouse_x,mouse_y,15,0,Math.TAU,true);
      game_canvas_context.closePath();
      game_canvas_context.stroke();
    }
  };

  for (x = 0; x < ARENA_WIDTH; x++) {
    dots[x] = [];
    for (y = 0; y < ARENA_HEIGHT; y++) {
      dots[x][y] = true;
    }
  }

  // blargh... this "function" is just to give me a new scope
  (function(){
    var i, loc_rand, vel_dir, vel_mag, x, y;
    for (i = 0; i < 8; ++i) {
      loc_rand = Math.random() * (ARENA_WIDTH + ARENA_HEIGHT) * TILE_SIZE;
      if (loc_rand < ARENA_WIDTH*TILE_SIZE) {
        x = loc_rand; y = 0;
      }
      else {
        x = 0; y = loc_rand - ARENA_WIDTH*TILE_SIZE;
      }
      vel_dir = Math.random() * Math.TAU;
      vel_mag = Math.random() * 3;
      asteroids.push({
        radius: (Math.random() * 1.2 + 0.7) * TILE_SIZE,
        x: x,
        y: y,
        vx: vel_mag * Math.cos(vel_dir),
        vy: vel_mag * Math.sin(vel_dir),
        });
    }
  }());

  $(document).mousedown(function(){
    mousedown = true;
    return false;
  });
  $(document).mouseup(function(){
    mousedown = false;
    return false;
  });
  $(document).mousemove(function(e){
    var offs = $('#game_canvas').offset();
    mouse_x = e.pageX - offs.left;
    mouse_y = e.pageY - offs.top;
    return false;
  });
  $(document).keydown(function(e){
    var keycode = (e.keyCode ? e.keyCode : e.which);
    var keystr = String.fromCharCode(keycode);
    if (keycode === 37 || keystr === "A") { wanted_movement = { x: -1, y: 0 }; }
    if (keycode === 38 || keystr === "W") { wanted_movement = { x: 0, y: -1 }; }
    if (keycode === 39 || keystr === "D") { wanted_movement = { x: 1, y: 0 }; }
    if (keycode === 40 || keystr === "S") { wanted_movement = { x: 0, y: 1 }; }
    return false;
  });



  (function tickloop(){
    setTimeout(tickloop, Math.floor(1000/30));
    if (tick_finished) {
      tick_finished = false;
      tick();
      tick_finished = true;
      ticks += 1;
    }
    else {
      tick_skips += 1;
    }
    $('#info').html('Info:<br/>Control the pac-man with the arrow keys or WASD. Aim with the mouse. Don\'t get hit by the asteroids.<br/>Ticks: '+ticks+'<br/>Ticks skipped: '+tick_skips);
  }());

});
    </script>''',
      '''<a class="skip" href="#content">Skip to content</a>
      '''+bars.bars_wrap({"games":True}, '''<main>
    <div style="float: left; cursor: crosshair"><canvas id="game_canvas" width="640" height="480">
Your browser does not support the canvas element.
    </canvas></div>
    <p id="info"></p>
  </div>
</main>'''), {}
    )
  )
