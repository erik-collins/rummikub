
class Tile:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __str__(self):
        return f'{self.color} {self.value}'

    def __repr__(self):
        return f'Tile(value={self.value},color={self.color})'

