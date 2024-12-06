from py5canvas import *
import cv2

w, h = 400, 400

vin = VideoInput(size=(w, h))

class Snake:
    def __init__(self):
        self.points = []
        self.color = np.zeros(3)
        
    def track_image(self, img, thresh):
        # Unusably slow! 
        # pts = []
        # for i in range(img.shape[0]):
        #     for j in range(img.shape[1]):
        #         if dist(img[i,j], self.color) < thresh:
        #             pts.append(np.array([j,i]))
        # Generated with the prompt:
        # "This numpy code, can you vectorize it:"
        # Followed by the code block above

        # Calculate the distances for all pixels in the image
        distances = np.linalg.norm(img - self.color, axis=2)
        # Create a mask for the pixels within the threshold
        mask = distances < thresh
        # Get the coordinates of the pixels that satisfy the condition
        pts = np.column_stack(np.where(mask))

        # End ChatGPT

        if debug:
            # Mask is a "boolean" image made of True and False
            # We can convert it to a viewable float image like this
            image(mask.astype(np.float32))

        if len(pts):
            average = sum(pts)/len(pts)
            self.add_point([average[1], average[0]])

    def add_point(self, p):
        self.points.append(p)
        if len(self.points) > 200:
            self.points.pop(0)

    def draw(self):
        if self.points:
            polyline(self.points)
            circle(self.points[-1], 5)

snake = Snake()
debug = True

def setup():
    create_canvas(w, h)

def draw():
    background(0)
    img = np.array(vin.read()) / 255

    if dragging:
        mx = int(mouse_x)
        my = int(mouse_y)
        if (mx >= 0 and mx < img.shape[1] and 
            my >= 0 and my < img.shape[0]):
            snake.color = img[my, mx]
    
    image(img)

    snake.track_image(img, 0.05)
    no_fill()
    stroke(255)
    snake.draw()

def key_pressed(key):
    global debug
    if key == ' ':
        debug = not debug

run()