import unittest
from kalha import Kalha


class KalahTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Kalha(6, 4)
        self.gameempty = Kalha(6, 0)
        self.gamesmalboard = Kalha(2, 6)

    def tearDown(self):
        pass

    def test_status(self):
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 4, 4, 100, 4, 4, 4, 4, 4, 4, 100))

    def test_minus_hole(self):
        self.assertRaises(IndexError, self.game.play, (-2))

    def test_bank_fail(self):
        self.assertRaises(IndexError, self.game.play, 6)

    def test_large_hole(self):
        self.assertRaises(IndexError, self.game.play, 8)

    def test_player_1(self):
        self.assertEqual(self.game.play(1), "Player 2 plays next")

    def test_player_2(self):
        self.game.play(1)
        self.assertEqual(self.game.play(1), "Player 1 plays next")

    def test_empty_hole(self):
        self.assertRaises(ValueError, self.gameempty.play, 4)

    def test_in_game_status(self):
        self.assertFalse(self.game.done())

    def test_init_score(self):
        self.assertEqual(self.game.score(), (0, 0))

    def test_simple_move(self):
        self.game.play(1)
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 100, 4, 4, 4, 4, 4, 4, 100))

    def test_crossing_move(self):
        self.game.play(4)
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 0, 5, 101, 5, 5, 4, 4, 4, 4, 100))

    def test_two_simple_moves(self):
        self.game.play(1)
        self.game.play(0)
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 100, 0, 5, 5, 5, 5, 4, 100))

    def test_player_two_crosses(self):
        self.game.play(1)
        self.game.play(0)
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 100, 0, 5, 5, 5, 5, 4, 100))
        self.game.play(4)
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 0, 6, 101, 1, 6, 6, 5, 5, 4, 100))
        self.game.play(4)
        self.assertEqual(self.game.status(), (5, 1, 6, 5, 0, 6, 101, 1, 6, 6, 5, 0, 5, 101))

    def test_Crossing_other_bank(self):
        self.gamesmalboard.play(0)
        self.assertEqual(self.gamesmalboard.status(), (1, 8, 101, 7, 7, 100))

    def test_bonus_move_player_one(self):
        result = self.game.play(2)
        self.assertEqual(result,"Player 1 plays next")
        self.assertEqual(self.game.status(), (4, 4, 0, 5, 5, 5, 101, 4, 4, 4, 4, 4, 4, 100))


if __name__ == '__main__':
    unittest.main()
