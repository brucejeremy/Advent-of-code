import numpy as np

devices = [0]
with open('adapters.txt', 'r') as adapters:
    for line in adapters.readlines():
        devices.append(int(line))

devices.sort()
devices.append(devices[-1]+3)
diff1 = 0
diff3 = 0
for idx in range(len(devices)-1):
    diff = devices[idx+1] - devices[idx]
    if diff == 1: diff1 += 1
    elif diff == 3: diff3 += 1

print('Part one:')
print(f'Diff1 = {diff1}, Diff3 = {diff3}, Result = {diff1*diff3}')

device_links = {}
for device in devices:
    device_links[device] = [device+inc if device+inc in devices else 0 for inc in range(1,4)]

arrangements = {}

def get_arrangements(num):
    if num in arrangements.keys(): return arrangements[num]
    links = device_links[num]
    if links.count(0) == 3: return 1
    total_arr = [get_arrangements(links[i]) if links[i] != 0 else 0 for i in range(3)]
    arrangements[num] = total_arr[0] + total_arr[1] + total_arr[2]
    return arrangements[num]

print('\nPart two:')
print(f'Arrangements = {get_arrangements(0)}')