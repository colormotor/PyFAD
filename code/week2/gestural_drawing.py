from py5canvas import *

amt = 0.1
brush_x = 0.0
brush_y = 0.0

def setup():
    create_canvas(512, 512)
    background(0)

def draw():
    # Allow to modify brush_x and brush_y
    global brush_x, brush_y
    # horizontal and vertical displacement
    dx = (mouse_x - brush_x) * amt 
    dy = (mouse_y - brush_y) * amt
    # update position
    brush_x = brush_x + dx
    brush_y = brush_y + dy
    d = dist(brush_x, brush_y, brush_x + dx, brush_y + dy)
    scale_factor = remap(d, 0, 50, 0.1, 1.0)
    if dragging:
        angle = atan2(dy, dx)
        line(brush_x, brush_y,  brush_x+dx, brush_y+dy);
        push_matrix()
        translate(brush_x, brush_y);
        rotate(angle);
        scale(scale_factor);
        triangle(0, -50, 100, 0, 0, 50);
        pop_matrix()
        #circle(brush_x, brush_y, 50*scale_factor)

run()