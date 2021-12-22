

lines = ''
with open('ops.txt', 'r') as ops:
    lines = [line.strip() for line in ops.readlines()]

visited = set()
next_op = 0

acc = 0
while next_op not in visited:
    visited.add(next_op)
    instr, val = lines[next_op].split()
    if instr == 'nop':
        next_op += 1
    else:
        num = int(val.replace('+', ''))
        if instr == 'acc':
            next_op += 1
            acc += num
        else: # jmp
            next_op += num

print('Part one:')
print(f'Acc = {acc}')

stop = False
for idx, line in enumerate(lines):
    instr, val = line.split()
    if instr != 'acc': # see if terminates after last line
        old_line = f'{instr} {val}'
        if instr == 'nop':
            lines[idx] = f'jmp {val}'
        else:
            lines[idx] = f'nop {val}'

        visited.clear()
        next_op = 0
        acc = 0
        while next_op not in visited:
            visited.add(next_op)
            instr, val = lines[next_op].split()
            if instr == 'nop':
                next_op += 1
            else:
                num = int(val.replace('+', ''))
                if instr == 'acc':
                    next_op += 1
                    acc += num
                else: # jmp
                    next_op += num
            if next_op == len(lines):
                stop = True
                break

        lines[idx] = old_line
    if stop: break

print('\nPart two:')
print(f'Acc = {acc}')