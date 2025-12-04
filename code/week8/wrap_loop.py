from py5canvas import *

num_frames = 100

def setup():
    create_canvas(400, 400)
    fill(255, 70)
    stroke(255)
    
    num_movie_frames(num_frames)
    frame_rate(60)

def draw_object(x, y, w):
    push_matrix()
    translate(x, y)
    # Draw something else here
    circle(0, 0, w)
    pop_matrix()

def draw():
    background(0)
    w = 40
    # We want the shape to fully disappear 
    # so the desired range is:
    wrap_dist = width+w*2
    # Draw multiple circles
    n = 10
    for i in range(n):
        # Offset of the circle on the range
        x = remap(i, 0, n, 0, wrap_dist)
        # We add the offset and modulo the result to wrap
        draw_object((frame_count + x)%wrap_dist - w, 
               height/2, 40)

    
run()