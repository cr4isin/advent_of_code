
from re import findall
from math import prod

with open('day_11\\input.txt') as f:
    initial_info = f.read().split('\n\n')

monkeys = [dict() for _ in initial_info]
for index, monkey_info in enumerate(initial_info):
    monkeys[index]['items'] = list(map(int, findall('Starting items: ([\d, ]+)', monkey_info)[0].split(', ')))
    monkeys[index]['operation'] = findall('new = (\w+) (\S) (\w+)', monkey_info)[0]
    monkeys[index]['test'] = tuple(map(int, (findall('divisible by (\d+)', monkey_info)[0], findall('true: throw to monkey (\d+)', monkey_info)[0], findall('false: throw to monkey (\d+)', monkey_info)[0])))

num_inspections = [0 for _ in monkeys]
for round in range(20):
    new_items = [list() for _ in monkeys]
    for index, monkey in enumerate(monkeys):
        for item in monkey['items']:
            a = item if monkey['operation'][0] == 'old' else int(monkey['operation'][0])
            b = item if monkey['operation'][2] == 'old' else int(monkey['operation'][2])
            if monkey['operation'][1] == '+':
                item = a + b
            elif monkey['operation'][1] == '*':
                item = a * b
            num_inspections[index] += 1
            item //= 3
            new_owner = monkey['test'][2] if item % monkey['test'][0] else monkey['test'][1]
            monkeys[new_owner]['items'].append(item)
        monkey['items'] = []

print(prod(sorted(num_inspections)[-2:]))
