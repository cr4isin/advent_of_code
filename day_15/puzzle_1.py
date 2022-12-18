
from re import findall

sensors, beacons, positions = set(), set(), set()
check_y = 2000000
with open('day_15\\input.txt') as file:
    for line in file:
        sx, sy, bx, by = map(int, findall('Sensor at x=([\d-]+), y=([\d-]+): closest beacon is at x=([\d-]+), y=([\d-]+)', line)[0])
        sensors.add((sx, sy))
        beacons.add((bx, by))
        d = abs(sx-bx) + abs(sy-by)
        dy = abs(sy-check_y)
        for i in range(d - dy + 1):
            positions.add((sx-i, check_y))
            positions.add((sx+i, check_y))

positions = positions.difference(sensors).difference(beacons)
print(len(positions))
