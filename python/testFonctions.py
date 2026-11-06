from Jeu_TicTacToe_Console import is_in
import unittest

class TestFonctions(unittest.TestCase):
	"""Teste les fonctions du TicTacToe avec differentes valeurs"""
	def test_is_in(self):
		"""Teste la fonction is_in avec differentes valeurs"""
		self.assertEqual(is_in( -1, [[0, 1, -1], [0, 0, 1], [1, 1, 1]]), True)
		self.assertEqual(is_in( -1, [[5, 2, 1], [10, 25, 4], [1, 3, 1]]), False)
		self.assertEqual(is_in( -1, [5, 2, -1]), False)


if __name__ == '__main__':
	unittest.main()