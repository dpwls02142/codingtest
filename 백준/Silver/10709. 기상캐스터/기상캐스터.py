import sys
h, w = map(int, sys.stdin.readline().rstrip().split())
clouds = []
for _ in range (h):
    clouds.append(list(sys.stdin.readline().rstrip()))
res = []
for i in range (h):
    temp = []
    cnt = 0
    for j in range (w):
        if clouds[i][j] == "c":
            temp.append(0)
            cnt += 1
            if j+1 < w and clouds[i][j+1] == "c":
                cnt = 0
        elif clouds[i][j] == "." and cnt >= 1:
            temp.append(cnt)
            cnt += 1
            if j+1 < w and clouds[i][j+1] == "c":
                cnt = 0
        elif clouds[i][j] == "." and cnt <= 0:
            temp.append(-1)
    res.append(temp)
for i in res:
    print(" ".join(map(str, i)))