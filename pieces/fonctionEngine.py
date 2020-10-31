from board import *
"""
----------------------------------------------------------------
fonctionEngine.py sert à contenir les fonctions appelées par engine.py il contient:
-La fonction commande qui permet de demander le coup que le joueur veut faire
    et de vérifier s'il est conforme à la syntaxe
-La fonction Deplacement qui deplace la pièce à la case demandée
    et laisse un vide à son ancienne position
-La fonction EchecMat qui permet de détecter si le roi blanc ou noir n'est plus dans la partie
-La fonction couleurJouez qui permet de détecter la couleur de la pièce séléctionnée
----------------------------------------------------------------
"""


def commande():
    print("Pour jouer utiliser |ligne de la pièce| |colonne de la pièce| |ligne d'arrivé| |colonne d'arrivé|")
    while True:
        try:
            Valable = False
            while Valable == False:
                Valable = True
                coordonnées = input("Jouer votre coup : ").split(" ")
                commandeTableau = []
                for i in coordonnées:
                    if i != "":
                        commandeTableau.append(int(i))
                    for i in range(len(commandeTableau)):
                        if commandeTableau[i] < 1 or commandeTableau[i] > 8:
                            Valable = False

            ligne = commandeTableau[0]-1
            colonne = commandeTableau[1]-1
            ligneArrive = commandeTableau[2]-1
            colonneArrive = commandeTableau[3]-1

            return(ligne, colonne, ligneArrive, colonneArrive)

            break
        except ValueError:
            print("Votre coup ne contient pas que des chiffres")

        except IndexError:
            print("Il faut quatre arguments pour jouez ")


def EchecMat():
    roiNoir = False
    roiBlanc = False
    for x in range(8):
        for y in range(8):
            if boardCoord[x][y] == "♔":
                roiNoir = True
            if boardCoord[x][y] == "♚":
                roiBlanc = True
    return(roiBlanc, roiNoir)


def couleurJouez(ligne, colonne):
    blanc = False
    noir = False
    for i in range(6):
        if boardCoord[ligne][colonne] == pieceBlanc[i]:
            print("vous avez sélectionné", pieceBlanc[i])
            blanc = True
        else:
            if boardCoord[ligne][colonne] == pieceNoir[i]:
                print("vous avez sélectionné", pieceNoir[i])
                noir = True

    return(noir, blanc)


def Deplacement(ligne, colonne, ligneArrive, colonneArrive):
    boardCoord[ligneArrive][colonneArrive] = boardCoord[ligne][colonne]
    boardCoord[ligne][colonne] = "-"
