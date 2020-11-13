from board import boardCoord, pieceBlanc, pieceNoir
import board as b
from tour import tour
from fou import fou
from roi import roi
from cavalier import cavalier
from dame import dame
from pion import pion
from echec import Echec


def coupPossible(color):
    Coups = []
    if color == "b":
        for ligne in range(8):
            for colonne in range(8):
                if boardCoord[ligne][colonne] in pieceBlanc:
                    if boardCoord[ligne][colonne] == b.bp:
                        for coup in (pion(boardCoord, ligne, colonne, color)):
                            boardCoord[coup[0]][coup[1]] = b.bp
                            if Echec(color):
                                pass
                            else:
                                Coups.append(coup)
                            boardCoord[ligne][colonne] = b.bp
                    elif boardCoord[ligne][colonne] == b.bt:
                        for coup in (tour(boardCoord, ligne, colonne, color)):
                            boardCoord[coup[0]][coup[1]] = b.bt
                            if Echec(color):
                                pass
                            else:
                                Coups.append(coup)
                            boardCoord[ligne][colonne] = b.bt
                    elif boardCoord[ligne][colonne] == b.bf:
                        for coup in (fou(boardCoord, ligne, colonne, color)):
                            boardCoord[coup[0]][coup[1]] = b.bf
                            if Echec(color):
                                pass
                            else:
                                Coups.append(coup)
                            boardCoord[ligne][colonne] = b.bf
                    elif boardCoord[ligne][colonne] == b.bc:
                        for coup in (
                                cavalier(boardCoord, ligne, colonne, color)):
                            boardCoord[coup[0]][coup[1]] = b.bc
                            if Echec(color):
                                pass
                            else:
                                Coups.append(coup)
                            boardCoord[ligne][colonne] = b.bc
                    elif boardCoord[ligne][colonne] == b.bd:
                        for coup in (dame(boardCoord, ligne, colonne, color)):

                            boardCoord[coup[0]][coup[1]] = b.bd
                            if Echec(color):
                                pass
                            else:
                                Coups.append(coup)
                            boardCoord[ligne][colonne] = b.bd

                    elif boardCoord[ligne][colonne] == b.br:
                        for coup in (roi(boardCoord, ligne, colonne, color)):
                            boardCoord[coup[0]][coup[1]] = b.br
                            if Echec(color):
                                pass
                            else:
                                Coups.append(coup)
                            boardCoord[ligne][colonne] = b.br
        return Coups

    elif color == "n":
        for ligne in range(8):
            for colonne in range(8):
                if boardCoord[ligne][colonne] in pieceNoir:
                    if boardCoord[ligne][colonne] == b.np:
                        for coup in (pion(boardCoord, ligne, colonne, color)):
                            boardCoord[coup[0]][coup[1]] = b.np
                            if Echec(color):
                                pass
                            else:
                                Coups.append(coup)
                            boardCoord[ligne][colonne] = b.np
                    elif boardCoord[ligne][colonne] == b.nt:
                        for coup in (tour(boardCoord, ligne, colonne, color)):
                            boardCoord[coup[0]][coup[1]] = b.nt
                            if Echec(color):
                                pass
                            else:
                                Coups.append(coup)
                            boardCoord[ligne][colonne] = b.nt
                    elif boardCoord[ligne][colonne] == b.nf:
                        for coup in (fou(boardCoord, ligne, colonne, color)):
                            boardCoord[coup[0]][coup[1]] = b.nf
                            if Echec(color):
                                pass
                            else:
                                Coups.append(coup)
                            boardCoord[ligne][colonne] = b.nf
                    elif boardCoord[ligne][colonne] == b.nc:
                        for coup in (
                                cavalier(boardCoord, ligne, colonne, color)):
                            boardCoord[coup[0]][coup[1]] = b.nc
                            if Echec(color):
                                pass
                            else:
                                Coups.append(coup)
                            boardCoord[ligne][colonne] = b.nc
                    elif boardCoord[ligne][colonne] == b.nd:
                        for coup in (dame(boardCoord, ligne, colonne, color)):
                            boardCoord[coup[0]][coup[1]] = b.nd
                            if Echec(color):
                                pass
                            else:
                                Coups.append(coup)
                            boardCoord[ligne][colonne] = b.nd

                    elif boardCoord[ligne][colonne] == b.nr:
                        for coup in (roi(boardCoord, ligne, colonne, color)):
                            print(coup)
                            boardCoord[coup[0]][coup[1]] = b.nr
                            if Echec(color):
                                pass
                            else:
                                Coups.append(coup)
                            boardCoord[ligne][colonne] = b.nr

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


def echecmat(color, color2, pieceCoord, coordRoi):
    a = piecepath(pieceCoord, coordRoi)
    b = coupPossible(color2)
    def any_in(a, b): return any(i in b for i in a)
    if (any_in(a, b)):
        return False
    else:
        return True


print(coupPossible("n"))
#print(echecmat("n", "b", [0, 1], [0, 3]))
