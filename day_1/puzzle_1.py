
with open('day_1\\input.txt') as f:
    print(max([sum(map(int,calorie_list.split('\n'))) for calorie_list in f.read().split('\n\n')]))