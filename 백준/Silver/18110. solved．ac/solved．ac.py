import sys
def round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
n = int(sys.stdin.readline().rstrip())
if n == 0:
    print(0)
else:
    level = []
    for _ in range (n):
        level.append(int(sys.stdin.readline().rstrip()))
    if len(level) == 1 and level[0] == 0:
        print(0)
    else:
        level.sort()
        a = round(n * 15.0 / 100.0)
        level = level[a:n-a]
        print(round(sum(level) / len(level)))