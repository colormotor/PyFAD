from py5canvas import *

def setup():
    create_canvas(512, 512)

def draw():
    background(0)
    circle(width/2, height/2, 100)

run()