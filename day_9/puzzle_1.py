
head = [0, 0]
tail = [0, 0]
visited_places = set()
direction = {
    'U': (0, 1),
    'R': (1, 0),
    'D': (0, -1),
    'L': (-1, 0),
}
with open('day_9\\input.txt') as file:
    for line in file.read().splitlines():
        direct, amount = line.split(' ')
        for _ in range(int(amount)):
            # Update Head
            head[0] += direction[direct][0]
            head[1] += direction[direct][1]
            # Update Tail
            delta_x = head[0]-tail[0]
            delta_y = head[1]-tail[1]
            if abs(delta_x) > 1 or abs(delta_y) > 1:
                if abs(delta_x) + abs(delta_y) > 2:
                    tail[0] += delta_x/abs(delta_x)
                    tail[1] += delta_y/abs(delta_y)
                else:
                    tail[0] += delta_x/abs(delta_x) if delta_x else 0
                    tail[1] += delta_y/abs(delta_y) if delta_y else 0
            visited_places.add(tuple(tail))
print(len(visited_places))
