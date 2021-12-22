
with open('numbers.txt', 'r') as nums:
    nums = [int(x.strip()) for x in nums.readline().split(',')]


def nth_term(nums, end_turn):
    last_turn = {}
    repeats = set()
    for idx,num in enumerate(nums):
        last_turn[num] = idx+1
        if idx < len(nums)-1:
            repeats.add(num)

    last_num = nums[-1]
    for turn in range(len(nums),end_turn):
        if last_num not in repeats:
            last_turn[last_num] = turn
            repeats.add(last_num)
            last_num = 0
        else:
            temp = last_num
            last_num = turn - last_turn[last_num]
            last_turn[temp] = turn
    return last_num

print('Part one:')
print(f'2020th number: {nth_term(nums, 2020)}')

print('\nPart two:')
print(f'30,000,000th number: {nth_term(nums, 30000000)}')