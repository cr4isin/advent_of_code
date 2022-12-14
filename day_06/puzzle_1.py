
with open('day_6\\input.txt') as file:
    text = file.read()
    for i in range(4, len(text)):
        if len(set(text[i-4:i])) == 4:
            print(i)
            break