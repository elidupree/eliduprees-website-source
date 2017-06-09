var decibel_log_factor = 20/Math.log(10);
function decibels_to_pressure (decibels) {
  return Math.exp(decibels/decibel_log_factor);
}
function pressure_to_decibels (pressure) {
  return Math.log (pressure)*decibel_log_factor;
}

var inv_log_cent_ratio = 1/Math.log (Math.pow (2,1/1200));
function frequency_to_cents (frequency) {
  return Math.log (frequency)*inv_log_cent_ratio;
}

function for_frequency_values (sample_rate, frequency_buffer, callback) {
  var rate = sample_rate;
  var frequency_buffer_length = frequency_buffer.length;
  for (var I = 0; I <frequency_buffer_length;++I) {
    var min_frequency = I*rate/frequency_buffer_length/2;
    var max_frequency = (I+1)*rate/frequency_buffer_length/2;
    callback (min_frequency, max_frequency, frequency_buffer [I], I);
  }
}

function get_cent_pressures (analyzer) {
  var frequency_buffer_length = analyzer.frequencyBinCount; 
  var frequency_data = new Float32Array(frequency_buffer_length);
  analyzer.getFloatFrequencyData (frequency_data);
  var cent_magnitudes = [];
  for (var index = 0; index <1200;++index) {cent_magnitudes.push (0);}
  
  for_frequency_values (analyzer.context.sampleRate, frequency_data, function (min_frequency, max_frequency, decibels) {
    if (min_frequency > 0) {
      var min_cents = frequency_to_cents (min_frequency);
      var max_cents = frequency_to_cents (max_frequency);
      var amount = decibels_to_pressure (decibels);
      for (var index = Math.floor (min_cents); index < max_cents;++index) {
        var value = amount;
        if (index < min_cents) {value *= 1 - (min_cents - Math.floor(min_cents));}
        if (index+1 > max_cents) {value *= max_cents - Math.floor(max_cents);}
        cent_magnitudes [index % 1200] += value;
      }
    }
  });
  return cent_magnitudes;
}
function get_cent_decibels (analyzer) {
  var result = get_cent_pressures (analyzer);
  for (var index = 0; index <1200;++index) {result [index] = pressure_to_decibels (result [index]);}
  return result;
}


var annoying = {};

annoying.create_memory = function(context) {
  return {
    samples: {},
    num_samples_ever: 0,
    context: context,
    max_samples: Math.floor(context.sampleRate / 20),
    totals: {},
    silence_threshold: 1/1024,
  };
}

annoying.process_sample = function(memory, sample) {
  // maintain a running root mean square of the last X samples
  
  if (memory.num_samples_ever >= memory.max_samples) {
    var removed_index = memory.num_samples_ever - memory.max_samples;
    var removed = memory.samples [removed_index];
    delete memory.samples [removed_index];
    Object.getOwnPropertyNames (removed.contributions).forEach(function(name) {
      memory.totals [name] -= removed.contributions [name];
    });
  }
  
  var contributions = {};
  memory.samples[memory.num_samples_ever] = {value: sample, contributions};
  ++memory.num_samples_ever;
  memory.num_samples_currently = Math.min(memory.num_samples_ever, memory.max_samples);
  
  function contribute (name, value) {
    contributions [name] = value;
    if (memory.totals [name] === undefined) {
      memory.totals [name] = 0;
    }
    memory.totals [name] += value;
  }
  
  contribute ("square", sample*sample);
  
  
  memory.root_mean_square = Math.sqrt(memory.totals.square / memory.num_samples_currently);
  
  contribute ("excess", Math.max(0, Math.abs(sample/(2*Math.max(memory.silence_threshold, memory.root_mean_square))) - 1));
  
  memory.average_excess = memory.totals.excess / memory.num_samples_currently;
}


