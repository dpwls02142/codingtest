import sys
a = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().rstrip().split()))
b.sort(reverse=True)

cnt = 1
res = 1

# 가장 많이 등장한 숫자가 어떤건지 구하면 최소 탑의 개수를 알 수 있음.
# 왜? 리스트 안에 포함되어 있는 숫자가 중복 될 경우, 탑에서 재사용 될 수 없음. 
# 따라서 중복된 숫자 중 가장 많이 중복된 횟수가 탑의 최소 개수가 됨.

for i in range (len(b)-1):
    if b[i] == b[i+1]:
        cnt += 1
        res = max(res, cnt)
    else:
        cnt = 1

print(res)