import sys
#  +/- 10까지 가능
# m: 방 정원
p, m = map(int, sys.stdin.readline().rstrip().split())
rooms = [] 

for _ in range(p):
    l, n = map(str, sys.stdin.readline().rstrip().split())
    l = int(l)
    found = False
    for room in rooms:
        if len(room) < m and room[0][0] - 10 <= l <= room[0][0] + 10:
            room.append((l, n))
            found = True
            break
    if not found:
        rooms.append([(l, n)])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    for player in sorted(room, key=lambda x: x[1]):
        print(*player)