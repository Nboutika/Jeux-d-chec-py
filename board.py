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

nt = '♜'
nc = '♞'
nf = '♝'
nr = '♚'
nd = '♛'
np = '♟︎'
bt = '♖'
bc = '♘'
bf = '♗'
br = '♔'
bd = '♕'
bp = '♙'

pieceBlanc = [bp, bt, bf, bc, bd, br]
pieceNoir = [np, nt, nf, nc, nd, nr]

boardCoord = [
    [nt, nc, nf, nd, nr, nf, nc, nt],
    [np, np, np, np, np, np, np, np],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    [bp, bp, bp, bp, bp, bp, bp, bp],
    [bt, bc, bf, bd, br, bf, bc, bt],
]


def affichageBoard():
    print(30*"-")
    print("   1  2  3  4  5  6  7  8")
    for l in range(8):
        L = l+1
        print(L, " ", end="")
        for c in range(8):
            print(boardCoord[l][c], " ", end="")
        print("")

    print("   1  2  3  4  5  6  7  8")
    print(30*"-")
