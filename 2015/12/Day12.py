

text = ''
with open('json.txt', 'r') as json:
    text = json.readline()

stripped = text.strip().replace('[','').replace(']','').replace('{','').replace('}','').replace('"','')

def isnumber(num):
    if num.isnumeric() or num.replace('-','').isnumeric():
        return True

def get_sum_of_nums(string):
    total = 0
    for segment in string.split(','):
        if ':' in segment:
            parts = segment.split(':')
            for part in parts:
                if isnumber(part):
                    total += int(part)
        else:
            if isnumber(segment):
                total += int(segment)
    return total

num_sum = get_sum_of_nums(stripped)
print('Part one:')
print(f'Sum = {num_sum}')

import re

def get_valid_nums(text):
    start_idx = idx = 0
    non_nested = ''
    valid = 0
    while idx < len(text):
        if '{' not in text and 'red' in text:
            return 0
        i = idx
        if text[idx] == '{':
            non_nested += text[start_idx:idx]
            i = idx
            parens = ['{']
            while len(parens) > 0:
                i += 1
                if text[i] != '}':
                    parens.pop()
                elif text[i] != '{':
                    parens.append('{')
            valid += get_valid_nums(text[idx+1:i])
            idx = i
            start_idx = i+1
        idx += 1
    non_nested += text[start_idx:]
    if 'red' in non_nested: return valid
    valid += get_sum_of_nums(non_nested.strip().replace('[','').replace(']','').replace('{','').replace('}','').replace('"',''))
    return valid

print('\nPart two:')
print(f'Sum (minus red objects) = {get_valid_nums(text)}')


