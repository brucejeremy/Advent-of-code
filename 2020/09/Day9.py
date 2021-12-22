

num_list = []
with open('sequence.txt', 'r') as sequence:
    for line in sequence.readlines():
        num_list.append(int(line))

last_25 = {}
for idx, num in enumerate(num_list[:25]):
    last_25[num] = []
    for num2 in num_list[idx+1:25]:
        last_25[num].append(num + num2)

invalid = 0
for idx, num in enumerate(num_list[25:]):
    valid_num = False
    for sums in last_25.values():
        if num in sums:
            valid_num = True
            break
    if not valid_num:
        invalid = (idx, num)
        break
    else:
        del last_25[num_list[idx]]
        last_25[num] = []
        for n in num_list[idx+1:idx+25]:
            last_25[num].append(num+n)
            # if len(last_25[n]) > 0: last_25[n].pop(0)

print('Part one:')
print(f'First invalid number is {invalid[1]}')


invalid_num = invalid[1]
idx = len(num_list) - 1
while num_list[idx] > invalid_num:
    idx -= 1

sum_list = [num_list[idx]]
for i in range(idx, 0, -1):
    sum_list.append(num_list[i])
    if sum(sum_list) > invalid_num:
        sum_list.pop(0)
    elif sum(sum_list) == invalid_num:
        break

print('\nPart two:')
print(f'Encryption weakness: {min(sum_list) + max(sum_list)}')
