import sys

n = int(sys.stdin.readline().rstrip())

words = []

for i in range (n):
    a = sys.stdin.readline().rstrip()
    words.append(a)

words = set(words)
words = sorted(words, key = len)
words = sorted(words)
words = sorted(words, key = len)

for i in words:
    print(i)