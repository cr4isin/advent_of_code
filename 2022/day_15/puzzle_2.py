
from re import findall

def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

dim = 4000000
sensor_info = []
with open('day_15\\input.txt') as file:
    for line in file:
        sx, sy, bx, by = map(int, findall('Sensor at x=([\d-]+), y=([\d-]+): closest beacon is at x=([\d-]+), y=([\d-]+)', line)[0])
        sensor_info.append(((sx, sy), dist(sx, sy, bx, by)))

for i in range(dim):
    j = 0
    while j < dim:
        dis = max(d-dist(*s, i, j) for s, d in sensor_info)
        if dis < 0:
            print(i*dim + j)
            break
        j += dis + 1
    else:
        continue
    break
