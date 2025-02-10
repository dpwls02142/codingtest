import sys

# 100x100 도화지 (초기값 0)
paper = [[0] * 100 for _ in range(100)]

n = int(sys.stdin.readline().strip())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    
    # x, y에 포함되는 부분을 1로 변경
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

result = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:  # 만약 해당 위치가 1이라면
            result += 1  # 검은 영역 개수를 증가

print(result)