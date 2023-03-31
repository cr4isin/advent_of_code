
with open('day_06\\input.txt') as file:
    text = file.read()
    for i in range(14, len(text)):
        if len(set(text[i-14:i])) == 14:
            print(i)
            break