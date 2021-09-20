#  #!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division

import os
import os.path
import gimp_stuff

input_dir = "ravelling_wrath/illustration_source_bitmaps"
output_dir = "media/generated_from_source_files/ravelling-wrath/illustrations"

  
dpi = 300
source_width = 1965
source_height = 2850
target_nominal_width = 6*dpi
target_nominal_height = 9*dpi
target_bleed_width = target_nominal_width + dpi//4
target_bleed_height = target_nominal_height + dpi//4

only = None
only = "21"
only = "dfjds"

custom = {
  "1-1": (275, 1595, True),
  "watchful-eye-ornate": (686, 1979, True),
  "7": (1418, None, False),
  "endless-maze-ornate": (810, 1890, True),
  "10": (None, 1800, False),
  "dauntless-gate-ornate": (966, 1880, True),
  "14": (None, 1906, False),
  "cloven-earth-ornate": (620, 2228, True),
  "burning-heart-ornate": (706, 1914, True),
  "21": (738, 1058, True),
}

for filename in os.listdir(input_dir):
  filename_base = os.path.splitext(filename)[0]
  if only and only != filename_base:
    continue
  input_path = f"{input_dir}/{filename}"
  output_path = f"{output_dir}/{filename}"
  output_path_left = output_path.replace(".png", "-left.png")
  output_path_right = output_path.replace(".png", "-right.png")
  
  crop_top = (source_height - target_nominal_height) // 2
  crop_bottom = crop_top + target_nominal_height
  crop_top_print = (source_height - target_bleed_height) // 2
  crop_bottom_print = crop_top_print + target_bleed_height
  
  if filename_base in custom:
    override_top, override_bottom, override_print = custom[filename_base]
    if override_top is not None:
      crop_top = override_top
      if override_print:
        crop_top_print = override_top
    if override_bottom is not None:
      crop_bottom = override_bottom
      if override_print:
        crop_bottom_print = override_bottom
        
  crop_height = crop_bottom - crop_top
  crop_height_print = crop_bottom_print - crop_top_print
  
  gimp_stuff.gimp_batch(f'''
(let* (
        (page (car (gimp-file-load RUN-NONINTERACTIVE "{input_path}" "{filename}")))
        (observed_height (car (gimp-image-height page)))
        (observed_width (car (gimp-image-width page)))
        (page_drawable (car (gimp-image-flatten page)))
        (page_left (car (gimp-image-duplicate page)))
        (page_left_drawable (car (gimp-image-get-active-layer page_left)))
        (page_right (car (gimp-image-duplicate page)))
        (page_right_drawable (car (gimp-image-get-active-layer page_right)))
      )
   
  (gimp-image-crop page {target_nominal_width} {crop_height} {(source_width - target_nominal_width) // 2} {crop_top})
  (gimp-image-scale-full page {target_nominal_width//2} {crop_height//2} INTERPOLATION-CUBIC)
  (file-png-save RUN-NONINTERACTIVE page page_drawable "{output_path}" "{filename}" 0 9 0 0 0 0 0)
  (file-jpeg-save RUN-NONINTERACTIVE page page_drawable "{output_path.replace('.png', '.jpg')}" "{filename}" 0.7 0 0 0 "" 0 0 0 0)
  (gimp-image-delete page)
  
  (gimp-image-crop page_left {target_bleed_width} {crop_height_print} {source_width - target_bleed_width} {crop_top_print}) 
  (file-png-save RUN-NONINTERACTIVE page_left page_left_drawable "{output_path_left}" "{filename}" 0 9 0 0 0 0 0)
  (gimp-image-delete page_left)
  
  (gimp-image-crop page_right {target_bleed_width} {crop_height_print} {0} {crop_top_print}) 
  (file-png-save RUN-NONINTERACTIVE page_right page_right_drawable "{output_path_right}" "{filename}" 0 9 0 0 0 0 0)
  (gimp-image-delete page_right)
)''')

  gimp_stuff.optimize (output_path, lossy = True, quality = "30-50")
  gimp_stuff.optimize (output_path_left, lossy = False)
  gimp_stuff.optimize (output_path_right, lossy = False)

  
  
  
  