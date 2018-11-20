import unittest
from kalha import Kalha


class KalahTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Kalha(6, 4)
        self.gameempty = Kalha(6, 0)
        self.gamesmalboard = Kalha(2, 6)
        self.gamemoderateboard = Kalha(4, 2)

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
        self.assertEqual(result, "Player 1 plays next")
        self.assertEqual(self.game.status(), (4, 4, 0, 5, 5, 5, 101, 4, 4, 4, 4, 4, 4, 100))

    def test_bonus_move_player_two(self):
        result = self.game.play(1)
        self.assertEqual(result, "Player 2 plays next")
        result = self.game.play(2)
        self.assertEqual(result, "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 100, 4, 4, 0, 5, 5, 5, 101,))

    def test_Crossing_other_bank_v2(self):
        result = self.game.play(3)
        self.assertEqual(result, "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 4, 4, 0, 5, 5, 101, 5, 4, 4, 4, 4, 4, 100,))
        result = self.game.play(3)
        self.assertEqual(result, "Player 1 plays next")
        self.assertEqual(self.game.status(), (5, 4, 4, 0, 5, 5, 101, 5, 4, 4, 0, 5, 5, 101,))

    def test_Crossing_other_bank_bonus_move_v3(self):
        result = self.game.play(3)
        self.assertEqual(result, "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 4, 4, 0, 5, 5, 101, 5, 4, 4, 4, 4, 4, 100,))
        result = self.game.play(2)
        self.assertEqual(result, "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 4, 4, 0, 5, 5, 101, 5, 4, 0, 5, 5, 5, 101,))

    def test_capture_player_one(self):
        result = self.game.play(5)
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 4, 0, 101, 5, 5, 5, 4, 4, 4, 100))
        result = self.game.play(3)
        self.assertEqual(self.game.status(), (5, 4, 4, 4, 4, 0, 101, 5, 5, 5, 0, 5, 5, 101))
        result = self.game.play(1)
        self.assertEqual(self.game.status(), (5, 0, 5, 5, 5, 0, 107, 0, 5, 5, 0, 5, 5, 101))

    def test_capture_player_two(self):
        result = self.gamemoderateboard.play(0)
        self.assertEqual(self.gamemoderateboard.status(), (0, 3, 3, 2, 100, 2, 2, 2, 2, 100))
        result = self.gamemoderateboard.play(2)
        self.assertEqual(self.gamemoderateboard.status(), (0, 3, 3, 2, 100, 2, 2, 0, 3, 101))
        result = self.gamemoderateboard.play(0)
        self.assertEqual(self.gamemoderateboard.status(), (0, 0, 3, 2, 100, 0, 3, 0, 3, 105))

    def test_non_capture(self):
        self.game.play(5)
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 4, 0, 101, 5, 5, 5, 4, 4, 4, 100))
        result = self.game.play(0)
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 4, 0, 101, 0, 6, 6, 5, 5, 5, 100))
        self.assertEqual(result, "Player 1 plays next")
        self.game.play(1)
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 1, 101, 0, 6, 6, 5, 5, 5, 100))

    def test_end_game_player_1_win(self):
        self.gamemoderateboard.play(2)
        self.assertEqual(self.gamemoderateboard.status(), (2, 2, 0, 3, 101, 2, 2, 2, 2, 100))
        self.gamemoderateboard.play(0)
        self.assertEqual(self.gamemoderateboard.status(), (0, 3, 0, 3, 104, 2, 0, 2, 2, 100))
        self.gamemoderateboard.play(0)
        self.assertEqual(self.gamemoderateboard.status(), (0, 3, 0, 3, 104, 0, 1, 3, 2, 100))
        self.gamemoderateboard.play(1)
        self.assertEqual(self.gamemoderateboard.status(), (0, 0, 1, 4, 105, 0, 1, 3, 2, 100))
        self.gamemoderateboard.play(2)
        self.assertEqual(self.gamemoderateboard.status(), (0, 0, 0, 5, 105, 0, 1, 3, 2, 100))
        self.gamemoderateboard.play(1)
        self.assertEqual(self.gamemoderateboard.status(), (0, 0, 0, 5, 105, 0, 0, 4, 2, 100))
        self.gamemoderateboard.play(3)
        print(self.gamemoderateboard.status())
        self.assertEqual(self.gamemoderateboard.status(), (0, 0, 0, 0, 106, 1, 1, 5, 3, 100))
        self.gamemoderateboard.play(0)
        self.assertEqual(self.gamemoderateboard.status(), (0, 0, 0, 0, 116, 0, 0, 0, 0, 100))
        self.assertEqual(self.gamemoderateboard.score(), (16, 0))
        self.assertTrue(self.gamemoderateboard.done())

    def test_end_game_player_1_win(self):
        self.gamemoderateboard.play(2)
        self.assertEqual(self.gamemoderateboard.status(), (2, 2, 0, 3, 101, 2, 2, 2, 2, 100))
        self.gamemoderateboard.play(0)
        self.assertEqual(self.gamemoderateboard.status(), (0, 3, 0, 3, 104, 2, 0, 2, 2, 100))
        self.gamemoderateboard.play(0)
        self.assertEqual(self.gamemoderateboard.status(), (0, 3, 0, 3, 104, 0, 1, 3, 2, 100))
        self.gamemoderateboard.play(1)
        self.assertEqual(self.gamemoderateboard.status(), (0, 0, 1, 4, 105, 0, 1, 3, 2, 100))
        self.gamemoderateboard.play(2)
        self.assertEqual(self.gamemoderateboard.status(), (0, 0, 0, 5, 105, 0, 1, 3, 2, 100))
        self.gamemoderateboard.play(1)
        self.assertEqual(self.gamemoderateboard.status(), (0, 0, 0, 5, 105, 0, 0, 4, 2, 100))
        self.gamemoderateboard.play(3)
        print(self.gamemoderateboard.status())
        self.assertEqual(self.gamemoderateboard.status(), (0, 0, 0, 0, 106, 1, 1, 5, 3, 100))
        self.gamemoderateboard.play(0)
        self.assertEqual(self.gamemoderateboard.status(), (0, 0, 0, 0, 116, 0, 0, 0, 0, 100))
        self.assertEqual(self.gamemoderateboard.score(), (16, 0))
        self.assertTrue(self.gamemoderateboard.done())
        self.assertEqual(self.gamemoderateboard.victory_state(),"Player 1 wins")

    def test_end_game_player_2_win(self):
        self.gamemoderateboard.set_board([1,0,5,1,0,0,0,1])
        self.gamemoderateboard.set_banks([0,10])
        self.gamemoderateboard.play(0)
        self.gamemoderateboard.play(3)
        self.assertEqual(self.gamemoderateboard.score(), (0, 18))
        self.assertTrue(self.gamemoderateboard.done())
        self.assertEqual(self.gamemoderateboard.victory_state(), "Player 2 wins")

    def test_end_game_tie(self):
        self.gamemoderateboard.set_board([0,0,0,1,0,0,0,0])
        self.gamemoderateboard.set_banks([0,1])
        self.gamemoderateboard.play(3)
        self.assertEqual(self.gamemoderateboard.score(), (1, 1))
        self.assertTrue(self.gamemoderateboard.done())
        self.assertEqual(self.gamemoderateboard.victory_state(), "Tie")


if __name__ == '__main__':
    unittest.main()
