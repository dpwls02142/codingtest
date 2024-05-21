# n = 바구니 개수
# m = 공을 바꾸는 횟수
# m번 공을 바꾼 이후에 각 바구니에 어떤 공이 들어있는지
# 반복문을 m만큼 돌고 i번 바구니와 j번 바구니에 들어있는 공을 교환.

n, m = map(int, input().split())
array = list(range(n+1))

for i in range (m):
    i, j = map(int, input().split())
    array[i], array[j] = array[j], array[i]

print(*array[1:]) # 개별적으로 출력되기 위해서 *으로 언패킹