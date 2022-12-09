import os
import sys
sys.path.append( os.path.join( os.getcwd(), '..', '..') )
from speed import timer_func
###################################################################

import numpy as np
from copy import deepcopy

forest = np.array([])
with open('trees.txt', 'r') as data:

    for line in data.readlines():
        nums = np.array([int(num) for num in line.strip()])
        forest = np.append(forest, nums)
        
dim = int( np.sqrt(len(forest)) )
forest = np.reshape( forest, (dim, dim) )

def visible_horiz( forest, from_left: bool ):
    horiz = deepcopy(forest)

    dim = len(forest)
    for row in range(1,dim-1):
        if from_left:
            for idx in range(1, dim-1):
                check = horiz[row][idx-1] if horiz[row][idx-1] > 0 else 0
                horiz[row,idx:] -= check
        else:
            for idx in range(dim-2, 0, -1):
                check = horiz[row][idx+1] if horiz[row][idx+1] > 0 else 0
                horiz[row,:idx+1] -= check

    visible_horiz = horiz > 0
    return visible_horiz

def visible_vert( forest, from_top: bool ):
    vert = deepcopy(forest)

    dim = len(forest)
    for col in range(1,dim-1):
        if from_top:
            for idx in range(1, dim-1):
                check = vert[idx-1][col] if vert[idx-1][col] > 0 else 0
                vert[idx:,col] -= check
        else:
            for idx in range(dim-2, 0, -1):
                check = vert[idx+1][col] if vert[idx+1][col] > 0 else 0
                vert[:idx+1,col] -= check

    visible_vert = vert > 0
    return visible_vert

def getVisibleTrees( forest:np.array, include_edge: bool ):

    visible = visible_horiz(forest, from_left=True)
    visible |= visible_horiz(forest, from_left=False)
    visible |= visible_vert(forest, from_top=True)
    visible |= visible_vert(forest, from_top=False)

    # Set edge visibility
    visible[0,:] = include_edge
    visible[-1,:] = include_edge
    visible[:,0] = include_edge
    visible[:,-1] = include_edge

    return visible

def getScenicScore( forest: np.array, r: int, c: int):
    height = forest[r][c]
    row = r - 1
    top = 0
    while row >= 0:
        top += 1
        if forest[row][ c ] >= height:
            break
        row -= 1
    
    row = r + 1
    bottom = 0
    while row < dim:
        bottom += 1
        if forest[row][ c ] >= height:
            break
        row += 1

    col = c - 1
    left = 0
    while col >= 0:
        left += 1
        if forest[ r ][ col ] >= height:
            break
        col -= 1
    
    col = c + 1
    right = 0
    while col < dim:
        right += 1
        if forest[ r ][ col ] >= height:
            break
        col += 1

    return top * bottom * left * right

visible_trees = None

@timer_func
def first_star():
    global visible_trees
    visible_trees = getVisibleTrees(forest, include_edge=True)
    return f'The number of visible trees is {sum(sum(visible_trees))}'

@timer_func
def second_star():

    rows, cols = np.where(visible_trees == True)

    best_score = 0
    for row, col in zip(rows, cols):
        score = getScenicScore(forest, row, col)
        if score > best_score:
            best_score = score

    return f'2. The best scenic score is {best_score}'

if __name__ == '__main__':
    first_star()
    second_star()