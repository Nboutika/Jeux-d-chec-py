from board import *
from pieces import * 
from engine import *

"""
Lancement du programme depuis ici 
"""
print("   1  2  3  4  5  6  7  8")
for l in range(8) :                 #Affichage du tableau initial de boardCoord 
    L=l+1
    print(L," ",end="")
    for c in range(8) :
        print(boardCoord[l][c]," ",end="")
    print("")

print("   1  2  3  4  5  6  7  8")

lancer=input("Veuillez appuyez sur entrée pour commencer")    #Attendre que entrée soit appuyez pour lancer le programme
Jeux()   

#Appel a la fonction jeux ou tout va se dérouler la bas 