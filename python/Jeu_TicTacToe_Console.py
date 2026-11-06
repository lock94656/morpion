# coding: utf-8

#------------------------------------------------------------------------------#
# PROJET Tic-Tac-Toe
# ---------------------------------------------------------------------------- #
# Élèves :      Hugo Gibert ; Alexandre Tardy
# ---------------------------------------------------------------------------- #
# Création              :   02/11/2026      par Philippe THOMAS
#                           base de travail commune à tous les élèves
#                           - trois variables
#                             une quatrième variable est à définir
#                           - structure du programme
#                           - affichage dans la console
#                           * signature des fonctions à écrire avec une chaîne
#                             de documentation (docstring)
# ---------------------------------------------------------------------------- #
# Dernière modification :   ../../....      par ...
#------------------------------------------------------------------------------#

# ---------------------------------------------------------------------------- #
# Inventaire des variables du jeu :
# ---------------------------------------------------------------------------- #
#
#   etat   : int  :  état du jeu
#                     -1 : victoire du joueur 1 ;   1 : tour du joueur 1
#                     -2 : victoire du joueur 2 ;   2 : tour du joueur 2
#                     -3 : abandon              ;   0 : égalité
#
#   tour   : int  :  numéro du tour de jeu (au plus 9)
#
#   grille : list :  [0,0,0, 0,0,0, 0,0,0]
#                     grille[0], grille[1], grille[2] : première ligne
#                     grille[3], grille[4], grille[5] : deuxième ligne
#                     grille[6], grille[7], grille[8] : troisième ligne
#                     grille[3*(l-1) + c - 1 : case de coordonnées (l,c)
#
#   il manque une quatrième variable pour compter les points...
#
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# CONSIGNES
# ---------------------------------------------------------------------------- #
#
#   compléter les parties de code manquantes :
#
#       - les points de suspension.
#
#   tester les fonctions en les appelant dans la console.
#
# ---------------------------------------------------------------------------- #









# ---------------------------------------------------------------------------- #
# Une fonction qui teste la présence d'un élément dans une séquence
# ---------------------------------------------------------------------------- #

def is_in(element, sequence):
	"""
	Renvoie True si element est dans sequence et False sinon
	(pour remplacer l'opérateur in ; pour préparer EP en Terminale)
	"""
	for i in sequence:
		if isinstance(i, list):
			for k in i:
				if k == element:
					return True
	return False


# ---------------------------------------------------------------------------- #
# Une fonction d'affichage de la grille
# ---------------------------------------------------------------------------- #

# Les caractères ASCII étendu (8859-1) pour les bordures
#
# - Bordures simples  - - - - - - - - - - - -
# 179 180 191 192 193 194 195 196 197 217 218
#  │   ┤   ┐   └   ┴   ┬   ├   ─   ┼   ┘   ┌
# - Bordures doubles  - - - - - - - - - - - -
# 185 186 187 188 200 201 202 203 204 205 206
#  ╣   ║   ╗   ╝  ╚   ╔   ╩   ╦   ╠   ═   ╬
# - - - - - - - - - - - - - - - - - - - - - -
#
# - Dessins des bordures de la grille - - - -
#
#    ' ┌───┬───┬───┐ '
#    ' │ . │ . │ . │ '
#    ' ├───┼───┼───┤ '
#    ' │ . │ . │ . │ '
#    ' ├───┼───┼───┤ '
#    ' │ . │ . │ . │ '
#    ' └───┴───┴───┘ '
# - - - - - - - - - - - - - - - - - - - - - -

def afficher_grille(grid, marks=' XO'):
    """
    Affiche la grille grid dans la console en utilisant la chaîne marks pour
    les symboles des deux joueurs.
    Ne renvoie rien.
    """
    # Définition des bordures de la grille
    t_line = ' ┌───┬───┬───┐ '          # Bordure supérieure
    p_line = ' │ {0} │ {1} │ {2} │ '    # Ligne pour les cases des joueurs
    s_line = ' ├───┼───┼───┤ '          # Séparateur horizontal
    b_line = ' └───┴───┴───┘ '          # Bordure inférieure
    # Affichage effectif de la grille, avec les marques des joueurs
    print(t_line)
    print(p_line.format(marks[grid[0]], marks[grid[1]], marks[grid[2]]))
    print(s_line)
    print(p_line.format(marks[grid[3]], marks[grid[4]], marks[grid[5]]))
    print(s_line)
    print(p_line.format(marks[grid[6]], marks[grid[7]], marks[grid[8]]))
    print(b_line)




# ---------------------------------------------------------------------------- #
# Une fonction de saisie des coordonnées
# ---------------------------------------------------------------------------- #

def saisir_coordonnees(grid, status):
    """
    Renvoie :
        - l'état de la partie (type int), égal au numéro du joueur (valeur de
          status transmise) ou à -3 (abandon) si 'Q' ou 'q' a été saisi ;
        - les coordonnées saisies L, C d'une case valide de la grille grid.
    Les coordonnées sont entrées sont la forme L,C.
    """
    L = input("Entrez le n° de ligne : ")
    if L.lower() == "q":
        return -3
    C = input("Entrez le n° de colonne : ")
    if C.lower() == "q":
        return -3
    elif L.isdigit() and C.isdigit():
        return int(status), [int(L),int(C)]
    else:
        return 'Tu ne sais pas ecrire un nombre'



# ---------------------------------------------------------------------------- #
# Une fonction de mise à jour de la grille et des sommes associées
# ---------------------------------------------------------------------------- #

def mettre_a_jour_grille_et_sommes(grid, sums, row, col, player):
    """
    Renvoie
        - la grille grid mise à jour ;
        - les sommes associées sums associées à la grille grid mises à jour.
    """
    # Mettre à jour la case de la grille
    grid[row][col] = player

    # Maj des sommes des lignes
    for i in range(3):
        sums[i] = sum(grid[i])

    # Maj des sommes des colonnes
    for k in range(3):
        sums[3+j] = sum(grid[i][j] for i in range(3))

    # Maj Diagonale principale
    sums[6] = sum(grid[i][i] for i in range(3))

    # Maj Diagonale secondaire
    sums[7] = sum(grid[i][2-i] for i in range(3))

    return grid, sums



# ---------------------------------------------------------------------------- #
# Une fonction de contrôle de l'état de la partie (victoire, égalité, continuer)
# ---------------------------------------------------------------------------- #

def controler_etat_du_jeu(round_of_play, sums, status):
    """
    Renvoie :
        - l'état de la partie (type int), égal :
            au numéro du joueur (1 ou 2) du tour suivant ;
            à 0 si il y a égalité ;
            à -1 si la joueur 1 a gagné ;
            à -2 si le joueur 2 a gagné ;
        - le tour de jeu, mis à jour si nécessaire.
    """
    for i in range(len(sums)):
        if sums[i] == 3:
            return -1
        elif sums[i] == -3:
            return -2



















# ---------------------------------------------------------------------------- #
# Une fonction d'affichage en fin de partie (victoire, égalité, interruption)
# ---------------------------------------------------------------------------- #

def afficher_message_de_fin(status):
    """
    Affiche le message de fin de partie d'après l'état de la partie status,
    égal à :
        -3 si la partie a été interrompue par 'Q' ou 'q' ;
        -2 si le joueur 2 a gagné ;
        -1 si le joueur 1 a gagné ;
         0 si il y a égalité.
    Ne renvoie rien.
    """
    if status == -3:
        print("la partie a été interrompue")
    elif status == -2:
        print("le joueur 2 a gagné")
    elif status == -1:
        print("le joueur 1 a gagné")
    elif status == 0:
        print("il y a égalité")
    else:
        print("t'as cassé le jeu")


# -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - #
# Fonction principale de jeu                                                   #
# -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - #

def tictactoe():
    """
    """
    # Initialisations -------------------------------------------------------- #
    ...
    ...
    ...
    ...
    # Affichage de la grille
    ...
    # Boucle de jeu ---------------------------------------------------------- #
    while ...:
        # La saisie des coordonnées
        ...
        # Les actions de mises à jour et de contrôle de l'état du jeu
        if ...:
            # Mise à jour de la grille
            ...
            # Contrôle des conditions de fin de jeu
            ...
        # Affichage de la grille
        ...
    # Fin de partie ---------------------------------------------------------- #
    ...


# -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - #
# Programme principal (appel de la fonction tictactoe()                        #
# -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - #

# tictactoe()