$(function(){
"use strict";


initialize_voice_practice_tool ({
  recording_created: function (recording) {
    initialize_source_recording (recording);
  },
  recording_changed: function (recording) {
    items [recording.codecophony_interface.name].data = recording.buffer.getChannelData (0);
  },
  recording_finished: function (recording) {
    var name = recording.codecophony_interface.name;
    set (name, items [name]);
  },
  sizes: function() {
    var width = $("body").width();
    var height = $("body").height();
    return {
      recent_magnitudes_width: Math.ceil (Math.min (width/4, 256)),  
      recent_magnitudes_height: Math.min (height/6, 128),
      histogram_width: Math.min (width/4, 256),
      histogram_height: Math.min (height/6, 128),
    }
  },
});

var audio = voice_practice_tool.audio;

var adjectives = "palpable, terrible, awesome, extreme, tragic, lamentable, radical, exploratory, sesquipedalian, despicable, proud, clever, subtle, shining, structural, perforated, triumphant, understandable, malicious, dreaded infinite, relaxed confident complete ambitious logical intuitive insightful eloquent efficient quick yucky unstoppable optimal angry factual altruistic good helpful justified kinesthetic complicated vivacious liminal persistent invincible virtual vivid unstable bounded unbounded preventative iterative burning tentative novel countable dramatic flexible sensory modified modular momentarily ethical automatic mundane formalized explicit evaluated incorrect reasonable pragmatic responsible determined complementary prompt adequate sufficient necessary required local straightforward enthusiastic useful mythological philosophical derived precise superficial vindictive counterintuitive idiosyncratic"
var nouns = "doom, destiny, phlogiston, visitor archway doorway wizard device liberation knowledge justice solution hypothesis question description poise persona movement sphere source destination comprehension system design specification clarity choices assertion warning story will imagination prediction regret transcendence despair kilometer label zenith xenophobia calamity vision exception vehicle verification accomplishment viewpoint reality evolution revolution transformation enjoyment barrier code principle ideology being entity number defiance mischief control decision mapping visualization resolution maintenance magic category instance measurement consideration ingenuity removal quantity pattern inference labor performance realization reference injustice safety cycle route process structure truth nanosecond challenge investigation sarcasm judgment omnipotence opportunity ordering diffusion substance overflow focus"
adjectives = adjectives.split(/[\s,]+/);
nouns = nouns.split(/[\s,]+/);
console.log ("Adjectives available: " + adjectives.length);
console.log ("Nouns available: " + nouns.length);

var items = {};
var dependencies = {};
var dependents = {};
var interfaces = {};
var worker_port;
var sandbox_port;
var sandbox_remote_port;
var worker_script;
var sandbox_initialized;
var last_heard_from_worker;
var last_started_script;

var sandbox = $("#sandbox").on ("load", function (event) {
  var channel = new MessageChannel();
  sandbox_port = channel.port1;
  sandbox_remote_port = channel.port2;
  initialize_sandbox ();
}) [0];

function initialize_sandbox () {
  if (worker_script && sandbox_port && !sandbox_initialized) {
    sandbox.contentWindow.postMessage ({action:"initialize", worker_script: worker_script}, "*", [sandbox_remote_port]);
    sandbox_port.onmessage = function (event) {
      error_from_worker (event.data);
    };
    sandbox_initialized = true;
    restart_worker();
  }
}

$.get ("/media/codecophony-worker.js?rr", function (script) {
  worker_script = script;
  initialize_sandbox ();
});

function awaiting_script (name) {
  interfaces [name].status = "awaiting";
  interfaces [name].error_display.text ("Waiting to be run ...");
}
function begin_script (name) {
  last_started_script = name;
  if (interfaces [name].status === "set_to_run") {
    interfaces [name].status = "running";
    interfaces [name].error_display.text ("Running...");
  }
}
function finish_script (name, success) {
  if (interfaces [name].status === "running") {
    interfaces [name].status = "finished";
    if (success) {interfaces [name].error_display.append ("\nCompleted successfully");}
  }
  Object.getOwnPropertyNames(dependents [name]).forEach(function (dependent) {
    if (interfaces [name].status === "finished") {
      remove_dependency (dependent, name);
      awaiting_script (dependent);
    }
  });
}
function user_warning (message) {
  interfaces [message.name].error_display.append ("\nWarning: " + message.message);
}
function user_error (message) {
  interfaces [message.name].error_display.append ("\nError: " + message.message);
}
function create_item (message) {
  set (message.name, message.value, true);
}

var handlers = {
  user_error: user_error,
  user_warning: user_warning,
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
  alert ("internal error in codecophony worker: "+ error.message);
}
function restart_worker() {
  /*if (worker) {
    worker.terminate();
  }
  worker = new Worker ("/media/codecophony-worker.js?rr");
  worker.onmessage = receive_from_worker;
  worker.onerror = error_from_worker;*/
  if (sandbox_initialized) {
    var channel = new MessageChannel();
    worker_port = channel.port1;
    sandbox.contentWindow.postMessage ({action:"restart_worker"}, "*", [channel.port2]);
    message_worker ({
      action: "initialize",
      items: items
    });
    last_heard_from_worker = Date.now();
    worker_port.onmessage = receive_from_worker;
  }
}
function message_worker (message) {
  if (worker_port) {worker_port.postMessage (message); return true;}
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

function invalidate_dependencies (name) {
  Object.getOwnPropertyNames(dependents [name]).forEach(function (dependent) {
    remove_dependency (dependent, name);
    awaiting_script (dependent);
  });
}

function set (name, value, generated) {
  items [name] = value;
  dependents [name] = dependents [name] || {};
  dependencies [name] = dependencies [name] || {};
  interfaces [name] = interfaces [name] || {name: name};
  
  if (generated) {
    if (interfaces [name].element) {
      interfaces [name].element.detach();
    }
    var element = interfaces [name].element = $('<div class="item">');
    element.prepend ($("<div>").text (name));
    var notes = [];
    function display (input) {
      if (typeof input === "object") {
        if (typeof input.pitch === "number" && typeof input.start === "number" && typeof input.duration === "number") {
          notes.push (input);
        }
        else if (input instanceof Float32Array && input.length >0) {
          var buffer = audio.createBuffer (1, input.length, audio.sampleRate);
          buffer.copyToChannel (input, 0, 0);
          var UI_stuff = interfaces [name];
          UI_stuff.recording = voice_practice_tool.create_recording (buffer, true);
          element.append (UI_stuff.recording.element);
          voice_practice_tool.draw_recording (UI_stuff.recording);
        }
        else {
          Object.getOwnPropertyNames (input).forEach(function(index) {
            display (input[index]);
          });
        }
      }
    }
    display (value);
    if (notes.length >0) {
      var notes_element = $('<canvas>');
      element.append (notes_element);
      var context = notes_element [0].getContext ("2d");
      
      var min_pitch = Infinity;
      var max_pitch = - Infinity;
      var min_time = Infinity;
      var max_time = - Infinity;
      notes.forEach(function(note) {
        min_pitch = Math.min (min_pitch, note.pitch);
        max_pitch = Math.max (max_pitch, note.pitch);
        min_time = Math.min (min_time, note.start);
        max_time = Math.max (max_time, note.start + note.duration);
      });
      var width = 200;
      var height = 100;
      var semitone_height = height/(1 + max_pitch - min_pitch);
      notes_element.attr ("width", width).attr ("height", height);
      context.fillStyle = "rgb(255, 0, 0)";
      function X (time) {return width*(time - min_time)/(max_time - min_time);}
      notes.forEach(function(note) {
        var start = X (note.start);
        context.fillRect (start, height - semitone_height*(1+note.pitch - min_pitch), X (note.start + note.duration) - start, semitone_height);
      });
    }
    $(".generated").append (element);
    
  }
  
  message_worker ({
    action: "item_changed",
    name: name,
    value: value
  });
  if (value && value.item_type === "script" && value.source !== "") {
    awaiting_script (name);
  }
  invalidate_dependencies (name);
}

function remove_item (name) {
  var result = items [name];
  if (result) {
    message_worker ({
      action: "item_changed",
      name: name,
      value: value
    });
  }
  invalidate_dependencies (name);
  Object.getOwnPropertyNames(dependencies [name]).forEach(function (dependency) {
    remove_dependency (name, dependency);
  });
  if (interfaces [name].element) {
    interfaces [name].element.detach();
  }
  delete dependencies [name];
  delete dependents [name];
  delete items [name];
  return result;
}

function rename_item (name, new_name) {
  var UI_stuff = interfaces [name];
  var item = remove_item (name);
  delete interfaces [name];
  UI_stuff.name = new_name;
  interfaces [new_name] = UI_stuff;
  set (new_name, item);
}

function instrument_URL (name) {
  return 'https://gleitz.github.io/midi-js-soundfonts/MusyngKite/' + name + '-ogg.js';
}

function fetch(url,type){return new Promise(function(done,reject){var req=new XMLHttpRequest;if(type)req.responseType=type;req.open("GET",url);req.onload=function(){req.status===200?done(req.response):reject(Error(req.statusText))};req.onerror=function(){reject(Error("Network Error"))};req.send()})}

loadAudio (instrument_URL ("reed_organ"), {fetch: fetch, context: audio}).then (function (buffers) {
  var converted = {};
  Object.getOwnPropertyNames(buffers).forEach(function (note) {
    converted [note] = buffers [note].getChannelData(0);
  });
  set ("reed_organ", {item_type: "midijs_soundfont_instrument", data: converted});
});

function initialize_source_recording (recording) {
  var name;
  while (!name || items [name]) {
    name = adjectives [Math.floor (Math.random()*adjectives.length)]+"-"+ nouns [Math.floor (Math.random()*nouns.length)];
  }
  var UI_stuff = interfaces [name] || {name: name};
  interfaces [name] = UI_stuff;
  recording.codecophony_interface = UI_stuff;
  
  set (name, recording.buffer.getChannelData(0));
  $(".recordings").append (recording.element);
  
  var name_input = UI_stuff.name_input = $('<input type="text">').val(name).on ("input", function (event) {
    UI_stuff.changed_name_to = name_input.val();
    UI_stuff.changed_at = Date.now();
  });
  var error_display = UI_stuff.error_display = $("<div>");
  recording.element.prepend (name_input).append (error_display);
}
function create_script (name, initial_source) {
  var UI_stuff = interfaces [name] || {name: name};
  interfaces [name] = UI_stuff;
  var script_box = $('<div class="item">').addClass("script_box");
  var name_input = UI_stuff.name_input = $('<input type="text">').val(name).on ("input", function (event) {
    UI_stuff.changed_name_to = name_input.val();
    UI_stuff.changed_at = Date.now();
  });
  var script_input = $('<textarea rows="6" cols="80">').text (initial_source).on ("input", function (event) {
    UI_stuff.changed_to = script_input.val();
    UI_stuff.changed_at = Date.now();
    error_display.text ("waiting for you to finish typing...");
  });
  var error_display = UI_stuff.error_display = $("<pre>");
  script_box.append (name_input).append (script_input).append (error_display);
  $(".codecophony_space").append (script_box);
  set (name, {item_type: "script", source: initial_source});
}
function create_script_UI () {
  var name = new_script_name_input.val();
  if (name !== "" && !items [name]) {
    create_script (name, "");
  }
}

var codecophony_box = $("<div>");
$(".codecophony_space").append (codecophony_box);
var new_script_button = $("<button>").text ("new script").click (create_script_UI);
codecophony_box.append (new_script_button);
var new_script_name_input = $('<input type="text">').keyup(function (event) {
  if (event.keyCode == 13) {
    create_script_UI();
  }
});
codecophony_box.append (new_script_name_input);



create_script ("example_script", `
var notes = codecophony.scrawl (
  "with instrument reed_organ pitch 0 duration 0.25 play 0 then 2 then 3 then 5 then 7 lasting 4"
)
create ("example_notes", notes);
create ("example_sequence", codecophony.render_note_array (notes));
`);
create_script ("example_copier", `
  create ("example_notes_copy", get ("example_notes"));
`);

function draw_codecophony() {
  requestAnimationFrame (draw_codecophony);
  
  var anything_running = false;
  var anything_set_to_run = false;
  var item_names = Object.getOwnPropertyNames (items);
  item_names.forEach (function (name) {
    var UI_stuff = interfaces [name];
    
    if (UI_stuff.changed_at && Date.now() > UI_stuff.changed_at + 1000) {
      if (UI_stuff.changed_to) {
        set (name, {item_type: "script", source: UI_stuff.changed_to});
        delete UI_stuff.changed_to;
      }
      if (UI_stuff.changed_name_to) {
        if (items [UI_stuff.changed_name_to]) {
          UI_stuff.error_display.text ("Error: another item already has the same name");
          UI_stuff.name_input.val (UI_stuff.name);
        } else {
          rename_item (name, UI_stuff.changed_name_to);
        }
        delete UI_stuff.changed_name_to;
      }
      delete UI_stuff.changed_at;
    }
    
    if (UI_stuff.status === "running") {
      anything_set_to_run = true;
      anything_running = true;
    }
    if (UI_stuff.status === "set_to_run") {
      anything_set_to_run = true;
    }
  });
  
  // items could have been renamed
  item_names = Object.getOwnPropertyNames (items);
  
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
      restart_worker();
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
