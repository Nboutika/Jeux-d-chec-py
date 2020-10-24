from board import *
from pieces import *
from engine import *

"""
Lancement du programme depuis ici 
"""

for ligne in range(8):  # Affichage du tableau initial de boardCoord
    L = ligne+1
    print(L, " ", end="")
    for colonne in range(8):
        print(boardCoord[ligne][colonne], " ", end="")
    print("")

print("   1  2  3  4  5  6  7  8")

# Attendre que entrée soit appuyez pour lancer le programme
lancer = input("Veuillez appuyez sur entrée pour commencer")
Jeux()

# Appel a la fonction jeux
