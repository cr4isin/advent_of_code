
from re import findall

# Setup
def sign(x):
    return x//abs(x) if x else 0

with open('day_14\\input.txt') as file:
    file_text = file.read()

min_x = min(map(int, findall('(\d+),\d+', file_text)))
max_x = max(map(int, findall('(\d+),\d+', file_text)))
max_y = max(map(int, findall('\d+,(\d+)', file_text)))
width = max_x - min_x + 3
height = max_y + 2
x_adjust = min_x - 1
cave = [['.' for y in range(height)] for x in range(width)]

# Draw Cave
for line in file_text.split('\n'):
    path = [list(map(int, point.split(','))) for point in line.split(' -> ')]
    for i in range(len(path)-1):
        init_x, init_y = path[i]
        final_x, final_y = path[i+1]
        if dx := sign(final_x - init_x):
            for j in range(init_x, final_x+dx, dx):
                cave[j-x_adjust][init_y] = '#'
        if dy := sign(final_y - init_y):
            for j in range(init_y, final_y+dy, dy):
                cave[init_x-x_adjust][j] = '#'

# Drop Sand
rested_grains = 0
floor_hit = False
while not floor_hit:
    current_x = 500
    current_y = 0
    rested = False
    while not rested:
        if current_y >= height-1:
            floor_hit = True
            break
        if cave[current_x-x_adjust][current_y+1] == '.':
            current_y += 1
        elif cave[current_x-x_adjust-1][current_y+1] == '.':
            current_x -= 1
            current_y += 1
        elif cave[current_x-x_adjust+1][current_y+1] == '.':
            current_x += 1
            current_y += 1
        else:
            cave[current_x-x_adjust][current_y] = 'o'
            rested_grains += 1
            rested = True

print(rested_grains)
