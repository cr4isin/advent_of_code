
with open('2015\\day_03\\input.txt') as file:
    text = file.read()

x = 0
y = 0
houses = {(x, y)}
robo_x = 0
robo_y = 0
robo_houses = {(robo_x, robo_y)}
for index, char in enumerate(text):
    if index % 2:
        if char == '<':
            x -= 1
        elif char == '>':
            x += 1
        elif char == 'v':
            y -= 1
        elif char == '^':
            y += 1
        houses.add((x, y))
    else:
        if char == '<':
            robo_x -= 1
        elif char == '>':
            robo_x += 1
        elif char == 'v':
            robo_y -= 1
        elif char == '^':
            robo_y += 1
        robo_houses.add((robo_x, robo_y))

print(len(houses.union(robo_houses)))
