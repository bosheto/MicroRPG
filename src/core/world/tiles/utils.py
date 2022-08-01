from core.world.tiles import *

def get_tile_from_index(index):
    if index == 0:
        return GrassTile()
    elif index == 1:
        return SandTile()
    elif index == 2:
        return StoneTile()

def get_index_from_tile(tile):
    return tile.tile_id
