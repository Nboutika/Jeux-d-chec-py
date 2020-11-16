from ressources.board import boardCoord
from ressources.echec import Echec, toutCoupsPossibles, coordRoi

"""
Cette fonction permet de tester si le coup proposé met en echec le roi en utilisant les deux autres fonctions du fichier 
Particularité pour le roque qui est un coup spécial 
On fait le deplacement on appel la fonction Echec on remet les pièces a leur position originale et on renvoie true ou false 
"""

def coupEchec(ligne, colonne, ligneArrive, colonneArrive, color):
    if (boardCoord[ligneArrive][colonneArrive] == "♜" and boardCoord[ligne][colonne] == "♚") or (boardCoord[ligneArrive][colonneArrive] == "♖" and boardCoord[ligne][colonne] == "♔"):
        return True
    else:
        stockPiece = fauxDeplacementEchec(
            ligne, colonne, ligneArrive, colonneArrive)
        if Echec(color) == False:
            fauxDeplacementEchecInverse(
                ligne, colonne, ligneArrive, colonneArrive, stockPiece)
            return True
        else:
            fauxDeplacementEchecInverse(
                ligne, colonne, ligneArrive, colonneArrive, stockPiece)
            return False



def fauxDeplacementEchec(ligne, colonne, ligneArrive, colonneArrive): 
    #Cette fonction fait un déplacement mais stock la position "mangée" dans et la renvoie 
    #Elle fonctionne de pair avec fauxDeplacementEchecInverse
    stockPiece = boardCoord[ligneArrive][colonneArrive]
    boardCoord[ligneArrive][colonneArrive] = boardCoord[ligne][colonne]
    boardCoord[ligne][colonne] = "-"
    return(stockPiece)


def fauxDeplacementEchecInverse(ligne, colonne, ligneArrive, colonneArrive, stockPiece):
    #Cette fonction fais le déplacement inverse et ce sert de la pièce stocker pour remettre le tableau a son état original
    #Elle fonctionne de pair avec fauxDeplacementEchec
    boardCoord[ligne][colonne] = boardCoord[ligneArrive][colonneArrive]
    boardCoord[ligneArrive][colonneArrive] = stockPiece
    return
