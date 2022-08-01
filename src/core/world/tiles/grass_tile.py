from core.world.tiles.tile import Tile

class GrassTile(Tile):
    def __init__(self, x, y, texture):
        Tile.__init__(self, x, y, 0, 0, texture)
    