import sys
input = sys.stdin.readline

s = input().rstrip()
    
s += s
total_a = s.count('a') // 2

min_swaps = float('inf')
count_a = 0

for i in range(len(s)):
    if i >= total_a:
        if s[i - total_a] == 'a':
            count_a -= 1
    if s[i] == 'a':
        count_a += 1
    if i >= total_a - 1:
        min_swaps = min(min_swaps, total_a - count_a)

print(min_swaps)