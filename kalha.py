# kalha class


class Kalha(object):
    def __init__(self, holes, seeds):
        self.board = {0: [seeds] * holes + [0], 1: [seeds] * holes + [0]}
        self.current_player = 0
        self.is_game_over = False
        self.game_status = ["Player 1 plays next", "Player 2 plays next", "Player 1 wins", "Player 2 wins", ]
        self.holes = holes

    def status(self):
        return tuple(self.board[0]) + tuple(self.board[1])

    def play(self, hole):
        if self.is_game_over:
            if self.board[self.current_player][self.holes] == self.board[1 - self.current_player][self.holes]:
                return "Tie"
            return self.game_status[2 + self.current_player]

        if self.holes <= hole or 0 > hole:
            raise IndexError("Illegal Move. Play a Different Hole")
        if not self.board[self.current_player][hole]:
            raise ValueError("Illegal Move. Empty Hole.")
        return self.game_status[1 - self.current_player]
