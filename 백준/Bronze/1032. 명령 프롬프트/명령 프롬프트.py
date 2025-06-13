import sys
input = sys.stdin.readline
# a?b.exe 첫번째 글자 a 세번째 글자 b
s = int(input().rstrip())
lst = [input().rstrip() for _ in range (s)]
temp = list(lst[0])
for i in range (1, s):
    for j in range (len(temp)):
        if temp[j] != lst[i][j]:
            temp[j] = "?"
print(''.join(temp))