from py5canvas import *

amt = 0.1
brush_pos = Vector(0, 0)

def setup():
    create_canvas(512, 512)
    background(0)

def draw():
    # Allow to modify brush_pos
    global brush_pos
    # Brush displacement vector (x and y)
    # It moves the brush position by a small amount in the direction of the mouse
    offset = (mouse_pos - brush_pos)*amt
    # Update the brush position
    brush_pos = brush_pos + offset
    # Get the scale based on speed of mouse movement (distance covered by offset)
    speed = mag(offset)
    # Remap speed to a scale factor
    scale_factor = remap(speed, 0, 50, 0.1, 1.0)
    if dragging:
        # Draw a line in the direction of movement
        stroke(255, 60)
        line(brush_pos, brush_pos + offset*8)
        # Rotate a triangle based on the orientation of the movement vector
        stroke(0)
        push()
        translate(brush_pos)
        rotate(heading(offset));
        scale(scale_factor);
        triangle(0, -50, 100, 0, 0, 50);
        pop()
        
run()