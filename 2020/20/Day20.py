import re, math

pieces = {}
with open('jigsaw.txt', 'r') as tiles:
    id = 0
    piece = []
    for line in tiles.readlines():
        if 'Tile' in line:
            _,id,_ = re.split(' |:', line)
        elif len(line.strip()) == 0:
            pieces[int(id)] = piece
            piece = []
        else:
            piece.append(line.strip())
    pieces[int(id)] = piece

total_pieces = int(math.sqrt(len(pieces.keys())))

piece_sides = {}
for id,piece in pieces.items():
    left = ['1' if r[0] == '#' else '0' for r in piece]
    right = ['1' if r[-1] == '#' else '0' for r in piece]
    top = ['1' if i == '#' else '0' for i in piece[0]]
    bottom = ['1' if i == '#' else '0' for i in piece[-1]]
    rev_top = top[::-1]
    # Add reverses of lists
    
    piece_sides[id] = [top, right, bottom, left]

piece_matches = {}
for id in pieces.keys():
    piece_matches[id] = [0,0,0,0]

for id,sides in piece_sides.items():
    for i, side in enumerate(sides):
        if piece_matches[id][i] == 0: continue
        matched = False
        for id2, piece in piece_sides.items():
            if id == id2: continue
            for pos, side2 in enumerate(piece):
                print(side, side2)
                if side == side2:
                    pieces_matches[id][i] = (id2, pos)
                    pieces_matches[id2][pos] = (id, i)
                    matched = True
                    break
            if matched: break
