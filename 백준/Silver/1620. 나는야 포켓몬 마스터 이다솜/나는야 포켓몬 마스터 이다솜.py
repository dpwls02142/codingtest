import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
pocket_num_to_name, pocket_name_to_num = {}, {}
for i in range (1, n + 1):
    name = input().rstrip()
    pocket_name_to_num[name] = i
    pocket_num_to_name[i] = name
for _ in range (m):
    find = input().rstrip()
    if find.isnumeric():
        find2 = int(find)
        print(pocket_num_to_name[find2])
    else:
        print(pocket_name_to_num[find])