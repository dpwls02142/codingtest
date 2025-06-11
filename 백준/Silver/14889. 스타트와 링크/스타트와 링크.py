import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input().rstrip())
lst = [list(map(int, input().rstrip().split())) for _ in range (n)]

def find(team):
    total = 0
    for i in range (len(team)):
        for j in range(i+1, len(team)):
            total += lst[team[i]][team[j]] + lst[team[j]][team[i]]
    return total

res = float('inf')
for start in combinations(range(n), n // 2):
    link = list(set(range(n)) - set(start))
    start_sum = find(start)
    link_sum = find(link)
    # print(start_sum, link_sum)
    res = min(res, abs(start_sum - link_sum))
    if res == 0:
        break

print(res)
