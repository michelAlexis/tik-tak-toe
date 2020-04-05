from random import randint

from tiktaktoe.models.board import Board
from tiktaktoe.models.player import Player
from tiktaktoe.utils.array_utils import in_bound

class TiktaktoeController:
    def __init__(self):
        self.board = Board()
        self.players = []
        self.current_player_index = -1
        self.win_length = 3

    def start_new_game(self):
        if not self.players:
            raise Exception('No player to play')
        self.board = Board()
        self._assign_random_player()

    def _assign_random_player(self):
        self.current_player_index = randint(0, len(self.players)-1)
    
    def get_current_player(self) -> Player:
        return self.players[self.current_player_index]

    def _assign_next_player(self):
        self.current_player_index += 1
        if not in_bound(self.players, self.current_player_index):
            self.current_player_index = 0
        return self.current_player_index


    def get_width(self) -> int:
        return self.board.width

    def get_height(self) -> int:
        return self.board.height

    def add_player(self, name: str, symbol: str):
        p = Player(name, symbol)
        self.players.append(p)

    def play(self, x: int, y: int):
        self.board.assign(x, y, self.get_current_player())
        self.check_win(x, y)


    def check_win(self, x: int, y: int):
        pass

