import pyray
from pyray import BLACK, BLUE
from core.world.chunk import Chunk
from core.constants import *
from core.entity import *
from core.position import Position
from core.world.overworld import World

# Initialization
pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT,'MicroRPG')
pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second

img = pyray.load_image("src/assets/SpriteSheet.png")
texture = pyray.load_texture_from_image(img)

c = Chunk(Position(0, 0), texture)
# c2 = Chunk(CHUNK_SIZE, 0, texture)
# c3 = Chunk(CHUNK_SIZE * 2, 0, texture)
# c4 = Chunk(0,CHUNK_SIZE, texture)

player = Player(Position.to_world_pos((SCREEN_WIDTH /2) ,( SCREEN_HEIGHT /2) ), texture)
# player = Player(Position(0,0), texture)

world = World(1233, player.position, texture)

# Main game loop
while not pyray.window_should_close():  # Detect window close button or ESC key
    # Update
    # TODO: Update your variables here
    player.move()

    # Draw
    pyray.begin_drawing()
    pyray.clear_background(BLACK)
    world.draw()
    #c.draw()
    # c2.draw()
    # c3.draw()
    # c4.draw()
    player.draw()
    pyray.end_drawing()


# De-Initialization
pyray.unload_texture(texture)
pyray.unload_image(img)
pyray.close_window()  # Close window and OpenGL context
