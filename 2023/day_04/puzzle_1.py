
from re import findall

with open('day_04\\input.txt') as file:
    file_text = file.read().splitlines()

total = 0
for line in file_text:
    count = 0
    card, ticket = line.split(':')
    winners, numbers = ticket.split('|')
    winning_numbers = findall('(\d+)', winners)
    for number in findall('(\d+)', numbers):
        if number in winning_numbers:
            count += 1
    if count:
        total += 2 ** (count - 1)

print(total)
