import sys

n = int(sys.stdin.readline().rstrip())
switch = list(map(int, sys.stdin.readline().rstrip().split()))
student = int(sys.stdin.readline().rstrip())

for _ in range(student):
    gender, give = map(int, sys.stdin.readline().rstrip().split())

    if gender == 1:
        for i in range(give - 1, n, give):
            switch[i] = 1 - switch[i]

    elif gender == 2:
        give -= 1
        switch[give] = 1 - switch[give]

        left, right = give - 1, give + 1
        while left >= 0 and right < n and switch[left] == switch[right]:
            switch[left] = 1 - switch[left]
            switch[right] = 1 - switch[right]
            left -= 1
            right += 1

for i in range(0, n, 20):
    print(" ".join(map(str, switch[i:i+20])))

# 1일때는 0으로 만들고 0일땐 1로 만들어야하니 value에 -1을 하면 됨. -> value가 0일땐 1-0=1, value가 1일땐 1-1=0.