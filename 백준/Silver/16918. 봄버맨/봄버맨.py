import sys
r, c, n = map(int, sys.stdin.readline().rstrip().split())
lst = []
for _ in range (r):
    a = list(map(str, sys.stdin.readline().rstrip()))
    lst.append(a)
if n == 1:
    for i in lst:
        print("".join(i))
    sys.exit()
if n % 2 == 0:
    for i in range (r):
        print("O" * c)
    sys.exit()
def explosion(grid):
    new_grid = [['O' for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'O':
                new_grid[i][j] = '.'
                if i > 0: new_grid[i-1][j] = '.'
                if i < r-1: new_grid[i+1][j] = '.'
                if j > 0: new_grid[i][j-1] = '.'
                if j < c-1: new_grid[i][j+1] = '.'
    return new_grid
if n % 4 == 3:
    result = explosion(lst)
    for i in result:
        print("".join(i))
elif n % 4 == 1:
    temp = explosion(lst)
    result = explosion(temp)
    for i in result:
        print("".join(i))