
opp = {'A':1, 'B':2, 'C':3}
mine = {'X':1, 'Y':2, 'Z':3}
result_points = { 2:0, 0:3, 1:6}
option_from_result = {1:2, 2:0, 3:1}

def parse_file():

    results = []
    with open('scheme.txt', 'r') as file:
        for line in file.readlines():
            them, me = line.strip().split(' ')
            results.append( [opp[them], mine[me]])
    return results

def first_star():
    results = parse_file()

    total = sum([ result_points[(result[1] - result[0]) % 3] + result[1] \
        for result in results ])

    print(f'1. Total score from strategy guide is {total}')

def second_star():
    results = parse_file()

    total = 0
    for result in results:
        total += (result[1] - 1)*3
        you = (result[0] + option_from_result[result[1]]) % 3
        total += you if you else 3
    print(f'2. Total score from strategy guide is {total}')

if __name__ == '__main__':
    first_star()
    second_star()
