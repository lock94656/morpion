from Jeu_TicTacToe_Console import *
import unittest
from unittest.mock import patch

class TestFonctions(unittest.TestCase):
	"""Teste les fonctions du TicTacToe avec differentes valeurs"""
		
	def test_is_in(self):
		"""Teste la fonction is_in avec differentes valeurs"""
		print("--------------------------------")
		print("test_is_in est en cours...")
		
		#test avec valeur d'entrée correcte
		self.assertEqual(is_in( -1, [0, 1, -1, 0, 0, 1, 1, 1, 1]), True)
		self.assertEqual(is_in( -1, [5, 2, -1]), True)
		
		#test avec valeur d'entrée erronée
		self.assertEqual(is_in( -1, [[5, 2, 1], [10, 25, 4], [1, 3, 1]]), False)

		print("=================================\n")

	@patch('Jeu_TicTacToe_Console.input')
	def test_saisir_coordonnees(self, mock_input):
		"""Teste la fonction saisir_coordonnees avec differentes valeurs"""
		
		print("--------------------------------")
		print("test_saisir_coordonnees est en cours...")
		
		mock_input.side_effect = ['1', '2'] #simule 2 inputs : 1 puis 2
		status, L, C = saisir_coordonnees([0, 1, -1, 0, 0, 1, 1, 1, 1], '1')
		self.assertEqual(int(status), 1)
		self.assertEqual(L, 1)
		self.assertEqual(C, 2)
		
		mock_input.side_effect = ['Q', '2'] #simule 2 inputs : Q puis 2
		status, L, C = saisir_coordonnees([0, 1, -1, 0, 0, 1, 1, 1, 1], '1')
		self.assertEqual(status, -3)
		self.assertEqual(L, -1)
		self.assertEqual(C, -1)
		
		mock_input.side_effect = ['2', '2'] #simule 2 inputs : 2 puis 2
		status, L, C = saisir_coordonnees([0, 1, -1, 0, 0, 1, 1, 1, 1], 'z')
		self.assertEqual(status, -2)
		self.assertEqual(L, -1)
		self.assertEqual(C, -1)
		
		print("=================================\n")
		
	#def test_mettre_a_jour_grille_et_sommes(self):
		

	def test_controler_etat_du_jeu(self):
		"""Teste la fonction controler_etat_du_jeu avec differentes valeurs"""
		print("--------------------------------")
		print("test_controler_etat_du_jeu est en cours...")
		
		self.assertEqual(controler_etat_du_jeu( 1, [0,1,2,-1,1,1,0,1],2), 10)
		
		print("=================================\n")
	# a completer
	
	def test_afficher_message_de_fin(self):
		"""Teste la fonction afficher_message_de_fin avec differentes valeurs"""
		print("--------------------------------")
		print("test_afficher_message_de_fin est en cours...")
		
		#test avec valeur d'entrée correcte
		self.assertEqual(afficher_message_de_fin(0), True)
		self.assertEqual(afficher_message_de_fin(-1), True)
		self.assertEqual(afficher_message_de_fin(-2), True)
		self.assertEqual(afficher_message_de_fin(-3), True)
		
		#test avec valeur d'entrée erronée
		self.assertEqual(afficher_message_de_fin(10), False)
		self.assertEqual(afficher_message_de_fin(1), False)
		self.assertEqual(afficher_message_de_fin(2), False)
		self.assertEqual(afficher_message_de_fin(3), False)

		print("=================================\n")


if __name__ == '__main__':
	unittest.main()