

num_rows = 128
num_cols = 8

seat_ids = []
with open('seats.txt', 'r') as seats:
    for line in seats.readlines():
        row_code = line[:7]
        col_code = line[7:]
        
        low = 0
        half_size = num_rows / 2
        for char in row_code:
            if char == 'B':
                low += half_size
            half_size /= 2
        seat_row = low

        low = 0
        half_size = num_cols / 2
        for char in col_code:
            if char == 'R':
                low += half_size
            half_size /= 2
        seat_col = low

        seat_ids.append( seat_row * 8 + seat_col )

print('Part one:')
print(f'Max seat id is {int(max(seat_ids))}')

import time

start = time.time()

seat_ids.sort()
expected_id_sum = (seat_ids[0] + seat_ids[-1]) / 2 * (len(seat_ids) + 1 )
missing_seat = int(expected_id_sum - sum(seat_ids))

end = time.time()
print(f"Runtime: {end - start}s")

print('\nPart two:')
print(f'My seat is {missing_seat}')



