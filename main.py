from board import *
from pieces import *


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


for l in range(8) :
    L=l+1
    print(L," ",end="")
    for c in range(8) :
        print(boardCoord[l][c]," ",end="")
    print("")

print("   1  2  3  4  5  6  7  8")

lancer=input("Veuillez appuyez sur entrée pour commencer")
Jeux(lancer)