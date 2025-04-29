import sys
from collections import deque
input = sys.stdin.readline

n, pop_value = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))
queue = deque(_ for _ in range (1, n + 1))
res = 0

for num in lst:
    idx = queue.index(num)
    if idx <= len(queue) // 2:
        queue.rotate(-idx)
        res += idx
    else:
        queue.rotate(len(queue) - idx)
        res += (len(queue) - idx)
    queue.popleft()
print(res)