
indeces_to_check = [20, 60, 100, 140, 180, 220]
total_signal_strength = 0
cycle = 1
X = 1
with open('day_10\\input.txt') as file:
    for line in file.read().splitlines():
        increment = 0
        if line.startswith('addx'):
            increment = int(line.split()[1])
            total_signal_strength += cycle*X if cycle in indeces_to_check else 0
            cycle += 1
        total_signal_strength += cycle*X if cycle in indeces_to_check else 0
        X += increment
        cycle += 1
print(total_signal_strength)
