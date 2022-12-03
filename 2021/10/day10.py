
def parse_file():
    lines = []
    with open('lines.txt', 'r') as file:
        for line in file.readlines():
            lines.append(line.strip())
    return lines

def get_incomplete(lines):
    subset = []
    for line in lines:
        stack = []
        corrupt = False
        for char in line:
            if char in starts:
                stack.append(char)
            else:
                start = stack.pop()
                if start != pair[char]:
                    corrupt = True
                    break
        if not corrupt:
            subset.append(line)
    return subset

starts = ['(', '[', '{', '<']
pair = { ')':'(', ']':'[', '}':'{', '>':'<' }
error_vals = {')':3, ']':57, '}':1197, '>':25137 }

def first_star():
    lines = parse_file()
    errors = []
    for line in lines:
        stack = []
        for char in line:
            if char in starts:
                stack.append(char)
            else:
                start = stack.pop()
                if start != pair[char]:
                    errors.append(char)
                    break

    total_error = sum([ error_vals[char] for char in errors])
    print(f'The total syntax error sum is {total_error}')


def second_star():
    lines = parse_file()
    incomplete = get_incomplete(lines)

    remaining = []
    # Find remaining brackets that are incomplete
    for line in incomplete:
        stack = []
        for char in line:
            if char in starts:
                stack.append(char)
            else:
                stack.pop()
        remaining.append(stack)

    incomp_vals = {'(':1, '[':2, '{':3, '<':4 }

    vals = []
    for stack in remaining:
        vals.append(0)
        while len(stack):
            char = stack.pop()
            vals[-1] *= 5
            vals[-1] += incomp_vals[char]

    vals.sort()
    print(f'The median error score is {vals[len(vals)//2]}')

if __name__ == '__main__':
    first_star()
    second_star()
