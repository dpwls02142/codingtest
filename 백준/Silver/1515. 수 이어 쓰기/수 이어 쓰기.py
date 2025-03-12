import sys
remove = sys.stdin.readline().rstrip()
if remove[0] == 1:
    print(remove[-1])
else:
    n = 0
    idx = 0
    temp = True
    while temp:
        n += 1
        for i in str(n):
            if remove[idx] == i:
                idx += 1
                if idx >= len(remove):
                    print(n)
                    temp = False
                    break
        if temp == False:
            break