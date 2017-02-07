$(function(){
"use strict";



/*



Codecophony data consists of "items". Each item has a unique id and some data.

The data is either JSON or an AudioBuffer(ish). Thus, they can live in any of the various places we might want to store them – JavaScript memory in the main thread, JavaScript memory in web workers, indexedDB, and the filesystem. AudioBuffers per se can only exist in the main thread, but we can convert them to-and-from fake AudioBuffers that just consist of Float32Arrays (for indexedDB and the web workers), or actual audio files (for the filesystem).

Items can also be broken down into "source items" and "generated items". Source items are manually created by the user, generally by writing scripts or recording audio. They are automatically assigned cryptographically-random ids, so that there are no collisions.

A special type of JSON source item is a "project". It gives a mapping of source item ids to human readable names, which must be unique within the project. This creates implicit "generated items" – identical to the source items, but with those names instead of the random id. Some of these generated items may be scripts that create explicit generated items, also with names that must be unique within the project. All generated items are specific to a project.

(In the UI, when you record audio or create a script, it becomes a new source item, and also is added to the current project with a random human readable name.)

Whenever a source item is created or modified, it is autosaved to the filesystem if possible. If that's not available, it is autosaved to indexedDB instead. When you open a project, all source items referenced by the project are loaded from the filesystem (or, if not found in the filesystem, from indexedDB). If they were in indexedDB and not in the file system, but now CAN be put to the file system, do that. (What's the best way to make sure everything gets autosaved to the file system when you install the extension? Having explicit code to do that seems tricky to maintain)

You can "export" a single project, which saves a directory containing all generated items of that project, or all source items used by that project (your choice). You can also "import" a project that was saved either way, which may use the project's name mapping in reverse to save the appropriate source items. (Note: we will need to handle the case where this tries to overwrite other source items.) You also can, optionally, have the project generated items be autosaved to a subdirectory, and when you load a project, codecophony checks whether there are autosaved generated items available. (Should this auto saving include the implicit generated items that are identical to source items? That could be convenient, but also wasteful)

Another special JSON source file is the "project list", which always has the id "project_list". This map source ids to project names. Importing a project adds an entry to this list. (I guess projects also have to remember their own names, at least when exported...)




Technical details:

in JavaScript memory, a item is represented as a object:
{
  id: string,
  data: object,
}

Fake AudioBuffers (a value of "data:" above) look like this:
{
  codecophony_item_type = "AudioBuffer",
  length: number,
  channel_data: [Float32Array],
}

Each thread keeps its own dictionary of the items:
{
  [id]: {
    item: item,
    // ... metadata
  },
  ...
}


*/

codecophony.transfer_item (port, item) {
  if (!port) {return;}
  port.postMessage ({
    
  })
}

// Use only in the main thread
codecophony.user_edited_item = function (id, data) {
  local record = codecophony.state.items_by_id [id];
  record.item.data = data;
  if (codecophony.to_trusted_worker) {
    codecophony.to_trusted_worker  }
}




});
