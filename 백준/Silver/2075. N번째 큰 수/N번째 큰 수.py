import sys
import heapq
n = int(sys.stdin.readline().rstrip())
heap = []
for _ in range (n):
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in nums:
        if len(heap) < n:
            heapq.heappush(heap, i)
        else:
            heapq.heappushpop(heap, i)
print(heap[0])