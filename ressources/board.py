"""
----------------------------------------------------------------
board.py contient:
-Le plateau avec les pièces en position initiale (tableau bidimensionnelles)
-Le plateau de la partie
-Les variables des pièces avec leur représentation visuelle
-Des tableaux qui représente l'hitorique des coups des pièces (pour l'égalité 3 mouvements répètes)
-Des tableaux qui contienent toutes les pièces d'une couleur 
-Un dictionnaire pour convertir les index des colonnes 
-La fonction affichageBoard qui permet d'afficher le plateau
-La fonction resetBoard qui permet de remettre le plateau avec les pièces en position originale
----------------------------------------------------------------
Utilisation d'unicode pour les pièces (bien vérifier si l'encodage est l'UTF-8)
    
Représentation des coordonnées du plateau depuis le terminal 
Dans le programme  les index de ligne sont diminués 1 
    a  b  c d e  f g  h 
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

boardCoordInit = [
    [nt, nc, nf, nd, nr, nf, nc, nt],
    [np, np, np, np, np, np, np, np],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    [bp, bp, bp, bp, bp, bp, bp, bp],
    [bt, bc, bf, bd, br, bf, bc, bt],
]

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


def resetBoard():
    for l in range(8):
        for c in range(8):
            boardCoord[l][c] = boardCoordInit[l][c]
