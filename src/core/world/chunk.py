from core.world.tiles.grass_tile import GrassTile
from core.world.tiles.stone_tile import StoneTile
from core.world.tiles.sand_tile import SandTile


import opensimplex

class Chunk:

    def __init__(self, x, y, texture):
        
        opensimplex.seed(123)
        
        self.x = x
        self.y = y
        self.w, self.h = 8, 8
        self.texture = texture
        self.chunk = []
        self.__generate_chunk()
    
    def draw(self):
        for y in range(8):
            for x in range(8):
                self.chunk[y][x].draw()

    def __generate_chunk(self):
        for y in range(self.h):
            
            row = []
            for x in range(self.w):                
                n = opensimplex.noise2(self.x+ x, self.y + y)
                row.append(self.__get_tile(x, y))

            self.chunk.append(row)

    def __get_tile(self, x, y):
        n = opensimplex.noise2(self.x+ x, self.y + y)

        if n < 0.01:
            return SandTile(self.x + x * 32,self.y + y * 32 ,self.texture)
        elif n < 0.2:
            return GrassTile(self.x + x * 32,self.y + y * 32 ,self.texture)
        else:
            return StoneTile(self.x + x * 32,self.y + y * 32 ,self.texture)
