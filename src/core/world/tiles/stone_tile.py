from core.world.tiles.tile import Tile

class StoneTile(Tile):
    
    def __init__(self):
        Tile.__init__(self, 3, 0)
        self.tile_id = 2