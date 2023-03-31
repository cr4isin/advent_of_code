
def is_nice(line: str):
    if any(substr in line for substr in ('ab', 'cd', 'pq', 'xy')):
        return False

    if sum(line.count(vowel) for vowel in 'aeiou') < 3:
        return False

    if not any(x == y for x, y in zip(line[:-1], line[1:])):
        return False
    return True

with open('2015\\day_05\\input.txt') as file:
    text = file.read()

print(sum(is_nice(line) for line in text.splitlines()))
