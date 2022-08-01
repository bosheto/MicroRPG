from core.world.tiles.tile import Tile

class StoneTile(Tile):
    
    def __init__(self, x, y, texture):
        Tile.__init__(self, x, y, 3, 0, texture)