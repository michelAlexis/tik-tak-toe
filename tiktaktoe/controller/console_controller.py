from .tiktaktoe_controller import TiktaktoeController as Controller

class ConsoleController:
    def __init__(self):
        self.controller = Controller()

    def start(self):
        self.controller.add_player('player 1', 'X')
        self.controller.add_player('player 2', 'O')
        self.controller.start_new_game()
        self.print_players()
        self.print_board()
        (x, y) = self.ask_input()
        self.controller.play(x, y)
        self.print_board()


    def print_board(self):
        print(self.get_serialized_board())

    def print_players(self):
        for player in self.controller.players:
            message = f"Name: {player.name}"
            if player == self.controller.get_current_player():
                message += ' *'
            print(message)

    def get_serialized_board(self) -> str:
        res = ''

        for row in self.controller.board.get_rows():
            for x, cell in enumerate(row):
                res += str(cell)
                if x != self.controller.get_width() - 1:
                    res += '|'

            res += '\n'

        return res

    def ask_input(self):
        print(f"{self.controller.get_current_player().name}'s turn")
        x = int(input('X :'))
        y = int(input('Y :'))
        return (x, y)