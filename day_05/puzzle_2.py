
from re import findall

with open('day_05\\input.txt') as file:
    # Read file
    file_text = file.read().splitlines()
    config = file_text[:8]
    instructions = file_text[10:]
    # Get stacks as strings
    stacks = zip(*([line[4*i:4*(i+1)] for i in range(len(line)//4 + 1)] for line in config))
    stacks_text = [''.join(reversed(findall('(\w)', ''.join(line)))) for line in stacks]
    # Operate instructions on stacks
    for line in instructions:
        amount, from_col, to_col = map(int, findall('move (\d+) from (\d+) to (\d+)', line)[0])
        stacks_text[to_col-1] += stacks_text[from_col-1][-amount:]
        stacks_text[from_col-1] = stacks_text[from_col-1][:-amount]

    print(''.join(t[-1] for t in stacks_text))
