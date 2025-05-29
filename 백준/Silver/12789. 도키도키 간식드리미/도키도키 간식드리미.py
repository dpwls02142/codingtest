import sys
input = sys.stdin.readline

n = int(input().rstrip())
snacks = list(map(int, input().rstrip().split()))
stack = []
order = 1
while snacks or stack:
    if snacks and snacks[0] == order:
        snacks.pop(0)
        order += 1
    elif stack and stack[-1] == order:
        stack.pop()
        order += 1
    elif snacks:
        stack.append(snacks.pop(0))
    else:
        break
if order == n + 1:
    print("Nice")
else:
    print("Sad")