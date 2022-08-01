from pyray import Rectangle, draw_texture_rec, Vector2, load_image, load_texture_from_image
from raylib.colors import WHITE
from core.position import Position
from core.constants import SPRITE_SIZE

class Tile:
    texture_x = 0
    texture_y = 0
    texture = None

    def __init__(self, x, y, tile_x, tile_y, texture):
        self.texture_x = tile_x
        self.texture_y = tile_y
        self.position = Position(x * SPRITE_SIZE, y * SPRITE_SIZE)
        self.texture = texture 


    def draw(self):
        rec = Rectangle(self.texture_x * SPRITE_SIZE, self.texture_y * SPRITE_SIZE , SPRITE_SIZE, SPRITE_SIZE)
        draw_texture_rec(self.texture, rec, Vector2(self.position.X, self.position.Y), WHITE)