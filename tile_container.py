from random import randint

class TileContainer:
    def __init__(self, tiles):
        self.inner_collection = tiles


    def pick_random(self):
        if not self.inner_collection:
            raise Exception('No tiles remaining')

        index = randint(0, len(self.inner_collection)-1)
        return self.inner_collection.pop(index)
    
    def pick_tile(self, desired):
        for tile in self.inner_collection:
            if tile.value == desired.value and tile.color == desired.color:
                self.inner_collection.remove(tile)
                return tile

        raise Exception(f'Did not find tile in collection: {desired}')
     