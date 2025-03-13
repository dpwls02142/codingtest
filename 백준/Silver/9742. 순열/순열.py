import sys
from itertools import permutations

while True:
    try:
        p, find = map(str, sys.stdin.readline().rstrip().split())
        find = int(find)

        res = permutations(p, len(p))
        for i, perm in enumerate(res , 1):
            if i == find:
                print(f'{p} {find} = {"".join(perm)}')
                break
            if i > find:
                break
        else:
            print(f'{p} {find} = No permutation')

    except ValueError:
        break