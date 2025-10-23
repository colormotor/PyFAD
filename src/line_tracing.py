from py5canvas import *

num_points = 20
spacing = 3

def setup():
    create_canvas(600, 600)

def draw():
    background(255)
    random_seed(10)
    #background(255)
    stroke(0)
    no_fill()
    line = []
    for i in range(num_points):
        y = remap(i, 0, num_points-1, 0, height)
        line.append(vector(-spacing, y))

    amount = 5
    x = 0
    while x < width: 
        begin_shape()
        for i in range(num_points):
            line[i] += vector(random(0, 1)*amount + spacing, 0)
            curve_vertex(line[i])
        end_shape()
        x += spacing

run()