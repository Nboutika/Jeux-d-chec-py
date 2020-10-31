from pieces.vide import vide
from ressources.board import boardCoord, pieceBlanc, pieceNoir
from pieces.boardlimit import boardlimit


def pion(boardCoord, ligne, colonne, ligneArrive, colonneArrive, couleur):
    legalmoves = []
    pospion = [ligne, colonne]
    if couleur == "n":
        color = pieceBlanc
        deplacement = [[1, -1], [1, 1]]
        if pospion[0] == 1:
            i = 1
            while True:
                row = pospion[0] + i
                column = pospion[1]
                if boardlimit(row, column) and vide(boardCoord, row, column):
                    legalmoves.append([row, column])
                    i += 1
                else:
                    break
            for possibilite in deplacement:
                rowDestroy = pospion[0] + possibilite[0]
                columnDestroy = pospion[1] + possibilite[1]
                if boardlimit(rowDestroy, columnDestroy) and boardCoord[rowDestroy][columnDestroy] in color:
                    legalmoves.append([rowDestroy, columnDestroy])
        else:
            row = pospion[0] + 1
            column = pospion[1]
            if boardlimit(row, column) and vide(boardCoord, row, column):
                legalmoves.append([row, column])
            for possibilite in deplacement:
                rowDestroy = pospion[0] + possibilite[0]
                columnDestroy = pospion[1] + possibilite[1]
                if boardlimit(rowDestroy, columnDestroy) and boardCoord[rowDestroy][columnDestroy] in color:
                    legalmoves.append([rowDestroy, columnDestroy])
    else:
        color = pieceNoir
        deplacement = [[-1, -1], [-1, 1]]
        if pospion[0] == 6:
            i = -1
            while True:
                row = pospion[0] + i
                column = pospion[1]
                if boardlimit(row, column) and vide(boardCoord, row, column):
                    legalmoves.append([row, column])
                    i += 1
                else:
                    break
            for possibilite in deplacement:
                rowDestroy = pospion[0] + possibilite[0]
                columnDestroy = pospion[1] + possibilite[1]
                if boardlimit(rowDestroy, columnDestroy) and boardCoord[rowDestroy][columnDestroy] in color:
                    legalmoves.append([rowDestroy, columnDestroy])
        else:
            row = pospion[0] - 1
            column = pospion[1]
            if boardlimit(row, column) and vide(boardCoord, row, column):
                legalmoves.append([row, column])
            for possibilite in deplacement:
                rowDestroy = pospion[0] + possibilite[0]
                columnDestroy = pospion[1] + possibilite[1]
                if boardlimit(rowDestroy, columnDestroy) and boardCoord[rowDestroy][columnDestroy] in color:
                    legalmoves.append([rowDestroy, columnDestroy])
    return [ligneArrive, colonneArrive] in legalmoves
