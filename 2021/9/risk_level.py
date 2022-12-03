

# Pad around the grid with 10s
grid = [[10 for _ in range(102)]]
with open('heatmap.txt', 'r') as map:
    for line in map.readlines():
        grid.append([10] + [int(num) for num in line.strip()] + [10])
grid.append( [10 for _ in range(102)] )


low_points = []
for row in range(1,len(grid)-1):
    for col in range(1, len(grid)-1):
        depth = grid[row][col]
        up = grid[row+1][col]
        down = grid[row-1][col]
        left = grid[row][col+1]
        right = grid[row][col-1]
        if depth < up and depth < down and \
            depth < left and depth < right:
                low_points.append(depth+1)

print('Part 1:')
print(f'There are {len(low_points)} low points with a risk value sum of {sum(low_points)}')


nines = 0

# Make grid where non-9s are -1 and 9s are 1
grid = []
with open('heatmap.txt', 'r') as map:
    for line in map.readlines():
        nines += sum([1 if num == '9' else 0 for num in line.strip()])
        grid.append([1] + [1 if num == '9' else -1 for num in line.strip()] + [1])
map_size = len(grid[0])
grid.append( [1 for _ in range(map_size)] )
grid.insert(0, [1 for _ in range(map_size)] )


equal_basins = {}
def determineBasin( up, down, left, right):
    if abs(up) == 1 and abs(down) == 1 \
        and abs(left) == 1 and abs(right) == 1: return -1
    if abs(up) != 1:
        if abs(left) != 1:
            if up != left:
                if up < left:
                    if up not in equal_basins: equal_basins[up] = set()
                    equal_basins[up].update(set([left]))
                else:
                    if left not in equal_basins: equal_basins[left] = set()
                    equal_basins[left].update(set([up]))
        return up
    if abs(left) != 1:
        return left

basins = [0,0]
for row in range(1,len(grid)-1):
    for col in range(1, len(grid[0])-1):
        depth = grid[row][col]
        if depth == 1: continue
        up = grid[row-1][col]
        down = grid[row+1][col]
        left = grid[row][col-1]
        right = grid[row][col+1]
        basin = determineBasin(up, down, left, right)
        if basin == -1: 
            basin = len(basins)
            basins.append(0)
        basins[basin] += 1
        grid[row][col] = basin

for idx, adds in sorted(list(equal_basins.items()), reverse=True):
    print(idx, adds)
    for other_idx in adds:
        basins[idx] += basins[other_idx]

# for row in grid:
#     for col in row:
#         print(f'{col:4}', end='')
#     print()

print('\nPart 2:')
basins.sort(reverse=True)
product = basins[0] * basins[1] * basins[2]
print(f'The 3 largest basins are : {basins[:3]} whose product is {product}')