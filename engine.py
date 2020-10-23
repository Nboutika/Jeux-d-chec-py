from board import *

"""
Programme de fonctionnement du jeux 
Utilise le tableau a double entrée de board.py 
Utilise pieces.py pour savoir si le mouvement est possible
"""

def Jeux() :
    roiNoir=True
    roiBlanc=True
    while roiNoir and roiBlanc == True :    #On fait tourner le jeux tant que les deux roix sont présent sur le plateau 

        Valable=False                       
        while Valable == False :            #On test si la commande est correcte sinon on en demande une nouvelle
            Valable=True
            print("Pour jouez utiliser |ligne de la pièce| |colonne de la pièce| |ligne d'arrivé| |colonne d'arrivé|")
            commande = input("Jouez votre coup : ").split(" ")
            commandeTableau = []
            for i in commande:              
                if i != "":
                    commandeTableau.append(int(i))
                for i in range(len(commandeTableau)) :
                    if commandeTableau[i]<1 or commandeTableau[i]>8 :
                        Valable=False



        ligne=commandeTableau[0]-1
        colonne=commandeTableau[1]-1
        ligneArrive=commandeTableau[2]-1                #On établit les valeurs en input dans des variables
        colonneArrive=commandeTableau[3]-1

"""
On test qu'elle est la piéce sélectionné au départ et on test si le mouvement demandé est
possible en fonction de pieces.py
"""
        if boardCoord[ligne][colonne] == "-" :
            print("il n'y a aucune pièce")
        else:
            if ligne==ligneArrive and colonne==colonneArrive:
                print("Il faut forcément faire un mouvement")
            else:
                if boardCoord[ligne][colonne]== "♜":
                    print("tour blanche")
                    if tour(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        print("mouvement possible")
                    else:
                        print("mouvement pas possible")


                if boardCoord[ligne][colonne]== "♞":
                    print("cavalier blanc")
                    if cavalier(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        print("mouvement possible")
                    else:
                        print("mouvement pas possible")

                if boardCoord[ligne][colonne]== "♝":
                    print("fou blanc")
                    if fou(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        print("mouvement possible")
                    else:
                        print("mouvement pas possible")        

                if boardCoord[ligne][colonne]== "♛":
                    print("reine blanc")
                    if dame(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        print("mouvement possible")
                    else:
                        print("mouvement pas possible")

                if boardCoord[ligne][colonne]== "♚":
                    print("roi blanc")
                    if roi(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        print("mouvement possible")
                    else:
                        print("mouvement pas possible")

                if boardCoord[ligne][colonne]== "♟︎":
                    print("pion blanc ")
                    if pionNoir(boardCoord,ligne,colonne,ligneArrive,colonneArrive) : #pas encore de fonction pion blanc
                        print("mouvement possible")
                    else:
                        print("mouvement pas possible")

                if boardCoord[ligne][colonne]== "♖":
                    print("tour noir")
                    if tour(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        print("mouvement possible")
                    else:
                        print("mouvement pas possible")

                if boardCoord[ligne][colonne]== "♘":
                    print("cavalier noir")
                    if cavalier(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        print("mouvement possible")
                    else:
                        print("mouvement pas possible")

                if boardCoord[ligne][colonne]== "♗":
                    print("fou noir")
                    if fou(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        print("mouvement possible")
                    else:
                        print("mouvement pas possible")

                if boardCoord[ligne][colonne]== "♕":
                    print("reine noir")
                    if dame(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        print("mouvement possible")
                    else:
                        print("mouvement pas possible")

                if boardCoord[ligne][colonne]== "♔":
                    print("roi noir")
                    if roi(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        print("mouvement possible")
                    else:
                        print("mouvement pas possible")

                if boardCoord[ligne][colonne]== "♙":
                    print("pion noir ")
                    if pionNoir(boardCoord,ligne,colonne,ligneArrive,colonneArrive) :
                        print("mouvement possible")
                    else:
                        print("mouvement pas possible")



                boardCoord[ligneArrive][colonneArrive]=boardCoord[ligne][colonne]
                boardCoord[ligne][colonne]="-"

            for l in range(8) :                     #On affiche le plateau après le coup
                L=l+1
                print(L," ",end="")
                for c in range(8) :
                    print(boardCoord[l][c]," ",end="")
                print("")

            print("   1  2  3  4  5  6  7  8")

            roiNoir=False               #On détecte si les rois sont encore présents et on renvoie en boolean 
            roiBlanc=False
            for x in range(8):
                for y in range(8):
                    if boardCoord[x][y] == "♔":
                        roiNoir=True
                    if boardCoord[x][y] == "♚":
                        roiBlanc=True
        

    if roiNoir == False:                #Si un roi a été détécté absent on cherche lequel et on affiche le vainqueur
        print("Le joueur blanc a gagné")
    else:
        print("Le joueur noir a gagné")
