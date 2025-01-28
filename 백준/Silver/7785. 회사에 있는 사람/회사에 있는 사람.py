import sys

a = int(sys.stdin.readline().rstrip())
b = set()

for i in range(a):
    name, action = sys.stdin.readline().rstrip().split()
    if action == 'enter':
        b.add(name)
    elif action == 'leave':
        b.remove(name)

for name in sorted(b, reverse=True):
    print(name)