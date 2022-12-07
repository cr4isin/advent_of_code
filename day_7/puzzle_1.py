
from collections import defaultdict
from re import findall

# Determine the total size of the files in each directory
position = 'C:'
dir_size = defaultdict(int)
with open('day_7\\input.txt') as file:
    for line in file.read().splitlines():
        # Move current directory
        if matches := findall('\$ cd ([\w./]+)', line):
            if matches[0] == '/':
                position = 'C:'
            elif matches[0] == '..':
                position = '\\'.join(position.split('\\')[:-1])
            else:
                position += '\\' + matches[0]
            dir_size[position] += 0
        # Add file size if a file was found in current directory
        elif matches := findall('(\d+) [\w.]+', line):
            dir_size[position] += int(matches[0])

# Calculate total dir sizes
total_dir_size = dict()
for key1 in dir_size:
    total_dir_size[key1] = sum(dir_size[key2] for key2 in dir_size if key2.startswith(key1))

print(sum(x for x in total_dir_size.values() if x <= 100000))
