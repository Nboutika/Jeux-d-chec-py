

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
    Représentation des coordonnées du pLigneArriveteau : 
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


"""
commande = input("Jouez votre coup : ").split(" ")
commandeTableau = []

for i in commande:
    if i != "":
        commandeTableau.append(int(i))

print(commandeTableau)

"""


ligne=int(input("Veuillez saisir un entier entre [0,7] pour la ligne de départ : "))
while ligne<0 or ligne>7 :
    ligne=int(input("Nombre incorrect , veuillez ressaisir un entier entre [0,7] pour la ligne de départ : "))

colonne=int(input("Veuillez saisir un entier entre [0,7] pour la colonne désirée : "))
while colonne<0 or colonne>7 : 
    colonne=int(input("Nombre incorrect , veuillez ressaisir un entier entre [0,7] pour la colonne désirée : "))


ligneArrive=int(input("Veuillez saisir un entier entre [0,7] pour la nouvelle ligne désirée : "))
while ligneArrive<0 or ligneArrive>7 :
    ligneArrive=int(input("Nombre incorrect , veuillez ressaisir un entier entre [0,7] pour la nouvelle ligne désirée : "))

colonneArrive=int(input("Veuillez saisir un entier entre [0,7] pour  la nouvelle colonne désirée : "))
while colonneArrive<0 or colonneArrive>7 : 
    colonneArrive=int(input("Nombre incorrect , veuillez ressaisir un entier entre [0,7] pour  la nouvelle colonne désirée : "))


if ligne==ligneArrive and colonne==colonneArrive:
    print("Il faut forcément faire un mouvement")
else:
    if b.BoardCoord[ligne][colonne]== "♜":
        print("tour blanche")

    if b.BoardCoord[ligne][colonne]== "♞":
        print("cavalier blanc")

    if b.BoardCoord[ligne][colonne]== "♝":
        print("fou blanc")

    if b.BoardCoord[ligne][colonne]== "♛":
        print("reine blanc")

    if b.BoardCoord[ligne][colonne]== "♚":
        print("roi blanc")

    if b.BoardCoord[ligne][colonne]== "♟︎":
        print("pion blanc ")

    if b.BoardCoord[ligne][colonne]== "♖":
        print("tour noir")

    if b.BoardCoord[ligne][colonne]== "♘":
        print("cavalier noir")

    if b.BoardCoord[ligne][colonne]== "♗":
        print("fou noir")

    if b.BoardCoord[ligne][colonne]== "♕":
        print("reine noir")

    if b.BoardCoord[ligne][colonne]== "♔":
        print("roi noir")

    if b.BoardCoord[ligne][colonne]== "♙":
        print("pion noir ")



    b.BoardCoord[ligneArrive][colonneArrive]=b.BoardCoord[ligne][colonne]
    b.BoardCoord[ligne][colonne]="-"

for l in range(8) :
    print(l," ",end="")
    for c in range(8) :
        print(b.BoardCoord[l][c]," ",end="")
    print("")

print("   a  b  c  d  e  f  g  h")

