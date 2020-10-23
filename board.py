from pieces import *

"""
Utilisation d'unicode pour les pièces (bien vérifier si l'encodage est l'UTF-8)
Chercher une solution pour les ColloneArrivéeses vides qui est agréable au regard pour pas que l'on se perde dans l'échiquier
(éviter le ColloneArrivéeractère unicode du point central par exemple qui visiblement n'est pas adapté)
Choix des coordonnées : Tableau[ligne][colonne] /!\ Attention ici en python l'index commence à 0 et non pas à 1 ! /!\
"""


class Board():
    def __init__(self):
        self.BoardCoord = [
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
    Représentation des coordonnées du plateau:
    0 1 2 3 4 5 6 7
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

b = Board()


print("Pour jouez utiliser |ligne de la pièce| |colonne de la pièce| |ligne d'arrivé| |colonne d'arrivé|")
commande = input("Jouez votre coup : ").split(" ")
commandeTableau = []

for i in commande:
    if i != "":
        commandeTableau.append(int(i))

for i in range(len(commandeTableau)):
    if commandeTableau[i] < 0 or commandeTableau[i] > 7:
        print("Pas dans l'intervalle")
    else:
        print("Dans l'intervalle")

ligne = commandeTableau[0]
colonne = commandeTableau[1]
ligneArrive = commandeTableau[2]
colonneArrive = commandeTableau[3]


print(ligne, colonne, ligneArrive, colonneArrive)
if ligne == ligneArrive and colonne == colonneArrive:
    print("Il faut forcément faire un mouvement")
else:
    if b.BoardCoord[ligne][colonne] == "♜":
        print("tour blanche")
        if tour(b.BoardCoord, ligne, colonne, ligneArrive, colonneArrive):
            print("mouvement possible")
        else:
            print("mouvement pas possible")
    if b.BoardCoord[ligne][colonne] == "♞":
        print("cavalier blanc")
        if cavalier(b.BoardCoord, ligne, colonne, ligneArrive, colonneArrive):
            print("mouvement possible")
        else:
            print("mouvement pas possible")
    if b.BoardCoord[ligne][colonne] == "♝":
        print("fou blanc")
        if fou(b.BoardCoord, ligne, colonne, ligneArrive, colonneArrive):
            print("mouvement possible")
        else:
            print("mouvement pas possible")
    if b.BoardCoord[ligne][colonne] == "♛":
        print("reine blanc")
        if dame(b.BoardCoord, ligne, colonne, ligneArrive, colonneArrive):
            print("mouvement possible")
        else:
            print("mouvement pas possible")
    if b.BoardCoord[ligne][colonne] == "♚":
        print("roi blanc")
        if roi(b.BoardCoord, ligne, colonne, ligneArrive, colonneArrive):
            print("mouvement possible")
        else:
            print("mouvement pas possible")
    if b.BoardCoord[ligne][colonne] == "♟︎":
        print("pion blanc ")
        # pas encore de fonction pion blanc
        if pionNoir(b.BoardCoord, ligne, colonne, ligneArrive, colonneArrive):
            print("mouvement possible")
        else:
            print("mouvement pas possible")
    if b.BoardCoord[ligne][colonne] == "♖":
        print("tour noir")
        if tour(b.BoardCoord, ligne, colonne, ligneArrive, colonneArrive):
            print("mouvement possible")
        else:
            print("mouvement pas possible")
    if b.BoardCoord[ligne][colonne] == "♘":
        print("cavalier noir")
        if cavalier(b.BoardCoord, ligne, colonne, ligneArrive, colonneArrive):
            print("mouvement possible")
        else:
            print("mouvement pas possible")
    if b.BoardCoord[ligne][colonne] == "♗":
        print("fou noir")
        if fou(b.BoardCoord, ligne, colonne, ligneArrive, colonneArrive):
            print("mouvement possible")
        else:
            print("mouvement pas possible")
    if b.BoardCoord[ligne][colonne] == "♕":
        print("reine noir")
        if dame(b.BoardCoord, ligne, colonne, ligneArrive, colonneArrive):
            print("mouvement possible")
        else:
            print("mouvement pas possible")
    if b.BoardCoord[ligne][colonne] == "♔":
        print("roi noir")
        if roi(b.BoardCoord, ligne, colonne, ligneArrive, colonneArrive):
            print("mouvement possible")
        else:
            print("mouvement pas possible")
    if b.BoardCoord[ligne][colonne] == "♙":
        print("pion noir ")
        if pionNoir(b.BoardCoord, ligne, colonne, ligneArrive, colonneArrive):
            print("mouvement possible")
        else:
            print("mouvement pas possible")
    b.BoardCoord[ligneArrive][colonneArrive] = b.BoardCoord[ligne][colonne]
    b.BoardCoord[ligne][colonne] = "-"
for l in range(8):
    print(l, " ", end="")
    for c in range(8):
        print(b.BoardCoord[l][c], " ", end="")
    print("")
print("   a  b  c  d  e  f  g  h")
