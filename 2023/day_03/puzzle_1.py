
from re import findall

with open('day_03\\input.txt') as file:
    file_text = file.read().splitlines()

height = len(file_text)
width = len(file_text[0])

total = 0
for row_index, line in enumerate(file_text):
    col_index = 0
    for value in findall('(\d+)', line):
        col_index = line.index(value, col_index)
        top_most = max(0, row_index - 1)
        bottom_most = min(height-1, row_index + 1)
        left_most = max(0, col_index - 1)
        right_most = min(width-1, col_index + len(value))
        found = False
        col_index += len(value)
        for row in range(top_most, bottom_most + 1):
            for col in range(left_most, right_most + 1):
                if (file_text[row][col] != '.') and (not file_text[row][col].isdigit()):
                    found = True
        if found:
            total += int(value)

print(total)
