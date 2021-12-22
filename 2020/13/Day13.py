
time = busses = []
bus_offsets = {}
with open('schedule.txt', 'r') as schedule:
    time = int(schedule.readline().strip())
    offset = 0
    for num in schedule.readline().strip().split(','):
        if num != 'x':
            busses.append(int(num))
            bus_offsets[int(num)] = offset
        offset += 1

diffs = [bus - (time % bus) for bus in busses]

bus_id = busses[diffs.index(min(diffs))]
print('Part one:')
print(f'Bus ID: {bus_id}, wait = {min(diffs)}, product = {bus_id * min(diffs)}')

val = busses[0]

last = busses[0]
lcm = busses[0]
for period in busses[1:]:
    val += bus_offsets[period] - bus_offsets[last]
    while val % period != 0:
        val += lcm
    lcm *= period
    last = period

print('\nPart two:')
print(f't0 = {val-bus_offsets[busses[-1]]}')