import os
import sys
sys.path.append( os.path.join( os.getcwd(), '..', '..') )
from speed import timer_func
###################################################################

@timer_func
def first_star():
    overlap = 0
    with open('assignments.txt', 'r') as file:
        for line in file.readlines():
            # Split input into start and end for each assignment
            first, second = [ part.split('-') for part in line.strip().split(',') ]
            # Create assignment sets
            assign1 = set(range(int(first[0]), int(first[1])+1))
            assign2 = set(range(int(second[0]), int(second[1])+1))
            # Determine subsets
            overlap += 1 if assign1.issubset( assign2 ) or assign2.issubset( assign1 ) else 0

    print(f'1. Number of overlaps is {overlap}')

@timer_func
def second_star():
    overlap = 0
    with open('assignments.txt', 'r') as file:
        for line in file.readlines():
            # Split input into start and end for each assignment
            first, second = [ part.split('-') for part in line.strip().split(',') ]
            # Create assignment sets
            first_assignments = set(range(int(first[0]), int(first[1])+1))
            second_assignments = set(range(int(second[0]), int(second[1])+1))

            overlap += 1 if len( second_assignments.intersection( first_assignments )) > 0 else 0

    print(f'2. Total assignment overlaps is {overlap}')
    
if __name__ == '__main__':
    first_star()
    second_star()
