with open('2015\\day_01\\input.txt') as file:
    text = file.read()

print(text.count('(') - text.count(')'))
