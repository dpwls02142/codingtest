import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
words = set()
for _ in range (n):
    word = sys.stdin.readline().rstrip()
    words.add(word)
for i in range (m):
    # temp = set(map(str, sys.stdin.readline().rstrip().split(",")))
    # words = words - temp
    temp = sys.stdin.readline().rstrip().split(",")
    for i in temp:
        if i in words:
            words.remove(i)
    print(len(words))