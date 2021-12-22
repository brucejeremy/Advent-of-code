
with open('depths.txt', 'r') as depths:

    prev = int(depths.readline())
    depth_list = [prev]
    increases = 0
    for line in depths.readlines():

        next = int(line)
        if next > prev: increases += 1
        prev = next
        depth_list.append(next)

    print(f'There are {increases} increases')

RANGE = 3
increases = 0
prev_sum = sum(depth_list[0:RANGE])
for i in range(1, len(depth_list)-2):

    next_sum = sum(depth_list[i:i+RANGE])
    if next_sum > prev_sum: increases += 1
    prev_sum = next_sum

print(f'There are {increases} increases of 3 consecutive depth sums')