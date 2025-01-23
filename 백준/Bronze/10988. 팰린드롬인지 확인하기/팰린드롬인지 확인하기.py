a = list(input())
b = a[::-1]
a = ''.join(a)
b = ''.join(b)
res = 0

if a == b:
    res = 1
else:
    res = 0

print(res)