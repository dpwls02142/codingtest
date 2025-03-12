import sys
# 최대값을 가진 기간이 몇 개 있는지를 출력.
n, x = map(int, sys.stdin.readline().rstrip().split())
today_visit = list(map(int, sys.stdin.readline().rstrip().split()))

window_sum = sum(today_visit[:x])
max_sum = window_sum
count = 1

for i in range(x, n):
    window_sum += today_visit[i] - today_visit[i - x]
    if window_sum > max_sum:
        max_sum = window_sum
        count = 1
    elif window_sum == max_sum:
        count += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)