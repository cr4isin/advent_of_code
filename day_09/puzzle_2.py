
rope = [[0, 0] for _ in range(10)]
visited_places = set()
direction = {
    'U': (0, 1),
    'R': (1, 0),
    'D': (0, -1),
    'L': (-1, 0),
}


def move_segment(leader: list[int], follower: list[int]):
    delta_x = leader[0]-follower[0]
    delta_y = leader[1]-follower[1]
    if abs(delta_x) > 1 or abs(delta_y) > 1:
        if abs(delta_x) + abs(delta_y) > 2:
            follower[0] += delta_x/abs(delta_x)
            follower[1] += delta_y/abs(delta_y)
        else:
            follower[0] += delta_x/abs(delta_x) if delta_x else 0
            follower[1] += delta_y/abs(delta_y) if delta_y else 0


with open('day_9\\input.txt') as file:
    for line in file.read().splitlines():
        direct, amount = line.split(' ')
        for _ in range(int(amount)):
            rope[0][0] += direction[direct][0]
            rope[0][1] += direction[direct][1]
            for i in range(len(rope)-1):
                move_segment(rope[i], rope[i+1])
            visited_places.add(tuple(rope[-1]))
print(len(visited_places))
