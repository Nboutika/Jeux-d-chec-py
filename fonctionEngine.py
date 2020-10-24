from board import *
"""
Ici engine.py appel les fonctions utiles a sont déroulement
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


def couleurJouez(ligne,colonne) :
    blanc=False
    noir=False
    for i in range(6) :
        if boardCoord[ligne][colonne]== pieceBlanc[i] :
            print("vous avez séléctionné",pieceBlanc[i])
            blanc=True
        else :
            if boardCoord[ligne][colonne]== pieceNoir[i] :
                print("vous avez séléctionné",pieceNoir[i])
                noir=True

    return(noir,blanc)