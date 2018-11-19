# kalha class


class Kalha(object):
    def __init__(self, holes, seeds):
        self.board = [seeds] * holes * 2
        self.banks = [0, 0]
        self.current_player = 0
        self.is_game_over = False
        self.game_status = ["Player 1 plays next", "Player 2 plays next", "Player 1 wins", "Player 2 wins", ]
        self.holes = holes

    def status(self):
        print(self.board)
        return tuple(
            self.board[0:self.holes] + [self.banks[0]] + self.board[self.holes:len(self.board)] + [self.banks[1]])

    def done(self):
        return self.is_game_over

    def score(self):
        # return (self.banks[0], self.banks[1])
        return tuple(self.banks)

    def validate_hole(self, hole):
        if self.holes <= hole or 0 > hole:
            raise IndexError("Illegal Move. Play a Different Hole")
        if not self.board[self.current_player * self.holes + hole]:
            raise ValueError("Illegal Move. Empty Hole.")

    def victory_state(self):
        if self.banks[0] == self.banks[1]:
            return "Tie"
        return self.game_status[2 + self.current_player]

    def play(self, hole):
        if self.done():
            return self.victory_state()

        self.validate_hole(hole)
        player_offset = self.current_player * self.holes
        # nonlocal amount
        amount = self.board[player_offset + hole]
        self.board[player_offset + hole] = 0
        # nonlocal hole_index
        hole_index = player_offset +hole + 1
        for x in range(amount):
            # print("hole index " + str(hole_index))
            if hole_index == player_offset + self.holes:
                amount -= 1
                self.banks[self.current_player] += 1
            if not amount:
                break
            self.board[hole_index] += 1
            amount -= 1
            hole_index += 1
            if hole_index == self.holes * 2:
                hole_index = 0

        self.current_player = 1 - self.current_player
        return self.game_status[self.current_player]
