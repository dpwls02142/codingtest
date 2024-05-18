n, w, l = map(int,input().split())
a = list(map(int,input().split()))

res = [0] * w
t = 0

while res:
    t += 1
    res.pop(0)
    if a:
        if sum(res) + a[0] <= l:
            res.append(a.pop(0))
        else:
            res.append(0)
print(t)