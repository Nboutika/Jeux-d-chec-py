from ressources.vide import vide
from ressources.boardlimit import boardlimit
from ressources.board import boardCoord, pieceBlanc, pieceNoir
from ressources.echec import Echec, toutCoupsPossibles
from ressources.echecmat import mouvementRoi
from ressources.coupEchec import fauxDeplacementEchec, fauxDeplacementEchecInverse

"""
----------------------------------------------------------------
Ici nous avons la fonction roqueRoi qui permet de vérifier si le roque est faisable ou non
La fonction renvoie True ou False 
----------------------------------------------------------------
"""

def roqueRoi(boardCoord, ligne, colonne, ligneArrive, colonneArrive, couleur):

    legalmoves = []
    if couleur == "n":  #Si la couleur est noir ca veut dire que la tour doit être ♜ pour le roque du roi noir
        color = "♜"
    else:
        color = "♖"    #Sinon ca veut dire que c'est le roi blanc et donc la tour blanche
    posRoi = [ligne, colonne]  
    deplacement = [[0, 1], [0, -1]]  #Ici déplacements possible pendant le roque 
    for possibilite in deplacement:
        i = 1
        while True: #boucle infini 
            row = posRoi[0]
            column = posRoi[1] + i * possibilite[1] 
             # On va prendre la position de départ auquel on aditionne la possibilité * i
             # On test qu'on est bien dans l'échequier que la case est vide et pas dans un coup possible de l'ennemie 
            if boardlimit(row, column) and vide(boardCoord, row, column) and not([row, column] in toutCoupsPossibles(couleur)):
                stockPiece = fauxDeplacementEchec(ligne, colonne, row, column) #Ici on fait le déplacement temporairement 
                if not(Echec(couleur)):  #On test que le roi n'est pas en echec si il ne l'est pas le coup est possible 
                    fauxDeplacementEchecInverse(
                        ligne, colonne, row, column, stockPiece) #On remet les pièces a leurs position d'origine 
                    legalmoves.append([row, column]) # et on met le coup dans les legalmoves
                    i += 1
                else:
                    fauxDeplacementEchecInverse(
                        ligne, colonne, row, column, stockPiece) #Si le coup n'est pas possible on remet les positions initiales et on break
                    break
            else:
                if boardlimit(row, column) and (boardCoord[row][column] == color):
                    legalmoves.append([row, column])  #Si ce n'est pas vide mais toujours dans le boardlimit et que la position contient la tour de la couleur 
                break                                 #legalmoves prend le coup
    return [ligneArrive, colonneArrive] in legalmoves #on renvoie si le coup est dans les coups possibles ou non (True,False)
