import os
import sys
sys.path.append( os.path.join( os.getcwd(), '..', '..') )
from speed import timer_func
###################################################################

import re

class Move:
    def __init__(self, move: str, src: str, dest: str):
        self.move = int(move)
        self.src = int(src)-1
        self.dest = int(dest)-1

def parse_file():
    instructions = []
    stacks = []
    with open('crates.txt', 'r') as data:
        for line in data.readlines():
            # Get move instructions
            if 'move' in line:
                instrs = re.match('move (\d+) from (\d+) to (\d+)', line).groups()
                instructions.append( Move(*instrs) )
            # Get initial stacks
            elif '[' in line:
                line = line.replace('    ', ' ').replace('\n','')
                # Get item for each stack in this row
                items = [ re.findall('\[([A-Z])\]', item) for item in line.split(' ')]
                if len(stacks) == 0:
                    stacks = items
                else:
                    # Append items to each stack
                    for i, stack in enumerate(stacks):
                        stack += items[i]

    # Reverse stacks to correct order
    for stack in stacks:
        stack = stack.reverse()

    return stacks, instructions

@timer_func
def first_star():
    stacks, instructions = parse_file()
    # Perform instructions
    for move in instructions:
        for _ in range(move.move):
            stacks[move.dest].append(stacks[move.src].pop())

    # Get top item in each stack
    answer = ''
    for stack in stacks:
        answer += stack[-1]

    print(f'1. All first items combined is "{answer}"')

@timer_func
def second_star():
    stacks, instructions = parse_file()
    # Perform instructions
    for move in instructions:
        stacks[move.dest] += stacks[move.src][-move.move:]
        stacks[move.src] = stacks[move.src][:-move.move]

    # Get top item in each stack
    answer = ''
    for stack in stacks:
        answer += stack[-1]

    print(f'2. All first items combined is "{answer}"')

if __name__ == '__main__':
    first_star()
    second_star()