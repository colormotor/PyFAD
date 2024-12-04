from py5canvas import *
import cv2

w, h = 400, 400

vin = VideoInput('fingers.mov', size=(w, h))
first_frame = None

def find_contours(im, invert=True, thresh=127):
    ''' Utility function to get contours compatible with py5canvas.
    Assumes a grayscale image as a result'''
    _, thresh_img = cv2.threshold(im, thresh, 256, int(invert))
    thresh_img = cv2.dilate(thresh_img, np.ones((5,5), dtype=np.uint8))
    contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    S = []
    for ctr in contours:
        S.append(np.vstack([ctr[:,0,0], ctr[:,0,1]]).T)
    return S


def setup():
    create_canvas(w, h)

def draw():
    global first_frame
    background(0)
    img = vin.read().convert('L')
    img = np.array(img)
    if first_frame is None:
        first_frame = img
    #img = np.maximum(img - first_frame, 0)
    contours = find_contours(img)
    image(img)
    stroke(255, 0, 0)
    fill(0, 128)
    shape(contours, close=True)

run()