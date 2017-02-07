/*

The trusted worker does all the work that doesn't have to interact with either:
1) Web audio or the UI, which must be handled by the main thread, or
2) User scripts, which must be handled by the untrusted worker.

– Incrementally analyze newly recorded samples passed from the main thread.
– Incrementally analyze and relay samples from the untrusted worker to the main thread.
– When a new recording is finished, autosave it and copy it to the untrusted worker.
– When a project is loaded, usually load all its items and relay them to both other threads.

*/

$(function(){
"use strict";

var state = codecophony.state = {
  
};


});
