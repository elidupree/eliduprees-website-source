$(function(){
"use strict";

var audio = window.audio_context_instance;


var items = {
  random_data:{item_type: "script", source:` create ("demonstration", get ("reed_organ")["C4"]); `}
  
};
var dependencies = {};
var dependents = {};
var worker;

function user_error (message) {
  alert ("user error in codecophony script "+ message.name +": "+ message.file + ":" + message.line + ": " + message.message);
}
function create_item (message) {
  set (message.name, message.value);
  if (message.value instanceof Float32Array) {
    var source =message.value ;
    var buffer = audio.createBuffer (1, source.length, audio.sampleRate);
    buffer.copyToChannel (source, 0, 0);
    draw_recording (create_recording (buffer));
  }
}

var handlers = {
  user_error: user_error,
  create_item: create_item,
  begin_script: function() {},
  finish_script: function() {}
}
function receive_from_worker(event) {
  handlers [event.data.action] (event.data);
}
function error_from_worker (error) {
  alert ("internal error in codecophony worker: "+ error.filename + ":" + error.lineno + ": " + error.message);
}
function restart_worker() {
  if (worker) {
    worker.terminate();
  }
  worker = new Worker ("/media/codecophony-worker.js?rr");
  worker.onmessage = receive_from_worker;
  worker.onerror = error_from_worker;
  message_worker ({
    action: "initialize",
    items: items
  });
  
}
function message_worker (message) {
  if (worker) {worker.postMessage (message);}
}

function remove_dependency(dependent, dependency) {
  delete dependencies [dependent] [dependency];
  delete dependents [dependency] [dependent];
}

function set (name, value) {
  items [name] = value;
  dependents [name] = dependents [name] || {};
  dependencies [name] = dependencies [name] || {};
  var my_dependents = dependents [name];
  message_worker ({
    action: "item_changed",
    name: name,
    value: value
  });
  Object.getOwnPropertyNames(my_dependents).forEach(function (dependent) {
    remove_dependency (dependent, name);
    message_worker ({
      action: "rerun",
      name: dependent,
    });
  });
}

function instrument_URL (name) {
  return 'https://gleitz.github.io/midi-js-soundfonts/MusyngKite/' + name + '-ogg.js';
}

function fetch(url,type){return new Promise(function(done,reject){var req=new XMLHttpRequest;if(type)req.responseType=type;req.open("GET",url);req.onload=function(){req.status===200?done(req.response):reject(Error(req.statusText))};req.onerror=function(){reject(Error("Network Error"))};req.send()})}


//restart_worker();

loadAudio (instrument_URL ("reed_organ"), {fetch: fetch, context: audio}).then (function (buffers) {
  
  var converted = {};
  Object.getOwnPropertyNames(buffers).forEach(function (note) {
    converted [note] = buffers [note].getChannelData(0);
  });
  set ("reed_organ", {item_type: "instrument", data: converted});
  
restart_worker();
});



function draw_codecophony() {
  requestAnimationFrame (draw_codecophony);
  
  
}
draw_codecophony();

});
