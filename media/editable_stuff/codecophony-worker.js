var items;
var stack;

// A wrapper to stop eval() from changing variables local to the codecophony internals
function codecophony_internals_evaluate_script (source) {
  return eval (source);
}

//A wrapper to namespace isolate the codecophony internals from user scripts
var codecophony = (function() {

var sample_rate = 44100;
var evaluate_script = codecophony_internals_evaluate_script;

function message_main (message) {
  self.postMessage (message);
}

function run_script (name) {
  var item = items [name];
  item.began = true;
  stack = {current: name, parent: stack};
  message_main({
    action: "begin_script",
    name: name,
  });
  var success = false;
  try {
    item.result = evaluate_script (item.source);
    success = true;
  } catch (error) {
    self.postMessage ({
      action: "user_error",
      name: name,
      file: error.filename,
      line: error.lineno,
      message: error.message
    });
  }
  message_main({
    action: "finish_script",
    name: name,
    success: success
  });
  item.finished = true;
  stack = stack.parent;
}

function initialize (message) {
  items = message.items;
}

function item_changed (message) {
  var name = message.name;
  var item = message.value;
  items [message.name] = item;
  
  if (item.item_type === "script") {
    run_script (name);
  }
}

var handlers = {
  initialize: initialize,
  item_changed: item_changed,
  run_script: function (message) {
    run_script (message.name);
  },
}

self.onmessage = function (event) {
  handlers [event.data.action] (event.data);
}

function get (name) {
  var item = items [name];
  var result;
  if (item.item_type === "script") {
    if (!item.began) {
      run_script (name, item);
    }
    result = item.result;
  }
  else {
    result = item.data;
  }
  message_main ({
    action: "add_dependency",
    dependent: stack.current,
    dependency: name
  });
  return result;
}
function create (name, value) {
  message_main({
    action: "create_item",
    name: name,
    value: value,
    created_by: stack.current
  });
}

var note_names = ["Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G"];
function semitones_to_note_name (semitones) {
  return note_names [(semitones+1) % 12] + Math.floor (semitones/12).toString();
}

function render_note_default (note) {
  var instrument = get (note.instrument);
  var instrument_samples = instrument [semitones_to_note_name (note.pitch)];
  var duration = Math.floor(note.duration*sample_rate);
  var data = new Float32Array (duration);
  for (var index = 0; index < duration;++index) {
    var cutoff = Math.min (1, (1-(index/sample_rate)/note.duration)*10);
    data [index] = (instrument_samples [index] || 0)*cutoff*note.volume;
  }
  
  return {
    item_type: "sequence",
    // round the start time to an integer so that samples can be combined easier
    start: Math.floor (note.start*sample_rate),
    data: data,
  }
}

function render_note (note) {
  return (note.renderer && get (note.renderer) || render_note_default) (note);
}

function add_sequences (sequences) {
  var min = Infinity;
  var exclusive_max = -Infinity;
  sequences.forEach (function (sequence) {
    min = Math.min (min, sequence.start);
    exclusive_max = Math.max (exclusive_max, sequence.start + sequence.data.length);
  });
  var duration = exclusive_max - min;
  var data = new Float32Array (duration);
  for (var index = 0; index < duration;++index) {
    data [index] = 0;
  }
  sequences.forEach (function (sequence) {
    for (var index = 0; index < sequence.data.length;++index) {
      data [index + sequence.start - min] += sequence.data [index];
    }
  });
  
  return {
    item_type: "sequence",
    start: min,
    data: data,
  }
}

function render_note_array (note_array) {
  var sequences = [];
  note_array.forEach (function (note) {
    sequences.push (render_note (note));
  });
  return add_sequences (sequences);
}

return {get: get, create: create, sample_rate: sample_rate, render_note: render_note, render_note_default: render_note_default, render_note_array: render_note_array, add_sequences: add_sequences};

})();

// Hide the wrapper function
codecophony_internals_evaluate_script = undefined;

// Conveniences for the user
var get = codecophony.get;
var create = codecophony.create;
