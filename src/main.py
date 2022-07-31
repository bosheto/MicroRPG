import pyray
from pyray import BLACK, BLUE


# Initialization
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT,'MicroRPG')
pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second


# Main game loop
while not pyray.window_should_close():  # Detect window close button or ESC key
    # Update
    # TODO: Update your variables here


    # Draw
    pyray.begin_drawing()
    pyray.clear_background(BLACK)
    pyray.draw_text('8', 4,50, 10, BLUE)
    pyray.end_drawing()


# De-Initialization
pyray.close_window()  # Close window and OpenGL context
