from board import *
from vide import vide
from boardlimit import boardlimit


def roi(boardCoord, ligne, colonne, couleur):
    legalmoves = []
    for lignes in boardCoord:
        for colonnes in lignes:
            if boardCoord.index(lignes) == ligne and lignes.index(colonnes) == colonne:
                posroi = [ligne, colonne]

                deplacement = [[1, 1], [1, -1],
                               [0, 1], [0, -1], [1, 0], [-1, 0], [-1, 1], [-1, -1]]
                for possibilite in deplacement:
                    row = posroi[0] + possibilite[0]
                    column = posroi[1] + possibilite[1]
                    if vide(boardCoord, row, column) and boardlimit(row, column):
                        legalmoves.append(boardCoord[row][column])
                    if (not boardCoord[ligne][colonne].startswith(couleur[0])) and boardlimit(row, column):
                        legalmoves.append(boardCoord[row][column])
    return legalmoves


print(roi(boardCoord, 3, 3, "nr"))
