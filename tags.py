
tags = {
  "lol":"Posts about laughing out loud",
  "omg":"Posts about my goodness",
}

def validate(tag_string):
  if tag_string not in tags:
    raise "Error: Using an undefined tag"

def tag_url(tag_string):
  validate(tag_string)
  return "/blog/tags/"+tag_string

def tag_link(tag_string):
  validate(tag_string)
  return '<a href="'+tag_url(tag_string)+'">'+tag_string+'</a>'
