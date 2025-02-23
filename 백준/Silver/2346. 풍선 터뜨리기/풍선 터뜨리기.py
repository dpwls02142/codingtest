import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
balloon = deque(range(1, n+1))
pball = list(map(int, sys.stdin.readline().rstrip().split()))

res = []

while balloon:
    res.append(balloon.popleft()) # 첫번째 풍선을 터뜨림. queue는 FIFO.
    
    if not balloon:
        break

    # 가장 마지막에 터뜨린 풍선 번호를 res에서 구하고,
    # 인덱스가 0부터 시작하니 그 값에 -1.
    move = pball[res[-1] - 1]

    if move > 0: # 양수면 오른쪽으로 이동
        balloon.rotate(-(move - 1))
    else: # 음수면 왼쪽으로 이동
        balloon.rotate(-move)

print(' '.join(map(str, res)))