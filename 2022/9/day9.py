import os
import sys
sys.path.append( os.path.join( os.getcwd(), '..', '..') )
from speed import timer_func
###################################################################

import numpy as np

class Location:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

class KnotModel:

    def __init__(self, width: int, height: int, knots: int):
        self.grid = np.zeros( (width, height) )
        self.knots = knots
        self.head = None
        self.tail = []
    
    def set_start(self, x: int, y: int):
        self.grid[x][y] = 1
        self.head = Location(x,y)
        for _ in range(self.knots):
            self.tail.append( Location(x,y) )
    
    def move_tail(self):
        start = self.head
        for knot in self.tail:
            end = knot
            if start.distance(end) >= 2.0:
                x_diff = start.x - end.x
                y_diff = start.y - end.y
                # Diagonal
                if abs(x_diff) > 0 and abs(y_diff) > 0:
                    end.y += np.sign(y_diff)
                    end.x += np.sign(x_diff)
                # One direction
                elif x_diff == 0:
                    end.y += np.sign(y_diff)
                else:
                    end.x += np.sign(x_diff)
            start = knot
        self.grid[self.tail[-1].x][self.tail[-1].y] += 1

    def move_head(self, direction: str, steps: int):
        is_x = True
        step = 1
        # Right is default direction
        if direction == 'R':
            pass
        elif direction == 'L':
            step *= -1
        elif direction == 'U':
            is_x = False
        elif direction == 'D':
            is_x = False
            step *= -1

        for _ in range(steps):
            if is_x: self.head.x += step
            else: self.head.y += step
            self.move_tail()


    def get_num_visited(self):
        return np.sum( self.grid > 0 )


def getActions() -> list:
    actions = []
    with open('steps.txt', 'r') as data:
        for line in data.readlines():
            actions.append( [ int(x) if x.isnumeric() else x for x in line.strip().split(' ') ] )
    return actions

def createGrid( actions: list, knots: int) -> KnotModel:
    x = [0]
    y = [0]
    currX = currY = 0
    for action in actions:
        if action[0] == 'L': currX -= action[1]
        if action[0] == 'R': currX += action[1]
        if action[0] == 'U': currY += action[1]
        if action[0] == 'D': currY -= action[1]
        x.append(currX)
        y.append(currY)

    x_min = min(x)
    x_len = max(x) - min(x) + 1

    y_min = min(y)
    y_len = max(y) - min(y) + 1

    model = KnotModel(x_len, y_len, knots=knots)
    model.set_start(-x_min, -min(y))
    return model

@timer_func
def first_star():
    actions = getActions()
    model = createGrid(actions, knots=1)
    for action in actions:
        model.move_head( action[0], action[1] )

    return f'1. The number of positions the tail visited is {model.get_num_visited()}'

@timer_func
def second_star():
    actions = getActions()
    model = createGrid(actions, knots=9)
    for action in actions:
        model.move_head( action[0], action[1] )

    return f'2. The number of positions the tail visited is {model.get_num_visited()}'

if __name__ == '__main__':
    first_star()
    second_star()