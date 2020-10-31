
"""
----------------------------------------------------------------
board.py contient:
-La fonction affichageBoard qui permet d'afficher le plateau
-Le plateau avec les pièces en position initiale 
-Les variables des pièces avec leur représentation visuelle
----------------------------------------------------------------
Utilisation d'unicode pour les pièces (bien vérifier si l'encodage est l'UTF-8)
    
Représentation des coordonnées du plateau depuis le terminal 
Dans le programme  les index sont diminués de 1 
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
nr = "♚"
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
    ["-", "-", "-", "-", "-", nc, "-", "-"],
    ["-", "-", "-", bc, "-", "-", "-", "-"],
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
