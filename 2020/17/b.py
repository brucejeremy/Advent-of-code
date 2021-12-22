
import itertools
from copy import deepcopy

ic = [ list(x) for x in open('config.txt').read().splitlines() ]

def spaceviewer(hyperspace): # Take a look at the current state of the system
    w_ = 0
    for w in hyperspace:
        # print(w)
        z_ = 0
        print('w='+str(w_))
        for z in w:
            # print(z)
            print('w='+str(w_)+', z='+str(z_))
            z_+=1
            [print(y) for y in z]
        w_+=1

def generate_plane(space):
    plane = space[0]
    empty = [ [ '.' for i in range(len(plane[0])) ] for j in range(len(plane)) ]
    space.insert(0, empty)
    space.append(deepcopy(empty))
    return space
space = generate_plane([ic])

def expand_space(space):
    space = generate_plane(generate_plane(space))
    space_ = deepcopy(space)
    empty = [ '.' for i in range(len(space[0][0])+4) ]
    for k in range(len(space)):
        for j in range(len(space[k])):
            space_[k][j] = ['.','.'] + space[k][j] + ['.','.']
        space_[k].insert(0,deepcopy(empty))
        space_[k].insert(0,deepcopy(empty))
        space_[k].append(deepcopy(empty))
        space_[k].append(deepcopy(empty))
        # print(empty)
        # print(len(space_[k]))
    return space_

def generate_space(z_,y_,x_):
    return [[['.' for x in range(x_)] for y in range(y_)] for z in range(z_)]

def expand_hyperspace(hyperspace):
    # hyperspace
    for w in range(len(hyperspace)):
        print()
        print(len(hyperspace[w]), len(hyperspace[w][0]), len(hyperspace[w][0][0]))
        hyperspace[w] = expand_space(hyperspace[w])
        print(len(hyperspace[w]), len(hyperspace[w][0]), len(hyperspace[w][0][0]))
    empty_space = generate_space(len(hyperspace[0]),len(hyperspace[0][0]),len(hyperspace[0][0][0]))
    hyperspace.insert(0,deepcopy(empty_space))
    hyperspace.insert(0,deepcopy(empty_space))
    hyperspace.append(deepcopy(empty_space))
    hyperspace.append(deepcopy(empty_space))
    return hyperspace

empty_space = generate_space(len(space),len(space[0]),len(space[0][0]))
hyperspace = [deepcopy(empty_space), deepcopy(empty_space), space, deepcopy(empty_space), deepcopy(empty_space)]
print(hyperspace)
spaceviewer(hyperspace)
# print(expand_space(hyperspace))
# spaceviewer(expand_hyperspace(hyperspace))

def search(i,j,k,w,space):
    c = 0
    # print('search',w,k,j,i)
    for w_ in range(w-1,w+2):
        for k_ in range(k-1,k+2):
            for j_ in range(j-1,j+2):
                for i_ in range(i-1,i+2):
                    if (w_ >= 0 and w_ < len(space) and k_ >= 0 and k_ < len(space[w_]) and j_ >= 0 and j_ < len(space[w_][k_]) and i_ >= 0 and i_ < len(space[w_][k_][j_])) and (w_ != w or k_ != k or j_ != j or i_ != i):
                        # print(w_,k_,j_,i_,"  ",len(space),len(space[w_]),len(space[w_][k_]),len(space[w_][k_][j_]))
                        # print(space[w_][k_][j_][i_])
                        if space[w_][k_][j_][i_] == '#':
                            c+=1
    return c

# print(len(space_),len(space_[0]),len(space_[0][0]))
def update_state(c, space):
    space = deepcopy(expand_hyperspace(space))
    # spaceviewer(space)
    space_ = deepcopy(space)
    change = False
    for w in range(0,len(space_)):
        for k in range(0,len(space_[0])):
            for j in range(0,len(space_[0][0])):
                for i in range(0,len(space_[0][0][0])):
                    adj = search(i,j,k,w,space)
                    if space[w][k][j][i] == '#' and adj not in [2,3]:
                        space_[w][k][j][i] = '.'
                        change = True
                    elif space[w][k][j][i] == '.' and adj == 3:
                        space_[w][k][j][i] = '#'
                        change = True
    if change == True and c < 5:
        c+=1
        # spaceviewer(space_)
        space_ = update_state(c, space_)
    return space_

hyperspace_ = update_state(0,hyperspace)

spaceviewer(hyperspace_)
print(sum([sum([ sum([ y.count('#') for y in z ]) for z in w]) for w in hyperspace_ ]))