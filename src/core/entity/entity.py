from core.position import Position
from pyray import Rectangle, draw_texture_rec, Vector2, load_image, load_texture_from_image
from raylib.colors import WHITE
from core.constants import SPRITE_SIZE

class Entity:

    def __init__(self, position, hp, mp, speed, sprite_x, sprite_y, texture):
        self.position = position
        self.hp = hp
        self.mp = mp 
        self.speed = speed
        self.texture_x = sprite_x
        self.texture_y = sprite_y
        self.texture = texture

    def draw(self):
        pos = Position.to_screen_pos(self.position)
        rec = Rectangle(self.texture_x * SPRITE_SIZE,  self.texture_y * SPRITE_SIZE, SPRITE_SIZE, SPRITE_SIZE)
        draw_texture_rec(self.texture, rec, Vector2(pos.X, pos.Y), WHITE)

    def move(self, position):
        self.position = position