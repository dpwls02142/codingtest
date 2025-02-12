# n개의 언덕으로 이뤄진 농장에서 
# 각 언덕의 높이가 0~100 사이의 정수값을 가짐.
# 이 때 가장 높은 언덕과 가장 낮은 언덕의 차가 17보다 커야됨.

import sys

n = int(sys.stdin.readline().rstrip())

hills = []

for i in range (n):
    a = int(sys.stdin.readline().rstrip())
    hills.append(a)

min_cost = float('inf')

for i in range(84):  # 최대값이 100이므로 low는 83까지 가능
    high = i + 17
    cost = 0

    for h in hills:
        if h < i:  # 너무 낮으면 올려야 함
            cost += (i - h) ** 2
        elif h > high:  # 너무 높으면 낮춰야 함
            cost += (h - high) ** 2

    min_cost = min(min_cost, cost)

print(min_cost)