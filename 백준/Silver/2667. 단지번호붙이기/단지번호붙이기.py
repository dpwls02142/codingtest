import sys
n = int(sys.stdin.readline().rstrip())
maps = []
for _ in range (n):
    maps.append(list(sys.stdin.readline().rstrip()))
houses = []
def dfs(i, j, groups):
    maps[i][j] = "0"
    groups.append(1)
    if i > 0 and maps[i-1][j] == "1":
        dfs(i-1, j, groups)
    if i < n-1 and maps[i+1][j] == "1":
        dfs(i+1, j, groups)
    if j > 0 and maps[i][j-1] == "1":
        dfs(i, j-1, groups)
    if j < n-1 and maps[i][j+1] == "1":
        dfs(i, j+1, groups)
for i in range (n):
    for j in range (n):
        if maps[i][j] == "1":
            groups = []
            dfs(i, j, groups)
            houses.append(groups)
# print(houses)
houses.sort(key=len)
print(len(houses))
for i in houses:
    print(len(i))