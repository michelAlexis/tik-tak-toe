from .player import Player
from .cell import Cell

class Board:
    def __init__(self, width: int = 3, height: int = 3):
        self.width = width
        self.height = height
        self._init_cells()

    def __str__(self) -> str:
        return str(self.array)

    def _init_cells(self):
        self.array = []
        for _ in range(self.width * self.height):
            self.array.append(Cell())


    def get_rows(self):
        for y in range(self.height):
            yield self.row(y)

    def row(self, index: int):
        res = []
        for x in range(self.width):
            res.append(self.get(x, index))
        return res

    def get(self, x: int, y: int) -> Cell:
        return self.array[y * self.width + x]

    def assign(self, x: int, y: int, player: Player):
        cell = self.get(x,y)
        cell.assign(player)