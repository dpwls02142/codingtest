import sys
t = int(sys.stdin.readline().rstrip())
for _ in range (t):
    h, w, n = map(int, sys.stdin.readline().rstrip().split())
    lst = []
    for i in range (1, w+1):
        for j in range (1, h+1):
            if i < 10:
                lst.append(str(j)+"0"+str(i))
            else:
                lst.append(str(j)+str(i))
    for i in range (len(lst)):
        if i == n - 1:
            print(lst[i])
            break