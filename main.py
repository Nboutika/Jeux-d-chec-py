from ressources.engine import Jeux
from ressources.board import affichageBoard, resetBoard

"""
----------------------------------------------------------------
Lancement du programme depuis ici 
----------------------------------------------------------------
"""

if __name__ == '__main__':
    affichageBoard()
    Jeux()

    lancer = input(
        "Veuillez saisir 'y' pour lancer le jeu tout autre caractère pour fermer le jeu : ").upper()

    while lancer == "Y":
        resetBoard()
        affichageBoard()
        Jeux()
        lancer = input(
            "Veuillez saisir 'y' pour lancer le jeu tout autre caractère pour fermer le jeu : ")

    print("Merci d'avoir joué")

"""
----------------------------------------------------------------
Ici la boucle while permet de rejouer une partie tant que le joueur rentre y ou Y 
Et le jeu se déroule dans la fonction Jeux()
----------------------------------------------------------------
"""