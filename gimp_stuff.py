#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division

import sys
import subprocess
import shlex
import comics

def gimp_batch(command):
  commandp = "gimp --no-interface --batch="+shlex.quote(command)+" --batch='(gimp-quit 0)'"
  print("calling:\n"+commandp)
  out = subprocess.Popen(commandp, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
  output = out.communicate()
  print(output)
  print("finished GIMP batch command")
  #print("gimp --no-interface --batch='"+command+"'")

def optimize (file, lossy = True):
  if lossy: subprocess.run (["pngquant", "--ext=.png", "--force", "--skip-if-larger", "--quality=70-100", "--speed=1", "--verbose", "256", "--", file])
  subprocess.run (["optipng", "-o4", file])

def generate_images(infile_path, infile_base, outfile_base, width, height, target_width, scale_full_page):
  output_dir = "./media/generated_from_source_files/"
  infile = infile_path+infile_base
  page_outfile_base = outfile_base+".png"
  page_outfile = output_dir+page_outfile_base
  thumbnail_top_outfile_base = outfile_base+"_thumbnail_top.png"
  thumbnail_top_outfile = output_dir+thumbnail_top_outfile_base
  thumbnail_full_outfile_base = outfile_base+"_thumbnail_full.png"
  thumbnail_full_outfile = output_dir+thumbnail_full_outfile_base
  
  #Scheme code
  gimp_batch('''
(let* (
        (page (car ('''+('file-jpeg-load' if infile_base.endswith(".jpg") else '''gimp-file-load''')+''' RUN-NONINTERACTIVE "'''+infile+'" "'+infile_base+'''")))
        (observed_height (car (gimp-image-height page)))
        (observed_width (car (gimp-image-width page)))
        (page_drawable (car (gimp-image-flatten page)))
        (thumbnail_top (car (gimp-image-duplicate page)))
        (thumbnail_top_drawable (car (gimp-image-get-active-layer thumbnail_top)))
        (thumbnail_full (car (gimp-image-duplicate page)))
        (thumbnail_full_drawable (car (gimp-image-get-active-layer thumbnail_full)))
      )
  '''+ ('''(gimp-image-scale-full page '''+ str (target_width) +''' (quotient (* '''+ str (height) +''' '''+ str (target_width) +''') '''+str (width) +''') INTERPOLATION-CUBIC)
  ; (gimp-image-convert-indexed page FIXED-DITHER MAKE-PALETTE 127 FALSE FALSE "")''' if scale_full_page else "") +'''
  (file-png-save RUN-NONINTERACTIVE page page_drawable "'''+page_outfile+'" "'+page_outfile_base+'''" 0 9 0 0 0 0 0)
  (gimp-image-delete page)
  
  (gimp-image-crop thumbnail_top (quotient '''+ str (width) +''' 2) (quotient (* 78 '''+ str (width) +''') 600) 0 0)
  (gimp-image-scale-full thumbnail_top 300 78 INTERPOLATION-CUBIC)
  ; (gimp-image-convert-indexed thumbnail_top NO-DITHER MAKE-PALETTE 63 FALSE FALSE "")
  (file-png-save RUN-NONINTERACTIVE thumbnail_top thumbnail_top_drawable "'''+thumbnail_top_outfile+'" "'+thumbnail_top_outfile_base+'''" 0 9 0 0 0 0 0)
  (gimp-image-delete thumbnail_top)
  
  (gimp-image-scale-full thumbnail_full 120 (quotient (* '''+ str (height)+''' 120) '''+str(width) +''') INTERPOLATION-CUBIC)
  ; (gimp-image-convert-indexed thumbnail_full NO-DITHER MAKE-PALETTE 63 FALSE FALSE "")
  (file-png-save RUN-NONINTERACTIVE thumbnail_full thumbnail_full_drawable "'''+thumbnail_full_outfile+'" "'+thumbnail_full_outfile_base+'''" 0 9 0 0 0 0 0)
  (gimp-image-delete thumbnail_full)
)''')
  optimize (page_outfile, True if scale_full_page else False)
  optimize (thumbnail_top_outfile)
  optimize (thumbnail_full_outfile)

#I know, I know, hard-coding file paths on my own system isn't the proper way to do this.
#In the future, I should probably make a second git repository for the comic source files.
metadata = {
"voldemorts_children": {
"path":"/n/art/voldemorts_children/",
"width": 3000, "height": 4000,
"scale_full_page": True,
},
"acobs": {
"path": "/n/art/placeholder_name_for_surreal_superhero_comic/",
"width": 576, "height": 845,
},
"people_are_wrong_sometimes": {
"path": "/n/backup_often/colby/EN197B/",
"width":2552, "height":3508,
"scale_full_page": True,
},
"studio_art": {
"path":"/n/art/studio_art/",
"scale_full_page": True,
},
}

def do_page(comic, num):
  page_dict =comics.comics_pages[comic][num]
  if comic == "studio_art":
    generate_images (metadata [comic] ["path"], page_dict ["source"], comics.comics_metadata [comic] ["abbr"] + "_" +str(page_dict["list_index"] + comics.comics_metadata [comic] ["image_url_offset"]),
      "observed_width", "observed_height", "(round (sqrt (/ (* 360000 observed_width) observed_height)))",
      "scale_full_page" in metadata [comic])
  else:
    generate_images(metadata [comic] ["path"], page_dict["xcf_base"] + ".xcf", comics.comics_metadata [comic] ["abbr"] + "_" +str(page_dict["list_index"] + comics.comics_metadata [comic] ["image_url_offset"]),metadata [comic] ["width"], metadata [comic] ["height"], comics.comics_metadata [comic] ["image_width"], "scale_full_page" in metadata [comic])

def do_pages ():
  comic = sys.argv[1]
  if len(sys.argv) > 3:
    for i in range(int(sys.argv[2]), int(sys.argv[3])+1):
      do_page(comic, i)
  else:   do_page(comic, int(sys.argv[2])) 
