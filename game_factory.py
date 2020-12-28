from itertools import cycle

from .tile import Tile
from .pickup_tiles import PickupTiles


class GameFactory:
    def __init__(self, values, colors, copies, jokers):
        self.values = values
        self.colors = colors
        self.copies = copies
        self.jokers = jokers

    def get_tiles(self):
        regular_tiles = [Tile(value, color) for value in self.values for color in self.colors]
        regular_tiles = [t for _ in range(self.copies) for t in regular_tiles]
        colors = cycle(self.colors)
        joker_tiles = [Tile('J', next(colors)) for _ in range(self.jokers)]
        return PickupTiles(regular_tiles + joker_tiles)
