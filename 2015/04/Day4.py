import hashlib

key = 'iwrupvqb'

result = '111111111111111111111111111111'
num = 0

while result[0:6] != '000000':
    check = f'{key}{num}'
    result = hashlib.md5(bytes(check, 'utf-8')).hexdigest()
    num += 1

print(num-1)