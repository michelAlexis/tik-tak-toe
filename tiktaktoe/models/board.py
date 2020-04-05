from .cell import Cell

class Board:
    def __init__(self, width: int = 3, height: int = 3):
        self.width = width
        self.height = height
        self.array = ([Cell()] * (width * height))

    def __str__(self) -> str:
        return str(self.array)

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