import re

can_contain_gold = {}
bag_contains = {}

with open('bag_rules.txt', 'r') as rules:

    for line in rules.readlines():
        bags = [bag.replace(' bag','') for bag in re.findall(r'[a-zA-Z]+ [a-zA-Z]+ bag', line)]
        
        for bag in bags[1:]:
            bag_contains.setdefault(bags[0], list()).append(bag)
        if bags[-1] == 'no other':
            can_contain_gold[bags[0]] = 0
        elif 'shiny gold' in bags[1:]:
            can_contain_gold[bags[0]]= 1
        else:
            can_contain_gold[bags[0]]= -1

def contains_gold_bag(color):
    if can_contain_gold[color] != -1:
        return can_contain_gold[color]
    else:
        can_have_gold = 0
        for bag in bag_contains[color]:
            can_have_gold |= contains_gold_bag(bag)
    return can_have_gold

for bag, contains in bag_contains.items():
    if can_contain_gold[bag] == -1:
        can_contain_gold[bag] = contains_gold_bag(bag)

print('Part one:')
print(f'Number of bags that can contain gold bag: {sum([gold for gold in can_contain_gold.values()])}')


can_contain_gold = {}
bag_contains = {}

with open('bag_rules.txt', 'r') as rules:

    for line in rules.readlines():
        key_bag = re.search(r'[a-zA-Z]+ [a-zA-Z]+ bag', line).group(0).replace(' bag', '')
        bags = [bag.replace(' bag','') for bag in re.findall(r'[0-9a-z]+ [a-zA-Z]+ [a-zA-Z]+ bag', line)]
        
        if 'no other bags' in line:
            bag_contains.setdefault(key_bag, list()).append( (0, 'none') )
        else:
            for bag in bags:
                num, adj, color = bag.split()
                bag_contains.setdefault(key_bag, list()).append((int(num), f'{adj} {color}'))

def num_bags_contains(color):
    total = 0
    for count, bag in bag_contains[color]:
        if count == 0:
            return count
        total += count + (count * num_bags_contains(bag))
    return total

print('Part two:')
print(f'Number of bags that a gold bag contains: {num_bags_contains("shiny gold")}')
