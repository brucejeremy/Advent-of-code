import os
import sys
sys.path.append( os.path.join( os.getcwd(), '..', '..') )
from speed import timer_func
###################################################################

priorities = {}
for i,num in enumerate(range(26)):
    priorities[chr(97+num)] = i+1
    priorities[chr(65+num)] = i+27

@timer_func
def first_star():

    priority = 0
    with open('rucksacks.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip()
            comp1 = set(line[:len(line)//2])
            comp2 = set(line[len(line)//2:])

            incorrect = comp1.intersection( comp2 ).pop()
            priority += priorities[incorrect]
    print(f'1. Sum of priorities is {priority}')

@timer_func
def second_star():
    
    priority = 0
    with open('rucksacks.txt', 'r') as file:
        group = []
        for line in file.readlines():
            line = line.strip()
            group.append(set(line))

            if len(group) == 3: 
                badge = group[0].intersection( group[1] ).intersection( group[2] ).pop()
                priority += priorities[badge]
                group = []

    print(f'2. Sum of priorities is {priority}')
    
if __name__ == '__main__':
    first_star()
    second_star()
