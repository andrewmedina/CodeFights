def sudoku2(grid):
    print(grid)
    for i in range(9):
        for j in range(9):
            if grid[i][j] != ".":
                if not check_grid(grid,grid[i][j],i,j):
                    return False
    return True
        
def check_grid(the_grid,num,x,y):
    for i in range(9):
        if (the_grid[x][i] == num and i != y) or (the_grid[i][y] == num and i != x):
            return False
    for i in range((x//3) * 3, ((x//3) * 3) + 3):
        for j in range((y//3) * 3, ((y//3) * 3) + 3):
            if the_grid[i][j] == num and (i != x or j != y):
                return False
    return True