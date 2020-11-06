def vide(boardCoord, ligneArrive, colonneArrive):
    # si c'est un "-" la case est vide donc on vérifie si c'est un tiret
    return boardCoord[ligneArrive][colonneArrive] == "-"
