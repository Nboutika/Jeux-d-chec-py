from vide import vide
from board import boardCoord, pieceBlanc, pieceNoir
from boardlimit import boardlimit


def dame(boardCoord,  ligne, colonne, couleur):
    legalmoves = []
    if couleur == "n":
        color = pieceBlanc
    else:
        color = pieceNoir
    posdame = [ligne, colonne]
    deplacement = [[1, 0], [0, 1], [-1, 0],
                   [0, -1], [1, 1], [1, -1], [-1, -1], [-1, 1]]
    for possibilite in deplacement:
        i = 1
        while True:
            row = posdame[0] + i * possibilite[0]
            column = posdame[1] + i * possibilite[1]
            if boardlimit(row, column) and vide(boardCoord, row, column):
                legalmoves.append([row, column])
                i += 1
            else:
                if boardlimit(row, column) and boardCoord[row][column] in color:
                    legalmoves.append([row, column])
                break
    return legalmoves
