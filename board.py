

"""
Utilisation d'unicode pour les pièces (bien vérifier si l'encodage est l'UTF-8)
Chercher une solution pour les cases vides qui est agréable au regard pour pas que l'on se perde dans l'échiquier
(éviter le caractère unicode du point central par exemple qui visiblement n'est pas adapté)
Choix des coordonnées : Tableau[ligne][colonne] /!\ Attention ici en python l'index commence à 0 et non pas à 1 ! /!\
"""


class BoardCoord:

    BoardCoord = [
        ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
        ['♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎'],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
        ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'],
    ]

"""
    Représentation des coordonnées du plateau : 
    0  1 2  3 4  5 6 7 
---------------------
0|  ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
1|  ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎
2|  -  - -  - - -  - -
3|  -  - -  - - -  - -
4|  -  - -  - - -  - -
5|  -  - -  - - -  - -
6|  ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
7|  ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
"""

b = BoardCoord()
l=int(input("Entrer un entier de la ligne désirée  inférieur a 8 : "))
c=int(input("Entrer un entier de la colonne désirée  inférieur a 8 : "))
print(b.BoardCoord[l][c])
