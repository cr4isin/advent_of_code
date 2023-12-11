
from re import findall
from math import sqrt, ceil, floor, prod

with open('day_06\\input.txt') as file:
    time_text, dist_text = file.read().splitlines()

time = map(int, findall('(\d+)', time_text))
dist = map(int, findall('(\d+)', dist_text))

counts = []
for T, D in zip(time, dist):
    lower = ceil(.5 * (T - sqrt(T*T - 4*D)))
    upper = floor(.5 * (T + sqrt(T*T - 4*D)))
    counts.append(1 + upper - lower)

print(prod(counts))
