start = 1113122113
iters = 40

def look_and_say(num):
    count = 1
    val = num[0]
    result = ''
    for digit in num[1:]:
        if digit == val:
            count += 1
        else:
            result += f'{count}{val}'
            val = digit
            count = 1
    result += f'{count}{val}'
    return result

final = str(start)
for _ in range(iters):
    final = look_and_say(final)

print('Part one:')
print(f'After {iters} iterations the number length is {len(final)} digits')

iters = 50
final = str(start)
for _ in range(iters):
    final = look_and_say(final)

print('\nPart two:')
print(f'After {iters} iterations the number length is {len(final)} digits')