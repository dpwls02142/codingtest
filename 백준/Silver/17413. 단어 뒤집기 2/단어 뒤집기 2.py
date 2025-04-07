import sys
import re
s = sys.stdin.readline().rstrip()
s = re.split(r'(<[^>]*>)', s)
parts = [part for part in s if part]
result = []
for part in parts:
    if part[0] == '<' and part[-1] == '>':
        result.append(part)
    else:
        words = part.split()
        reversed_words = [word[::-1] for word in words]
        result.append(' '.join(reversed_words))
print(''.join(result))