import sys
n = int(sys.stdin.readline().rstrip())
res_year = 2024
res_month = 1
for i in range (n):
    res_month += 7
    if res_month > 12:
        res_month -= 12
        res_year += 1
print(res_year, res_month)