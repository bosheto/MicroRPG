import opensimplex

from core.world.tiles import *
from core.position import Position
from core.constants import CHUNK_SIZE
import numpy as np

class Chunk:

    def __init__(self, position, texture):
        
        opensimplex.random_seed()
        self.position = position
        self.w, self.h = CHUNK_SIZE, CHUNK_SIZE
        self.texture = texture
        self.chunk = []
        self.__generate_chunk()
    
    def draw(self):
        for y in range(self.h):
            for x in range(self.w):
                get_tile_from_index(self.chunk[y][x]).draw(self.position.add(Position(x, y)), self.texture)
                

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
            return get_index_from_tile(SandTile())
        elif n < 0.2:
            return get_index_from_tile(GrassTile())
        else:
            return get_index_from_tile(StoneTile())
