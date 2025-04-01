import sys
n = int(sys.stdin.readline().rstrip())
cnt = 1
i = 1
while i < 1000000000:
    for j in range(1, 10):
        if i * j <= n:
            cnt += 1
    i = i * 10 + 1 
print(cnt)