#     a b c d e f g h
#
# 8   T C F R r F C T
# 7   p p p p p p p p
# 6   * * * * * * * *
# 5   * * * * * * * *
# 4   * * * * * * * *
# 3   * * * * * * * *
# 2   p p p p p p p p
# 1   T C F r R F C T

"""
Utilisation d'unicode pour les pièces (bien vérifier si l'encodage est l'UTF-8)
Chercher une solution pour les cases vides qui est agréable au regard pour pas que l'on se perde dans l'échiquier
(éviter le caractère unicode du point central par exemple qui visiblement n'est pas adapté)
Choix des coordonnées : Tableau[ligne][colonne] /!\ Attention ici en python l'index commence à 0 et non pas à 1 ! /!\
"""


class Board():
    def __init__(self):

        self.boardContent = [
            ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
            ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ['♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎'],
            ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']]


b = Board()
print(b.boardContent)
