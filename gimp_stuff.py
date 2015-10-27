#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division


import subprocess
import shlex

def gimp_batch(command):
  commandp = "gimp --no-interface --batch="+shlex.quote(command)+" --batch='(gimp-quit 0)'"
  print("calling:\n"+commandp)
  out = subprocess.Popen(commandp, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
  output = out.communicate()
  print(output)
  print("finished GIMP batch command")
  #print("gimp --no-interface --batch='"+command+"'")

def generate_vc_images(xcf_basename, page_number):
  generate_images("/n/art/voldemorts_children/", xcf_basename+".xcf", "VC_"+str(page_number))

def generate_images(infile_path, infile_base, outfile_base):
  output_dir = "./media/generated_from_source_files/"
  infile = infile_path+infile_base
  page_outfile_base = outfile_base+".png"
  page_outfile = output_dir+page_outfile_base
  thumbnail_top_outfile_base = outfile_base+"_thumbnail_top.png"
  thumbnail_top_outfile = output_dir+thumbnail_top_outfile_base
  thumbnail_full_outfile_base = outfile_base+"_thumbnail_full.png"
  thumbnail_full_outfile = output_dir+thumbnail_full_outfile_base
  
  gimp_batch('''
(let* (
        (page (car (gimp-file-load RUN-NONINTERACTIVE "'''+infile+'" "'+infile_base+'''")))
        (page_drawable (car (gimp-image-flatten page)))
        (thumbnail_top (car (gimp-image-duplicate page)))
        (thumbnail_top_drawable (car (gimp-image-get-active-layer thumbnail_top)))
        (thumbnail_full (car (gimp-image-duplicate page)))
        (thumbnail_full_drawable (car (gimp-image-get-active-layer thumbnail_full)))
      )
  (gimp-image-scale-full page 750 1000 INTERPOLATION-CUBIC)
  (gimp-image-convert-indexed page FIXED-DITHER MAKE-PALETTE 127 FALSE FALSE "")
  (file-png-save RUN-NONINTERACTIVE page page_drawable "'''+page_outfile+'" "'+page_outfile_base+'''" 0 9 0 0 0 0 0)
  (gimp-image-delete page)
  
  (gimp-image-crop thumbnail_top 1500 390 0 0)
  (gimp-image-scale-full thumbnail_top 300 78 INTERPOLATION-CUBIC)
  (gimp-image-convert-indexed thumbnail_top NO-DITHER MAKE-PALETTE 63 FALSE FALSE "")
  (file-png-save RUN-NONINTERACTIVE thumbnail_top thumbnail_top_drawable "'''+thumbnail_top_outfile+'" "'+thumbnail_top_outfile_base+'''" 0 9 0 0 0 0 0)
  (gimp-image-delete thumbnail_top)
  
  (gimp-image-scale-full thumbnail_full 120 160 INTERPOLATION-CUBIC)
  (gimp-image-convert-indexed thumbnail_full NO-DITHER MAKE-PALETTE 63 FALSE FALSE "")
  (file-png-save RUN-NONINTERACTIVE thumbnail_full thumbnail_full_drawable "'''+thumbnail_full_outfile+'" "'+thumbnail_full_outfile_base+'''" 0 9 0 0 0 0 0)
  (gimp-image-delete thumbnail_full)
)''')

