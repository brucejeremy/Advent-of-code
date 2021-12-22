

sections = []
with open('tickets.txt', 'r') as tickets:
    section = []
    for line in tickets.readlines():
        if len(line.strip()) > 0:
            section.append(line.strip())
        if line == '\n':
            if len(section) > 0:
                sections.append(section)
                section = []
    sections.append(section)

# determine valid ranges
rules = {}
for rule in sections[0]:
    name,ranges = rule.split(':')
    r1,_,r2 = ranges.split()
    range1 = [int(bound) for bound in r1.split('-')]
    range2 = [int(bound) for bound in r2.split('-')]
    rules[name] = [range1, range2]

# determine valid nearby tickets
total_invalid = 0
invalid_tickets = []
for idx, ticket in enumerate(sections[2][1:]):
    ticket_valid = True
    for val in ticket.split(','):
        valid = False
        num = int(val)
        for rule in rules.values():
            if rule[0][0] <= num <= rule[0][1] or \
                rule[1][0] <= num <= rule[1][1]:
                    valid = True
                    break
        if not valid:
            total_invalid += num
            ticket_valid = False
    if not ticket_valid:
        invalid_tickets.append(idx)

print('Part one:')
print(f'Sum of invalid passes: {total_invalid}\n')

# remove invalid tickets
for invalid in invalid_tickets:
    sections[2][invalid+1] = ''

import copy

fields = {}
poss_lengths = []
for name, rule in rules.items():
    possible_field_idx = list(range(len(rules)))
    for idx, ticket in enumerate(sections[2][1:]):
        for i, val in enumerate(ticket.split(',')):
            if i not in possible_field_idx or val == '': continue

            num = int(val)
            if not (rule[0][0] <= num <= rule[0][1] or \
                rule[1][0] <= num <= rule[1][1]):
                    possible_field_idx[i] = -1
    fields[name] = [idx for idx in possible_field_idx if idx > -1]
    poss_lengths.append(len(fields[name]))

for idx in sorted(range(len(poss_lengths)), key=lambda k: poss_lengths[k]):
    taken = list(fields.values())[idx]
    for i, key in enumerate(fields.keys()):
        if idx != i:
            for num in taken:
                if num in fields[key]:
                    fields[key].remove(num)

prod = 1
departure_idxs = [v[0] for k,v in fields.items() if 'departure' in k]
print(sections[1][1:][0])
for idx, num in enumerate(sections[1][1:][0].split(',')):
    if idx in departure_idxs: prod *= int(num)

print('Part two:')
print(f'Product of departure values: {prod}')