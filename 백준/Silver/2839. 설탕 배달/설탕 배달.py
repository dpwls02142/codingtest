n = int(input())
cnt = 0

while n >= 0:
    if n % 5 == 0:  # n이 5로 나누어 떨어지면
        cnt += n // 5  # 5로 나눈 몫을 cnt에 더하고
        print(cnt)  # cnt를 출력한 후
        break  # 종료.
    n -= 3  # n이 5로 나누어 떨어지지 않으면, n에서 3을 빼고
    cnt += 1  # cnt를 1 증가
else:  # 3이나 5로 안 나눠지면
    print(-1)  # -1을 출력.