import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

res = str(a * b * c)

for i in range (0, 10):
    print(res.count(str(i)))