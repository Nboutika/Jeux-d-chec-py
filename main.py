from ressources.engine import Jeux
from ressources.board import affichageBoard

"""
----------------------------------------------------------------
Lancement du programme depuis ici 
----------------------------------------------------------------
"""

if __name__ == '__main__':
    affichageBoard()

    lancer = input("Veuillez appuyez sur entrée pour commencer")
    Jeux()
