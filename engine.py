from board import *

"""
Programme de fonctionnement du jeux
Utilise le tableau a double entrée de board.py
Utilise pieces.py pour savoir si le mouvement est possible
"""


def commande():  # On test si la commande est correcte sinon on en demande une nouvelle
    Valable = False
    while Valable == False:
        Valable = True
        print("Pour jouez utiliser |ligne de la pièce| |colonne de la pièce| |ligne d'arrivé| |colonne d'arrivé|")
        coordonnées = input("Jouez votre coup : ").split(" ")
        commandeTableau = []
        for i in coordonnées:
            if i != "":
                commandeTableau.append(int(i))
            for i in range(len(commandeTableau)):
                if commandeTableau[i] < 1 or commandeTableau[i] > 8:
                    Valable = False

    ligne = commandeTableau[0]-1
    colonne = commandeTableau[1]-1
    # On établit les valeurs en input dans des variables
    ligneArrive = commandeTableau[2]-1
    colonneArrive = commandeTableau[3]-1

    return(ligne, colonne, ligneArrive, colonneArrive)


def Jeux():
    roiNoir = True
    roiBlanc = True
    while roiNoir and roiBlanc == True:  # On fait tourner le jeux tant que les deux roix sont présent sur le plateau

        ligne, colonne, ligneArrive, colonneArrive = commande()
        tour = 1
        blanc = tour % 2 > 0
        noir = tour % 2 == 0
        if blanc == True:
            if boardCoord[ligne][colonne] == "-":  # On regarde si c'est une pièce ou non
                print("il n'y a aucune pièce")
            else:
                if ligne == ligneArrive and colonne == colonneArrive:  # On regarde si il y'a un déplacement ou non
                    print("Il faut forcément faire un mouvement")
                else:  # On cherche qu'elle est le type de pièces séléctionné et si le déplacement est possible ou non
                    if boardCoord[ligne][colonne] == "♜":
                        print("vous avez séléctionné la tour blanche")
                        if tour(boardCoord, ligne, colonne, ligneArrive, colonneArrive):
                            boardCoord[ligneArrive][colonneArrive] = boardCoord[ligne][colonne]
                            boardCoord[ligne][colonne] = "-"
                        else:
                            print(
                                "Déplacement de la pièce impossible veuillez faire autre chose")

                    if boardCoord[ligne][colonne] == "♞":
                        print("vous avez séléctionné  le cavalier blanc")
                        if cavalier(boardCoord, ligne, colonne, ligneArrive, colonneArrive):
                            boardCoord[ligneArrive][colonneArrive] = boardCoord[ligne][colonne]
                            boardCoord[ligne][colonne] = "-"
                        else:
                            print(
                                "Déplacement de la pièce impossible veuillez faire autre chose")

                    if boardCoord[ligne][colonne] == "♝":
                        print("vous avez séléctionné  le fou blanc")
                        if fou(boardCoord, ligne, colonne, ligneArrive, colonneArrive):
                            boardCoord[ligneArrive][colonneArrive] = boardCoord[ligne][colonne]
                            boardCoord[ligne][colonne] = "-"
                        else:
                            print(
                                "Déplacement de la pièce impossible veuillez faire autre chose")

                    if boardCoord[ligne][colonne] == "♛":
                        print("vous avez séléctionné  la reine blanc")
                        if dame(boardCoord, ligne, colonne, ligneArrive, colonneArrive):
                            boardCoord[ligneArrive][colonneArrive] = boardCoord[ligne][colonne]
                            boardCoord[ligne][colonne] = "-"
                        else:
                            print(
                                "Déplacement de la pièce impossible veuillez faire autre chose")

                    if boardCoord[ligne][colonne] == "♚":
                        print("vous avez séléctionné  le roi blanc")
                        if roi(boardCoord, ligne, colonne, ligneArrive, colonneArrive):
                            boardCoord[ligneArrive][colonneArrive] = boardCoord[ligne][colonne]
                            boardCoord[ligne][colonne] = "-"
                        else:
                            print(
                                "Déplacement de la pièce impossible veuillez faire autre chose")
                            if boardCoord[ligne][colonne] == "♙":
                                print("vous avez séléctionné  le pion blanc ")
                                if pionBlanc(boardCoord, ligne, colonne, ligneArrive, colonneArrive):
                                    boardCoord[ligneArrive][colonneArrive] = boardCoord[ligne][colonne]
                                    boardCoord[ligne][colonne] = "-"
                                    tour += 1
                                else:
                                    print(
                                        "Déplacement de la pièce impossible veuillez faire autre chose")
                print("   1  2  3  4  5  6  7  8")
                for l in range(8):  # On affiche le plateau après le coup
                    L = l+1
                    print(L, " ", end="")
                    for c in range(8):
                        print(boardCoord[l][c], " ", end="")
                    print("")
                print("   1  2  3  4  5  6  7  8")

        elif noir == True:
            if boardCoord[ligne][colonne] == "-":
                print("il n'y a aucune pièce")
            else:
                if ligne == ligneArrive and colonne == colonneArrive:  # On regarde si il y'a un déplacement ou non
                    print("Il faut forcément faire un mouvement")
                else:  # On cherche qu'elle est le type de pièces séléctionné et si le déplacement est possible ou non
                    if boardCoord[ligne][colonne] == "♖":
                        print("vous avez séléctionné  la tour noir")
                        if tour(boardCoord, ligne, colonne, ligneArrive, colonneArrive):
                            boardCoord[ligneArrive][colonneArrive] = boardCoord[ligne][colonne]
                            boardCoord[ligne][colonne] = "-"
                        else:
                            print(
                                "Déplacement de la pièce impossible veuillez faire autre chose")

                    if boardCoord[ligne][colonne] == "♘":
                        print("vous avez séléctionné  le cavalier noir")
                        if cavalier(boardCoord, ligne, colonne, ligneArrive, colonneArrive):
                            boardCoord[ligneArrive][colonneArrive] = boardCoord[ligne][colonne]
                            boardCoord[ligne][colonne] = "-"
                        else:
                            print(
                                "Déplacement de la pièce impossible veuillez faire autre chose")

                    if boardCoord[ligne][colonne] == "♗":
                        print("vous avez séléctionné  le fou noir")
                        if fou(boardCoord, ligne, colonne, ligneArrive, colonneArrive):
                            boardCoord[ligneArrive][colonneArrive] = boardCoord[ligne][colonne]
                            boardCoord[ligne][colonne] = "-"
                        else:
                            print(
                                "Déplacement de la pièce impossible veuillez faire autre chose")

                    if boardCoord[ligne][colonne] == "♕":
                        print("vous avez séléctionné  la reine noir")
                        if dame(boardCoord, ligne, colonne, ligneArrive, colonneArrive):
                            boardCoord[ligneArrive][colonneArrive] = boardCoord[ligne][colonne]
                            boardCoord[ligne][colonne] = "-"
                        else:
                            print(
                                "Déplacement de la pièce impossible veuillez faire autre chose")

                    if boardCoord[ligne][colonne] == "♔":
                        print("vous avez séléctionné  le roi noir")
                        if roi(boardCoord, ligne, colonne, ligneArrive, colonneArrive):
                            boardCoord[ligneArrive][colonneArrive] = boardCoord[ligne][colonne]
                            boardCoord[ligne][colonne] = "-"
                        else:
                            print(
                                "Déplacement de la pièce impossible veuillez faire autre chose")

                    if boardCoord[ligne][colonne] == "♟︎":
                        print("vous avez séléctionné  le pion blanc ")
                        if pionNoir(boardCoord, ligne, colonne, ligneArrive, colonneArrive):
                            boardCoord[ligneArrive][colonneArrive] = boardCoord[ligne][colonne]
                            boardCoord[ligne][colonne] = "-"
                            tour += 1
                        else:
                            print(
                                "Déplacement de la pièce impossible veuillez faire autre chose")
                print("   1  2  3  4  5  6  7  8")
                for l in range(8):  # On affiche le plateau après le coup
                    L = l+1
                    print(L, " ", end="")
                    for c in range(8):
                        print(boardCoord[l][c], " ", end="")
                    print("")
                print("   1  2  3  4  5  6  7  8")
        else:
            print("ce n'est pas votre tour")

        """roiNoir = False  # On détecte si les rois sont encore présents et on renvoie en boolean
            roiBlanc = False
            for x in range(8):
                for y in range(8):
                    if boardCoord[x][y] == "♔":
                        roiNoir = True
                    if boardCoord[x][y] == "♚":
                        roiBlanc = True"""

    if roiNoir == False:  # Si un roi a été détécté absent on cherche lequel et on affiche le vainqueur
        print("Le joueur blanc a gagné")
    else:
        print("Le joueur noir a gagné")
