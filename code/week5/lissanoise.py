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

t = 0
steps = 50

def setup():
    create_canvas(512, 512)
    background(0)
def draw():
    background(0, 10)
    #   return
    fill(255, 100)
    no_stroke()
    
    n = 200
    delta = TWO_PI / 2
    a, b = 0.25, 0.9

    for i in range(n):
        t = remap(i, 0, n, 0, TWO_PI) + frame_count*0.1
        x = noise(t * a + delta)*2-1
        y = noise(t * b)*2-1
        circle((width / 2) + x * 400, (height / 2) + y * 400, 3)

# Run the sketch
run()
