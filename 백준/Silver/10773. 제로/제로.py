import sys
from collections import deque
k = int(sys.stdin.readline().rstrip())
money = deque()
for _ in range (k):
    m = int(sys.stdin.readline().rstrip())
    if m == 0:
        money.popleft()
    else:
        money.appendleft(m)
print(sum(money))