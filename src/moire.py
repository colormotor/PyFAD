#!/usr/bin/env python3
from py5canvas import *

def setup():
    create_canvas(400, 400)
    background(0)
    frame_rate(60)

def draw():
    background(0)
    no_fill()
    stroke(255)
    stroke_weight(1.5)

    # Center the drawing
    translate(width / 2, height / 2)

    # # Draw the first set of rotating vertical lines
    push_matrix()
    rotate(radians(frame_count))
    line_sequence(-width, width, 7, width)
    pop_matrix()

    # # Draw the second set of rotating vertical lines
    push_matrix()
    rotate(radians(-frame_count*0.8))
    line_sequence(-width, width, 7, width)
    pop_matrix()

def key_pressed():
    save('test.pdf')
    
def line_sequence(x0, x1, spacing, height):
    x = x0
    while x < x1:
        line(x, -height, x, height)
        x += spacing
    
run()
