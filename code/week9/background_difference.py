from py5canvas import *
import cv2

w, h = 400, 400

vin = VideoInput(size=(w, h))

background_img = np.zeros((h, w))

def setup():
    create_canvas(w, h)

def draw():
    background(0)
    img = np.array(vin.read().convert('L'))/255
    #diff_img = np.abs(img - background_img)
    diff_img = cv2.absdiff(img, background_img)
    #cv2.absdiff
    image(diff_img)

def key_pressed(key):
    global background_img
    if key == ' ':
        background_img = np.array(vin.read().convert('L'))/255

run()