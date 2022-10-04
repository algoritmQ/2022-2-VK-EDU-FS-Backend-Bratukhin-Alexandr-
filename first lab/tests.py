import unittest
from tic_tac import TicTacGame

class TicTacGame_tasts(unittest.TestCase):

    def test_validate_input(self):
        self.assertEqual(TicTacGame.validate_input(self, -5, 1), False)
        self.assertEqual(TicTacGame.validate_input(self, 'wf', 1), False)
        self.assertEqual(TicTacGame.validate_input(self, 20, 1), False)

    def test_check_winner_1(self):
        self.assertEqual(TicTacGame.check_winner(self, ['X', 'X', 'X', 4, 'O', 'O', 7, 8, 9]), "X")

    def test_check_winner_2(self):
        self.assertEqual(TicTacGame.check_winner(self, [1, 2, 'O', 'X', 'X', 'X', 'O', 8, 9], ), "X")

    def test_check_winner_3(self):
        self.assertEqual(TicTacGame.check_winner(self, [1, 2, 3, 4, 'O', 'O', 'X', 'X', 'X']), "X")

    def test_check_winner_4(self):
        self.assertEqual(TicTacGame.check_winner(self, ['X', 2, 'O', 4, 'X', 'O', 7, 8, 'X']), "X")

    def test_check_winner_5(self):
        self.assertEqual(TicTacGame.check_winner(self, ['O', 'O', 'X', 4, 'X', 6, 'X', 8, 9]), "X")

    def test_check_winner_6(self):
        self.assertEqual(TicTacGame.check_winner(self, ['O', 'O', 'O', 4, 'X', 6, 7, 'X', 'X']), "O")

    def test_check_winner_7(self):
        self.assertEqual(TicTacGame.check_winner(self, ['X', 2, 'X', 'O', 'O', 'O', 'O', 8, 'X']), "O")

    def test_check_winner_8(self):
        self.assertEqual(TicTacGame.check_winner(self, ['X', 2, 'X', 4, 'X', 'O', 'O', 'O', 'O']), "O")

    def test_check_winner_9(self):
        self.assertEqual(TicTacGame.check_winner(self, ['O', 2, 'X', 4, 'O', 'X', 'X', 8, 'O']), "O")

    def test_check_winner_10(self):
        self.assertEqual(TicTacGame.check_winner(self, ['X', 'X', 'O', 'X', 'O', 6, 'O', 8, 9]), "O")

    def test_check_winner_11(self):#проверка на ничью
        self.assertEqual(TicTacGame.check_winner(self, ['O', 'X', 'X', 'X', 'X', 'O', 'O', '0', 'X']), "")
