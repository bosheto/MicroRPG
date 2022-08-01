# from core.world.tiles.grass_tile import GrassTile
# from core.world.tiles.stone_tile import StoneTile
# from core.world.tiles.sand_tile import SandTile

from core.world.tiles import *
from core.position import Position
from core.constants import CHUNK_SIZE

import opensimplex

class Chunk:

    def __init__(self, x, y, texture):
        
        # opensimplex.seed(123)
        opensimplex.random_seed()
        self.position = Position(x, y) 
        self.w, self.h = CHUNK_SIZE, CHUNK_SIZE
        self.texture = texture
        self.chunk = []
        self.__generate_chunk()
    
    def draw(self):
        for y in range(self.h):
            for x in range(self.w):
                self.chunk[y][x].draw()

    def __generate_chunk(self):
        for y in range(self.h):
            
            row = []
            for x in range(self.w):                
                row.append(self.__get_tile(x, y))

            self.chunk.append(row)

    def __get_tile(self, x, y):
        pos = self.position.add(Position(x,y))
        n = opensimplex.noise2(pos.X, pos.Y)


        if n < 0.01:
            return SandTile(self.position.X + x ,self.position.Y + y ,self.texture)
        elif n < 0.2:
            return GrassTile(self.position.X + x ,self.position.Y + y  ,self.texture)
        else:
            return StoneTile(self.position.X + x ,self.position.Y + y,self.texture)
