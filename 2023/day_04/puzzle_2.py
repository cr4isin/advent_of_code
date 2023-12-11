
from re import findall
from collections import defaultdict

with open('day_04\\input.txt') as file:
    file_text = file.read().splitlines()

total = 0
card_counts = defaultdict(lambda: 1)
for line in file_text:
    count = 0
    card_text, ticket_text = line.split(':')
    winners_text, numbers_text = ticket_text.split('|')
    card = int(findall('(\d+)', card_text)[0])
    winning_numbers = findall('(\d+)', winners_text)
    for number in findall('(\d+)', numbers_text):
        if number in winning_numbers:
            count += 1
    for i in range(count):
        card_counts[card + i + 1] += card_counts[card]

print(sum(card_counts[i] for i in range(1,len(file_text)+1)))
