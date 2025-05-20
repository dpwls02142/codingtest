# 에라토스테네스의 체는 소수를 빠르게 찾을 때 용이함
# 왜? 작은 소수부터 그에 해당하는 배수를 지워나가니까
# 소수가 아닌 것들은 계속 지워짐
# 그렇기에 반복문도 순차적으로 돌려도 상관 없는거 
import sys
input = sys.stdin.readline
n, k = map(int, input().rstrip().split())
lst = [0 for _ in range (n+1)]
cnt = 0
for i in range (2, n + 1):
    if lst[i] == 0:
        for j in range (i, n + 1, i):
            if lst[j] == 0:
                lst[j] = 1
                cnt += 1
                if cnt == k:
                    print(j)
                    sys.exit(0)