from copy import deepcopy

plane = []
dim = 0
with open('config.txt', 'r') as config:
    for line in config.readlines():
        row = [0 if c == '.' else 1 for c in line.strip()]
        plane.append(row)

def add_buffer(space):
    dim = len(space[0]) + 2
    blank_row = [ 0 for c in range(len(space[0][0])+2) ]

    for plane in space:
        for row in plane:
            row.insert(0,0)
            row.append(0)
        plane.insert(0, deepcopy(blank_row))
        plane.append(deepcopy(blank_row))

    plane = []
    
    for _ in range(dim):
        plane.append(deepcopy(blank_row))

    space.insert(0, deepcopy(plane))
    space.append(deepcopy(plane))
    return space

def check_neighbors(space, p, r, c, new_space):
    total = 0
    for plane in space[p-1:p+2]:
        for row in plane[r-1:r+2]:
            total += sum(row[c-1:c+2])
    total -= space[p][r][c]
    if space[p][r][c] == 0 and total == 3:
        new_space[p][r][c] = 1
    elif space[p][r][c] == 1 and total != 2 and total != 3:
        new_space[p][r][c] = 0
    return new_space

def get_total_active(space):
    total = 0
    for plane in space:
        for row in plane:
            total += sum(row)
    return total

def print_space(space):
    for plane in space:
        for row in plane:
            print(''.join([str(num) for num in row]))
        print()

dim = len(plane[0]) + 2
planes = 3
hyperspace = deepcopy([[plane]])
space = add_buffer([plane])

iters = 6

for idx in range(iters):
    space = add_buffer(space)
    new_space = deepcopy(space)
    for plane_idx in range(1,planes+1):
        for row_idx in range(1,dim+1):
            for col_idx in range(1,dim+1):
                new_space = check_neighbors(space,plane_idx,row_idx,col_idx,new_space)
    dim += 2
    planes += 2
    space = new_space

print('Part one:')
print(f'Total active = {get_total_active(space)}')

#################################################
### Part two
#################################################

def add_buffer_4d(hyperspace):
    dim = len(hyperspace[0]) + 2
    blank_row = [ 0 for c in range(len(hyperspace[0][0])+2) ]
    blank_plane = [ deepcopy(blank_row) for r in range(len(hyperspace[0][0])+2) ]

    for space in hyperspace:
        for plane in space:
            for row in plane:
                row.insert(0,0)
                row.append(0)
            plane.insert(0, deepcopy(blank_row))
            plane.append(deepcopy(blank_row))
        space.insert(0, deepcopy(blank_plane))
        space.append(deepcopy(blank_plane))
    
    space = []
    for _ in range(dim):
        space.append(deepcopy(blank_plane))

    hyperspace.insert(0, deepcopy(space))
    hyperspace.append(deepcopy(space))
    return hyperspace

def check_neighbors_4d(hyperspace, h, p, r, c, new_hyperspace):
    total = 0
    for space in hyperspace[h-1:h+2]:
        for plane in space[p-1:p+2]:
            for row in plane[r-1:r+2]:
                total += sum(row[c-1:c+2])
    total -= hyperspace[h][p][r][c]
    if hyperspace[h][p][r][c] == 0 and total == 3:
        new_hyperspace[h][p][r][c] = 1
    elif hyperspace[h][p][r][c] == 1 and total != 2 and total != 3:
        new_hyperspace[h][p][r][c] = 0
    return new_hyperspace

def get_total_active_4d(hyperspace):
    total = 0
    for space in hyperspace:
        for plane in space:
            for row in plane:
                total += sum(row)
    return total

def print_space_4d(hyperspace):
    for space in hyperspace:
        for plane in space:
            for row in plane:
                print(''.join([str(num) for num in row]))
            print()
        print('----------------')

dim = len(hyperspace[0][0][0]) + 2
planes = 3
spaces = 3

hyperspace = add_buffer_4d(hyperspace)

iters = 6

for idx in range(iters):
    hyperspace = add_buffer_4d(hyperspace)
    new_hyperspace = deepcopy(hyperspace)
    for space_idx in range(1,spaces+1):
        for plane_idx in range(1,planes+1):
            for row_idx in range(1,dim+1):
                for col_idx in range(1,dim+1):
                    new_hyperspace = check_neighbors_4d(hyperspace,space_idx,plane_idx,row_idx,col_idx,new_hyperspace)
    dim += 2
    planes += 2
    spaces += 2
    hyperspace = new_hyperspace

print('\nPart two:')
print(f'Total active = {get_total_active_4d(hyperspace)}')