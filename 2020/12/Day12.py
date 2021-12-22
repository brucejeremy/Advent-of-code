

directions = []
with open('navigation.txt', 'r') as nav:
    directions = [line.strip() for line in nav.readlines()]

position = [0,0]
cardinals = [(0,1), (1,-1), (0,-1), (1,1)]
forward_cardinal = 0
forward = cardinals[forward_cardinal]
key_cardinal = { 'N':(1,1), 'E':(0,1), 'S':(1,-1), 'W':(0,-1) }
# (a,b) => a {0 = rotate, 1 = move}, b {divisor}
key_forward = { 'R': (0,90), 'L': (0,-90), 'F': (1,1) }

for direction in directions:
    key = direction[0]
    val = int(direction[1:])
    if key in key_cardinal:
        move = key_cardinal[key]
        position[move[0]] += val * move[1]
    else:
        move = key_forward[key]
        if move[0] == 0:
            forward_cardinal += val//move[1]
            forward = cardinals[forward_cardinal % 4]
        else:
            position[forward[0]] += val * forward[1]

print('Part one:')
print(f'Final position = {position}')
print(f'Manhattan distance = {sum([abs(coord) for coord in position])}')
import numpy as np

position = [0,0]
waypoint = np.matrix([10,1])
clockwise = np.matrix([[0,-1],[1,0]])
cntr_clockwise = np.matrix([[0,1],[-1,0]])
# key_cardinal = { 'N':(1,1), 'E':(0,1), 'S':(1,-1), 'W':(0,-1) }
key_forward = { 'R': (0,90,clockwise), 'L': (0,-90,cntr_clockwise), 'F': (1,None) }

for direction in directions:
    key = direction[0]
    val = int(direction[1:])
    if key in key_cardinal:
        move = key_cardinal[key]
        temp = waypoint.tolist()[0]
        temp[move[0]] += val * move[1]
        waypoint = np.matrix(temp)
    else:
        move = key_forward[key]
        if move[0] == 0:
            for _ in range(abs(val//move[1])):
                waypoint = np.matmul(waypoint, move[2])
        else:
            position[0] += val * waypoint.item(0)
            position[1] += val * waypoint.item(1)


print('\nPart two:')
print(f'Final position = {position}')
print(f'Manhattan distance = {sum([abs(coord) for coord in position])}')