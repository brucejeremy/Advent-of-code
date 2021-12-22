import re

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

curr_passport = []
valid = 0
with open('input.txt', 'r') as passports:
    for line in passports.readlines():
        if line.strip() == '':
            if len(curr_passport) == len(fields) or \
                len(curr_passport) == len(fields)-1 and 'cid' not in curr_passport:
                valid += 1
            curr_passport = []
            continue
        for part in line.split(' '):
            field = part.split(':')[0]
            curr_passport.append(field)

if len(curr_passport) == len(fields) or \
    len(curr_passport) == len(fields)-1 and 'cid' not in curr_passport:
    valid += 1

print('Part one:')
print(f'Number of valid passports: {valid}')

curr_passport = []
hair_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
valid = 0
with open('passports.txt', 'r') as passports:
    for line in passports.readlines():
        if line.strip() == '':
            if len(curr_passport) == len(fields) or \
                len(curr_passport) == len(fields)-1 and 'cid' not in curr_passport:
                valid += 1
            curr_passport = []
            continue
        parts = line.split(' ')
        for part in parts:
            field = part.split(':')[0]
            value = part.split(':')[1].strip()
            if field == 'byr':
                year = int(value)
                if year < 1920 or year > 2002:
                    break
            elif field == 'iyr':
                year = int(value)
                if year < 2010 or year > 2020:
                    break
            elif field == 'eyr':
                year = int(value)
                if year < 2020 or year > 2030:
                    break
            elif field == 'hgt':
                unit = value[-2:]
                if unit != 'cm' and unit != 'in':
                    break
                height_val = int(value[:-2])
                if unit == 'cm':
                    if height_val < 150 or height_val > 193:
                        break
                elif unit == 'in':
                    if height_val < 59 or height_val > 76:
                        break
            elif field == 'hcl':
                if not len(value) == 7 or not re.search('#[0-9a-f]{6}', value):
                    break
            elif field == 'ecl':
                if value not in hair_colors:
                    break
            elif field == 'pid':
                if not value.isnumeric() or len(value) != 9:
                    break
            elif field == 'cid':
                pass
            curr_passport.append(field)

if len(curr_passport) == len(fields) or \
    len(curr_passport) == len(fields)-1 and 'cid' not in curr_passport:
    valid += 1

print('\nPart two:')
print(f'Number of valid passports: {valid}')