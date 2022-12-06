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
    
    stream = ''
    with open('signal.txt', 'r') as data:
        stream = data.read()
    
    return [c for c in stream]

def getStartIdx( signal: list, size: int ):
    for idx in range(len(signal)-size):
        if len( set(signal[idx:idx+size]) ) == size:
            break
    return idx + size


@timer_func
def first_star():
    signal = parse_file()
    position = getStartIdx( signal, 4)
    return f'1. Start-of-packet is at index {position}'


@timer_func
def second_star():
    signal = parse_file()
    position = getStartIdx( signal, 14)
    return f'2. Start-of-message is at index {position}'

if __name__ == '__main__':
    first_star()
    second_star()