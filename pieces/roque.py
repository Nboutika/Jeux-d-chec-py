from ressources.vide import vide
from ressources.boardlimit import boardlimit
from ressources.board import boardCoord, pieceBlanc, pieceNoir
from ressources.echec import Echec, toutCoupsPossibles
from ressources.echecmat import mouvementRoi
from ressources.coupEchec import fauxDeplacementEchec, fauxDeplacementEchecInverse

<<<<<<< HEAD

=======
>>>>>>> 0f8ae819259a121193218e38187ea10e58cc0fb5
def roqueRoi(boardCoord, ligne, colonne, ligneArrive, colonneArrive, couleur):

    legalmoves = []
    if couleur == "n":
        color = "♜"
    else:
        color = "♖"
    posRoi = [ligne, colonne]
    deplacement = [[0, 1], [0, -1]]
    for possibilite in deplacement:
        i = 1
        while True:
            row = posRoi[0]
            column = posRoi[1] + i * possibilite[1]
            if boardlimit(row, column) and vide(boardCoord, row, column) and not([row,column] in toutCoupsPossibles(couleur)) :
                stockPiece = fauxDeplacementEchec(ligne, colonne, row, column)
                if not(Echec(couleur)):
                    fauxDeplacementEchecInverse(ligne, colonne, row, column, stockPiece)
                    legalmoves.append([row, column])
                    i += 1
                else :
                    fauxDeplacementEchecInverse(ligne, colonne, row, column, stockPiece)
                    break
            else:
                if boardlimit(row, column) and (boardCoord[row][column] == color) :
                    legalmoves.append([row, column])
                break
    return [ligneArrive, colonneArrive] in legalmoves
