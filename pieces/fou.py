from board import boardCoord, pieceBlanc, pieceNoir
from vide import vide
from boardlimit import boardlimit


def fou(boardCoord,  ligne, colonne, ligneArrive, colonneArrive, couleur):
    legalmoves = []
    if couleur == "n":
        color = pieceBlanc
    else:
        color = pieceNoir
    posfou = [ligne, colonne]
    deplacement = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
    for possibilite in deplacement:
        i = 1
        while True:
            row = posfou[0] + i * possibilite[0]
            column = posfou[0] + i * possibilite[1]
            if vide(boardCoord, row, column) and boardlimit(row, column):
                legalmoves.append([row, column])
                i += 1
            else:
                if boardCoord[row][column] in color and boardlimit(row, column):
                    legalmoves.append([row, column])
                break
    return [ligneArrive, colonneArrive] in legalmoves
