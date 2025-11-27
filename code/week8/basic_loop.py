#!/usr/bin/env python3
from py5canvas import *

num_frames = 300

def setup():
    create_canvas(512, 512)
    # You can set it from UI also
    num_movie_frames(num_frames)

def draw():
    background(0)
    translate(center)
    fill(255)
    no_stroke()

    # One cycle for the loop duration
    anim_angle = TWO_PI*(frame_count/num_frames)
    rotate(anim_angle)
    circle(200, 0, 50)
    

run()
