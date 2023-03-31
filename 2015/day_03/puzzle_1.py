
with open('2015\\day_03\\input.txt') as file:
    text = file.read()

x = 0
y = 0
houses = {(x, y)}
for char in text:
    if char == '<':
        x -= 1
    elif char == '>':
        x += 1
    elif char == 'v':
        y -= 1
    elif char == '^':
        y += 1
    houses.add((x, y))

print(len(houses))
