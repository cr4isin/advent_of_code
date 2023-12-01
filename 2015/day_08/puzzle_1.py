
with open('2015\\day_08\\input.txt') as file:
    text = file.read()

total = 0
for line in text.splitlines():
    total += len(line) - len(eval(line))
print(total)
