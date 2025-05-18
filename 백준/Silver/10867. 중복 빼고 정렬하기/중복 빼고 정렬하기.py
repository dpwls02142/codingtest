import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().rstrip().split()))
lst_sort = sorted(set(lst))
print(' '.join(map(str, lst_sort)))