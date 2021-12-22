
total_paper = 0
present_dims = []
with open('presents.txt', 'r') as presents:
    for line in presents.readlines():
        dims = [int(num) for num in line.strip().split('x')]
        present_dims.append(dims)
        areas = [dims[0]*dims[1], dims[0]*dims[2], dims[1]*dims[2] ]
        min_area = min(areas)
        total_paper += sum(2*areas) + min_area

print('Part one:')
print(f"Wrapping paper needed: {total_paper} sq. ft.")

total_ribbon = 0
for dim in present_dims:
    vol = dim[0] * dim[1] * dim[2]
    dim.remove(max(dim))
    total_ribbon += sum(dim)*2 + vol

print('\nPart two:')
print(f'Ribbon needed: {total_ribbon} ft.')