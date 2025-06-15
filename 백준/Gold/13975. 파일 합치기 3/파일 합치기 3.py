import sys
input = sys.stdin.readline
import heapq
t = int(input().rstrip())
for _ in range (t):
    n = int(input().rstrip())
    files = list(map(int, input().rstrip().split()))
    heapq.heapify(files)
    res = 0
    while len(files) > 1:
        f = heapq.heappop(files)
        s = heapq.heappop(files)
        cost = f + s
        res += cost
        heapq.heappush(files, cost)
    print(res)