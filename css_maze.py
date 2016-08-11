import math
wallcolor="#00ffff"

def positionstyle(x,y,neg=False):
  return 'left: '+("-" if neg else "")+str(x*3)+'em; top: '+("-" if neg else "")+str(y*3)+'em;'

def youlose(x,y):
  return '<div class="wholebox youlose" style="'+positionstyle(x,y,True)+'">You lost! Return to start</div>'

def wall(x,y):
  return '<div class="wall" style="'+positionstyle(x,y)+'">'+youlose(x,y)+'</div>'
  
def key(contents):
  return '<div class="key" style="'+positionstyle(x,y)+'"><div class="wholebox keybox" style="'+positionstyle(x,y,True)+'">'+contents+'</div></div>'

def reward_sparkles(angle):
  return '<div class="sparkles" style="left:'+str(math.cos(angle)*40+50)+'%; top:'+str(math.sin(angle)*40+50)+'%;"></div>'

print('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>CSS Maze!</title>
    <style type="text/css">
div.gamearea {
  position: relative;
  margin: 5em auto;
  width: 30em;
  height: 30em;
}
div.wall {
  position: absolute;
  background-color: '''+wallcolor+''';
  height: 3em;
  width: 3em;
  z-index: 10;
}
div.wholebox {
  position: absolute;
  height: 30em;
  width: 30em;
}
div.youlose {
  display: none;
  background-color: '''+wallcolor+''';
  color: black;
  text-align: center;
  z-index: 100;
}
div.keybox {
}
body,html,marquee {height:100%;}
div.key div.door { display: }
div.wall:hover>div.youlose { display: block; }
div.reward {height:100%; width:1px; display:inline-block; background-color:red;}
div.sparkles {height:3em; width:3em; margin: -1.5em; border-radius:1.5em; background-color:green; z-index: 400; display:none; position: absolute;}
div.reward:hover div.sparkles {display:block; }
    </style>
  </head>
  <body>
    <marquee>'''+''.join(['<div class="reward">'+reward_sparkles(x/500)+reward_sparkles(x/500+math.pi*2/3)+reward_sparkles(x/500+math.pi*4/3)+reward_sparkles(x/300)+reward_sparkles(x/300+math.pi*2/3)+reward_sparkles(x/300+math.pi*4/3)+'</div>' for x in range(0,6283)])+'''</marquee>
    <div class="gamearea">'''+wall(2,0)+wall(3,0)+wall(0,2)+wall(0,3)+'''</div>
  </body>
</html>''')
