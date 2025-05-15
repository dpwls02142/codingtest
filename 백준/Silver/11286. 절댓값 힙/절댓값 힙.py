import sys
import heapq
input = sys.stdin.readline
n = int(input().rstrip())
heap = []
res = []
for _ in range (n):
    x = int(input().rstrip())
    if x == 0:
        if heap:
            temp, ori = heapq.heappop(heap)
            print(ori)
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))