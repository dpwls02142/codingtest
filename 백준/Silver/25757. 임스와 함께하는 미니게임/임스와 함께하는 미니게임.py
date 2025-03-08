import sys
n, t = map(str, sys.stdin.readline().rstrip().split())

game_type = {"Y": 1, "F": 2, "O": 3}
step = game_type[t]

user = []
for _ in range (int(n)):
    user.append(sys.stdin.readline().rstrip())
user = set(user)

res = len(user) // step
print(res)