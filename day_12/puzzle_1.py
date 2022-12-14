
height = dict(zip('abcdefghijklmnopqrstuvwxyz', range(26)))
height['S'] = 0
height['E'] = 25

with open('day_12\\input.txt') as file:
    elevation_map: list[list[str]] = [list(row) for row in file.read().splitlines()]

for row_index, row in enumerate(elevation_map):
    if 'S' in row:
        origin = row_index, row.index('S')
    if 'E' in row:
        destination = row_index, row.index('E')

num_rows, num_cols = len(elevation_map), len(elevation_map[0])
visited_places = set([origin])
new_places = set([origin])
steps = 0

while destination not in visited_places:
    steps += 1
    places_to_reach = set()
    for position in new_places:
        x, y = position
        current_height = height[elevation_map[x][y]]
        if x > 0 and height[elevation_map[x-1][y]] - current_height <= 1:
            places_to_reach.add((x-1, y))
        if x < num_rows-1 and height[elevation_map[x+1][y]] - current_height <= 1:
            places_to_reach.add((x+1, y))
        if y > 0 and height[elevation_map[x][y-1]] - current_height <= 1:
            places_to_reach.add((x, y-1))
        if y < num_cols-1 and height[elevation_map[x][y+1]] - current_height <= 1:
            places_to_reach.add((x, y+1))
    new_places = places_to_reach.difference(visited_places)
    visited_places = visited_places.union(new_places)

print(steps)
