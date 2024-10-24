from py5canvas import *

num_points = 20
spacing = 5

def setup():
    create_canvas(600, 600)

def draw():
    random_seed(10)
    background(255)
    stroke(0)
    no_fill()
    line = []
    for y in linspace(0, height, num_points):
        line.append(Vector(-spacing, y))

    amount = 5 #remap(mouse_x, 0, width, 0.0, 10.0)
    x = 0
    while x < width+spacing: 
        begin_shape()
        for i in range(num_points):
            line[i] += Vector(random(0, 1)*amount + spacing, 0)
            curve_vertex(line[i])
        end_shape()
        x += spacing
run()