from re import findall

grid = [[0]*1000 for _ in range(1000)]

with open('2015\\day_06\\input.txt') as file:
    text = file.read()

for line in text.splitlines():
    x1, y1, x2, y2 = map(int,findall(' (\d+),(\d+) through (\d+),(\d+)', line)[0])
    if line.startswith('turn on'):
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                grid[x][y] += 1
    elif line.startswith('turn off'):
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                grid[x][y] = max(0,grid[x][y]-1)
    elif line.startswith('toggle'):
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                grid[x][y] += 2

print(sum(sum(row) for row in grid))
