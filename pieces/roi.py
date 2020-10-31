from board import boardCoord, pieceBlanc, pieceNoir
from vide import vide
from boardlimit import boardlimit


def roi(boardCoord, ligne, colonne, ligneArrive, colonneArrive, couleur):
    legalmoves = []
    if couleur == "n":
        color = pieceBlanc
    else:
        color = pieceNoir

    posroi = [ligne, colonne]

    deplacement = [[1, 1], [1, -1],
                   [0, 1], [0, -1], [1, 0], [-1, 0], [-1, 1], [-1, -1]]
    for possibilite in deplacement:
        row = posroi[0] + possibilite[0]
        column = posroi[1] + possibilite[1]
        if vide(boardCoord, row, column) and boardlimit(row, column):
            legalmoves.append(boardCoord[row][column])
        elif boardCoord[row][column] in color and boardlimit(row, column):
            legalmoves.append(boardCoord[row][column])
    return boardCoord[ligneArrive][colonneArrive] in legalmoves
