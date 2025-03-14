import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
words = []
for _ in range (n):
    words.append(sys.stdin.readline().rstrip())

a = words[0]
a_counter = Counter(a)
cnt = 0

for word in words[1:]:
    word_counter = Counter(word)
    if a_counter == word_counter:
        cnt += 1
    elif len(a) == len(word):
        diff_count = sum((a_counter - word_counter).values()) + sum((word_counter - a_counter).values())
        if diff_count == 2:
            cnt += 1
    elif abs(len(a) - len(word)) == 1:
        diff_count = sum((a_counter - word_counter).values()) + sum((word_counter - a_counter).values())
        if diff_count == 1:
            cnt += 1

print(cnt)