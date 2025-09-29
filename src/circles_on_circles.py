from py5canvas import *

def setup():
    size(800, 800)
    
def draw_circle_on_circle(layout_angle, center, radius):
    begin_shape()
    for angle in linspace(0, TWO_PI, 5, False):
        r = remap(sin(angle*2 + layout_angle*4), -1, 1, radius*0.4, radius)        
        p = direction(angle)*r + center
        curve_vertex(p)
    end_shape(CLOSE)

def draw():
    t = frame_count / 1000
    
    background(255)
    no_fill()
    stroke(0, 128)
    
    translate(width / 2, height / 2)
    
    num_circles = 170
    layout_radius = width*0.2
    circle_radius = 250

    # Iterate over angles that cover a circle (0 to TWO_PI)
    # For each circle draw 
    for angle in linspace(0, TWO_PI, num_circles, False):
        center = direction(angle)*layout_radius
        # Same as 
        # center = Vector(cos(angle),
        #                 sin(angle))*layout_radius
        draw_circle_on_circle(angle, center, circle_radius)        

def key_pressed(key):
    if key == ' ':
        save('circles.svg')
        
run()