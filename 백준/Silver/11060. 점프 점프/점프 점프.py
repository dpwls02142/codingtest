import sys
n = int(sys.stdin.readline().rstrip())
maze = list(map(int, sys.stdin.readline().rstrip().split()))
jump, end, max_jump = 0, 0, 0
for i in range (n-1):
    max_jump = max(max_jump, i + maze[i])
    if i == end:
        jump += 1
        end = max_jump
        if end < i:
            print(-1)
            break
else:
    if end >= n-1:
        print(jump)
    else:
        print(-1)