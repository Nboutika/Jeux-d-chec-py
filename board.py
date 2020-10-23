

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
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
        ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'],
    ]

"""
    Représentation des coordonnées du plateau : 
    0 1 2 3 4 5 6 7 
---------------------
0|  ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
1|  ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎
2|  - - - - - - - -
3|  - - - - - - - -
4|  - - - - - - - -
5|  - - - - - - - -
6|  ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
7|  ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
"""

b = BoardCoord()

l=int(input("Veuillez saisir un entier entre [0,7] pour la ligne désirée : "))
while l<0 or l>7 :
    l=int(input("Nombre incorrect , veuillez ressaisir un entier entre [0,7] pour la ligne désirée : "))

c=int(input("Veuillez saisir un entier entre [0,7] pour  la colonne désirée : "))
while c<0 or c>7 : 
    c=int(input("Nombre incorrect , veuillez ressaisir un entier entre [0,7] pour  la colonne désirée : "))

print(b.BoardCoord[l][c])

for ligne in range(8) :
    for colonne in range(8) :
        print(b.BoardCoord[ligne][colonne]," ",end='')
    print("")
