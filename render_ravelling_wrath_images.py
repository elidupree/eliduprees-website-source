  #!/usr/bin/python3
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

for filename in os.listdir(input_dir):
  input_path = f"{input_dir}/{filename}"
  output_path = f"{output_dir}/{filename}"
  output_path_left = output_path.replace(".png", "-left.png")
  output_path_right = output_path.replace(".png", "-right.png")
  
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
   
  (gimp-image-crop page {target_nominal_width} {target_nominal_height} {(source_width - target_nominal_width) // 2} {(source_height - target_nominal_height) // 2})
  (gimp-image-scale-full page {target_nominal_width//2} {target_nominal_height//2} INTERPOLATION-CUBIC)
  (file-png-save RUN-NONINTERACTIVE page page_drawable "{output_path}" "{filename}" 0 9 0 0 0 0 0)
  (file-jpeg-save RUN-NONINTERACTIVE page page_drawable "{output_path.replace('.png', '.jpg')}" "{filename}" 0.7 0 0 0 "" 0 0 0 0)
  (gimp-image-delete page)
  
  (gimp-image-crop page_left {target_bleed_width} {target_bleed_height} {source_width - target_bleed_width} {(source_height - target_bleed_height) // 2}) 
  (file-png-save RUN-NONINTERACTIVE page_left page_left_drawable "{output_path_left}" "{filename}" 0 9 0 0 0 0 0)
  (gimp-image-delete page_left)
  
  (gimp-image-crop page_right {target_bleed_width} {target_bleed_height} {0} {(source_height - target_bleed_height) // 2}) 
  (file-png-save RUN-NONINTERACTIVE page_right page_right_drawable "{output_path_right}" "{filename}" 0 9 0 0 0 0 0)
  (gimp-image-delete page_right)
)''')

  gimp_stuff.optimize (output_path, lossy = True, quality = "30-50")
  gimp_stuff.optimize (output_path_left, lossy = False)
  gimp_stuff.optimize (output_path_right, lossy = False)

  
  
  
  
