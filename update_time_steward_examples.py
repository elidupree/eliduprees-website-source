#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division

import os
import sys
import os.path
import shutil

directory = sys.argv[1]
shutil.copy(os.path.join (directory, "emscripten-examples.js"), "./media/vendor/time-steward-examples/emscripten-examples.js")
shutil.copy(os.path.join (directory, "emscripten-examples.css"), "./media/vendor/time-steward-examples/emscripten-examples.css")
shutil.copy(os.path.join (directory, "target/asmjs-unknown-emscripten/release/examples/bouncy_circles_rowless.js"), "./media/vendor/time-steward-examples/bouncy-circles.js")
shutil.copy(os.path.join (directory, "target/asmjs-unknown-emscripten/release/examples/simple_diffusion_rowless.js"), "./media/vendor/time-steward-examples/simple-diffusion.js")
