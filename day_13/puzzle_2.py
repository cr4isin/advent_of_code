
import ast
from functools import cmp_to_key

with open('day_13\\input.txt') as file:
    packets = list(map(ast.literal_eval, file.read().replace('\n\n', '\n').split('\n')))
    packets.append([[2]])
    packets.append([[6]])


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


sorted_list = sorted(packets, key=cmp_to_key(compare))
print((sorted_list.index([[2]])+1)*(sorted_list.index([[6]])+1))
