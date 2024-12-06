''' Basic OSC functionality demo
Will require installing pythonosc (in your env!!) with 

pip install python-osc

An OSC server and client are started up automatically by py5sketch.
By default, the client will run on localhost with port 9998,
and the server will listen on port 9999
You can configure these by creating an `osc.json` file that is located in the same directory as the script
a default setup would look like this
{
    'server port': 9999,
    'client address': 'localhost',
    'client port': '9998'
}
These parameters will not change until you restart py5sketch
'''
from py5canvas import *

bg = 255

def setup():
    create_canvas(512, 512)

def draw():
    background(bg)
    send_osc('/value', sin(frame_count/100))

def received_osc(addr, val):
    global bg
    print('recv')
    if 'bg' in addr:
        bg = val

def key_pressed(key):
    print('Sending osc')
    send_osc('/value', 10.0)
run()