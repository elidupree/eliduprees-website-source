var items;
var stack;

// A wrapper to stop eval() from changing variables local to the codecophony internals
function codecophony_internals_evaluate_script (source) {
  return eval (source);
}

//A wrapper to namespace isolate the codecophony internals from user scripts
var codecophony = (function() {

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

return {get: get, create: create};

})();

// Hide the wrapper function
codecophony_internals_evaluate_script = undefined;

// Conveniences for the user
var get = codecophony.get;
var create = codecophony.create;
