
directions = ''
with open('directions.txt', 'r') as parens:
    directions = parens.readline().strip()

floor = 0
position = 1
basement_pos = 0
for char in directions:
    if char == '(':
        floor += 1
    else:
        floor -= 1
    if not basement_pos and floor < 0:
        basement_pos = position
    position += 1
print('Part one:')
print(f'Final floor: {floor}')

print('Part two:')
print(f'Santa enters basement on position {basement_pos}')