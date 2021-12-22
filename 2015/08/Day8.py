
total_chars = 0
non_mem_chars = 0

with open('strings.txt', 'r') as strings:

    for line in strings.readlines():
        total_chars += len(line)

        idx = 1
        non_mem_cnt = 2 # starting and ending quotes
        while idx < len(line):
            if line[idx] == '\\':
                check = line[idx+1]
                if check == '\\' or check == '\"':
                    non_mem_cnt += 1
                    idx += 2
                elif check == 'x':
                    non_mem_cnt += 3
                    idx += 4
            else:
                idx += 1
        non_mem_chars += non_mem_cnt
        

print('Part one:')
print(f'Difference between total and mem chars is {non_mem_chars}')

extra_encoded_chars = 0
with open('strings.txt', 'r') as strings:

    for line in strings.readlines():
        total_chars += len(line)

        idx = 0
        extra_encoded = 2 # start and end quotes
        while idx < len(line):
            if line[idx] == '\\' or line[idx] == '\"':
                extra_encoded += 1
            idx += 1
        extra_encoded_chars += extra_encoded

print('\nPart two:')
print(f'Difference between newly encoded and original is {extra_encoded_chars}')