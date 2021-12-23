

num_seq = {0: 'abcefg', 1: 'cf', 2: 'acdeg', 3: 'acdfg', 4: 'bcdf', \
    5: 'abdfg', 6: 'abdefg', 7: 'acf', 8: 'abcdefg', 9: 'abcdfg'}

num_sets = {n:set([letter for letter in s]) for n,s in num_seq.items()}

numbers = []
outputs = []
with open('signals.txt', 'r') as signals:

    for line in signals.readlines():
        nums, outs = line.split('|')
        numbers.append([ n.strip() for n in nums.strip().split(' ')])
        outputs.append([ o.strip() for o in outs.strip().split(' ')])

# 1, 4, 7, 8
target_count = 0
for out_set in outputs:
    for out in out_set:
        if len(out) == 2 or len(out) == 4 or \
            len(out) == 3 or len(out) == 7:
            target_count += 1

print('Part one:')
print(f'Number of outputs that are 1, 4, 7, or 8 = {target_count}')

def removeLetter( possible_sets: dict, letter: str):
    for set_ in possible_sets:
        possible_sets[set_] -= set(letter)
    return possible_sets


def unscrambleSignal( nums, outs ):
    all_letters = set(['a','b','c','d','e','f','g'])
    possibilities = {l:all_letters for l in all_letters}
    counts = {l:0 for l in all_letters}
    lengths = [ [] for i in range(8)]
    for num in nums:
        for l in counts.keys():
            if l in num: counts[l] += 1
        lengths[len(num)].append(set([letter for letter in num]))

    f = e = ''
    for letter, count in counts.items():
        if count == 4:
            possibilities[letter] = set('e')
            e = letter
        elif count == 6: possibilities[letter] = set('b')
        elif count == 9: 
            possibilities[letter] = set('f')
            f = letter
        elif count == 7:
            possibilities[letter] = set(['d','g'])
        elif count == 8:
            possibilities[letter] = set(['a','c'])

    # Determine C
    c = list(lengths[2][0] - set(f))[0]
    possibilities = removeLetter( possibilities, 'c')
    possibilities[c] = set('c')

    # Determine E
    cde1 = (lengths[6][0] - lengths[6][1]).union(lengths[6][1] - lengths[6][0])
    cde2 = (lengths[6][1] - lengths[6][2]).union(lengths[6][2] - lengths[6][1])
    cde3 = (lengths[6][2] - lengths[6][0]).union(lengths[6][0] - lengths[6][2])
    d = list(cde1.union(cde2).union(cde3) - set(c) - set(e))[0]
    possibilities = removeLetter( possibilities, 'd')
    possibilities[d] = set('d')

    set_num = 0
    for out in outs:
        out_set = set()
        for letter in out:
            out_set.update(possibilities[letter])
        for num, set_ in num_sets.items():
            if out_set == set_:
                set_num = set_num * 10 + num
                break
    return set_num

total = 0
for i in range(len(numbers)):
    total += unscrambleSignal( numbers[i], outputs[i])

print('\nPart two:')
print(f'The final sum is {total}')