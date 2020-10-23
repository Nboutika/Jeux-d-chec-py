from board import *
from pieces import *
from engine import *

"""
Lancement du programme depuis ici 
"""

for l in range(8):  # Affichage du tableau initial de boardCoord
    L = l+1
    print(L, " ", end="")
    for c in range(8):
        print(boardCoord[l][c], " ", end="")
    print("")

print("   1  2  3  4  5  6  7  8")

# Attendre que entrée soit appuyez pour lancer le programme
lancer = input("Veuillez appuyez sur entrée pour commencer")
Jeux()

# Appel a la fonction jeux
