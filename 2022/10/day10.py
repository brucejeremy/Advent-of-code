import os
import sys
sys.path.append( os.path.join( os.getcwd(), '..', '..') )
from speed import timer_func
###################################################################

import numpy as np

class XRegister:

    def __init__(self, start: int=1):
        self.x = [start]
        self.crt = []
        self.width = 40

    def update_crt(self):
        x_horiz = self.x[-1] % self.width
        x_pos = len(self.crt) % self.width
        self.crt.append( '#' if abs(x_horiz - x_pos) <= 1 else '.' )

    def noop(self):
        self.update_crt()
        self.x.append( self.x[-1] )
    
    def addx(self, val: int):
        self.noop()
        self.update_crt()
        self.x.append( self.x[-1] + val )

def getInstructions() -> list:
    instrs = []
    with open('program.txt', 'r') as data:
        for line in data.readlines():
            instrs.append( line.strip().split(' '))
    return instrs

program = XRegister()

@timer_func
def first_star():
    instrs = getInstructions()

    for inst in instrs:
        if inst[0] == 'noop': program.noop()
        else: program.addx( int(inst[1]) )

    signal_strength = 0
    cycles = [20, 60, 100, 140, 180, 220]
    for cycle in cycles:
        signal_strength += cycle * program.x[cycle-1]

    return f'1. The sum of signal strength is {signal_strength}'

@timer_func
def second_star():
    
    WIDTH = 40
    for row in range(len(program.crt)//WIDTH):
        for col in range(WIDTH):
            print(program.crt[row*WIDTH + col], end='')
        print()
    return f'2. What 8 capital letters are shown?'

if __name__ == '__main__':
    first_star()
    second_star()