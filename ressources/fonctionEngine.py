from ressources.board import boardCoord, pieceBlanc, pieceNoir, dictionnaireIndex, affichageBoard
import ressources.board as boardVariable
from ressources.egalite import egalite
from pieces.roque import roqueRoi
"""
----------------------------------------------------------------
fonctionEngine contient une grosse partie des fonction appelé par engine se fichier sert strictement aux appels a fonction d'engine 
----------------------------------------------------------------
"""

#Une fois appelée elle renvoie les coordonnées du coup rentrer par le joueur
def commande():
    while True:
        try:        #Boucle try pour être sur d'avoir un coup valide
            Valable = False
            while Valable == False:
                Valable = True
                print("exemple de coup : b4 h6")
                coordonnées = input("Jouer votre coup : ").split(" ")  #On récupère le input du joueur qu'on casse en un tableau a chaque " "

                ligne = int(coordonnées[0][1])-1        #Ici on récupere les ligne qui son [1-8] auxquelles ont retire 1 car l'index des tabeau commence a 0 alors que l'échequier commence a 1 
                ligneArrive = int(coordonnées[1][1])-1
                colonne = int(dictionnaireIndex[coordonnées[0][0].upper()])  #ici on récuper les colonnes [A-H] on applique upper pour prendre majuscule minuscule  on sert du dictionnaire pour les convertir en index python
                colonneArrive = int(
                    dictionnaireIndex[coordonnées[1][0].upper()])
                if (ligne < 0) or (ligne > 7) or (ligneArrive < 0) or (ligneArrive > 7):  #on test que les coordonnés sont bien dans le plateau
                    affichageBoard()    #si elles ne le sont pas on affiche a nouveau le plateau 
                    Valable = False
                    print("les lignes du plateau ne vont que de 1 à 8 ") #on indique le message d'erreur pour aider l'utilisateur 

                else:
                    return(ligne, colonne, ligneArrive, colonneArrive)

        except IndexError: #Ici on récupère l'erreur qu'il n'ait pas assez d'arguments et on affiche un message explicatif de l'erreur
            affichageBoard()
            print("Il faut quatre arguments pour jouer et séparer d'un espace les coordonnées de départ et d'arriver")
            Valable = False
            affichageBoard()

        except ValueError: #Ici le joueur a mit des lettres pour les lignes 
            print("Voici un exemple de coup valide : c4 d6")
            Valable = False
            affichageBoard()

        except KeyError:    #Ici le joueur a mit des chiffres pour les colonnes 
            print("Voici un exemple de coup valide : a1 a5")
            Valable = False
            affichageBoard()


#Fonction qui permet de récupérer la couleur de la pièce sélectionnée et d'afficher la pièce
def couleurJouez(ligne, colonne):
    blanc = False
    noir = False
    for i in range(6):#On navigue sur les tableaux répertoriant toutes les pièces d'une couleur 
        if boardCoord[ligne][colonne] == pieceBlanc[i]:
            print("vous avez sélectionné", pieceBlanc[i])
            blanc = True
        else:
            if boardCoord[ligne][colonne] == pieceNoir[i]:
                print("vous avez sélectionné", pieceNoir[i])
                noir = True

    return(noir, blanc) #On renvoie True pour la couleur jouer et false pour l'autre 

#Ici on fait le déplacement demandé par le joueur
def Deplacement(ligne, colonne, ligneArrive, colonneArrive):
    boardCoord[ligneArrive][colonneArrive] = boardCoord[ligne][colonne]
    boardCoord[ligne][colonne] = "-"

#Ici on regarde si un pion a traversé le plateau si oui on le transforme en reine 
def pionConvertir():
    for colonnePlateau in range(8):
        if boardCoord[0][colonnePlateau] == boardVariable.bp:
            boardCoord[0][colonnePlateau] = boardVariable.bd
        if boardCoord[7][colonnePlateau] == boardVariable.np:
            boardCoord[7][colonnePlateau] = boardVariable.nd

#On a la fonction qui fait le roque et vérifie si il est possible 
def roque(roqueCouleur, ligne, colonne, ligneArrive, colonneArrive):
    roqueFait = False
    if roqueCouleur == 1:  # On recherche la couleur du roque  ici c'est le roque noir
        if colonneArrive == 0: #Comme les tours ne sont pas censé avoir bougé on connait leur colonne 
            if roqueRoi(boardCoord, ligne, colonne, ligneArrive, colonneArrive, "n"): #on regarde si le roque est faisaible avec la fonction roqueRoi
                boardCoord[ligneArrive][3] = boardCoord[ligneArrive][colonneArrive] #Si il est faisaible on change les pièces 
                boardCoord[ligne][2] = boardCoord[ligne][colonne]
                roqueFait = True
                print("Vous avez fait le grand roque") #On affiche le roque fait pour plus de clairté dans le jeu 
        else:
            if colonneArrive == 7:  #Même bloc qu'au dessus 
                if roqueRoi(boardCoord, ligne, colonne, ligneArrive, colonneArrive, "n"):
                    boardCoord[ligneArrive][5] = boardCoord[ligneArrive][colonneArrive]
                    boardCoord[ligne][6] = boardCoord[ligne][colonne]
                    roqueFait = True
                    print("Vous avez fait le petit roque")
    else:  # Roque blanc
        if colonneArrive == 0:
            if roqueRoi(boardCoord, ligne, colonne, ligneArrive, colonneArrive, "b"):
                boardCoord[ligneArrive][3] = boardCoord[ligneArrive][colonneArrive]
                boardCoord[ligne][2] = boardCoord[ligne][colonne]
                roqueFait = True
                print("Vous avez fait le grand roque")
        else:
            if colonneArrive == 7:
                if roqueRoi(boardCoord, ligne, colonne, ligneArrive, colonneArrive, "b"):
                    boardCoord[ligneArrive][5] = boardCoord[ligneArrive][colonneArrive]
                    boardCoord[ligne][6] = boardCoord[ligne][colonne]
                    roqueFait = True
                    print("Vous avez fait le petit roque")

    if roqueFait == True:
        boardCoord[ligne][colonne] = "-"
        boardCoord[ligneArrive][colonneArrive] = "-"
        return True
    else:
        print("Le roque n'est pas possible ")
        return False

#Ici on a la fonction qui fait le coup quand il est valable 
def coupJouer(ligne, colonne, ligneArrive, colonneArrive, pieceJouer):
    Deplacement(ligne, colonne,
                ligneArrive, colonneArrive)#On fait le déplacement 
    coupJouerTriple = egalite(
        ligne, colonne, ligneArrive, colonneArrive, pieceJouer)#On ajoute le mouvement dans l'historique
    tourjouez = True
    return(coupJouerTriple, tourjouez)#et on renvoie les boolean nécessaire au engine 
