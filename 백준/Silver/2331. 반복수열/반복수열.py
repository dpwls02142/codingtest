import sys
input = sys.stdin.readline

a, p = map(str, input().split())
between = [str(a)]
res = []
check = True
result = 0
while check:
    temp = 0
    for i in between:
        for j in i:
            temp += pow(int(j), int(p))
    between.append(str(temp))
    if str(temp) in res:
        result = res.index(str(temp))
        check = False
    else:
        res.append(between.pop(0))
print(result)