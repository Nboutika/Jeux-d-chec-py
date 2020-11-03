from ressources.board import boardCoord, pieceBlanc, pieceNoir, dictionnaireIndex
import ressources.board as boardVariable
from ressources.egalite import egalite
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
    while True:
        try:
            Valable = False
            while Valable == False:
                Valable = True
                print(
                    "Pour jouer utiliser |ligne de la pièce colonne de la pièce|     |ligne d'arrivé colonne d'arrivé|")
                coordonnées = input("Jouer votre coup : ").split(" ")

                ligne = int(coordonnées[0][0])-1
                ligneArrive = int(coordonnées[1][0])-1
                colonne = int(dictionnaireIndex[coordonnées[0][1].upper()])
                colonneArrive = int(
                    dictionnaireIndex[coordonnées[1][1].upper()])
                if (ligne < 0) or (ligne > 7) or (ligneArrive < 0) or (ligneArrive > 7):
                    Valable = False
                    print("les lignes du plateau ne vont que de 1 à 8 ")

                else:
                    return(ligne, colonne, ligneArrive, colonneArrive)

        except IndexError:
            print("Il faut quatre arguments pour jouer et séparer d'un espace les coordonnées de départ et d'arriver")
            Valable = False

        except ValueError:
            print("Voici un exemple de coup valide : 4c 6d")
            Valable = False

        except KeyError:
            print("Voici un exemple de coup valide : 1a 3a")
            Valable = False


def EchecMat():
    roiNoir = False
    roiBlanc = False
    for x in range(8):
        for y in range(8):
            if boardCoord[x][y] == "♚":
                roiNoir = True
            if boardCoord[x][y] == "♔":
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

def pionConvertir():
    for colonnePlateau in range(8):
        if boardCoord[0][colonnePlateau] == boardVariable.bp :
            boardCoord[0][colonnePlateau] = boardVariable.bd
        if boardCoord[7][colonnePlateau] == boardVariable.np :
            boardCoord[7][colonnePlateau] = boardVariable.nd


def roque(roqueCouleur,ligne, colonne,ligneArrive, colonneArrive):
    if roqueCouleur == 1:     #Roque noir
        if colonneArrive == 0:
            print("Le grand roque noir")
            boardCoord[ligneArrive][3] = boardCoord[ligneArrive][colonneArrive]
            boardCoord[ligne][2] = boardCoord[ligne][colonne]
        else:
            print("le petit roque noir")
            boardCoord[ligneArrive][5] = boardCoord[ligneArrive][colonneArrive]
            boardCoord[ligne][6] = boardCoord[ligne][colonne]
    else :                  #Roque blanc 
        if colonneArrive == 0:
            print("Le grand roque blanc")
            boardCoord[ligneArrive][3] = boardCoord[ligneArrive][colonneArrive]
            boardCoord[ligne][2] = boardCoord[ligne][colonne]
        else:
            print("le petit roque blanc")
            boardCoord[ligneArrive][5] = boardCoord[ligneArrive][colonneArrive]
            boardCoord[ligne][6] = boardCoord[ligne][colonne]

    boardCoord[ligne][colonne] = "-"
    boardCoord[ligneArrive][colonneArrive] = "-"




