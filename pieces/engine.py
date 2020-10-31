from board import *
from fonctionEngine import *
from tour import tour
from fou import fou
from roi import roi
from cavalier import cavalier
from dame import dame
from pion import pion
from vide import vide
from boardlimit import boardlimit

"""
----------------------------------------------------------------
Trame du jeu, définit le rythme de la partie  il contient :
-La fonction Jeu qui test : 
    tant que  les deux rois sont présents :
        Une fois la fonction commande appelée test :
        si la pièce sélectionnée est un "-" :
            on dit pourquoi ça n'a pas fonctionné
        sinon 
            si les coordonnées de départ sont les mêmes que celles d'arriver :
                on dit pourquoi ça n'a pas fonctionné
            sinon
                on appelle la fonction couleurJouez pour savoir de quelle couleur est la pièce
                si elle est noire et que c'est le tour au noir de jouer :
                    on cherche à quoi elle correspond chez les pièces noires 
                        si la fonction qui test si le coup est possible est vrai :
                            on fait appel à la fonction deplacement 
                            et on dit que le tour a été joué
                sinon si c'est au tour des blancs de jouer : 
                    on fait pareil que pour les pièces noires, mais avec les blanches 
                
                si le tour a été joué  
                    on incrémente le nombre de tour 
                    et avec afficheBoard on affiche le nouveau plateau 
                sinon
                    on dit que ce n'est pas au tour de la couleur jouer 
            on test avec la fonction EchecMat si les deux rois sont présents ou non 
    une fois qu'un des deux rois n'est plus sur le plateau on cherche lequel et on dit notre vainqueur
----------------------------------------------------------------
"""


def Jeux():
    roiNoir = True
    roiBlanc = True
    blanc = False
    noir = False
    nombredetour = 0
    while roiNoir and roiBlanc == True:
        tourjouez = False
        ligne, colonne, ligneArrive, colonneArrive = commande()

        if boardCoord[ligne][colonne] == "-":
            print("la position donnée ne contient aucune pièce")
        else:
            if ligne == ligneArrive and colonne == colonneArrive:
                print(
                    "la position de départ ne peut pas être la même que celle d'arrivée")
            else:
                noir, blanc = couleurJouez(ligne, colonne)

                if noir == True and nombredetour % 2 == 1:
                    if boardCoord[ligne][colonne] == "♟︎":
                        if pion(boardCoord, ligne, colonne, ligneArrive, colonneArrive, "n"):
                            Deplacement(ligne, colonne,
                                        ligneArrive, colonneArrive)
                            tourjouez = True
                        else:
                            print(
                                "Le pion noir  ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                    if boardCoord[ligne][colonne] == "♜":
                        if tour(boardCoord, ligne, colonne, ligneArrive, colonneArrive, "n"):
                            Deplacement(ligne, colonne,
                                        ligneArrive, colonneArrive)
                            tourjouez = True
                        else:
                            print(
                                "La tour ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                    if boardCoord[ligne][colonne] == "♞":
                        if cavalier(boardCoord, ligne, colonne, ligneArrive, colonneArrive, "n"):
                            Deplacement(ligne, colonne,
                                        ligneArrive, colonneArrive)
                            tourjouez = True
                        else:
                            print(
                                "Le cavalier ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                    if boardCoord[ligne][colonne] == "♝":
                        if fou(boardCoord, ligne, colonne, ligneArrive, colonneArrive, "n"):
                            Deplacement(ligne, colonne,
                                        ligneArrive, colonneArrive)
                            tourjouez = True
                        else:
                            print(
                                "Le fou ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                    if boardCoord[ligne][colonne] == "♚":
                        if roi(boardCoord, ligne, colonne, ligneArrive, colonneArrive, "n"):
                            Deplacement(ligne, colonne,
                                        ligneArrive, colonneArrive)
                            tourjouez = True
                        else:
                            print(
                                "Le roi ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                    if boardCoord[ligne][colonne] == "♛":
                        if dame(boardCoord, ligne, colonne, ligneArrive, colonneArrive, "n"):
                            Deplacement(ligne, colonne,
                                        ligneArrive, colonneArrive)
                            tourjouez = True
                        else:
                            print(
                                "La reine ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                else:
                    if nombredetour % 2 == 0:
                        if boardCoord[ligne][colonne] == "♙":
                            if pion(boardCoord, ligne, colonne, ligneArrive, colonneArrive, "b"):
                                Deplacement(ligne, colonne,
                                            ligneArrive, colonneArrive)
                                tourjouez = True
                            else:
                                print(
                                    "Le pion blanc ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                        if boardCoord[ligne][colonne] == "♖":
                            if tour(boardCoord, ligne, colonne, ligneArrive, colonneArrive, "b"):
                                Deplacement(ligne, colonne,
                                            ligneArrive, colonneArrive)
                                tourjouez = True
                            else:
                                print(
                                    "La tour ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                        if boardCoord[ligne][colonne] == "♘":
                            if cavalier(boardCoord, ligne, colonne, ligneArrive, colonneArrive, "b"):
                                Deplacement(ligne, colonne,
                                            ligneArrive, colonneArrive)
                                tourjouez = True
                            else:
                                print(
                                    "Le cavalier ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                        if boardCoord[ligne][colonne] == "♗":
                            if fou(boardCoord, ligne, colonne, ligneArrive, colonneArrive, "b"):
                                Deplacement(ligne, colonne,
                                            ligneArrive, colonneArrive)
                                tourjouez = True
                            else:
                                print(
                                    "Le fou ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                        if boardCoord[ligne][colonne] == "♔":
                            if roi(boardCoord, ligne, colonne, ligneArrive, colonneArrive, "b"):
                                Deplacement(ligne, colonne,
                                            ligneArrive, colonneArrive)
                                tourjouez = True
                            else:
                                print(
                                    "Le roi ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                        if boardCoord[ligne][colonne] == "♕":
                            if dame(boardCoord, ligne, colonne, ligneArrive, colonneArrive, "b"):
                                Deplacement(ligne, colonne,
                                            ligneArrive, colonneArrive)
                                tourjouez = True
                            else:
                                print(
                                    "La reine ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                if tourjouez == True:
                    nombredetour = nombredetour+1
                    print("Vous êtes au tour ", nombredetour)
                    affichageBoard()
                else:
                    print("C'est au tour de votre adversaire de jouer")

            roiBlanc, roiNoir = EchecMat()

    if roiNoir == False:
        print("Le joueur blanc a gagné")
    else:
        print("Le joueur noir a gagné")
    print("Vous avez gagné en ", nombredetour, " tours")
