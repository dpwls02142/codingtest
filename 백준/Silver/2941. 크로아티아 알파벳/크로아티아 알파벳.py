import sys

input_word = sys.stdin.readline().rstrip()
croataia_word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
res, i = 0, 0

while i < len(input_word):
    matched = False
    for x in croataia_word:
        if input_word[i:i+len(x)] == x:
            i += len(x)
            res += 1
            matched = True
            break
    
    if not matched:
        i += 1
        res += 1

print(res)