from board import boardCoord, pieceBlanc, pieceNoir
from vide import vide
from boardlimit import boardlimit


def roi(boardCoord, ligne, colonne, ligneArrive, colonneArrive, couleur):
    legalmoves = []
    if couleur == "n":
        color = pieceBlanc
    else:
        color = pieceNoir
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
                    if boardCoord[row][column] in color and boardlimit(row, column):
                        legalmoves.append(boardCoord[row][column])
    return boardCoord[ligneArrive][colonneArrive] in legalmoves


print(roi(boardCoord, 0, 4, 1, 4, "n"))
