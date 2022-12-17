
with open('day_08\\input.txt') as file:
    tree_grid = [list(map(int, line)) for line in file.read().splitlines()]
n = len(tree_grid)
m = len(tree_grid[0])
visible_trees = 2*n + 2*m - 4
for i in range(1, n-1):
    for j in range(1, m-1):
        visible_trees += any([
            all(tree_grid[k][j] < tree_grid[i][j] for k in range(0, i)),
            all(tree_grid[k][j] < tree_grid[i][j] for k in range(i+1, n)),
            all(tree_grid[i][k] < tree_grid[i][j] for k in range(0, j)),
            all(tree_grid[i][k] < tree_grid[i][j] for k in range(j+1, m))
        ])
print(visible_trees)
