from py5canvas import *

def setup():
    create_canvas(512, 512)

def draw():
    background(0)
    y = sin(frame_count*0.01)*height*0.5
    circle(width/2, 
           height/2 + y,
           100)
    print(frame_count)
    
run()