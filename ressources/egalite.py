from ressources.board import *

"""
----------------------------------------------------------------
On a 3 fonctions qui marchent ensemble 
clearTableauB va remettre a 0 tout les historique en tableau des pièces blanche sauf celle passé en argument
clearTableauN va faire pareil mais pour les noir 

egalite et la fonction principale qui renvoie un boolean qui dis si oui ou non la couleur a fait 3 fois le même mouvements
les pions ne peuvent pas répeter leur mouvement ils n'ont donc pas d'historique ce qui permet de gagner un peu de mémoire 
on a besoin de garder que les coup de la dernière pièce jouer on peut donc effacer tout les autres tableau pour garder de la mémoire 
l'algo est le même pour toute les pièces execption au pion
----------------------------------------------------------------
"""

def clearTableauB(historiquexB):
    if historiquexB != "historiqueTourB" : historiqueTourB.clear()
    if historiquexB != "historiqueCavalierB" : historiqueCavalierB.clear()
    if historiquexB != "historiqueFouB" : historiqueFouB.clear()
    if historiquexB != "historiqueRoiB" : historiqueRoiB.clear()
    if historiquexB != "historiqueReineB" : historiqueReineB.clear()
    coupJouerTripleBlanc=False
    return(coupJouerTripleBlanc)

def clearTableauN(historiquexN):
    if historiquexN != "historiqueTourN" : historiqueTourN.clear()
    if historiquexN != "historiqueCavalierN" : historiqueCavalierN.clear()
    if historiquexN != "historiqueFouN" : historiqueFouN.clear()
    if historiquexN != "historiqueRoiN" : historiqueRoiN.clear()
    if historiquexN != "historiqueReineN" : historiqueReineN.clear()
    coupJouerTripleNoir=False
    return(coupJouerTripleNoir)

def egalite(ligne, colonne, ligneArrive, colonneArrive, pieceJouer):
    if pieceJouer in pieceBlanc :    #correspond aux blancs
        if pieceJouer ==bp: #correspond au pion blanc 

            coupJouerTripleBlanc = clearTableauB("all") #on nettoie tout les historique blanc

        if pieceJouer ==bt:  #correspond a la tour blanche

            historiqueTourB.extend([ligne, colonne, ligneArrive, colonneArrive]) #On ajoute a l'hitorique le coup fait 
            coupJouerTripleBlanc = clearTableauB("historiqueTourB") 
                #on nettoie tout les autres historique vu que la règle spécifie la même pièces on fait donc un gain de mémoire
            if len(historiqueTourB)> 24 : #Si la tour a déjà plus de 6 coup enregistrer on supprimer le plus ancien   
                historiqueTourB[:4]=[]

            if len(historiqueTourB) == 24 : #Si la tour a 6 coup on test si ils sont identique
                if (historiqueTourB[0]==historiqueTourB[6]==historiqueTourB[8]) and (historiqueTourB[1]==historiqueTourB[7]==historiqueTourB[9]) and (historiqueTourB[2]==historiqueTourB[4]==historiqueTourB[10]) and (historiqueTourB[3]==historiqueTourB[5]==historiqueTourB[11]):
                    #On a un très long if qui test si les coups correspondent et donnent 3 position identique 
                    coupJouerTripleBlanc=True
            

        if pieceJouer ==bc:  #correspond au cavalier blanc 

            historiqueCavalierB.extend([ligne, colonne, ligneArrive, colonneArrive])
            coupJouerTripleBlanc = clearTableauB("historiqueCavalierB")

            if len(historiqueCavalierB)> 24 :
                historiqueCavalierB[:4]=[]

            if len(historiqueCavalierB) == 24 :
                if (historiqueCavalierB[0]==historiqueCavalierB[6]==historiqueCavalierB[8]==historiqueCavalierB[14]==historiqueCavalierB[16]==historiqueCavalierB[22]) and (historiqueCavalierB[1]==historiqueCavalierB[7]==historiqueCavalierB[9]==historiqueCavalierB[15]==historiqueCavalierB[17]==historiqueCavalierB[23]) and (historiqueCavalierB[2]==historiqueCavalierB[4]==historiqueCavalierB[10]==historiqueCavalierB[12]==historiqueCavalierB[18]==historiqueCavalierB[20]) and (historiqueCavalierB[3]==historiqueCavalierB[5]==historiqueCavalierB[11]==historiqueCavalierB[13]==historiqueCavalierB[19]==historiqueCavalierB[21]):
                    coupJouerTripleBlanc=True

        
        if pieceJouer ==bf:  #correspond au fou blanc 

            historiqueFouB.extend([ligne, colonne, ligneArrive, colonneArrive])
            coupJouerTripleBlanc = clearTableauB("historiqueFouB")

            if len(historiqueFouB)> 24 :
                historiqueFouB[:4]=[]

            if len(historiqueFouB) == 24 :
                if (historiqueFouB[0]==historiqueFouB[6]==historiqueFouB[8]) and (historiqueFouB[1]==historiqueFouB[7]==historiqueFouB[9]) and (historiqueFouB[2]==historiqueFouB[4]==historiqueFouB[10]) and (historiqueFouB[3]==historiqueFouB[5]==historiqueFouB[11]):
                    coupJouerTripleBlanc=True


        if pieceJouer ==br:  #correspond au roi blanc 

            historiqueRoiB.extend([ligne, colonne, ligneArrive, colonneArrive])
            coupJouerTripleBlanc = clearTableauB("historiqueRoiB")

            if len(historiqueRoiB)> 24 :
                historiqueRoiB[:4]=[]

            if len(historiqueRoiB) == 24 :
                if (historiqueRoiB[0]==historiqueRoiB[6]==historiqueRoiB[8]) and (historiqueRoiB[1]==historiqueRoiB[7]==historiqueRoiB[9]) and (historiqueRoiB[2]==historiqueRoiB[4]==historiqueRoiB[10]) and (historiqueRoiB[3]==historiqueRoiB[5]==historiqueRoiB[11]):
                    coupJouerTripleBlanc=True


        if pieceJouer ==bd:  #correspond au la reine blanche

            historiqueReineB.extend([ligne, colonne, ligneArrive, colonneArrive])
            coupJouerTripleBlanc = clearTableauB("historiqueReineB")

            if len(historiqueReineB)>24 :
                historiqueReineB[:4]=[]

            if len(historiqueReineB) == 24 :
                if (historiqueReineB[0]==historiqueReineB[6]==historiqueReineB[8]) and (historiqueReineB[1]==historiqueReineB[7]==historiqueReineB[9]) and (historiqueReineB[2]==historiqueReineB[4]==historiqueReineB[10]) and (historiqueReineB[3]==historiqueReineB[5]==historiqueReineB[11]):
                    coupJouerTripleBlanc=True

        return(coupJouerTripleBlanc)

    else: #Même fonctionnement que pour les blanc mais pour la couleur noir 
        if pieceJouer ==np: #correspond au pion bnoir
            coupJouerTripleNoir = clearTableauN("all")

        if pieceJouer ==nt:  #correspond a la tour noir

            historiqueTourN.extend([ligne, colonne, ligneArrive, colonneArrive])
            coupJouerTripleNoir = clearTableauN("historiqueTourN")

            if len(historiqueTourN)> 24 :
                historiqueTourN[:4]=[]

            if len(historiqueTourN) == 24 :
                if (historiqueTourN[0]==historiqueTourN[6]==historiqueTourN[8]) and (historiqueTourN[1]==historiqueTourN[7]==historiqueTourN[9]) and (historiqueTourN[2]==historiqueTourN[4]==historiqueTourN[10]) and (historiqueTourN[3]==historiqueTourN[5]==historiqueTourN[11]):
                    coupJouerTripleNoir=True


        if pieceJouer ==nc:  #correspond au cavalier noir

            historiqueCavalierN.extend([ligne, colonne, ligneArrive, colonneArrive])
            coupJouerTripleNoir = clearTableauN("historiqueCavalierN")

            if len(historiqueCavalierN)> 24 :
                historiqueCavalierN[:4]=[]

            if len(historiqueCavalierN) == 24 :
                if (historiqueCavalierN[0]==historiqueCavalierN[6]==historiqueCavalierN[8]==historiqueCavalierN[14]==historiqueCavalierN[16]==historiqueCavalierN[22]) and (historiqueCavalierN[1]==historiqueCavalierN[7]==historiqueCavalierN[9]==historiqueCavalierN[15]==historiqueCavalierN[17]==historiqueCavalierN[23]) and (historiqueCavalierN[2]==historiqueCavalierN[4]==historiqueCavalierN[10]==historiqueCavalierN[12]==historiqueCavalierN[18]==historiqueCavalierN[20]) and (historiqueCavalierN[3]==historiqueCavalierN[5]==historiqueCavalierN[11]==historiqueCavalierN[13]==historiqueCavalierN[19]==historiqueCavalierN[21]):
                    coupJouerTripleNoir=True


        if pieceJouer ==nf:  #correspond au fou noir

            historiqueFouN.extend([ligne, colonne, ligneArrive, colonneArrive])
            coupJouerTripleNoir = clearTableauN("historiqueFouN")

            if len(historiqueFouN)> 24 :
                historiqueFouN[:4]=[]

            if len(historiqueFouN) == 24 :
                if (historiqueFouN[0]==historiqueFouN[6]==historiqueFouN[8]) and (historiqueFouN[1]==historiqueFouN[7]==historiqueFouN[9]) and (historiqueFouN[2]==historiqueFouN[4]==historiqueFouN[10]) and (historiqueFouN[3]==historiqueFouN[5]==historiqueFouN[11]):
                    coupJouerTripleNoir=True


        if pieceJouer ==nr:  #correspond au roi noir

            historiqueRoiN.extend([ligne, colonne, ligneArrive, colonneArrive])
            coupJouerTripleNoir = clearTableauN("historiqueRoiN")

            if len(historiqueRoiN)> 24 :
                historiqueRoiN[:4]=[]

            if len(historiqueRoiN) == 24 :
                if (historiqueRoiN[0]==historiqueRoiN[6]==historiqueRoiN[8]) and (historiqueRoiN[1]==historiqueRoiN[7]==historiqueRoiN[9]) and (historiqueRoiN[2]==historiqueRoiN[4]==historiqueRoiN[10]) and (historiqueRoiN[3]==historiqueRoiN[5]==historiqueRoiN[11]):
                    coupJouerTripleNoir=True


        if pieceJouer ==nd:  #correspond a la reine noir

            historiqueReineN.extend([ligne, colonne, ligneArrive, colonneArrive])
            coupJouerTripleNoir = clearTableauN("historiqueReineN")

            if len(historiqueReineN)> 24 :
                historiqueReineN[:4]=[]

            if len(historiqueReineN) == 24 :
                if (historiqueReineN[0]==historiqueReineN[6]==historiqueReineN[8]) and (historiqueReineN[1]==historiqueReineN[7]==historiqueReineN[9]) and (historiqueReineN[2]==historiqueReineN[4]==historiqueReineN[10]) and (historiqueReineN[3]==historiqueReineN[5]==historiqueReineN[11]):
                    coupJouerTripleNoir=True

        return(coupJouerTripleNoir)


