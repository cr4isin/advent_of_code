
from re import findall

with open('day_4\\input.txt') as file:
    count = 0
    for line in file:
        a, b, c, d = map(int, findall('(\d+)-(\d+),(\d+)-(\d+)', line)[0])
        count += any(i in range(a, b+1) for i in range(c, d+1))
print(count)
