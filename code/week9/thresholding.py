from py5canvas import *
import cv2

w, h = 400, 400

vin = VideoInput('fingers.mov', size=(w, h))

def setup():
    create_canvas(w, h)

def draw():
    background(0)
    img = vin.read().convert('L')
    levels = np.array(img.quantize(2))
    img = np.array(img)
    # The cv2.threshold function returns two values, we are interested only in the second
    # so we can use the _ symbol to just capture the value we are not interested in
    _, img2 = cv2.threshold(img, 128, 255, 0) # the last parameter set to 1 inverts the result
    image(img2)

run()