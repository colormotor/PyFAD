'''
TASKS:
- comment/uncomment the increment of `amp_mod_phase` to stop/start the animation
- experiment with different values for amp_mod_phase and carrier_freq to develop your understanding of how the sketch works
- experiment with different values of amp_mod_freq to get a good understanding of what is going on
'''
from py5canvas import *

amp_mod_phase = 2.5 
amp_mod_freq = 0.01
carrier_freq = 0.05

def setup():
    create_canvas(400, 400)

def draw():
    global amp_mod_phase
    
    background(0)
    no_fill()
    stroke(255)
    translate(0, height / 2)
    
    begin_shape()
    for x in range(width):
        amp = sin(x * amp_mod_freq + amp_mod_phase)*100
        y = sin(x * carrier_freq)*amp
        vertex(x, y)
    end_shape()
    
    amp_mod_phase += 0.05

# Run the sketch
run()
