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

historiqueTourB = []
historiqueCavalierB = []
historiqueFouB = []
historiqueRoiB = []
historiqueReineB = []

historiqueTourN = []
historiqueCavalierN = []
historiqueFouN = []
historiqueRoiN = []
historiqueReineN = []


pieceBlanc = [bp, bt, bf, bc, bd, br]
pieceNoir = [np, nt, nf, nc, nd, nr]

boardCoord = [
    ["-", "-", "-", nc, nr, "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", bc, "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", br, "-", "-", "-"],
]


dictionnaireIndex = {"A": "0", "B": "1", "C": "2", "D": "3", "E": "4", "F": "5", "G": "6", "H": "7"
                     }


def affichageBoard():
    print(30*"-")
    print("   A  B  C  D  E  F  G  H")
    for l in range(8):
        L = l+1
        print(L, " ", end="")
        for c in range(8):
            print(boardCoord[l][c], " ", end="")
        print("")

    print("   A  B  C  D  E  F  G  H")
    print(30*"-")
