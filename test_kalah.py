import unittest
from kalha import Kalha


class KalahTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Kalha(6, 4)
        self.game_empty = Kalha(6, 0)
        self.game_small_board = Kalha(2, 6)
        self.game_moderate_board = Kalha(4, 2)

    def tearDown(self):
        pass

    def test_status(self):
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0))

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
        self.assertRaises(ValueError, self.game_empty.play, 4)

    def test_in_game_status(self):
        self.assertFalse(self.game.done())

    def test_init_score(self):
        self.assertEqual(self.game.score(), (0, 0))

    def test_simple_move(self):
        self.game.play(1)
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 4, 4, 4, 4, 4, 0))

    def test_crossing_move(self):
        self.game.play(4)
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 0, 5, 1, 5, 5, 4, 4, 4, 4, 0))

    def test_two_simple_moves(self):
        self.game.play(1)
        self.game.play(0)
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5, 4, 0))

    def test_player_two_crosses(self):
        self.game.play(1)
        self.game.play(0)
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5, 4, 0))
        self.game.play(4)
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 0, 6, 1, 1, 6, 6, 5, 5, 4, 0))
        self.game.play(4)
        self.assertEqual(self.game.status(), (5, 1, 6, 5, 0, 6, 1, 1, 6, 6, 5, 0, 5, 1))

    def test_Crossing_other_bank(self):
        self.game_small_board.play(0)
        self.assertEqual(self.game_small_board.status(), (1, 8, 1, 7, 7, 0))

    def test_bonus_move_player_one(self):
        result = self.game.play(2)
        self.assertEqual(result, "Player 1 plays next")
        self.assertEqual(self.game.status(), (4, 4, 0, 5, 5, 5, 1, 4, 4, 4, 4, 4, 4, 0))

    def test_bonus_move_player_two(self):
        result = self.game.play(1)
        self.assertEqual(result, "Player 2 plays next")
        result = self.game.play(2)
        self.assertEqual(result, "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 4, 0, 5, 5, 5, 1,))

    def test_Crossing_other_bank_v2(self):
        result = self.game.play(3)
        self.assertEqual(result, "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 4, 4, 0, 5, 5, 1, 5, 4, 4, 4, 4, 4, 0,))
        result = self.game.play(3)
        self.assertEqual(result, "Player 1 plays next")
        self.assertEqual(self.game.status(), (5, 4, 4, 0, 5, 5, 1, 5, 4, 4, 0, 5, 5, 1,))

    def test_Crossing_other_bank_bonus_move_v3(self):
        result = self.game.play(3)
        self.assertEqual(result, "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 4, 4, 0, 5, 5, 1, 5, 4, 4, 4, 4, 4, 0,))
        result = self.game.play(2)
        self.assertEqual(result, "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 4, 4, 0, 5, 5, 1, 5, 4, 0, 5, 5, 5, 1,))

    def test_capture_player_one(self):
        result = self.game.play(5)
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 4, 0, 1, 5, 5, 5, 4, 4, 4, 0))
        result = self.game.play(3)
        self.assertEqual(self.game.status(), (5, 4, 4, 4, 4, 0, 1, 5, 5, 5, 0, 5, 5, 1))
        result = self.game.play(1)
        self.assertEqual(self.game.status(), (5, 0, 5, 5, 5, 0, 7, 0, 5, 5, 0, 5, 5, 1))

    def test_capture_player_two(self):
        result = self.game_moderate_board.play(0)
        self.assertEqual(self.game_moderate_board.status(), (0, 3, 3, 2, 0, 2, 2, 2, 2, 0))
        result = self.game_moderate_board.play(2)
        self.assertEqual(self.game_moderate_board.status(), (0, 3, 3, 2, 0, 2, 2, 0, 3, 1))
        result = self.game_moderate_board.play(0)
        self.assertEqual(self.game_moderate_board.status(), (0, 0, 3, 2, 0, 0, 3, 0, 3, 5))

    def test_non_capture(self):
        self.game.play(5)
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 4, 0, 1, 5, 5, 5, 4, 4, 4, 0))
        result = self.game.play(0)
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 4, 0, 1, 0, 6, 6, 5, 5, 5, 0))
        self.assertEqual(result, "Player 1 plays next")
        self.game.play(1)
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 1, 1, 0, 6, 6, 5, 5, 5, 0))

    def test_end_game_player_1_win(self):
        self.game_moderate_board.set_board([1, 0, 5, 1, 0, 0, 0, 1])
        self.game_moderate_board.set_banks([10, 0])
        self.game_moderate_board.play(0)
        self.game_moderate_board.play(3)
        self.assertEqual(self.game_moderate_board.status(), (0, 0, 0, 0, 17, 0, 0, 0, 0, 1))
        self.assertEqual(self.game_moderate_board.score(), (17, 1))
        self.assertTrue(self.game_moderate_board.done())

    # def test_end_game_player_1_win(self):
    #     self.game_moderate_board.play(2)
    #     self.assertEqual(self.game_moderate_board.status(), (2, 2, 0, 3, 1, 2, 2, 2, 2, 0))
    #     self.game_moderate_board.play(0)
    #     self.assertEqual(self.game_moderate_board.status(), (0, 3, 0, 3, 4, 2, 0, 2, 2, 0))
    #     self.game_moderate_board.play(0)
    #     self.assertEqual(self.game_moderate_board.status(), (0, 3, 0, 3, 4, 0, 1, 3, 2, 0))
    #     self.game_moderate_board.play(1)
    #     self.assertEqual(self.game_moderate_board.status(), (0, 0, 1, 4, 5, 0, 1, 3, 2, 0))
    #     self.game_moderate_board.play(2)
    #     self.assertEqual(self.game_moderate_board.status(), (0, 0, 0, 5, 5, 0, 1, 3, 2, 0))
    #     self.game_moderate_board.play(1)
    #     self.assertEqual(self.game_moderate_board.status(), (0, 0, 0, 5, 5, 0, 0, 4, 2, 0))
    #     self.game_moderate_board.play(3)
    #     print(self.game_moderate_board.status())
    #     self.assertEqual(self.game_moderate_board.status(), (0, 0, 0, 0, 6, 1, 1, 5, 3, 0))
    #     self.game_moderate_board.play(0)
    #     self.assertEqual(self.game_moderate_board.status(), (0, 0, 0, 0, 16, 0, 0, 0, 0, 0))
    #     self.assertEqual(self.game_moderate_board.score(), (16, 0))
    #     self.assertTrue(self.game_moderate_board.done())
    #     self.assertEqual(self.game_moderate_board.victory_state(), "Player 1 wins")

    def test_end_game_player_2_win(self):
        self.game_moderate_board.set_board([1, 0, 5, 1, 0, 0, 0, 1])
        self.game_moderate_board.set_banks([0, 10])
        self.game_moderate_board.play(0)
        self.game_moderate_board.play(3)
        self.assertEqual(self.game_moderate_board.score(), (7, 11))
        self.assertTrue(self.game_moderate_board.done())
        self.assertEqual(self.game_moderate_board.victory_state(), "Player 2 wins")

    def test_bunos_then_end_game(self):
        self.game_moderate_board.set_board([0, 0, 0, 1, 0, 0, 0, 0])
        self.game_moderate_board.set_banks([0, 0])
        self.game_moderate_board.play(3)
        self.assertEqual(self.game_moderate_board.score(), (1, 0))
        self.assertTrue(self.game_moderate_board.done())
        self.assertEqual(self.game_moderate_board.victory_state(), "Player 1 wins")

    def test_end_game_tie(self):
        self.game.set_board([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        self.game.set_banks([0, 0])
        self.game.play(1)
        self.game.play(5)
        self.assertEqual(self.game.score(), (1, 1))
        self.assertTrue(self.game.done())
        self.assertEqual(self.game.victory_state(), "Tie")

    def test_repr(self):
        assert repr(Kalha(6, 4)) == "Kalah(4, 6, status=(4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0), player=0)"

    def test_str(self):
        print(str(Kalha(6, 4)))
        assert str(Kalha(6, 4)) == '╭──╮╭──╮╭──╮╭──╮╭──╮╭──╮╭──╮╭──╮\n│  ││04││04││04││04││04││04││00│\n│  │╰──╯╰──╯╰──╯╰──╯╰──╯╰──╯│  │\n│  │╭──╮╭──╮╭──╮╭──╮╭──╮╭──╮│  │\n│00││04││04││04││04││04││04││  │\n╰──╯╰──╯╰──╯╰──╯╰──╯╰──╯╰──╯╰──╯'

        if __name__ == '__main__':
            unittest.main()
