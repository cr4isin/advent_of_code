
from re import findall
from collections import defaultdict

with open('day_05\\input.txt') as file:
    seed_text, *file_text = file.read().strip().split('\n\n')

seed_maps = list()
for seed_group in findall('(\d+ \d+)', seed_text):
    seed_start, seed_length = map(int, seed_group.split(' '))
    seed_maps.append((seed_start, seed_length))


maps = defaultdict(list)
for map_text in file_text:
    map_name, *map_lines = map_text.split('\n')
    for line in map_lines:
        maps[map_name].append(tuple(map(int, findall('(\d+)', line))))

def single_map(values, seed):
    for source_start, dest_start, range_len in values:
        if seed in range(source_start, source_start + range_len):
            seed += dest_start - source_start
            break
    return seed

def all_maps(seed):
    for values in reversed(maps.values()):
        seed = single_map(values, seed)
    return seed

location = 1
while True:
    seed = all_maps(location)
    for seed_start, seed_length in seed_maps:
        if seed in range(seed_start, seed_start + seed_length):
            print(location)
            break
    else:
        location += 1
        continue
    break