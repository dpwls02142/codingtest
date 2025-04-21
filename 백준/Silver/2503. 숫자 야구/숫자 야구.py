import sys
input = sys.stdin.readline
n = int(input())
temp = []
for _ in range (n):
    ask, strike, ball = map(int, input().split())
    temp.append((str(ask), strike, ball))
p_ans = []
for i in range (1, 10):
    for j in range (1, 10):
        if i == j:
            continue
        for k in range (1, 10):
            if k == i or k == j:
                continue
            p_ans.append(str(i*100 + j*10 + k))
for ask, s, b in temp:
    filter_res = []
    for answer in p_ans:
        current_s, current_b = 0, 0
        for i in range(3):
            if ask[i] == answer[i]:
                current_s += 1
        for i in range(3):
            for j in range(3):
                if i != j and ask[i] == answer[j]:
                    current_b += 1
        if current_s == s and current_b == b:
            filter_res.append(answer)
    p_ans = filter_res
print(len(p_ans))