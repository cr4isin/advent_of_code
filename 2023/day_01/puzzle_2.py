
digit_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

with open('day_01\\input.txt') as file:
    file_text = file.read().splitlines()

total = 0
for line in file_text:
    for digit_text, digit in digit_map.items():
        line = line.replace(digit_text, digit_text+digit+digit_text)
    digits = list(filter(lambda x: x.isdigit(), line))
    total += int(digits[0] + digits[-1])

print(total)
