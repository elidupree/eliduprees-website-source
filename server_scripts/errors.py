#!/usr/local/bin/python

import datetime
import os
import traceback

class WebsiteError(Exception):
  def __init__(self, error_message):
    # Logging here, rather than logging in every except: clause that handles this exception, is a hack, but since it's essentially internal debugging code, it's an acceptable hack.
    try:
      with open("/home/private/logs/all_website_errors", "a") as error_log:
        error_log.write(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")+": "+os.environ.get('SCRIPT_NAME', "unknown script")+": "+error_message+"\n")
    except IOError:
      error_message = error_message + "; additional error while trying to log the error in a file"
    self.error_message = error_message

def UncaughtError():
  error_message = "Unexpected error in "+os.environ.get('SCRIPT_NAME', "unknown script")+": "+traceback.format_exc()
  # Hack: Logging (we construct a website error but don't raise it)
  WebsiteError(error_message)
  return error_message

def ajax_error_message(error_message):
  # This is no official format; I simply have my scripts check for messages beginning with "ERROR: "
  return '''Content-type: text/plain; charset=utf-8

ERROR: ''' + error_message

def ajax_or_error(ajax_func):
  try:
    return ajax_func()

  except WebsiteError as e:
    return ajax_error_message(e.error_message)

  except:
    return ajax_error_message(UncaughtError())

