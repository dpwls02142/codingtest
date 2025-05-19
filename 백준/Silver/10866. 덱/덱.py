import sys
input = sys.stdin.readline
from collections import deque
n = int(input().rstrip())
deq = deque()
for _ in range (n):
    a = list(input().rstrip().split())
    if len(a) >= 2:
        command, num = a[0], a[1]
        if command == "push_front":
            deq.appendleft(int(num))
        else:
            deq.append(int(num))
    else:
        command = a[0]
        if command == "pop_front":
            if deq:
                print(deq.popleft())
            else:
                print(-1)
        elif command == "pop_back":
            if deq:
                print(deq.pop())
            else:
                print(-1)
        elif command == "size":
            print(len(deq))
        elif command == "empty":
            if deq:
                print(0)
            else:
                print(1)
        elif command == "front":
            if deq:
                print(deq[0])
            else:
                print(-1)
        else:
            if deq:
                print(deq[-1])
            else:
                print(-1)