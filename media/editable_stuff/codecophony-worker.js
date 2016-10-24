// A wrapper to stop eval() from changing variables local to the codecophony internals
function codecophony_internals_evaluate_script (source) {
  var items = new Proxy ({},{
    get: function (target, property, receiver) {
      return codecophony.get (property);
    },
    set: function (target, property, value, receiver) {
      return codecophony.create (property, value);
    },
  });
  return eval (source);
}

//A wrapper to namespace isolate the codecophony internals from user scripts
var codecophony = (function() {

var items;
var script_results;
var stack;
var script_context;

var sample_rate = 44100;
var evaluate_script = codecophony_internals_evaluate_script;
var port;

function message_main (message) {
  port.postMessage (message);
}

function user_warning (message) {
  message_main ({
    action: "user_warning",
    name: stack.current,
    message: message
  });
}

function run_script (name) {
  var item = items [name];
  item.began = true;
  stack = {current: name, parent: stack, current_items: {}};
  message_main({
    action: "begin_script",
    name: name,
  });
  var success = false;
  try {
    script_results [name] = deepFreeze(evaluate_script (item.source));
    success = true;
  } catch (error) {
    message_main({
      action: "user_error",
      name: name,
      message: /*error.message + */error.stack
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

function deepFreeze (o) {
  // this does not work. You get a type error when the object contains any array buffers.
  // I'm disabling it completely in case there are OTHER undocumented type errors. :/
  return o;

  if (o !== null
      && (typeof o === "object" || typeof o === "function")
      && !Object.isFrozen(o)) {
      
  Object.freeze(o);

  Object.getOwnPropertyNames(o).forEach(function (prop) {
    if (o.hasOwnProperty(prop)) {
      deepFreeze(o[prop]);
    }
  });
  
  }
  return o;
};

function initialize (message) {
  items = message.items;
  script_results = {};
  Object.getOwnPropertyNames(items).forEach(function (name) {
    deepFreeze (items [name]);
  });
}

function item_changed (message) {
  var name = message.name;
  var item = message.value;
  items [message.name] = item;
  delete script_results[message.name];
  deepFreeze (item);
}

var handlers = {
  initialize: initialize,
  item_changed: item_changed,
  run_script: function (message) {
    Math.seedrandom ("codecophony");
    run_script (message.name);
  },
}

self.onmessage = function (event) {
  port = event.ports [0];
  port.onmessage = function(event) {
    handlers [event.data.action] (event.data);
  };
}

function get (name) {
  if (stack.current_items [name]) {return stack.current_items [name];}
  var item = items [name];
  var result;
  if (item && item.item_type === "script") {
    if (!item.began) {
      run_script (name, item);
    }
    result = script_results [name];
  }
  else if (item) {
    result = _.cloneDeepWith (item, function (value) {
      if (value instanceof Float32Array) {
        var result = new Float32Array (value.length);
        result.set (value);
        return result;
      }
    });
  }
  message_main ({
    action: "add_dependency",
    dependent: stack.current,
    dependency: name
  });
  stack.current_items [name] = result;
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

var note_names = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"];
function semitones_to_note_name (semitones) {
  return note_names [(semitones+48) % 12] + (Math.floor ((semitones+48)/12)).toString();
}

function render_note_default (note) {
  var empty = {
      item_type: "sequence",
      start: start,
      data: new Float32Array (0),
    };

  var instrument = get (note.instrument);
  if (!(instrument && instrument.item_type === "midijs_soundfont_instrument")) {
    user_warning (`"${note.instrument}" is not a recognized type of instrument. (Perhaps it isn't loaded yet, or perhaps you misspelled it?)`);
    return empty;
  }
  var instrument_samples = instrument.data [semitones_to_note_name (note.pitch)];
  
  // hack: as far as I can tell, midi.js DOESN'T provide the loop position data from sound fonts,
  // so I just hackily extend the note by crossfading the end part repeatedly.
  var half_loop_length = Math.floor (instrument_samples.length*0.2);
  var loop_length = half_loop_length*2;
  var loop_start = instrument_samples.length - loop_length;
  function sample_integer (position) {
    if (position < instrument_samples.length-half_loop_length) {return instrument_samples [position];}
    var position_1 = (position - loop_start) % loop_length;
    var position_2 = (position_1 + half_loop_length) % loop_length;
    var weight_2 = Math.abs (position_1 - half_loop_length)/half_loop_length;
    var weight_1 = 1 - weight_2;
    //console.log (position_1, position_2, weight_1, weight_2);
    return instrument_samples [loop_start + position_1]*Math.sqrt (weight_1) + instrument_samples [loop_start + position_2]*Math.sqrt (weight_2);
  }
  function sample (position) {
    return sample_integer (Math.floor (position))*(1-(position % 1)) + sample_integer (Math.ceil(position))*(position % 1);
  }
  
  // round the start time to an integer so that samples can be combined easier
  var start = Math.floor (note.start*sample_rate);
  
  if (!instrument_samples) {
    user_warning (`Pitch ${note.pitch} (${semitones_to_note_name (note.pitch)}) is not available from instrument "${note.instrument}"`);
    return empty;
  }
  
  var decay = note.decay || 0.2;
  var speed = 1;
  if (typeof note.speed === "number") {
    speed = note.speed;
  }
  else if (note.speed) {
    speed = get (note.speed);
  }
  var duration = Math.floor((note.duration+decay)*sample_rate);
  var data = new Float32Array (duration);
  var instrument_position = 0;
  for (var index = 0; index < duration;++index) {
    var cutoff = Math.min (1, 1 - ((index/sample_rate) - note.duration)/decay);
    
    data [index] = sample (instrument_position)*cutoff*note.volume;
    
    if (typeof speed === "number") {
      instrument_position += speed;
    }
    else {
      instrument_position += speed (index/sample_rate, note);
    }
  }
  
  return {
    item_type: "sequence",
    start: start,
    data: data,
  }
}

function render_note (note) {
  return (note.renderer && get (note.renderer) || render_note_default) (note);
}

function recursively (something, actions) {
  function handle (input) {
    if (typeof input === "object") {
      if (typeof input.pitch === "number" && typeof input.start === "number" && typeof input.duration === "number") {
        actions.note_action && actions.note_action (input);
      }
      else if (is_sequence(input)) {
        actions.sequence_action && actions.sequence_action (input);
      }
      else {
        Object.getOwnPropertyNames (input).forEach(function(index) {
          handle (input[index]); 
        });
      }
    }
  }
  handle (something);
}

function is_sequence (sequence) {
  return sequence && (sequence instanceof Float32Array || (typeof sequence.start === "number" && sequence.data instanceof Float32Array));
}

function normalized_sequence (sequence) {
  if (sequence instanceof Float32Array) {
    return {
      item_type: "sequence",
      start: 0,
      data: sequence
    };
  }
  return sequence;
}


function add_sequences (sequences) {
  var min = Infinity;
  var exclusive_max = -Infinity;
  recursively (sequences, {sequence_action: function (sequence) {
    sequence = normalized_sequence(sequence);
    min = Math.min (min, sequence.start);
    exclusive_max = Math.max (exclusive_max, sequence.start + sequence.data.length);
  }});
  var duration = exclusive_max - min;
  var data = new Float32Array (duration);
  for (var index = 0; index < duration;++index) {
    data [index] = 0;
  }
  recursively (sequences, {sequence_action: function (sequence) {
    sequence = normalized_sequence(sequence);
    for (var index = 0; index < sequence.data.length; ++index) {
      data [index + sequence.start - min] += sequence.data [index];
    }
  }});
  
  return {
    item_type: "sequence",
    start: min,
    data: data,
  }
}

function render_notes (notes) {
  var sequences = [];
  recursively (notes, {note_action: function (note) {
    sequences.push (render_note (note));
  }});
  return add_sequences (sequences);
}

function amplify (stuff, factor) {
  recursively (stuff, {
    note_action: function (note) {
      note.volume = (note.volume || 1)*factor;
    },
    sequence_action: function (sequence) {
      var buffer = normalized_sequence (sequence).data;
      for (var index = 0; index < buffer.length; ++index) {
        buffer [index] *= factor;
      }
    }
  });
}

function scrawl (input) {
  var commands = input.split (/\s+|(\[|\])/).filter (function (command) {
    return command !== undefined && command !== ""; 
  });
  var notes = [];
  var context_stack = [{duration: 1, start: 0, pitch: 0, volume: 1}];
  var current_note;
  var most_recent_note;
  
  var finish_note = function() {
    if (current_note) {
      /*var note = {};
      context_stack.forEach (function (context) {
        Object.assign (note, context);
      });
      Object.assign (note, current_note);*/
      notes.push (current_note);
      most_recent_note = current_note;
    }
  }
  
  function context_add (index, value) {
    (current_note || current_context()) [index] += value;
  }
  function context_multiply (index, value) {
    (current_note || current_context()) [index] *= value;
  }
  function context_set (index, value) {
    (current_note || current_context()) [index] = value;
  }
  function current_context() {
    return context_stack[context_stack.length - 1];
  }
  function current_context_copy() {
    return Object.assign ({}, current_context());
  }
  
  var handlers = {
    "[": function() {context_stack.push (current_context_copy());},
    "]": function() {context_stack.pop ();},
    "play": function() {
      finish_note();
      current_note = current_context_copy();
    },
    "and": function() {
      finish_note();
      current_note = current_context_copy();
      current_note.start = most_recent_note.start;
    },
    "then": function() {
      finish_note();
      current_note = current_context_copy();
      current_note.start = most_recent_note.start + most_recent_note.duration;
    },
    "with": function() {
      finish_note();
      current_note = undefined;
    },
  };
  for (index = 0; index <commands.length;++index) {
    var command = commands [index];
    if (handlers [command]) {
      handlers [command]();
    }
    else {
      var as_integer = parseInt (command);
      if (!isNaN (as_integer)) {
        context_add ("pitch", as_integer);
      }
      else {
        ++index;
        var value = commands [index];
        var as_float = parseFloat (value);
        if (command === "duration" || command === "lasting") {
          context_multiply ("duration", as_float);
        }
        else if (command === "volume") {
          context_multiply ("volume", as_float);
        }
        else if (command === "pitch" || command === "transpose") {
          context_add ("pitch", as_float);
        }
        else if (!isNaN (as_float)) {
          context_set (command, as_float);
        }
        else {
          context_set (command, value);
        }
      }
    }
  };
  finish_note();
  //console.log (commands);
  //console.log (notes);
  return notes;
}

return {get: get, create: create, sample_rate: sample_rate, render_note: render_note, render_note_default: render_note_default, render_notes: render_notes, add_sequences: add_sequences, scrawl: scrawl, amplify: amplify};

})();

// Hide the wrapper function
codecophony_internals_evaluate_script = undefined;

// Conveniences for the user
//var get = codecophony.get;
//var create = codecophony.create;
