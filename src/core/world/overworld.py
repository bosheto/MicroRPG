import opensimplex
from core.world.chunk import Chunk
from core.position import Position
from core.constants import *

class World:

    def __init__(self, seed, player_position, texture):
        self.seed = seed
        #opensimplex.seed(seed)
        self.chunks = []
        self.player_pos = player_position
        self.texture = texture
        self.initialize_world()


    def initialize_world(self):
        spawn_chunk_pos = self.player_pos.subtract(Position(CHUNK_SIZE / 2 , CHUNK_SIZE / 2))
        self.chunks.append(Chunk(spawn_chunk_pos, self.texture))
        for pos in self.__get_surrounding_positions(spawn_chunk_pos):
            self.chunks.append(Chunk(pos, self.texture))

    def draw(self):
        for chunk in self.chunks:
            chunk.draw()

    def __get_surrounding_positions(self, position):
        return [
            position.add(Position(-CHUNK_SIZE, -CHUNK_SIZE)),
            position.add(Position(-CHUNK_SIZE, 0)),
            position.add(Position(-CHUNK_SIZE, CHUNK_SIZE)),
            position.add(Position(0, CHUNK_SIZE)),
            position.add(Position(CHUNK_SIZE, CHUNK_SIZE)),
            position.add(Position(CHUNK_SIZE, 0)),
            position.add(Position(CHUNK_SIZE, -CHUNK_SIZE)),
            position.add(Position(0, -CHUNK_SIZE)),
        ]