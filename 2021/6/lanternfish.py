
fish = []
with open( 'starting_fish.txt', 'r') as fish:

    line = fish.readline()
    fish = [int(timer.strip()) for timer in line.split(',')]

MAX_DAYS = 9
fish_timers = [0 for _ in range(MAX_DAYS)]
for f in fish:
    fish_timers[f] += 1

sim_days = 80
for _ in range(sim_days):
    reset_fish = fish_timers[0]
    fish_timers = fish_timers[1:] + [fish_timers[0]]
    fish_timers[6] += reset_fish

print('Part one:')
print(f'Total number of fish after {sim_days} days: {sum(fish_timers)}')


total_sim_days = 256
for _ in range(total_sim_days - sim_days):
    reset_fish = fish_timers[0]
    fish_timers = fish_timers[1:] + [fish_timers[0]]
    fish_timers[6] += reset_fish

print('\nPart two:')
print(f'Total number of fish after {sim_days} days: {sum(fish_timers)}')
