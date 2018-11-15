import unittest
from kalha import Kalha


class KalahTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Kalha(6, 4)

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


if __name__ == '__main__':
    unittest.main()
