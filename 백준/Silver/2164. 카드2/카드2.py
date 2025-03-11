import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
if n == 1:
    print(1)
else:
    card = [x for x in range (1, n+1)]
    card = deque(card)

    while card:
        temp = card.popleft()
        card.append(card.popleft())
        if len(card) == 1:
            break
    print(card[0])