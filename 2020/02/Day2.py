
valid_passwords = 0
total_passwords = 0
with open('passwords.txt', 'r') as passwords:
    for line in passwords:
        parts = line.split(':')
        reqs = parts[0].split()
        req_nums = [int(x) for x in reqs[0].split('-')]
        req_letter = reqs[1]
        password = parts[1].strip()

        letter_cnt = password.count(req_letter)
        if req_nums[0] <= letter_cnt <= req_nums[1]:
            valid_passwords += 1
        total_passwords += 1

print("Part one:")
print(f'Valid passwords: {valid_passwords} out of {total_passwords}')

valid_passwords = 0
with open('passwords.txt', 'r') as passwords:
    for line in passwords:
        parts = line.split(':')
        reqs = parts[0].split()
        req_nums = [int(x) for x in reqs[0].split('-')]
        req_letter = reqs[1]
        password = parts[1].strip()

        if (password[req_nums[0]-1] == req_letter) != \
            (password[req_nums[1]-1] == req_letter):
            valid_passwords += 1

print("Part two:")
print(f'Valid passwords: {valid_passwords} out of {total_passwords}')

