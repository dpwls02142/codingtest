n = int(input())

for i in range (n):
    n = list(input())
    cnt = 0
    res = 0
    for j in n:
        if j == 'O':
            cnt += 1
            res += cnt
        elif j == 'X':
            cnt = 0
    print(res)