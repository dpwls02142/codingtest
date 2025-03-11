import sys
import math

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
x = list(map(int, sys.stdin.readline().rstrip().split()))

if m == 1:
    # 가로등이 하나인 경우
    print(n)
else:
    height = []
    
    # 시작 지점(0)부터 첫 번째 가로등까지
    height.append(x[0] - 0)
    
    # 마지막 가로등부터 끝 지점(n)까지
    height.append(n - x[-1])
    
    # 각 가로등 사이의 거리
    for i in range(1, len(x)):
        # 두 가로등 사이의 거리의 절반(올림)
        dist = x[i] - x[i-1]
        height.append(math.ceil(dist / 2))
    
    print(max(height))