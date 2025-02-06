import sys
# 입력값이 55-50+40이라 했을 때, 더하기를 먼저하고(50+40) 뺄셈을 해야(55-90) 최소값(-35)이 나오니,
# 일단 -를 기준으로 입력값을 분리하고,
a = list(sys.stdin.readline().rstrip().split('-'))
res = []

# res에다가 더하기 한 값을 저장하고,
for i in a:
    sum = 0
    b = i.split('+')
    for j in b:
        sum += int(j)
    res.append(sum)
    
# 처음은 무조건 숫자로 시작하니, res[0]부터 res[i]까지 뺀 값을 누적
b = res[0]
for i in range (1, len(res)):
    b -= res[i]

print(b)