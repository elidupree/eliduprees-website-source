$(function(){
"use strict";

var audio = window.audio_context_instance;


var items = {
  random_data:"",
}
var dependencies = {}
var dependents = {}
var worker;

function receive_from_worker(event) {
  
}
function restart_worker() {
  if (worker) {
    worker.terminate();
  }
  worker = new Worker ("/media/codecophony-worker.js?rr");
  worker.onmessage = receive_from_worker;
  worker.postMessage ({
    action: "initialize",
    items: items
  });
  
}

function remove_dependency(dependent, dependency) {
  delete dependencies [dependent] [dependency];
  delete dependents [dependency] [dependent];
}

function set (id, value) {
  items [id] = value;
  var dependents = dependents [id];
  message_worker ({
    action: "item_changed",
    id: id,
    value: value
  });
  dependents.getOwnPropertyNames().forEach(function (dependent) {
    remove_dependency (dependent, id);
    message_worker ({
      action: "rerun",
      id: dependent,
      value: value,
    });
  });
}

function instrument_URL (name) {
  return 'https://gleitz.github.io/midi-js-soundfonts/MusyngKite/' + name + '-ogg.js';
}

function fetch(url,type){return new Promise(function(done,reject){var req=new XMLHttpRequest;if(type)req.responseType=type;req.open("GET",url);req.onload=function(){req.status===200?done(req.response):reject(Error(req.statusText))};req.onerror=function(){reject(Error("Network Error"))};req.send()})}
loadAudio (instrument_URL ("reed_organ"), {fetch: fetch, context: audio}).then (function (buffers) {
  draw_recording (create_recording (buffers ["C4"]));
});



function draw_codecophony() {
  requestAnimationFrame (draw_codecophony);
  
  
}
draw_codecophony();

});
