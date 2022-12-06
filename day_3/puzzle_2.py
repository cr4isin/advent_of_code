
letters = 'abcdefghijklmnopqrstuvwxyz'
priority = dict(zip(letters + letters.upper(), range(1, 53)))
score = 0
with open('day_3\\input.txt') as file:
    rucksacks = file.read().splitlines()
    groups = [rucksacks[3*i:3*(i+1)] for i in range(len(rucksacks)//3)]
    for group in groups:
        score += priority[[c for c in group[0] if c in group[1] and c in group[2]][0]]
print(score)
