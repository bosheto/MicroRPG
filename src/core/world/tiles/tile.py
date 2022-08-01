from pyray import Rectangle, draw_texture_rec, Vector2, load_image, load_texture_from_image
from raylib.colors import WHITE
from core.position import Position

class Tile:
    texture_x = 0
    texture_y = 0
    texture = None

    def __init__(self, x, y, tile_x, tile_y, texture):
        self.texture_x = tile_x
        self.texture_y = tile_y
        self.position = Position(x, y)
        self.texture = texture 


    def draw(self):
        rec = Rectangle(self.texture_x * 32, self.texture_y * 32 , 32, 32)
        draw_texture_rec(self.texture, rec, Vector2(self.position.X, self.position.Y), WHITE)