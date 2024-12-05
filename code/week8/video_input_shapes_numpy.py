from py5canvas import *
from PIL import ImageOps

# brush_x = brush_x + (mouse_x - brush_x)*0.1
# brush_x = lerp(brush_x, mouse_x, 0.1)

w, h = 400, 400
vin = VideoInput(size=(w, h))

# Start from a black image
img = np.zeros((w, h))

def setup():
    create_canvas(w, h)

def draw():
    global img # We ar modifying img

    background(255)
    fill(0, 128)
    no_stroke()

    # Get a new image, convert to grayscale and then numpy
    new_img = vin.read() # PIL Image
    new_img = new_img.convert('L')
    new_img = np.array(new_img)/255
    
    # Interpolate towards the new image
    img = lerp(img, new_img, 0.1)
    image(img)

    return

    spacing = width/img.shape[1]
    for y in range(img.shape[0]):
        for x in range(img.shape[1]): #
            push()
            v = img[y, x] # In range 0 1
            radius =  remap(v, (0, 1), (spacing*2, 0.0))
            translate(x*spacing+spacing/2, y*spacing+spacing/2)
            circle(0, 0, radius)
            pop()

run()