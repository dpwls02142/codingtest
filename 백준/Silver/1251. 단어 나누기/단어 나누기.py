import sys
input = sys.stdin.readline
s = input().rstrip()
n = len(s)
best_res = ""
for i in range (1, n):
    for j in range (i + 1, n):
        first = s[:i]
        second = s[i:j]
        third = s[j:]

        reversed_f, reversed_s, reversed_t = first[::-1], second[::-1], third[::-1]

        res = reversed_f + reversed_s + reversed_t

        if best_res == "" or best_res > res:
            best_res = res
print(best_res)