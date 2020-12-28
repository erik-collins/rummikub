from .tile_container import TileContainer

class PickupTiles(TileContainer):
    def __init__(self, tiles):
        super().__init__(tiles)

    def describe(self):
        print(f'There are {len(self.inner_collection)} tiles remaining.')

    def pickup(self, count=1):
            return [self.pick_random() for _ in range(count)]
