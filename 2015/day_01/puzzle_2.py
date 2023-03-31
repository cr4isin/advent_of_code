with open('2015\\day_01\\input.txt') as file:
    text = file.read()

floor = 0
for index, char in enumerate(text, start=1):
    floor += 1 if char == '(' else -1
    if floor < 0:
        print(index)
        break