"use strict";
var inches = 96
var millimeters = 3.78;
var pixels = 1;


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
  var bucket = [];
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
      if (bucket.paths [index].strokeColor === bucket.paths [index + 1].strokeColor && Math.abs (difference.dot (bucket.normal)) < 0.0001 && difference.dot (bucket.perpendicular) < 0.0001) {
        var second_second = bucket.paths [index + 1].lastSegment. point;
        var second_difference = second_second - first_second;
        if (second_difference.dot (bucket.perpendicular) > 0) {
          bucket.paths [index].segments [1] = bucket.paths [index+1].segments [1];
        }
        bucket.paths.splice (index + 1, 1) ;
      }
      else {++index;}
    }
    bucket.paths.forEach(function(path) {context.path.push (path) ; });
  });
}



var cardboard_width = 0.06*inches;
var filter_width = (3+15/16)*inches;
var filter_length = 5.75*inches;
var filter_depth = 0.5*inches;
var filter_border = 3/16*inches;


var box_width = filter_width;
var box_length = filter_length;
var box_depth = 1.5*inches;
var protrusion_width = box_width/3;
var protrusion_length = cardboard_width*2;

var holder_protrusion_length = filter_depth + 0.25*inches;

var box_diagonal = new Point (box_width, box_depth).length;
var protrusion_surroundings = (box_width - protrusion_width)/2;
var filter_inner_length = filter_length - filter_border*2;
var filter_inner_width = filter_width - filter_border*2;



function protrusion (fold_vector, perpendicular_vector, fold_function) {
  var start = context.position;
  cut_by (perpendicular_vector);
  cut_by (fold_vector);
  cut_by (perpendicular_vector*-1);
  move_to (start);
  (fold_function || score_by) (fold_vector) ;
}

function box_side (direction) {
  cut_by (protrusion_surroundings, 0);
  protrusion (new Point (protrusion_width, 0), new Point (0, protrusion_length*direction));
  cut_by (protrusion_surroundings, 0);
  if (direction >0) {score_towards (0, - box_length);}
  protrusion (new Point (box_depth, 0), new Point (0, box_width*direction));
  if (direction >0) {score_towards (0, - box_length);}
  cut_by (box_diagonal, 0);
  if (direction >0) {score_towards (0, - box_length);}
  cut_by (box_depth, 0);
  if (direction >0) {score_towards (0, - box_length);}
  cut_by (box_width, 0);
}

function box() {
  var start = context.position;
  cut_by (0, box_length);
  box_side (1) ;
  cut_by (0, - box_length);
  
  move_by (- filter_border, filter_border) ;
  protrusion (new Point (-filter_inner_width, 0), new Point (0, filter_inner_length), cut_by);
  
  move_to (start);
  box_side (- 1);
  move_to (start);
  move_by (filter_border, filter_border) ;
  protrusion (new Point (filter_inner_width, 0), new Point (0, filter_inner_length), cut_by);
}

function holder (direction) {
  var start = context.position;
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
}

context = new_context();

box();
move_by (0,11*inches);
holder (1) ;
move_by (0,7*inches);
holder (- 1);

context.paths.forEach(function(path) {
  path.strokeWidth = 2*pixels;
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
