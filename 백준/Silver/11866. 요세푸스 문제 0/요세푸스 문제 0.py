import sys
from collections import deque
n, k = map(int, sys.stdin.readline().rstrip().split())
lst = deque(range(1, n + 1))
res = []
while lst:
    lst.rotate(-(k-1))
    res.append(lst.popleft())
print("<" + ", ".join(map(str, res)) + ">")