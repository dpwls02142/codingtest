t = int(input())

results = []

for _ in range(t):
    a, b = map(int, input().split())
    last_digit = pow(a, b, 10)
    
    if last_digit == 0:
        last_digit = 10
    
    results.append(last_digit)

for result in results:
    print(result)
