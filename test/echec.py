from board import boardCoord, pieceBlanc, pieceNoir
import board as b
from tour import tour
from fou import fou
from roi import roi
from cavalier import cavalier
from dame import dame
from pion import pion


def coordRoi(color):
    for x in range(8):
        for y in range(8):
            if boardCoord[x][y] == "♚" and color == "n":
                return [x, y]

            if boardCoord[x][y] == "♔" and color == "b":
                return [x, y]


def coupPossibles(color):
    if color == "n":
        color = "b"
        for ligne in range(8):
            for colonne in range(8):
                if boardCoord[ligne][colonne] in pieceBlanc:
                    if boardCoord[ligne][colonne] == b.bp:
                        for coup in (pion(boardCoord, ligne, colonne, color)):
                            if coordRoi("n") == coup:
                                return True, [ligne, colonne]
                    elif boardCoord[ligne][colonne] == b.bt:
                        for coup in (tour(boardCoord, ligne, colonne, color)):
                            if coordRoi("n") == coup:
                                return True, [ligne, colonne]
                    elif boardCoord[ligne][colonne] == b.bf:
                        for coup in (fou(boardCoord, ligne, colonne, color)):
                            if coordRoi("n") == coup:
                                return True, [ligne, colonne]
                    elif boardCoord[ligne][colonne] == b.bc:
                        for coup in (
                                cavalier(boardCoord, ligne, colonne, color)):
                            if coordRoi("n") == coup:
                                return True, [ligne, colonne]
                    elif boardCoord[ligne][colonne] == b.bd:
                        for coup in (dame(boardCoord, ligne, colonne, color)):
                            if coordRoi("n") == coup:
                                return True, [ligne, colonne]

                    elif boardCoord[ligne][colonne] == b.br:
                        for coup in (roi(boardCoord, ligne, colonne, color)):
                            if coordRoi("n") == coup:
                                return True, [ligne, colonne]
        return False, []

    elif color == "b":
        color = "n"
        for ligne in range(8):
            for colonne in range(8):
                if boardCoord[ligne][colonne] in pieceNoir:
                    if boardCoord[ligne][colonne] == b.np:
                        for coup in (pion(boardCoord, ligne, colonne, color)):
                            if coordRoi("b") == coup:
                                return True, [ligne, colonne]
                    elif boardCoord[ligne][colonne] == b.nt:
                        for coup in (tour(boardCoord, ligne, colonne, color)):
                            if coordRoi("b") == coup:
                                return True, [ligne, colonne]
                    elif boardCoord[ligne][colonne] == b.nf:
                        for coup in (fou(boardCoord, ligne, colonne, color)):
                            if coordRoi("b") == coup:
                                return True, [ligne, colonne]
                    elif boardCoord[ligne][colonne] == b.nc:
                        if coordRoi("b") == coup:
                            return True, [ligne, colonne]
                        for coup in (
                                cavalier(boardCoord, ligne, colonne, color)):
                            if coordRoi("b") == coup:
                                return True, [ligne, colonne]
                    elif boardCoord[ligne][colonne] == b.nd:
                        for coup in (dame(boardCoord, ligne, colonne, color)):
                            if coordRoi("b") == coup:
                                return True, [ligne, colonne]
                    elif boardCoord[ligne][colonne] == b.nr:
                        for coup in (roi(boardCoord, ligne, colonne, color)):
                            if coordRoi("b") == coup:
                                return True, [ligne, colonne]
        return False, []


def Echec(color):
    bool, table = coupPossibles(color)
    return bool