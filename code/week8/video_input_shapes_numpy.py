from py5canvas import *
from PIL import ImageOps

w, h = 400, 400
vin = VideoInput(size=(w, h))

# Start from a black image
img = np.zeros((30, 30))

def setup():
    create_canvas(w, h)

def draw():
    global img # We ar modifying img

    background(255)
    fill(0, 128)
    no_stroke()

    # Get a new image, convert to grayscale and then numpy
    new_img = vin.read()
    new_img = new_img.resize((30,30)).convert('L')
    new_img = np.array(new_img)/255
    # Interpolate towards the new image
    img = lerp(img, new_img, 0.1)

    spacing = width/img.shape[1]
    for y in range(img.shape[0]):
        for x in range(img.shape[1]): #
            push()
            v = img[y, x] # In range 0 1
            radius =  remap(v, (0, 1), (spacing, 0.0))
            translate(x*spacing+spacing/2, y*spacing+spacing/2)
            circle(0, 0, radius)
            pop()

run()