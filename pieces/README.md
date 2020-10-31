Toutes les pièces suivent à peu près le même paterne :

Tout d'abord on prend en paramètre :
l'échiquier
La position de départ
La position d'arrivé
la couleur

ensuite on regarde la couleur de la pièce et on stock dans une variable le tableau des couleurs adverses

Ensuite on créer une variable contenant la position de la pièce
On créer une variable contenant tous les déplacements possibles :
    ils seront stocké dans un tableau à l'intérieur d'un tableau

On va faire une boucle for pour essayer chaque possibilité pour chaque déplacement possible :
    on va  additionner la position de départ avec la possibilité(donc ligne départ + ligne dans possibilité et 
    colonne de départ + colonne dans possibilité)
        On vérifie ensuite si pour chaque possibilité on a une pièce ou non :
            si la case est dans l'échiquier et vide :
                on ajoute les coordonnées dans le tableau des possibilités
            sinon si on a une pièce :
                on va vérifier la couleur, si c'est une couleur adverse:
                    Ajout des coordonnées dans le tableau

Cas de la tour, du fou, et de la dame ou l'on multiplie:
    on fait pareil que ci-dessus, sauf que pour chaque possibilité on va :
        déclarer une variable d'incrémentation (ici "i")
        on fait une boucle infinie où :
            On essaie chaque possibilité de mouvement(position départ + i * possibilité (La multiplication est prioritaire))
                si la case est dans l'échiquier et est vide :
                    on ajoute les coordonnées dans le tableau
                    on incrémente "i"
                sinon
                    si on a une pièce de couleur adverse : 
                        on ajoute les coordonnées dans le tableau
                    on break et on met donc fin à la boucle

Ensuite après avoir fait tout ça :
on renvoie simplement si les coordonnées d'arrivés sont dans notre tableau des mouvements possibles sous forme booléen

On pourrait également renvoyer simplement les possibilités et faire le test dans l'engine directement c'est au choix


/!\ Le Cavalier et le fou sont commentés pour montrer ce qui est dis ci-dessus /!\

Autre cas spécial :
    le pion : 
        code commenté
        