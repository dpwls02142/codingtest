import sys
j = int(sys.stdin.readline().rstrip())
a = int(sys.stdin.readline().rstrip())
cnt = 0
size = {}

def size_to_num(s):
    if s == 'S':
        return 0
    elif s == 'M':
        return 1
    else:  # 'L'
        return 2

for i in range(1, j+1):
    value = sys.stdin.readline().rstrip()
    size[i] = [size_to_num(value)]

for i in range(a):
    want_size, want_num = sys.stdin.readline().rstrip().split()
    want_num = int(want_num)
    want_size_num = size_to_num(want_size)
    
    if want_num in size and want_size_num <= size[want_num][0]:
        del size[want_num]
        cnt += 1

print(cnt)