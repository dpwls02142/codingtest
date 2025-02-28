import sys

n = int(sys.stdin.readline().rstrip())
channel = []
for _ in range (n):
    channel.append(sys.stdin.readline().rstrip())

kbs1 = channel.index("KBS1")
kbs2 = channel.index("KBS2")

if kbs1 > kbs2:
    kbs2 += 1

print("1" * kbs1 + "4" * kbs1 + "1" * kbs2 + "4" * (int(kbs2)-1))