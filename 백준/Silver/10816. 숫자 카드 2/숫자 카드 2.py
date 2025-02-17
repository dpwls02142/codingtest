import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().rstrip().split()))

# a를 딕셔너리로 만들어서
# key엔 a의 value값을 넣고, value엔 key가 몇 번 등장했는지를 cnt.
# == a에 있는 숫자가 각각 몇 번 등장했는지 셈.
cnt = {}
for i in a:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

# b값에 맞는 cnt의 key값을 갖고와서,
# cnt의 key값에 value가 없으면 0을, 
# 있으면 value값을 반환.
for j in b:
    res = cnt.get(j)
    if res == None:
        print(0, end=' ')
    else:
        print(res, end=' ')