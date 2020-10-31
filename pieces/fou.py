from pieces.vide import vide
from ressources.board import boardCoord, pieceBlanc, pieceNoir
from pieces.boardlimit import boardlimit


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
            column = posfou[1] + i * possibilite[1]
            if boardlimit(row, column) and vide(boardCoord, row, column):
                legalmoves.append([row, column])
                i += 1
            else:
                if boardlimit(row, column) and boardCoord[row][column] in color:
                    legalmoves.append([row, column])
                break
    return [ligneArrive, colonneArrive] in legalmoves
