from core.tile import Tile

class Chunk:

    def __init__(self, x, y, texture):

        self.x = x
        self.y = y

        w, h = 8, 8
        self.texture = texture
        self.chunk = [[Tile(self.x + ix * 32,self.y + iy * 32 ,3 ,0 ,self.texture) for ix in range(w)] for iy in range(h)]

    def draw(self):
        for y in range(8):
            for x in range(8):
                self.chunk[y][x].draw()

