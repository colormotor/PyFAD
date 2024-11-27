from py5canvas import *
from PIL import ImageOps

w, h = 400, 400
vin = VideoInput('fingers.mov', size=(w, h))

def setup():
    create_canvas(w, h)

def draw():
    img = vin.read()
    # Uncomment to mirror
    # img = ImageOps.mirror(img)

    image(vin.read())

run()