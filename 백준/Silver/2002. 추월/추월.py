import sys
input = sys.stdin.readline
n = int(input().rstrip())
inlet, outlet = [], []
for _ in range (n):
    inlet.append(input().rstrip())
for _ in range (n):
    outlet.append(input().rstrip())
order = {car: idx for idx, car in enumerate(inlet)}
count = 0
for i in range(n):
    for j in range(i+1, n):
        if order[outlet[i]] > order[outlet[j]]:
            count += 1
            break

print(count)