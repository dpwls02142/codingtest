import sys
n = int(sys.stdin.readline().rstrip())
lst = [0 for _ in range (1001)] # x는 1부터니까 0번째 인덱스 사용 x
t_idx, t = 0, 0
for _ in range (n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    lst[x] = y
    if t < y:
        t = y
        t_idx = x
# print(t_idx, t)
curr = 0
res = 0
# 왼쪽
for i in range (1, t_idx + 1): # 1, 10까지
    curr = max(curr, lst[i]) # 0, 4
    res += curr
# 오른쪽
curr = 0
for i in range (1000, t_idx, -1): # 1000부터 11까지
    curr = max(curr, lst[i])
    res += curr
print(res)