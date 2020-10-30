nt = '♜'
nc = '♞'
nf = '♝'
nr = "♚"
nd = '♛'
np = '♟︎'
bt = '♖'
bc = '♘'
bf = '♗'
br = '♔'
bd = '♕'
bp = '♙'
boardCoord = [
    [nt, nc, nf, nd, nr, nf, nc, nt],
    [np, np, np, np, np, np, np, np],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    [bp, bp, bp, bp, bp, bp, bp, bp],
    [bt, bc, bf, bd, br, bf, bc, bt],
]

print(boardCoord.index(nr))
