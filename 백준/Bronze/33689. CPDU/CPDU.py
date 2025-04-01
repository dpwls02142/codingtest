import sys
n = int(sys.stdin.readline().rstrip())
lst = []
cnt = 0 
for _ in range (n):
    lst.append(sys.stdin.readline().rstrip())
for i in lst:
    if i[0] == "C":
        cnt += 1
print(cnt)