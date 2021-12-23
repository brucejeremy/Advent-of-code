
directions = []
with open('directions.txt', 'r') as dirs:

    for line in dirs.readlines():

        dir, val = line.split(' ')
        if dir == 'forward': directions.append( (int(val), 0) )
        else:
            if dir == 'down': directions.append( (0, int(val) ) )
            else: directions.append( (0, -int(val) ) )

print('Part one:')
x = y = 0
for pair in directions:
    x += pair[0]
    y += pair[1]

print(f'The final position is ({x}, {y})')
print(f'Product is {x*y}')

print('\nPart two:')
x = y = aim = 0
for pair in directions:
    x += pair[0]
    aim += pair[1]
    if pair[1] == 0: y += aim * pair[0]
    


print(f'The final position is ({x}, {y})')
print(f'Product is {x*y}')