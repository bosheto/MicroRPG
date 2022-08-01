from core.constants import *

class Position:

    def __init__(self, x, y):
        self.X = x;
        self.Y = y;

    def add(self, position):
        return Position(self.X + position.X, self.Y + position.Y)
    
    def subtract(self, position):
        return Position(self.X - position.X, self.Y - position.Y)

    @classmethod
    def to_world_pos(self, x, y):
        return Position(x / SPRITE_SIZE, y / SPRITE_SIZE)

    @classmethod
    def to_screen_pos(self, position):
        return Position(position.X * SPRITE_SIZE, position.Y * SPRITE_SIZE)