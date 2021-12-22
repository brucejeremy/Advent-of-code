
nums = []
with open('expense_report.txt', 'r') as report:
    for line in report.readlines():
        nums.append(int(line.strip()))

found = False
for idx, num in enumerate(nums):
    for j in range(idx+1, len(nums)):
        if num + nums[j] == 2020:
            print(f'{num}, {nums[j]}, {num*nums[j]}')
            found = True
            break
    if found: break

found = False
for idx, num in enumerate(nums):
    for j in range(idx+1, len(nums)):
        for k in range(j+1, len(nums)):
            if num + nums[j] + nums[k] == 2020:
                print(f'{num}, {nums[j]}, {nums[k]}, {num*nums[j]*nums[k]}')
                found = True
                break
        if found: break
    if found: break
