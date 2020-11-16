# Premier Projet Python - ARIES Lucas / BOUTIKAR Nassim

On vous présente ici notre **premier** projet en python, ce n'est pas le plus optimisé, on a essayé d'optimiser le plus possible mais nous n'avons pas vu les classes et c'est une difficulté supplémentaire surtout pour un jeu d'échec et surtout notre premier projet en python et en programmation en général.

## Les règles :

Règles basiques des échecs, ici dans ce jeu nous avons implémenté : Le pion qui peut se déplacer d'une, ou de deux cases lorsqu'il n'a jamais été joué, ensuite nous avons également le **roque** qui est fonctionnel, la **promotion** du pion en dame automatique, le système d'**échec**, vous ne pourrez pas jouer un coup qui vous mettrais en échec, l'**échec et mat** est également implémenté.
On a le **pat** lorsque aucun mouvement n'est possible ainsi que le **pat** lorsque les deux joueurs jouent successivements 3 fois le même coup.
Les **tours** des joueurs sont bien évidemment respectés, le joueur qui a le trait est donc le seul à pouvoir jouer.
Les pièces ne sautent pas au dessus des autres pièces (sauf le cavalier) On a donc plus qu'assez de **fonctionnalités** pour jouer une bonne partie d'échec entre amis.

## Ce que nous n'avons pas eu le temps d'ajouter

Actuellement, le jeu d'échec n'a pas de système de "en passant" malheureusement, on ne peut jouer qu'à deux et non pas contre une IA , on utilise pas de classe, de plus ce projet est notre premier projet à nous deux, n'ayant encore eu aucun cours sur l'IA on ne pouvait l'implémenter dans les délais 

## Spécificités

Le jeu se joue entièrement sur **terminal** ce qui le rend très portatif

Le joueur rentre les coordonnées de son coup dans le terminal quand il lui est demandé de jouer son coup

La syntaxe est la suivante : **|colonne de la pièce ligne de la pièce| |colonne d'arriver ligne d'arriver|** le joueur doit rentrer les **coordonnées** de la pièce qu'il sélectionne colonne et ligne collée puis un espace et ensuite les nouvelles coordonnées ce qui donne 
|exemples||||
|---|---|---|---|
|a2 h4|b4 a6|h8 a1| f5 h6|


Pour faire le **roque** il faut sélectionner le **roi** en première position et la **tour** souhaitée en position d'arriver

On ne peut pas relancer de partie tant que celle-ci n'est pas fini

