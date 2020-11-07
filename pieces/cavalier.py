from ressources.vide import vide
from ressources.board import boardCoord, pieceBlanc, pieceNoir
from ressources.boardlimit import boardlimit


def cavalier(boardCoord, ligne, colonne, couleur):
    legalmoves = []
    if couleur == "n":  # Si le cavalier est noir
        color = pieceBlanc  # il peut manger les pièces blanches
    else:  # si il n'est pas noir (donc forcément blanc)
        color = pieceNoir  # il peut manger les pièces noires

    poscavalier = [ligne, colonne]  # on prend la position du cavalier
    deplacement = [[2, 1], [2, -1], [-2, 1],
                   [-2, -1], [-1, -2], [1, -2], [1, 2], [-1, 2]]  # on liste ici tous les déplacements possibles du cavalier
    for possibilite in deplacement:  # Pour chaque déplacement possible
        # la ligne équivaux à celle de départ + le déplacement possible pour la ligne
        row = poscavalier[0] + possibilite[0]
        column = poscavalier[1] + possibilite[1]  # pareil pour la colonne
        # Si cette position est comprise dans l'échiquier et que c'est vide
        if boardlimit(row, column) and vide(boardCoord, row, column):
            legalmoves.append([row, column])  # Le mouvement est possible
        # Sinon si on a une pièce qui est de la couleur adverse
        elif boardlimit(row, column) and boardCoord[row][column] in color:
            legalmoves.append([row, column])  # Le mouvement est possible
    # On renvoie un booléen qui regarde si le déplacement du joueur est possible
    return legalmoves