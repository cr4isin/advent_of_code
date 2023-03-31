
print(max([sum(map(int,calorie_list.split('\n'))) for calorie_list in open('day_01\\input.txt').read().split('\n\n')]))