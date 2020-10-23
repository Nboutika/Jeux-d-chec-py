
"""
Initialisation des pièces
La tour : Elle se déplace en ligne et colonne([+x][+0] OU [+0][+x])
Le cavalier : Il se déplace en "L" donc il se déplace de 2 lignes et 1 colonne([1][0]) mais dans tous les sens 
Donc +-[2]+-[1] ET aussi +-[1]+-[2]
Le fou : il se déplace toujours en diagonale [+x][+x]
La dame : Elle a tous les mouvements des autres pièces sauf le cavalier
Le roi : comme la dame mais de 1 en 1
Pion : les noirs se déplace en ligne [+x][0]
Pion blanc : [-x][0]

# l = ligne départ
# c = colonne départ
# la, colonneArrive = ligne/colonne arrivé

boardCoord = []
ligne = None
colonne = None
colonneArrive = None
ligneArrive = None
"""

def vide(boardCoord,  ligne, colonne, ligneArrive, colonneArrive):
    return boardCoord[ligneArrive][colonneArrive] == "-"

def pionNoir(boardCoord,  ligne, colonne, ligneArrive, colonneArrive):
    return (colonne == colonneArrive and ligneArrive == ligne + 1) and vide(boardCoord,  ligne, colonne, ligneArrive, colonneArrive)


def tour(boardCoord,  ligne, colonne, ligneArrive, colonneArrive):
    return ligne == ligneArrive or colonne == colonneArrive and vide(boardCoord,  ligne, colonne, ligneArrive, colonneArrive)


def cavalier(boardCoord,  ligne, colonne, ligneArrive, colonneArrive):
    return (ligne - 2 <= ligneArrive <= ligne + 2 and colonne - 1 <= colonneArrive <= colonne + 1) or (colonne - 2 <= colonneArrive <= colonne + 2 and ligne - 1 <= ligneArrive <= ligne + 1) and vide(boardCoord,  ligne, colonne, ligneArrive, colonneArrive)


def fou(boardCoord,  ligne, colonne, ligneArrive, colonneArrive):
    return colonneArrive == ligneArrive and vide(boardCoord,  ligne, colonne, ligneArrive, colonneArrive)


def dame(boardCoord,  ligne, colonne, ligneArrive, colonneArrive):
    return (fou(boardCoord,  ligne, colonne, ligneArrive, colonneArrive) or tour(boardCoord,  ligne, colonne, ligneArrive, colonneArrive)) and vide(boardCoord,  ligne, colonne, ligneArrive, colonneArrive)


def roi(boardCoord,  ligne, colonne, ligneArrive, colonneArrive):
    return ((ligne - 1 <= ligneArrive <= ligne + 1) and (colonne - 1 <= colonne <= colonne + 1)) and vide(boardCoord,  ligne, colonne, ligneArrive, colonneArrive)