from py5canvas import *

amt = 0.1
brush_pos = Vector(0, 0)
positions = []
offsets = []

def setup():
    create_canvas(512, 512)
    background(0)

def draw():
    background(0)

    # Allow to modify brush_pos
    global brush_pos
    # Brush displacement vector (x and y)
    # It moves the brush position by a small amount in the direction of the mouse
    offset = (mouse_pos - brush_pos)*amt
    # Update the brush position
    brush_pos = brush_pos + offset

    if dragging:
        positions.append(brush_pos)
        offsets.append(offset)

    if len(positions) > 200:
        positions.pop(0)
        offsets.pop(0)

    num_positions = len(positions)
    for i in range(num_positions):
        pos = positions[i]
        offset = offsets[i]
        # Get the scale based on speed of mouse movement (distance covered by offset)
        speed = mag(offset)
        # Remap speed to a scale factor
        scale_factor = remap(speed, 0, 50, 0.1, 1.0)
        
        # Draw a line in the direction of movement
        stroke(255, 60)
        line(pos, pos + offset*8)
        # Rotate a triangle based on the orientation of the movement vector
        stroke(0)
        push()
        translate(pos)
        rotate(heading(offset))
        scale(scale_factor)
        triangle(0, -50, 100, 0, 0, 50);
        pop()
        
def key_pressed(key):
    if key == ' ':
        save('brush.pdf')
        
run(show_toolbar=True)