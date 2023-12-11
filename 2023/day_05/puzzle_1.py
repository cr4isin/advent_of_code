
from re import findall
from collections import defaultdict

with open('day_05\\input.txt') as file:
    seed_text, *file_text = file.read().strip().split('\n\n')

seeds = map(int, findall('(\d+)', seed_text))

maps = defaultdict(list)
for map_text in file_text:
    map_name, *map_lines = map_text.split('\n')
    for line in map_lines:
        maps[map_name].append(tuple(map(int, findall('(\d+)', line))))

def single_map(values, seed):
    for dest_start, source_start, range_len in values:
        if seed in range(source_start, source_start + range_len):
            seed += dest_start - source_start
            break
    return seed

def all_maps(seed):
    for values in maps.values():
        seed = single_map(values, seed)
    return seed

print(min(map(all_maps, seeds)))
