
house_grid = { 0: [0]}

directions = ''
with open('house_directions.txt', 'r') as house_dir:
    directions = house_dir.readline().strip()

x = 0
y = 0
for move in directions:
    if move == 'v':
        y -= 1
    elif move == '^':
        y += 1
    elif move == '<':
        x -= 1
    elif move == '>':
        x += 1
    if x not in house_grid:
        house_grid[x] = [y]
    if y not in house_grid[x]:
        house_grid[x].append(y)

houses = 0
for key, value in house_grid.items():
    houses += len(value)

print('Part one:')
print(f'Houses visited: {houses}')

house_grid = { 0: [0]}
santa_x = 0
santa_y = 0
robo_x = 0
robo_y = 0
for idx, move in enumerate(directions):
    if idx % 2 == 0:
        x = santa_x
        y = santa_y
    else:
        x = robo_x
        y = robo_y

    if move == 'v':
        y -= 1
    elif move == '^':
        y += 1
    elif move == '<':
        x -= 1
    elif move == '>':
        x += 1
    if x not in house_grid:
        house_grid[x] = [y]
    if y not in house_grid[x]:
        house_grid[x].append(y)

    if idx % 2 == 0:
        santa_x = x
        santa_y = y
    else:
        robo_x = x
        robo_y = y

houses = 0
for key, value in house_grid.items():
    houses += len(value)
print('Part two:')
print(f'Houses visited: {houses}')