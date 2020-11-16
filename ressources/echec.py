from ressources.board import boardCoord, pieceBlanc, pieceNoir
import ressources.board as b
from pieces.tour import tour
from pieces.fou import fou
from pieces.roi import roi
from pieces.cavalier import cavalier
from pieces.dame import dame
from pieces.pion import pion

# on test toutes les cases de l'échiquier jusqu'à trouver le roi


def coordRoi(color):
    for x in range(8):
        for y in range(8):
            if boardCoord[x][y] == "♚" and color == "n":
                return [x, y]

            if boardCoord[x][y] == "♔" and color == "b":
                return [x, y]


# On récupère tous les coups possibles de l'adversaire pour savoir si le roi est en échec
def toutCoupsPossibles(color):
    if color == "n":  # Pour le roi noir
        color = "b"  # on prend les coups possibles des pièces blanches
        for ligne in range(8):
            for colonne in range(8):
                # Si la pièce est blanche (définie dans le board)
                # Pour chaque pièce on regarde si le roi est capturable, si oui on renvoie vrai (échec) et les
                # coordonnées de la pièce qui met en échec(utile pour le mat)
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
        # Si aucune pièce ne peut capturer le roi alors le roi n'est pas en échec (et tableau vide car aucune pièce)
        return False, []

    elif color == "b":  # Pareil mais pour les blancs
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


# Je passe par une fonction intermédiaire car je renvoie un booléen et un tableau, cependant uniquement le booléen m'intéresse ici
def Echec(color):
    # table renvoie les coordonnées de la pièce qui attaque, inutile pour notre fonction d'échec
    bool, table = toutCoupsPossibles(color)
    return bool
