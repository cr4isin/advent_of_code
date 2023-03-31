
with open('day_08\\input.txt') as file:
    tree_grid = [list(map(int, line)) for line in file.read().splitlines()]
n = len(tree_grid)
m = len(tree_grid[0])
max_scenic_score = 0
for i in range(1, n-1):
    for j in range(1, m-1):
        north = south = east = west = 0
        for k in reversed(range(0,i)):
            north += 1
            if tree_grid[k][j] >= tree_grid[i][j]:
                break
        for k in range(i+1,n):
            south += 1
            if tree_grid[k][j] >= tree_grid[i][j]:
                break
        for k in reversed(range(0,j)):
            west += 1
            if tree_grid[i][k] >= tree_grid[i][j]:
                break
        for k in range(j+1,m):
            east += 1
            if tree_grid[i][k] >= tree_grid[i][j]:
                break
        max_scenic_score = max(max_scenic_score, north*east*south*west)
print(max_scenic_score)
