from board import boardCoord, pieceBlanc, pieceNoir
import board as b
from tour import tour
from fou import fou
from roi import roi
from cavalier import cavalier
from dame import dame
from pion import pion
from echec import Echec, coordRoi, coupPossibles


def coupPossible(color):
    Coups = []
    if color == "b":
        for ligne in range(8):
            for colonne in range(8):
                if boardCoord[ligne][colonne] in pieceBlanc:
                    if boardCoord[ligne][colonne] == b.bp:
                        for coup in (pion(boardCoord, ligne, colonne, color)):
                            boardCoord[ligne][colonne] = "-"
                            temp = boardCoord[coup[0]][coup[1]]
                            boardCoord[coup[0]][coup[1]] = b.bp
                            if not Echec(color):
                                Coups.append(coup)
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.bp

                    elif boardCoord[ligne][colonne] == b.bt:
                        for coup in (tour(boardCoord, ligne, colonne, color)):
                            boardCoord[ligne][colonne] = "-"
                            temp = boardCoord[coup[0]][coup[1]]
                            boardCoord[coup[0]][coup[1]] = b.bt
                            if not Echec(color):
                                Coups.append(coup)
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.bt

                    elif boardCoord[ligne][colonne] == b.bf:
                        for coup in (fou(boardCoord, ligne, colonne, color)):
                            boardCoord[ligne][colonne] = "-"
                            temp = boardCoord[coup[0]][coup[1]]
                            boardCoord[coup[0]][coup[1]] = b.bf
                            if not Echec(color):
                                Coups.append(coup)
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.bf

                    elif boardCoord[ligne][colonne] == b.bc:
                        for coup in (
                                cavalier(boardCoord, ligne, colonne, color)):
                            boardCoord[ligne][colonne] = "-"
                            temp = boardCoord[coup[0]][coup[1]]
                            boardCoord[coup[0]][coup[1]] = b.bc
                            if not Echec(color):
                                Coups.append(coup)
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.bc

                    elif boardCoord[ligne][colonne] == b.bd:
                        for coup in (dame(boardCoord, ligne, colonne, color)):

                            boardCoord[ligne][colonne] = "-"
                            temp = boardCoord[coup[0]][coup[1]]
                            boardCoord[coup[0]][coup[1]] = b.bd
                            if not Echec(color):
                                Coups.append(coup)
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.bd
        return Coups

    elif color == "n":
        for ligne in range(8):
            for colonne in range(8):
                if boardCoord[ligne][colonne] in pieceNoir:
                    if boardCoord[ligne][colonne] == b.np:
                        for coup in (pion(boardCoord, ligne, colonne, color)):
                            boardCoord[ligne][colonne] = "-"
                            temp = boardCoord[coup[0]][coup[1]]
                            boardCoord[coup[0]][coup[1]] = b.np
                            if not Echec(color):
                                Coups.append(coup)
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.np
                    elif boardCoord[ligne][colonne] == b.nt:
                        for coup in (tour(boardCoord, ligne, colonne, color)):
                            boardCoord[ligne][colonne] = "-"
                            temp = boardCoord[coup[0]][coup[1]]
                            boardCoord[coup[0]][coup[1]] = b.nt
                            if not Echec(color):
                                Coups.append(coup)
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.nt
                    elif boardCoord[ligne][colonne] == b.nf:
                        for coup in (fou(boardCoord, ligne, colonne, color)):
                            boardCoord[ligne][colonne] = "-"
                            temp = boardCoord[coup[0]][coup[1]]
                            boardCoord[coup[0]][coup[1]] = b.nf
                            if not Echec(color):
                                Coups.append(coup)
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.nf
                    elif boardCoord[ligne][colonne] == b.nc:
                        for coup in (
                                cavalier(boardCoord, ligne, colonne, color)):
                            boardCoord[ligne][colonne] = "-"
                            temp = boardCoord[coup[0]][coup[1]]
                            boardCoord[coup[0]][coup[1]] = b.nc
                            if not Echec(color):
                                Coups.append(coup)
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.nc
                    elif boardCoord[ligne][colonne] == b.nd:
                        for coup in (dame(boardCoord, ligne, colonne, color)):
                            boardCoord[ligne][colonne] = "-"
                            temp = boardCoord[coup[0]][coup[1]]
                            boardCoord[coup[0]][coup[1]] = b.nd
                            if not Echec(color):
                                Coups.append(coup)
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.nd

        return Coups


def piecepath(pieceCoord, kingCoord):
    path = []
    path.append(pieceCoord)
    x = kingCoord[0] - pieceCoord[0]
    y = kingCoord[1] - pieceCoord[1]
    if x != 0:
        x1 = x // abs(x)
    else:
        x1 = x
    if y != 0:
        y1 = y // abs(y)
    else:
        y1 = y
    i = 1
    while True:
        row = pieceCoord[0] + i * x1
        column = pieceCoord[1] + i * y1
        if [row, column] == kingCoord:
            break
        else:
            path.append([row, column])
            i += 1
    return path


def mouvementRoi(color):
    Coups = []
    ligne = coordRoi(color)[0]
    colonne = coordRoi(color)[1]
    for coup in (roi(boardCoord, ligne, colonne, color)):
        boardCoord[ligne][colonne] = "-"
        temp = boardCoord[coup[0]][coup[1]]
        boardCoord[coup[0]][coup[1]] = b.nr
        if not Echec(color):
            Coups.append(coup)
        boardCoord[coup[0]][coup[1]] = temp
        boardCoord[ligne][colonne] = b.nr
    return Coups


def echecmat(color):
    bool, table = coupPossibles(color)
    a = piecepath(table, coordRoi(color))
    b = coupPossible(color)
    def any_in(a, b): return any(i in b for i in a)
    if not (any_in(a, b)):
        if mouvementRoi(color) == []:
            return True
        else:
            return False
    else:
        return False


print(echecmat("n"))
