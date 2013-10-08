#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division


import subprocess

def gimp_batch(command):
  #print("calling GIMP batch command..."+command)
  #out = subprocess.Popen(["gimp", "--no-interface", "--batch='"+command+"'"], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
  #out.wait()
  #print(out.communicate())
  #print("finished GIMP batch command...")
  print("gimp --no-interface --batch='"+command+"'")

def generate_vc_images(xcf_basename, page_number):
  generate_images("/n/art/voldemorts_children/", xcf_basename+".xcf", "VC_"+str(page_number))

def generate_images(infile_path, infile_base, outfile_base):
  infile = infile_path+infile_base
  page_outfile_base = outfile_base+".png"
  page_outfile = "./build/media/"+page_outfile_base
  thumbnail_outfile_base = outfile_base+"_thumbnail.png"
  thumbnail_outfile = "./build/media/"+thumbnail_outfile_base
  
  gimp_batch('''
(let* (
        (page (car (gimp-file-load RUN-NONINTERACTIVE "'''+infile+'" "'+infile_base+'''")))
        (pdrawable (car (gimp-image-flatten page)))
        (thumbnail (car (gimp-image-duplicate page)))
        (tdrawable (car (gimp-image-get-active-layer thumbnail)))
      )
  (gimp-image-scale-full page 750 1000 INTERPOLATION-CUBIC)
  (gimp-image-convert-indexed page FIXED-DITHER MAKE-PALETTE 127 FALSE FALSE "")
  (file-png-save RUN-NONINTERACTIVE page pdrawable "'''+page_outfile+'" "'+page_outfile_base+'''" 0 9 0 0 0 0 0)
  (gimp-image-delete page)
  
  (gimp-image-crop thumbnail 3000 780 0 0)
  (gimp-image-scale-full thumbnail 300 78 INTERPOLATION-CUBIC)
  (gimp-image-convert-indexed thumbnail NO-DITHER MAKE-PALETTE 63 FALSE FALSE "")
  (file-png-save RUN-NONINTERACTIVE thumbnail tdrawable "'''+thumbnail_outfile+'" "'+thumbnail_outfile_base+'''" 0 9 0 0 0 0 0)
  (gimp-image-delete thumbnail)
)''')

