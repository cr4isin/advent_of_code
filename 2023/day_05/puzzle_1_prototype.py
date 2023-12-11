
from re import findall
from collections import defaultdict

with open('day_05\\input2.txt') as file:
    seed_text, *file_text = file.read().strip().split('\n\n')

seeds = map(int, findall('(\d+)', seed_text))

maps = defaultdict(dict)
for map_text in file_text:
    map_name, *map_lines = map_text.split('\n')
    for line in map_lines:
        dest_start, source_start, length = map(int, findall('(\d+)', line))
        maps[map_name].update(zip(range(source_start, source_start+length), range(dest_start, dest_start + length)))

def map_seed(seed):
    for map in maps.values():
        seed = map.get(seed, seed)
    return seed

print(min(map(map_seed, seeds)))
