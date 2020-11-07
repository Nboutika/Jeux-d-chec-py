from ressources.vide import vide
from ressources.board import boardCoord, pieceBlanc, pieceNoir
from ressources.boardlimit import boardlimit


def roi(boardCoord, ligne, colonne, couleur):
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
        if boardlimit(row, column) and vide(boardCoord, row, column):
            legalmoves.append([row, column])
        elif boardlimit(row, column) and boardCoord[row][column] in color:
            legalmoves.append([row, column])
    return legalmoves