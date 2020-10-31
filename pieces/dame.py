from pieces.vide import vide
from ressources.board import boardCoord, pieceBlanc, pieceNoir
from pieces.boardlimit import boardlimit


def dame(boardCoord,  ligne, colonne, ligneArrive, colonneArrive, couleur):
    legalmoves = []
    if couleur == "n":
        color = pieceBlanc
    else:
        color = pieceNoir
    postour = [ligne, colonne]
    deplacement = [[1, 0], [0, 1], [-1, 0],
                   [0, -1], [1, 1], [1, -1], [-1, -1], [-1, 1]]
    for possibilite in deplacement:
        i = 1
        while True:
            row = postour[0] + i * possibilite[0]
            column = postour[1] + i * possibilite[1]
            if boardlimit(row, column) and vide(boardCoord, row, column):
                legalmoves.append([row, column])
                i += 1
            else:
                if boardlimit(row, column) and boardCoord[row][column] in color:
                    legalmoves.append([row, column])
                break
    return [ligneArrive, colonneArrive] in legalmoves
