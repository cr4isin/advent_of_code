
def paper_area(l, w, h):
    x = l*w
    y = l*h
    z = w*h
    return 2 * (x + y + z) + min(x, y, z)

with open('2015\\day_02\\input.txt') as file:
    text = file.read()

total_area = 0
for line in text.split('\n'):
    l, w, h = map(int, line.split('x'))
    total_area += paper_area(l, w, h)

print(total_area)
