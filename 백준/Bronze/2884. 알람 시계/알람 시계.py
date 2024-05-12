def adjust_alarm(h, m):
    if m < 45:
        h -= 1
        m += 15
        if h < 0:
            h = 23
    else:
        m -= 45
    return h, m

h, m = map(int, input().split())
h, m = adjust_alarm(h, m)
print(h, m)