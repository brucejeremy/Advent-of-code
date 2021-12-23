

crabs = []
with open('positions.txt', 'r') as positions:

    line = positions.readline()
    crabs = [ int(horiz.strip()) for horiz in line.split(',')]

min_pos = 0
min_fuel = max(crabs)**2
for num in range( min(crabs), max(crabs)+1 ):
    fuel = [ abs(pos - num) for pos in crabs ]
    total_fuel = sum(fuel)
    if total_fuel < min_fuel:
        min_fuel = total_fuel
        min_pos = num

print('Part one:')
print(f'Minimum amount of constant fuel needed is {min_fuel} to get to position {min_pos}')

min_pos = 0
min_fuel = max(crabs)**3
for num in range( min(crabs), max(crabs)+1 ):
    fuel = [ (abs(pos - num) + 1)*abs(pos - num)/2 for pos in crabs ]
    total_fuel = sum(fuel)
    if total_fuel < min_fuel:
        min_fuel = total_fuel
        min_pos = num

print('\nPart two:')
print(f'Minimum amount of increasing fuel needed is {int(min_fuel)} to get to position {min_pos}')
