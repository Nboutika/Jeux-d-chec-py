from ressources.board import affichageBoard, boardCoord
from ressources.fonctionEngine import commande, couleurJouez, Deplacement, pionConvertir, egalite, roque, coupJouer
from pieces.tour import tour
from pieces.fou import fou
from pieces.roi import roi
from pieces.cavalier import cavalier
from pieces.dame import dame
from pieces.pion import pion
from ressources.echec import Echec, coordRoi, toutCoupsPossibles
from ressources.egalite import egalite
from ressources.coupEchec import coupEchec
from ressources.echecmat import echecmat, pat
"""
----------------------------------------------------------------
La fonction Jeux est la Trame du jeu elle définit le rythme de la partie son déroulement ect... :
Elle fait appel a de nombreuses fonctions qui permettent son bon fonctionnement et qui ensemble font un jeu d'échec fonctionnel 

----------------------------------------------------------------
"""


def Jeux():
    roiNoir = True          #On initialise toute les variables nécéssaires 
    roiBlanc = True
    roiNoirPat = True
    roiBlancPat = True
    egaliteMouvements = True
    noir = False
    coupJouerTripleNoir = False
    nombredetour = 0
    ntGauche = False
    ntDroite = False
    btGauche = False
    btDroite = False
    roiBlancJouer = False
    roiNoirJouer = False
    print("Pour jouer utiliser |colonne de la pièce ligne de la pièce|     |colonne d'arriver ligne d'arriver|") 
    #On affiche le fonctionnement des coups pour le joueurs

    while roiNoir and roiBlanc and egaliteMouvements and roiNoirPat and roiBlancPat == True: 
        #Tant que l'un des rois n'est pas echec et mat ou en pat et qu'il n'y a pas d'égalité à cause de mouvements répéter 
        tourjouez = False  #Variable très importante 
        ligne, colonne, ligneArrive, colonneArrive = commande() #On récupère le coup du joueur 
        pieceJouer = boardCoord[ligne][colonne]

        if boardCoord[ligne][colonne] == "-":  #On test qu'il y'a bien une pièce
            affichageBoard()
            print("la position donnée ne contient aucune pièce")
        else:
            if ligne == ligneArrive and colonne == colonneArrive: #Que le joueur est bien fait un mouvement 
                affichageBoard()
                print(
                    "la position de départ ne peut pas être la même que celle d'arrivée")
            else:
                noir, blanc = couleurJouez(ligne, colonne)  #On fait appel à une fonction pour savoir la couleur jouer 
                fonction = None
                if noir == True and nombredetour % 2 == 1:  #Si la pièce et noir et que le tour est au joueur noir (Le joueur noir joue au tour 1 3 5) donc on test si le tour est impair 
                    if coupEchec(ligne, colonne, ligneArrive, colonneArrive, "n"): #On test si le coup met le roi noir en echec 
                        if boardCoord[ligne][colonne] == "♟︎":  #Ce passe une phase de recherche pour trouver la pièce jouer 
                            fonction = pion                     #Si on la trouve on met une variable a la fonction de la pièce
                            affichagePiece = "Le pion noir"     #Et affichage a ce qu'elle correspond 

                        if boardCoord[ligne][colonne] == "♜":
                            fonction = tour
                            affichagePiece = "La tour noir"
                        if boardCoord[ligne][colonne] == "♞":
                            fonction = cavalier
                            affichagePiece = "Le cavalier noir"
                        if boardCoord[ligne][colonne] == "♝":
                            fonction = fou
                            affichagePiece = "Le fou noir"
                        if boardCoord[ligne][colonne] == "♛":
                            fonction = dame
                            affichagePiece = "La reine noir"

                        if boardCoord[ligne][colonne] == "♚":  #Particularité pour le roi 
                            if boardCoord[ligneArrive][colonneArrive] == "♜" and roiNoirJouer == False:  #On test si le joueur veut faire le roque et si le roiNoir n'a jamais été jouer 
                                roqueCouleur = 1 
                                if (colonneArrive == 7 and ntDroite == False) or (colonneArrive == 0 and ntGauche == False): #On test soit la colonne de gauche ou de droite si elle a été jouer ou non 
                                    if roque(roqueCouleur, ligne, colonne, ligneArrive, colonneArrive):  #On appel la fonction roque pour savoir si le roque est possible 
                                        coupJouerTripleNoir = egalite(
                                            ligne, colonne, ligneArrive, colonneArrive, pieceJouer)  #On remet les historique de la couleur a 0 (car le roque ne peut être répéter )
                                        tourjouez = True    #on dis que le roiNoir a été jouer pour ne pas pouvoir refaire un roque et tourJouez aussi
                                        roiNoirJouer = True
                                    else:
                                        print(
                                            "Le roque n'est pas possible avec ses conditions")
                                else:
                                    print(
                                        "La tour a déjà été jouée dans la partie")
                            else:
                                if [ligneArrive, colonneArrive] in roi(boardCoord, ligne, colonne,  "n"): #Si ce n'est pas le roque on test si le coup du roi est possible 
                                    coupJouerTripleNoir, tourjouez = coupJouer(
                                        ligne, colonne, ligneArrive, colonneArrive, pieceJouer)  #On ajoute son coup dans l'historique
                                    roiNoirJouer = True #on dis qu'il a été jouer 
                                else:
                                    print(
                                        "Le roi ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                        if not fonction is None:  #Si une pièce autre que le roi a été jouer 
                            if [ligneArrive, colonneArrive] in fonction(boardCoord, ligne, colonne,  "n"):  #on test si son coup est possible 
                                coupJouerTripleNoir, tourjouez = coupJouer(
                                    ligne, colonne, ligneArrive, colonneArrive, pieceJouer)     #on met met tourjouez a vrai et on met dans l'hitorique 
                            else:
                                print(
                                    affichagePiece + " ne peut se déplacer comme ça, veuillez faire un autre coup")
                    else:
                        print(
                            "Vous ne pouvez pas être en echec a la fin de votre tour ")
                else:
                    if blanc == True and nombredetour % 2 == 0:     #Pareil que pour les noir mais pour les blanc   on test si le nombre de tour est pair car les blanc joue en (0,2,4,6)
                        if coupEchec(ligne, colonne, ligneArrive, colonneArrive, "b"):

                            if boardCoord[ligne][colonne] == "♙":
                                fonction = pion
                                affichagePiece = "Le pion blanc"
                            if boardCoord[ligne][colonne] == "♖":
                                fonction = tour
                                affichagePiece = "La tour blanche"
                            if boardCoord[ligne][colonne] == "♘":
                                fonction = cavalier
                                affichagePiece = "Le cavalier blanc"
                            if boardCoord[ligne][colonne] == "♗":
                                fonction = fou
                                affichagePiece = "Le fou blanc"
                            if boardCoord[ligne][colonne] == "♕":
                                fonction = dame
                                affichagePiece = "La reine blanche"

                            if boardCoord[ligne][colonne] == "♔":
                                if boardCoord[ligneArrive][colonneArrive] == "♖" and roiBlancJouer == False:
                                    roqueCouleur = 0
                                    if (colonneArrive == 7 and btDroite == False) or (colonneArrive == 0 and btGauche == False):
                                        if roque(roqueCouleur, ligne, colonne, ligneArrive, colonneArrive):
                                            coupJouerTripleBlanc = egalite(
                                                ligne, colonne, ligneArrive, colonneArrive, pieceJouer)
                                            tourjouez = True
                                            roiBlancJouer = True
                                        else:
                                            print(
                                                "le roque n'est pas possible avec ses conditions")
                                    else:
                                        print(
                                            "La tour a déjà été jouée dans la partie")
                                else:
                                    if [ligneArrive, colonneArrive] in roi(boardCoord, ligne, colonne,  "b"):
                                        coupJouerTripleBlanc, tourjouez = coupJouer(
                                            ligne, colonne, ligneArrive, colonneArrive, pieceJouer)
                                        roiBlancJouer = True
                                    else:
                                        print(
                                            "Le roi ne peut pas se déplacer comme ça, veuillez faire un autre coup")

                            if not fonction is None:
                                if [ligneArrive, colonneArrive] in fonction(boardCoord, ligne, colonne,  "b"):
                                    coupJouerTripleBlanc, tourjouez = coupJouer(
                                        ligne, colonne, ligneArrive, colonneArrive, pieceJouer)
                                else:
                                    print(
                                        affichagePiece + " ne peut se déplacer comme ça, veuillez faire un autre coup")
                        else:
                            print(
                                "Vous ne pouvez pas être en echec a la fin de votre tour ")

                if tourjouez == True:       #On test si le tour a été jouer  il peut ne pas être car le coup était impossible invalide 
                    if Echec("n"):          #On affiche les rois en echec
                        print("Le roi noir est en échec")
                    if Echec("b"):
                        print("Le roi blanc est en échec")
                    nombredetour = nombredetour+1       #On incrémente le tour
                    print("Vous êtes au tour ", nombredetour) #On rappel le tour 
                    pionConvertir()     #On transforme tout les pion qui sont en fin d'échequier en reine si il y'en a 
                    affichageBoard()    #On affiche le nouveau plateau 
                    if coupJouerTripleBlanc and coupJouerTripleNoir == True: #on regarde si on a eu 3 position identique 
                        egaliteMouvements = False  #Si oui on casse le while tout en haut et on sort du jeux avec egaliteMouvements=False
                    if ligne == 7:   #si on arrive la c'est que le coup a été jouer on peut donc savoir la pièce jouer
                        if colonne == 0: #On peut dire si une tour a été jouer ou non  (utile pour le roque)
                            btGauche = True
                        if colonne == 7:
                            btDroite = True
                    if ligne == 0:
                        if colonne == 0:
                            ntGauche = True
                        if colonne == 7:
                            ntDroite = True

                else:           #Si le tour n'a pas été jouer on raffiche le plateau et on précise qui doit jouer 
                    affichageBoard()
                    if nombredetour % 2 == 1:
                        print("C'est au noir de jouer ")
                    else:
                        print("C'est au blanc de jouer")
            #Si l'une des 4 variables devient faux la boucle while sera cassé ce qui signifie que la partie est fini 
            if Echec("n"): #On regarde si les rois sont Echec et mat et si ils sont pas echec sont t'il en pat 
                roiNoir = not(echecmat("n"))
            else:
                if nombredetour % 2 == 1:  #On vérifie que c'est au noir de jouer 
                    roiNoirPat = not(pat("n"))

            if Echec("b"):
                roiBlanc = not(echecmat("b"))
            else:
                if nombredetour % 2 == 0: #On vérifie que c'est au blanc de jouer 
                    roiBlancPat = not(pat("b"))     

    #Une fois la boucle while cassé on recherche la raison 
    #Et on affiche le print en conséquence 
    if egaliteMouvements == False: 
        print("La partie se finit sur égalité, car vous avez répété 3fois les mêmes déplacements")
    else:
        if roiBlancPat == False:
            print("La partie se finit sur égalité car le joueur blanc est en pat.")

        elif roiNoirPat == False:
            print("La partie se finit sur égalité car le joueur noir est en pat.")

        else:
            if roiNoir == False:
                print("Le joueur blanc a gagné")
            else:
                print("Le joueur noir a gagné")
            print("Vous avez gagné en ", nombredetour, " tours")
