from py5canvas import *

num_points = 20
spacing = 3

def setup():
    create_canvas(600, 600)

def draw():
    background(255)
    random_seed(10)

    translate(center)

    stroke(0)
    no_fill()
    line = []
    for i in range(num_points):
        angle = remap(i, 0, num_points, 0, TWO_PI)
        line.append(direction(angle))

    amount = 5
    x = 0
    while x < width: 
        begin_shape()
        for i in range(num_points):
            angle = remap(i, 0, num_points, 0, TWO_PI)
            line[i] += direction(angle)*(spacing + random(0, 1)*(amount))
            curve_vertex(line[i])
        end_shape(CLOSE)
        x += spacing

run()