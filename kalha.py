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

    def done(self):
        return self.is_game_over

    def score(self):
        return (self.board[0][self.holes], self.board[1][self.holes])

    def validate_hole(self, hole):
        if self.holes <= hole or 0 > hole:
            raise IndexError("Illegal Move. Play a Different Hole")
        if not self.board[self.current_player][hole]:
            raise ValueError("Illegal Move. Empty Hole.")

    def victory_state(self):
        if self.board[self.current_player][self.holes] == self.board[1 - self.current_player][self.holes]:
            return "Tie"
        return self.game_status[2 + self.current_player]

    def play(self, hole):
        if self.done():
            return self.victory_state()

        self.validate_hole(hole)

        for x in range(hole, hole + self.board[self.current_player][hole]):
            self.board[self.current_player][x+1] += 1
        self.board[self.current_player][hole] = 0

        self.current_player = 1 - self.current_player
        return self.game_status[self.current_player]
