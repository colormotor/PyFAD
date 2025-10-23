from py5canvas import *

num_points = 20
spacing = 5

circle(10, 10, 20)


def setup():
    create_canvas(600, 600)

def draw():
    random_seed(10)
    background(255)
    translate(center)

    stroke(0)
    no_fill()
    
    angles = linspace(0, PI*2, num_points, False)
    line = []
    for angle in angles:
        line.append(direction(angle))

    radius = 50
    amount = 5 #remap(mouse_x, 0, width, 0.0, 10.0)
    while radius < width: 
        begin_shape()
        for i in range(num_points):
            line[i] += direction(angles[i])*(random(0, 1)*amount + spacing)
            curve_vertex(line[i])
        end_shape(CLOSE)
        radius += spacing

run()