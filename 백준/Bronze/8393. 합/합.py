n = int(input())

res = 0

if (1 <= n <= 10000):
    for i in range(1, n+1):
        res += i
        
print(res)