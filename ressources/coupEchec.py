from ressources.board import boardCoord
from ressources.echec import Echec, coupPossible, coordRoi

def coupEchec(ligne, colonne, ligneArrive, colonneArrive, color):

    stockPiece = fauxDeplacementEchec(ligne, colonne, ligneArrive, colonneArrive)
    if Echec(color) == False:
        fauxDeplacementEchecInverse(ligne, colonne, ligneArrive, colonneArrive, stockPiece)
        return True
    else :
        fauxDeplacementEchecInverse(ligne, colonne, ligneArrive, colonneArrive, stockPiece)
        return False


def fauxDeplacementEchec(ligne, colonne, ligneArrive, colonneArrive):

    stockPiece = boardCoord[ligneArrive][colonneArrive]
    boardCoord[ligneArrive][colonneArrive] = boardCoord[ligne][colonne]
    boardCoord[ligne][colonne] = "-"
    return(stockPiece)

def fauxDeplacementEchecInverse(ligne, colonne, ligneArrive, colonneArrive, stockPiece):

    boardCoord[ligne][colonne] = boardCoord[ligneArrive][colonneArrive]
    boardCoord[ligneArrive][colonneArrive] = stockPiece
    return 