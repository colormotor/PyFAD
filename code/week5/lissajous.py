'''
  Lissajous curve:
  https://en.wikipedia.org/wiki/Lissajous_curve
  http://paulbourke.net/geometry/harmonograph/
  - Try different parameters as show in the Wikipedia page
  - Try to animate the curve (use frame_count)
  - Experiment with modulation
  - Draw a curve replacing the circles with `begin_shape()` and `end_shape(CLOSE)` and `vertex` in the loop
  - Try to adapt ideas from the harmonograph article to the sketch
'''

from py5canvas import *

steps = 50

def setup():
    create_canvas(512, 512)

def draw():
    background(0)
    fill(255, 100)
    no_stroke()
    
    n = 300
    delta = TWO_PI / 4
    a, b = 3.0, 2.0

    for i in range(n):
        t = remap(i, 0, n, 0, TWO_PI)
        x = sin(t * a + delta)
        y = sin(t * b)
        circle((width / 2) + x * 200, (height / 2) + y * 200, 5)

# Run the sketch
run()
