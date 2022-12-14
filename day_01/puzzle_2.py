
print(sum(sorted(sum(map(int,calorie_list.split('\n'))) for calorie_list in open('day_1\\input.txt').read().split('\n\n'))[-3:]))