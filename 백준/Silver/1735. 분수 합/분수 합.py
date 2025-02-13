import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
c, d = map(int, sys.stdin.readline().rstrip().split())

nume = a * d + c * b
deno = b * d

x = nume
y = deno
while y:
    x, y = y, x % y  # 유클리드 호제법에선 무조건 x,y를 동시에 업데이트 해야한다.
g = x 

nume //= g
deno //= g

print(nume, deno)