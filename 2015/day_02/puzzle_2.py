
def ribbon_length(l, w, h):
    return 2 * (l + w + h - max(l, w, h)) + l * w * h


with open('2015\\day_02\\input.txt') as file:
    text = file.read()

total_area = 0
for line in text.split('\n'):
    l, w, h = map(int, line.split('x'))
    total_area += ribbon_length(l, w, h)

print(total_area)
