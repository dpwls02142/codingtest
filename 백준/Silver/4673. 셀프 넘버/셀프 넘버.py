result = set()
for i in range (1, 10001):
    res = i
    while i > 0:
        res += i % 10
        i //= 10
    if res <= 10000:
        result.add(res)
for i in range (1, 10001):
    if i not in result:
        print(i)