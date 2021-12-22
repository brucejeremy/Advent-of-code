

grid = []
with open('trees.txt', 'r') as tree_map:
    for line in tree_map:
        grid.append(line.strip())

# traverse slope
lateral_pos = 3
trees_hit = 0
for idx in range(1, len(grid)):
    if grid[idx][lateral_pos] == '#':
        trees_hit += 1
    lateral_pos += 3
    lateral_pos %= len(grid[0])

print("Part one:")
print(f'Trees hit: {trees_hit}')

# different slopes
print("Part two:")
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
trees_hit = [0 for x in range(len(slopes))]
for run_num, slope in enumerate(slopes):
    lateral_pos = d_lateral = slope[0]
    d_down = slope[1]
    for idx in range(d_down, len(grid), d_down):
        if grid[idx][lateral_pos] == '#':
            trees_hit[run_num] += 1
        lateral_pos += d_lateral
        lateral_pos %= len(grid[0])

    print(f'Trees hit: {trees_hit[run_num]}')

prod = 1
for hits in trees_hit:
    prod *= hits

print(f'Product of hits: {prod}')
