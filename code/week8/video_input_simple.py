from py5canvas import *
from PIL import ImageOps

w, h = 400, 400
# Remove 'fingers.mov ,' to use webcam
vin = VideoInput('fingers.mov', size=(w, h))

def setup():
    create_canvas(w, h)

def draw():
    img = vin.read()
    image(img)

run()