
from re import findall
from collections import defaultdict
from math import prod

with open('day_03\\input.txt') as file:
    file_text = file.read().splitlines()

height = len(file_text)
width = len(file_text[0])

gear_values = defaultdict(list)
for row_index, line in enumerate(file_text):
    col_index = 0
    for value in findall('(\d+)', line):
        col_index = line.index(value, col_index)
        top_most = max(0, row_index - 1)
        bottom_most = min(height-1, row_index + 1)
        left_most = max(0, col_index - 1)
        right_most = min(width-1, col_index + len(value))
        col_index += len(value)
        for row in range(top_most, bottom_most + 1):
            for col in range(left_most, right_most + 1):
                if file_text[row][col] == '*':
                    gear_values[(row, col)].append(int(value))

total = 0
for values in gear_values.values():
    if len(values) == 2:
        total += prod(values)

print(total)
