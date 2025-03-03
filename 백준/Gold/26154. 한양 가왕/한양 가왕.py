N, M = map(int, input().split())

machines = []
for _ in range(N):
    p1, p2 = map(int, input().split())
    machines.append([p1, p2, 0])

moveCnt = M if M <= N else N + (M % N)

for _ in range(moveCnt):
    firstMoveIdx = 0
    moveIdx = 2

    if machines[0][0] > machines[0][1]:
        firstMoveIdx = 1

    for i in range(1, N):
        if machines[i][0] > machines[i][1]:
            machines[i-1][moveIdx] = machines[i][0]
            moveIdx = 0
        else:
            machines[i-1][moveIdx] = machines[i][1]
            moveIdx = 1

    machines[N-1][moveIdx] = machines[0][firstMoveIdx]
    machines[0][firstMoveIdx] = machines[0][2]

for i in range(N):
    print(min(machines[i][0], machines[i][1]), max(machines[i][0], machines[i][1]))