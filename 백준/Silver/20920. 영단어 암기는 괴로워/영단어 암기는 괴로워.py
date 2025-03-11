import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
word = []
for _ in range (n):
    word.append(str(sys.stdin.readline().rstrip()))

often_word = {}
for idx, value in enumerate(word):
    if len(value) >= m:
        often_word[value] = 0
    else:
        continue

for i in range (len(word)):
    if word[i] in often_word.keys():
        often_word[word[i]] += 1
res = sorted(often_word.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
# print(res)
for i in range (len(res)):
    print(res[i][0])