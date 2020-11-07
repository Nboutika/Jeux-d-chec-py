from ressources.board import affichageBoard, boardCoord
from ressources.fonctionEngine import commande, roiPresent, couleurJouez, Deplacement, pionConvertir, egalite, roque, coupJouer
from pieces.tour import tour
from pieces.fou import fou
from pieces.roi import roi
from pieces.cavalier import cavalier
from pieces.dame import dame
from pieces.pion import pion
from ressources.echec import Echec, coordRoi, coupPossible
from ressources.egalite import egalite
from ressources.coupEchec import coupEchec
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
    egaliteMouvements = True
    noir = False
    coupJouerTripleNoir=False
    nombredetour = 0
    ntGauche = False
    ntDroite = False
    btGauche = False
    btDroite = False
    roiBlancJouer = False
    roiNoirJouer = False
    print("Pour jouer utiliser |colonne de la pièce ligne de la pièce|     |colonne d'arrivé ligne d'arrivé|")

    while roiNoir and roiBlanc and egaliteMouvements == True:
        tourjouez = False
        ligne, colonne, ligneArrive, colonneArrive = commande()
        pieceJouer=boardCoord[ligne][colonne]

        if boardCoord[ligne][colonne] == "-":
            print("la position donnée ne contient aucune pièce")
        else:
            if ligne == ligneArrive and colonne == colonneArrive:
                print(
                    "la position de départ ne peut pas être la même que celle d'arrivée")
            else:
                noir, blanc = couleurJouez(ligne, colonne)

                if noir == True and nombredetour % 2 == 1:
                    if Echec("n"):  
                        if coupEchec(ligne, colonne, ligneArrive, colonneArrive, "n"):
                            if boardCoord[ligne][colonne] == "♟︎":
                                if [ligneArrive, colonneArrive] in pion(boardCoord, ligne, colonne, "n") :
                                    coupJouerTripleNoir, tourjouez = coupJouer(ligne, colonne, ligneArrive, colonneArrive, pieceJouer)
                                else:
                                    print(
                                        "Le pion noir  ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                            if boardCoord[ligne][colonne] == "♜":
                                if [ligneArrive, colonneArrive] in tour(boardCoord, ligne, colonne, "n"):
                                    coupJouerTripleNoir, tourjouez = coupJouer(ligne, colonne, ligneArrive, colonneArrive, pieceJouer)
                                else:
                                    print(
                                        "La tour ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                            if boardCoord[ligne][colonne] == "♞":
                                if [ligneArrive, colonneArrive] in cavalier(boardCoord, ligne, colonne, "n"):
                                    coupJouerTripleNoir, tourjouez = coupJouer(ligne, colonne, ligneArrive, colonneArrive, pieceJouer)
                                else:
                                    print(
                                        "Le cavalier ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                            if boardCoord[ligne][colonne] == "♝":
                                if [ligneArrive, colonneArrive] in fou(boardCoord, ligne, colonne, "n"):
                                    coupJouerTripleNoir, tourjouez = coupJouer(ligne, colonne, ligneArrive, colonneArrive, pieceJouer)
                                else:
                                    print(
                                        "Le fou ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                            if boardCoord[ligne][colonne] == "♚":
                                if boardCoord[ligneArrive][colonneArrive] =="♜" and roiNoirJouer == False :
                                    roqueCouleur=1
                                    if roque(roqueCouleur,ligne, colonne,ligneArrive, colonneArrive) :                                                                      
                                        coupJouerTripleNoir = egalite(ligne, colonne, ligneArrive, colonneArrive, pieceJouer)
                                        tourjouez = True
                                        roiNoirJouer = True
                                else:
                                    if [ligneArrive, colonneArrive] in roi(boardCoord, ligne, colonne,  "n"):
                                        coupJouerTripleNoir, tourjouez = coupJouer(ligne, colonne, ligneArrive, colonneArrive, pieceJouer)
                                        roiNoirJouer = True
                                    else:
                                        print(
                                            "Le roi ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                            if boardCoord[ligne][colonne] == "♛":
                                if [ligneArrive, colonneArrive] in dame(boardCoord, ligne, colonne, "n"):
                                    coupJouerTripleNoir, tourjouez = coupJouer(ligne, colonne, ligneArrive, colonneArrive, pieceJouer)
                                else:
                                    print(
                                        "La reine ne peut pas se déplacer comme ça, veuillez faire un autre coup")
                        else :
                            print("Le coup doit vous faire sortir de l'échec ")
                else:
                    if blanc == True and nombredetour % 2 == 0:
                        if Echec("b"):  
                            if coupEchec(ligne, colonne, ligneArrive, colonneArrive, "b"):
                                if boardCoord[ligne][colonne] == "♙":
                                    if [ligneArrive, colonneArrive] in pion(boardCoord, ligne, colonne, "b"):
                                        coupJouerTripleBlanc, tourjouez = coupJouer(ligne, colonne, ligneArrive, colonneArrive, pieceJouer)
                                    else:
                                        print(
                                            "Le pion blanc ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                                if boardCoord[ligne][colonne] == "♖":
                                    if [ligneArrive, colonneArrive] in tour(boardCoord, ligne, colonne, "b"):
                                        coupJouerTripleBlanc, tourjouez = coupJouer(ligne, colonne, ligneArrive, colonneArrive, pieceJouer)
                                    else:
                                        print(
                                            "La tour ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                                if boardCoord[ligne][colonne] == "♘":
                                    if [ligneArrive, colonneArrive] in cavalier(boardCoord, ligne, colonne,  "b"):
                                        coupJouerTripleBlanc, tourjouez = coupJouer(ligne, colonne, ligneArrive, colonneArrive, pieceJouer)
                                    else:
                                        print(
                                            "Le cavalier ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                                if boardCoord[ligne][colonne] == "♗":
                                    if [ligneArrive, colonneArrive] in fou(boardCoord, ligne, colonne,  "b"):
                                        coupJouerTripleBlanc, tourjouez = coupJouer(ligne, colonne, ligneArrive, colonneArrive, pieceJouer)
                                    else:
                                        print(
                                            "Le fou ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                                if boardCoord[ligne][colonne] == "♔":
                                    if boardCoord[ligneArrive][colonneArrive] =="♖" and roiBlancJouer == False:
                                        roqueCouleur=0
                                        if roque(roqueCouleur,ligne, colonne,ligneArrive, colonneArrive) :                                                                      
                                            coupJouerTripleBlanc = egalite(ligne, colonne, ligneArrive, colonneArrive, pieceJouer)
                                            tourjouez = True
                                            roiBlancJouer = True
                                    else :
                                        if [ligneArrive, colonneArrive] in roi(boardCoord, ligne, colonne,  "b"):
                                            coupJouerTripleBlanc, tourjouez = coupJouer(ligne, colonne, ligneArrive, colonneArrive, pieceJouer)
                                            roiBlancJouer = True
                                        else:
                                            print(
                                                "Le roi ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                                if boardCoord[ligne][colonne] == "♕":
                                    if [ligneArrive, colonneArrive] in dame(boardCoord, ligne, colonne, "b"):
                                        coupJouerTripleBlanc, tourjouez = coupJouer(ligne, colonne, ligneArrive, colonneArrive, pieceJouer)
                                    else:
                                        print("La reine ne peut pas se déplacer comme ça, veuillez faire un autre coup")
                            else : 
                                print("Le coup doit vous faire sortir de l'échec")

                if tourjouez == True:
                    nombredetour = nombredetour+1
                    print("Vous êtes au tour ", nombredetour)
                    pionConvertir()
                    affichageBoard()
                    if coupJouerTripleBlanc and coupJouerTripleNoir == True : 
                        egaliteMouvements =False
                    if ligne == 7:
                        if colonne == 0:
                            btGauche = True
                        if colonne == 7:
                            btDroite = True
                    if ligne == 0: 
                        if colonne == 0:
                            ntGauche = True
                        if colonne == 7:
                            ntDroite = True 
                    
                else:
                    if nombredetour % 2 == 1:
                        print("C'est au noir de jouer ")
                    else:
                        print("C'est au blanc de jouer")

            roiBlanc, roiNoir = roiPresent()

    if egaliteMouvements == False:
        print("La partie se finit sur égalité, car vous avez répété 3fois les mêmes déplacements")
    else:
        if roiNoir == False:
            print("Le joueur blanc a gagné")
        else:
            print("Le joueur noir a gagné")
        print("Vous avez gagné en ", nombredetour, " tours")
