import sys
input = sys.stdin.readline
n = int(input().rstrip())
students = []
cnts = []
for _ in range (n):
    students.append(list(map(int, input().rstrip().split())))
max_cnt = -1
res = 0
for i in range (n):
    cnt = 0
    for j in range (n):
        if i == j:
            continue
        for k in range (5):
            if students[i][k] == students[j][k]:
                cnt += 1
                break
    if cnt > max_cnt:
        max_cnt = cnt
        res = i + 1
print(res)