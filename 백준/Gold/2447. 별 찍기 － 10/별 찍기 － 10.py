import sys
input = sys.stdin.readline

n = int(input())
arr = [[' ' for _ in range (n)] for _ in range (n)]

def draw(arr, x, y, n):
    if n == 1:
        arr[x][y] = '*'
        return
    size = n // 3
    for i in range (3):
        for j in range (3):
            if i == 1 and j == 1:
                continue
            draw(arr, x+i*size, y+j*size, size)

draw(arr, 0, 0, n)
for i in arr:
    print(''.join(i))