import sys
n = int(sys.stdin.readline().rstrip())
tab = list(map(int, sys.stdin.readline().rstrip().split()))
alright_tab = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0
while tab != alright_tab:
    positive = [i for i in range(n) if tab[i] < alright_tab[i]]
    negative = [i for i in range(n) if tab[i] > alright_tab[i]]
    
    if positive:
        start = positive[0]
        end = start
        for i in range(1, len(positive)):
            if positive[i] == positive[i-1] + 1:
                end = positive[i]
            else:
                break
        for i in range(start, end+1):
            tab[i] += 1
        cnt += 1
    
    elif negative:
        start = negative[0]
        end = start
        for i in range(1, len(negative)):
            if negative[i] == negative[i-1] + 1:
                end = negative[i]
            else:
                break
        for i in range(start, end+1):
            tab[i] -= 1
        cnt += 1

print(cnt)