import sys

a = int(sys.stdin.readline().rstrip())
cnt, res = 0, 0
b = sys.stdin.readline().rstrip().split(" ")

while cnt < a:
    num = int(b[cnt])
    
    if num != 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            res += 1
    
    cnt += 1

print(res)