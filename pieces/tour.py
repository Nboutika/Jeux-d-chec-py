from board import boardCoord, pieceBlanc, pieceNoir
from vide import vide
from boardlimit import boardlimit


def tour(boardCoord, ligne, colonne, ligneArrive, colonneArrive, couleur):
    legalmoves = []
    if couleur == "n":
        color = pieceBlanc
    else:
        color = pieceNoir
    postour = [ligne, colonne]
    deplacement = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for possibilite in deplacement:
        i = 1
        while True:
            row = postour[0] + i * possibilite[0]
            column = postour[1] + i * possibilite[1]
            if boardlimit(row, column) and vide(boardCoord, row, column):
                legalmoves.append(boardCoord[row][column])
                i += 1
            else:
                if boardlimit(row, column) and boardCoord[row][column] in color:
                    legalmoves.append(boardCoord[row][column])
                break
    return boardCoord[ligneArrive][colonneArrive] in legalmoves
