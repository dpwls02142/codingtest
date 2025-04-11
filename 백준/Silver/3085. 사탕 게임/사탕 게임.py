import sys
n = int(sys.stdin.readline().rstrip())
candy = []
for _ in range (n):
    candy.append(list(sys.stdin.readline().rstrip()))

def count():
    max_cnt = 1
    for i in range (n):
        cnt = 1
        for j in range (n-1):
            if candy[i][j] == candy[i][j+1]:
                cnt += 1
                if cnt >= max_cnt:
                    max_cnt = cnt
            else:
                cnt = 1
    for j in range (n):
        cnt = 1
        for i in range (n-1):
            if candy[i][j] == candy[i+1][j]:
                cnt += 1
                if cnt >= max_cnt:
                    max_cnt = cnt
            else:
                cnt = 1
    return max_cnt

max_cnt = 0
for i in range (n):
    for j in range (n-1):
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        max_cnt = max(max_cnt, count())
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
for j in range (n):
    for i in range (n-1):
        candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
        max_cnt = max(max_cnt, count())
        candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
print(max_cnt)