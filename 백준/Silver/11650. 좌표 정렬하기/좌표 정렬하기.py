import sys
n = int(sys.stdin.readline().rstrip())
b = []
res = []

for i in range(n):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    b.append(a)

# x좌표 기준으로, x좌표가 같으면 y좌표 기준으로 정렬
b.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print(b[i][0], b[i][1])