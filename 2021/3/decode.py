

nums = []
with open('diagnostic.txt', 'r') as codes:

    for line in codes.readlines():

        nums.append(line.strip())

zero_counts = [ 0 for _ in range(len(nums[0]))]
for code in nums:
    for i, bit in enumerate(code):
        if bit == '0': zero_counts[i] += 1

gamma = ''
for cnt in zero_counts:
    gamma += '0' if cnt > len(nums)/2 else '1'

gamma = int(gamma, 2)
epsilon = gamma ^ (2**len(zero_counts)-1)

print('Part one:')
print(f'Gamma = {gamma}, Epsilon = {epsilon}, product = {gamma*epsilon}')

def splitByBit( nums: list, majority: bool, bitNum: int, default: int) -> list:
    zeroBits = []
    oneBits = []
    for num in nums:
        if num[bitNum] == '0': zeroBits.append(num)
        else: oneBits.append(num)
    if majority:
        if default == 0:
            return zeroBits if len(zeroBits) >= len(oneBits) else oneBits
        else:
            return zeroBits if len(zeroBits) > len(oneBits) else oneBits
    else:
        if default == 0:
            return zeroBits if len(zeroBits) <= len(oneBits) else oneBits
        else:
            return zeroBits if len(zeroBits) < len(oneBits) else oneBits

oxy_nums = nums

for i, cnt in enumerate(zero_counts):
    oxy_nums = splitByBit( oxy_nums, True, i, 1)
    if len(oxy_nums) == 1: break

co2_nums = nums
for i, cnt in enumerate(zero_counts):
    co2_nums = splitByBit( co2_nums, False, i, 0)
    if len(co2_nums) == 1: break

oxy_rating = int(oxy_nums[0], 2)
co2_rating = int(co2_nums[0], 2)
print('\nPart two:')
print(f'Oxygen rating = {oxy_rating}, CO2 rating = {co2_rating}, product = {oxy_rating*co2_rating}')