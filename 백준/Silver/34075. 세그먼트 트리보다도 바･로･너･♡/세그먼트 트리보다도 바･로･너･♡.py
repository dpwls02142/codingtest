import sys
input = sys.stdin.readline

n = int(input())
algorithm = []
for _ in range (n):
    a, b = map(str, input().rstrip().split())
    algorithm.append((a, int(b)))
m = int(input())
members = {}
for _ in range (m):
    c, d = map(str, input().rstrip().split())
    members[c] = int(d)

preferences = {}
for member, tier in members.items():
    sorted_algos = sorted(algorithm, key=lambda x: (abs(x[1] - tier), x[0]))
    preferences[member] = [algo[0] for algo in sorted_algos]
# print(preferences)
current_member = None
q = int(input())
for _ in range(q):
    query = input().strip()
    if query.endswith("- chan!"):
        name = query.split(" - ")[0]
        current_member = name
        print("hai!")
    else:
        top2 = preferences[current_member][:2]
        print(f"{top2[1]} yori mo {top2[0]}")