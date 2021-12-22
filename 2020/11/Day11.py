import copy

master_seats = []

with open('seats.txt', 'r') as seat_map:
    for line in seat_map.readlines():
        row = [0]
        for char in line.strip():
            if char == '.':
                row.append(-1)
            if char == 'L':
                row.append(0)
        row.append(0)
        master_seats.append(row)

buffer_row = [0 for seat in master_seats[0]]
master_seats.insert(0, buffer_row)
master_seats.append(buffer_row)

def check_neighbors(row, col, seats, new_seats):
    front = sum([1 if seat==1 else 0 for seat in seats[row-1][col-1:col+2]])
    same = sum([1 if seat==1 else 0 for seat in seats[row][col-1:col+2]]) - seats[row][col]
    back = sum([1 if seat==1 else 0 for seat in seats[row+1][col-1:col+2]])
    occupied = front + same + back
    new_state = seats[row][col]
    if occupied == 0:
        new_state = 1
    elif occupied >= 4:
        new_state = 0
    if new_seats[row][col] > -1 and new_state != new_seats[row][col]:
        new_seats[row][col] = new_state
        return 1, seats, new_seats
    return 0, seats, new_seats

def print_seats(seats):
    for row in seats[1:-1]:
        for seat in row[1:-1]:
            if seat == -1: print('.', end='')
            elif seat == 1: print('#', end='')
            else: print('L', end='')
        print()
    print()

changes = 1

width = len(master_seats)-1
height = len(master_seats[0])-1

seats = copy.deepcopy(master_seats)
new_seats = copy.deepcopy(master_seats)
round_ = 1
while True:
    round_change = 0
    for i in range(1,width):
        for j in range(1,height):
            change, seats, new_seats = check_neighbors(i, j, seats, new_seats)
            round_change += change
    seats = copy.deepcopy(new_seats)
    if round_change == 0: break
    round_ += 1

occupied = sum([sum([1 if seat==1 else 0 for seat in row]) for row in seats])

print('\nPart one:')
print(f'Occupied seats: {occupied}')


directions = [(-1,-1), (-1, 0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
def find_closest_seat(row, col, seats, dir):
    x,y = directions[dir]
    while True:
        try:
            seat = seats[row+x][col+y]
            if seat == 0: return False
            if seat == 1: return True
        except:
            return False
        row += x
        col += y

def check_neighbors2(row, col, seats, new_seats, show=False):
    occupied = sum([find_closest_seat(row, col, seats, d) for d in range(len(directions))])
    if show: print(occupied)
    new_state = seats[row][col]
    if occupied == 0:
        new_state = 1
    elif occupied >= 5:
        new_state = 0
    if new_seats[row][col] > -1 and new_state != new_seats[row][col]:
        new_seats[row][col] = new_state
        return 1, seats, new_seats
    return 0, seats, new_seats



seats = copy.deepcopy(master_seats)
new_seats = copy.deepcopy(seats)

round_ = 1
while True:
    round_change = 0
    for i in range(1,width):
        for j in range(1,height):
            change, seats, new_seats = check_neighbors2(i, j, seats, new_seats)
            round_change += change
    # print(f'Round {round_}: {round_change}')
    seats = copy.deepcopy(new_seats)
    if round_change == 0: break
    round_ += 1

occupied = sum([sum([1 if seat==1 else 0 for seat in row]) for row in seats])

print('\nPart two:')
print(f'Occupied seats: {occupied}')

