import sys
input = sys.stdin.readline
from collections import deque
n = int(input().rstrip())
stack = deque()
for _ in range (n):
    n = list(map(int, input().rstrip().split()))
    if len(n) >= 2:
        stack.append(n[1])
    else:
        command = n[0]
        if command == 2:
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif command == 3:
            print(len(stack))
        elif command == 4:
            if stack:
                print(0)
            else:
                print(1)
        else:
            if stack:
                print(stack[-1])
            else:
                print(-1)