import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0
for i in range (n):
    t1, t2, t3 = map(int, sys.stdin.readline().rstrip().split())
    if t1 == -1 and t2 == -1 and t3 == -1:
        continue
    temp = True
    if t1 == -1 and t2 != -1:
        temp = False
    if t2 == -1 and t3 != -1:
        temp = False
    if t1 != -1 and t2 != -1 and t1 > t2:
        temp = False
    if t2 != -1 and t3 != -1 and t2 > t3:
        temp = False
    if temp:
        cnt += 1
print(cnt)