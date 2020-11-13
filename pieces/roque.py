from ressources.vide import vide
from ressources.boardlimit import boardlimit
from ressources.board import boardCoord, pieceBlanc, pieceNoir
from ressources.echec import Echec, toutCoupsPossibles

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
                legalmoves.append([row, column])
                i += 1
            else:
                if boardlimit(row, column) and (boardCoord[row][column] == color) :
                    legalmoves.append([row, column])
                break
    return [ligneArrive, colonneArrive] in legalmoves