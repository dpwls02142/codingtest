import sys
n = int(sys.stdin.readline().rstrip())
a = []
for i in range (n):
    a.append(list(map(int, sys.stdin.readline().rstrip().split())))

rank = [1] * n
for i in range(n):
    for j in range(n):
        if i != j:
            # (키, 몸무게) 모두 비교 대상보다 작다면 등수를 증가
            if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
                rank[i] += 1
print(" ".join(map(str, rank)))