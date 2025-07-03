import sys
input = sys.stdin.readline

t = int(input().rstrip())
for i in range (t):
    a, n = map(int, input().rstrip().split())
    res = ""
    while a:
        temp = a % n
        if temp < 10:
            res += str(temp)
        else:
            res += chr(ord('a') + temp - 10) 
        a //= n
    res2 = res[::-1]
    if res == res2:
        print(1)
    else:
        print(0)