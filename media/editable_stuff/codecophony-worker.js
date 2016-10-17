var items;
var stack;

function message_main (message) {
  self.postMessage (message);
}

// TODO: namespace isolate some of these from user scripts
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
    item.result = eval (item.source);
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
