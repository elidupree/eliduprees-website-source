"use strict";
var inches = 96
var millimeters = 3.78;
var pixels = 1;
var turn = Math.PI*2;

var context;

function new_context() {
  return {
    position: new Point (0, 0),
    paths: [],
  };
}
function get_context() {return context;}

function segment (first, second, color) {
  var path = new Path ([first.clone(), second.clone()]);
  path.strokeColor = color;
  path.strokeWidth = 0.01*millimeters;
  return path;
}

function move_to (position, coordinate) {
  if (coordinate !== undefined) {position = new Point (position, coordinate) ;}
  get_context();
  context.position = position;
}

function cut_to (position, coordinate) {
  if (coordinate !== undefined) {position = new Point (position, coordinate) ;}
  get_context();
  context.paths.push (segment (context.position, position, "#0000ff"));
  context.position = position;
}

function score_to (position, coordinate) {
  if (coordinate !== undefined) {position = new Point (position, coordinate) ;}
  get_context();
  context.paths.push (segment (context.position, position, "#ff0000"));
  context.position = position;
}

function move_by (position, coordinate) {
  if (coordinate !== undefined) {position = new Point (position, coordinate) ;}
  get_context();
  context.position += position;
}

function cut_by (position, coordinate) {
  if (coordinate !== undefined) {position = new Point (position, coordinate) ;}
  get_context();
  context.paths.push (segment (context.position, context.position + position, "#0000ff"));
  context.position += position;
}

function score_by (position, coordinate) {
  if (coordinate !== undefined) {position = new Point (position, coordinate) ;}
  get_context();
  context.paths.push (segment (context.position, context.position + position, "#ff0000"));
  context.position += position;
}

function cut_towards (position, coordinate) {
  if (coordinate !== undefined) {position = new Point (position, coordinate) ;}
  get_context();
  context.paths.push (segment (context.position, context.position + position, "#0000ff"));
}

function score_towards (position, coordinate) {
  if (coordinate !== undefined) {position = new Point (position, coordinate) ;}
  get_context();
  context.paths.push (segment (context.position, context.position + position, "#ff0000"));
}

function organize() {
  var paths_by_normal = {};
  var buckets = [];
  context.paths.forEach(function(path) {
    var normal = path.getTangentAt (0);
    if (normal.x <0 || (normal.x === 0 && normal.y <0)) {
      normal *= -1;
      path.reverse();
    }
    var index = "_"+normal.x+"_"+normal.y;
    var bucket = paths_by_normal [index];
    if (!bucket) {
      bucket = paths_by_normal [index] = paths_by_normal [index] || {normal: normal, index: index, perpendicular: normal.rotate (90), paths: []};
      buckets.push (bucket);
    }
    bucket.paths.push (path);
  });
  context.paths = [];
  buckets.forEach(function(bucket) {
    var evaluate = function (path) {
      var point = path.firstSegment. point;
      return point.dot (bucket.perpendicular) + point.dot (bucket.normal)*0.00001;
    };
    bucket.paths.sort (function (first, second) {return evaluate (first) - evaluate (second)});
    for (var index = 0; index <bucket.paths.length - 1;) {
      var first_second = bucket.paths [index].lastSegment. point;
      var second_first = bucket.paths [index + 1].firstSegment. point;
      var difference = second_first - first_second;
      if (bucket.paths [index].strokeColor.toString() === bucket.paths [index + 1].strokeColor.toString() && Math.abs (difference.dot (bucket.normal)) < 0.0001 && difference.dot (bucket.perpendicular) < 0.0001) {
        var second_second = bucket.paths [index + 1].lastSegment. point;
        var second_difference = second_second - first_second;
        if (second_difference.dot (bucket.perpendicular) > 0) {
          bucket.paths [index].segments [1] = bucket.paths [index+1].segments [1];
        }
        bucket.paths [index + 1].remove();
        bucket.paths.splice (index + 1, 1) ;
      }
      else {++index;}
    }
    bucket.paths.forEach(function(path) {context.paths.push (path) ; });
  });
}



function protrusion (fold_vector, perpendicular_vector, fold_function) {
  var start = context.position.clone();
  cut_by (perpendicular_vector);
  cut_by (fold_vector);
  cut_by (perpendicular_vector*-1);
  move_to (start);
  (fold_function || score_by) (fold_vector) ;
}

function circumscribed_circle (center, radius, segments) {
  var inaccuracy = Math.cos (turn*0.5/segments);
  var start = context.position.clone();
  var position = function (angle) {
    return center + new Point (Math.cos (angle), Math.sin (angle))*radius;
  };
  for (var index = 0; index <segments;++index) {
    context.position = start;
    var first_angle = turn*(index - 0.5)/segments;
    var second_angle = turn*(index + 0.5)/segments;
    move_to(position (first_angle));
    cut_to (position (second_angle));
  }
  move_to (start);
}



var cardboard_width = 0.06*inches;
var filter_width = (3+15/16)*inches;
var filter_length = 5.75*inches;
var filter_depth = 0.5*inches;
var filter_border = 3/16*inches;
var prefilter_depth = 0.25*inches;
var fan_width = 40*millimeters;
var fan_depth = 20*millimeters;
var fan_opening_width = fan_width - 3*millimeters;

var padding_width = 3/8*inches;
// Note: these sizes may be slightly smaller than my actual head, so that the foam grips my head instead of just sliding past it.
// The first prototype has something like 6+3/8 x 7+5/8, and the front-to-back grip is better than the side grip, so I made it narrower.
var head_width = (6+1/8)*inches;
var head_length = (7+5/8)*inches;
//var head_circumference = 22*inches;
var band_depth = 1*inches;
var wall_height = 7*inches;
var wall_overlap = 1*inches;
var air_holes_width = 1*inches;
var back_wall_distance = cardboard_width + (0.08)*inches;
var brim_min_width = 2*inches;
var wall_holder_length = band_depth + (1/8)*inches;
var wall_holder_tab_length = 0.5*inches;



// Depending on your assumptions, the leeway should be somewhere between 0 and cardboard_width.
// If it's too low, the filters might not quite fit. If it's too high, they might slide around a bit. Not fitting is a bigger inconvenience.
var box_leeway = cardboard_width;
var box_width = filter_width + 2*box_leeway;
var box_length = filter_length + 2*box_leeway;
var box_depth = 2*inches;
var protrusion_width = box_width/3;
var protrusion_length = 0.25*inches; //cardboard_width*2;

var holder_protrusion_length = filter_depth + 0.25*inches;

var box_diagonal = new Point (box_width, box_depth).length;
var protrusion_surroundings = (box_width - protrusion_width)/2;
var filter_inner_length = filter_length - filter_border*2;
var filter_inner_width = filter_width - filter_border*2;

var roof_opening_width = filter_inner_width;
var roof_opening_length = box_length;
var roof_opening_slot_depth = cardboard_width + cardboard_width + prefilter_depth


var wall_slope_tester = new Point (box_width, box_depth).normalize();
var wall_slope_with_respect_to_fan = new Point (0, 1).dot (wall_slope_tester.rotate (90))/new Point (0, 1).dot (wall_slope_tester);
var minimum_possible_fan_offset = fan_depth/wall_slope_with_respect_to_fan;
var maximum_possible_fan_offset = box_diagonal - fan_width - fan_depth*wall_slope_with_respect_to_fan;
// I think I want to put the fan equidistant between the 2 filters.
// maximum_possible_fan_offset is the offset when it touches one filter wall;
// 0 is the offset when it touches the other (impossible, but theoretically).
var fan_offset = maximum_possible_fan_offset/2;
//console.log (minimum_possible_fan_offset, fan_offset, maximum_possible_fan_offset, box_diagonal) ;
var fan_center_offset = fan_offset + fan_width/2;


function box_side (direction) {
  cut_by (protrusion_surroundings, 0);
  protrusion (new Point (protrusion_width, 0), new Point (0, protrusion_length*direction), move_by);
  cut_by (protrusion_surroundings, 0);
  if (direction >0) {score_towards (0, - box_length);}
  cut_by (box_depth, 0); //protrusion (new Point (box_depth, 0), new Point (0, box_width*direction));
  if (direction >0) {
    score_towards (0, - box_length);
    circumscribed_circle (context.position + new Point (fan_center_offset, - box_length/2), fan_opening_width/2, 8);
  }
  cut_by (box_diagonal, 0);
  if (direction >0) {score_towards (0, - box_length);}
  cut_by (box_depth, 0);
  if (direction >0) {score_towards (0, - box_length);}
  protrusion (new Point (box_width, 0), new Point (0, box_depth*direction)); //cut_by (box_width, 0);
}

function box() {
  var start = context.position.clone();
  cut_by (0, box_length);
  box_side (1) ;
  cut_by (0, - box_length);
  
  move_by (- filter_border - box_leeway, filter_border + box_leeway) ;
  protrusion (new Point (-filter_inner_width, 0), new Point (0, filter_inner_length), cut_by);
  
  move_to (start);
  box_side (- 1);
  move_to (start);
  move_by (filter_border + box_leeway, filter_border + box_leeway) ;
  protrusion (new Point (filter_inner_width, 0), new Point (0, filter_inner_length), cut_by);
}

function holder (direction) {
  var start = context.position.clone();
  protrusion (new Point (0, box_length), new Point (-holder_protrusion_length, 0));
  cut_by (box_width, 0);
  protrusion (new Point (0, -box_length), new Point (holder_protrusion_length, 0));
  if (direction < 0) {
    protrusion (new Point (- box_width, 0), new Point (0, - holder_protrusion_length));
  }
  else {
    protrusion (new Point (-protrusion_surroundings, 0), new Point (0, - holder_protrusion_length));
    cut_by (- protrusion_width, 0) ;
    protrusion (new Point (-protrusion_surroundings, 0), new Point (0, - holder_protrusion_length));
  }
  move_by (filter_border + box_leeway, filter_border + box_leeway) ;
  protrusion (new Point (filter_inner_width, 0), new Point (0, filter_inner_length), cut_by);
}


var brim_segments = 24;
function hat() {

  function offset (index) {return turn*index/brim_segments;}
  function head_vector (offset) {
    return new Point (
      (head_width/2)*Math.cos (offset),
      (head_length/2)*Math.sin (offset)
    );
  }
  
  var data = [];
  for (var index = 0; index <brim_segments;++index) {
    data.push ({});
  }
  var index, current, previous, next;
  function iterate (callback) {
    for (index = 0; index <brim_segments;++index) {
      current = data [index];
      next = data [(index + 1) % brim_segments];
      previous = data [(index + brim_segments - 1) % brim_segments];
      callback();
    }
  }
  
  
  iterate (function() {
    current.head_vector = head_vector (offset (index));
  });
  iterate (function() {
    current.previous_perpendicular = (current.head_vector - previous.head_vector).rotate (-90).normalize();
    current.previous_middle = (current.head_vector + previous.head_vector)/2;
    current.wall_bonus = Math.max (0, 1 - Math.abs ((index-0.5)/(brim_segments/4) - 1)*1.5);
    current.wall_distance = padding_width + cardboard_width + air_holes_width*current.wall_bonus + back_wall_distance*(1 - current.wall_bonus);
    current.wall_vector = current.previous_middle + current.previous_perpendicular*current.wall_distance;
    current.wall_holder_vector = current.wall_vector + current.previous_perpendicular*cardboard_width;
    current.brim_vector = current.wall_holder_vector + current.previous_perpendicular*brim_min_width;
  });
  iterate (function() {
    current.middle_perpendicular = (current.previous_perpendicular + next.previous_perpendicular).normalize();
    current.band_vector = current.head_vector + current.middle_perpendicular*padding_width;
    current.band_holder_vector = current.band_vector + current.middle_perpendicular*cardboard_width;
    current.band_holder_tab_vector = current.band_holder_vector - current.middle_perpendicular*band_depth;
    
    current.wall_holder_perpendicular = (next.wall_holder_vector - current.wall_holder_vector).rotate (- 90).normalize();
    
    var small = 0.1;
    var big = 0.8;    
    current.air_holes = [
      previous.band_holder_vector*big + current.band_holder_vector*small + current.wall_holder_vector*small,
      previous.band_holder_vector*small + current.band_holder_vector*big + current.wall_holder_vector*small,
      previous.band_holder_vector*small + current.band_holder_vector*small + current.wall_holder_vector*big,
      next.wall_holder_vector*big + current.band_holder_vector*small + current.wall_holder_vector*small,
      next.wall_holder_vector*small + current.band_holder_vector*big + current.wall_holder_vector*small,
      next.wall_holder_vector*small + current.band_holder_vector*small + current.wall_holder_vector*big,
    ];
  });
  iterate (function() {
    current.wall_holder_fold_1 = current.wall_holder_vector + current.wall_holder_perpendicular*wall_holder_length;
    current.wall_holder_fold_2 = next.wall_holder_vector + current.wall_holder_perpendicular*wall_holder_length;
    current.wall_holder_end_1 = current.wall_holder_fold_1 + current.wall_holder_perpendicular*wall_holder_tab_length;
    current.wall_holder_end_2 = current.wall_holder_fold_2 + current.wall_holder_perpendicular*wall_holder_tab_length;
  });
  
  var brim_center = new Point (27*inches, 0);
  var roof_center = new Point (40*inches, 0);
  var wall_start = new Point (20*inches, 10*inches);
  var band_start = new Point (20*inches, 20*inches);
  var wall_length_so_far = wall_overlap;
  var band_length_so_far = 0;
  
  iterate (function() {
    move_to (brim_center + current.band_holder_vector);
    cut_to (brim_center + current.band_holder_tab_vector);
    cut_to (brim_center + next.band_holder_tab_vector);
    cut_to (brim_center + next.band_holder_vector);
    score_to (brim_center + current.band_holder_vector);
    
    move_to (brim_center + current.brim_vector);
    cut_to (brim_center + next.brim_vector) ;
    
    var wall_segment_length = (current.wall_vector - next.wall_vector).length;
    var band_segment_length = (current.band_vector - next.band_vector).length;
    
    if (current.wall_bonus >0.3) {
      move_to (brim_center + current.air_holes [0]);
      cut_to (brim_center + current.air_holes [1]);
      cut_to (brim_center + current.air_holes [2]);
      cut_to (brim_center + current.air_holes [0]);
    }
    /*if (current.wall_bonus >0.3 && next.wall_bonus >0.3 && index % 3 !== 0) {
      move_to (brim_center + current.air_holes [3]);
      cut_to (brim_center + current.air_holes [4]);
      cut_to (brim_center + current.air_holes [5]);
      cut_to (brim_center + current.air_holes [3]);
    }*/
    
    if (index % 3 === 0) {
      var centers = [roof_center, brim_center];
      centers.forEach(function(center) {
      move_to (center + current.wall_holder_vector);
      cut_to (center + current.wall_holder_fold_1);
      cut_to (center + current.wall_holder_end_1);
      cut_to (center + current.wall_holder_end_2);
      cut_to (center + current.wall_holder_fold_2);
      cut_to (center + next.wall_holder_vector);
      score_to (center + current.wall_holder_vector);
      move_to (center + current.wall_holder_fold_1);
      score_to (center + current.wall_holder_fold_2);
      });
      
      move_to (wall_start + new Point (wall_length_so_far, wall_holder_length));
      protrusion (new Point (wall_segment_length, 0), new Point (0, -cardboard_width), cut_by);
      
      move_to (wall_start + new Point (wall_length_so_far, wall_height - wall_holder_length));
      protrusion (new Point (wall_segment_length, 0), new Point (0, cardboard_width), cut_by);
    }
    else {
      move_to (roof_center + current.wall_holder_vector);
      cut_to (roof_center + current.wall_holder_fold_1);
      cut_to (roof_center + current.wall_holder_fold_2);
      cut_to (roof_center + next.wall_holder_vector);
      score_to (roof_center + current.wall_holder_vector);
    }
    wall_length_so_far += wall_segment_length;
    band_length_so_far += band_segment_length;
  });
  
  move_to (roof_center + new Point (- roof_opening_width/2, - roof_opening_length/2));
  cut_to (roof_center + new Point (- roof_opening_width/2, roof_opening_length/2));
  score_to (roof_center + new Point (roof_opening_width/2, roof_opening_length/2));
  cut_to (roof_center + new Point (roof_opening_width/2, -roof_opening_length/2));
  score_to (roof_center + new Point (-roof_opening_width/2, -roof_opening_length/2));
  move_to (roof_center + new Point (- roof_opening_width/2, 0));
  cut_to (roof_center + new Point (roof_opening_width/2, 0));
  move_to (roof_center + new Point (- protrusion_width/2, - roof_opening_length/2 + roof_opening_slot_depth));
  protrusion (new Point (protrusion_width, 0), new Point (0, cardboard_width), cut_by);
  move_to (roof_center + new Point (- protrusion_width/2, roof_opening_length/2 - roof_opening_slot_depth));
  protrusion (new Point (protrusion_width, 0), new Point (0, -cardboard_width), cut_by);
  
  move_to (wall_start);
  protrusion (new Point (wall_length_so_far, 0), new Point (0, wall_height), cut_by);
  move_to (band_start);
  protrusion (new Point (band_length_so_far, 0), new Point (0, band_depth), cut_by);
}



context = new_context();

box();
move_by (0,11*inches);
holder (1) ;
move_by (0,7*inches);
holder (- 1);
hat();

/*

  Note: Other pieces that aren't made of cardboard:
  
  the fan
  the USB cord to power the fan
  the HEPA filter
  the pre-filter
  the foam padding around the head
  
  the thin foam padding used for sealing the fan and brim-to-wall-to-roof (and box to roof?)
  the cloth cover
  
  glue to attach the band and cloth
  packing tape to assemble the purifier box and to suppress smells
  
  optionally, a USB battery pack
  
  
  
  Hat caveats:
  avoid rain
  carbon filter collects smells
  the constant airflow occasionally makes my eyes dry
  tiny sound and vibration
  slightly top-heavy
  specific to head size
  
*/

function hip_support () {
  var reference = new Point (3.5*inches, 1.5*inches);
  cut_by(new Point (2*inches, 0));
  score_towards (0, reference.length);
  protrusion (new Point ({length: reference.y, angle: reference.angle}), new Point ({length: (1)*inches, angle: reference.angle-90}));
  score_towards (new Point ({length: reference.x, angle: reference.angle+90}));
  cut_by(new Point ({length: (2)*inches, angle: reference.angle}));
  score_towards (new Point ({length: reference.x, angle: reference.angle+90}));
  protrusion (new Point ({length: reference.y + (1.5)*inches, angle: reference.angle}), new Point ({length: (1)*inches, angle: reference.angle-90}));
  var something = context.position.clone();
  score_by(new Point ({length: reference.length, angle: 90+reference.angle*2}));
  var whatever = context.position.clone();
  cut_by (new Point ({length: 2.5*inches, angle: reference.angle*2}));
  var weird_distance = 3.3*inches;
  score_towards (new Point ({length: weird_distance, angle: reference.angle*2-90}));
  cut_by (new Point ({length: 1*inches, angle: reference.angle*2}));
  cut_by (new Point ({length: weird_distance, angle: reference.angle*2-90}));
  cut_by (new Point ({length: 1*inches, angle: reference.angle*2-180}));
  cut_to (something);
  move_to (whatever);
  cut_by (new Point ({length: (0+2+1.5)*inches, angle: 180+reference.angle}));
  cut_by (-2*inches, 0);
}
function corner_support() {
  var reference = new Point (3*inches - cardboard_width*2, 2*inches);
  var depth = 2.5*inches;
  var something = context.position.clone();
  cut_by (0, depth);
  cut_by (reference.y, 0);
  score_towards (0, - depth);
  score_by (reference.length, 0);
  score_towards (0, - depth);
  var whatever = context.position.clone();
  cut_by(new Point ({length: reference.x, angle: 180-reference.angle}));
  cut_by(new Point ({length: reference.y, angle: 270-reference.angle}));
  move_to (whatever) ;
  cut_by (reference.x, 0);
  //score_towards (0, - depth);
  //cut_by (reference.y, 0);
  cut_by (0, - depth);
  //cut_to (something);
  cut_by (- reference.x, 0);
  //whatever = context.position.clone();
  score_towards (- reference.length, 0);
  protrusion (new Point ({length: reference.x, angle: 180 + reference.angle}), new Point ({length: depth, angle: 270 + reference.angle}));
  protrusion (new Point ({length: reference.y, angle: 90 + reference.angle}), new Point ({length: depth, angle: 180 + reference.angle}));
  
  cut_by (- reference.y, 0);
}
move_to (0, -20*inches);
hip_support();
move_to (0, -30*inches);
corner_support();

organize();

context.paths.forEach(function(path) {
  path.strokeWidth = 1*pixels;
});

var exportSVG = function() {
  var svg = project.exportSVG();
  // create a doctype
  var svgDocType = document.implementation.createDocumentType('svg', "-//W3C//DTD SVG 1.1//EN", "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd");
  // a fresh svg document
  var svgDoc = document.implementation.createDocument('http://www.w3.org/2000/svg', 'svg', svgDocType);
  // replace the documentElement with our svg
  svgDoc.replaceChild(svg, svgDoc.documentElement);
  // get the data
  var svgData = (new XMLSerializer()).serializeToString(svgDoc);

  // now you've got your svg data, the following will depend on how you want to download it
  // e.g yo could make a Blob of it for FileSaver.js
  /*
  var blob = new Blob([svgData.replace(/></g, '>\n\r<')]);
  saveAs(blob, 'myAwesomeSVG.svg');
  */
  // here I'll just make a simple a with download attribute

  var a = document.createElement('a');
  a.href = 'data:image/svg+xml; charset=utf8, ' + encodeURIComponent(svgData.replace(/></g, '>\n\r<'));
  a.download = 'air-purifier-box.svg';
  a.innerHTML = 'download the svg file';
  $("#content").append(a);
};

exportSVG();
