
# Readable Version
with open('day_01\\input.txt') as file:
    file_text = file.read().splitlines()

total = 0
for line in file_text:
    digits = list(filter(lambda x: x.isdigit(), line))
    total += int(digits[0] + digits[-1])

print(total)

# One-Line Version
print(sum(int(digits[0]+digits[-1]) for digits in (list(filter(lambda x: x.isdigit(), line)) for line in open('day_01\\input.txt').read().splitlines())))
