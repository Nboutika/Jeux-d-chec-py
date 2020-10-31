from ressources.board import affichageBoard
from ressources.engine import Jeux

"""
----------------------------------------------------------------
Lancement du programme depuis ici 
----------------------------------------------------------------
"""

if __name__ == '__main__':
    affichageBoard()

    lancer = input("Veuillez appuyez sur entrée pour commencer")
    Jeux()
