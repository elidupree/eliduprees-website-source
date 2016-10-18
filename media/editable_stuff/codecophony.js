$(function(){
"use strict";

var audio = window.audio_context_instance;


var items = {
  //random_data:{item_type: "script", source:` create ("demonstration", get ("reed_organ")["C4"]); `}
  /*random_data:{item_type: "script", source:`
    create ("foo", codecophony.render_note ({
      instrument: "reed_organ",
      volume: 1,
      pitch: 51,
      start: 0,
      duration: 1,
    }));
  `}*/
};
var dependencies = {};
var dependents = {};
var interfaces = {};
var worker;
var last_heard_from_worker;
var last_started_script;

function awaiting_script (name) {
  interfaces [name].status = "awaiting";
  interfaces [name].error_display.text ("waiting to be run ...");
}
function begin_script (name) {
  last_started_script = name;
  if (interfaces [name].status === "set_to_run") {
    interfaces [name].status = "running";
    interfaces [name].error_display.text ("running...");
  }
}
function finish_script (name, success) {
  if (interfaces [name].status === "running") {
    interfaces [name].status = "finished";
    if (success) {interfaces [name].error_display.text ("Completed successfully");}
  }
  Object.getOwnPropertyNames(dependents [name]).forEach(function (dependent) {
    if (interfaces [name].status === "finished") {
      remove_dependency (dependent, name);
      awaiting_script (dependent);
    }
  });
}
function user_error (message) {
  //alert ("user error in codecophony script "+ message.name +": "+ message.file + ":" + message.line + ": " + message.message);
  interfaces [message.name].error_display.text ("Error: " + message.message);
}
function create_item (message) {
  set (message.name, message.value);
}

var handlers = {
  user_error: user_error,
  create_item: create_item,
  begin_script: function(message) {
    begin_script (message.name);
  },
  finish_script: function(message) {
    finish_script (message.name, message.success);
  },
  add_dependency: function (message) {
    add_dependency (message.dependent, message.dependency);
  },
}
function receive_from_worker(event) {
  last_heard_from_worker = Date.now();
  handlers [event.data.action] (event.data);
}
function error_from_worker (error) {
  last_heard_from_worker = Date.now();
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
  last_heard_from_worker = Date.now();
}
function message_worker (message) {
  if (worker) {worker.postMessage (message); return true;}
}

function add_dependency(dependent, dependency) {
  dependencies [dependent] [dependency] = true;
  dependents [dependency] = dependents [dependency] || {};
  dependents [dependency] [dependent] = true;
}
function remove_dependency(dependent, dependency) {
  delete dependencies [dependent] [dependency];
  delete dependents [dependency] [dependent];
}

function set (name, value) {
  items [name] = value;
  dependents [name] = dependents [name] || {};
  dependencies [name] = dependencies [name] || {};
  interfaces [name] = interfaces [name] || {};
  
  if (value.item_type === "sequence") {
    var source = value.data;
    var buffer = audio.createBuffer (1, source.length, audio.sampleRate);
    buffer.copyToChannel (source, 0, 0);
    if (interfaces [name].recording) {
      replace_recording (interfaces [name].recording, buffer);
    } else {
      interfaces [name].recording = create_recording (buffer);
    }
    draw_recording (interfaces [name].recording);
  }
  
  var my_dependents = dependents [name];
  message_worker ({
    action: "item_changed",
    name: name,
    value: value
  });
  if (value.item_type === "script" && value.source !== "") {
    awaiting_script (name);
  }
  Object.getOwnPropertyNames(my_dependents).forEach(function (dependent) {
    remove_dependency (dependent, name);
    awaiting_script (dependent);
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

function create_script (name, initial_source) {
  interfaces [name] = interfaces [name] || {};
  var script_box = $("<div>").text (name);
  var script_input = $('<textarea rows="10" cols="80">').text (initial_source).on ("input", function (event) {
    interfaces [name].changed_to = script_input.val();
    interfaces [name].changed_at = Date.now();
    error_display.text ("waiting for you to finish typing...");
  });
  var error_display = $("<div>");
  interfaces [name].error_display = error_display;
  script_box.append (script_input).append (error_display);
  $(".codecophony_space").append (script_box);
  set (name, {item_type: "script", source: initial_source});
}

var codecophony_box = $("<div>");
$(".codecophony_space").append (codecophony_box);
var new_script_button = $("<button>").text ("new script").click (function (event) {
  var name = new_script_name_input.val();
  if (name !== "" && !items [name]) {
    create_script (name, "");
  }
});
codecophony_box.append (new_script_button);
var new_script_name_input = $('<input type="text">').change (function (event) {});
codecophony_box.append (new_script_name_input);


create_script ("example_script", `
  create ("example_output", codecophony.render_note_array (codecophony.scrawl (
    "with instrument reed_organ pitch 0 duration 0.25 play 0 then 2 then 3 then 5 then 7 lasting 4"
  )));
`);

function draw_codecophony() {
  requestAnimationFrame (draw_codecophony);
  
  var anything_running = false;
  var anything_set_to_run = false;
  var item_names = Object.getOwnPropertyNames (items);
  item_names.forEach (function (name) {
    if (interfaces [name].status === "running") {
      anything_set_to_run = true;
      anything_running = true;
    }
    if (interfaces [name].status === "set_to_run") {
      anything_set_to_run = true;
    }
    if (interfaces [name].changed_at && Date.now() > interfaces [name].changed_at + 1000) {
      set (name, {item_type: "script", source: interfaces [name].changed_to});
      delete interfaces [name].changed_at;
      delete interfaces [name].changed_to;
    }
  });
  if (anything_running) {
    if (Date.now() > last_heard_from_worker + 10000) {
      item_names.forEach (function (name) {
        if (interfaces [name].status === "running") {
          if (last_started_script === name) {
            interfaces [name].error_display.text ("Error: timed out");
          }
          else {
            interfaces [name].error_display.text ("Couldn't finish because "+ last_started_script +" timed out");
          }
          finish_script (name, false);
        }
      });
    }
  }
  if (!anything_set_to_run) {
    item_names.forEach (function (name) {
      if (interfaces [name].status === "awaiting" && !anything_set_to_run) {
        if (message_worker ({
          action: "run_script",
          name: name,
        })){
          interfaces [name].status = "set_to_run";
          anything_set_to_run = true;
        }
      }
    });
  }
}
draw_codecophony();

});
