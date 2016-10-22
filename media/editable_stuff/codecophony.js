$(function(){
"use strict";


initialize_voice_practice_tool ({
  recording_created: function (recording) {
    initialize_source_recording (recording);
  },
  recording_changed: function (recording) {
    items [recording.codecophony_interface.project_entry.name] = recording.buffer.getChannelData (0);
  },
  recording_finished: function (recording) {
    var UI_stuff = recording.codecophony_interface;
    var name = UI_stuff.project_entry.name;
    save (UI_stuff.project_entry.id, items [name]);
    set (name, items [name]);
    console.log(project, items, UI_stuff);
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

var adjectives = "palpable, terrible, awesome, extreme, tragic, lamentable, radical, exploratory, sesquipedalian, despicable, proud, clever, subtle, shining, structural, perforated, triumphant, understandable, malicious, dreaded infinite, relaxed confident complete ambitious logical intuitive insightful eloquent efficient quick yucky unstoppable optimal angry factual altruistic good helpful justified kinesthetic complicated vivacious liminal persistent invincible virtual vivid unstable bounded unbounded preventative iterative burning tentative novel countable dramatic flexible sensory modified modular momentary ethical automatic mundane formalized explicit evaluated incorrect reasonable pragmatic responsible determined complementary prompt adequate sufficient necessary required local straightforward enthusiastic useful mythological philosophical derived precise superficial vindictive counterintuitive idiosyncratic, immediate"
var nouns = "doom, destiny, phlogiston, visitor archway doorway wizard device liberation knowledge justice solution hypothesis question description poise persona movement sphere source destination comprehension system design specification clarity choices assertion warning story will imagination prediction regret transcendence despair kilometer label zenith xenophobia calamity vision exception vehicle verification accomplishment viewpoint reality evolution revolution transformation enjoyment barrier code principle ideology being entity number defiance mischief control decision mapping visualization resolution maintenance magic category instance measurement consideration ingenuity removal quantity pattern inference labor performance realization reference injustice safety cycle route process structure truth nanosecond challenge investigation sarcasm judgment omnipotence opportunity ordering diffusion substance overflow focus"
adjectives = adjectives.split(/[\s,]+/);
nouns = nouns.split(/[\s,]+/);
console.log ("Adjectives available: " + adjectives.length);
console.log ("Nouns available: " + nouns.length);

var items;// = {};
var dependencies;// = {};
var dependents;// = {};
var interfaces;// = {};
var project_id;
var project;
var project_list;
var worker_port;
var sandbox_port;
var sandbox_remote_port;
var worker_script;
var lodash_script;
var sandbox_initialized;
var last_heard_from_worker;
var last_started_script;
var database;

(function(){
  var request = indexedDB.open("codecophony", 2);
  request.onerror = function (event) {
  
  };
  request.onsuccess = function (event) {
    database = event.target.result;
    load ("project_list", function (p) {
      project_list = p || [];
      project_list.forEach(function(id) {
        load (id, function (project) {
          if (project) {
            add_project_selection (id, project);
          }
          else {
            console.log ("Warning: deleting list entry for nonexistent project " + id);
            project_list = project_list.filter (function (other_id) {return other_id !== id;});
            save ("project_list", project_list);
          }
        });
      });
    });
  };
  request.onupgradeneeded = function (event) {
    var database = event.target.result;
    database.createObjectStore ("files", {keyPath: "id"});
  }
})();

function save (id, data, onsuccess) {
  database.transaction (["files"], "readwrite").objectStore ("files").put ({id: id, data: data}).onsuccess = onsuccess;
}
function load (id, onload) {
  database.transaction (["files"]).objectStore ("files").get (id).onsuccess = function (event) {
    onload(event.target.result && event.target.result.data);
  };
}

var sandbox = $("#sandbox").on ("load", function (event) {
  var channel = new MessageChannel();
  sandbox_port = channel.port1;
  sandbox_remote_port = channel.port2;
  initialize_sandbox ();
}) [0];

function initialize_sandbox () {
  if (lodash_script && worker_script && sandbox_port && !sandbox_initialized) {
    sandbox.contentWindow.postMessage ({action:"initialize", worker_script: lodash_script+"\n"+worker_script}, "*", [sandbox_remote_port]);
    sandbox_port.onmessage = function (event) {
      error_from_worker (event.data);
    };
    sandbox_initialized = true;
  }
}

$.get ("/media/codecophony-worker.js?rr", function (script) {
  worker_script = script;
  initialize_sandbox ();
});
$.get ("/media/lodash.js?rr", function (script) {
  lodash_script = script;
  initialize_sandbox ();
});

function generate_id() {
  function display (u32) {return ("0000000" + u32.toString (16)).substr (-8);}
  var array = new Uint32Array (4);
  window.crypto.getRandomValues (array);
  return display (array [0]) + display (array [1]) + display (array [2]) + display (array [3]);
}
function generate_name() {
  return adjectives [Math.floor (Math.random()*adjectives.length)]+"_"+ nouns [Math.floor (Math.random()*nouns.length)];
}
function generate_item_name() {
  var name;
  while (!name || items [name]) {
    name = generate_name();
  }
  return name;
}

$(".project_select").append ($("<button>").text ("new project").click (function() {new_project ();}));

function add_project_selection (id, project) {
  var name_input = $('<input type="text">').val(project.name).on ("input", function (event) {
    project.name = name_input.val();
  });
  var edit_button = $("<button>").text ("edit").click (function() {load_project (id);});

  $(".project_select").append (name_input, edit_button);
}

function new_project () {
  var id = generate_id();
  var project = {
    name: generate_name(),
    entries: [],
  };
  add_project_selection (id, project);
  project_list.push (id);
  save ("project_list", project_list);
  save (id, project);
}

function load_project (new_project_id) {
  if (!(database && sandbox_initialized)) {return;}
  project_id = new_project_id;
  items = {};
  dependencies = {};
  dependents = {};
  interfaces = {};
  
  load (project_id, function (p) {
   project = p;
   project.entries.forEach(function(entry) {
    
    if (entry.entry_type === "midijs_soundfont_instrument") {
      load_instrument_item (entry);
    }
    else {
      load (entry.id, function (item) {
        if (item) {
          if (item.item_type == "script") {
            create_script (entry.name, item.source);
            interfaces [entry.name].project_entry = entry;
          }
          else {
            set (entry.name, item);
            interfaces [entry.name].project_entry = entry;
            if (item instanceof Float32Array) {
              var buffer = audio.createBuffer (1, item.length, audio.sampleRate);
              buffer.copyToChannel (item, 0, 0);
              var UI_stuff = interfaces [entry.name];
              var recording = voice_practice_tool.create_recording (buffer, true);
              recording.codecophony_interface = UI_stuff;
              create_source_recording_UI (recording);
              voice_practice_tool.draw_recording (recording);
            }
          }
        }
      });
    }
   });
   
  });
  $(".project_editor").show();
  $(".project_select").hide();
  restart_worker();
}
function unload_project () {
  Object.getOwnPropertyNames(interfaces).forEach(function (name) {
    var UI_stuff = interfaces [name];
    if (UI_stuff.element) {
      UI_stuff.element.detach();
    }
  });

  items = undefined;
  dependencies = undefined;
  dependents = undefined;
  interfaces = undefined;
  project = undefined;
  project_id = undefined;
  
  $(".project_editor").hide();
  $(".project_select").show();
}

function instrument_URL (name) {
  return 'https://gleitz.github.io/midi-js-soundfonts/MusyngKite/' + name + '-ogg.js';
}

function fetch(url,type){return new Promise(function(done,reject){var req=new XMLHttpRequest;if(type)req.responseType=type;req.open("GET",url);req.onload=function(){req.status===200?done(req.response):reject(Error(req.statusText))};req.onerror=function(){reject(Error("Network Error"))};req.send()})}
    
function load_instrument_item (entry) {
      loadAudio (entry.URL, {fetch: fetch, context: audio}).then (function (buffers) {
        var converted = {};
        Object.getOwnPropertyNames(buffers).forEach(function (note) {
          converted [note] = buffers [note].getChannelData(0);
        });
        set (entry.name, {item_type: "midijs_soundfont_instrument", data: converted});
        interfaces [entry.name].project_entry = entry;
        var element = interfaces [entry.name].element = $(`<div class="item">Imported instrument: ${entry.name}</div>`)
        $(".codecophony_instruments").append (element);
      });
}




function awaiting_script (name) {
  interfaces [name].status = "awaiting";
  if (!interfaces [name].running) {
    interfaces [name].error_display.text ("Waiting to be run ...");
  }
}
function begin_script (name) {
  last_started_script = name;
  interfaces [name].running = true;
  if (interfaces [name].status === "set_to_run") {
    interfaces [name].status = "properly_running";
    interfaces [name].error_display.text ("Running...");
  }
}
function finish_script (name, success) {
  if (interfaces [name].status === "properly_running") {
    interfaces [name].status = "finished";
    if (success) {interfaces [name].error_display.append ("\nCompleted successfully");}
  }
  if (interfaces [name].running) {
    interfaces [name].running = false;
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
  interfaces [name] = interfaces [name] || {};
  
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
          var recording = voice_practice_tool.create_recording (buffer, true);
          element.append (recording.element);
          voice_practice_tool.draw_recording (recording);
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
  UI_stuff.project_entry.name = new_name;
  save (project_id, project);
  interfaces [new_name] = UI_stuff;
  set (new_name, item);
}


function create_source_recording_UI (recording) {
  var UI_stuff = recording.codecophony_interface;
  var name_input = UI_stuff.name_input = $('<input type="text">').val(UI_stuff.project_entry.name).on ("input", function (event) {
    UI_stuff.changed_name_to = name_input.val();
    UI_stuff.changed_at = Date.now();
  });
  var error_display = UI_stuff.error_display = $("<div>");
  recording.element.prepend (name_input).append (error_display);
  
  UI_stuff.element = recording.element;
  $(".recordings").append (recording.element);
}

function initialize_source_recording (recording) {
  var name = generate_item_name();

  var UI_stuff = interfaces [name] || {};
  interfaces [name] = UI_stuff;
  recording.codecophony_interface = UI_stuff;
  
  set (name, recording.buffer.getChannelData(0));
  
  UI_stuff.project_entry = {entry_type: "recording", id: generate_id(), name: name,};
  project.entries.push (UI_stuff.project_entry);
  save (project_id, project);
  create_source_recording_UI (recording);
}

function create_script (name, initial_source, add_to_project) {
  var UI_stuff = interfaces [name] || {};
  interfaces [name] = UI_stuff;
  var script_box = UI_stuff.element = $('<div class="item">').addClass("script_box");
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
  script_box.append ("Script name: ", name_input).append (script_input).append (error_display);
  $(".codecophony_scripts").append (script_box);
  
  var item = {item_type: "script", source: initial_source};
  set (name, item);
  
  if (add_to_project) {
    UI_stuff.project_entry = {entry_type: "script", id: generate_id(), name: name,};
    project.entries.push (UI_stuff.project_entry);
    save (project_id, project);
    save (UI_stuff.project_entry.id, item);
  }
}
function create_script_from_UI () {
  create_script (generate_item_name(), "", true);
}

var codecophony_box = $("<div>");
$(".codecophony_space").append (codecophony_box);
var new_script_button = $("<button>").text ("New script").click (create_script_from_UI);

var unload_project_button = $("<button>").text ("Quit to project-selection screen").click (unload_project);

var instrument_importer = $('<select class="import_instruments"> <option>Import instruments…</option></select>').on ("input", function() {
  var instrument = instrument_importer.val();
  if (instrument && !items [instrument]) {
    var entry = {
      entry_type: "midijs_soundfont_instrument",
      URL: instrument_URL (instrument),
      name: instrument,
    };
    project.entries.push (entry);
    save (project_id, project);
    load_instrument_item (entry);
  }
});

codecophony_box.append (new_script_button,unload_project_button,instrument_importer);
$(".codecophony_space").append ($('<div class="codecophony_instruments">'));
$(".codecophony_space").append ($('<div class="codecophony_scripts">'));



$.get ("https://gleitz.github.io/midi-js-soundfonts/MusyngKite/names.json", function (something) {
  something.forEach(function(name) {
    instrument_importer.append ($(`<option value="${name}">${name}</option>`));
  });
});

/*create_script ("example_script", `
var notes = codecophony.scrawl (
  "with instrument reed_organ pitch 0 duration 0.25 play 0 then 2 then 3 then 5 then 7 lasting 4"
)
create ("example_notes", notes);
create ("example_sequence", codecophony.render_note_array (notes));
`);
create_script ("example_copier", `
  create ("example_notes_copy", get ("example_notes"));
`);*/

function draw_codecophony() {
  requestAnimationFrame (draw_codecophony);
  
  if (!items) {return;}
  var anything_running = false;
  var anything_set_to_run = false;
  var item_names = Object.getOwnPropertyNames (items);
  item_names.forEach (function (name) {
    var UI_stuff = interfaces [name];
    
    if (UI_stuff.changed_at && Date.now() > UI_stuff.changed_at + 1000) {
      if (UI_stuff.changed_to) {
        var item = {item_type: "script", source: UI_stuff.changed_to};
        set (name, item);
        save (UI_stuff.project_entry.id, item);
        delete UI_stuff.changed_to;
      }
      if (UI_stuff.changed_name_to) {
        if (items [UI_stuff.changed_name_to]) {
          UI_stuff.error_display.text ("Error: another item already has the same name");
          UI_stuff.name_input.val (UI_stuff.project_entry.name);
        } else {
          rename_item (name, UI_stuff.changed_name_to);
        }
        delete UI_stuff.changed_name_to;
      }
      delete UI_stuff.changed_at;
    }
    
    if (UI_stuff.running) {
      anything_set_to_run = true;
      anything_running = true;
    }
    else if (UI_stuff.status === "set_to_run") {
      anything_set_to_run = true;
    }
  });
  
  // items could have been renamed
  item_names = Object.getOwnPropertyNames (items);
  
  if (anything_running) {
    if (Date.now() > last_heard_from_worker + 10000) {
      item_names.forEach (function (name) {
        if (interfaces [name].running) {
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
          interfaces [name].error_display.text ("Sending to worker thread…");
          anything_set_to_run = true;
        }
      }
    });
  }
}
draw_codecophony();

});
