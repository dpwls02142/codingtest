import sys
n = int(sys.stdin.readline().rstrip())
schedule = []
for i in range (n):
    schedule.append(list(map(int, sys.stdin.readline().rstrip().split())))
dp = [0] * (n + 1)
for i in range(n - 1, -1, -1): #  4, 3, 2, 1, 0
    time = schedule[i][0] # 2
    profit = schedule[i][1] # 15
    if i + time <= n: # 4 + 2 <= 7
        dp[i] = max((profit + dp[i + time]), dp[i + 1]) # 15, 
    else:
        dp[i] = dp[i + 1] # dp[5] = dp[6]
print(dp[0])

# 일을 안 했을 때도 고려해야됨
# max_profit = []
# for start in range(n):
#     total_profit = 0
#     day = start # 0

#     while day < n:
#         time = schedule[day][0]
#         profit = schedule[day][1]
#         if day + time <= n:
#             total_profit += profit
#             day += time
#         else:
#             break

#     max_profit.append(total_profit)

# print(max(max_profit))