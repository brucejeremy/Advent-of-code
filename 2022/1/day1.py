
import os
import sys
sys.path.append( os.path.join( os.getcwd(), '..', '..') )
from speed import timer_func
###################################################################

def parse_file():
    elves = [0]
    with open('calories.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip()
            calories = 0 if line == '' else int(line)
            if calories:
                elves[-1] += calories
            else:
                elves.append(0)
    return elves

@timer_func
def first_star():
    
    elves = parse_file()
    print(f'The max calories is {max(elves)}')

@timer_func
def second_star():
    elves = parse_file()
    sorted = elves.sort()
    print(f'The sum of the top three calories is {sum(elves[-3:])}')

if __name__ == '__main__':
    first_star()
    second_star()
