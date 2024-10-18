from py5canvas import *

num_rows = 20
num_cols = 20
seed = 30
saving = False

def setup():
    create_canvas(800, 600)
    background(255)  # Set background to white
    frame_rate(60)

def draw():
    global seed, saving
    background(255)

    random_seed(seed)  # Set the random seed

    tile_width = width / num_cols
    tile_height = height / num_rows

    # Draw from the center of each tile
    translate(tile_width / 2, tile_height / 2)

    for i in range(num_rows):
        for j in range(num_cols):
            push()
            translate(tile_width * j, tile_height * i)
            draw_tile(i, j, tile_width, tile_height)
            pop()


def draw_tile(row, col, cell_width, cell_height):
    stroke(0)
    scale(0.5)

    choice = random_int(2) 

    if choice == 0:
        line(-cell_width, -cell_height, cell_width, cell_height)
    elif choice == 1:
        line(cell_width, -cell_height, -cell_width, cell_height)

# def key_pressed():
#     global seed, saving
#     if key == ' ':
#         saving = True
#     if key == 'a':
#         seed -= 1
#     if key == 'd':
#         seed += 1

run()
