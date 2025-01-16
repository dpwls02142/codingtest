import sys

t = int(input())

if t <= 1000000:
    for i in range(t):
        a = sys.stdin.readline().rstrip()

        numbers = a.split()

        c = int(numbers[0])
        d = int(numbers[1])

        if 1 <= c <= 1000 and 1 <= d <= 1000:
            print(c + d)