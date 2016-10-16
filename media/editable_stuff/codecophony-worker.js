var items;
var stack;
var dependencies = {};
var dependents = {};

// TODO: namespace isolate some of these from user scripts
function run_script (name) {
  var item = items [name];
  item.began = true;
  stack = {current: name, parent: stack};
  self.postMessage ({
    action: "begin_script",
    name: name,
  });
  try {
    item.result = eval (item.source);
  } catch (error) {
    self.postMessage ({
      action: "user_error",
      name: name,
      file: error.filename,
      line: error.lineno,
      message: error.message
    });
  }
  self.postMessage ({
    action: "finish_script",
    name: name,
  });
  item.finished = true;
  stack = stack.parent;
}

function initialize (message) {
  items = message.items;
  Object.getOwnPropertyNames (items).forEach (function (name) {
    dependencies [name] = {};
    dependents [name] = {};
  });
  Object.getOwnPropertyNames (items).forEach (function (name) {
    var item = items [name];
    if (item.item_type === "script" && !item.began) {
      run_script (name);
    }
  });
}

function item_changed (message) {
  var name = message.name;
  var item = message.value;
  items [message.name] = item;
  dependents[name] = dependents[name] || {};
  dependencies[name] = dependencies[name] || {};
  var my_dependents = [];
  
  Object.getOwnPropertyNames (dependents[name]).forEach (function (dependent) {
    remove_dependency (dependent, name);
    dependents.push (dependent);
  });
  if (item.item_type === "script") {
    run_script (name);
  }
  my_dependents.forEach (function (dependent) {
    run_script (dependent);
  });
}

function rerun (message) {
  run_script (message.name);
}


function remove_dependency(dependent, dependency) {
  delete dependencies [dependent] [dependency];
  delete dependents [dependency] [dependent];
}
function add_dependency(dependent, dependency) {
  dependencies [dependent] [dependency] = true;
  dependents [dependency] [dependent] = true;
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
  add_dependency (stack.current, name);
  return result;
}
function create (name, value) {
  self.postMessage ({
    action: "create_item",
    name: name,
    value: value,
    created_by: stack.current
  });
}

var handlers = {
  initialize: initialize,
  item_changed: item_changed,
  rerun: rerun
}

self.onmessage = function (event) {
  handlers [event.data.action] (event.data);
}
