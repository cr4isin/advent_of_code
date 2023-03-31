
import ast

with open('day_13\\input.txt') as file:
    packets = file.read().split('\n\n')


def compare(a, b):
    if a == b:
        return 0
    if type(a) == int and type(b) == int:
        return -1 if a < b else 1
    elif type(a) == list and type(b) == int:
        return compare(a, [b])
    elif type(a) == int and type(b) == list:
        return compare([a], b)
    else:
        for a1, b1 in zip(a, b):
            x = compare(a1, b1)
            if x:
                return x
        return -1 if len(a) < len(b) else 1


total = 0
for index, pair in enumerate(packets, start=1):
    p1, p2 = map(ast.literal_eval, pair.split('\n'))
    if compare(p1, p2) <= 0:
        total += index

print(total)
