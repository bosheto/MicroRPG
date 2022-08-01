import pyray
from pyray import BLACK, BLUE
from core.world.chunk import Chunk

# Initialization
SCREEN_WIDTH = 1240
SCREEN_HEIGHT = 800

pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT,'MicroRPG')
pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second

img = pyray.load_image("src/assets/SpriteSheet.png")
texture = pyray.load_texture_from_image(img)

c = Chunk(0,0, texture)
c2 = Chunk(16 * 32, 0, texture)
c3 = Chunk(32 * 32, 0, texture)
# Main game loop
while not pyray.window_should_close():  # Detect window close button or ESC key
    # Update
    # TODO: Update your variables here


    # Draw
    pyray.begin_drawing()
    pyray.clear_background(BLACK)
    c.draw()
    c2.draw()
    c3.draw()
    pyray.draw_text('8', 4,50, 10, BLUE)
    pyray.end_drawing()


# De-Initialization
pyray.close_window()  # Close window and OpenGL context
