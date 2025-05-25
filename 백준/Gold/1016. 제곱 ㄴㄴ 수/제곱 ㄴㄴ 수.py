import sys
input = sys.stdin.readline
minRange, maxRange = map(int, input().rstrip().split())
length = maxRange - minRange + 1
isSquare = [1] * length
i = 2
while i * i <= maxRange:
    square = i * i
    start = ((minRange + square - 1) // square) * square
    for j in range (start, maxRange + 1, square):
        isSquare[j - minRange] = 0
    i += 1
print(sum(isSquare))