from ressources.board import boardCoord, pieceBlanc, pieceNoir
import ressources.board as b
from pieces.tour import tour
from pieces.fou import fou
from pieces.roi import roi
from pieces.cavalier import cavalier
from pieces.dame import dame
from pieces.pion import pion
from ressources.echec import Echec, coordRoi, toutCoupsPossibles

# Ici on récupère les coups possibles, mais on retire toute action provoquant un échec de sorte à vraiment avoir des coups possibles


def coupPossible(color):
    Coups = []
    if color == "b":  # Les coups possibles des blancs
        for ligne in range(8):
            for colonne in range(8):
                if boardCoord[ligne][colonne] in pieceBlanc:
                    # On test toutes les pièces
                    if boardCoord[ligne][colonne] == b.bp:
                        for coup in pion(boardCoord, ligne, colonne, color):  # Pour chaque coup
                            # On enlève la pièce de sa position
                            boardCoord[ligne][colonne] = "-"
                            # Variable tampon pour la pièce qui était à cette endroit
                            temp = boardCoord[coup[0]][coup[1]]
                            # On effectue le mouvement
                            boardCoord[coup[0]][coup[1]] = b.bp
                            # Si après le mouvement on n'est pas en échec
                            if not Echec(color):
                                # Le coup est valide donc on l'ajoute à notre tableau
                                Coups.append(coup)
                            # On remplace les pièces au bon endroit
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.bp
                    # Le procédé ci dessus se répète pour chaque pièce
                    elif boardCoord[ligne][colonne] == b.bt:
                        for coup in tour(boardCoord, ligne, colonne, color):
                            boardCoord[ligne][colonne] = "-"
                            temp = boardCoord[coup[0]][coup[1]]
                            boardCoord[coup[0]][coup[1]] = b.bt
                            if not Echec(color):
                                Coups.append(coup)
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.bt

                    elif boardCoord[ligne][colonne] == b.bf:
                        for coup in fou(boardCoord, ligne, colonne, color):
                            boardCoord[ligne][colonne] = "-"
                            temp = boardCoord[coup[0]][coup[1]]
                            boardCoord[coup[0]][coup[1]] = b.bf
                            if not Echec(color):
                                Coups.append(coup)
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.bf

                    elif boardCoord[ligne][colonne] == b.bc:
                        for coup in cavalier(boardCoord, ligne, colonne, color):
                            boardCoord[ligne][colonne] = "-"
                            temp = boardCoord[coup[0]][coup[1]]
                            boardCoord[coup[0]][coup[1]] = b.bc
                            if not Echec(color):
                                Coups.append(coup)
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.bc

                    elif boardCoord[ligne][colonne] == b.bd:
                        for coup in dame(boardCoord, ligne, colonne, color):

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
                        for coup in pion(boardCoord, ligne, colonne, color):
                            boardCoord[ligne][colonne] = "-"
                            temp = boardCoord[coup[0]][coup[1]]
                            boardCoord[coup[0]][coup[1]] = b.np
                            if not Echec(color):
                                Coups.append(coup)
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.np
                    elif boardCoord[ligne][colonne] == b.nt:
                        for coup in tour(boardCoord, ligne, colonne, color):
                            boardCoord[ligne][colonne] = "-"
                            temp = boardCoord[coup[0]][coup[1]]
                            boardCoord[coup[0]][coup[1]] = b.nt
                            if not Echec(color):
                                Coups.append(coup)
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.nt
                    elif boardCoord[ligne][colonne] == b.nf:
                        for coup in fou(boardCoord, ligne, colonne, color):
                            boardCoord[ligne][colonne] = "-"
                            temp = boardCoord[coup[0]][coup[1]]
                            boardCoord[coup[0]][coup[1]] = b.nf
                            if not Echec(color):
                                Coups.append(coup)
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.nf
                    elif boardCoord[ligne][colonne] == b.nc:
                        for coup in cavalier(boardCoord, ligne, colonne, color):
                            boardCoord[ligne][colonne] = "-"
                            temp = boardCoord[coup[0]][coup[1]]
                            boardCoord[coup[0]][coup[1]] = b.nc
                            if not Echec(color):
                                Coups.append(coup)
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.nc
                    elif boardCoord[ligne][colonne] == b.nd:
                        for coup in dame(boardCoord, ligne, colonne, color):
                            boardCoord[ligne][colonne] = "-"
                            temp = boardCoord[coup[0]][coup[1]]
                            boardCoord[coup[0]][coup[1]] = b.nd
                            if not Echec(color):
                                Coups.append(coup)
                            boardCoord[coup[0]][coup[1]] = temp
                            boardCoord[ligne][colonne] = b.nd

        return Coups


# Chemin emprunter par la pièce pour mettre en échec le roi
# J'ai créer cette fonction sans l'aide d'internet je suis donc plutôt fier de moi et j'écouterai mes prochains cours de math
def piecepath(pieceCoord, kingCoord):
    path = []
    # La dans le chemin emprunter par la pièce, on a la position de la pièce elle même (qui pourra être capturer peut-être)
    path.append(pieceCoord)
    # Ici on fait la différence des emplacements entre le roi et la pièce
    x = kingCoord[0] - pieceCoord[0]
    y = kingCoord[1] - pieceCoord[1]
    # On divise pas par zéro mathématique de base je ne vous apprends rien
    if x != 0:
        # On prend la valeur absolue pour avoir les négatifs (étudier le fonctionnement des signes mathématiques)
        x1 = x // abs(x)
    else:
        x1 = x  # si x = 0 bah on a besoin de rien faire on est sur la même ligne que le roi
    if y != 0:
        y1 = y // abs(y)  # même chose pour la colonne
    else:
        y1 = y  # ici y = 0 indique qu'on est sur la même colonne
    i = 1
    # Boucle infini
    while True:
        # Ici on va récuperer la ligne et la colonne grâce à notre x1 et y1  en partant de la pièce (d'où la valeur absolue sinon on n'aura pas le chemin emprunter)
        row = pieceCoord[0] + i * x1
        column = pieceCoord[1] + i * y1
        # quand on arrive enfin aux coordonnées du roi on peut arrêter la boucle et renvoyer notre chemin
        if [row, column] == kingCoord:
            break
        # Si on arrive pas sur les coordonnées du roi on ajoute les cases dans notre tableau et on incrémente i pour se rapprocher
        else:
            path.append([row, column])
            i += 1
    return path


# Ici on va récuperer les mouvements du roi qui ne cause pas un échec cette fonction est similaire à celle du dessous mais pour le roi
def mouvementRoi(color):
    if color == "n":  # roi noir

        Coups = []
        ligne = coordRoi(color)[0]  # Fonction déclaré pour l'échec
        colonne = coordRoi(color)[1]
        # j'ai déjà commenté ceci dans la fonction coupPossible
        for coup in (roi(boardCoord, ligne, colonne, color)):
            boardCoord[ligne][colonne] = "-"
            temp = boardCoord[coup[0]][coup[1]]
            boardCoord[coup[0]][coup[1]] = b.nr
            if not Echec(color):
                Coups.append(coup)
            boardCoord[coup[0]][coup[1]] = temp
            boardCoord[ligne][colonne] = b.nr
        return Coups
    else:
        Coups = []
        ligne = coordRoi(color)[0]
        colonne = coordRoi(color)[1]
        for coup in (roi(boardCoord, ligne, colonne, color)):
            boardCoord[ligne][colonne] = "-"
            temp = boardCoord[coup[0]][coup[1]]
            boardCoord[coup[0]][coup[1]] = b.br
            if not Echec(color):
                Coups.append(coup)
            boardCoord[coup[0]][coup[1]] = temp
            boardCoord[ligne][colonne] = b.br
        return Coups
    """La différence entre mouvementRoi et coup possible, c'est que l'on va récupérer les coups possibles pour bloquer un échec mais
        Le roi ne peut pas bloquer un échec lui même, cela n'a aucun sens j'ai donc séparer le roi du reste"""


def echecmat(color):
    # Ici pareil que pour l'échec j'ai besoin que d'un return et non des deux
    bool, table = toutCoupsPossibles(color)
    # Si on a bien une pièce qui met en échec mais normalement on appelle cette fonction uniquement si le roi est en échec donc pas vraiment besoin de vérifier
    if table:
        # On prend le chemin emprunter par la pièce pour mettre le roi en échec
        a = piecepath(table, coordRoi(color))
        # on récupère nos coups possibles pour tenter de bloquer l'échec
        b = coupPossible(color)
        # De base c'était un lambda mais VSC me l'a converti en fonction
        # On a ici une fonction qui vérifier si on a AU MOINS une valeur du chemin emprunter DANS les coups possibles
        def any_in(a, b): return any(i in b for i in a)
        # Si aucun mouvement ne permet de bloquer l'échec
        if not (any_in(a, b)):
            # On vérifie si le roi peut s'en sortir tout seul en se déplaçant
            if mouvementRoi(color) == []:
                # Si le roi n'a aucun mouvement possible il est échec et mat
                return True
            # Si il a un mouvement possible, il n'est pas mat
            else:
                return False
        # Si une pièce permet de bloquer l'échec (n'oublions pas que on peut également capturer la pièce attanquante) on est pas mat
        else:
            return False
    if not table:  # Si aucune pièce ne met en échec, on n'est pas mat plutôt logique
        return False


"""
J'ai pensé à ajouter cette fonction Pat dans le tas car je me suis rendu compte que c'était très simple de l'implémenté
et que ma fonction échec et mat de base faisait pat si on ne vérifiait pas l'échec au préalable
"""


def pat(color):
    # Si on a aucun mouvement possible (considérant l'échec)
    if coupPossible(color) == []:
        # Et que notre roi ne peut se déplacer
        if mouvementRoi(color) == []:
            # Il y a égalité
            return True
        else:
            return False
    else:
        return False
    # Bien évidemment ici on ne teste pas l'échec avant, le pat = échec et mat sans être en échec au préalable
