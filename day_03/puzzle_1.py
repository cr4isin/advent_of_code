
letters = 'abcdefghijklmnopqrstuvwxyz'
priority = dict(zip(letters + letters.upper(), range(1, 53)))
score = 0
with open('day_3\\input.txt') as file:
    for line in file.read().splitlines():
        comp_len = len(line) // 2
        score += priority[[c for c in line[:comp_len] if c in line[comp_len:]][0]]
print(score)
