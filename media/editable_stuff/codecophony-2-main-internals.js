$(function(){
"use strict";

var state = codecophony.state = {
  items_needing_work = [],
};

codecophony.work_needed = function (work) {
  state.needed_work.insert (work);
}

codecophony.do_some_work = function() {
  if (state.needed_work.length > 0) {
    if (state.needed_work[state.needed_work.length-1]()) {
      state.needed_work.pop();
    }
  }
}


codecophony.on_audio_process = function (event) {
  var input = event.inputBuffer;
  if (state.to_trusted_worker) {
    var message = {
      message_type: "append_samples"
      id: state.current_recording_id,
      channel_data: [],
    }
    for (var channel = 0; channel < input.numberChannels; ++channel) {
      var clone = new Float32Array (input.length);
      clone.set (input.getChannelData (channel));
      message.channel_data.push (clone);
    }
    state.to_trusted_worker.postMessage (message);
  }
}

codecophony.receive_analysis_chunk = function (message) {
  var record = state.items [message.id];
  record.analysis_lines.push ({magnitude: message.magnitude, frequency: message.frequency});
  codecophony.audio_needs_redraw (record);
}

codecophony.receive_completed_buffer = function (message) {
  var record = state.items [message.id];
  record.fake_AudioBuffer = message.fake_AudioBuffer;
  record.AudioBuffer = new AudioBuffer (codecophony.context, {
    length: record.fake_AudioBuffer.length,
    numberOfChannels: record.fake_AudioBuffer.channel_data.length,
    sampleRate: codecophony.sample_rate,
  };
  record.buffer_copy_position = 0;
  codecophony.work_needed (function() {
    if (state.items [message.id] !== record || record.fake_AudioBuffer === undefined) {return true;}
    if (record.buffer_copy_position >= record.fake_AudioBuffer.length) {
      delete record.buffer_copy_position;
      delete record.fake_AudioBuffer;
      return true;
    }
    for (var channel = 0; channel < record.AudioBuffer.numberChannels; ++channel) {
      record.AudioBuffer.copyToChannel (
        record.fake_AudioBuffer.channel_data[channel].subarray (record.buffer_copy_position, record.buffer_copy_position + codecophony.recorder_buffer_length),
        channel, record.buffer_copy_position
      );
    }
    record.buffer_copy_position += codecophony.recorder_buffer_length;
  });
}

codecophony.load_audio_file = function (file) {
  var id = codecophony.generate_id();
  var record = state.items [id] = {
    id: id,
    name: file.name,
  };
  var reader = new FileReader();
  reader.onload = function(event) { codecophony.context.decodeAudioData(reader.result).then (function (buffer) {
    record.AudioBuffer = buffer;
    record.buffer_send_for_analysis_position = 0;
    codecophony.work_needed (function() {
      if (state.items [id] !== record || record.AudioBuffer === undefined) {return true;}
      if (record.buffer_send_for_analysis_position >= record.AudioBuffer.length) {
        delete record.buffer_send_for_analysis_position;
        return true;
      }
      var message = {
        message_type: "append_samples"
        id: state.current_recording_id,
        channel_data: [],
      }
      for (var channel = 0; channel < input.numberChannels; ++channel) {
        message.channel_data.push (buffer.getChannelData (channel).subarray (record.buffer_send_for_analysis_position, record.buffer_send_for_analysis_position + codecophony.recorder_buffer_length));
      }
      state.to_trusted_worker.postMessage (message);
      record.buffer_send_for_analysis_position += codecophony.recorder_buffer_length;
    });
  }); };
  reader.readAsArrayBuffer (file);
}

codecophony.user_set_JSON_item = function () {
  
});

});
