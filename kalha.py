# kalha class


class Kalha(object):
    def __init__(self, holes, seeds):
        self.board = {0: [seeds] * holes + [0], 1: [seeds] * holes + [0]}
        self.current = 0

    def status(self):
        return tuple(self.board[0]) + tuple(self.board[1])

