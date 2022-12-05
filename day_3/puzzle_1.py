
letters = 'abcdefghijklmnopqrstuvwxyz'
priority = dict(zip(letters + letters.upper(), range(1, 53)))
score = 0
with open('day_3\\input.txt') as file:
    for line in file:
        comp_len = len(line.strip()) // 2
        score += priority[next(iter(set(line.strip()[:comp_len]).intersection(set(line.strip()[comp_len:]))))]
print(score)
