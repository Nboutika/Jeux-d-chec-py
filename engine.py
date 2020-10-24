from board import *
from fonctionEngine import *

"""
Programme de fonctionnement du jeux 
Utilise le tableau a double entrée de board.py 
Utilise pieces.py pour savoir si le mouvement est possible
utilise les fonction de fonctionEngine
Se lance depuis le main.py
"""

"""
Fonction Jeux la fonction principale 
qui test diffénts conditions :
Si un roi est mangé alors partie fini 
En fonction de la pièces séléctionnés testé si :
    il y'a une piéces sinon demander nouvelle commande

    il y'a un déplacement éffectué sinon nouvelle commande

    une pièces est séléctionné est ce que le mouvement demandé est possible 
    on utilise les fonction de pieces.py pour tester si oui alors on fait 
    appel a la fonction Deplacement sinon on demande une nouvelle commande
    
"""
def Jeux() :
    roiNoir=True
    roiBlanc=True
    blanc=False
    noir=False
    nombredetour=0
    while roiNoir and roiBlanc == True :    #On fait tourner le jeux tant que les deux roix sont présent sur le plateau 
        tourjouez=False
        ligne,colonne,ligneArrive,colonneArrive = commande()

        if boardCoord[ligne][colonne] == "-" :      #On regarde si c'est une pièce ou non       
            print("il n'y a aucune pièce")
        else:
            if ligne==ligneArrive and colonne==colonneArrive:       #On regarde si il y'a un déplacement ou non 
                print("Il faut forcément faire un mouvement")
            else:
                noir,blanc = couleurJouez(ligne,colonne)    
                                                                 #On cherche qu'elle est le type de pièces séléctionné et si le déplacement est possible ou non
                if noir == True and nombredetour % 2 == 1:
                    if boardCoord[ligne][colonne]== "♟︎":
                        if pionNoir(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                            Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                            tourjouez = True
                        else:
                            print("Déplacement de la pièce impossible veuillez faire autre chose")

                    if boardCoord[ligne][colonne]== "♜":
                        if tour(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                            Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                            tourjouez = True
                        else:
                            print("Déplacement de la pièce impossible veuillez faire autre chose")

                    if boardCoord[ligne][colonne]== "♞":
                        if cavalier(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                            Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                            tourjouez = True
                        else:
                            print("Déplacement de la pièce impossible veuillez faire autre chose")

                    if boardCoord[ligne][colonne]== "♝":
                        if fou(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                            Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                            tourjouez = True
                        else:
                            print("Déplacement de la pièce impossible veuillez faire autre chose")

                    if boardCoord[ligne][colonne]== "♚":
                        if roi(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                            Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                            tourjouez = True
                        else:
                            print("Déplacement de la pièce impossible veuillez faire autre chose")

                    if boardCoord[ligne][colonne]== "♛":
                        if dame(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                            Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                            tourjouez = True
                        else:
                            print("Déplacement de la pièce impossible veuillez faire autre chose")

                else:
                    if nombredetour % 2 == 0 :
                        if boardCoord[ligne][colonne]== "♙":
                            if pionBlanc(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                                Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                                tourjouez = True
                            else:
                                print("Déplacement de la pièce impossible veuillez faire autre chose")

                        if boardCoord[ligne][colonne]== "♖":
                            if tour(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                                Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                                tourjouez = True
                            else:
                                print("Déplacement de la pièce impossible veuillez faire autre chose")

                        if boardCoord[ligne][colonne]== "♘":
                            if cavalier(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                                Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                                tourjouez = True
                            else:
                                print("Déplacement de la pièce impossible veuillez faire autre chose")

                        if boardCoord[ligne][colonne]== "♗":
                            if fou(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                                Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                                tourjouez = True
                            else:
                                print("Déplacement de la pièce impossible veuillez faire autre chose")

                        if boardCoord[ligne][colonne]== "♔":
                            if roi(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                                Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                                tourjouez = True
                            else:
                                print("Déplacement de la pièce impossible veuillez faire autre chose")

                        if boardCoord[ligne][colonne]== "♕":
                            if dame(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                                Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                                tourjouez = True
                            else:
                                print("Déplacement de la pièce impossible veuillez faire autre chose")


                if tourjouez == True :
                    nombredetour=nombredetour+1
                    print("Vous êtes au tour ",nombredetour)
                    affichageBoard()
                else:
                    print("Ce n'est pas a votre tour de jouez")

            roiBlanc,roiNoir =EchecMat()

    if roiNoir == False:                #Si un roi a été détécté absent on cherche lequel et on affiche le vainqueur
        print("Le joueur blanc a gagné")
    else:
        print("Le joueur noir a gagné")
    print("Vous avez gagné en ",nombredetour)
