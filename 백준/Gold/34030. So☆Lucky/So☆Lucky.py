import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))

odd, even = [], []
groups = []

for i in lst:
    if i % 2 == 1:
        odd.append(i)
    else:
        even.append(i)
    if groups and (groups[-1][0] + i) % 2 == 0:
        groups[-1].append(i)
    else:
        groups.append([i])

if odd == sorted(odd) and even == sorted(even):
    print('So Lucky')
else:
    print('Unlucky')

for group in groups:
    group.sort()

flat = []
for group in groups:
    flat.extend(group)

if flat == sorted(flat):
    print('So Lucky')
else:
    print('Unlucky')