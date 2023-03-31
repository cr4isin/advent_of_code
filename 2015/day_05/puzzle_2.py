
def is_nice(line: str):
    if not any(line.count(substr) > 1 for substr in (x + y for x, y in zip(line[:-1], line[1:]))):
        return False

    if not any(x == y for x, y in zip(line[:-2], line[2:])):
        return False
    return True

with open('2015\\day_05\\input.txt') as file:
    text = file.read()

print(sum(is_nice(line) for line in text.splitlines()))
