from tiktaktoe.models.board import Board

class TiktaktoeController:
    def __init__(self):
        self.board = Board()

    def get_serialized_board(self) -> str:
        res = ''

        for row in self.board.get_rows():
            for x, cell in enumerate(row):
                res += str(cell)
                if x != self.board.width - 1:
                    res += '|'

            res += '\n'

        return res