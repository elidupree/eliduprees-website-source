#!/usr/local/bin/python

import cgi
import errors

global form
form = cgi.FieldStorage()

def ensure_presence_and_uniqueness_of_and_get_field(fieldname):
  result_list = form.getlist(fieldname)
  if len(result_list) == 0:
    raise errors.WebsiteError("No '"+fieldname+"' field given.")
  elif len(result_list) > 1:
    raise errors.WebsiteError("More than one '"+fieldname+"' field given.")
  return result_list[0]
