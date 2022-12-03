import numpy as np

def parse_file():
    nums = []
    with open('octopus.txt', 'r') as file:
        for line in file.readlines():
            for char in line.strip():
                nums.append(int(char))
    return np.array(nums).reshape(10,10)

def print_grid(grid):
    for line in grid:
        for num in line:
            print(f'{num}', end=' ')
        print()

def step_grid(grid):
    grid += 1

grid = parse_file()
step_grid(grid)
print(grid)
