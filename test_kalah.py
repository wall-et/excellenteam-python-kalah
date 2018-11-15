import unittest
from kalha import Kalha


class KalahTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Kalha(6, 4)
        self.gameempty = Kalha(6, 0)

    def tearDown(self):
        pass

    def test_status(self):
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0))

    def test_minus_hole(self):
        self.assertRaises(IndexError, self.game.play, (-2))

    def test_large_hole(self):
        self.assertRaises(IndexError, self.game.play, 8)

    def test_player_1(self):
        self.assertEqual(self.game.play(1), "Player 2 plays next")

    def test_player_2(self):
        self.game.play(1)
        self.assertEqual(self.game.play(1), "Player 1 plays next")

    def test_empty_hole(self):
        self.assertRaises(ValueError, self.gameempty.play, 4)

if __name__ == '__main__':
    unittest.main()
