from core.entity.entity import Entity
from core.position import Position
from pyray import KeyboardKey
from pyray import is_key_down

class Player(Entity):

    def __init__(self, position, texture):
        Entity.__init__(self, position, 10, 10, 0.1 , 0, 1, texture)

    def move(self):
        
        if is_key_down(KeyboardKey.KEY_W):
            self.position = Position(self.position.X, self.position.Y - self.speed)
            
        if is_key_down(KeyboardKey.KEY_S):
            self.position = Position(self.position.X, self.position.Y + self.speed)
        
        if is_key_down(KeyboardKey.KEY_A):
            self.position = Position(self.position.X - self.speed, self.position.Y)

        if is_key_down(KeyboardKey.KEY_D):
            self.position = Position(self.position.X + self.speed, self.position.Y)

        
        Entity.move(self, self.position)