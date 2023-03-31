
display = [['.']*40 for _ in range(6)]
cycle = 1
X = 1
with open('day_10\\input.txt') as file:
    for line in file.read().splitlines():
        increment = 0
        if line.startswith('addx'):
            increment = int(line.split()[1])
            display[(cycle-1)//40][(cycle-1)%40] = '#' if abs((cycle-1)%40-X) <= 1 else '.'
            cycle += 1
        display[(cycle-1)//40][(cycle-1)%40] = '#' if abs((cycle-1)%40-X) <= 1 else '.'
        X += increment
        cycle += 1
print('\n'.join(''.join(row) for row in display))
