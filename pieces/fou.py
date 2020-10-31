from ressources.vide import vide
from ressources.board import boardCoord, pieceBlanc, pieceNoir
from ressources.boardlimit import boardlimit


def fou(boardCoord,  ligne, colonne, ligneArrive, colonneArrive, couleur):
    legalmoves = []
    if couleur == "n":  # si la couleur est noir
        color = pieceBlanc  # les adversaires sont blancs
    else:
        color = pieceNoir  # sinon les adversaires sont noirs
    posfou = [ligne, colonne]  # position actuelle de la pièce
    # déplacement possible du fou
    deplacement = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
    for possibilite in deplacement:
        i = 1
        while True:  # boucle infinie
            # On va prendre la position de départ auquel on aditionne la possibilité * i
            row = posfou[0] + i * possibilite[0]
            column = posfou[1] + i * possibilite[1]
            # si c'est dans l'échiquier et que la case est vide
            if boardlimit(row, column) and vide(boardCoord, row, column):
                # on ajoute les coordoonées dans le tableau des mouvements possibles
                legalmoves.append([row, column])
                i += 1
            else:
                # si on a une pièce dans l'échiquier et de couleur adverse
                if boardlimit(row, column) and boardCoord[row][column] in color:
                    # on ajoute les coordoonées aux mouvements possibles
                    legalmoves.append([row, column])
                break  # on stop la boucle infinie car on ne peut sauter au dessus des pièces
    # on renvoie si le mouvement du joueur est possible
    return [ligneArrive, colonneArrive] in legalmoves
