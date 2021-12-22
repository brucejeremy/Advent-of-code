
import time

class light_direction:

    def __init__(self, string):
        self.parse_string(string)

    def parse_string(self, string):
        parts = string.strip().split('through')
        x = parts[0].strip().split(' ')
        self.direction = x[-2]
        start_coords = x[-1].strip().split(',')
        self.start_x = int(start_coords[0])
        self.start_y = int(start_coords[1])
        end_coords = parts[1].strip().split(',')
        self.end_x = int(end_coords[0])
        self.end_y = int(end_coords[1])


light_directions = []
with open('light_directions.txt', 'r') as dirs:
    for line in dirs.readlines():
        light_directions.append(light_direction(line))

print("Part one (binary):")
start = time.time()

grid = []
side = 1000
for _ in range(side):
    grid.append(0)

operations = ['off', 'on', 'toggle']
for direction in light_directions:
    width = direction.end_x - direction.start_x
    mask = ((1 << (width + 1)) - 1) << direction.start_x
    operation = operations.index(direction.direction)
    for idx in range(direction.start_y, direction.end_y+1):
        if operation == 2:
            grid[idx] ^= mask
        elif operation == 1:
            grid[idx] |= mask
        else:
            grid[idx] &= ~mask
            
lights_on = 0
for row in grid:
    lights_on += str(bin(row)).count('1')
end = time.time()

print(f"Number of lights on: {lights_on}")
print(f'Runtime: {end - start}')


print("Part one:")
start = time.time()

grid = []
side = 1000
for _ in range(side):
    grid.append([])
    for _ in range(side):
        grid[-1].append(0)

operations = ['off', 'on', 'toggle']
for direction in light_directions:
    operation = operations.index(direction.direction)
    for i in range(direction.start_x, direction.end_x+1):
        for j in range(direction.start_y, direction.end_y+1):
            if operation == 2:
                grid[i][j] ^= 1
            else:
                grid[i][j] = operation
            
lights_on = 0
for row in grid:
    lights_on += sum(row)
end = time.time()

print(f"Number of lights on: {lights_on}")
print(f'Runtime: {end - start}')



# print("\nPart two:")
# start = time.time()

# grid = []
# side = 1000
# for _ in range(side):
#     grid.append([])
#     for _ in range(side):
#         grid[-1].append(0)

# operations = ['off', 'on', 'toggle']
# for direction in light_directions:
#     operation = operations.index(direction.direction)
#     for i in range(direction.start_x, direction.end_x+1):
#         for j in range(direction.start_y, direction.end_y+1):
#             if operation == 0:
#                 if grid[i][j] > 0:
#                     grid[i][j] -= 1
#             else:
#                 grid[i][j] += operation
            
# brightness = 0
# for row in grid:
#     brightness += sum(row)

# print(f"Brightness of lights: {brightness}")

# end = time.time()
# print(f'Runtime: {end - start}')