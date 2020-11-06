def boardlimit(ligneArrive, colonneArrive):
    # limite de l'échiquier {0 - 7}
    return ligneArrive > -1 and ligneArrive < 8 and colonneArrive > -1 and colonneArrive < 8
