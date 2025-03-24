import sys
import heapq
n = int(sys.stdin.readline().rstrip())
heap = []
zero_cnt = 0
res = []
for _ in range (n):
    x = int(sys.stdin.readline().rstrip())
    if x > 0:
        heapq.heappush(heap, x)
    elif x == 0:
        if len(heap) > 0:
            res.append(heapq.heappop(heap))
        else:
            res.append(0)
        zero_cnt += 1
for i in range (zero_cnt):
    print(res[i])