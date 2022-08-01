from core.world.tiles.tile import Tile

class SandTile(Tile):
    def __init__(self, x, y, texture):
        Tile.__init__(self, x, y, 1, 0, texture)