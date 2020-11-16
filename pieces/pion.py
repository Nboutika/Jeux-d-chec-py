from ressources.vide import vide
from ressources.board import boardCoord, pieceBlanc, pieceNoir
from ressources.boardlimit import boardlimit


def pion(boardCoord, ligne, colonne, couleur):
    legalmoves = []
    pospion = [ligne, colonne]  # position de départ du pion
    if couleur == "n":  # pion noir
        color = pieceBlanc  # couleur des pions adverses
        # déplacement possible pour manger une pièce
        deplacement = [[1, -1], [1, 1]]
        if pospion[0] == 1:  # si le pion est à sa position de départ et donc il peut bouger soit de 1 ou de 2 cases au choix
            i = 1
            while i <= 2:  # Pareil que pour le fou/tour/dame boucle infinie avec un i que l'on va incrémenter
                # le pion avance uniquement en ligne et pour le pion noir on incrémente de 1
                row = pospion[0] + i
                column = pospion[1]  # la colonne ne change pas
                # si c'est dans l'échiquier et vide
                if boardlimit(row, column) and vide(boardCoord, row, column):
                    # on ajoute les coordonnées aux mouvements possibles
                    legalmoves.append([row, column])
                    i += 1
                else:
                    break  # si la case n'est pas vide alors on arrête la boucle car le pion ne mange pas en ligne droite
            for possibilite in deplacement:  # on voit si une pièce est en diagonal
                rowDestroy = pospion[0] + possibilite[0]
                columnDestroy = pospion[1] + possibilite[1]

                # si une pièce est en diagonal alors on peut manger cette pièce
                if boardlimit(rowDestroy, columnDestroy) and boardCoord[rowDestroy][columnDestroy] in color:
                    legalmoves.append([rowDestroy, columnDestroy])
        else:  # si le pion n'est pas en position de départ
            # mouvement basique de pion de 1 en 1 en ligne
            row = pospion[0] + 1
            column = pospion[1]
            if boardlimit(row, column) and vide(boardCoord, row, column):
                legalmoves.append([row, column])
            for possibilite in deplacement:
                rowDestroy = pospion[0] + possibilite[0]
                columnDestroy = pospion[1] + possibilite[1]
                if boardlimit(rowDestroy, columnDestroy) and boardCoord[rowDestroy][columnDestroy] in color:
                    legalmoves.append([rowDestroy, columnDestroy])

    else:  # Si le pion est blanc
        color = pieceNoir
        # le pion blanc fait l'inverse du noir c'est donc des -1 et non des 1
        deplacement = [[-1, -1], [-1, 1]]
        if pospion[0] == 6:  # position de départ du pion blanc
            i = -1
            while i >= -2:
                # On ajoute des nombres négatifs mais on aurait pu  soustraire des nombres positifs
                row = pospion[0] + i
                column = pospion[1]
                if boardlimit(row, column) and vide(boardCoord, row, column):
                    legalmoves.append([row, column])
                    i -= 1  # on décrémente car pion blanc donc inverse du pion noir
                else:
                    break
            for possibilite in deplacement:
                rowDestroy = pospion[0] + possibilite[0]
                columnDestroy = pospion[1] + possibilite[1]
                if boardlimit(rowDestroy, columnDestroy) and boardCoord[rowDestroy][columnDestroy] in color:
                    legalmoves.append([rowDestroy, columnDestroy])
        else:  # si le pion n'est pas en position de départ donc mouvement normal
            row = pospion[0] - 1
            column = pospion[1]
            if boardlimit(row, column) and vide(boardCoord, row, column):
                legalmoves.append([row, column])
            for possibilite in deplacement:
                rowDestroy = pospion[0] + possibilite[0]
                columnDestroy = pospion[1] + possibilite[1]
                if boardlimit(rowDestroy, columnDestroy) and boardCoord[rowDestroy][columnDestroy] in color:
                    legalmoves.append([rowDestroy, columnDestroy])
    # on renvoie si le mouvement est possible
    return legalmoves
