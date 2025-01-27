n = int(input())
i = 1

while True:
    
    if (1 + (3 * (i * (i-1)))) >= n:
        break
    i += 1

print(i)