

groups = []
groups2 = []
with open('questionnaire.txt', 'r') as answers:
    group = ''
    group2 = []
    for line in answers.readlines():
        if line == '\n':
            groups.append(group)
            groups2.append(group2)
            group = ''
            group2 = []
            continue
        group += line.strip()
        group2.append( set([c for c in line.strip()]) )
    groups.append(group)
    groups2.append(group2)

letters = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

total = 0
for group in groups:
    total += sum([1 if x in group else 0 for x in letters])

print('Part one:')
print(f"Sum of counts: {total}")

total = 0
for group in groups2:
    overlap_set = group[0]
    for answers in group[1:]:
        overlap_set = overlap_set.intersection(answers)
    total += len(overlap_set)

print('\nPart two:')
print(f'Sum of counts: {total}')