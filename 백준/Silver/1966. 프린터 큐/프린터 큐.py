import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
for _ in range (n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    if x == 1 and y == 0:
        temp = int(sys.stdin.readline().rstrip())
        print(1)
    else:
        lst = list(map(int, sys.stdin.readline().rstrip().split()))
        docs = deque([(i, p) for i, p in enumerate(lst)])
        cnt = 0
        while docs:
            a = docs.popleft()
            valid = False
            for i in docs:
                if a[1] < i[1]:
                    valid = True
                    docs.append(a)
                    break
            else:
                cnt += 1
                if a[0] == y:
                    print(cnt)
                    break