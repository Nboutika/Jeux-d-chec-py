from pieces.fou import fou
from pieces.tour import tour


def dame(boardCoord,  ligne, colonne, ligneArrive, colonneArrive, couleur):
    return (fou(boardCoord,  ligne, colonne, ligneArrive, colonneArrive, couleur) or tour(boardCoord,  ligne, colonne, ligneArrive, colonneArrive, couleur))
