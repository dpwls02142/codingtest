import sys
t = int(sys.stdin.readline().rstrip())
for _ in range (t):
    clot = int(sys.stdin.readline().rstrip())
    cloths = {}
    for _ in range (clot):
        name, cate = map(str, sys.stdin.readline().rstrip().split())
        if cate in cloths:
            cloths[cate] += 1
        else:
            cloths[cate] = 1
    # print(cloths)
    res = 1
    for i in cloths.values():
        res *= (i + 1)
    print(res - 1)