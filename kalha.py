# kalha class


class Kalha(object):
    def __init__(self, holes, seeds):
        self.board = [seeds] * holes * 2
        self.banks = [0, 0]
        self.current_player = 0
        self.is_game_over = False
        self.game_status = ["Player 1 plays next", "Player 2 plays next", "Player 1 wins", "Player 2 wins", ]
        self.holes = holes
        self.seeds = seeds

    def status(self):

        return tuple(
            self.board[0:self.holes] + [self.banks[0]] + self.board[self.holes:len(self.board)] + [self.banks[1]])

    def done(self):
        return self.is_game_over

    def score(self):
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

    def calculate_is_game_over(self):
        player_offset = self.current_player * self.holes
        for x in range(player_offset, player_offset + self.holes):
            if self.board[x]:
                return
        self.is_game_over = True
        player_offset = (1 - self.current_player) * self.holes
        for x in range(player_offset, player_offset + self.holes):
            self.banks[self.current_player] += self.board[x]
            self.board[x] = 0

    def play(self, hole):
        if self.done():
            return self.victory_state()

        self.validate_hole(hole)

        player_offset = self.current_player * self.holes
        seeds_count = self.board[player_offset + hole]
        self.board[player_offset + hole] = 0
        hole_index = player_offset + hole

        for x in range(seeds_count):
            hole_index += 1
            if hole_index == self.holes * 2:
                hole_index = 0
            if hole_index == (player_offset + self.holes) % (self.holes * 2) and seeds_count:
                seeds_count -= 1
                self.banks[self.current_player] += 1
            if not seeds_count:
                break
            self.board[hole_index] += 1
            seeds_count -= 1

        if self.board[hole_index] == 1 and self.board[self.holes * 2 - 1 - hole_index] != 0:
            self.board[hole_index] = 0
            self.banks[self.current_player] += 1 + self.board[self.holes * 2 - 1 - hole_index]
            # self.banks[self.current_player] += self.board[self.holes*2 - 1 - hole_index]
            self.board[self.holes * 2 - 1 - hole_index] = 0

        if hole_index != (player_offset + self.holes) % (self.holes * 2):
            self.current_player = 1 - self.current_player

        self.calculate_is_game_over()

        return self.game_status[self.current_player]

    def set_board(self, board):
        self.board = board

    def set_banks(self, banks):
        self.banks = banks

    def __repr__(self):
        print(f"Kalah({self.seeds}, {self.holes}, status={self.status()}, player={self.current_player})")
        return f"Kalah({self.seeds}, {self.holes}, status={self.status()}, player={self.current_player})"
