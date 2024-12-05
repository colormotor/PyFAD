from py5canvas import *
import cv2

w, h = 400, 400

vin = VideoInput(size=(w, h))

particles = []

previous_img = np.zeros((h, w))

def setup():
    create_canvas(w, h)

def draw():
    global previous_img, particles
    background(0)
    img = np.array(vin.read().convert('L'))/255
    # diff_img = np.abs(img - background_img)
    diff_img = cv2.absdiff(img, previous_img)
    previous_img = img
    image(diff_img)

    if frame_count > 0:
        # Get rid of "dead" particles:
        # Creates a new list, 
        # re-adding a particle only if the condition on the end is True
        particles = [p for p in particles if p.life >= 0]
        
        # Add new particle in brightest spot 
        if len(particles) < 200:
            # Slow version
            # Uses loops so will hog framerate
            # max_row = 0
            # max_col = 0
            # max_val = 0
            # for i in range(diff_img.shape[0]):
            #     for j in range(diff_img.shape[1]):
            #         # If pixel brightness more than max,
            #         # store new max and indices of pixel
            #         if diff_img[i, j] > max_val:
            #             max_val = diff_img[i, j]
            #             max_row = i
            #             max_col = j

            # Fast version, using numpy "vectorized operations"
            # max_row_vals = np.max(diff_img, axis=1)
            # max_row = np.argmax(max_row_vals) 
            # max_col_vals = np.max(diff_img, axis=0)  
            # max_col = np.argmax(max_col_vals)
            # max_val = diff_img[max_row, max_col]

            # Even more concise version
            max_row, max_col = np.unravel_index(np.argmax(diff_img), diff_img.shape)
            max_val = diff_img[max_row, max_col]

            if max_val > 0.4:
                particles.append(Particle([max_col, max_row]))

    for p in particles:
        p.update(1/60)
        p.draw()

run()

class Particle:
    def __init__(self, pos, lifetime=3.0):
        self.lifetime = lifetime
        self.life = self.lifetime
        self.reset(pos)

    def reset(self, pos):
        self.pos = np.array(pos).astype(np.float64)
        self.vel = np.zeros(2)
        angle = -PI/2 + np.random.uniform(-1, 1)*0.2
        self.acc = np.array([np.cos(angle), np.sin(angle)])*400*np.random.uniform(0.5, 1.0)
        self.life = self.lifetime
    
    def update(self, dt, force=np.zeros(2)):
        self.acc += force
        self.acc += Vector(0, 9.8) # Gravity
        self.vel += self.acc*dt 
        self.pos += self.vel*dt
        self.life -= dt
        
    def draw(self):
        fill(255, 255*(self.life/self.lifetime))
        circle(self.pos, 5)

