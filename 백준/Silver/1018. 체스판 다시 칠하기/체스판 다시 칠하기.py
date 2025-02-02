import sys

n, m = map(int, sys.stdin.readline().split())
a, b = [], []
min_cnt = float('inf') # 다시 칠해야 되는 횟수가 적어야 하기 때문에 infinity한 수로 초기화

for i in range (n):
    for j in range (1):
        a = list(sys.stdin.readline().rstrip())
    b.append(a)

for x in range(n - 7): # 8*8 크기로 어디서든 자를 수 있어야 되기에 -7
    for y in range(m - 7):
        # cnt1은 흰색이 처음일때, cnt2는 검정색이 처음일 때 
        cnt1, cnt2 = 0, 0 

        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    # 'W'로 시작하는 체스판일 때
                    if b[x + i][y + j] != 'W': # 짝수칸이 'W'가 아니라면
                        cnt1 += 1 
                    # 'B'로 시작하는 체스판일 때
                    if b[x + i][y + j] != 'B': # 짝수칸이 'B'가 아니라면
                        cnt2 += 1
                else:
                    # 'W'로 시작하는 체스판일 때
                    if b[x + i][y + j] != 'B':  # 홀수칸이 'B'가 아니라면
                        cnt1 += 1
                    # 'B'로 시작하는 체스판일 때
                    if b[x + i][y + j] != 'W':  # 홀수칸이 'W'가 아니라면
                        cnt2 += 1

        if cnt1 < min_cnt:
            min_cnt = cnt1
        if cnt2 < min_cnt:
            min_cnt = cnt2

print(min_cnt)