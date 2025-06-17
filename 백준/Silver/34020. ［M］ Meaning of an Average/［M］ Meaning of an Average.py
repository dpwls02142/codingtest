import sys
import heapq
import math
input = sys.stdin.readline
n = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
heapq.heapify(lst)
if len(lst) == 1:
    res = lst[0]
else:
    res = 0
    a = heapq.heappop(lst)
    b = heapq.heappop(lst)
    res += ((a + b) // 2)
    while len(lst) >= 1:
        res += heapq.heappop(lst)
        res /= 2
if res % 2 == 0:
    print(math.trunc(res))
else:
    print(res)