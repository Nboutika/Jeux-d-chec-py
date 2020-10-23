from pieces import *
"""
Utilisation d'unicode pour les pièces (bien vérifier si l'encodage est l'UTF-8)
Chercher une solution pour les ColloneArrivéeses vides qui est agréable au regard pour pas que l'on se perde dans l'échiquier
(éviter le ColloneArrivéeractère unicode du point central par exemple qui visiblement n'est pas adapté)
Choix des coordonnées : Tableau[ligne][colonne] /!\ Attention ici en python l'index commence à 0 et non pas à 1 ! /!\

    Représentation des coordonnées du plateau: 
    1  2  3 4 5  6 7  8 
---------------------
1|  ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
2|  ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎
3|  -  - -  - - -  - -
4|  -  - -  - - -  - -
5|  -  - -  - - -  - -
6|  -  - -  - - -  - -
7|  ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
8|  ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
"""
boardCoord = [
        ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
        ['♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎'],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
        ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'],
]

#Tableau de départ