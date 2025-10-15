from py5canvas import *

# This example also uses a "naive" custom random number generator to demonstrate the use of seeds for reproducibility
# Dont use in your code simply replace with random() and random_seed()
my_seed = 10
def my_random_seed(value):
    random_seed(value) # The built-in random seed function
    global my_seed
    my_seed = value

def my_random(a=0, b=1):
    #return random(a, b) # Replace with built-in random function
    global my_seed
    #my_seed = my_seed + 1 # Simply incrementing the seed is not a good idea
    my_seed = (my_seed * 9301 + 49297) % 167449 
    return (my_seed%233280 / 233280) * (b - a) + a

def setup():
    create_canvas(400, 400)
    frame_rate(60)

def draw():
    my_random_seed(101)
    background(0)
    # Origin at center
    translate(width/2, height/2)
    # Sun
    fill(255, 128, 0)
    circle(0, 0, 40)

    for i in range(5):
        dist = 70 + i*30
        no_fill()
        stroke(255, 50)
        circle(0, 0, dist*2)

        no_stroke()
        push_matrix() # Save current transformation
        rotate(radians(random(0, 360)) + frame_count*my_random(0.001, 0.05))
        translate(dist, 0)
        fill(0, 150, 200)
        circle(0, 0, random(5, 10))
        pop_matrix() # Restore last saved transformation

run()