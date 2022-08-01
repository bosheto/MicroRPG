
class Position:

    def __init__(self, x, y):
        self.X = x;
        self.Y = y;

    def add(self, position):
        return Position(self.X + position.X, self.Y + position.Y)
    
    def subtract(self, position):
        return Position(self.X - position.X, self.Y - position.Y)
