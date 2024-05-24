n, k = map(int,input().split())
res = []
cnt = 0

for i in range (n):
    a = int(input())
    res.append(a)
res.sort(reverse=True)

for j in res:
    if k >= j:
        cnt += k // j
        k %= j
        if k <= 0:
            break

print(cnt)