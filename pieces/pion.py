from board import boardCoord, pieceBlanc, pieceNoir
from boardlimit import boardlimit
from vide import vide


def pion(boardCoord, ligne, colonne, ligneArrive, colonneArrive, couleur):
    legalmoves = []
    pospion = [ligne, colonne]
    if couleur == "n":
        color = pieceBlanc
        deplacement = [[1, -1], [1, 1]]
        if pospion[0] == 1:
            premierdeplacement = [[1], [2]]
            for possibilite in premierdeplacement:
                print(possibilite[0])
                row = pospion[0] + possibilite[0]
                column = pospion[1]
                if vide(boardCoord, row, column) and boardlimit(row, column):
                    legalmoves.append(boardCoord[row][column])
            for possibilite in deplacement:
                rowDestroy = pospion[0] + possibilite[0]
                columnDestroy = pospion[1] + possibilite[1]
                if boardCoord[rowDestroy][columnDestroy] in color and boardlimit(rowDestroy, columnDestroy):
                    legalmoves.append(boardCoord[rowDestroy][columnDestroy])
        else:
            row = pospion[0] + 1
            column = pospion[1]
            if vide(boardCoord, row, column) and boardlimit(row, column):
                legalmoves.append(boardCoord[row][column])
            for possibilite in deplacement:
                rowDestroy = pospion[0] + possibilite[0]
                columnDestroy = pospion[1] + possibilite[1]
                if boardCoord[rowDestroy][columnDestroy] in color and boardlimit(rowDestroy, columnDestroy):
                    legalmoves.append(boardCoord[rowDestroy][columnDestroy])
    else:
        color = pieceNoir
        deplacement = [[-1, -1], [-1, 1]]
        if pospion[0] == 6:
            premierdeplacement = [[-1], [-2]]
            for x in premierdeplacement:
                row = pospion[0] + x[0]
                column = pospion[1]
                if vide(boardCoord, row, column) and boardlimit(row, column):
                    legalmoves.append(boardCoord[row][column])
            for possibilite in deplacement:
                rowDestroy = pospion[0] + possibilite[0]
                columnDestroy = pospion[1] + possibilite[1]
                if boardCoord[rowDestroy][columnDestroy] in color and boardlimit(rowDestroy, columnDestroy):
                    legalmoves.append(boardCoord[rowDestroy][columnDestroy])
        else:
            row = pospion[0] - 1
            column = pospion[1]
            if vide(boardCoord, row, column) and boardlimit(row, column):
                legalmoves.append(boardCoord[row][column])
            for possibilite in deplacement:
                rowDestroy = pospion[0] + possibilite[0]
                columnDestroy = pospion[1] + possibilite[1]
                if boardCoord[rowDestroy][columnDestroy] in color and boardlimit(rowDestroy, columnDestroy):
                    legalmoves.append(boardCoord[rowDestroy][columnDestroy])
    return boardCoord[ligneArrive][colonneArrive] in legalmoves
