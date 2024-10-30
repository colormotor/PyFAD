
'''
TASK
- experiment with changing the values of amplitude and frequency. 
= Change how much input is incremented by. 
    - Observe the results and try to understand how each part of the code functions.
- adapt the code so that phase_inc controls how much of the sine function is rendered by the circles
- experiment with different values of phase_inc
'''

from py5canvas import *

def setup():
    create_canvas(500,500)

def draw():
    background(0);
    fill(255);

    translate(0, height/2) # translate the coordinate space to center it around the y origin

    amplitude = 100
    frequency = 0.1
    t = (frame_count/60)*TWO_PI # Assumes 60 frames per second
    for i in range(20):
        phase = i  # the phase increases for each circle
        y = sin(t * frequency + phase) * amplitude # calculate the y position
        circle(i * width/20, y, 10)
    
run()
