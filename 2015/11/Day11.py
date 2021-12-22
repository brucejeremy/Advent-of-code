

key = 'hepxcrrq'

password = [c for c in key]

not_contain = ['i', 'o', 'l']
alphabet = [chr(num) for num in range(97, 123)]
next_letter = { }
for i, l in enumerate(alphabet):
    next_letter[l] = alphabet[(i+1)%len(alphabet)]
straights = [ ''.join(alphabet[i:i+3]) for i in range(24)]
doubles = [ l*2 for l in alphabet ]

def get_next_password(p):
    for idx in range(-1, -len(p), -1):
        p[idx] = next_letter[p[idx]]
        if p[idx] != 'a':
            return p

def get_next_valid_password(password, valids_to_find):
    next_passwords = []
    valid_found = 0
    while valid_found != valids_to_find:
        password = get_next_password(password)
        pass_str = ''.join(password)
        crit1 = sum([0 if l not in pass_str else 1 for l in not_contain])
        crit2 = sum([1 if straight in pass_str else 0 for straight in straights])
        crit3 = sum([1 if double in pass_str else 0 for double in doubles])
        # print(f'{pass_str} {crit1} {crit2} {crit3}')
        if not crit1 and crit2 and crit3 >= 2:
            next_passwords.append(pass_str)
            valid_found += 1
    return next_passwords[-1]
    
print('Part one:')
next_password = get_next_valid_password(password, 1)
print(f'Next password is {next_password}')

print('\nPart two:')
password = [c for c in next_password]
print(f'Next password is {get_next_valid_password(password, 1)}')