from core.world.tiles.tile import Tile

class SandTile(Tile):
    def __init__(self):
        Tile.__init__(self, 1, 0)
        self.tile_id = 1