from random import randint

from tiktaktoe.models.board import Board
from tiktaktoe.models.player import Player

class TiktaktoeController:
    def __init__(self):
        self.board = Board()
        self.players = []
        self.current_player = None

    def start_new_game(self):
        if not self.players:
            raise Exception('No player to play')
        self.board = Board()
        self._assign_random_player()

    def _assign_random_player(self):
        i = randint(0, len(self.players)-1)
        self.current_player = self.players[i]

    def get_width(self) -> int:
        return self.board.width

    def get_height(self) -> int:
        return self.board.height

    def add_player(self, name: str, symbol: str):
        p = Player(name, symbol)
        self.players.append(p)

    def play(self, x: int, y: int):
        self.board.assign(x, y, self.current_player)
