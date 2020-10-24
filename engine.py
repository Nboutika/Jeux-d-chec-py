from board import *

"""
Programme de fonctionnement du jeux 
Utilise le tableau a double entrée de board.py 
Utilise pieces.py pour savoir si le mouvement est possible
Se lance depuis le main.py
"""

"""
Fonction commande permet de demander au joueur de jouer son coup avec la syntaxe
ligne colonne ligneArrive colonneArrive et renvoie ses variables
Détecte si les valeurs des coordonnés sont dans le tableau sinon en demande de nouvelle
"""
def commande():      
    while True:
        try:
            Valable=False               
            while Valable == False :           
                Valable=True
                print("Pour jouez utiliser |ligne de la pièce| |colonne de la pièce| |ligne d'arrivé| |colonne d'arrivé|")
                coordonnées = input("Jouez votre coup : ").split(" ")
                commandeTableau = []  
                for i in coordonnées:              
                    if i != "":
                        commandeTableau.append(int(i))
                    for i in range(len(commandeTableau)) :
                        if commandeTableau[i]<1 or commandeTableau[i]>8 :
                            Valable=False

            ligne=commandeTableau[0]-1
            colonne=commandeTableau[1]-1
            ligneArrive=commandeTableau[2]-1               
            colonneArrive=commandeTableau[3]-1

            return(ligne,colonne,ligneArrive,colonneArrive)

            break
        except ValueError:
            print("Ce n'est pas un nombre réessaye")

        except IndexError:
            print("Il faut 4 arguments")

"""
Fonction Deplacement permet de déplacer les coordonnées séléctionnés dans le tableau et met a son 
ancienne position le caractére vide "-"
"""
def Deplacement(ligne,colonne,ligneArrive,colonneArrive) :
    boardCoord[ligneArrive][colonneArrive]=boardCoord[ligne][colonne]
    boardCoord[ligne][colonne]="-"



def EchecMat():
    roiNoir=False               #On détecte si les rois sont encore présents et on renvoie en boolean 
    roiBlanc=False
    for x in range(8):
        for y in range(8):
            if boardCoord[x][y] == "♔":
                roiNoir=True
            if boardCoord[x][y] == "♚":
                roiBlanc=True
    return(roiBlanc,roiNoir)
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
    while roiNoir and roiBlanc == True :    #On fait tourner le jeux tant que les deux roix sont présent sur le plateau 

        ligne,colonne,ligneArrive,colonneArrive = commande()

        if boardCoord[ligne][colonne] == "-" :      #On regarde si c'est une pièce ou non       
            print("il n'y a aucune pièce")
        else:
            if ligne==ligneArrive and colonne==colonneArrive:       #On regarde si il y'a un déplacement ou non 
                print("Il faut forcément faire un mouvement")
            else:                                                     #On cherche qu'elle est le type de pièces séléctionné et si le déplacement est possible ou non
                if boardCoord[ligne][colonne]== "♜":
                    print("vous avez séléctionné la tour blanche")
                    if tour(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                    else:
                        print("Déplacement de la pièce impossible veuillez faire autre chose")


                if boardCoord[ligne][colonne]== "♞":
                    print("vous avez séléctionné  le cavalier blanc")
                    if cavalier(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                    else:
                        print("Déplacement de la pièce impossible veuillez faire autre chose")

                if boardCoord[ligne][colonne]== "♝":
                    print("vous avez séléctionné  le fou blanc")
                    if fou(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                    else:
                        print("Déplacement de la pièce impossible veuillez faire autre chose")        

                if boardCoord[ligne][colonne]== "♛":
                    print("vous avez séléctionné  la reine blanc")
                    if dame(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                    else:
                        print("Déplacement de la pièce impossible veuillez faire autre chose")

                if boardCoord[ligne][colonne]== "♚":
                    print("vous avez séléctionné  le roi blanc")
                    if roi(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                    else:
                        print("Déplacement de la pièce impossible veuillez faire autre chose")

                if boardCoord[ligne][colonne]== "♟︎":
                    print("vous avez séléctionné  le pion blanc ")
                    if pionBlanc(boardCoord,ligne,colonne,ligneArrive,colonneArrive) : #pas encore de fonction pion blanc
                        Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                    else:
                        print("Déplacement de la pièce impossible veuillez faire autre chose")

                if boardCoord[ligne][colonne]== "♖":
                    print("vous avez séléctionné  la tour noir")
                    if tour(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                    else:
                        print("Déplacement de la pièce impossible veuillez faire autre chose")

                if boardCoord[ligne][colonne]== "♘":
                    print("vous avez séléctionné  le cavalier noir")
                    if cavalier(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                    else:
                        print("Déplacement de la pièce impossible veuillez faire autre chose")

                if boardCoord[ligne][colonne]== "♗":
                    print("vous avez séléctionné  le fou noir")
                    if fou(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                    else:
                        print("Déplacement de la pièce impossible veuillez faire autre chose")

                if boardCoord[ligne][colonne]== "♕":
                    print("vous avez séléctionné  la reine noir")
                    if dame(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                    else:
                        print("Déplacement de la pièce impossible veuillez faire autre chose")

                if boardCoord[ligne][colonne]== "♔":
                    print("vous avez séléctionné  le roi noir")
                    if roi(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                    else:
                        print("Déplacement de la pièce impossible veuillez faire autre chose")

                if boardCoord[ligne][colonne]== "♙":
                    print("vous avez séléctionné  le pion noir ")
                    if pionNoir(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        Deplacement(ligne,colonne,ligneArrive,colonneArrive)
                    else:
                        print("Déplacement de la pièce impossible veuillez faire autre chose")

            affichageBoard()
            roiBlanc,roiNoir =EchecMat()

    if roiNoir == False:                #Si un roi a été détécté absent on cherche lequel et on affiche le vainqueur
        print("Le joueur blanc a gagné")
    else:
        print("Le joueur noir a gagné")

