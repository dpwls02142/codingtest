import sys
line = []
for _ in range (10):
    line.append(list(map(str, sys.stdin.readline().rstrip().split())))
s = False
for i in range (10):
    if len(set(line[i])) == 1:
        s = True
        break
if not s:
    for j in range (len(line[0])):
        temp = set()
        for i in range (10):
            temp.add(line[i][j])
        if len(temp) == 1:
            s = True
            break
if s:
    print(1)
else:
    print(0)