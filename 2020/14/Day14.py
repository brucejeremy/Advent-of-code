
instructions = []
with open('startup.txt', 'r') as inst:
    for line in inst.readlines():
        left, right = [s.strip() for s in line.split('=')]
        if left == 'mask':
            instructions.append((0,right))
        else:
            index = left.split('[')[1].strip(']')
            instructions.append((1,int(index), int(right)))

memory = {}
mask = ''
for instruction in instructions:
    if instruction[0] == 0:
        mask = instruction[1]
    else:
        ones_mask = int(mask.replace('X','0'), 2)
        zeros_mask = int(mask.replace('X','1'), 2)
        result = instruction[2] | ones_mask
        result &= zeros_mask
        memory[instruction[1]] = result

print('Part one:')
print(f'Sum of startup values: {sum(memory.values())}')

import re

bit_width = 36
ones = (1 << bit_width) - 1
zeros = 0

memory = {}
mask = ''

for instruction in instructions:
    if instruction[0] == 0:
        mask = instruction[1]
    else:
        addr_mask = f'{instruction[1]:036b}'
        temp_mask = []
        for i, val in enumerate(mask):
            if val == '0': temp_mask.append(addr_mask[i])
            elif val == '1': temp_mask.append('1')
            else: temp_mask.append('X')

        indexes = [f.start() for f in re.finditer('X', mask)]
        temp_mask = int(''.join(temp_mask).replace('X','0'), 2)
        for num in range(1 << len(indexes)):
            val = str('{:0{length}b}'.format(num, length=len(indexes)))
            ones_mask = zeros
            zeros_mask = ones
            for idx, bit in enumerate(val):
                if bit == '1':
                    ones_mask |= (1 << (bit_width - indexes[idx] - 1) )
                else:
                    zeros_mask &= ~(1 << (bit_width - indexes[idx] - 1) )
            mem_idx = (temp_mask | ones_mask) & zeros_mask
            memory[mem_idx] = instruction[2]

print('\nPart two:')
print(f'Sum of startup values: {sum(memory.values())}')