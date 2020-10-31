from ressources.vide import vide
from ressources.board import boardCoord, pieceBlanc, pieceNoir
from ressources.boardlimit import boardlimit


def cavalier(boardCoord, ligne, colonne, ligneArrive, colonneArrive, couleur):
    legalmoves = []
    if couleur == "n":
        color = pieceBlanc
    else:
        color = pieceNoir

    poscavalier = [ligne, colonne]
    deplacement = [[2, 1], [2, -1], [-2, 1],
                   [-2, -1], [-1, -2], [1, -2], [1, 2], [-1, 2]]
    for possibilite in deplacement:
        row = poscavalier[0] + possibilite[0]
        column = poscavalier[1] + possibilite[1]
        if boardlimit(row, column) and vide(boardCoord, row, column):
            legalmoves.append([row, column])
        elif boardlimit(row, column) and boardCoord[row][column] in color:
            legalmoves.append([row, column])
    return [ligneArrive, colonneArrive] in legalmoves
