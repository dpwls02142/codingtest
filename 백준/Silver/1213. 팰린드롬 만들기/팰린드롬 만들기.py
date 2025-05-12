import sys
from collections import Counter
input = sys.stdin.readline
s = input().strip()
counter = Counter(s)

odds = [value for value, count in counter.items() if count % 2 == 1]
if len(odds) > 1:
    print("I'm Sorry Hansoo")
else:
    result = ""
    for value in sorted(counter.keys()):
        result += value * (counter[value] // 2)
    middle = ""
    if odds:
        middle = odds[0]
    palindrome = result + middle + result[::-1]
    print(palindrome)