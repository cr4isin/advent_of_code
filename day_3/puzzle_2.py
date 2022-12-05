
letters = 'abcdefghijklmnopqrstuvwxyz'
priority = dict(zip(letters + letters.upper(), range(1, 53)))
score = 0
with open('day_3\\input.txt') as file:
    rucksacks = file.read().split('\n')
    groups = [rucksacks[3*i:3*(i+1)] for i in range(len(rucksacks)//3)]
    for group in groups:
        score += priority[next(iter(set(group[0]).intersection(set(group[1]).intersection(set(group[2])))))]
print(score)
