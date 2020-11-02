from ressources.board import *

def egalite(ligne, colonne, ligneArrive, colonneArrive, pieceJouer):
    if pieceJouer in pieceBlanc :    #correspond aux blancs
        if pieceJouer ==bp: #correspond au pion blanc 
            historiqueCavalierB.clear()
            historiqueFouB.clear()
            historiqueRoiB.clear()
            historiqueTourB.clear()
            historiqueReineB.clear()
            coupJouerTripleBlanc=False

        if pieceJouer ==bt:  #correspond a la tour blanche

            historiqueTourB.append(ligne)
            historiqueTourB.append(colonne)
            historiqueTourB.append(ligneArrive)
            historiqueTourB.append(colonneArrive)

            historiqueCavalierB.clear()
            historiqueFouB.clear()
            historiqueRoiB.clear()
            historiqueReineB.clear()
            coupJouerTripleBlanc=False

            if len(historiqueTourB)>12 :
                historiqueTourB[:4]=[]

            if len(historiqueTourB) == 12 :
                if (historiqueTourB[0]==historiqueTourB[6]==historiqueTourB[8]) and (historiqueTourB[1]==historiqueTourB[7]==historiqueTourB[9]) and (historiqueTourB[2]==historiqueTourB[4]==historiqueTourB[10]) and (historiqueTourB[3]==historiqueTourB[5]==historiqueTourB[11]):
                    coupJouerTripleBlanc=True


        if pieceJouer ==bc:  #correspond au cavalier blanc 

            historiqueCavalierB.append(ligne)
            historiqueCavalierB.append(colonne)
            historiqueCavalierB.append(ligneArrive)
            historiqueCavalierB.append(colonneArrive)

            historiqueTourB.clear()
            historiqueFouB.clear()
            historiqueRoiB.clear()
            historiqueReineB.clear()
            coupJouerTripleBlanc=False

            if len(historiqueCavalierB)>12 :
                historiqueCavalierB[:4]=[]

            if len(historiqueCavalierB) == 12 :
                if (historiqueCavalierB[0]==historiqueCavalierB[6]==historiqueCavalierB[8]) and (historiqueCavalierB[1]==historiqueCavalierB[7]==historiqueCavalierB[9]) and (historiqueCavalierB[2]==historiqueCavalierB[4]==historiqueCavalierB[10]) and (historiqueCavalierB[3]==historiqueCavalierB[5]==historiqueCavalierB[11]):
                    coupJouerTripleBlanc=True

        
        if pieceJouer ==bf:  #correspond au fou blanc 

            historiqueFouB.append(ligne)
            historiqueFouB.append(colonne)
            historiqueFouB.append(ligneArrive)
            historiqueFouB.append(colonneArrive)

            historiqueCavalierB.clear()
            historiqueTourB.clear()
            historiqueRoiB.clear()
            historiqueReineB.clear()
            coupJouerTripleBlanc=False

            if len(historiqueFouB)>12 :
                historiqueFouB[:4]=[]

            if len(historiqueFouB) == 12 :
                if (historiqueFouB[0]==historiqueFouB[6]==historiqueFouB[8]) and (historiqueFouB[1]==historiqueFouB[7]==historiqueFouB[9]) and (historiqueFouB[2]==historiqueFouB[4]==historiqueFouB[10]) and (historiqueFouB[3]==historiqueFouB[5]==historiqueFouB[11]):
                    coupJouerTripleBlanc=True


        if pieceJouer ==br:  #correspond au roi blanc 

            historiqueRoiB.append(ligne)
            historiqueRoiB.append(colonne)
            historiqueRoiB.append(ligneArrive)
            historiqueRoiB.append(colonneArrive)

            historiqueCavalierB.clear()
            historiqueFouB.clear()
            historiqueTourB.clear()
            historiqueReineB.clear()
            coupJouerTripleBlanc=False

            if len(historiqueRoiB)>12 :
                historiqueRoiB[:4]=[]

            if len(historiqueRoiB) == 12 :
                if (historiqueRoiB[0]==historiqueRoiB[6]==historiqueRoiB[8]) and (historiqueRoiB[1]==historiqueRoiB[7]==historiqueRoiB[9]) and (historiqueRoiB[2]==historiqueRoiB[4]==historiqueRoiB[10]) and (historiqueRoiB[3]==historiqueRoiB[5]==historiqueRoiB[11]):
                    coupJouerTripleBlanc=True


        if pieceJouer ==bd:  #correspond au la reine blanche

            historiqueReineB.append(ligne)
            historiqueReineB.append(colonne)
            historiqueReineB.append(ligneArrive)
            historiqueReineB.append(colonneArrive)

            historiqueCavalierB.clear()
            historiqueFouB.clear()
            historiqueRoiB.clear()
            historiqueTourB.clear()
            coupJouerTripleBlanc=False

            if len(historiqueReineB)>12 :
                historiqueReineB[:4]=[]

            if len(historiqueReineB) == 12 :
                if (historiqueReineB[0]==historiqueReineB[6]==historiqueReineB[8]) and (historiqueReineB[1]==historiqueReineB[7]==historiqueReineB[9]) and (historiqueReineB[2]==historiqueReineB[4]==historiqueReineB[10]) and (historiqueReineB[3]==historiqueReineB[5]==historiqueReineB[11]):
                    coupJouerTripleBlanc=True

        return(coupJouerTripleBlanc)

    else:
        if pieceJouer ==np: #correspond au pion bnoir
            historiqueCavalierN.clear()
            historiqueFouN.clear()
            historiqueRoiN.clear()
            historiqueTourN.clear()
            historiqueReineN.clear()
            coupJouerTripleNoir=False

        if pieceJouer ==nt:  #correspond a la tour noir

            historiqueTourN.append(ligne)
            historiqueTourN.append(colonne)
            historiqueTourN.append(ligneArrive)
            historiqueTourN.append(colonneArrive)

            historiqueCavalierN.clear()
            historiqueFouN.clear()
            historiqueRoiN.clear()
            historiqueReineN.clear()
            coupJouerTripleNoir=False

            if len(historiqueTourN)>12 :
                historiqueTourN[:4]=[]

            if len(historiqueTourN) == 12 :
                if (historiqueTourN[0]==historiqueTourN[6]==historiqueTourN[8]) and (historiqueTourN[1]==historiqueTourN[7]==historiqueTourN[9]) and (historiqueTourN[2]==historiqueTourN[4]==historiqueTourN[10]) and (historiqueTourN[3]==historiqueTourN[5]==historiqueTourN[11]):
                    coupJouerTripleNoir=True


        if pieceJouer ==nc:  #correspond au cavalier noir

            historiqueCavalierN.append(ligne)
            historiqueCavalierN.append(colonne)
            historiqueCavalierN.append(ligneArrive)
            historiqueCavalierN.append(colonneArrive)

            historiqueTourN.clear()
            historiqueFouN.clear()
            historiqueRoiN.clear()
            historiqueReineN.clear()
            coupJouerTripleNoir=False

            if len(historiqueCavalierN)>12 :
                historiqueCavalierN[:4]=[]

            if len(historiqueCavalierN) == 12 :
                if (historiqueCavalierN[0]==historiqueCavalierN[6]==historiqueCavalierN[8]) and (historiqueCavalierN[1]==historiqueCavalierN[7]==historiqueCavalierN[9]) and (historiqueCavalierN[2]==historiqueCavalierN[4]==historiqueCavalierN[10]) and (historiqueCavalierN[3]==historiqueCavalierN[5]==historiqueCavalierN[11]):
                    coupJouerTripleNoir=True


        if pieceJouer ==nf:  #correspond au fou noir

            historiqueFouN.append(ligne)
            historiqueFouN.append(colonne)
            historiqueFouN.append(ligneArrive)
            historiqueFouN.append(colonneArrive)

            historiqueCavalierN.clear()
            historiqueTourN.clear()
            historiqueRoiN.clear()
            historiqueReineN.clear()
            coupJouerTripleNoir=False

            if len(historiqueFouN)>12 :
                historiqueFouN[:4]=[]

            if len(historiqueFouN) == 12 :
                if (historiqueFouN[0]==historiqueFouN[6]==historiqueFouN[8]) and (historiqueFouN[1]==historiqueFouN[7]==historiqueFouN[9]) and (historiqueFouN[2]==historiqueFouN[4]==historiqueFouN[10]) and (historiqueFouN[3]==historiqueFouN[5]==historiqueFouN[11]):
                    coupJouerTripleNoir=True


        if pieceJouer ==nr:  #correspond au roi noir

            historiqueRoiN.append(ligne)
            historiqueRoiN.append(colonne)
            historiqueRoiN.append(ligneArrive)
            historiqueRoiN.append(colonneArrive)

            historiqueCavalierN.clear()
            historiqueFouN.clear()
            historiqueTourN.clear()
            historiqueReineN.clear()
            coupJouerTripleNoir=False

            if len(historiqueRoiN)>12 :
                historiqueRoiN[:4]=[]

            if len(historiqueRoiN) == 12 :
                if (historiqueRoiN[0]==historiqueRoiN[6]==historiqueRoiN[8]) and (historiqueRoiN[1]==historiqueRoiN[7]==historiqueRoiN[9]) and (historiqueRoiN[2]==historiqueRoiN[4]==historiqueRoiN[10]) and (historiqueRoiN[3]==historiqueRoiN[5]==historiqueRoiN[11]):
                    coupJouerTripleNoir=True


        if pieceJouer ==nd:  #correspond a la reine noir

            historiqueReineN.append(ligne)
            historiqueReineN.append(colonne)
            historiqueReineN.append(ligneArrive)
            historiqueReineN.append(colonneArrive)

            historiqueCavalierN.clear()
            historiqueFouN.clear()
            historiqueRoiN.clear()
            historiqueTourN.clear()
            coupJouerTripleNoir=False

            if len(historiqueReineN)>12 :
                historiqueReineN[:4]=[]

            if len(historiqueReineN) == 12 :
                if (historiqueReineN[0]==historiqueReineN[6]==historiqueReineN[8]) and (historiqueReineN[1]==historiqueReineN[7]==historiqueReineN[9]) and (historiqueReineN[2]==historiqueReineN[4]==historiqueReineN[10]) and (historiqueReineN[3]==historiqueReineN[5]==historiqueReineN[11]):
                    coupJouerTripleNoir=True

        return(coupJouerTripleNoir)